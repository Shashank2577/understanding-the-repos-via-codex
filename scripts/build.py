#!/usr/bin/env python3
"""Render curated reports and a dependency-free static website."""
from pathlib import Path
import hashlib, html, json, re, shutil, sys, textwrap
from urllib.parse import quote
from markdown_it import MarkdownIt
from catalog import PROJECTS
from journeys import JOURNEYS
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
if SITE.exists(): shutil.rmtree(SITE)
SITE.mkdir(exist_ok=True)
INV={r['id']:r for r in json.loads((ROOT/'inventory.json').read_text())}
MANIFEST=ROOT/'.research/manifest.json'
LOCAL={r['id']:r for r in json.loads(MANIFEST.read_text())} if MANIFEST.exists() else {}
REMOTE='https://github.com/Shashank2577/understanding-the-repos-via-codex'
E=html.escape
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
def bullets(items): return '\n'.join('- '+s for s in items)
def flow_svg(p):
    n=len(p['flow']); h=n*72+12
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 {h}" role="img" aria-label="{E(p["name"])} workflow"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="none" stroke="#6B7068"/></marker></defs>']
    for i,t in enumerate(p['flow']):
        y=10+i*72
        if i: out.append(f'<path d="M310 {y-22}V{y-3}" stroke="#6B7068" marker-end="url(#arrow)"/>')
        out.append(f'<rect x="8" y="{y}" width="604" height="50" rx="6" fill="#FBFBF8" stroke="#DADCD2"/><text x="28" y="{y+31}" font-family="system-ui,sans-serif" font-size="16" fill="#1F2328">{i+1:02d} · {E(t)}</text>')
    return ''.join(out)+'</svg>'
