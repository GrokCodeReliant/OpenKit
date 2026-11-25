# Open Kit — Chapel Furnishings Icons

Eight inventory icons for choir and sacristy fittings of a small chapel: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`. Drawn with thick strokes, few details, and high value contrast so the shapes hold at 32px.

These are unmanned choir and sacristy fittings.

## Contents

| Icon | Function |
|------|----------|
| `icon-chapel-piscina` | Stone wall face with an arched niche and a pale half-round stone basin on the sill |
| `icon-chapel-ambry` | Stone wall face with a small recessed timber cupboard door, iron straps and a hinge |
| `icon-chapel-pulpit` | Enclosed timber preaching box on a short stair, with a projecting book board |
| `icon-chapel-stall` | Single high-backed timber choir stall with side wings and a seat |
| `icon-chapel-prie-dieu` | Open-front timber kneeler with a low step and a slanted book rest |
| `icon-chapel-credence` | Small timber side table with a lower shelf and two plain lidded bronze cruets |
| `icon-chapel-cruets` | Pair of plain lidded bronze flasks with simple handles, slightly set apart |
| `icon-chapel-sanctus-bell` | Classic hand bell with a short timber handle and a rounded flared bronze cup |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**. Inspected at 32/48/64/96 on light and dark slots.

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| piscina | 32px | Wall face, arched niche, and half-round basin on the sill read at 32; the rim and the interior shadow are clearer at 48 |
| ambry | 32px | Wall face and recessed timber door read at 32; the hinge straps and the hasp are clearer at 48 |
| pulpit | 32px | Enclosed box, posts, and stair read at 32; the book board is clearer at 48 |
| stall | 32px | High back and seat read at 32; the side wings are clearer at 48 |
| prie-dieu | 32px | Open front, kneeling step, and slanted rest read at 32 |
| credence | 32px | Table, lower shelf, and two cruets read at 32; the cruet lids are clearer at 48 |
| cruets | 32px | The paired flasks read at 32; the lids and the handles are clearer at 48 |
| sanctus-bell | 32px | Short handle and rounded bronze cup read at 32; the lip and the clapper are clearer at 48 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA PNG (one copy each)
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
