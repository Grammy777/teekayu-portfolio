---
name: Teekayu Prachayakul Portfolio
description: Cool paper, near-black ink and one acid-lime highlighter; a bilingual single page that reads like a marked-up spec.
colors:
  paper: "#f5f6f3"
  paper-2: "#ecede8"
  ink: "#15171a"
  ink-hover: "#2b2f35"
  ink-2: "#4a4f57"
  ink-3: "#6b7079"
  rule: "#d8dbd4"
  mark: "#d4f53c"
  mark-soft: "#eefab8"
  ok: "#2f7d4f"
  mark-hover: "#e2fa6e"
  on-stage: "#ffffff"
  cover: "#15171a"
  cover-fg: "#f5f6f3"
  cover-fg-2: "#b9bec5"
  cover-fg-3: "#8e949c"
  cover-rule: "#33373d"
  cover-ok: "#5fd38a"
  on-mark-2: "#2f3a12"
  st-req: "#2f5fd0"
  st-req-tint: "#e6edfb"
  st-req-ink: "#1d3f94"
  st-spec: "#7a3fc8"
  st-spec-tint: "#f0e8fb"
  st-spec-ink: "#4e2290"
  st-build: "#0c7a5e"
  st-build-tint: "#ddf3ec"
  st-build-ink: "#0a5c47"
  st-test: "#b04e0c"
  st-test-tint: "#fbe9dc"
  st-test-ink: "#8a3a07"
typography:
  display:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2.1rem, 7vw, 3.25rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  display-contact:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.15rem, 4.6vw, 2rem)"
    fontWeight: 700
    lineHeight: 1.3
  headline:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.45rem, 3.6vw, 1.75rem)"
    fontWeight: 700
    lineHeight: 1.25
  title:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.25
  body-lead:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.7
  body:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.75
    fontFeature: "\"kern\""
  body-sm:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 600
    lineHeight: 1.35
  caption:
    fontFamily: "Anuphan, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "0.02em"
rounded:
  track: "2px"
  mark: "3px"
  panel: "16px"
  focus: "4px"
  sm: "8px"
  md: "10px"
  pill: "999px"
spacing:
  gutter: "clamp(20px, 4vw, 48px)"
  row: "22px"
  row-lg: "28px"
  section: "56px"
  section-lg: "72px"
  column-gap: "72px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.ink-hover}"
    textColor: "{colors.paper}"
  lang-switch:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "8px 13px"
    height: "32px"
  lang-switch-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
  stage-chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-2}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  stage-chip-current:
    backgroundColor: "{colors.mark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
  nav-link:
    textColor: "{colors.ink-3}"
    padding: "7px 0"
  nav-link-active:
    textColor: "{colors.ink}"
  media-frame:
    backgroundColor: "{colors.paper-2}"
    rounded: "{rounded.md}"
---

# Design System: Teekayu Prachayakul Portfolio

## Overview

**Creative North Star: "The Marked-Up Spec"**

The page behaves like a requirements document someone has read carefully with a highlighter in hand. Cool off-white paper, near-black ink, hairline rules between rows, and exactly one loud colour: an acid-lime marker that lands on the few words and states that matter right now. Nothing floats, nothing glows, nothing is boxed into cards; structure comes from rules, columns and type weight.

Density is calm and editorial. Thai and Latin share one family (Anuphan) at generous line height, so both scripts sit in the same rhythm and Thai stacked vowels never collide. On desktop a sticky left column holds identity, navigation and the email action while content scrolls past on the right; on phones the same content stacks under a slim sticky bar that carries the language switch. The signature motion is a four-stage pipeline (Requirement, Spec, Build, Test) that fills in ink as the reader scrolls through the work it describes.

The system refuses the dark neon developer portfolio and the cream résumé: no dark ground, no glow, no gradient text, no warm parchment.

**Key Characteristics:**
- One cool-paper ground, one near-black ink, one acid-lime marker; greys are cool ink tints, not neutrals of their own.
- Hairline rules (1px) are the only structural device; media frames are the only bordered rectangles.
- Pills for things you press or that carry state; soft 10px corners for images; everything else square.
- A single variable family (Anuphan, 100–700) for both scripts, weight doing the hierarchy work.
- Motion is short, eased and tied to reading position; it disappears completely under reduced motion.

