# openkit-icons-ingredients-b1

Eight raw culinary / foraging ingredient inventory icons (256×256 RGBA PNG + editable SVG). Generic archetypes only.

## Contents

| Icon | Function |
|------|----------|
| `icon-ingredient-carrot` | Raw carrot |
| `icon-ingredient-onion` | Raw onion bulb |
| `icon-ingredient-cabbage` | Raw cabbage head |
| `icon-ingredient-egg` | Raw egg |
| `icon-ingredient-garlic` | Raw garlic bulb |
| `icon-ingredient-berries` | Berry cluster |
| `icon-ingredient-honey-jar` | Honey jar |
| `icon-ingredient-flour-sack` | Flour sack |

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
| carrot | 32px | Greens thin at 32; root silhouette holds |
| onion | 32px | Bulb readable; sprouts weak below 48 |
| cabbage | **48px** | Layered leaf lobes clearer ≥48; silhouette OK at 32 |
| egg | 32px | Strong oval silhouette |
| garlic | **48px** | Clove splits + connected papery neck clearer ≥48 |
| berries | 32px | Cluster reads; leaf weak at 32 |
| honey-jar | 48px | Lid + fill level clearer ≥48 |
| flour-sack | **48px** | Gathered neck + cord + cloth folds clearer ≥48 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA transparent PNG for each item
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `MANIFEST.json` — per-file SHA256 + sizes

No scripts, fonts, or external references in shipping SVG.
