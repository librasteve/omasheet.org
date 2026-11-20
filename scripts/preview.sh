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

(cd "$SRC" && ruby scripts/escape_liquid.rb \
  external/omasheet/README.md \
  external/omasheet/docs/format.md \
  external/omasheet/docs/expressions.md \
  external/omasheet/docs/app.md \
  external/omasheet/docs/interop.md >/dev/null)

cd "$ROOT"
bundle exec jekyll build -s "$SRC" -d "$OUT"
echo "Built to $OUT"