## Colors

A near-monochrome cool palette with a single highlighter accent whose rarity is the point.

### Primary
- **Acid-Lime Marker** (mark): the highlighter. Drawn as a hard-stop band behind the lower half of key words (the role line, the contact email), as the fill of the current pipeline step dot, as the fill of the current stage chip, and as the text-selection colour. Ink sits on it at 14.5:1.
- **Pale Lime Wash** (mark-soft): only the 4px halo ring around the current pipeline step dot. Never a surface.

### Neutral
- **Cool Paper** (paper): the page ground and every sticky bar's background, so sticky layers read as the same sheet rather than as floating panels.
- **Shaded Paper** (paper-2): the recessed fill behind screenshots while they load and the hover fill on the inactive language option. Not a section background.
- **Graphite Ink** (ink): all headings and body text, the primary button, the active language pill, the pipeline fill line, completed step dots, the active nav dash, and the focus outline.
- **Slate Ink** (ink-2): secondary text: leads, dates, stack lines, chip text, inactive language option, certificate meta. 7.6:1 on paper.
- **Pencil Grey** (ink-3): tertiary text only: nav links at rest, step sub-labels, project meta lines, footer, and the resting underline colour of text links. 4.59:1 on paper; it drops to 4.23:1 on paper-2, so it never carries text on that surface.
- **Hairline** (rule): every 1px divider, the unfilled pipeline track, idle step-dot borders, chip borders, the language-switch outline and media-frame borders. Decorative only; never text.
- **Signal Green** (ok): the 9px availability dot beside "open to roles". One use.

### Named Rules
**The One Marker Rule.** Lime appears only where the reader's attention should land now: at most the role line, the contact email, and the single current pipeline step and chip. If two things on screen are lime and neither is "current", one of them is wrong.

**The Same-Sheet Rule.** Sticky layers (top bar, pipeline bar, sidebar) use the paper colour plus a hairline, never a tint, blur or shadow. Depth is implied by the rule, not by material.

## Typography

**Display Font:** Anuphan (self-hosted variable woff, weights 100–700) with system-ui, -apple-system, Segoe UI, sans-serif
**Body Font:** Anuphan (same file)

**Character:** A single humanist Thai-Latin family carries every role. Weight (400, 500, 600, 700) and size do all the hierarchy work, so the Thai and English versions of the page look like the same document.

### Hierarchy
- **Display** (700, clamp(2.1rem, 7vw, 3.25rem), 1.15): the person's name only, in the intro. English tightens tracking to -0.025em; Thai keeps -0.01em.
- **Display Contact** (700, clamp(1.15rem, 4.6vw, 2rem), 1.3): the email address in the contact section, drawn with the marker band. Breaks anywhere so it never overflows a phone.
- **Headline** (700, clamp(1.45rem, 3.6vw, 1.75rem), 1.25): section headings (Experience, Projects, Skills, About, Contact).
- **Title** (700, 1.25rem, 1.25): project names. The internship role line uses a close sibling (700, 1.1875rem, 1.4); the role subtitle in the intro is 600 at clamp(1.1rem, 3.2vw, 1.3rem).
- **Body Lead** (400, 1.125rem, 1.7): the one-line thesis in the intro, capped at 34ch.
- **Body** (400, 1.0625rem, 1.75): all running text. Measure capped at 60–62ch for leads, work rows and About.
- **Label** (600, 0.875rem): stack lines, meta lines (500), project context lines, step names (700). Nav links and sub-headings use 0.9375rem at 600–700.
- **Caption** (700, 0.75rem, +0.02em): stage chips and step sub-labels (sub-labels at 400 in Pencil Grey).

### Named Rules
**The Tall Line Rule.** Body copy keeps line-height at 1.7 or more. Thai above-and-below marks need the room; tightening body leading to Latin-only defaults breaks the Thai page first.

