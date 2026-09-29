#!/usr/bin/env python3
"""Builds Shotlist_Ramadan.html from the locked scenes, then the PDF is rendered with
shotlist-builder/tools/render_pdf.sh. Append a new entry to SCENES as each scene locks.
Template: ~/.claude/skills/shotlist-builder/templates/PDF_TEMPLATE.md"""
import datetime, pathlib

HERE = pathlib.Path(__file__).parent
TODAY = "2026-09-27"

PROJECT = "رمضان — Saudi Ramadan Stock Album"
PREPARED_FOR = "Laqta Albums · Bido Visuals"

MODEL = ("Seedance 2.5 · omni_reference · set in UI: 16:9 · 1080p · duration per shot "
         "(max 30 s) · generate_audio ON")

STYLE_PREFIX = (
    "Photoreal premium Saudi Ramadan TV-commercial cinema, 8K IMAX register, shot on physical "
    "cinema lenses with true perspective and straight lines. Cinematography in the manner of "
    "Emmanuel Lubezki and Roger Deakins. Every light in frame comes from a practical source "
    "visible in the scene; light direction and contrast follow the scene's lighting block. "
    "Colour follows the scene's 60:30:10 hour palette. 180-degree shutter "
    "motion blur, 24 fps cinematic cadence. Skin carries pore-level realism — fine hair, "
    "uneven tone, capillary flush, pore shadows matching the practical light. Eyes are wet and "
    "alive with catchlights; breath is visible; every reaction has a micro-pause before it; "
    "every gaze holds a target inside the scene. Real weight and inertia, grounded contact "
    "shadows. Composition on thirds and the golden ratio; everyone already moving at frame 1. "
    "Characters, props and location identical to their references in every shot. "
    "One continuous shot, no montage, no cutaways, no flashbacks, no cinematic transitions. "
    "Audio: complete diegetic sound effects only — everything heard is what a microphone "
    "standing in the scene would pick up. NO BGM. 16:9."
)
STYLE_NOTE = ("Adapted from shotlist-builder STYLE_BLOCK.md (base block) for this project: "
              "16:9 not 21:9 · duration set per shot in the UI, not in the footer · haze set per "
              "scene, not everywhere · 24 fps cinematic, not 60 fps · written in positive form for "
              "the stage-4 audit · the anti-cut line is the film-workflow U1 block, verbatim. "
              "Stage 3b renders it in the prompt's language.")

RULES = [
    "ONE RENDER = ONE CONTINUOUS SHOT = ONE ACTION. Every row is its own generation "
    "(overrides the skill's 15-second multi-shot groups).",
    "No 1-second establishing wide per scene: renders do not share frames, so it cannot hold "
    "the layout and would be an unsellable 1-second clip. Each scene's wide shot establishes; "
    "the layout is held by the location plate + the GEO block pasted in every prompt.",
    "Complete sound effects only — no music, no melody, no speech, no voiced laugh. No أذان, "
    "recitation or تكبير in any clip.",
    "The son and the daughter are written by role, clothing and action — never an age, never "
    "boy / girl / child / kid / young / teen / little.",
    "NON-IP: no brands, no logos. Show goods that are naturally unbranded — loose, in sacks, bare glass, kraft paper — never blank boxes or labels.",
]

MUSIC = "None — no music in any clip and none planned for edit timing. Every clip ships with complete SFX."

# ---------------------------------------------------------------- assets
ASSETS = [
    ("@char_c3-father", "Character", "home sheet (bare-headed) · outdoor = + shemagh + naal",
     "Saudi father, broad through the chest, beard. White thobe with a standing mandarin collar and buttons.", "1"),
    ("@char_c5-son", "Character", "home sheet · outdoor = + naal-son",
     "The son. White thobe, mandarin collar.", "1"),
    ("@char_c6-daughter", "Character", "home sheet · outdoor = + sandals-daughter",
     "The daughter. Rose dress, long dark hair.", "1"),
    ("@loc_l1-market-day", "Location", "day · عصر · single 3/4 frame (rebuilt at 3a, 2026-09-23)",
     "Quiet Saudi supermarket aisle. Open wooden date bins with wooden scoops along the west side; white shelving "
     "along the east holding a bulk spice and coffee section — open jute sacks of cardamom, cloves, dried black limes "
     "and pale coffee beans, bare glass honey jars, kraft rice sacks; pale tile floor; overhead ceiling lights; warm "
     "spotlights over the bins. Nothing printed anywhere. Empty of people.", "1"),
    ("@prop_p1-dates", "Prop", "loose in the bins",
     "Golden سكري and darker خلاص dates, loose.", "1 · recurs all day"),
    ("@prop_p3-shemagh", "Prop", "worn",
     "Red-and-white شماغ with black عقال, fine check at true scale — the father's outdoor head.", "1"),
    ("@prop_p4-naal", "Prop", "worn", "Adult leather نعال — the father only.", "1"),
    ("@prop_p6-naal-son", "Prop", "worn", "Leather نعال sized for the son.", "1"),
    ("@prop_p7-sandals-daughter", "Prop", "worn", "Strapped leather sandals sized for the daughter.", "1"),
    ("@prop_trolley", "Prop · <b>NEW</b>", "—",
     "Plain metal supermarket trolley with a grey plastic panel, no logo. Locks the same trolley across separate renders.", "1"),
    ("@prop_date-bag", "Prop · <b>NEW</b>", "open (1.5) → knotted (from 1.6)",
     "Plain clear produce bag, no print. A knotted-state tag will be needed when it returns in scene 3.", "1 · 3"),
]

CAST = [
    ("@char_c3-father",
     "Tics: reads the light through a window or doorway to judge the hour, whenever time matters · thumb once "
     "along the beard line while weighing a choice · hands resting still on what he carries (not hurried). "
     "Eyes: calm, slow full blinks, quiet scanning, eyes reach a person before the head turns. "
     "Gait: \"provider's pace\" — long even steps, whole-foot landings. Mask → crack: composed and unhurried → "
     "before his own father he becomes a son (chin lowers, gaze drops, hands serve). Softens for: his daughter. "
     "Fasting all day: dry lips, a dry swallow.",
     "Silent in every scene — breath only.", "—", "\"the father\" — role, clothing, action"),
    ("@char_c5-son",
     "Tics: copies his father's hand movements half a beat late, without knowing · squares his shoulders when "
     "an adult's eyes are on him · attention drifts sideways when unwatched, then snaps back. "
     "Eyes: watchful, tracks adults' hands, checks his father first, quick blinks when concentrating. "
     "Gait: \"shadow walk\" — half a step behind his father, matching the stride, skipping a step to keep up. "
     "Mask → crack: borrowed grown-up composure → a grin he cannot hold when a grown-up sees him get it right. "
     "Softens for: his grandfather.",
     "Silent in every scene — breath only.", "—", "\"the son\" — never boy / child / kid / young / little; no age"),
    ("@char_c6-daughter",
     "Tics: takes a sleeve or a hand and leads, when she wants someone to see · nudges things a finger's width "
     "back to exact, when something sits off · rises on her toes while waiting for an answer. "
     "Eyes: quick, darting, reach the target before the body turns, read faces. "
     "Gait: \"scout's trot\" — short quick steps a pace ahead, turning back to check. "
     "Mask → crack: bright busy certainty → goes still and quiet when overlooked. Softens for: her father's nod.",
     "Silent in every scene — breath only.", "—", "\"the daughter\" — never girl / child / kid / young / little; no age"),
]

# ---------------------------------------------------------------- scenes
LIGHT_S1 = ("Scene-1 look LOCKED to the user's reference frame (2026-09-24): bright, clean, high-key supermarket light — rows of warm-white recessed ceiling downlights give soft, even light from above; faces fully and evenly lit; white thobes clean and bright; warm spotlights make the dates glow gold; pale glossy floor with soft reflections; soft low contrast, neutral-warm white balance. No film light.")