for p in PROJECTS:
    id=p['id']; folder=ROOT/'reports'/id; inv=INV[id]
    write(ROOT/'assets'/f'{id}-flow.svg',flow_svg(p))
    related=', '.join(f'[{next(x["name"] for x in PROJECTS if x["id"]==r)}](../{r}/REPORT.md)' for r in p['overlap'])
    report=f'''# {p['name']}

**Recommendation:** {p['verdict']}

| Snapshot | Assessment |
|---|---|
| Supplied location ID | {id} |
| Product family | {p['group']} |
| Implementation stage | {p['stage']} |
| Review date | 2026-09-26 |
| Local state | {inv['working_tree']} |

## Vision and the problem it addresses

{p['vision']}

**Who needs it:** {p['users']}

**The moment it becomes useful:** {p['trigger']}

## How it works

![Conceptual workflow for {p['name']}](../../assets/{id}-flow.svg)

This diagram summarizes the inspected design. It is not evidence of a successful end-to-end deployment. For a hands-on journey, use the [onboarding guide](ONBOARDING.md).

## How well it addresses the problem

{bullets(p['strengths'])}

These are implementation strengths. Repeated use, customer demand and measured business outcomes remain separate questions.

## What is missing or unproven

{bullets(p['gaps'])}

## Smallest useful next step

{p['nextstep']}

**Acceptance exercise:** {p['validation']}

This is a proposed validation exercise unless explicitly recorded as executed in [VALIDATION](../../VALIDATION.md).

## Position in the portfolio

Related work: {related}.

Read the [overlap and integration decisions](../../portfolio/SYNTHESIS.md) before merging features. Shared vocabulary does not guarantee shared IDs, permissions, storage or lifecycle semantics.

| Reviewer judgment, 1–5 | Score |
|---|---|
| Effort to a credible narrow pilot | {p['effort']} |
| Potential breadth and recurrence of the need | {p['upside']} |
| Integration, operational and consequence exposure | {p['risk']} |

These are ordinal planning judgments, not completion percentages or a commercial valuation. Empty/archive projects should be parked rather than treated as active bets.

## Evidence and next reading

[Source references and snapshot limits](EVIDENCE.md) · [Developer / Claude onboarding](ONBOARDING.md) · [Portfolio synthesis](../../portfolio/SYNTHESIS.md)
'''
    write(folder/'REPORT.md',report)
    rows='\n'.join(f'| {i+1}. {a} | {b} | {c} |' for i,(a,b,c) in enumerate(JOURNEYS[id]))
    extra='\nRead the [extended five-layer UI, personas and savings guide](../../onboarding/CAIRN.md).\n' if id=='cairn' else ''
    history=''
    if id=='spreix-brain': history='\n![Historical Spreix Brain graph fixture](../../assets/spreix-brain-historical.png)\n\nHistorical repository screenshot, not a current runtime check. The screen explicitly says “Phase 1 — stub extraction”; the five-entity fixture and issue badge must not be presented as a production success.\n'
    onboard=f'''# Onboarding: {p['name']}

**Goal:** understand one useful workflow, prove its result and know which responsibilities belong to the developer versus Claude.

## Environment and first start

{p['setup']}

Use the original repository’s README and local agent instructions for exact environment configuration. This report records the inspected snapshot; provider availability, credentials and external services were not assumed to work. Begin with synthetic data and the smallest complete workflow below.

## Interface journey

The steps describe expected behavior from the inspected implementation/documentation. They are a validation script, not a claim that every click was exercised. Actual checks are listed in [VALIDATION](../../VALIDATION.md).

| Step | Developer / user action | What should be observable |
|---|---|---|
{rows}
{history}{extra}
## What Claude should do

{p['claude']}

A useful starting instruction is: “Help me complete the first workflow in this guide. Check the current README and configuration, identify any unavailable dependency, show the source evidence behind the result, and run the relevant acceptance check. Distinguish what you observed from what you inferred.”

If a tool or provider fails, Claude should name the failed dependency, preserve successful intermediate work and report the degraded state. It should not replace an unavailable result with a confident-looking invented answer. A screenshot, generated summary or green counter is evidence of only the state it actually shows.

## Use it by role

| Role | First objective | Evidence of value |
|---|---|---|
| End user / individual developer | Complete the three-step journey for the problem below | A useful result whose supporting source can be checked |
| Implementing developer | Trace input → transformation → persistence/output; then test failure and replay | Correct identifiers, no silent duplicate work, actionable error state |
| Reviewer / team lead | Challenge one result and inspect its derivation | Corrections survive the next run and limitations stay visible |
| Owner / operator | Prove setup, scope, permissions and cost behavior in the intended environment | Repeatable operation without hidden manual repair |
| Claude / coding assistant | Follow the repository-specific role described above | Real tool results, scoped changes, explicit verification and no invented evidence |

The concrete user problem is: {p['trigger']}

## Validate that it works

{p['validation']}

Keep a small record: source revision, fixture/input ID, command or UI action, expected output, actual output and failure details. Test presence and code inspection are not substitutes for running this exercise. Current demonstrated strengths and gaps are in the [report](REPORT.md).

## Measure usefulness and savings

No measured financial ROI was established for this project. Time yourself completing the same meaningful task manually and with the tool; include setup amortization, correction/review time, provider charges and retry/support time. Compare accepted results of similar quality. A higher activity count is not automatically higher productivity.

For this project, begin with its smallest useful experiment: {p['nextstep']}

The [Cairn savings guide](../../onboarding/CAIRN.md) explains the distinction between context compression, added cost and measured task outcomes. Its dollar example is hypothetical and should not be reused as this product’s ROI.

## Read next

[Report](REPORT.md) · [Evidence](EVIDENCE.md) · [Portfolio boundaries](../../portfolio/SYNTHESIS.md)
'''
    write(folder/'ONBOARDING.md',onboard)
    # Retain hashed evidence on builds from published source without local checkouts.
    if LOCAL or not (folder/'EVIDENCE.md').exists():
        evidence=[]
        for path,line in p['evidence']:
            local=Path(LOCAL[id]['path'])/path if id in LOCAL else None
            digest=hashlib.sha256(local.read_bytes()).hexdigest() if local and local.is_file() else 'not available in local snapshot'
            remote=(inv['remote'] or '').removesuffix('.git')
            link=f'[{path}:{line}]({remote}/blob/{inv["commit"]}/{quote(path)}#L{line})' if remote and inv['commit'] else f'`{path}:{line}`'
            evidence.append(f'### {link}\n\nLocal snapshot SHA-256: `{digest}`\n')
        write(folder/'EVIDENCE.md',f'''# Evidence: {p['name']}

Reviewed 2026-09-26. Source HEAD: `{inv['commit'] or 'no git history'}`. Working tree: **{inv['working_tree']}**. Inventory counts {inv['tracked_files']} tracked/bundle files; this is not a count of files individually reviewed.

Source links are pinned to HEAD where possible. Pre-existing dirty files and untracked additions can differ or be absent from these links. File hashes below identify the local bytes inspected; this atlas does not redistribute the source. Private links require access. Non-git bundles have path references only.

{''.join(evidence) if evidence else 'The supplied directory was empty; there are no code references.'}

## Confidence and validation

Representative implementation, configuration and documentation paths were inspected. [VALIDATION](../../VALIDATION.md) records commands actually executed and environment failures. Acceptance exercises in the report/onboarding are proposed work unless that ledger explicitly records them as performed.

See [methodology](../../METHODOLOGY.md) for evidence labels and [assets provenance](../../ASSETS.md) for screenshots. This review does not certify production reliability, isolation, accuracy or commercial demand.
''')
    write(folder/'STATUS.md',f'# {p["name"]} — review status\n\nReport, onboarding, workflow diagram and source evidence complete for the 2026-09-26 snapshot.\n\nNext validation: {p["validation"]}\n')
