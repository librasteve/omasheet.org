#!/usr/bin/env bash
# Build the site locally for preview without modifying external/omasheet.
# Usage: scripts/preview.sh [output-dir]   (default: _site)
# Copies the source to a temp dir, applies escape_liquid.rb there (as the
# Pages workflow does), then runs jekyll against the copy.
set -euo pipefail

# The default Homebrew Ruby lacks the bundled gems; 3.1 has them.
export PATH=/opt/homebrew/opt/ruby@3.1/bin:$PATH

ROOT=$(cd "$(dirname "$0")/.." && pwd)
OUT=$(cd "$(dirname "${1:-$ROOT/_site}")" && pwd)/$(basename "${1:-$ROOT/_site}")
SRC=$(cd "$(mktemp -d)" && pwd -P)
trap 'rm -rf "$SRC"' EXIT

rsync -a --exclude .git --exclude _site --exclude vendor/bundle --exclude .bundle "$ROOT/" "$SRC/"

# To preview docs that are not on omasheet main yet, point at a checkout:
#   OMASHEET_REPO=../omasheet scripts/preview.sh
if [ -n "${OMASHEET_REPO:-}" ]; then
  rsync -a --delete "$OMASHEET_REPO/docs/" "$SRC/external/omasheet/docs/"
  cp "$OMASHEET_REPO/README.md" "$SRC/external/omasheet/README.md"
fi

# Only escape the docs that exist in this checkout (the submodule may lag behind).
(cd "$SRC" && files=""; for f in README.md docs/format.md docs/expressions.md docs/app.md docs/interop.md; do
  [ -f "external/omasheet/$f" ] && files="$files external/omasheet/$f"; done
  ruby scripts/escape_liquid.rb $files >/dev/null)

cd "$ROOT"
bundle exec jekyll build -s "$SRC" -d "$OUT"
echo "Built to $OUT"
