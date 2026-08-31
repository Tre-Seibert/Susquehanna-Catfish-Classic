# Susquehanna Catfish Classic — Website

Static, mobile-first site for the Susquehanna Catfish Classic. No build step, no dependencies to install — it's plain HTML, Tailwind via CDN, and one stylesheet.

## Run it

Open `index.html` in a browser. That's it.

For a local server (needed if you add anything that fetches files):

```bash
# Python
python -m http.server 8000

# or Node
npx serve .
```

Then visit <http://localhost:8000>.

## Structure

```
website/
├── index.html      Home — hero, details, registration, merch
├── rules.html      About & tournament rules
├── contact.html    Locations & map for Lake Clarke Marina
├── css/styles.css  Heritage theme: palette, paper texture, components
├── js/main.js      Mobile nav, form handling, footer year
└── assets/         Logo + imagery (see "Assets still needed")
```

## Assets

The hooked fish is in the homepage hero. The golden-hour river photo is the hero background (`hero--photo`): portrait crop on phones, wide crop from 768px up.

Still needed:

| File | Where it appears |
|---|---|
| `logo-stacked.png` | Full lockup with type (hero currently uses the fish only) |
| `og-image.jpg` | Social sharing preview |
| Real merch mockups | Shirt / hat on garments |

## Still to wire up

- **Registration form** — currently client-side only. It validates and shows a confirmation, but *nothing is sent anywhere*. Connect it to Formspree, Netlify Forms, or a backend before going live.
- **Payment** — no processor connected. Stripe Payment Links or a PayPal button are the fastest paths; both drop straight into the form section.
- **Merch store** — "Notify Me" buttons are placeholders. Snipcart or Shopify Buy Buttons work well for a small run.
- **Email address** — `info@susquehannacatfishclassic.com` on the contact page is a placeholder.
- **Rules** — sections 3, 4, 5, and 6 are marked as drafts pending committee sign-off.

## Deploy

Any static host works. Drag the `website/` folder onto:

- **Netlify** — drag-and-drop at [app.netlify.com/drop](https://app.netlify.com/drop). Free forms included, which solves the registration problem.
- **Cloudflare Pages** or **Vercel** — connect a repo, no build command needed.
- **GitHub Pages** — push and enable Pages in repo settings.

Recommendation: **Netlify**, because its built-in form handling means registration works with just one attribute added to the `<form>` tag (`data-netlify="true"`) and no backend at all.

## Notes

- **Tailwind is loaded from the Play CDN.** Fine for this scale, and it keeps the site editable by anyone without a toolchain. If it grows, install Tailwind properly and build a real stylesheet — the config block at the top of each HTML file ports straight over.
- **Fonts** (Alfa Slab One, Staatliches, Yellowtail, Libre Franklin) load from Google Fonts. All free for commercial use.
- **Accessibility:** skip links, ARIA labels on the nav toggle, visible focus rings, and semantic landmarks are in place. Color contrast was measured, not eyeballed — see the contrast table in the brand guidelines.
- **The 2027 dates (Aug 27–28) are computed correctly** as the last Friday and Saturday of August. Future years: 2028 is Aug 25–26, 2029 is Aug 24–25.