S1_SHOTS = [
    dict(
        num="1.1", plan="WS", plan_label="Wide shot", dur=6, speed="real-time",
        mode="R2V — elements only", frames="— (backup if the video drifts: still FF-1.1)",
        media="— (old take b57f32f8 retired 2026-09-23: it shows a different aisle)",
        context="First day of Ramadan, afternoon. The family walks the date aisle smiling and stops at the bins; the daughter shows her father one golden date.",
        action="0–3 s: the three walk toward camera, smiling · 3–4 s: they stop at the bins · 4–6 s: the daughter picks one golden date and holds it up to her father; he smiles and nods.",
        final="All three at rest at the bins — the daughter holding the date up at frame-left, the son beside her, the father smiling behind the stopped trolley.",
        lens="50mm · normal, about 47° · family sharp, far end gently soft", camera="chest height, level · axis side SOUTH · dolly back ahead of them, easing to rest as they stop (calm → smooth)",
        tags="@char_c3-father (identity) + @prop_p3-shemagh (head) + @prop_p4-naal (feet) · @char_c5-son (identity) + @prop_p6-naal-son · @char_c6-daughter (identity) + @prop_p7-sandals-daughter · @loc_l1-market-day (main view, looking north) · @prop_trolley · @prop_p1-dates",
        first="The three mid-stride about 5 m from camera: the father centre behind the trolley, the daughter a pace ahead at his right along the bins, the son half a step behind her · hands: father both on the trolley handle; the son and daughter free",
        blocking="Father x≈50%, centre of the aisle, trolley in front, facing camera (south) · daughter x≈35%, along the bins, a pace ahead · son x≈40%, half a step behind the daughter · path: straight toward camera, stopping at the bins · occlusion: son partly behind the daughter · open space: the empty aisle north behind them",
        intent="Father — get the shopping done, and glad to let his daughter stop him · tactic: keep moving → give in happily · business: the trolley",
        beats="① three walking rhythms: the daughter two quick steps to each of her father's, the son's feet landing between his sister's ② the kids grin at each other; the father smiles watching them ③ she stops; the son a beat later; the father's hands stop on the handle ④ she lifts one date up to him, beaming; the son leans in grinning ⑤ his smile widens — one small nod",
        listeners="All three active. Stops staggered 0.3–0.5 s apart — daughter, then son, then father.",
        dialogue="None. All three silent — breath only.",
        sfx="Trolley wheels rolling on tile and easing to a stop · three sets of sandal footsteps at different rhythms · the refrigeration hum · a hand moving through loose dates · music: none",
        seam="—",
        light=LIGHT_S1, atmos="Clean conditioned air, no haze. Nothing moves but the family.",
        physics="The trolley has weight — wheels roll and settle. Thobes crease and swing with each step. Contact shadows under feet and wheels.",
        scale="Exactly three people. The father tallest; the son's head at about his father's chest; the daughter slightly shorter than the son.",
        state="Baseline — trolley empty, no bag in play.",
        contin="— (first shot of the scene)",
        text="None. Loose dates, spice sacks and bare glass jars — no printed packaging in frame.",
        warn="⚠️⚠️⚠️ nobody looks at the lens · the father's شماغ ON (it vanished in an earlier take) · sandals on all three feet · the three walk out of step.",
        test="Complete action + happy faces: do all three hold identity at 47°, with the kids out of step and the backlight reading?",
    ),
    dict(
        num="1.2", plan="MS", plan_label="Medium-wide shot", dur=8, speed="real-time — normal speed, no slow motion",
        mode="R2V — elements only", frames="— (backup if the video drifts: still FF-1.2)", media="—",
        context="Complete stock moment: the daughter stops her father's trolley, shows him the dates she wants, and he happily says yes.",
        action="0–2 s: she hurries to the bin and tugs her father's sleeve; the trolley stops · 2–4 s: she points into the golden dates, bouncing on her toes, looking up at him · 4–6 s: he leans in, looks, smiles and nods clearly · 6–8 s: she claps once and hops; the son grins; the father laughs silently — at rest.",
        final="At rest: the daughter beaming at the bin, the son grinning beside her, the father smiling behind the stopped trolley.",
        lens="50mm · normal, about 47° · full figures, far end gently soft", camera="chest height · south-east of the pair · axis side SOUTH · smooth handheld, slight push-in as she points",
        tags="@char_c3-father (identity) + @prop_p3-shemagh + @prop_p4-naal · @char_c6-daughter (identity) + @prop_p7-sandals-daughter · @char_c5-son (background, soft) + @prop_p6-naal-son · @loc_l1-market-day (bin side) · @prop_trolley",
        first="The three walking toward the bins: the daughter a pace ahead at frame-left, the father behind the trolley at frame-right, the son behind them",
        blocking="Daughter frame-left x≈35%, at the bin, facing her father (east) · father frame-right x≈62%, facing south, turning west to her · 1 m apart closing to 0.5 m · son background x≈45%, 1 m behind, soft · trolley in the frame-right foreground, cut by the frame edge",
        intent="Daughter — make her father look · obstacle: he is walking on · tactic: lead him (pull) · INNER \"These ones. Look.\" · business: his sleeve. Father — keep moving → shift at her pull: indulge her · INNER \"Alright. Show me.\" · business: the trolley, interrupted",
        beats="① the tug — trolley stops ② she points and waits on her toes ③ his nod — a clear yes ④ her clap-and-hop, the son's grin, the father's silent laugh",
        listeners="The son, soft in the background: stops 0.4 s after the trolley stops; his eyes go to his father's face.",
        dialogue="None. Silent — breath only; her quick inhale as she pulls.",
        sfx="Trolley wheels scuffing to a stop · sandal steps · one hand clap · a hop landing on tile · refrigeration hum · music: none",
        seam="—",
        light=LIGHT_S1 + " Here: the bins' gold rakes across the daughter at frame-left.",
        atmos="Clean air, no haze.",
        physics="The trolley's momentum carries it a few centimetres after his hands stop. The sleeve pulls taut under her grip.",
        scale="Her head below her father's shoulder. Exactly three people; the son soft.",
        state="Trolley stopped at the bins (since 1.2).",
        contin="Overlapping coverage of the stop inside 1.1, from closer — match positions, not the exact frame.",
        text="None.",
        warn="⚠️⚠️⚠️ The trolley STOPS and stays stopped — no drift after. ⚠️ Her pull reads as a light tug, not a grab. ⚠️ Nobody looks at the lens. ⚠️ The father's شماغ on.",
        test="Real-time speed + a complete message: does the whole ask-and-yes read in 8 s without slow motion?",
    ),
    dict(
        num="1.3", plan="CU", plan_label="Close-up", dur=6, speed="real-time — natural human speed",
        mode="R2V — elements only", frames="— (backup if the video drifts: still FF-1.3)", media="—",
        context="STOCK CLIP 3 — complete on its own: in close-up, the daughter picks one golden date and holds it in front of her, smiling as she looks at it.",
        action="0–2 s: her hand picks one golden date from the bin · 2–4 s: she holds it in front of her at chest height, looking down at it · 4–6 s: a light, soft smile with closed lips — no teeth — at rest.",
        final="At rest: the date held at chest height in her fingers, her eyes on it, a light closed-lip smile.",
        lens="85mm · short telephoto, about 29° · focus on her eyes and the date", camera="her eye height · south-east of her · axis side SOUTH · smooth handheld, natural breathing",
        tags="@char_c6-daughter (identity) · @prop_p1-dates (loose in the bin) · @loc_l1-market-day (bins, soft)",
        first="Head and shoulders: the daughter at the bin, her hand reaching into the golden dates at the frame-left edge",
        blocking="She stands at the bin (frame-left edge), face three-quarter to camera · her father off-frame right, about 1 m · open space frame-right above her head, where her look goes",
        intent="Make her father choose her dates · obstacle: his mind is elsewhere · tactic: wait for the verdict, on her toes · INNER \"These ones — look.\" · business: pointing",
        beats="① she picks one date ② holds it at chest height, eyes on it ③ a light closed-lip smile at the corners of her mouth (user 2026-09-27: the wide grin read fake)",
        listeners="Her father, off-frame right — present only through her eyeline.",
        dialogue="None. Breath only — a quick inhale at ①.",
        sfx="A hand moving through loose dates · refrigeration hum · music: none",
        seam="—",
        light=LIGHT_S1 + " Here: the spot on the bin bounces gold up off the dates onto her face from below-left.",
        atmos="Clean air.",
        physics="Dates shift under her fingertip.",
        scale="Head and shoulders.",
        state="Trolley stopped at the bins (since 1.2).",
        contin="From 1.2 — she has drawn her father to the bin; her hand is off his sleeve and pointing.",
        text="None.",
        warn="⚠️⚠️⚠️ Exactly one date in her fingers · five natural fingers · her gaze goes to frame-right, never the lens · age: 'the daughter' only.",
        test="Does her face hold in close-up, with one date and a natural, happy performance at real speed?",
    ),
    dict(
        num="1.4", plan="CU", plan_label="Close-up", dur=5, speed="real-time",
        mode="R2V — elements only", frames="— (backup if the video drifts: still FF-1.4)", media="—",
        context="STOCK CLIP 4 — complete on its own: in close-up, the father smiles at his daughter and gives her the agree sign: yes, the dates are hers for Ramadan.",
        action="0–1 s: already smiling at his daughter (below camera-left) · 1–3 s: smile widens, brows lift once, small head tilt · 3–4 s: the agree sign — one nod with a brief closed-eye blink · 4–5 s: eyes reopen on her, broad warm smile, at rest.",
        final="At rest: chest up, face three-quarter, eyes on his daughter below camera-left, a broad warm smile.",
        lens="18° classic telephoto · camera 5 m · frame 1.2–2.0 m high (chest-up)", camera="lens 1.6 m high · 5 m south of him, facing north · axis side SOUTH · near-still handheld · focus on his eyes",
        tags="@char_c3-father (identity) + @prop_p3-shemagh (head) · @loc_l1-market-day (shelving, soft)",
        first="Chest-up, father at x≈60%, face three-quarter to camera, already smiling, eyes on his daughter below camera-left; bins below the frame",
        blocking="See MAP_1.4.svg · father 1.1 m east of the bins (top 0.9 m), eyes 1.7 m · daughter 1 m south-west of him at the bin edge, face 1.15 m, out of frame · his eyeline: to her the whole shot, about 25° down, camera-left",
        intent="Promise his daughter the dates · INNER \"You want these? … Done. They are yours.\" · tactic: warm teasing → the agree sign · business: hands still on the trolley",
        beats="① already smiling at her ② smile widens, brows lift once, head tilts ③ the agree sign: one nod with a closed-eye blink ④ at rest, broad warm smile (ACTING.md · SHOT 1.4, user 2026-09-27)",
        listeners="The daughter, off-frame — her reaction lives in 1.3.",
        dialogue="None. Breath only — a soft happy breath out through the nose with the nod.",
        sfx="A slow exhale through the nose · the refrigeration hum · a trolley far away · music: none",
        seam="—",
        light=LIGHT_S1 + " Here: the bins' gold wraps his cheek from frame-left.",
        atmos="Clean air.",
        physics="—",
        scale="Head and shoulders.",
        state="Trolley stopped at the bins (since 1.2).",
        contin="Overlaps 1.3 — his nod here lands at the same moment as her reaction there.",
        text="None.",
        warn="⚠️⚠️⚠️ شماغ on, its check at true scale — fine red-and-white, never gingham. ⚠️ One nod, not a series. ⚠️ Natural warm smile, lips closed — no mugging. ⚠️ Eyes never to the lens. ⚠️ The kids stay off-frame.",
        test="A happy father from frame one, a readable agree sign, eyes on his daughter, 5 s real time.",
    ),
    dict(
        num="1.5", plan="MS", plan_label="Medium shot", dur=10, speed="real-time — natural human speed",
        mode="R2V — elements only", frames="—", media="—",
        context="STOCK CLIP 2 — complete on its own: the son and daughter fill a bag of dates, and their father takes it from them with a smile and puts it in the trolley.",
        action="0–5 s: three scoops — each drops about fifteen dates into the empty bag the son holds open; the bag ends half full · 5–7 s: the son lifts the open bag to his father; he takes it, smiling at them · 7–9 s: he sets it upright in the trolley basket as it is, open · 9–10 s: all three smiling, at rest.",
        final="At rest: the open half-full bag standing in the trolley basket, visible through the wire; the father smiling at his son and daughter.",
        lens="50mm · normal, about 47° · the three sharp, the aisle behind gently soft", camera="chest height · south of the bin · axis side SOUTH · smooth handheld, natural breathing, positions held",
        tags="@char_c3-father (identity) + @prop_p3-shemagh · @char_c5-son (identity) · @char_c6-daughter (identity) · @prop_date-bag (open → full → knotted) · @prop_p1-dates (loose in the bin) · @prop_trolley · @loc_l1-market-day (bin side)",
        first="The daughter at the bin holding the wooden scoop, already dipping it into the golden dates · the son beside her holding the empty bag open with both hands · the father behind the trolley, hands on the handle, smiling at them",
        blocking="Bin along frame-left · daughter frame-left x≈28%, at the bin edge, facing the bin · son x≈45%, beside her, facing her, holding the bag over the bin edge · father frame-right x≈68%, 1 m from the son, behind the trolley, facing them · trolley in the frame-right foreground · framed from the waist up",
        intent="Daughter — fill the bag herself · Son — be useful, hold it steady · Father — let them do it, then finish the job · business: scoop, bag, knot",
        beats="① three scoops, the dates rattling in ② the son lifts the bag to his father ③ he takes it, smiling at them ④ the open bag set in the trolley — all three smiling",
        listeners="The father watches their hands, smiling, until the son lifts the bag to him.",
        dialogue="None.",
        sfx="Dates rattling off the wooden scoop · dates dropping into the plastic bag — crinkle and soft thuds · the bag knotted · the bag settling in the wire basket · refrigeration hum · music: none",
        seam="—",
        light="The spot above the bin makes the dates glow gold; the bag's plastic catches one highlight; the ceiling light behind as a soft backlight.",
        atmos="Clean air.",
        physics="Each scoop adds about fifteen dates; the bag starts empty and ends half full, the size of a large grapefruit, open at the top. It keeps that fill and lands upright in the basket with weight.",
        scale="Exactly three people, one bag, one scoop. About forty-five dates in the bag at the end. The scoop about 20 cm long.",
        state="Trolley stopped at the bins (since 1.2) · bag: empty → full → knotted and in the trolley (this shot).",
        contin="Stands alone as stock; follows 1.2 in the edit.",
        text="None — the bag is plain.",
        warn="⚠️⚠️⚠️ The bag starts EMPTY — only the dates poured on screen · the bag stays open (no knot, no seal) · it stays visible in the basket to the last frame · one bag, one scoop, five fingers.",
        test="Does the fill-and-hand-over read in 10 s at natural speed, with a believable fill and the scene's locked bright look?",
    ),
]

