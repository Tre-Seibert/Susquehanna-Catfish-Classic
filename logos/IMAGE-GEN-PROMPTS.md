# Image Generation Prompts — Susquehanna Catfish Classic

Copy-paste prompts for producing the brand artwork. Written for **Claude.ai, ChatGPT/DALL·E, Midjourney, or Ideogram**. Notes per tool are at the bottom.

---

## ⚠️ Read this first — the text problem

**AI image models garble lettering.** They will produce "SUSQUEHANNAA CATFSH CLASSIC" and you won't be able to fix it inside the image.

So the professional workflow is:

1. **Generate the illustration only** — the catfish, the scene, the badge frame — with *no text at all* (Prompts 1–4).
2. **Set the type separately** in Illustrator, Affinity Designer, Figma, or even Canva, using the real fonts specified in the brand guidelines.
3. Combine the two.

Prompt 5 generates a full badge *with* text — use it only for **concepting and client presentation**, never as the final production file. If the client loves a text-included version, have the type reset properly before it goes to the screen printer.

**Ideogram is the exception** — it handles text far better than the others. If you have access to it, use it for the text-inclusive versions.

---

## The palette (paste into any prompt as needed)

```
Susquehanna Slate #2E4A52 · Rust Red #A8442A · Aged Ochre #C68B2C
Moss Green #5A6B4A · Walnut Brown #4A3728 · Aged Oat #EDE4D0 · River Ink #211D1A
```

---

## Prompt 1 — Primary catfish illustration (the hero asset)

**Use for:** the core mark. Everything else derives from this. Generate this first and get it right before moving on.

```
A vintage 1950s screen-printed illustration of a large flathead catfish in profile,
facing right. Heritage American outdoor-brand style — like an old tackle shop sign or
a mid-century fishing lure box label.

Bold hand-drawn linework with visible ink weight variation. Limited flat color
separation, only 3 colors: deep muted slate blue-teal (#2E4A52), warm rust red
(#A8442A), and aged oat cream (#EDE4D0). Subtle halftone dot shading and light
distressed texture, as if screen printed on cotton decades ago and slightly faded.

The catfish should look characterful and slightly weathered — prominent barbels
(whiskers) sweeping back, broad flat head, powerful body, visible fin structure.
Confident and rugged, not cartoonish, not photorealistic, not cute.

Flat 2D vector-style illustration. No gradients, no chrome, no 3D rendering,
no drop shadows, no lens flare. Plain white background. No text, no lettering,
no words anywhere in the image.
```

**Settings:** square (1:1). Generate 4+ variations.
**If it comes out wrong:** the usual failure is "too cute" or "too realistic." Add `less cartoonish, more like a woodcut` or `less detailed, bolder shapes`.

---

## Prompt 2 — Circular heritage badge frame (no text)

**Use for:** the patch/badge mark. Type gets set into the banners afterward.

```
A vintage circular badge emblem frame in 1950s heritage American outdoor style.
Empty ring border with a thin inner pinstripe line, and two blank ribbon banners —
one arcing across the top, one across the bottom — left completely empty for text
to be added later.

Colors: deep muted slate blue-teal (#2E4A52) outer ring, aged oat cream (#EDE4D0)
interior, warm rust red (#A8442A) banners. Slight distressed screen-print texture,
faded and worn like an old embroidered patch or enamel sign.

Flat 2D vector illustration, bold clean linework, limited flat colors, no gradients,
no 3D, no shadows. Centered composition. Plain white background.
Absolutely no text, no letters, no numbers, no symbols in the banners — leave them blank.
```

**Settings:** square (1:1).
**Note:** models love to sneak text into banners. If it does, regenerate with `the ribbon banners must be completely empty and smooth` appended.

---

## Prompt 3 — Simplified one-color mark (shirts & patches)

**Use for:** single-screen printing, embroidery, hats, stamps. Cheapest to produce.

```
A vintage single-color catfish silhouette illustration, 1950s heritage outdoor
brand style. One color only: deep slate blue-teal (#2E4A52) on plain white.

Bold simplified shapes with strong silhouette readability — prominent sweeping
barbels, broad flat head, clear fin shapes. Woodcut or linocut feel with confident
carved linework. Minimal interior detail, only enough to read as a catfish at small size.

Flat 2D, no gradients, no halftones, no shading, no outlines around the outside.
Must remain legible when scaled down to one inch wide. Plain white background.
No text, no lettering.
```

