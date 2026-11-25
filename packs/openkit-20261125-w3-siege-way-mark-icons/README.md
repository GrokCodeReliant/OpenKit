# Open Kit — Siege and Way-Mark Icons (20261125 wave 3)

Eight inventory icons for castle-yard engines and two travel markers: maps, journals, and UI. Original CC0 geometry. Editable SVG + transparent PNG pairs under `icons/`. Drawn with thick strokes, few details, and high value contrast so the shapes hold at 32px.

These are unmanned engines and markers, not hand-held weapons.

## Contents

| Icon | Function |
|------|----------|
| `icon-siege-battering-ram` | Heavy timber ram with a blunt dark iron cap, on two A-frame trestles |
| `icon-siege-ballista` | Stand-mounted ballista with bow arms, string, and a bolt |
| `icon-siege-pavise` | Tall standing shield with a rear prop and a plain face |
| `icon-siege-mantlet` | Wide wheeled screen with a viewing slit and a plain face |
| `icon-siege-stone-shot` | Cluster of three siege stone balls |
| `icon-siege-bolt-rack` | Low rack holding four heavy ballista bolts |
| `icon-sundial` | Horizontal sundial on a short plinth, with a right-triangle gnomon blade |
| `icon-waystone` | Rough-hewn standing marker with an incised ring |

## Alignment (inventory icons)

These are **inventory / UI icons**, not world-ground sprites.

- Canvas: untrimmed **256×256**
- Intended placement: **visual center alignment** of the artwork within the square
- **Not** an engine ground-plane pivot; do not treat bottom-of-bbox as a foot point

## Display size (honest)

PNG masters are **256×256 export resolution**, not native UI scale. Inventory slots often show **32–64px**. Inspected at 32/48/64/96 on light and dark slots.

| Icon | Min recommended | Notes |
|------|-----------------|-------|
| battering-ram | 32px | Log, blunt dark iron cap, and A-frame trestles read at 32 |
| ballista | 32px | Stand and bow arms read at 32; the string is faint at 32 (clearer at 48) |
| pavise | 32px | Tall standing shield reads at 32; can read as a door/headstone at a glance (rear prop clearer at 48) |
| mantlet | 32px | Wide screen, slit, and wheels read at 32 |
| stone-shot | 32px | Three stone spheres, one larger, read at 32 |
| bolt-rack | 32px | Low rack and heavy-headed bolts read at 32; heads are clearer at 48 |
| sundial | 32px | Plinth, dial, and right-triangle gnomon blade read at 32; rim ticks are clearer at 48 |
| waystone | 32px | Rough standing stone and incised ring read at 32 |

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
