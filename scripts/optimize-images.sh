#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ASSETS="$ROOT/assets"
CWEBP="$(command -v cwebp)"

if [[ -z "$CWEBP" ]]; then
  echo "cwebp is required. Install with: brew install webp"
  exit 1
fi

resize() {
  local file="$1"
  local max="$2"
  [[ -f "$file" ]] || return 0
  local width
  width="$(sips -g pixelWidth "$file" 2>/dev/null | awk '/pixelWidth/ {print $2}')"
  if [[ -n "$width" && "$width" -gt "$max" ]]; then
    sips -Z "$max" "$file" >/dev/null
  fi
}

to_webp() {
  local file="$1"
  local quality="${2:-82}"
  [[ -f "$file" ]] || return 0
  "$CWEBP" -quiet -q "$quality" "$file" -o "${file%.png}.webp"
}

echo "Removing unused reference assets..."
rm -f \
  "$ASSETS/unik.png" \
  "$ASSETS/automobile-collection-reference.png" \
  "$ASSETS/changan-slider-reference.png" \
  "$ASSETS"/Screenshot_*.png \
  "$ASSETS"/Konga_Mikano_SIS-*.png \
  "$ASSETS/.DS_Store"

echo "Resizing category and collection images (800px)..."
for name in executivesuv commercial leisure residential enterprise industrial; do
  resize "$ASSETS/${name}.png" 800
done

echo "Resizing hub backgrounds (1200px)..."
resize "$ASSETS/motorbg.png" 1200

echo "Resizing vehicle showcase images (1200px)..."
for name in changancar deepalcar maxuscar; do
  resize "$ASSETS/${name}.png" 1200
done

echo "Resizing hero banner (1400px)..."
resize "$ASSETS/eado.png" 1400

echo "Resizing logos (320px)..."
for name in changanlogo deepallogo maxuslogo mikano-logo; do
  resize "$ASSETS/${name}.png" 320
done

echo "Resizing brand model images (560px)..."
while IFS= read -r -d '' file; do
  resize "$file" 560
done < <(find "$ASSETS/brands" -name '*.png' -print0)

echo "Generating WebP variants..."
while IFS= read -r -d '' file; do
  to_webp "$file" 82
done < <(find "$ASSETS" -name '*.png' -not -path '*/.DS_Store' -print0)

echo "Done. Asset size:"
du -sh "$ASSETS"