BLOCKING_SVG_S1 = """
<svg width="560" viewBox="0 0 680 650" xmlns="http://www.w3.org/2000/svg" style="display:block;margin:4mm 0 6mm">
<defs>
 <marker id="ag" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#5F5E5A" stroke-width="1.5"/></marker>
 <marker id="ac" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#D85A30" stroke-width="1.5"/></marker>
 <marker id="at" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#1D9E75" stroke-width="1.5"/></marker>
 <marker id="ap" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M2 1L8 5L2 9" fill="none" stroke="#7F77DD" stroke-width="1.5"/></marker>
</defs>
<g font-family="Helvetica, Arial, sans-serif">
<text x="340" y="44" text-anchor="middle" font-size="12" fill="#5F5E5A">North · far end of the store, empty</text>
<rect x="120" y="60" width="100" height="480" rx="4" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.8"/>
<text x="170" y="92" text-anchor="middle" font-size="14" font-weight="600" fill="#633806">Date bins</text>
<text x="170" y="110" text-anchor="middle" font-size="12" fill="#854F0B">warm spots</text>
<rect x="460" y="60" width="100" height="480" rx="4" fill="#F1EFE8" stroke="#888780" stroke-width="0.8"/>
<text x="510" y="92" text-anchor="middle" font-size="14" font-weight="600" fill="#444441">Shelving</text>
<text x="510" y="110" text-anchor="middle" font-size="12" fill="#5F5E5A">spice sacks</text>
<line x1="226" y1="280" x2="450" y2="280" stroke="#888780" stroke-width="0.8" stroke-dasharray="5 4"/>
<text x="432" y="268" text-anchor="middle" font-size="12" fill="#5F5E5A">axis</text>
<rect x="332" y="305" width="60" height="45" rx="4" fill="#ffffff" stroke="#888780" stroke-width="0.8"/>
<text x="362" y="332" text-anchor="middle" font-size="12" fill="#444441">trolley</text>
<line x1="248" y1="272" x2="228" y2="262" stroke="#D85A30" stroke-width="1.5" marker-end="url(#ac)"/>
<line x1="346" y1="272" x2="302" y2="256" stroke="#1D9E75" stroke-width="1.5" marker-end="url(#at)"/>
<line x1="298" y1="236" x2="338" y2="264" stroke="#7F77DD" stroke-width="1.5" marker-end="url(#ap)"/>
<circle cx="262" cy="280" r="16" fill="#FAECE7" stroke="#D85A30" stroke-width="0.8"/><text x="262" y="285" text-anchor="middle" font-size="14" font-weight="600" fill="#712B13">D</text>
<circle cx="362" cy="280" r="16" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.8"/><text x="362" y="285" text-anchor="middle" font-size="14" font-weight="600" fill="#085041">F</text>
<circle cx="285" cy="225" r="16" fill="#EEEDFE" stroke="#7F77DD" stroke-width="0.8"/><text x="285" y="230" text-anchor="middle" font-size="14" font-weight="600" fill="#3C3489">S</text>
<text x="312" y="304" text-anchor="middle" font-size="12" fill="#5F5E5A">~1 m</text>
""" + "".join(
    f'<rect x="{x}" y="{y}" width="36" height="20" rx="4" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.8"/>'
    f'<text x="{x+18}" y="{y+14}" text-anchor="middle" font-size="13" font-weight="600" fill="#2C2C2A">{n}</text>'
    f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="#5F5E5A" stroke-width="1.2" marker-end="url(#ag)"/>'
    for n, x, y, a, b, c, d in [
        ("1.1", 322, 560, 340, 556, 340, 506), ("1.2", 412, 420, 416, 418, 398, 390),
        ("1.3", 252, 400, 268, 396, 264, 304), ("1.4", 292, 440, 318, 436, 330, 394),
        ("1.5", 222, 330, 234, 326, 228, 304), ("1.6", 362, 480, 374, 476, 366, 362)]
) + """
<text x="340" y="612" text-anchor="middle" font-size="12" fill="#5F5E5A">F father · D daughter · S son · numbered boxes = camera per shot</text>
<text x="340" y="634" text-anchor="middle" font-size="12" fill="#5F5E5A">Dashed axis runs through F and D — every camera stays south of it · 100 px ≈ 1 m</text>
</g></svg>
"""

