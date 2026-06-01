#!/usr/bin/env python3
# build_site.py — emits consistent static HTML for the DM&ED course site.
# Output is plain HTML in build/ (no build step needed to deploy).
import html, os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_ITEMS = [
    ("u1", "unit-1.html", "U1 · Foundations"),
    ("u2", "unit-2.html", "U2 · CAD"),
    ("u3", "unit-3.html", "U3 · Fingerboard"),
    ("u4", "unit-4.html", "U4 · Laser"),
    ("u5", "unit-5.html", "U5 · Capstone"),
    ("lab", "lab-reference.html", "Lab"),
    ("glossary", "glossary.html", "Glossary"),
    ("resources", "resources.html", "Resources"),
]

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{html.escape(desc)}">
<title>{html.escape(title)}</title>
<script>try{{var t=localStorage.getItem('dmed-theme');if(t==='dark')document.documentElement.dataset.theme='dark';}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>"""

def nav(active):
    links = []
    for key, href, label in NAV_ITEMS:
        cur = ' aria-current="page"' if key == active else ""
        links.append(f'    <a href="{href}"{cur}>{label}</a>')
    links = "\n".join(links)
    return f"""
<nav class="site-nav">
  <a class="nav-logo" href="index.html">DIGITAL MFG <em>&amp; ED</em></a>
  <div class="nav-links">
{links}
    <button class="theme-toggle" data-theme-toggle aria-label="Toggle light or dark theme">
      <span class="light-label">◑ Dark</span><span class="dark-label">◐ Light</span>
    </button>
  </div>
</nav>"""

FOOTER = """
<footer>
  <div>
    <div class="footer-logo">DIGITAL MFG <em>&amp; ED</em></div>
    <div class="footer-sub">Stauffer Middle School · Downey Unified · Fall 2026<br>18-week course · measure → model → make</div>
  </div>
  <div class="footer-cols">
    <div class="footer-col">
      <h5>Units</h5>
      <a href="unit-1.html">U1 · Foundations</a>
      <a href="unit-2.html">U2 · CAD in Onshape</a>
      <a href="unit-3.html">U3 · The Fingerboard</a>
      <a href="unit-4.html">U4 · Laser &amp; Rack</a>
      <a href="unit-5.html">U5 · Capstone</a>
    </div>
    <div class="footer-col">
      <h5>Reference</h5>
      <a href="lab-reference.html">Lab &amp; safety</a>
      <a href="glossary.html">Glossary</a>
      <a href="resources.html">Pacing &amp; rubrics</a>
    </div>
  </div>
</footer>

<script src="assets/theme.js" defer></script>
</body>
</html>
"""

def write(name, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(body)
    print("wrote", name)

# ---------- UNIT DATA ----------
UNITS = [
  {"n":1,"slug":"unit-1.html","color":"--draw","prev":("index.html","← Home","Course overview"),
   "next":("unit-2.html","Next →","U2 · CAD in Onshape"),
   "eyebrow":"Unit 1 · Weeks 1–3","title":"Foundations:<br>Measure &amp; Sketch",
   "intro":"Before anything gets printed or cut, you learn to <strong>measure precisely</strong> and <strong>draw clearly</strong>. These three weeks build the two habits the whole course depends on — calipers in your hand and dimensions on your page — and end with your first laser-cut object.",
   "weeks":[
     {"w":"Week 1","meta":"Aug 13–14 · Measurement log","title":"Measurement &amp; Calipers",
      "make":"You learn to read <b>dial and digital calipers</b> to a thousandth of an inch — the skill the whole course rests on.",
      "obj":["Read both a dial and a digital caliper to 0.001 in.","Use the right caliper jaws for a thickness, an outside diameter, a depth, and an inside opening.","Zero the tool, square the jaws, and measure with light, consistent pressure.","Switch a digital caliper between inches and millimeters."],
      "idea":"<strong>A part is only as good as your ability to measure it.</strong> From now on the calipers never go back in the drawer — you'll check every print and every laser cut for the rest of the semester.",
      "tag":"Log","del":"Completed measurement log + two reflection sentences <strong>(10 pts)</strong>"},
     {"w":"Week 2","meta":"Aug 17–21 · Dimensioned drawing","title":"Sketching &amp; Dimensioning",
      "make":"You turn a real object into a <b>dimensioned multiview drawing</b> — front, top, and side — plus an isometric view.",
      "obj":["Draw the three standard views (front, top, side) in correct projection.","Add an isometric view to show the object in 3D.","Dimension each feature once, using extension and dimension lines.","Add a title block: your name, the object, the date, and the units."],
      "idea":"This is the shared language of engineering drawings — <strong>dimension once, clearly</strong>, so anyone can build the part from your page.",
      "tag":"Drawing","del":"Dimensioned multiview + isometric drawing <strong>(10 pts)</strong>"},
     {"w":"Week 3","meta":"Aug 24–28 · Build + fit check","title":"Fingerboard Display Stand",
      "make":"Your <b>first laser-cut object</b>: a chipboard stand that holds a fingerboard, cut from one shared Onshape master file.",
      "obj":["Read a flat (2D) layout and picture how scored folds become a 3D object.","Tell cut lines apart from score lines on a laser file.","Assemble the stand and check that the fingerboard actually fits.","Explain why a fold needs a score line, not a cut."],
      "idea":"Your teacher runs the laser — you design and fit. This is the first <strong>make → measure → fit</strong> loop, and a preview of the press-fit joints you'll cut in Unit 4.",
      "tag":"Build","del":"Assembled stand + fit check <strong>(graded as completion)</strong>"},
   ]},
  {"n":2,"slug":"unit-2.html","color":"--cad","prev":("unit-1.html","← Prev","U1 · Foundations"),
   "next":("unit-3.html","Next →","U3 · The Fingerboard"),
   "eyebrow":"Unit 2 · Weeks 4–7","title":"CAD in Onshape",
   "intro":"You move from paper to the screen — the first time the computer, not a caliper, holds your dimensions. You'll learn <strong>parametric CAD</strong> in Onshape, print your first real part, and design a skateboard you'll later shrink into your fingerboard.",
   "weeks":[
     {"w":"Week 4","meta":"Aug 31–Sep 4 · Onshape Unit 1","title":"Welcome to Onshape",
      "make":"You learn parametric CAD by working through Onshape's Intro to CAD (lessons 1.1–1.4) on a shared model.",
      "obj":["Navigate the Onshape interface and set your workspace units to inches.","Sketch, extrude, and edit features to build a simple part.","Check a part for interference — where two things overlap.","See how a 2D drawing comes from a 3D model."],
      "idea":"Set your units to inches first — same as your calipers. A <strong>measurement bridge</strong> entry ties an on-screen dimension to a real caliper reading, so CAD and the physical world stay connected.",
      "tag":"CAD","del":"Onshape Unit 1 (1.1–1.4) + measurement bridge <strong>(45 pts)</strong>"},
     {"w":"Week 5","meta":"Sep 7–11 · Cube + accuracy log","title":"First Print: Calibration Cube",
      "make":"You model a 2.000 in cube, your teacher prints it, and you measure how close the machine actually got.",
      "obj":["Model a precise 2.000 in cube and export it for printing.","Measure the printed cube on every axis with calipers.","Calculate deviation: measured size minus designed size.","Explain why a real machine never makes exactly what you draw."],
      "idea":"This is where <strong>tolerance</strong> begins — the gap between the size you asked for and the size you got. The whole capstone is built on managing that gap.",
      "tag":"Print","del":"Calibration cube + accuracy log <strong>(20 pts)</strong>"},
     {"w":"Weeks 6–7","meta":"Sep 14–25 · Onshape Unit 2","title":"Designing a Skateboard",
      "make":"Over two weeks you work through Onshape Unit 2 (2.1–2.4) and design a skateboard — the model you'll shrink into your fingerboard deck.",
      "obj":["Build a multi-feature part with sketches, extrudes, and a revolve.","Use mates and degrees of freedom to assemble parts.","Place mounting holes where the hardware actually goes.","Explain why hole placement decides whether the trucks fit."],
      "idea":"Mates and revolves are the exact skills the capstone teams use to <strong>snap park sections together</strong> and shape ramps and bowls.",
      "tag":"CAD","del":"Onshape Unit 2 (2.1–2.4) + bolt-hole note <strong>(45 pts)</strong>"},
   ]},
  {"n":3,"slug":"unit-3.html","color":"--print","prev":("unit-2.html","← Prev","U2 · CAD in Onshape"),
   "next":("unit-4.html","Next →","U4 · Laser &amp; Rack"),
   "eyebrow":"Unit 3 · Weeks 8–11","title":"The Fingerboard",
   "intro":"Now the hero object gets real. You design the <strong>96 × 32 mm deck</strong> for printing, print it and fit real trucks in millimeters, customize and ride-test it, then produce a proper working drawing.",
   "weeks":[
     {"w":"Week 8","meta":"Sep 28–Oct 2 · DFP checklist","title":"Design for Printing",
      "make":"You prepare your deck model to actually print well — and learn the conversion that makes the metric deck possible.",
      "obj":["Apply 1 in = 25.4 mm to move between inch and millimeter dimensions.","Apply the clearance rule: a hole = peg + clearance, so parts fit.","Spot and fix print problems — overhangs, thin walls, tiny features.","Build a design-for-printing checklist for your deck."],
      "idea":"<strong>Too tight = interference, too loose = slop.</strong> Clearance is how you land in between — the same idea you'll use for truck fit, kerf, and the capstone.",
      "tag":"Checklist","del":"Design-for-printing checklist <strong>(20 pts)</strong>"},
     {"w":"Week 9","meta":"Oct 5–9 · Working fingerboard","title":"Print the Deck + Fit the Trucks",
      "make":"Your teacher prints your 96 × 32 mm deck. You mount real trucks and wheels — measuring in millimeters — and log the fit.",
      "obj":["Switch your digital caliper to millimeters to measure real hardware.","Check that the printed truck-holes match the trucks, and fix them if not.","Assemble a working fingerboard with trucks and wheels.","Log the fit: what was tight, what was loose, what you'd change."],
      "idea":"This is the metric standard paying off: the 96 × 32 mm deck meets real trucks, and the <strong>inch→mm conversion</strong> from Week 8 becomes load-bearing.",
      "tag":"Build","del":"Working fingerboard + fit log <strong>(25 pts)</strong>"},
     {"w":"Week 10","meta":"Oct 12–16 · Customized deck","title":"Now Shred! — Customize &amp; Ride-Test",
      "make":"You customize your deck — graphics, shape, concave — your teacher reprints it, and you ride-test the result.",
      "obj":["Modify your deck model for grip, shape, or personal graphics.","Predict how a change will affect the ride before printing.","Ride-test the customized deck and compare to your prediction.","Log what worked and what you'd change next."],
      "idea":"Iteration in action: change one thing, test it, keep what works. <strong>That loop is the heart of engineering design.</strong>",
      "tag":"Build","del":"Customized deck + ride-test log <strong>(20 pts)</strong>"},
     {"w":"Week 11","meta":"Oct 19–23 · Working drawing","title":"Working Drawing of the Deck",
      "make":"You produce a complete, dimensioned working drawing of your deck — the kind a manufacturer could build from.",
      "obj":["Generate orthographic views straight from your Onshape model.","Dimension every feature once, clearly, with sensible tolerances.","Add a title block and any notes a builder would need.","Read your own drawing back to check nothing's missing."],
      "idea":"This closes the loop from Week 2's hand drawing — <strong>same language, now generated from a real 3D model.</strong>",
      "tag":"Drawing","del":"Working drawing of the deck <strong>(20 pts)</strong>"},
   ]},
  {"n":4,"slug":"unit-4.html","color":"--laser","prev":("unit-3.html","← Prev","U3 · The Fingerboard"),
   "next":("unit-5.html","Next →","U5 · Capstone"),
   "eyebrow":"Unit 4 · Weeks 12–13","title":"Laser &amp; Rack",
   "intro":"Two weeks on the lasers. You learn how a laser actually cuts, measure the <strong>kerf</strong> it removes, then use that number to design a press-fit plywood rack for your fingerboards. Your teacher operates both lasers — you design and measure.",
   "weeks":[
     {"w":"Week 12","meta":"Oct 26–30 · Kerf &amp; settings card","title":"How the Laser Works: Capabilities &amp; Kerf",
      "make":"You learn what each laser can and can't do, then measure the <b>kerf</b> — the width of material the beam removes.",
      "obj":["Explain how a laser cuts, scores, and engraves (vector vs. raster).","Choose the right machine for a material using the rule of thumb.","Predict, then measure, the kerf from a teacher-cut coupon (drawn − measured).","Record a kerf &amp; settings card you'll reuse next week."],
      "idea":"Kerf is tolerance for the laser: the beam always removes a little material, so a slot cut to the exact size comes out too big. <strong>You design around it.</strong> Note the two lasers differ — the LC40 cuts clear and colored acrylic; the Ador cuts dark/black acrylic only.",
      "tag":"Card","del":"Kerf &amp; settings card <strong>(20 pts)</strong>"},
     {"w":"Week 13","meta":"Nov 2–6 · Rack + fit log","title":"Fingerboard Rack",
      "make":"You design a slot-together plywood rack that holds your fingerboards — using your Week 12 kerf so the joints press-fit with no glue.",
      "obj":["Caliper the plywood thickness and an assembled fingerboard.","Apply slot width = plywood thickness − kerf for a glue-free press-fit.","Lay out a simple rack that fits the laser bed and the plywood sheet.","Press-fit it, load your boards, and log one change."],
      "idea":"Tab-and-slot joints press-fit when each slot is cut narrower than the plywood by the measured kerf — a direct preview of the <strong>capstone's press-fit connections.</strong>",
      "tag":"Build","del":"Fingerboard rack + fit log <strong>(20 pts)</strong>"},
   ]},
  {"n":5,"slug":"unit-5.html","color":"--cap","prev":("unit-4.html","← Prev","U4 · Laser &amp; Rack"),
   "next":("index.html","Home →","Course overview"),
   "eyebrow":"Unit 5 · Weeks 14–18","title":"Capstone:<br>Skate Park",
   "intro":"Everything comes together. <strong>Twelve teams of three</strong> design and build one connected skate park — each section printed to a shared <strong>connection standard</strong> so the pieces actually fit together. The capstone is graded as one project worth <strong>100 points</strong>, and the grade closes this fall.",
   "weeks":[
     {"w":"Week 14","meta":"Nov 9–13 · Brief + connection standard","title":"Capstone Launch",
      "make":"Your team gets the brief and agrees on a <b>connection standard</b> — the shared peg size, spacing, and clearance every section must use so they all connect.",
      "obj":["Understand the brief: 12 teams, one connected park.","Agree a connection standard (peg = hole − clearance) with your team.","Claim your section and sketch the idea.","Record the standard so every teammate builds to it."],
      "idea":"A connection standard is <strong>tolerance for a whole class</strong>: if everyone uses the same peg-and-clearance, twelve separately-built sections snap together.",
      "tag":"Capstone","del":"Connection standard + section plan <strong>(part of 100 pts)</strong>"},
     {"w":"Week 15","meta":"Nov 16–20 · Section models + drawing","title":"Capstone Design",
      "make":"You model your section to the standard and produce an assembly drawing. <b>Files are due before Thanksgiving</b> so they print over the break.",
      "obj":["Model your section at real scale, designed for printing, within the 180 mm bed.","Build the connection features exactly to the team standard.","Produce a section + assembly working drawing.","Submit print-ready files before the break."],
      "idea":"Each section caps at <strong>180 mm</strong> so it fits the printer bed; the connectors use the clearance rule so neighboring sections mate. Thanksgiving is the main print window.",
      "tag":"Capstone","del":"Section models + drawing <strong>(part of 100 pts)</strong>"},
     {"w":"Week 16","meta":"Nov 30–Dec 4 · Fit check","title":"Fit &amp; Iterate",
      "make":"Printed sections come back from the break. Your team fits them together, finds what doesn't mate, and iterates.",
      "obj":["Caliper the printed connectors and test the fit between sections.","Diagnose interference (too tight) or slop (too loose).","Adjust the model and reprint only the parts that need it.","Log each change and why you made it."],
      "idea":"This is the tolerance spine's payoff — <strong>real parts, real fit, real iteration</strong>, across a whole class's worth of sections.",
      "tag":"Capstone","del":"Fit-tested section + change log <strong>(part of 100 pts)</strong>"},
     {"w":"Week 17","meta":"Dec 7–11 · Protected buffer","title":"Assemble",
      "make":"Teams join their sections into the full park and solve the last connection problems. This week is a protected buffer for reprints and fixes.",
      "obj":["Connect your section to your neighbors' to the shared standard.","Solve last-mile fit issues across team boundaries.","Finish at least one printed, fit-tested section per team.","Prepare the park for the showcase."],
      "idea":"The buffer exists because real builds run long — and because the same students return in spring to finish any remaining sections.",
      "tag":"Capstone","del":"Assembled, connected sections <strong>(part of 100 pts)</strong>"},
     {"w":"Week 18","meta":"Dec 14–18 · Showcase; grades close","title":"Showcase &amp; Reflection",
      "make":"The class shows off the finished park. You reflect on tolerance, iteration, and what your team would change.",
      "obj":["Present your section and how it connects to the whole park.","Explain a tolerance decision your team made, and why.","Reflect on what worked, what didn't, and what you'd change.","Close out your OneNote portfolio for the semester."],
      "idea":"One fingerboard became a whole skate park — and the same idea, <strong>tolerance</strong>, runs from your Week 1 caliper reading to this final connection.",
      "tag":"Capstone","del":"Showcase + reflection — completes the <strong>100-pt capstone</strong>"},
   ]},
]

def render_unit(u):
    lessons = []
    for wk in u["weeks"]:
        objs = "\n".join(f"        <li>{o}</li>" for o in wk["obj"])
        lessons.append(f"""
  <article class="lesson" style="--c:var({u['color']})">
    <div class="lesson-body">
      <div class="lesson-top">
        <span class="lesson-num">{wk['w']}</span>
        <span class="lesson-meta">{wk['meta']}</span>
      </div>
      <h2 class="lesson-title">{wk['title']}</h2>
      <p class="lesson-make">{wk['make']}</p>
      <h4>You will be able to</h4>
      <ul class="obj-list">
{objs}
      </ul>
      <p class="idea">{wk['idea']}</p>
      <div class="deliverable"><span class="tag">{wk['tag']}</span> {wk['del']}</div>
    </div>
  </article>""")
    ph, pl, pn = u["prev"]
    nh, nl, nn = u["next"]
    title_plain = u["title"].replace("<br>", " ")
    body = head(f"Unit {u['n']} · {title_plain} — Digital Manufacturing & Engineering Design",
                f"Unit {u['n']} of an 18-week middle school course in digital manufacturing and engineering design.")
    body += nav(f"u{u['n']}")
    body += f"""
<header class="unit-hero" style="--c:var({u['color']})">
  <div class="unit-eyebrow">{u['eyebrow']}</div>
  <h1 class="unit-title">{u['title']}</h1>
  <p class="unit-intro">{u['intro']}</p>
</header>

<div class="lessons">
{''.join(lessons)}
</div>

<nav class="unit-nav">
  <a href="{ph}"><span class="un-label">{pl}</span><span class="un-name">{pn}</span></a>
  <a class="next" href="{nh}"><span class="un-label">{nl}</span><span class="un-name">{nn}</span></a>
</nav>
"""
    body += FOOTER
    write(u["slug"], body)

for u in UNITS:
    render_unit(u)

# ---------- LAB REFERENCE ----------
def machines_block():
    return """
  <div class="machines-grid">
    <div class="machine-card" style="--c:var(--print)">
      <div class="mc-type">3D Printer · FDM</div><div class="mc-name">Bambu Lab P1S</div>
      <div class="mc-spec">Bambu Studio · PLA · 0.2 mm</div>
      <div class="mc-desc">The course workhorse — every print, from the calibration cube to the capstone sections.</div>
    </div>
    <div class="machine-card" style="--c:var(--laser)">
      <div class="mc-type">Laser · CO&#8322; 40 W</div><div class="mc-name">Dremel LC40</div>
      <div class="mc-spec">~20 × 12 in bed · manual focus</div>
      <div class="mc-desc">The heavy cutter: thicker and faster, and the only machine that cuts <b>clear and colored acrylic</b>. Runs Dremel's own software (not LightBurn). Discontinued — treat it as irreplaceable.</div>
    </div>
    <div class="machine-card" style="--c:var(--laser)">
      <div class="mc-type">Laser · Diode 20 W</div><div class="mc-name">Flux Ador</div>
      <div class="mc-spec">~16.9 × 11.8 in · autofocus · air assist</div>
      <div class="mc-desc">The finer-detail engraver. Cuts wood, plywood (~3 mm), leather, card, fabric, and <b>dark/black acrylic only</b> — no clear, no color printing. Beam Studio native; LightBurn via bridge cable.</div>
    </div>
    <div class="machine-card muted" style="--c:var(--cnc)">
      <div class="mc-type">CNC Router</div><div class="mc-name">X-Carve Pro 4×2</div>
      <div class="mc-spec">Easel</div>
      <div class="mc-desc">In the lab, but <b>not used in this course</b> — an optional teacher demo only.</div>
    </div>
  </div>
  <div class="rule-box">
    <h4>Which laser?</h4>
    <ul>
      <li><b>Clear or colored acrylic</b> → LC40 only. The Ador's diode wavelength can't cut it.</li>
      <li><b>Wood, plywood, leather, card, or dark material</b> → either machine.</li>
      <li><b>Thicker or faster cutting</b> → LC40.</li>
    </ul>
  </div>"""

lab = head("Lab Reference — Digital Manufacturing & Engineering Design",
           "Lab reference: machines, the laser rule of thumb, measurement standards, and safety rules.")
lab += nav("lab")
lab += f"""
<header class="unit-hero" style="--c:var(--laser)">
  <div class="unit-eyebrow">Reference · For the single operator</div>
  <h1 class="unit-title">Lab Reference</h1>
  <p class="unit-intro">The teacher operates every machine; students design and measure but never run a printer or a laser. This page is the quick reference for the lab — the machines, which one to reach for, the measurement standards, and the standing safety rules.</p>
</header>

<section class="section">
  <div class="section-label">The lab</div>
  <h2 class="section-headline">Machines &amp; who runs them</h2>
  {machines_block()}
</section>

<section class="prose">
  <div class="section-label">Measurement</div>
  <h2 class="section-headline" style="margin-bottom:1rem;">How we measure</h2>
  <p><strong>Inches are the default.</strong> The course measures in inches with calipers in every unit; the dial and digital calipers from Week 1 never go back in the drawer.</p>
  <p><strong>Millimeters where the part is metric.</strong> The fingerboard deck and its holes (Week 9), the working drawing (Week 11), the laser kerf and rack (Weeks 12–13), and the capstone connection standard are all in mm.</p>
  <p><strong>1 in = 25.4 mm</strong> is taught in Week 8 and used for real in Week 9, when the 96 × 32 mm deck meets real trucks. The digital caliper's in/mm toggle, introduced in Week 1, becomes load-bearing there.</p>
  <p><strong>The refrain, all semester:</strong> too tight = interference, too loose = slop. Clearance, kerf, and the capstone connection standard are all ways of landing in between.</p>
</section>

<section>
  <div class="prose"><div class="section-label">Safety</div><h2 class="section-headline">The standing rules</h2></div>
  <div class="safety-grid">
    <div class="safety-card" style="--c:var(--print)">
      <h4>3D printer</h4>
      <ul>
        <li>The nozzle (~200 °C) and bed are hot during and just after a print — students never reach into the machine.</li>
        <li>The teacher removes parts with the proper tool; the build area stays ventilated.</li>
        <li>No student touches the printer mid-print. The single-operator rule is the safety rule.</li>
      </ul>
    </div>
    <div class="safety-card" style="--c:var(--laser)">
      <h4>Lasers</h4>
      <ul>
        <li>The teacher operates both lasers; students never run them.</li>
        <li>Fume extraction runs the whole time and the lid stays closed while cutting.</li>
        <li>Approved materials only — never PVC, vinyl, or unknown plastics; they release toxic gas.</li>
        <li>Laser + wood or paper is a fire risk: never leave a job unattended, keep the bed clear, keep the extinguisher accessible.</li>
      </ul>
    </div>
  </div>
</section>
"""
lab += FOOTER
write("lab-reference.html", lab)

# ---------- GLOSSARY ----------
GLOSS = [
  ("Tolerance","--draw","Wk 5","The allowed difference between the size you design and the size a machine actually makes. Managing tolerance is the spine of the whole course."),
  ("Interference","--draw","Wk 5","When two parts overlap and won't fit — <b>too tight</b>. The opposite of slop."),
  ("Slop","--draw","Wk 5","When a fit is <b>too loose</b> and wobbles. The opposite of interference; you aim to land between the two."),
  ("Clearance","--print","Wk 8","Extra space added on purpose so parts fit: a hole = peg + clearance. How you avoid both interference and slop."),
  ("Deviation","--cad","Wk 5","Measured size minus designed size — how far off the machine was. You log it for the calibration cube."),
  ("Caliper","--draw","Wk 1","A precision tool that reads thickness, diameter, depth, and inside openings to a thousandth of an inch. It never leaves your side."),
  ("Dial vs. digital caliper","--draw","Wk 1","Two caliper types you'll read. The digital one toggles between inches and millimeters."),
  ("Parametric CAD","--cad","Wk 4","Computer-aided design where dimensions drive the model — change a number and the part updates. You use Onshape."),
  ("Onshape","--cad","Wk 4","The browser-based CAD tool for the course. You set your units to inches to match your calipers."),
  ("Sketch","--cad","Wk 4","A 2D outline on a plane that you turn into 3D with features like extrude and revolve."),
  ("Extrude","--cad","Wk 4","Pushing a 2D sketch into 3D to give it thickness."),
  ("Revolve","--cad","Wk 6","Spinning a sketch around an axis to make round shapes — how a ramp or bowl gets formed."),
  ("Mate","--cad","Wk 6","A relationship that joins parts in an assembly and controls how they move."),
  ("Degrees of freedom","--cad","Wk 6","The ways a part can still move after it's mated — the capstone teams use mates and DOF to connect sections."),
  ("Interference (CAD)","--cad","Wk 4","A check in CAD that finds where two bodies overlap before you ever print."),
  ("Measurement bridge","--cad","Wk 4","A notebook/CAD entry that links an on-screen dimension to a real caliper reading, keeping the model honest."),
  ("Orthographic views","--draw","Wk 2","The straight-on front, top, and side views of an object, drawn in correct projection."),
  ("Isometric view","--draw","Wk 2","A single 3D-looking view that shows three faces at once."),
  ("Multiview drawing","--draw","Wk 2","A drawing that combines the orthographic views plus dimensions and a title block."),
  ("Title block","--draw","Wk 2","The labeled corner of a drawing: name, object, date, and units."),
  ("Working drawing","--print","Wk 11","A complete, dimensioned drawing a manufacturer could build the part from — generated from your model."),
  ("FDM","--print","Wk 5","Fused Deposition Modeling — the 3D-printing method the Bambu P1S uses, laying down melted plastic layer by layer."),
  ("PLA","--print","Wk 5","The plastic filament used for printing — the house default at a 0.2 mm layer height."),
  ("Slicer","--print","Wk 5","Software (Bambu Studio) that turns a 3D model into machine instructions and estimates print time."),
  ("Design for printing","--print","Wk 8","Adjusting a model so it prints reliably — managing overhangs, thin walls, and tiny features."),
  ("Vector vs. raster","--laser","Wk 12","A laser cuts/scores along vector lines and engraves images as a raster (row-by-row) pattern."),
  ("Score","--laser","Wk 3","A shallow laser line that lets material fold without being cut through — how the display stand bends."),
  ("Kerf","--laser","Wk 12","The width of material the laser beam burns away. A slot cut to the exact size comes out too big — so you design around it."),
  ("Press-fit (tab-and-slot)","--laser","Wk 13","A joint that holds with no glue because the slot is cut narrower than the material by the measured kerf."),
  ("Connection standard","--cap","Wk 14","The shared peg size, spacing, and clearance every capstone team builds to, so 12 sections snap together."),
  ("Capstone","--cap","Wk 14","The final project: twelve teams build one connected skate park, graded as a single 100-point project."),
  ("Single-operator loop","--cad","Wk 5","The course rhythm: you design in class, the teacher runs the machine between sessions, you measure and iterate next time."),
]
gl = head("Glossary — Digital Manufacturing & Engineering Design",
          "Glossary of key terms for the course, from tolerance and clearance to kerf and the connection standard.")
gl += nav("glossary")
gl += """
<header class="unit-hero" style="--c:var(--cad)">
  <div class="unit-eyebrow">Reference · Key terms</div>
  <h1 class="unit-title">Glossary</h1>
  <p class="unit-intro">The vocabulary that runs through the course — the words for measuring precisely, modeling in CAD, and making parts that actually fit. Each term notes the week it first shows up.</p>
</header>
<div class="gloss-wrap">
"""
for term, color, wk, defn in GLOSS:
    gl += f"""  <div class="gloss" style="--c:var({color})">
    <div class="gloss-week">{wk}</div>
    <div class="gloss-term">{term}</div>
    <div class="gloss-def">{defn}</div>
  </div>
"""
gl += "</div>\n" + FOOTER
write("glossary.html", gl)

# ---------- RESOURCES ----------
SPINE = [
  ("1","Aug 13–14","Measurement &amp; calipers — caliper log","—","10"),
  ("2","Aug 17–21","Orthographic + isometric sketching","—","10"),
  ("3","Aug 24–28","Fingerboard display stand (laser-cut)","Laser","completion"),
  ("4","Aug 31–Sep 4","Welcome to Onshape (Unit 1, 1.1–1.4)","Onshape","45"),
  ("5","Sep 7–11","First print: 2.000 in calibration cube","Bambu","20"),
  ("6–7","Sep 14–25","Designing a skateboard (Unit 2, 2.1–2.4)","Onshape","45"),
  ("8","Sep 28–Oct 2","Design for printing (deck prep)","Onshape","20"),
  ("9","Oct 5–9","Print the deck + fit the trucks (mm)","Bambu","25"),
  ("10","Oct 12–16","Now Shred! — customize + ride-test","Onshape+Bambu","20"),
  ("11","Oct 19–23","Working drawing of the deck","Onshape","20"),
  ("12","Oct 26–30","How the laser works: capabilities &amp; kerf","Laser","20"),
  ("13","Nov 2–6","Fingerboard rack (laser-cut plywood)","Laser","20"),
  ("14","Nov 9–13","Capstone launch: brief + connection standard","Onshape","—"),
  ("15","Nov 16–20","Capstone design: section models + drawing","Onshape","—"),
  ("—","Nov 23–27","Thanksgiving — main capstone print window","Bambu","—"),
  ("16","Nov 30–Dec 4","Capstone fit &amp; iterate","Bambu","—"),
  ("17","Dec 7–11","Capstone assemble (protected buffer)","Bambu","—"),
  ("18","Dec 14–18","Capstone showcase + reflection; grades close","—","100"),
]
spine_rows = "\n".join(
  f'      <tr><td class="num">{w}</td><td>{d}</td><td>{t}</td><td>{m}</td><td class="num">{p}</td></tr>'
  for (w,d,t,m,p) in SPINE)

GRADES = [
  ("1","Measurement log + reflection","10"),("2","Dimensioned multiview drawing","10"),
  ("3","Display stand (build + fit check)","completion"),("4","Onshape Unit 1 + measurement bridge","45"),
  ("5","Calibration cube + accuracy log","20"),("6–7","Onshape Unit 2 + bolt-hole note","45"),
  ("8","Design-for-printing checklist","20"),("9","Working fingerboard + fit log","25"),
  ("10","Customized deck + ride-test log","20"),("11","Working drawing of the deck","20"),
  ("12","Kerf &amp; settings card","20"),("13","Fingerboard rack + fit log","20"),
  ("14–18","Capstone: skate park (one project grade)","100"),
]
grade_rows = "\n".join(
  f'      <tr><td class="num">{w}</td><td>{d}</td><td class="num">{p}</td></tr>'
  for (w,d,p) in GRADES)

res = head("Resources — Digital Manufacturing & Engineering Design",
           "Pacing guide, grading at a glance, and the student documentation system (engineering notebook + OneNote).")
res += nav("resources")
res += f"""
<header class="unit-hero" style="--c:var(--cap)">
  <div class="unit-eyebrow">For teachers · Pacing · Rubrics · Documentation</div>
  <h1 class="unit-title">Resources</h1>
  <p class="unit-intro">The pacing guide, the grading totals, and how students document their work. The detailed teacher's guide and the student documentation handout are kept as separate documents.</p>
</header>

<section class="prose">
  <div class="section-label">Pacing</div>
  <h2 class="section-headline" style="margin-bottom:1rem;">The 18-week spine</h2>
  <p>Anchored to the real first-semester calendar. Meeting weeks vary with holidays; the four no-class windows (Labor Day, the Oct 12 staff-development Monday, Veterans Day, and the nine-day Thanksgiving break) are the main print windows.</p>
  <table class="ref-table">
    <thead><tr><th class="num">Wk</th><th>Dates</th><th>Topic / what gets made</th><th>Machine</th><th class="num">Pts</th></tr></thead>
    <tbody>
{spine_rows}
    </tbody>
  </table>
</section>

<section class="prose">
  <div class="section-label">Grading</div>
  <h2 class="section-headline" style="margin-bottom:1rem;">Grading at a glance</h2>
  <p>Twelve graded deliverables plus the 100-point capstone. Week 3 is graded as completion (no point rubric in its deck).</p>
  <table class="ref-table">
    <thead><tr><th class="num">Wk</th><th>Deliverable</th><th class="num">Points</th></tr></thead>
    <tbody>
{grade_rows}
      <tr class="total"><td class="num">—</td><td>Graded total</td><td class="num">255 + capstone 100</td></tr>
    </tbody>
  </table>
</section>

<section class="prose">
  <div class="section-label">Documentation</div>
  <h2 class="section-headline" style="margin-bottom:1rem;">How students document their work</h2>
  <p>Students keep two records that feed a third. The <strong>paper engineering notebook</strong> is where thinking happens — sketches, raw caliper readings, quick math. <strong>OneNote</strong> is the curated portfolio: cleaned-up evidence for each deliverable. <strong>Canvas</strong> is where the graded version is turned in. The notebook feeds OneNote; OneNote feeds Canvas.</p>
  <h3>The four-part OneNote page</h3>
  <p>Every deliverable lands as one OneNote page on the same template: <strong>the design</strong> (drawing or CAD screenshot), <strong>the made part</strong> (a photo, caliper in frame), <strong>designed vs. measured</strong> (the numbers), and a short <strong>reflection</strong> (what you'd change).</p>
  <h3>The engineering notebook</h3>
  <p>Set it up in Week 1 — numbered pages, a table of contents, dated entries — and keep it all semester. It's the one rail students never hand in; it's for thinking, not neatness. The polished version of any entry gets copied into OneNote.</p>
</section>

<div style="height:2rem"></div>
"""
res += FOOTER
write("resources.html", res)

print("DONE")
