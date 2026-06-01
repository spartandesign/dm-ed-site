# Digital Manufacturing & Engineering Design — Course Syllabus Site

A single-page syllabus website for the 18-week middle-school course at Stauffer Middle
School, Downey Unified. Plain static HTML, no build step. All teaching content, assignments,
and grades live in the Canvas course; this page is the public front door and points to it.

## What's here
```
index.html            The syllabus (course description, the 18-week arc, grading, the lab)
404.html              Friendly not-found page
assets/style.css      All styling (light + dark themes, @font-face)
assets/theme.js       The light/dark toggle
assets/fonts/         Bundled woff2 fonts + their OFL licenses (offline-ready)
netlify.toml          Deploy config (publish the root, no build)
```

## Set the Canvas link (important)
The "Go to the Canvas course" buttons currently point at a placeholder,
`https://YOUR-CANVAS-COURSE-URL`. Once your Canvas course is published, open `index.html`
and replace every `https://YOUR-CANVAS-COURSE-URL` with your real course URL (it appears a
few times — nav, hero, the closing band, and the footer). Save, commit, and push.

## Themes
Loads in a projector-friendly light theme by default; the "Dark" toggle in the nav switches
to the night palette and remembers the choice.

## Fonts
Bebas Neue, Space Mono, and DM Sans are bundled locally in `assets/fonts/`, so the page needs
no internet for the exact look. All three are under the SIL Open Font License.

## Deploy to Netlify
1. Push this folder to a GitHub repository.
2. Netlify: Add new site → Import an existing project → GitHub → pick the repo.
3. Leave the build command blank; publish directory is the root (netlify.toml sets this).
4. Deploy. Pushes to the main branch redeploy automatically.
You can also drag this folder onto the Netlify dashboard for a one-off deploy.
