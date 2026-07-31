# Metric Views in Genie Spaces — Presentation

A self-contained HTML slide deck for an internal Techcombank enablement session
on using Databricks Unity Catalog **metric views** inside **AI/BI Genie spaces**.

## The deck

**[`metric-views-in-genie-tcb.html`](metric-views-in-genie-tcb.html)** — 16 slides.

Compares two ways of giving Genie the business meaning behind our data:

- **Method A** — tables and views, curated in the space (comments, synonyms,
  example SQL, text instructions). Colour-coded **gold** throughout.
- **Method B** — a metric view as the semantic layer in Unity Catalog.
  Colour-coded **red** throughout.

The spine of the deck is the side-by-side comparison (slide 7), a worked example
showing the SQL Genie writes each way (slide 8), an honest account of how each
method fails (slide 9), and the hybrid pattern to standardise on (slide 14).

## Viewing

Open the file directly in a browser — no build step, no server, no dependencies.

**Controls**

| Key | Action |
|---|---|
| `←` `→` `Space` `PageUp/Dn` | Navigate |
| `Home` / `End` | First / last slide |
| `S` | Toggle speaker notes |
| `F` | Fullscreen |
| `Ctrl+P` | Print — one slide per page |

Clicking the left/right half of the slide also navigates, and touch swipe works.
Deep links work via the hash: `…/deck.html#7` opens slide 7.

## Published artifact

The deck is also published as a private Claude Artifact:

**https://claude.ai/code/artifact/f1fe984e-4c25-4f1b-bcfa-93df10a23135**

Artifacts wrap the supplied file in their own `<!doctype html><head>…</head><body>`
skeleton, so the published copy must contain page content only. `build-artifact.py`
strips the wrapper from the source deck and writes `artifact.html` (gitignored —
it is generated, not source):

```
python build-artifact.py
```

To update the live page, regenerate and republish. From a session that did not
originally publish it, pass the URL above explicitly, otherwise a second artifact
is minted at a new URL instead of updating this one.

## Editing

The deck is a **single self-contained HTML file** — CSS, JS and content in one
place, no external requests (no CDN, no web fonts, no images). Keep it that way;
it gets opened offline and from local disk.

### Structure

```
<style>        design tokens in :root, then components
<div id="stage">    fixed 1280×720 stage, scaled to viewport by JS
  <section class="slide" data-title="…">   one per slide
    <aside class="notes">   speaker notes (hidden; shown via S)
<script>       syntax highlighter + navigation
```

### Rules that keep it from breaking

- **The stage is a fixed 1280×720 box.** Content that overflows is clipped, not
  scrolled. After adding content, verify it still fits (see below).
- Slide count in the footer is derived automatically — no need to update it.
- Code blocks use `<pre data-lang="yaml">` or `data-lang="sql">` and are
  highlighted at load by a small regex highlighter in the page. Escape `<` and
  `>` as `&lt;` / `&gt;` inside them.
- Layout helpers: `.fill`, `.split`, `.grid2/3/4`, `.stack`, `.card`, `.callout`,
  `.chip`, `.tblwrap`. Prefer these over new bespoke CSS.
- Colour carries meaning: **gold = Method A (tables & views)**, **red = Method B
  (metric views)**. Don't use them decoratively.

### Checking a slide still fits

The deck was validated with a Playwright script that measures per-slide
overflow against the stage bounds. On this machine Chromium downloads fail, so
launch with the system Chrome channel:

```python
browser = playwright.chromium.launch(channel="chrome")
```

Measure each slide's lowest element against `stage.bottom - 70px` (the footer
band). Anything over ~5px is a real overflow.

## Theme

Techcombank "champagne & gold" identity:

| Token | Value | Use |
|---|---|---|
| `--ground` | `#F6EFE1` | Champagne page ground |
| `--red` | `#E4002B` | Techcombank red — primary accent, Method B |
| `--gold` | `#A67C3D` | Secondary accent, Method A |
| `--ink` | `#1A1614` | Warm near-black text |
| `--code-bg` | `#221B17` | Dark code panels |

Fonts are system stacks (Inter / IBM Plex Mono with fallbacks) so the file stays
dependency-free.

## Content accuracy

Checked against Databricks docs as of **2026-07-31**. Two details that older
material gets wrong and that should not be regressed:

- The metric view YAML spec is **`version: 1.1`**.
- The dimension block is called **`fields`**, not `dimensions`.

Other facts asserted in the deck, with sources:

- A Genie space supports up to **30 tables**; the guidance is **five or fewer** —
  [Curate an effective Genie Agent](https://docs.databricks.com/aws/en/genie/best-practices)
- **Up to 10 synonyms** per field or measure, 255 chars each, imported into Genie
  automatically —
  [Agent metadata in metric views](https://docs.databricks.com/aws/en/uc-semantics/agent-metadata)
- Guidance priority is **SQL expressions → example SQL → text instructions**,
  the last "only as a last resort" — same best-practices page.
- Metric view YAML reference and worked example —
  [Create a metric view](https://docs.databricks.com/aws/en/metric-views/create)

## Placeholders to replace before presenting

- Slide 2 uses illustrative figures (`₫4.2bn / 4.7bn / 3.9bn`).
- Slide 10 uses NIM and CASA ratio as stand-in KPI names.
- Table names throughout (`tcb.gold.mv_sales`, `tcb.gold.fct_orders`) are
  illustrative, modelled on the TPC-H sample schema.
