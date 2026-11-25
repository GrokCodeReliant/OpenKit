# Open Kit — Keep Stable Icons

Eight inventory icons for keep-yard stable architecture and fittings: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`. Drawn with thick strokes, few details, and high value contrast so the shapes hold at 32px.

## Contents

| Icon | Function |
|------|----------|
| `icon-stable-stall` | Timber stall front with a low slatted breast between two posts and an open bay above |
| `icon-stable-door` | Timber split stable door with the upper leaf swung open and the lower leaf closed, strap hinges, and a thin stone surround |
| `icon-stable-hay-hatch` | Small square hay hatch high on a stone wall, with hay spilling out and a shutter swung open to the side |
| `icon-stable-manger` | Timber hay rack on legs with sloping slats and a hay tuft on top |
| `icon-stable-saddle-rack` | Timber saddle stand with a rounded ridge rest on a sturdy post, empty |
| `icon-stable-peg-rail` | Wall-mounted timber board with five pegs angled up and a rope loop on one peg |
| `icon-stable-watering-tub` | Low round coopered timber tub with two iron hoops and a water disc below the rim |
| `icon-stable-blanket-rail` | Tall two-post timber blanket rail with a high bar, a lower bar, iron caps, and a plain blanket over the top bar |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**. Inspected at 32/48/64/96 on light and dark slots.

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| stall | 32px | Posts, low slatted breast, and open bay read at 32; the slats are clearer at 48 |
| door | 32px | Closed lower leaf, open upper leaf, and the horizontal split read at 32; the strap hinges and the latch are clearer at 48 |
| hay-hatch | 32px | Compact wall, spilling hay, and the open shutter read at 32; the shutter boards are clearer at 48 |
| manger | 32px | Sloping slats and the hay tuft read at 32; the individual slats are clearer at 48 |
| saddle-rack | 32px | Sturdy post and rounded ridge rest read at 32 |
| peg-rail | 48px | The board reads at 32; the five pegs and the rope loop need 48 |
| watering-tub | 32px | Low wide tub, two hoops, and the water disc read at 32; the stave lines are clearer at 48 |
| blanket-rail | 32px | Tall posts, two bars, iron caps, and the draped blanket read at 32 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA PNG (one copy each)
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
