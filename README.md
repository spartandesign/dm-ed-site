# Digital Manufacturing &amp; Engineering Design — Course Site

A plain static website (the student "textbook") for the 18-week middle-school course
at Stauffer Middle School, Downey Unified. No build step, no framework — just HTML and
one CSS file. It drops straight into GitHub and deploys on Netlify.

## What's here

```
index.html            Home / course overview
unit-1.html           U1 · Foundations — Measure & Sketch   (Weeks 1–3)
unit-2.html           U2 · CAD in Onshape                   (Weeks 4–7)
unit-3.html           U3 · The Fingerboard                  (Weeks 8–11)
unit-4.html           U4 · Laser & Rack                     (Weeks 12–13)
unit-5.html           U5 · Capstone — Skate Park            (Weeks 14–18)
lab-reference.html    Machines, the laser rule, measurement standards, safety
glossary.html         Key terms, color-coded by strand
resources.html        Pacing spine, grading at a glance, the documentation system
404.html              Friendly not-found page
assets/style.css      All styling (light + dark themes, @font-face)
assets/theme.js       The light/dark toggle
assets/fonts/         Bundled woff2 fonts + their OFL licenses (offline-ready)
netlify.toml          Deploy config (publish the root, no build)
tools/build_site.py   Optional generator — regenerates the unit & reference pages
```

## Themes (projector-friendly)

The site loads in a **light, high-contrast theme by default** — built to stay legible on a
classroom projector (warm paper background, near-black text, larger type, darker accent
colors). The **"Dark" toggle** in the nav switches to the original night palette for students
reading on their own devices, and the choice is remembered in the browser.

## Editing content

Every page is plain HTML you can edit directly — open a file, change the text, save.

If you'd rather edit content in one place and keep all the unit pages perfectly consistent,
edit the data in `tools/build_site.py` and run it:

```
python3 tools/build_site.py
```

It rewrites `unit-1.html` … `unit-5.html`, `lab-reference.html`, `glossary.html`, and
`resources.html`. The generator is optional — the site works without it, and `index.html`
is maintained by hand.

## Fonts

The three typefaces (Bebas Neue, Space Mono, DM Sans) are **bundled locally** in
`assets/fonts/` as woff2 and declared with `@font-face` in `assets/style.css`. The site
needs **no internet** for the exact look — it renders identically on a classroom machine
that's offline. All three are under the SIL Open Font License; the license files sit
alongside the fonts.

## Deploy to Netlify

1. Push this folder to a GitHub repository.
2. In Netlify: **Add new site → Import an existing project → GitHub**, and pick the repo.
3. Leave the build command blank and set the publish directory to the repository root
   (the included `netlify.toml` already does this).
4. Deploy. Every push to the main branch republishes automatically.

You can also drag this folder straight onto the Netlify dashboard for a one-off deploy.