SCENES = [
    dict(
        n=1, locked="2026-09-23",
        header="INT. SUPERMARKET — AFTERNOON · first day of Ramadan · التسوق",
        location="@loc_l1-market-day · day · عصر · first day of Ramadan · interior, conditioned air",
        geo=[
            "AISLE = a straight supermarket aisle running away from the main view to the NORTH, about 2.4 m wide, pale tile floor.",
            "DATE BINS = open wooden bins of loose dates with wooden scoops, waist height, along the WEST side (screen-left in the main view).",
            "SHELVING = white shelving of bulk spices and coffee in open jute sacks, bare glass honey jars and kraft rice sacks, along the EAST side (screen-right in the main view).",
            "FAR END = the north end of the aisle, soft and empty.",
            "180° AXIS: the line through THE FATHER and THE DAUGHTER at the bins. The camera stays SOUTH of it. It never crosses.",
            "LIGHT: rows of warm-white recessed ceiling downlights light the whole aisle evenly from above; warm spotlights fall on the date bins from above, on the west.",
        ],
        voices="None — nobody speaks in this scene.",
        lighting=("Scene-1 look = the user's reference frame: bright even ceiling downlights, warm gold spots on the bins · OFF: every film light · no haze · palette 60:30:10 = clean bright white and pale grey (ceiling, floor, shelving, thobes) · warm wood and sand (bins, baskets, sacks) · gold and amber (dates, honey)"),
        background="Quiet aisle by the user's choice — no other shoppers; the far end soft and empty · crowd: 0",
        svg=BLOCKING_SVG_S1,
        shots=S1_SHOTS,
    ),
]

# ---------------------------------------------------------------- scene 2 · الزينة (added 2026-09-27)
LIGHT_S2 = ("Scene-2 look matches scene 1 (user 2026-09-27): bright, clean, high-key. Soft afternoon daylight through the large west window "
            "and warm-white ceiling downlights light the room evenly; faces fully and evenly lit; white thobes clean and bright; soft low contrast, "
            "neutral-warm white balance. Once switched on, the strings' small bulbs glow warm gold and stay clearly visible against the bright room. No film light.")

S2_COMMON_TAGS = "@char_c1-grandfather_v1 (identity — white طاقية, gold-rimmed glasses, barefoot) · @char_c5-son_v1 (identity, barefoot) · @char_c6-daughter_v1 (identity, barefoot)"

