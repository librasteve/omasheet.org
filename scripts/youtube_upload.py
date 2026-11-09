#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "google-api-python-client",
#   "google-auth-oauthlib",
# ]
# ///
"""Upload a video to YouTube via the Data API v3 (resumable upload).

One-time setup:
  1. https://console.cloud.google.com -> create a project, enable "YouTube Data API v3".
  2. APIs & Services -> OAuth consent screen: External, add yourself as a test user.
  3. Credentials -> Create credentials -> OAuth client ID -> "Desktop app".
     Download the JSON and save it as ~/.config/omasheet-youtube/client_secret.json
     (outside the repo on purpose; the repo is public).
  4. First run opens a browser: pick the Google account and, when asked, the
     librasteve channel. The token is cached in ~/.config/omasheet-youtube/youtube_token.json.

Usage:
  scripts/youtube_upload.py "videos/bank-report/Screen Recording ....mov" \
      --title "Omasheet: bank transactions report" \
      --description-file videos/bank-report/description.txt \
      --playlist Omasheet --privacy unlisted

Notes:
  * Unverified API projects force uploads to private; verify the project or
    flip visibility to unlisted/public in Studio afterwards.
  * The API quota is ~6 uploads/day on the default allocation.
"""

import argparse
import os
import sys
import time
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Secrets live outside the (public) repo. Override with YOUTUBE_UPLOAD_CONFIG_DIR.
CONFIG_DIR = Path(os.environ.get("YOUTUBE_UPLOAD_CONFIG_DIR", "~/.config/omasheet-youtube")).expanduser()
CLIENT_SECRET = CONFIG_DIR / "client_secret.json"
TOKEN = CONFIG_DIR / "youtube_token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube"]


def get_service():
    creds = None
    if TOKEN.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CLIENT_SECRET.exists():
                sys.exit(f"Missing {CLIENT_SECRET} - see setup notes in this script's docstring.")
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)
        CONFIG_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)
        TOKEN.write_text(creds.to_json())
        TOKEN.chmod(0o600)
    return build("youtube", "v3", credentials=creds)


def with_retry(request, tries=5):
    """Execute an API request, retrying transient 409/5xx errors with backoff."""
    for attempt in range(tries):
        try:
            return request.execute()
        except HttpError as e:
            if e.resp.status not in (409, 500, 502, 503, 504) or attempt == tries - 1:
                raise
            wait = 2 ** (attempt + 1)
            print(f"Transient error {e.resp.status}, retrying in {wait}s...")
            time.sleep(wait)


def add_to_playlist(yt, video_id, name, privacy):
    pid = find_or_create_playlist(yt, name, privacy)
    body = {"snippet": {"playlistId": pid, "resourceId": {"kind": "youtube#video", "videoId": video_id}}}
    with_retry(yt.playlistItems().insert(part="snippet", body=body))
    print(f"Added to playlist '{name}'.")


def find_or_create_playlist(yt, name, privacy):
    req = yt.playlists().list(part="snippet", mine=True, maxResults=50)
    while req:
        resp = req.execute()
        for item in resp["items"]:
            if item["snippet"]["title"] == name:
                return item["id"]
        req = yt.playlists().list_next(req, resp)
    body = {"snippet": {"title": name}, "status": {"privacyStatus": privacy}}
    return with_retry(yt.playlists().insert(part="snippet,status", body=body))["id"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video", type=Path, nargs="?", help="video file to upload")
    p.add_argument("--video-id", help="skip the upload; act on an already-uploaded video (e.g. add to playlist)")
    p.add_argument("--title")
    p.add_argument("--description", default="")
    p.add_argument("--description-file", type=Path)
    p.add_argument("--tags", default="omasheet,spreadsheet,markdown", help="comma separated")
    p.add_argument("--privacy", choices=["private", "unlisted", "public"], default="unlisted")
    p.add_argument("--playlist", help="playlist name (created if missing)")
    p.add_argument("--category", default="28", help="YouTube category id (28 = Science & Technology)")
    p.add_argument("--thumbnail", type=Path, help="optional custom thumbnail image")
    args = p.parse_args()

    if args.video_id:
        yt = get_service()
        if args.playlist:
            add_to_playlist(yt, args.video_id, args.playlist, args.privacy)
        return
    if not args.video or not args.title:
        p.error("video and --title are required unless --video-id is given")
    if not args.video.is_file():
        sys.exit(f"No such file: {args.video}")
    description = args.description_file.read_text() if args.description_file else args.description

    yt = get_service()
    body = {
        "snippet": {
            "title": args.title,
            "description": description,
            "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
            "categoryId": args.category,
        },
        "status": {"privacyStatus": args.privacy, "selfDeclaredMadeForKids": False},
    }
    media = MediaFileUpload(str(args.video), chunksize=16 * 1024 * 1024, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)

    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"\rUploading... {int(status.progress() * 100)}%", end="", flush=True)
    video_id = resp["id"]
    print(f"\nUploaded: https://youtu.be/{video_id}")

    if args.thumbnail:
        yt.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(str(args.thumbnail))).execute()
        print("Thumbnail set.")

    if args.playlist:
        add_to_playlist(yt, video_id, args.playlist, args.privacy)


if __name__ == "__main__":
    main()