**Settings:** square (1:1).
**Why one color matters:** every additional color is another screen and another setup fee at the printer. A strong one-color mark keeps shirt costs down and looks more authentically vintage anyway.

---

## Prompt 4 — River scene (website hero background)

**Use for:** the hero section background on the site, behind a dark overlay.

```
A wide atmospheric photograph of the lower Susquehanna River in Pennsylvania at
golden hour, shot from water level. Wide calm river, low forested ridgelines in the
distance, warm hazy light, soft mist on the water. A small working marina with
modest boat slips visible on the left bank, out of focus.

Muted warm color grading — desaturated teals and warm ochres, slightly faded like
aged film. Kodak Portra 400 look. Cinematic wide aspect ratio, natural light only,
no people, no text, no watermarks.
```

**Settings:** wide (16:9 or 21:9).
**Note:** this is the one asset where photorealism is right. Keep it understated — it sits *behind* text, so it must not compete. Generate a few and pick the calmest.

---

## Prompt 5 — Full badge WITH text (concepting only)

**Use for:** showing the client a complete-looking mark. ⚠️ Not production-ready — reset the type properly before handoff.

```
A vintage circular tournament badge logo in 1950s heritage American outdoor style,
like an old fishing club patch or tackle shop sign.

Text layout, spelled exactly:
- Curved across the top banner: "SUSQUEHANNA"
- Curved across the bottom banner: "CATFISH CLASSIC"
- Small text under the bottom banner: "LONG LEVEL, PA"
- In the center: a bold vintage illustration of a flathead catfish in profile

Typography: heavy vintage slab serif capitals, sign-painter style, slightly condensed.

Colors: deep muted slate blue-teal (#2E4A52), warm rust red (#A8442A), aged ochre
(#C68B2C), aged oat cream (#EDE4D0). Distressed screen-print texture, faded and worn.

Flat 2D vector illustration, bold linework, limited flat colors, no gradients,
no 3D, no chrome, no drop shadows. Centered, symmetrical. Plain white background.
```

**Settings:** square (1:1). Expect to run this 10+ times to get clean spelling.

---

## Prompt 6 — T-shirt back print

**Use for:** merch concepting.

```
A vintage screen-printed t-shirt back graphic, 1950s heritage American outdoor style.
Large bold flathead catfish illustration centered, with decorative banner shapes
above and below it left blank for text.

Printed on a heather oatmeal cream shirt. Colors limited to three inks: deep slate
blue-teal (#2E4A52), warm rust red (#A8442A), and aged ochre (#C68B2C).
Visible screen-print texture with slight ink cracking and fading, like a well-worn
vintage souvenir shirt.

Flat 2D illustration, no gradients, no 3D mockup rendering. Front-facing flat lay.
No text, no lettering — leave banner areas empty.
```

---

## Prompt 7 — Sticker / patch set

```
A set of three vintage fishing tournament stickers arranged on a plain white
background, 1950s heritage outdoor style: one circular badge, one die-cut catfish
shape, one horizontal rectangular bumper sticker with blank banner areas.

Colors: deep slate blue-teal (#2E4A52), warm rust red (#A8442A), aged oat cream
(#EDE4D0). Distressed screen-print texture, slightly worn edges.

Flat 2D vector illustration, bold linework, limited flat colors, no gradients,
no 3D, no shadows. No text, no lettering anywhere.
```

---

## Prompt 8 — Composite approved fish into the badge (use this next)

**Use for:** the circular lockup. Do **not** generate a new catfish.

**Attach these two files, in this order:**
1. `logos/flathead-catfish-vintage-screenprint.png` — the approved profile fish
2. `logos/badge-frame.png` — the empty circular badge

### 8a — Production (no lettering)

Use this if you will set type later in Figma / Illustrator / Canva.