# Markdown-to-HTML rendering, preserving relative report and asset paths.
def page(title,body,depth=0,source=None,wide=False,route=''):
    pre='../'*depth
    source_link=f'<a href="{REMOTE}/blob/main/{source}">Read Markdown ↗</a>' if source else ''
    home=f'{pre}index.html'; projects=f'{pre}projects.html'; decisions=f'{pre}portfolio/SYNTHESIS.html'; guide=f'{pre}onboarding/CAIRN.html'
    active=lambda token: ' aria-current="page"' if route==token else ''
    nav=f'<header class="mast"><a class="brand" href="{home}">FIELD GUIDE <span> / CODEX</span></a><nav aria-label="Main navigation"><a href="{home}"{active("index.html")}>Start here</a><a href="{projects}"{active("projects.html")}>Explore 20 projects</a><a href="{decisions}"{active("portfolio/SYNTHESIS.md")}>Portfolio direction</a><a href="{guide}"{active("onboarding/CAIRN.md")}>Developer &amp; Claude guide</a></nav></header>'
    context=''
    if route.startswith('reports/'):
        bits=route.split('/'); id=bits[1]; label=bits[-1].replace('.md','').replace('.html','').replace('REPORT','Report').replace('ONBOARDING','Onboarding').replace('EVIDENCE','Evidence')
        data=next(x for x in PROJECTS if x['id']==id); base=f'{pre}reports/{id}/'
        context=f'<div class="contextbar"><div class="breadcrumbs"><a href="{home}">Start</a><span>/</span><a href="{projects}">Projects</a><span>/</span><strong>{E(data["name"])}</strong><span>/</span><span>{E(label)}</span></div><nav aria-label="Project guide"><a href="{base}REPORT.html">Report</a><a href="{base}ONBOARDING.html">How to use</a><a href="{base}EVIDENCE.html">Evidence</a><a href="{projects}">← All projects</a></nav></div>'
    elif route.startswith('portfolio/') or route.startswith('onboarding/'):
        label='Portfolio decisions' if route.startswith('portfolio/') else 'Onboarding'
        context=f'<div class="contextbar"><div class="breadcrumbs"><a href="{home}">Start</a><span>/</span><a href="{projects}">Explore projects</a><span>/</span><span>{label}</span></div><a href="{projects}">← Explore all projects</a></div>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="A source-grounded field guide to twenty repositories: vision, architecture, overlap, onboarding and evidence."><title>{E(title)} · Repository atlas</title><link rel="stylesheet" href="{pre}assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a>{nav}{context}<main id="main" class="{'wide' if wide else 'document'}">{body}</main><footer><span>Snapshot · 26 September 2026</span><a href="{pre}METHODOLOGY.html">Method &amp; limits</a><a href="{pre}VALIDATION.html">What was tested</a>{source_link}<a href="{REMOTE}">GitHub ↗</a></footer><script src="{pre}assets/app.js" defer></script></body></html>'''
