# Open Kit — Cloister Walk Icons

Eight inventory icons for a cloister walk: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`. Drawn with thick strokes, few details, and high value contrast so the shapes hold at 32px.

These are unmanned walk fittings, not weapons, and not world-ground tiles.

## Contents

| Icon | Function |
|------|----------|
| `icon-cloister-arcade` | Intact stone walk bay: slim piers, a pointed two-centred arch with a keystone, and a stone wall face around it |
| `icon-cloister-bench` | Backless stone bench with a thick slab and two solid ends |
| `icon-cloister-hopper` | Wall-mounted lead rain hopper with a flared open head, a downpipe, and a shoe |
| `icon-cloister-alms-box` | Plain strapped timber chest on a short post, with a coin slot on the lid |
| `icon-cloister-trough` | Long, low, open stone washing trough with shallow water |
| `icon-cloister-grille` | Iron gate filling a stone arch, including the head, with plain bars |
| `icon-cloister-capital` | Stone column capital with a flat abacus, a cushion body, and a short shaft stub |
| `icon-cloister-lantern` | Short walk lantern with a square glazed box and a plain cap |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**. Inspected at 32/48/64/96 on light and dark slots.

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| arcade | 32px | Piers, wall face, and pointed opening read at 32; the voussoirs and spandrels are clearer at 48 |
| bench | 32px | Thick slab and two solid ends read at 32; the iron pins are clearer at 48 |
| hopper | 32px | Wall plane, flared head, and downpipe read at 32; the shoe is clearer at 48 |
| alms-box | 32px | Chest, post, strap, and hasp read at 32; the lid coin slot is clearer at 48 |
| trough | 32px | Long low basin and shallow water read at 32; the rim staples are clearer at 48 |
| grille | 32px | Stone arch and iron gate read at 32; the bars in the arch head are clearer at 48 |
| capital | 32px | Flat abacus, cushion, and shaft stub read at 32 |
| lantern | 32px | Short post, plain cap, and glazed box read at 32; the panes are clearer at 48 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA PNG (one copy each)
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