```
Composite these two attached images into one circular tournament badge. Do not
redraw, restyle, or invent a new fish.

IMAGE 1 is the exact catfish to use — vintage screen-printed flathead in profile,
facing right, three inks (slate teal, rust red on fins/gills, cream belly, halftone
shading). Copy this fish as faithfully as possible. Same pose, same linework, same
whiskers, same colors. Do not cartoon it, do not make it photorealistic, do not
flip it.

IMAGE 2 is the exact badge frame to use — circular slate-teal ring, cream interior,
two empty rust-red ribbon banners (one arcing across the top, one across the
bottom) with swallowtail ends. Keep this frame. Do not redesign the ring, pinstripes,
or banners.

Place the catfish from IMAGE 1 in the cream center of IMAGE 2. Scale the whole
fish to fit inside the inner circle — head, body, tail, and barbels all visible,
nothing clipped. Centered, facing right. A little breathing room from the inner
pinstripe. The fish sits on the cream field, not on a black or white box.

Leave both ribbon banners completely empty and smooth. No text, no letters, no
numbers, no dummy Latin, no symbols.

Same distressed screen-print texture as the source images. Flat 2D, limited flat
color, no gradients, no chrome, no 3D, no drop shadows. Square 1:1. Plain white
background around the badge. Transparent-looking white, not a drop shadow.
```

**Settings:** square (1:1). If the fish gets redrawn, stop and say "use IMAGE 1 as a literal copy, do not reinterpret." If letters appear in the banners, append `the ribbon banners must be completely empty and smooth`.

### 8b — Client concept (with lettering)

Use this only to show a finished-looking mark. Spelling will be unreliable. Reset type in real fonts before anything goes to a printer. **Ideogram** if you have it.

```
Composite these two attached images into one circular tournament badge. Do not
redraw, restyle, or invent a new fish.

IMAGE 1 is the exact catfish — vintage screen-printed flathead in profile, facing
right. Copy it faithfully into the center of the badge. Same pose, linework,
whiskers, and three-ink palette (slate teal #2E4A52, rust red #A8442A, aged oat
#EDE4D0).

IMAGE 2 is the exact badge frame — circular slate-teal ring, cream interior, two
rust-red ribbon banners with swallowtail ends. Keep this frame.

Place the catfish in the cream center, fully visible, nothing clipped, facing right.

Lettering, spelled exactly, heavy vintage slab-serif capitals (sign-painter, slightly
condensed), aged oat cream (#EDE4D0) on the rust banners:
- Top banner, curved along the arc: SUSQUEHANNA
- Bottom banner, curved along the arc: CATFISH CLASSIC
- Small text just under the bottom banner, outside the ring: LONG LEVEL, PA

No other words. No misspellings. No extra slogans.

Same distressed screen-print texture. Flat 2D, no gradients, no chrome, no 3D,
no drop shadows. Square 1:1. Plain white background.
```

**Settings:** square (1:1). Expect several runs to get spelling clean. If the fish changes, go back to 8a and add type yourself.

**Cleaner than either prompt:** drop IMAGE 1 on IMAGE 2 in Figma or Photoshop, then set Alfa Slab One / Staatliches on the banners. AI is the slow way to composite two images you already like.

---

## Tool-specific notes

| Tool | Notes |
|---|---|
| **Ideogram** | Best text rendering by far. Use for any prompt that includes lettering (5). Set style to "Design." |
| **Midjourney** | Best illustration quality. Append `--style raw --ar 1:1`. Add `--no text, words, letters` to suppress lettering. Use `--cref` to keep the fish consistent across assets. |
| **ChatGPT / DALL·E** | Good at following detailed instructions, weaker on vintage texture. Ask it to "make it flatter and more screen-printed" as a follow-up. |
| **Claude.ai** | Good for iterating conversationally — paste the prompt, then refine in plain language. |

## After you generate

1. **Get the background out.** Use [remove.bg](https://remove.bg) or Photoshop to knock out white and export transparent PNG.
2. **Vectorize it.** Run it through Illustrator's Image Trace or [vectorizer.ai](https://vectorizer.ai) so it scales cleanly and the screen printer can separate colors. Raster art at shirt size will look rough.
3. **Set the real type** in Alfa Slab One / Staatliches per the brand guidelines.
4. **Count your colors.** Confirm the final art uses 3 inks or fewer before it goes to the printer.
5. Drop finals into `logos/` as `logo-primary.png`, `logo-primary.svg`, `icon-mark.png`, `badge.png`.

## Consistency across assets

The fish must look like the *same fish* everywhere. Best approach: nail Prompt 1, then for every later asset either reference that image directly (Midjourney `--cref`, or upload it in ChatGPT/Claude and say "use this exact fish") or composite the approved fish in manually rather than regenerating it.
