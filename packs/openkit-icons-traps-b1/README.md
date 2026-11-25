# openkit-icons-traps-b1

Eight mechanical-trap inventory icons: dungeon and wilderness devices for loot, crafting, or quests (256×256 RGBA PNG + editable SVG). Generic archetypes only.

## Contents

| Icon | Function |
|------|----------|
| `icon-trap-bear` | Open-jaw bear trap |
| `icon-trap-spikes` | Floor spike plate |
| `icon-trap-blade` | Swinging pendulum blade |
| `icon-trap-dart` | Fletched dart |
| `icon-trap-tripwire` | Tripwire between two stakes |
| `icon-trap-snare` | Rope snare with bent rod |
| `icon-trap-plate` | Stone pressure plate |
| `icon-trap-pit` | Open pit with hinged lid |

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
| bear | 32px | Jaws and pan read at 32; teeth clearer ≥48 |
| spikes | 32px | Strong silhouette |
| blade | **48px** | Crescent reads as a comma or leaf at 32; chain knob is a dot |
| dart | 32px | Clear arrow-like silhouette; fletching clearer ≥48 |
| tripwire | **48px** | Collapses to an H-shape at 32 |
| snare | **48px** | Loop is a weak curl at 32; rod and noose read at 48 |
| plate | 32px | Square tile reads at 32; bolts and mark clearer ≥48 |
| pit | **48px** | Hatch and hole read at 48; 32 is a small dark window |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `icons/` — paired editable SVG + 256×256 RGBA transparent PNG for each item
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `MANIFEST.json` — per-file SHA256 + sizes

No scripts, fonts, or external references in shipping SVG.