def render_doc(path):
    rel=path.relative_to(ROOT);src=path.read_text()
    body=md.render(src)
    body=re.sub(r'href="([^"#:?]+)\.md([#?][^"]*)?"',lambda m:f'href="{m[1]}.html{m[2] or ""}"',body)
    body=re.sub(r'<table>', '<p class="table-hint">On a small screen, swipe horizontally to read every column.</p><div class="table-wrap" tabindex="0" role="region" aria-label="Scrollable comparison"><table>',body).replace('</table>','</table></div>')
    body=re.sub(r'<h2>(.*?)</h2>',lambda m:f'<h2 id="{re.sub(r"[^a-z0-9]+","-",m[1].lower()).strip("-")}">{m[1]}</h2>',body)
    headings=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>',body)
    toc='<details class="toc"><summary>On this page</summary><ol>'+''.join(f'<li><a href="#{id}">{t}</a></li>' for id,t in headings)+'</ol></details>' if headings else ''
    title=src.splitlines()[0].lstrip('# ')
    body=body.replace('</h1>','</h1>'+toc,1)
    route=str(rel)
    write(SITE/rel.with_suffix('.html'),page(title,body,len(rel.parts)-1,str(rel),route=route))
for path in sorted(ROOT.glob('*.md')):
    if not path.name.startswith('.'): render_doc(path)
for base in ['reports','portfolio','onboarding']:
    for path in sorted((ROOT/base).rglob('*.md')): render_doc(path)