**The One Family Rule.** No second typeface, no monospace for "code-ness", no system display face. Emphasis is weight, the marker, or an underline.

## Layout

A centred shell (max 1200px) with a fluid gutter of clamp(20px, 4vw, 48px).

- **Phone (<640px):** single column. A 56px sticky top bar (short name + language switch, hairline under it). The intro ends with a hairline. The pipeline bar sticks directly under the top bar at full bleed (it cancels the gutter with negative margins), and step sub-labels are hidden with step names dropping to 0.75rem.
- **Tablet (≥640px):** rows gain a label column: work rows become 8.5rem + 1fr, skill rows 12rem + 1fr, project rows split media and text 5fr : 6fr with a 28px gap.
- **Desktop (≥1024px):** the top bar disappears and the shell becomes two columns, minmax(320px, 5fr) and 7fr with a 72px gap. The left column is a full-viewport sticky sidebar (name, role, location, thesis, availability, email button, five-item nav, language switch pinned to the bottom). On viewports shorter than 720px the sidebar stops sticking so nothing gets clipped. The pipeline bar sticks to the top of the right column with a 20px paper fade beneath it so rows slide under cleanly.

Rhythm: sections open 56px apart on phones and 72px on desktop, with headings 22px above their content. List rows are separated by hairlines with 22px (work), 28px (projects), 16px (skills) or 14px (certificates) of vertical padding. Contact gets extra air (64px top) and the footer sits 72px below it.

**The Rows-Not-Cards Rule.** Collections (work, projects, skills, certificates) are rows divided by 1px hairlines, never grids of boxed cards.

## Elevation & Depth

Flat. There are no drop shadows anywhere. Layering is conveyed by the hairline under a sticky layer and by stacking order alone. Two non-shadow devices exist and are both functional: the current pipeline step carries a crisp 4px Pale Lime ring (a spread ring with no blur, marking "you are here"), and on desktop the sticky pipeline bar is followed by a 20px paper-to-transparent scrim so content does not cut hard against it.

### Shadow Vocabulary
- **Current-step ring** (`box-shadow: 0 0 0 4px var(--mark-soft)`): only on the active pipeline dot. Not reusable as a hover or card effect.

### Named Rules
**The Flat Sheet Rule.** Nothing lifts off the page. A new surface that "needs" a shadow needs a hairline instead.

## Shapes

Three corner values, each tied to a meaning. Pills (999px) for anything pressable or stateful: the email button, the language switch and its options, stage chips. Soft corners (10px) for media frames only: screenshots sit in a 1px Hairline frame on Shaded Paper with clipped corners. Small corners (8px) only on the skip link; 4px rounds the focus outline. Circles for status dots (pipeline steps at 14px, availability at 9px). Everything else, including rows and sections, is square and borderless except for hairline dividers.

The marker is a shape too: a hard-edged band painted with stopped linear gradients from about 52–58% to 92–94% of the line box, so it reads as a highlighter stroke across the lower half of the letters, not as a filled box or a gradient.

## Components