S2_SHOTS = [
    dict(
        num="2.1", plan="WS", plan_label="Wide shot", dur=8, speed="real-time — natural human speed",
        mode="R2V — elements only", frames="—", media="—",
        context="STOCK CLIP — complete on its own: first day of Ramadan, afternoon. A grandfather steadies a ladder while his grandson hangs a string of Ramadan lights across the bare majlis wall and his granddaughter hands it up.",
        action="0–2 s: the son stands on the ladder's fourth step, leaning toward the wall; the daughter below on her toes lifts the string of lights up to him · 2–5 s: he hooks one end onto a small clip high on the wall, then the other end about two metres along · 5–8 s: he lets go; the unlit string hangs in a wide shallow curve across the middle of the wall; the daughter drops onto her heels, grinning; the grandfather looks up at it, smiling — at rest.",
        final="At rest: the unlit string hanging in a wide curve across the middle of the far wall, the son on the ladder looking at it, the daughter grinning up, the grandfather's palms still on the ladder.",
        lens="35mm · wide, about 63° · all three and the whole north wall sharp", camera="chest height, level · 4 m south of the ladder, facing north · axis side SOUTH · locked-off with a slight smooth breathing drift (calm)",
        tags=S2_COMMON_TAGS + " · @loc_l4-majlis-day (locked plate, facing the far wall — walls bare) · @prop_ladder · @prop_light-string (unlit; twenty small frosted bulbs — count + size in the prompt text)",
        first="The son already on the fourth step at frame-centre, leaning toward the wall, arms raised · the grandfather at the ladder's left foot, both palms on its rails · the daughter at its right on her toes, arms up, holding the string · hands: the daughter holds the string; the son reaches for it",
        blocking="See MAP_2_blocking.svg · ladder on the rug at the centre, its front feet at the front edge of the far seating, about 1 m from the far wall (x≈50%) · son on the 4th step (≈1 m up), leaning over the seating toward the wall · grandfather x≈40%, 0.6 m left of the ladder, facing the wall, head tipped back · daughter x≈60%, 0.7 m right of the ladder · open space: the bare upper wall",
        intent="Son — hang the top himself · obstacle: the height · tactic: reach and hook · INNER \"I've got it.\" · Daughter — her part in it · she can't reach, so she hands up · Grandfather — the room done his way, through his grandson's hands · business: palms on the ladder",
        beats="① the hand-up: her arms high, his arms reaching ② the hooks — one end, then the other ③ the wave: the daughter drops onto her heels grinning first, the son looks down at her half a beat later, the grandfather's slow smile last",
        listeners="The grandfather: palms never leave the ladder while the son is on it; eyes on the string, then the son.",
        dialogue="None. All three silent — breath only.",
        sfx="The ladder creaking under the son's weight · the bulbs clinking against each other · two small clicks as the ends go onto the clips · bare feet shifting on the rug · a car passing outside · music: none",
        seam="—",
        light=LIGHT_S2 + " Here: the string is unlit.",
        atmos="Still indoor air; the sheer curtain at the west window stirs faintly.",
        physics="The ladder flexes slightly under the son's weight; the string sags between its two ends in one shallow curve and swings gently to rest.",
        scale="Exactly three people. The string about two metres long with twenty small frosted globe bulbs, each about 3 cm across, one every 10 cm, hung at about 2.3 m on a 3 m wall. The son on the ladder's fourth step, his hands at the top of the wall; the grandfather tallest on the floor; the daughter a little shorter than the son.",
        state="Baseline — the plate: every wall bare · one unlit string in the daughter's hands.",
        contin="— (first shot of the scene)",
        text="None. Nothing printed anywhere.",
        warn="⚠️⚠️⚠️ The string stays UNLIT the whole clip. ⚠️⚠️⚠️ Only the far wall gets the string — the side walls stay bare. ⚠️⚠️ The grandfather's hands stay on the ladder; the ladder stands on the rug, never on the seating. ⚠️ All three barefoot. ⚠️ Nobody looks at the lens. ⚠️ Exactly one ladder, one string.",
        test="Does the locked majlis plate hold with three people, a real ladder and one unlit string — at real speed?",
    ),
    dict(
        num="2.2", plan="MS", plan_label="Medium shot", dur=8, speed="real-time — natural human speed",
        mode="R2V — elements only", frames="—", media="—",
        context="STOCK CLIP — complete on its own: the grandfather hands up a brass crescent; the son hangs it at the centre of the wall; the daughter spots it tilting and the son sets it straight.",
        action="0–2 s: the grandfather lifts the brass crescent up with his right hand; the son takes it in his right hand · 2–4 s: he hangs it on a small clip at the centre of the wall, just under the curve of the string; it hangs a little tilted · 4–6 s: the daughter points at it; the son nudges it level with a fingertip · 6–8 s: the daughter drops onto her heels, grinning; the son grins down at her; the grandfather nods, smiling — at rest.",
        final="At rest: the crescent hanging level at the centre of the wall, the son on the ladder grinning down, the daughter beaming, the grandfather's left palm back on the ladder.",
        lens="50mm · normal, about 47° · the three and the crescent sharp", camera="chest height, slightly low · 2.8 m south-west of the ladder, facing north-east · axis side SOUTH · smooth handheld, small tilt up as the crescent is hung",
        tags=S2_COMMON_TAGS + " · @loc_l4-majlis-day (locked plate, facing the far wall — walls bare) · @prop_ladder · @prop_crescent · @prop_light-string (hung in 2.1, unlit)",
        first="The grandfather at the ladder's left foot, his right arm raised holding the crescent up · the son on the third step reaching down for it · the daughter at the right on her toes, watching · hands: crescent in the grandfather's right hand",
        blocking="See MAP_2_blocking.svg · grandfather frame-left x≈35% · ladder and son x≈55% · daughter frame-right x≈72% · the crescent's clip at the centre of the far wall, just under the string",
        intent="Daughter — her part seen · tactic: correct (points at the tilt) · INNER \"It's crooked.\" · Son — hang it right · Grandfather — hand it up, then approve",
        beats="① the hand-up — right hand to right hand ② the crescent hangs tilted ③ her point ④ his fingertip nudge — level ⑤ the wave: daughter, son, grandfather's nod",
        listeners="The grandfather watches the crescent, not the children; his nod comes last.",
        dialogue="None.",
        sfx="The brass crescent tapping the wall as it is hung · a light scrape as it is nudged · the ladder creaking · bare feet on the rug · music: none",
        seam="—",
        light=LIGHT_S2 + " Here: the brass crescent catches a warm highlight from the window.",
        atmos="Still indoor air.",
        physics="The crescent swings a little on its clip before it settles; it has the weight of solid brass.",
        scale="The crescent about 30 cm tall — the size of a dinner plate. Exactly one crescent.",
        state="The string UNLIT, hung in a curve across the far wall (since 2.1) · side walls bare.",
        contin="From 2.1 — the string hangs in its curve across the far wall; the son still on the fourth step.",
        text="None — the crescent is plain brass, no engraving.",
        warn="⚠️⚠️⚠️ One crescent, plain, no text. ⚠️⚠️ Right hands for giving and taking. ⚠️ The string stays unlit and stays hung. ⚠️ Side walls bare.",
        test="Does the tilt → correction read clearly in 8 s, with a solid brass crescent that behaves like metal?",
    ),
    dict(
        num="2.3", plan="MS", plan_label="Medium shot", dur=6, speed="real-time — natural human speed",
        mode="R2V — elements only", frames="—", media="—",
        context="STOCK CLIP — complete on its own: the grandson climbs down from the ladder and his grandfather pats his back, proud of him.",
        action="0–2 s: the son steps down the ladder facing it, one step at a time, onto the rug · 2–4 s: the grandfather pats his back twice with an open palm, smiling · 4–6 s: the son's grin breaks out, then he straightens his shoulders; the daughter beside them grins — at rest.",
        final="At rest: grandfather and grandson side by side at the foot of the ladder, the grandfather's hand on the son's back, both smiling; the daughter grinning beside them.",
        lens="50mm · normal, about 47° · the grandfather and the son sharp", camera="chest height · 2.8 m south-east of the ladder, facing north-west · axis side SOUTH · smooth handheld, natural breathing",
        tags=S2_COMMON_TAGS + " · @loc_l4-majlis-day (locked plate, facing the far wall — walls bare) · @prop_ladder · @prop_light-string (hung, unlit) · @prop_crescent (hung)",
        first="The son on the second step, facing the ladder, one foot reaching down · the grandfather at the ladder's left foot, one palm on the rail · the daughter at the right",
        blocking="See MAP_2_blocking.svg · son lands at the ladder's foot, x≈50% · grandfather x≈38%, turning to him · daughter x≈65% · the hung crescent visible above them",
        intent="Grandfather — reward · two pats · Son — hold his composure, lose it to a grin · INNER \"Well done.\"",
        beats="① the careful climb down ② two pats ③ the grin he can't hold down ④ he straightens again",
        listeners="The daughter grins at her brother, then glances toward the wall switch.",
        dialogue="None.",
        sfx="Bare feet on the wooden steps · the ladder creaking as weight leaves it · two soft pats on cloth · feet landing on the rug · music: none",
        seam="—",
        light=LIGHT_S2,
        atmos="Still indoor air.",
        physics="The ladder settles as his weight leaves it. The pats are light — the thobe dimples under the palm.",
        scale="The son's head reaches about the grandfather's shoulder once on the floor.",
        state="The string UNLIT across the far wall (since 2.1) · crescent level at its centre (since 2.2).",
        contin="From 2.2 — the crescent level at the wall's centre.",
        text="None.",
        warn="⚠️⚠️ The son climbs down facing the ladder. ⚠️ Two pats, not a slap. ⚠️ The string unlit.",
        test="Does the proud pat + the held-back grin read in 6 s?",
    ),
    dict(
        num="2.4", plan="WS", plan_label="Wide shot", dur=8, speed="real-time — natural human speed",
        mode="R2V — elements only", frames="—", media="—",
        context="HERO STOCK CLIP — complete on its own: the grandfather nods to his granddaughter; she runs to the switch by the door and turns on the Ramadan lights; the string above the crescent lights up and so do their faces.",
        action="0–2 s: the grandfather lifts his chin toward the wall switch by the door — one small nod to the daughter · 2–4 s: she trots barefoot across the rug and the tiles to the switch, passing in front of the olive tree · 4–5 s: she presses it with her right hand — the string of lights comes on above the crescent · 5–8 s: the wave — she turns first, looking up at the wall; the son looks up half a beat later with a wide grin; the grandfather last, a long exhale and a wide smile — at rest.",
        final="At rest: the string glowing warm gold across the far wall above the crescent, the daughter by the switch looking up, the son and the grandfather at the ladder smiling up at the lights.",
        lens="35mm · wide, about 63° · the room sharp", camera="chest height · in the near-left of the room by the coffee corner, facing the far-right corner — sees the far wall, the ladder, the door and the switch · axis side SOUTH · locked-off, slight breathing drift",
        tags=S2_COMMON_TAGS + " · @loc_l4-majlis-day (locked plate, facing the far wall — walls bare) · @prop_ladder · @prop_light-string (hung; comes on at 4 s) · @prop_crescent (hung)",
        first="The grandfather and the son at the foot of the ladder, the daughter beside them at frame-centre-right, all three barefoot · the string UNLIT across the far wall, the crescent under it",
        blocking="See MAP_2_blocking.svg · grandfather x≈40% · son x≈48% · daughter starts x≈56%, trots about 3 m to frame-right to the switch beside the door (≈1.2 m high) · path: across the rug, then in front of the olive tree on the tiles",
        intent="Grandfather — hand the moment on · a nod, never a pointed arm · INNER \"Go on — light it.\" · Daughter — her part, seen · run and press · INNER \"Now!\"",
        beats="① the chin-nod ② her scout's trot ③ the press — the interrupted stillness: everything lights ④ the reaction wave: daughter, son, grandfather",
        listeners="All three active; reactions staggered 0.5 s apart.",
        dialogue="None. Breath only — her quick inhale as the lights come on; his long nose-exhale.",
        sfx="Quick bare feet on the rug, then on tile · the switch clicking · a soft electrical hum as the bulbs come on · a car passing outside · music: none",
        seam="—",
        light=LIGHT_S2 + " Here: unlit until 4 s, then the string comes on at once and stays on — a warm gold glow across the far wall above the crescent, clearly visible in the bright room.",
        atmos="Still indoor air.",
        physics="The bulbs come on instantly, all together — no flicker, no fade. Her bare feet push off the rug.",
        scale="Exactly three people. The switch at her chest height.",
        state="The string hung across the far wall (since 2.1) · crescent level (since 2.2) · the son on the floor (since 2.3) · string UNLIT → LIT at 4 s (this shot).",
        contin="From 2.3 — the son off the ladder beside his grandfather.",
        text="None — a plain white switch, no markings.",
        warn="⚠️⚠️⚠️ The string is unlit until the press, then ON to the last frame — never lit from frame 1, never switching off. ⚠️⚠️⚠️ Only the far-wall string lights; the side walls stay bare. ⚠️⚠️ She passes in front of the olive tree, never through it. ⚠️⚠️ The nod is small — no pointed arm. ⚠️ Right hand on the switch. ⚠️ Nobody looks at the lens.",
        test="Does the dark → lit change land on the press, with a glow that reads in a bright room?",
    ),
    dict(
        num="2.5", plan="CU", plan_label="Close-up", dur=5, speed="real-time",
        mode="R2V — elements only", frames="—", media="—",
        context="STOCK CLIP — complete on its own: an elder's face as the Ramadan lights come on — the warm glow rises on his face and he smiles.",
        action="0–1 s: the grandfather looking up at the far wall, calm · 1–2 s: the lights come on — a warm gold glow rises on his face and glasses · 2–4 s: his eyes travel slowly along the lit string to the crescent; a long exhale through the nose · 4–5 s: a wide open smile creasing his whole face — at rest.",
        final="At rest: chest-up, face three-quarter, eyes up on the lit wall, a wide warm smile, gold light on his cheek and glasses.",
        lens="85mm · short telephoto, about 29° · focus on his eyes", camera="his eye height, 1.6 m · 1.2 m south-east of him, facing north-west · axis side SOUTH · near-still handheld",
        tags="@char_c1-grandfather_v1 (identity — white طاقية, gold-rimmed glasses) · @loc_l4-majlis-day (locked plate, soft behind)",
        first="Chest-up, the grandfather at x≈45%, face three-quarter, looking up at frame-left",
        blocking="See MAP_2_blocking.svg · he stands at the ladder's left foot · his eyeline: up and north, to the crescent and the string, about 30° above level · open space above-left of his head",
        intent="See his house made right · the dignified mask → the wide open smile (his crack)",
        beats="① calm, looking up ② the glow arrives ③ eyes travel along the lit wall, long exhale ④ the wide smile",
        listeners="Off-frame: the grandchildren — only through his eyeline.",
        dialogue="None. Breath only — the long nose-exhale.",
        sfx="The switch clicking off-frame · a soft electrical hum · a slow breath out · music: none",
        seam="—",
        light=LIGHT_S2 + " Here: the lights' warm glow rises on his face from above frame-left at 1 s and stays.",
        atmos="Still indoor air.",
        physics="—",
        scale="Chest-up.",
        state="The string UNLIT → LIT at 1 s (this shot).",
        contin="Overlaps 2.4 — his smile here is the last of the wave there.",
        text="None.",
        warn="⚠️⚠️⚠️ Glasses and white طاقية as in the sheet. ⚠️⚠️ The glow comes on once and stays. ⚠️ Tight shot = eyes and breath only, no big face movement until the smile. ⚠️ Eyes never to the lens.",
        test="Does the elder's face hold identity in close-up, with the light change read on his skin?",
    ),
    dict(
        num="2.6", plan="WS", plan_label="Wide shot from behind", dur=6, speed="real-time",
        mode="R2V — elements only", frames="—", media="—",
        context="STOCK CLIP — complete on its own: a grandfather and his grandchildren stand together in the majlis, looking up at the Ramadan lights and the crescent they hung.",
        action="0–2 s: the three step back onto the middle of the rug, side by side, backs three-quarter to camera · 2–4 s: they look up at the lit string and the crescent; the grandfather rests his hand on the son's shoulder · 4–6 s: the daughter looks from the lights up to her grandfather's face and back — at rest.",
        final="At rest: the three side by side, the grandfather's hand on the son's shoulder, all looking up at the glowing string and the crescent on the far wall.",
        lens="35mm · wide, about 63° · the lit wall and the three sharp", camera="chest height, slightly low · 2.5 m behind them, south, facing north · axis side SOUTH · slow smooth push-in of about 0.5 m",
        tags=S2_COMMON_TAGS + " · @loc_l4-majlis-day (locked plate, facing the far wall — walls bare) · @prop_ladder · @prop_light-string (lit) · @prop_crescent (hung)",
        first="The three stepping back onto the middle of the rug, backs three-quarter to camera · the string LIT",
        blocking="See MAP_2_blocking.svg (g · s · d) · grandfather x≈42% · son x≈50% · daughter x≈58% · 1.8 m from the north wall · faces tipped up",
        intent="All three — take in the finished room · the grandfather claims the son with a hand on the shoulder",
        beats="① step back ② look up ③ the hand on the shoulder ④ her glance to his face and back",
        listeners="—",
        dialogue="None.",
        sfx="Bare feet stepping back on the rug · the lights' faint hum · a car passing outside · music: none",
        seam="—",
        light=LIGHT_S2 + " Here: the far-wall string lit the whole clip.",
        atmos="Still indoor air.",
        physics="Thobes and the daughter's dress settle as they stop.",
        scale="Exactly three people.",
        state="The string LIT across the far wall (since 2.4) · crescent level (since 2.2) · side walls bare.",
        contin="From 2.4 — the string lit.",
        text="None.",
        warn="⚠️⚠️ The string lit the whole clip; side walls bare. ⚠️ Faces seen three-quarter from behind — nobody turns to the lens. ⚠️ All three barefoot.",
        test="Does the lit string read as the scene's payoff in a bright afternoon room?",
    ),
]

