# openkit-icons-map-poi-b1

Eight map point-of-interest / settlement icons (256×256 RGBA PNG + editable SVG) for minimaps, journals, and world markers. Generic archetypes only.

## Contents

| Icon | Function |
|------|----------|
| `icon-poi-dungeon` | Stone arch entrance |
| `icon-poi-forge` | Horned anvil and hammer |
| `icon-poi-harbor` | Connected anchor |
| `icon-poi-inn` | Timber inn with tankard sign |
| `icon-poi-keep` | Battlement tower |
| `icon-poi-market` | Striped awning stall |
| `icon-poi-mine` | Crossed pickaxes over ore |
| `icon-poi-shrine` | Pedestal with flame |

## Display size (honest)

PNG/SVG masters are authored at **256×256 export resolution**, not native UI scale. Typical POI / minimap display is often **32–64px**. Recommended minimum on-screen size for reliable recognition of all eight: **48px**. At 32px silhouettes mostly hold, but fine details (pick tips, anchor flukes, anvil horn) become marginal.

These are inventory / map UI icons, not world-ground sprites. Align to the visual center of the untrimmed 256×256 canvas. This is not an engine ground-plane pivot.

## Usage

Drop PNGs into a UI atlas or load SVGs directly. No runtime code or fonts required. Consistent thick dark outline style.

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA transparent PNG for each item
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `MANIFEST.json` — per-file SHA256 + sizes

No scripts, fonts, or external references in shipping SVG.