### Buttons
Confident and solid; there is only one.
- **Shape:** full pill (999px), 48px minimum height.
- **Primary:** Graphite Ink fill, Cool Paper text at 600, 22px side padding, an 18px stroke icon leading the label with a 10px gap.
- **Hover / Active:** fill lifts to a slightly lighter graphite (#2b2f35) over 0.2s; press nudges it down 1px. Focus uses the global 2px ink outline at 3px offset.
- **Secondary:** there is no secondary button. Secondary actions are text links.

### Text Links
- **Style:** 600 weight, 1px underline offset 4px in Pencil Grey.
- **Hover:** the underline darkens to ink and thickens to 2px.
- **Arrow link variant:** the same link with a trailing up-right arrow icon that shifts 2px up and right on hover; used for "open the live site" and certificate view/verify links, with a hidden "(opens in a new tab)" note.

### Chips (stage chips)
- **Style:** pill outline in Hairline, Slate Ink caption text, transparent on paper.
- **State:** the chip on the row currently being read fills with Acid-Lime Marker and its border and text go to lime and ink, transitioning over 0.3s. The project line beside it darkens from Slate to Graphite at the same time.

### Navigation
- **Style:** desktop only, five links stacked in the sidebar at 0.9375rem, 600, Pencil Grey, each preceded by a 28px hairline dash in the current colour.
- **Hover:** text goes to ink.
- **Active (section in view):** text goes to ink and the dash grows to 64px and 2px thick, eased with cubic-bezier(.16, 1, .3, 1) over 0.35s.
- **Mobile:** no nav; the page is a single read-through and the top bar carries only the short name and the language switch.

### Language Switch
- **Style:** a segmented pill: 1px Hairline outline, 3px inner padding, two options (ไทย / EN) at 0.8125rem, 600, 32px minimum height.
- **Active:** Graphite Ink pill with paper text; the focus ring flips to paper so it stays visible on the dark pill.
- **Hover (inactive):** Shaded Paper fill, ink text.
- **Behaviour:** swaps every string in place from one table, updates `lang`, title and description, remembers the choice, and writes `?lang=` to the URL.

### Media Frames
- **Corner Style:** 10px, clipped.
- **Background:** Shaded Paper behind the image; a near-black tray (#101215) for the phone-screenshot row, with three phones bottom-aligned.
- **Border:** 1px Hairline (tray border matches the tray).
- **Shadow Strategy:** none (see Elevation & Depth).

### Pipeline (signature component)
A four-step horizontal track (Requirement, Spec, Build, Test) that sticks above the work rows. A 2px Hairline track runs between the 14px dots; an ink fill line grows along it continuously in proportion to how far the reading line (mid-viewport) has travelled through the work rows. Steps behind the current one become solid ink dots; the current step becomes an Acid-Lime dot with an ink border, the Pale Lime ring, and an underlined step name. Each work row carries the matching stage chip, so the bar and the rows always agree. Under reduced motion all transitions are zeroed and the bar simply snaps.

### Highlighter Mark
Inline emphasis for the two or three phrases that define the person (the role titles) and for the contact email. On the email the band grows taller on hover (background-size from 100% to 160% over 0.3s).

## Do's and Don'ts

### Do:
- **Do** keep the page on Cool Paper with Graphite Ink text and let hairline rules (1px Hairline) carry all structure.
- **Do** reserve Acid-Lime Marker for the role line, the contact email and the single current pipeline state, per The One Marker Rule.
- **Do** keep body line-height at 1.7–1.75 and measures at 60–62ch so Thai and English read in the same rhythm.
- **Do** use pills (999px) for pressable or stateful controls and 10px corners only on image frames.
- **Do** make every sticky layer paper plus a bottom hairline.
- **Do** ship every string in both Thai and English from the same table, and keep 32px minimum hit areas on secondary controls and 48px on the primary button.
- **Do** honour reduced motion by removing transitions, not by swapping in alternatives.

### Don't:
- **Don't** add drop shadows, blurred glows or lifted cards; the only ring in the system is the current pipeline step's.
- **Don't** fill text with gradients or use soft multi-stop gradients as decoration; gradients exist only as hard-stop marker bands and the one functional paper scrim.
- **Don't** introduce a dark ground, neon accents or a second accent colour.
- **Don't** box collections into card grids; use hairline-divided rows.
- **Don't** add a second typeface, a monospace "dev" face or a system display face.
- **Don't** set Pencil Grey text on Shaded Paper or use Hairline as a text colour.

## Colour roles (colorize pass, Oct 2026)

- **Cover:** the intro is a dark cover (`cover`), a full-height column on desktop and a full-bleed band plus the top bar on mobile. Text on it uses `cover-fg` / `cover-fg-2` / `cover-fg-3`; the role words sit on solid lime blocks, and the primary email button turns lime on the cover.
- **Stage hues:** each stage of work owns one hue (Requirement blue, Spec violet, Build green, Test orange). The pipeline dot, the pipeline fill and the row's stage chip share it: tint chip with ink-on-tint text at rest, solid chip with white text on the current row. The stage name is always written, so colour is never the only cue.
- **Contact field:** Contact is the one lime field on the page, because it is the goal. Inside it, links and the copy button switch to ink.