BLOCKING_SVG_S2 = (HERE / "MAP_2_blocking.svg").read_text(encoding="utf-8")

SCENE_2 = dict(
    n=2, locked="2026-09-27",
    header="INT. MAJLIS — AFTERNOON · first day of Ramadan · الزينة",
    location="@loc_l4-majlis-day (locked 2026-09-28, walls bare) · day · عصر · first day of Ramadan · interior · the decorations come from @prop_light-string + @prop_crescent",
    geo=[
        "FAR WALL = the wall facing the main view, bare warm-white plaster — the family decorates it in this scene.",
        "SEATING = beige floor seating in a U along the west, far and east walls, 0.7 m deep.",
        "RUG = a large sand-and-ivory rug in the middle of the floor, up to the seating.",
        "WINDOW = a wide window in the WEST wall (screen-left).",
        "DOOR + SWITCH = a light-oak door in the EAST wall at the screen-right edge, near the camera; a white switch beside it at 1.2 m.",
        "OLIVE TREE = near-right, in a stone pot between the east seating and the door.",
        "180° AXIS: the line through THE GRANDFATHER and THE DAUGHTER at the foot of the ladder. The camera stays SOUTH of it. It never crosses.",
        "LIGHT: soft afternoon daylight through the west window and the ceiling spots light the room evenly; soft shadows fall toward the east wall.",
    ],
    voices="None — nobody speaks in this scene.",
    lighting=("Matches scene 1: bright, clean, high-key · window + ceiling spots + cove · the far-wall string OFF until 2.4, ON after · OFF: every film light · no haze · "
              "palette 60:30:10 (عصر, research look 2026-09-27) = white, cream and sand (walls, tiles, rug, thobes) · beige and light oak (seating, door, ladder) · brushed brass with a touch of sadu red (crescent, lit bulbs, sadu band)"),
    background="Empty room but the three — no one else · crowd: 0",
    svg=BLOCKING_SVG_S2,
    shots=S2_SHOTS,
)
SCENES.append(SCENE_2)

