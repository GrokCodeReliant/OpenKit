# Open Kit — Dungeon Keep & Dungeoneering Icons (20261125 wave 1)

Eight inventory icons for keep architecture and climbing or loot silhouettes: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`.

## Contents

| Icon | Function |
|------|----------|
| `icon-dungeon-portcullis` | Closed iron portcullis in a short stone arch |
| `icon-dungeon-arrow-slit` | Stone wall face with a tall narrow arrow slit |
| `icon-dungeon-cresset` | Standing iron fire-basket on a post |
| `icon-dungeon-manacles` | Empty open iron cuffs linked by a short chain |
| `icon-dungeon-key-ring` | Split iron ring with four different antique keys |
| `icon-dungeon-grappling-hook` | Three-prong iron grapnel with a short rope eye |
| `icon-dungeon-piton` | Climbing piton with a spiked blade and an eye |
| `icon-dungeon-murder-hole` | Ceiling slab with a central opening, seen from below |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square cell
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**.

Recommended minimum display sizes (after inspecting 32/48/64/96 light+dark previews):

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| portcullis | 32px | Arch and grate read at 32 |
| arrow-slit | 32px | Tall narrow slit in a stone wall face reads at 32; the masonry courses are clearer at 48 |
| cresset | 32px | Basket on a post reads at 32; coals and flame clearer ≥48 |
| manacles | **48px** | Open cuffs are a pair of faint C-shapes at 32; chain and hinges read at 48 |
| key-ring | **48px** | At 32 the keys collapse to a cluster; the ring and mixed bits read at 48 |
| grappling-hook | **48px** | At 32 it is a small claw; rope and three prongs read at 48 |
| piton | **48px** | At 32 it is a thin bent spike; the eye and dogleg read at 48 |
| murder-hole | **48px** | At 32 it is a small dark window in a trapezoid; the soffit and opening read at 48 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA PNG (one copy each)
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `INVENTORY.md` — per-item source and license
- `HONEST_LOOK.md` — small-size notes
- `MANIFEST.json` — per-file SHA256 + sizes
- `SHA256SUMS` — checksums of staged files except itself
- `VALIDATOR_RESULTS.json` — icon gate results

No scripts, fonts, or external references in shipping SVG.
