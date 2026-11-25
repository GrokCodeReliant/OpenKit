# Open Kit — Garden Court Icons

Eight inventory icons for a cloister garth or small planted court: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`. Drawn with thick strokes, few details, and high value contrast so the shapes hold at 32px.

These are unmanned garden furniture and tools, not weapons and not world-ground tiles.

## Contents

| Icon | Function |
|------|----------|
| `icon-garden-birdbath` | Stone pedestal with a shallow open bowl |
| `icon-garden-planter` | Low rectangular stone box with soil and a rounded shrub |
| `icon-garden-trellis` | Tall rectangular timber trellis with an open diamond lattice and a climbing vine |
| `icon-garden-cold-frame` | Low timber box with a sloped glazed lid, slightly open |
| `icon-garden-lavabo` | Tall stone wash basin with a deeper bronze-lined bowl and a spout |
| `icon-garden-watering-can` | Metal watering can with a handle and a rose spout |
| `icon-garden-herb-bed` | Low bordered herb bed with several small plants |
| `icon-garden-fountain` | Small free-standing basin fountain with a short central jet |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**. Inspected at 32/48/64/96 on light and dark slots.

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| birdbath | 32px | Short pedestal and shallow open bowl read at 32; close to the lavabo at 32 |
| planter | 32px | Stone box, soil, and rounded shrub read at 32 |
| trellis | 32px | Tall posts, open diamond lattice, and climbing vine read at 32; vine leaves are clearer at 48 |
| cold-frame | 32px | Low timber box and sloped lid read at 32; glaze panes and the propped opening are clearer at 48 |
| lavabo | 32px | Tall pedestal and deeper basin read at 32; close to the birdbath at 32; the bronze spout is clearer at 48 |
| watering-can | 32px | Body, handle, and rose spout read at 32; the handle is boxy; the rose holes are clearer at 48 |
| herb-bed | 32px | Bordered bed and planted clumps read at 32; the clumps read as round shrubs; the taller herb is clearer at 48 |
| fountain | 32px | Low basin and short central jet read at 32 |

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