ASSETS += [
    ("@char_c1-grandfather_v1", "Character", "home · white knitted طاقية · gold-rimmed glasses · barefoot",
     "The grandfather. Lean, a little stooped, neat white beard. White thobe with a standing mandarin collar and buttons.", "2"),
    ("@loc_l4-majlis-day", "Location · <b>REGISTERED</b> 2026-09-28", "day · عصر · every wall bare · single wide frame facing the far wall",
     "Locked plate (job 691b45b1, GPT Image 2.5 Sunburst + NB2 edits): modern Saudi family majlis — beige woven floor seating in a U with a red sadu band and upright armrests, sand-ivory rug, cream tiles, gypsum cove ceiling, west window, coffee corner near-left, olive tree near-right by the door. The lights are hung in the videos.", "2 · 10"),
    ("@prop_ladder", "Prop · <b>NEW</b>", "—", "Plain wooden step ladder, about 1.5 m, five steps.", "2"),
    ("@prop_crescent", "Prop · <b>REGISTERED</b> 2026-09-28", "—",
     "One plain brushed-brass crescent about 30 cm tall, smooth unmarked faces, a small hanging loop at its upper tip.", "2 · 10"),
    ("@prop_light-string", "Prop · <b>NEW</b>", "unlit (the video lights it)",
     "One string about 2 m long: fifteen grape-sized clear bulbs in small brass sockets on thin copper wire, a small plain white plug.", "2 · 10"),
]
CAST.insert(0, ("@char_c1-grandfather_v1",
     "Tics: rests both palms on something solid whenever he stands still · directs with a nod or the chin, never a raised arm · "
     "pats a back twice when pleased. Eyes: deep-set, warm, long gazes, slow full blinks. Gait: \"elder's measured step\". "
     "Mask → crack: calm dignity → a wide open smile when a grandchild gets it right. Softens for: his grandson.",
     "Silent in every scene — breath only; a long nose-exhale when something is done well.", "—", "\"the grandfather\" — role, clothing, action"))

# ---------------------------------------------------------------- markdown copy (for working from)
def build_md():
    L = [f"# Shotlist — Ramadan (working copy)", "",
         "Generated by `shotlist_build.py` — the same data as the PDF. Edit the .py, not this file.", "",
         f"**Model:** {MODEL}", "", f"**Style prefix:** {STYLE_PREFIX}", "", f"**Music:** {MUSIC}", "",
         "**Project rules:**"] + [f"- {r}" for r in RULES] + ["", "## Assets", "", "| @tag | Type | State | Description | Scenes |", "|---|---|---|---|---|"]
    L += [f"| {a} | {b.replace('<b>','**').replace('</b>','**')} | {c} | {d} | {e} |" for a,b,c,d,e in ASSETS]
    L += ["", "## Cast", ""] + [f"- **{a}** — {b} · Voice: {c} · Age: {e}" for a,b,c,d,e in CAST]
    for sc in SCENES:
        L += ["", f"## Scene {sc['n']} · {sc['header']} — {sc['locked']}", "",
              f"**Location:** {sc['location']}", "", "**GEO layout (static — pasted byte-identical into every prompt of this scene):**"]
        L += [f"- {g}" for g in sc["geo"]]
        L += ["", f"**Lighting:** {sc['lighting']}", "", f"**Background:** {sc['background']}", ""]
        for s in sc["shots"]:
            L += [f"### {s['num']} · {s['plan_label']} · {s['dur']} s · {s['speed']}", "",
                  f"- **Test objective:** {s['test']}", f"- **Mode:** {s['mode']} · frames: {s['frames']} · media: {s['media']}",
                  f"- **Context:** {s['context']}", f"- **Action (timed):** {s['action']}", f"- **Final frame:** {s['final']}",
                  f"- **Lens:** {s['lens']}", f"- **Camera:** {s['camera']}", f"- **Tags + roles:** {s['tags']}",
                  f"- **First frame:** {s['first']}", f"- **Blocking:** {s['blocking']}", f"- **Intent:** {s['intent']}",
                  f"- **Beats:** {s['beats']}", f"- **Listeners:** {s['listeners']}", f"- **Dialogue:** {s['dialogue']}",
                  f"- **SFX:** {s['sfx']}", f"- **Seam:** {s['seam']}", f"- **Light:** {s['light']}", f"- **Atmosphere:** {s['atmos']}",
                  f"- **Physics:** {s['physics']}", f"- **Scale:** {s['scale']}", f"- **Scene state:** {s['state']}",
                  f"- **Continuity in:** {s['contin']}", f"- **On-screen text:** {s['text']}", f"- **⚠️ Warning:** {s['warn']}", ""]
    (HERE / "Shotlist_Ramadan.md").write_text("\n".join(L), encoding="utf-8")
    print("wrote Shotlist_Ramadan.md")


