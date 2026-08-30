# Susquehanna Catfish Classic

Branding kit and website for an annual catfish tournament on the lower Susquehanna River, hosted by **Lake Clarke Marina** in Wrightsville, PA.

> **Where Giants Run the River**
> August 27–28, 2027 · $125/boat · 4 anglers max · Weigh-in 4:00 PM Saturday

---

## Status

| Deliverable | Status |
|---|---|
| Name, tagline, positioning | ✅ Done |
| Competitive research | ✅ Done |
| Color palette (with measured contrast) | ✅ Done |
| Typography system | ✅ Done |
| Brand guidelines | ✅ Done |
| Merch specs for printer | ✅ Done |
| Website (3 pages, tested) | ✅ Done |
| **Logo artwork** | ⏳ Illustration done (profile + hooked + badge frame). Lockups/type not set yet |
| Registration backend / payment | ⏳ Not wired up |
| Final rules (sections 3–6) | ⏳ Pending committee |

---

## Start here

**→ `logos/`**

Source illustrations are in:

- `flathead-catfish-vintage-screenprint.png` — primary mark (profile, facing right)
- `flathead-catfish-hooked-fighting-vintage-screenprint.png` — merch / poster illustration
- `badge-frame.png` — empty heritage badge (type still needs setting)

Transparent web versions live in `website/assets/`. Next: vectorize the profile fish, set type in Alfa Slab One / Staatliches, and build the stacked lockup.

---

## Structure

```
Susquehanna Catfish Classic/
├── README.md                      you are here
├── logos/
│   └── IMAGE-GEN-PROMPTS.md       7 prompts + production workflow
├── brand-guidelines/
│   └── brand-guidelines.md        full brand system
├── merch-mockups/
│   └── merch-specs.md             printer-facing specs
└── website/
    ├── README.md                  how to run + deploy
    ├── index.html                 home
    ├── rules.html                 about & rules
    ├── contact.html               locations & maps
    ├── css/styles.css
    ├── js/main.js
    └── assets/                    (artwork goes here)
```

## Run the site

Open `website/index.html` in a browser. No build step. See `website/README.md` for deploy options.

---

## Key decisions

**Direction: vintage / heritage river-town.** The category is saturated with dimensional, gradient-heavy, navy-and-gold marks — King Kat, Twisted Cat Outdoors, and most regional trails all look alike. A flat, faded, heritage-print identity differentiates immediately, and costs far less to screen print since every gradient is another screen.

**Palette:** Susquehanna Slate `#2E4A52`, Rust Red `#A8442A`, Aged Ochre `#C68B2C`, Moss Green `#5A6B4A`, Walnut Brown `#4A3728`, Aged Oat `#EDE4D0`, River Ink `#211D1A`. Neutrals are deliberately warm — never substitute pure white or black.

**Type:** Alfa Slab One (display), Staatliches (condensed), Yellowtail (script accent), Libre Franklin (body). All free Google Fonts.

**Merch rule:** three inks maximum on any piece.

---

## ⚠️ Worth knowing

**There's already a catfish tournament series operating out of Long Level.** The [Catfish Mafia Tournament Series](https://tm.americancatfishingassociation.com/catfish-mafia-tournament-series-long-level/about-the-tournament/) runs 8 events a year on the Susquehanna from Sunbury to the Conowingo pool, listed under the American Catfishing Association as "Catfish Mafia Tournament Series – Long Level" (contact: Andrew Lentz).

Not a name collision, but Long Level isn't open territory. Worth a conversation with the client about differentiation — and possibly about coordinating dates so the two events don't cannibalize the same local field.

**Verified facts** (not assumed):
- Lake Clarke Marina — 1552 Long Level Rd, Wrightsville, PA 17368 · (717) 252-2881
- Last Fri/Sat of August: **2027 = Aug 27–28**, 2028 = Aug 25–26, 2029 = Aug 24–25

---

## Next steps

1. Vectorize the profile fish and set type on the badge frame (Alfa Slab One / Staatliches)
2. Build stacked + horizontal lockups; one-color mark for hats
3. Get rules sections 3–6 signed off by the committee
4. Connect the registration form (Netlify Forms is the fastest path — see `website/README.md`)
5. Set up the real `info@` email address
6. Shoot real photography at the marina to replace the generated hero
