# openkit-icons-creature-parts-b1

Eight creature-part crafting / loot inventory icons: raw animal and monster drops for crafting, trading, or quests (256×256 RGBA PNG + editable SVG). Generic archetypes only.

## Contents

| Icon | Function |
|------|----------|
| `icon-creature-antler` | Branching antler with burr base |
| `icon-creature-bone` | Long bone |
| `icon-creature-carapace` | Beetle wing-case shell (front plate and two wing cases) |
| `icon-creature-claw` | Hooked claw in a furred toe sheath |
| `icon-creature-fang` | Curved fang with root |
| `icon-creature-feather` | Feather with quill |
| `icon-creature-shell` | Spiral sea shell |
| `icon-creature-wing` | Leathery membrane wing |

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
| antler | **48px** | Tines merge into a twig shape at 32 |
| bone | 32px | Strong silhouette |
| carapace | 32px | Split wing cases readable at 32 |
| claw | **48px** | Dark claw is low-contrast on very dark slots below 48 |
| fang | **48px** | Thin at 32; gum line clearer ≥48 |
| feather | **48px** | Quill thin at 32; vane reads |
| shell | 32px | Spiral reads at 32 |
| wing | 32px | Scalloped edge reads; finger struts clearer ≥48 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA transparent PNG for each item
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `MANIFEST.json` — per-file SHA256 + sizes

No scripts, fonts, or external references in shipping SVG.