# ---------------------------------------------------------------- render
CSS = """
@page { size: A3 landscape; margin: 12mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, Helvetica, Arial, "Geeza Pro", "PingFang SC", sans-serif; font-size: 9.5pt; color: #111; margin: 0; }
header.top { border-bottom: 2px solid #b91c1c; padding-bottom: 6mm; margin-bottom: 6mm; }
header.top h1 { font-size: 20pt; margin: 0 0 2mm; }
header.top .sub { color: #555; margin-bottom: 3mm; }
.stats { display: flex; gap: 10mm; margin-top: 3mm; }
.stat .v { font-size: 16pt; font-weight: 600; } .stat .l { color: #666; font-size: 8pt; }
.assets, .cast { margin: 4mm 0 8mm; } .assets h2, .cast h2 { font-size: 13pt; margin: 0 0 2mm; }
.assets table td:first-child, .cast table td:first-child { font-family: Menlo, monospace; white-space: nowrap; }
.scene { break-before: page; }
.scene-head { border-left: 4px solid #b91c1c; padding-left: 4mm; margin-bottom: 4mm; }
.scene-num { font-size: 8pt; letter-spacing: .1em; color: #b91c1c; font-weight: 600; }
.scene-title { font-size: 14pt; margin: 1mm 0; }
.scene-meta { color: #444; display: flex; gap: 8mm; }
table { width: 100%; border-collapse: collapse; }
th { background: #f3f4f6; text-align: left; font-size: 8.5pt; }
th, td { border: 1px solid #d1d5db; padding: 2mm; vertical-align: top; }
tr { break-inside: avoid; }
.badge { display: inline-block; padding: .5mm 2mm; border-radius: 2mm; font-size: 8pt; background: #fee2e2; color: #7f1d1d; }
.warn { color: #b45309; }
table.constants th, table.shot th { width: 12%; background: #f9fafb; }
table.shot { margin-bottom: 6mm; break-inside: avoid; }
table.shot tr.strip td { background: #fef2f2; font-size: 8.5pt; }
div.group-head { background: #eef2ff; border-left: 4px solid #4f46e5; padding: 2mm 3mm; margin: 5mm 0 2mm; font-size: 9pt; break-after: avoid; }
table.shot tr.grp td { background: #f3f4f6; font-size: 7.5pt; letter-spacing: .08em; text-transform: uppercase; color: #6b7280; padding: 1mm 2mm; }
ul.rules { margin: 0; padding-left: 5mm; } ul.rules li { margin: .5mm 0; }
section.cast { break-inside: avoid; }
.assets h2, .cast h2 { break-after: avoid; }
div.group-head { break-before: page; }
table.shot { font-size: 8.6pt; }
table.shot th, table.shot td { padding: 1.3mm 2mm; }
table.shot tr.grp { break-after: avoid; }

.small { color: #666; font-size: 8pt; }
"""

def row(th, td): return f"<tr><th>{th}</th><td colspan='5'>{td}</td></tr>"
def grp(t): return f"<tr class='grp'><td colspan='6'>{t}</td></tr>"

def shot_card(s, g):
    return f"""
<div class="group-head"><b>Group {g}</b> · {s['dur']} s · shot {s['num']} · single continuous take · cuts: none ·
lens: {s['lens'].split(' ·')[0]} · <b>Test objective:</b> {s['test']}</div>
<table class="shot">
 <tr class="strip"><td><b>{s['num']}</b></td><td>Group {g}</td><td>cinedance</td>
  <td>{s['dur']} s · {s['speed']}</td><td>clean head → clean tail (trim ½ s each end)</td><td>{s['mode']} · start/end frame {s['frames']}</td></tr>
 {row('Media refs', s['media'])}
 {grp('What happens')}
 {row('Scene context', s['context'])}{row('Action (timed)', s['action'])}{row('Final frame', s['final'])}
 {grp('Frame')}
 {row('Lens', f"<span class='badge'>{s['plan_label']}</span> {s['lens']}")}{row('Camera', s['camera'])}
 {grp('Space')}
 {row('Tags + roles', s['tags'])}{row('First frame', s['first'])}{row('Blocking', s['blocking'])}
 {grp('Performance')}
 {row('Intent', s['intent'])}{row('Beats', s['beats'])}{row('Listeners', s['listeners'])}
 {grp('Sound')}
 {row('Dialogue', s['dialogue'])}{row('VO', '—')}{row('SFX · music', s['sfx'])}{row('Seam', s['seam'])}
 {grp('World')}
 {row('Light', s['light'])}{row('Atmosphere', s['atmos'])}{row('Physics', s['physics'])}{row('Scale', s['scale'])}
 {grp('State')}
 {row('Scene state', s['state'])}{row('Continuity in', s['contin'])}{row('On-screen text', s['text'])}
 {grp('Risk')}
 <tr><th>⚠️ Warning</th><td colspan="5" class="warn">{s['warn']} Age: role + clothing only. NON-IP: no brands, nothing printed.</td></tr>
</table>"""

def scene_block(sc, g0):
    shots = sc["shots"]; total = sum(s["dur"] for s in shots)
    geo = "<br>".join("— " + x for x in sc["geo"])
    cards = "".join(shot_card(s, g0 + i) for i, s in enumerate(shots))
    return f"""
<section class="scene" id="sc{sc['n']}">
 <div class="scene-head">
  <div class="scene-num">SCENE {sc['n']} · LOCKED {sc['locked']}</div>
  <h2 class="scene-title">{sc['header']}</h2>
  <div class="scene-meta"><span>{len(shots)} shots · {len(shots)} generation groups · {total} s</span><span><b>Format:</b> 16:9 · 24 fps</span></div>
 </div>
 <table class="constants">
  <tr><th>Location</th><td>{sc['location']}</td></tr>
  <tr><th>GEO layout (static)</th><td>{geo}<br><i class="small">(version A — shots {shots[0]['num']}–{shots[-1]['num']} · pasted byte-identical into every prompt of this scene)</i></td></tr>
  <tr><th>Voice locks</th><td>{sc['voices']}</td></tr>
  <tr><th>Lighting</th><td>{sc['lighting']}</td></tr>
  <tr><th>Background</th><td>{sc['background']}</td></tr>
 </table>
 {sc['svg']}
 {cards}
</section>"""

def build():
    n_shots = sum(len(s["shots"]) for s in SCENES)
    assets = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in ASSETS)
    cast = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in CAST)
    rules = "".join(f"<li>{r}</li>" for r in RULES)
    blocks, g = [], 1
    for sc in SCENES:
        blocks.append(scene_block(sc, g)); g += len(sc["shots"])
    locked = ", ".join(str(s["n"]) for s in SCENES)
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Shotlist — Ramadan · scenes {locked}</title><style>{CSS}</style></head>
<body>
<header class="top">
 <h1>Shotlist — Ramadan · scenes locked: {locked} of 15</h1>
 <div class="sub">{PROJECT} · Prepared for {PREPARED_FOR} · {TODAY} · built per scene — this file grows as each scene locks</div>
 <table class="constants">
  <tr><th>Target model</th><td>{MODEL}</td></tr>
  <tr><th>Style prefix</th><td>{STYLE_PREFIX}<br><span class="small">{STYLE_NOTE}</span></td></tr>
  <tr><th>Music</th><td>{MUSIC}</td></tr>
  <tr><th>Project rules</th><td><ul class="rules">{rules}</ul></td></tr>
 </table>
 <div class="stats">
  <div class="stat"><div class="v">{len(SCENES)}</div><div class="l">scenes locked</div></div>
  <div class="stat"><div class="v">{n_shots}</div><div class="l">shots</div></div>
  <div class="stat"><div class="v">{n_shots}</div><div class="l">generation groups (1 shot each)</div></div>
 </div>
</header>
<section class="assets"><h2>Asset list — build list for stage 3a (register there)</h2>
 <table><thead><tr><th>@tag</th><th>Type</th><th>State</th><th>Description</th><th>Scenes</th></tr></thead><tbody>{assets}</tbody></table></section>
<section class="cast"><h2>Cast sheet</h2>
 <table><thead><tr><th>@tag</th><th>Acting core (from 2B)</th><th>Voice lock (from 2A)</th><th>Phonetics</th><th>Age handling</th></tr></thead><tbody>{cast}</tbody></table></section>
{''.join(blocks)}
</body></html>"""
    out = HERE / "Shotlist_Ramadan.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.name} — {len(SCENES)} scene(s), {n_shots} shots")

if __name__ == "__main__":
    build()
    build_md()
