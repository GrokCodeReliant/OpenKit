# openkit-sprites-civic-b1

Eight civic / roadside world-prop sprites (256×256 RGBA PNG + editable SVG) for 2D placement. Generic archetypes only.

## Contents

| Sprite | Function |
|--------|----------|
| `sprite-fountain-plaza` | Tiered plaza fountain |
| `sprite-mailbox` | Roadside mailbox on post |
| `sprite-milestone` | Tall stone milestone with rounded head and carved direction chevron |
| `sprite-birdbath` | Garden birdbath |
| `sprite-pillory` | Wooden pillory with transparent head/hand cutouts |
| `sprite-stone-bollard` | Short squat wide stone bollard |
| `sprite-mounting-block` | Horse mounting block (stepped) |
| `sprite-flagpole` | Flagpole with hanging flag |

## Ground-plane anchor (numeric)

**Convention:** top-left pixel origin on the untrimmed 256×256 master canvas.

**Common ground-plane reference for all eight sprites:**

- Pixel: **`(128, 232)`**
- Normalized (from top-left): **`(0.5, 0.90625)`**

This is a **canvas coordinate on the untrimmed master**, not a bottom-of-bbox trim and not an engine-integrated pivot. To place the prop on a ground line in a scene, set the sprite pivot / origin to these coordinates (or the equivalent normalized values). Ground shadow / base ellipse may extend **below** y=232 toward the canvas bottom; that extent is intentional and is not the pivot.

Each entry in `MANIFEST.json` repeats `anchor_point_px` and `anchor_point_normalized` for the sprite.

SVG sources use `transform="translate(128 232) scale(0.82) translate(-128 -232)"` so geometry scales about the ground reference and `(128,232)` stays fixed.

## Display size (honest)

PNG masters are **256×256 export resolution**, not native game scale. Typical world-prop display is often **48–96px**.

Recommended minimum display sizes (after visual inspection of 32/48/64/96 previews on light and dark):

| Sprite | Min recommended | Notes |
|--------|-----------------|-------|
| fountain-plaza | 48px | Tiers merge below 48 |
| mailbox | 48px | Flag readable ≥48 |
| milestone | 48px | Chevron readable ≥48; ok silhouette at 32 |
| birdbath | 48px | Basin water cue weak below 48 |
| pillory | **64px** | Transparent head+hand cutouts readable at 64; at 32 hand holes may close under filtering |
| stone-bollard | 32px | Squat silhouette holds |
| mounting-block | 48px | Step count clearer ≥48 |
| flagpole | 48px | Flag stripes weak below 48 |

## License

CC0 1.0 Universal — see `LICENSE`. Credits: see `CREDITS.md`.

## Layout

- `sprites/` — paired editable SVG + 256×256 RGBA transparent PNG for each item
- `sheet/CONTACT_SHEET.png` — export-resolution contact sheet
- `MANIFEST.json` — per-file SHA256 + sizes

No scripts, fonts, or external references in shipping SVG.
