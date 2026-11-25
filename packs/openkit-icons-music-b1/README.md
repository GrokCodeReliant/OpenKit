# openkit-icons-music-b1

Eight music / instrument icons (256×256 RGBA PNG + editable SVG) for inventory, bard kits, shops, and UI. Generic archetypes only.

## Contents

| Icon | Function |
|------|----------|
| `icon-music-bagpipes` | Bag with drones, blowpipe, and chanter |
| `icon-music-bell` | Hanging bell with clapper |
| `icon-music-drum` | Drum with crossed sticks |
| `icon-music-fiddle` | Waisted violin-body fiddle with separate bow |
| `icon-music-flute` | Diagonal transverse flute with finger holes |
| `icon-music-harp` | Frame harp with thick strings |
| `icon-music-horn` | Curved/looped hunting horn with continuous tube and flared bell |
| `icon-music-lute` | Pear/teardrop lute with connected neck, bridge, and pegbox |

## Display size (honest)

Masters are **256×256 export resolution**, not native UI scale. Typical inventory/UI display is often **32–64px**. Recommended minimum on-screen size for reliable recognition of all eight: **48px**. At 32px silhouettes mostly hold; thinner elements (flute holes, harp strings, fiddle bow, horn loop hole) become marginal. Opaque-pixel coverage alone does not certify recognition.

These are inventory / UI icons, not world-ground sprites. Align to the visual center of the untrimmed 256×256 canvas. This is not an engine ground-plane pivot.

## Usage

Drop PNGs into a UI atlas or load SVGs directly. No runtime code or fonts required.

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA transparent PNG for each item
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `MANIFEST.json` — per-file SHA256 + sizes

No scripts, fonts, or external references in shipping SVG.
