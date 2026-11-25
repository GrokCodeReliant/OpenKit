# Open Kit — Crypt Undercroft Icons (20261125 wave 2)

Eight inventory icons for indoor cellar, crypt, and water-store silhouettes: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`. Drawn with thick strokes, few details, and high value contrast so most shapes hold at 32px.

## Contents

| Icon | Function |
|------|----------|
| `icon-dungeon-cistern` | Short masonry water cistern with an iron band |
| `icon-dungeon-wall-fountain` | Wall fountain with a spout and projecting basin |
| `icon-dungeon-urn` | Lidded burial urn on a short plinth |
| `icon-dungeon-ossuary-cist` | Closed stone ossuary cist with iron straps |
| `icon-dungeon-memorial-slab` | Memorial floor slab with an incised eight-petal rosette |
| `icon-dungeon-secret-door` | Hidden door in a stone wall with a ring pull |
| `icon-dungeon-sluice` | Drainage sluice with a raised iron plate |
| `icon-dungeon-spiral-stair` | Spiral stair around a stone newel |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square cell
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**. Inspected at 32/48/64/96 on light and dark slots.

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| cistern | 32px | Short tank, rim, and dark water read at 32; no crank or well parapet |
| wall-fountain | 32px | Wall, spout, and basin read at 32 |
| urn | 32px | Lidded ovoid on a plinth reads at 32 |
| ossuary-cist | 32px | Low stone box, flat lid, and horizontal straps read at 32 |
| memorial-slab | 32px | Slab and incised eight-petal rosette read at 32 |
| secret-door | 32px | Inset panel and ring pull read at 32; the running joint is clearer ≥48 |
| sluice | 32px | Frame, raised plate, and water gap read at 32 |
| spiral-stair | **48px** | The thick rail can read as a coil on a pole at a glance; use 48. See HONEST_LOOK.md. |

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