shutil.copytree(ROOT/'assets',SITE/'assets',dirs_exist_ok=True)
write(SITE/'assets/data.json',json.dumps(PROJECTS,ensure_ascii=False))
# Hero and progressive-enhancement project directory.
cards=''.join(f'''<article class="project" data-group="{E(p['group'])}" data-search="{E((p['name']+' '+p['id']+' '+p['group']+' '+p['vision']).lower())}"><div class="project-meta"><span>{i+1:02d}</span><span>{E(p['group'])}</span></div><h3><a href="reports/{p['id']}/REPORT.html">{E(p['name'])} <span aria-hidden="true">↗</span></a></h3><p class="stage">{E(p['stage'])}</p><p>{E(p['verdict'])}</p><div class="project-links"><a href="reports/{p['id']}/ONBOARDING.html">How to use</a><a href="reports/{p['id']}/EVIDENCE.html">Evidence</a></div></article>''' for i,p in enumerate(PROJECTS))
options=''.join(f'<option value="{p["id"]}">{E(p["name"])}</option>' for p in PROJECTS)
groups=''.join(f'<option>{E(g)}</option>' for g in dict.fromkeys(p['group'] for p in PROJECTS))
score_rows=''.join(f'<tr data-effort="{p["effort"]}" data-upside="{p["upside"]}" data-risk="{p["risk"]}"><th scope="row"><a href="reports/{p["id"]}/REPORT.html">{E(p["name"])}</a></th><td>{p["effort"]}</td><td>{p["upside"]}</td><td>{p["risk"]}</td></tr>' for p in PROJECTS)
body=f'''<section class="hero"><div><p class="eyebrow">A FIELD GUIDE TO THE WORK ALREADY HERE</p><h1>Twenty repositories.<br>Three coherent directions.</h1><p class="lede">Understand what each project does, where the ideas overlap, and which work deserves the next week of attention.</p><div class="actions"><a class="button" href="#projects">Explore the repositories ↓</a><a class="text-link" href="portfolio/SYNTHESIS.html">Read the portfolio decisions ↗</a></div></div><aside class="editor-note"><span class="eyebrow">THE CENTRAL FINDING</span><p>Consolidate around a user’s job. Preserve the useful pieces. Prove one complete workflow before expanding the platform.</p><p class="small">Local source review · selected tests · live Cairn screens.<br>Recommendations are hypotheses, not market validation.</p></aside></section>
<div class="ledger"><div><strong>20</strong><span>locations reviewed</span></div><div><strong>3</strong><span>proposed product lines</span></div><div><strong>4</strong><span>projects with test runs</span></div><div><strong>1</strong><span>empty directory surfaced</span></div></div>
<section id="map"><div class="section-heading"><div><p class="eyebrow">01 / THE PORTFOLIO</p><h2>Organize by the problem.</h2></div><p>This is a recommended structure. The lines below describe possible collaboration, not existing integrations.</p></div><div class="lanes"><article><span class="lane-number">01</span><h3>Engineering evidence</h3><p>“Can we support our delivery and AI-use claims?”</p><p><strong>Receipts + Prompture</strong><br>Sovix CLI provides a small entry point. Evaluate Qmmit’s capture pieces before consolidating.</p></article><article><span class="lane-number">02</span><h3>Agent memory &amp; delivery</h3><p>“Can agents change code without relearning it?”</p><p><strong>Cairn + Foundry</strong><br>Architecture Foundry and Java rules add discipline. Keep knowledge separate from permission to act.</p></article><article><span class="lane-number">03</span><h3>Team knowledge &amp; action</h3><p>“What did we decide, and what happens next?”</p><p><strong>Notetaker → Spreix Platform</strong><br>Cortex’s compiler and Brain’s uncertainty inbox are complementary building blocks.</p></article></div><p class="aside-note">OBSERVE has a distinct operations buyer. Lumen is a document-platform choice. FreeLLMAPI is infrastructure; Scratch is a local writing surface. Empty and seed folders are not additional businesses.</p></section>
<section class="split" id="decisions"><div><p class="eyebrow">02 / THE NEXT MOVE</p><h2>Start small.<br>Make the result inspectable.</h2><ol class="editor-list"><li><strong>Ship an evidence review.</strong> Use Receipts and Sovix CLI with one fixed corpus, one disputed metric and reproducible arithmetic.</li><li><strong>Prove Cairn’s task benefit.</strong> Measure total cost and accepted-change time, including follow-up reads and enrichment.</li><li><strong>Close the meeting loop.</strong> Recording → cited decision → corrected knowledge → reviewed draft. Replays must not duplicate work.</li></ol><a href="portfolio/SYNTHESIS.html">See estimates, integration contracts and stop conditions ↗</a></div><aside class="stakes"><p class="eyebrow">HIGHEST STAKES</p><h3>Platform, Foundry, OBSERVE</h3><p>Potentially broad recurring value, with larger operational responsibilities: tenant isolation, agent authority and production diagnosis.</p><hr><p><strong>Before more scope:</strong> require an independent pilot, a clear failure test and a measured outcome.</p><p class="small">Cairn and Meeting Intelligence offer narrower daily or weekly workflows to validate first.</p></aside></section>
<section id="projects"><div class="section-heading"><div><p class="eyebrow">03 / THE REPOSITORY INDEX</p><h2>Every project, with its evidence.</h2></div><p>Each folder contains a report, developer/Claude onboarding, source references and a visual workflow.</p></div><div class="filters"><label>Find a project<input id="search" type="search" placeholder="Name, problem or local folder…"></label><label>Product family<select id="group"><option value="">All families</option>{groups}</select></label><output id="count" aria-live="polite">20 projects</output></div><div class="project-grid">{cards}</div><p id="empty" hidden>No projects match. Clear the search or choose all families.</p></section>
<section id="compare"><div class="section-heading"><div><p class="eyebrow">04 / WHERE THEY OVERLAP</p><h2>Compare the actual jobs.</h2></div><p>A shared word such as “brain” or “agent” is not enough reason to merge two systems.</p></div><div class="compare-controls"><label>First project<select id="left">{options}</select></label><label>Second project<select id="right">{options}</select></label></div><div id="comparison" aria-live="polite"><p>Choose two projects to compare their roles, workflows and gaps. The full overlap table is also available in the <a href="portfolio/SYNTHESIS.html">portfolio report</a>.</p></div></section>
<section id="onboarding"><div class="section-heading"><div><p class="eyebrow">05 / FIRST SUCCESS</p><h2>What you do. What Claude does.</h2></div><p>Cairn’s five layers are explained in depth, with real screens, fixture exercises and a careful reading of savings.</p></div><div class="persona-buttons" role="group" aria-label="Choose your role"><button data-persona="developer" aria-pressed="true">Developer</button><button data-persona="claude" aria-pressed="false">Claude</button><button data-persona="lead" aria-pressed="false">Team lead</button><button data-persona="owner" aria-pressed="false">Owner / finance</button></div><div id="persona" class="persona" aria-live="polite"></div><div class="screen-pair"><figure><a href="assets/cairn-map-live.png"><img loading="lazy" src="assets/cairn-map-live.png" alt="Live Cairn Map with code communities and source areas" width="2048" height="1119"></a><figcaption>LIVE UI · Map shows structure and provenance. Graph size does not establish accuracy.</figcaption></figure><figure><a href="assets/cairn-specs-live.png"><img loading="lazy" src="assets/cairn-specs-live.png" alt="Live Cairn Specs with 75 tasks done and Analyze still offered as next stage" width="2048" height="1119"></a><figcaption>LIVE UI · 75/75 tasks coexist with an open Analyze stage. Completion and verification differ.</figcaption></figure></div><a class="button" href="onboarding/CAIRN.html">Read the full five-layer onboarding ↗</a></section>
<section class="split" id="savings"><div><p class="eyebrow">06 / UNDERSTAND THE SAVINGS</p><h2>Compression is one measure.<br>Task economics is another.</h2><p>The live Cairn panel showed 391 estimated tokens sent against a 144,228 source-file estimate: about 369×. It did not measure what an agent otherwise would have read.</p><a href="assets/cairn-overview-live.png"><img class="savings-shot" loading="lazy" src="assets/cairn-overview-live.png" alt="Cairn live context comparison: 391 tokens versus an estimated 144228 source tokens"></a><p class="small">Existing local records, not a benchmark created in this review. Full explanation and scope caveats are in the <a href="onboarding/CAIRN.html">onboarding guide</a>.</p></div><form class="calculator" id="calculator"><p class="eyebrow">HYPOTHETICAL TASK CALCULATOR</p><h3>Would the task cost less?</h3><label>Baseline task cost ($)<input id="baseline" type="number" min="0" step="0.01" value="1.20" required></label><label>Assisted task cost, including reads ($)<input id="assisted" type="number" min="0" step="0.01" value="0.65" required></label><label>Extra attributable enrichment / infrastructure ($)<input id="overhead" type="number" min="0" step="0.01" value="0.10" required></label><output id="saving-result" aria-live="polite"></output><p class="small">Illustrative inputs, not product results or current model prices. Do not count overhead twice. Compare accepted results of similar quality.</p></form></section>
<section id="ranking"><div class="section-heading"><div><p class="eyebrow">07 / EFFORT, UPSIDE &amp; EXPOSURE</p><h2>Tradeoffs, without a fake winner score.</h2></div><p>Reviewer judgments from 1 (low) to 5 (high). Effort means reaching a narrow credible pilot. Upside means plausible breadth and recurrence of the need.</p></div><label class="sort-label">Sort by<select id="sort"><option value="original">Portfolio order</option><option value="effort">Lowest pilot effort</option><option value="upside">Highest potential upside</option><option value="risk">Highest exposure</option></select></label><div class="table-wrap" tabindex="0" role="region" aria-label="Project tradeoff scores"><table><thead><tr><th scope="col">Project</th><th scope="col">Effort / 5</th><th scope="col">Upside / 5</th><th scope="col">Risk / 5</th></tr></thead><tbody id="scores">{score_rows}</tbody></table></div><p class="small">Park the empty Company Brain directory and Stage 0 seed. Scores do not make them implemented products or prove customer demand.</p></section>
<section class="closing"><p class="eyebrow">THE WORK IS SAVED</p><h2>A durable home for the understanding.</h2><p>The brief, source snapshots, decisions, onboarding and validation record are committed together. Future sessions can continue from the documentation.</p><div class="actions"><a href="onboarding/MAINTAINER.html">Developer &amp; Claude maintainer guide ↗</a><a href="VALIDATION.html">What was actually tested ↗</a><a href="METHODOLOGY.html">Read the review limits ↗</a></div></section>'''
write(SITE/'projects.html',page('Explore all 20 repositories',body,wide=True,route='projects.html'))
home_body='''<section class="hero home-hero"><div><p class="eyebrow">THE FIELD GUIDE TO YOUR SOFTWARE PORTFOLIO</p><h1>Make the agent era<br>work you can trust.</h1><p class="lede">Give coding agents reliable context. Bound what they can do. Show people what they changed and what the evidence says.</p><p class="vision-note">That is the clearest shared direction across this portfolio. The pieces already exist in different repositories; they are not integrated into one product today.</p><div class="actions"><a class="button" href="portfolio/SYNTHESIS.html">See the recommended direction →</a><a class="text-link" href="projects.html">Browse all 20 projects</a></div></div><aside class="editor-note"><span class="eyebrow">THE RECOMMENDATION</span><p>Cairn remembers.<br>Foundry bounds the work.<br>Receipts shows the evidence.</p><p class="small">Explore those as one product direction through a narrow pilot. Keep meetings, observability, and model routing distinct until users prove the connections.</p></aside></section>
<section class="home-three"><p class="eyebrow">ONE VISION · THREE NECESSARY JOBS</p><div class="home-columns"><article><span>01 / REMEMBER</span><h2>Give agents the right context.</h2><p>Cairn maps code, requirements, history, memory and prior agent sessions.</p><a href="reports/cairn/REPORT.html">See Cairn’s evidence and gaps →</a></article><article><span>02 / BOUND</span><h2>Keep changes inside the rules.</h2><p>Foundry dispatches scoped work to agents, then routes it through human and executable gates.</p><a href="reports/aisdlc/REPORT.html">See Foundry’s evidence and gaps →</a></article><article><span>03 / PROVE</span><h2>Show what actually happened.</h2><p>Receipts and Sovix CLI make engineering measurements reproducible. Prompture adds detailed capture.</p><a href="reports/github-2/REPORT.html">See Receipts’ evidence and gaps →</a></article></div><p class="direction-note"><strong>Portfolio recommendation:</strong> these projects currently have different storage, identities, permissions and operating models. The synthesis defines what a pilot must prove before connecting them.</p></section>
<section class="home-route"><div><p class="eyebrow">PICK UP WHERE YOU ARE</p><h2>What are you trying to understand?</h2></div><div class="route-cards"><a href="projects.html"><span>01 · SURVEY</span><h3>Find the project</h3><p>Search all 20. Open the vision, users, workflow, gaps and test instructions.</p><b>Explore the directory →</b></a><a href="portfolio/SYNTHESIS.html"><span>02 · DECIDE</span><h3>Choose what to build next</h3><p>Compare overlaps, quick wins, product combinations and high stakes bets.</p><b>Read the recommendation →</b></a><a href="onboarding/CAIRN.html"><span>03 · START</span><h3>Onboard a developer or Claude</h3><p>Follow Cairn’s five layers with real screens, persona workflows and validation.</p><b>Open the guide →</b></a></div></section>
<section class="home-proof"><div><p class="eyebrow">EVIDENCE BEFORE CONFIDENCE</p><h2>Know what was actually checked.</h2><p>The review includes selected source paths, four local test runs, a read-only look at Cairn’s interface and a separate validation record. Most products were not deployed or tested end to end.</p><a href="VALIDATION.html">See test results and limits →</a></div><div class="proof-counts"><p><strong>20</strong> repository locations</p><p><strong>4</strong> projects with test commands run</p><p><strong>1</strong> intentionally surfaced empty directory</p><p><strong>0</strong> customer ROI studies</p></div></section>'''
write(SITE/'index.html',page('Start here · Understanding the repositories',home_body,wide=True,route='index.html'))
write(SITE/'.nojekyll','')
print(f'Built {len(PROJECTS)} project reports and {len(list(SITE.rglob("*.html")))} HTML pages.')
