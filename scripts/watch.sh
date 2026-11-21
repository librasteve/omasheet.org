#!/usr/bin/env bash
# Rebuild the preview whenever the guide, layouts, styles or omasheet docs
# change, then reload the Chrome tab showing it.
# Usage: scripts/watch.sh          (stop with Ctrl+C)
set -uo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
cd "$ROOT"
export OMASHEET_REPO=${OMASHEET_REPO:-../omasheet}
WATCH=(guide.md getting-started.md index.html positioning.md _layouts _includes _pages _data assets/css "$OMASHEET_REPO/docs")

stamp() { find "${WATCH[@]}" -type f -exec stat -f '%m' {} + 2>/dev/null | sort -n | tail -1; }

last=""
while true; do
  now=$(stamp)
  if [ "$now" != "$last" ]; then
    last=$now
    if scripts/preview.sh >/tmp/omasheet-watch.log 2>&1; then
      echo "$(date +%T) rebuilt"
      osascript -e 'tell application "Google Chrome" to repeat with w in windows
repeat with t in tabs of w
if URL of t contains "localhost:8766" then reload t
end repeat
end repeat' >/dev/null 2>&1
    else
      echo "$(date +%T) build failed:"; grep -iE 'error' /tmp/omasheet-watch.log | head -5
    fi
  fi
  sleep 2
done
