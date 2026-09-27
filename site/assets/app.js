'use strict';
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
if ($('search')) {
  const projects = [...document.querySelectorAll('.project')];
  const filter = () => {
    const q = $('search').value.trim().toLowerCase(), group = $('group').value;
    let count = 0;
    projects.forEach(p => { const show = p.dataset.search.includes(q) && (!group || p.dataset.group === group); p.hidden = !show; count += Number(show); });
    $('count').textContent = `${count} project${count === 1 ? '' : 's'}`;
    $('empty').hidden = count !== 0;
  };
  $('search').addEventListener('input', filter); $('group').addEventListener('change', filter);
  const personas = {
    developer:['Start with one safe change.','Doctor → Map / Impact → Specs / Why → source edit → tests → one durable memory. Verify a real caller and acceptance criterion before relying on the summary.'],
    claude:['Use context, then verify it.','Read the injected brief when configured. Call context or impact before editing, why before guessing intent, and remember for durable learning. Cite sources, run actual checks and disclose missing tools.'],
    lead:['Review the claim behind the counter.','Compare the requirement, affected code and test evidence. Specs progress, drift checks and session summaries are separate signals. Measure review rework and accepted changes.'],
    owner:['Measure the complete task.','Compare actual model bills, enrichment, review minutes and accepted results. The compression panel estimates a source-file baseline; it is not an invoice reduction or a productivity guarantee.']
  };
  function persona(key) { const [title, text] = personas[key]; $('persona').innerHTML = `<h3>${title}</h3><p>${text}</p>`; document.querySelectorAll('[data-persona]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.persona === key))); }
  document.querySelectorAll('[data-persona]').forEach(b => b.addEventListener('click', () => persona(b.dataset.persona))); persona('developer');
  function savings() {
    const values = ['baseline','assisted','overhead'].map(id => $(id).value.trim());
    const [baseline, assisted, overhead] = values.map(Number);
    if (values.some(x => x === '') || [baseline, assisted, overhead].some(x => !Number.isFinite(x) || x < 0)) { $('saving-result').textContent = 'Enter three non-negative amounts.'; return; }
    const net = baseline - assisted - overhead;
    $('saving-result').textContent = `$${Math.abs(net).toFixed(2)} ${net >= 0 ? 'less' : 'more'} per task${baseline > 0 ? ` · ${Math.abs(net / baseline * 100).toFixed(1)}% ${net >= 0 ? 'reduction' : 'increase'}` : ' · no percentage baseline'}`;
  }
  $('calculator').addEventListener('submit', e => e.preventDefault()); $('calculator').addEventListener('input', savings); savings();
  const scoreRows = [...$('scores').children];
  $('sort').addEventListener('change', () => { const k = $('sort').value; const rows = [...scoreRows]; if(k !== 'original') rows.sort((a,b) => k === 'effort' ? +a.dataset[k] - +b.dataset[k] : +b.dataset[k] - +a.dataset[k]); $('scores').replaceChildren(...rows); });
  fetch('assets/data.json').then(r => {if(!r.ok)throw Error('Catalog unavailable'); return r.json();}).then(data => {
    $('left').value='cairn'; $('right').value='kb';
    const side = p => `<article class="compare-side"><p class="eyebrow">${esc(p.group)}</p><h3>${esc(p.name)}</h3><h4>The user and need</h4><p>${esc(p.users)}</p><p>${esc(p.trigger)}</p><h4>Core approach</h4><p>${esc(p.vision)}</p><h4>What is still missing</h4><p>${esc(p.gaps[0])}</p><h4>Recommended next step</h4><p>${esc(p.nextstep)}</p><a href="reports/${encodeURIComponent(p.id)}/REPORT.html">Read the complete report ↗</a></article>`;
    function compare() {
      const a=data.find(p=>p.id===$('left').value), b=data.find(p=>p.id===$('right').value);
      const related=a.overlap.includes(b.id)||b.overlap.includes(a.id);
      const note=a.id===b.id?'You selected the same project. Choose a different one to compare.':related?'These projects have a documented overlap. Read the portfolio decision before combining their data or authority models.':a.group===b.group?'These projects address adjacent needs in the same family. The reports do not establish a direct integration.':'These projects serve different primary jobs. Reuse may still be possible, but no existing connection is implied.';
      $('comparison').innerHTML=`<p class="overlap-note">${note} <a href="portfolio/SYNTHESIS.html">Integration decisions ↗</a></p><div class="comparison-grid">${side(a)}${side(b)}</div>`;
    }
    $('left').addEventListener('change',compare); $('right').addEventListener('change',compare); compare();
  }).catch(() => { $('comparison').innerHTML='<p>The interactive catalog could not load. Open the site through a local HTTP server, or read the <a href="portfolio/SYNTHESIS.html">full overlap table</a>.</p>'; });
}
