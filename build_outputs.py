# -*- coding: utf-8 -*-
"""
Builder script to generate:
1. speech_video_processing_handbook.html & index.html (Self-contained offline mobile study app with Student Exam Notes)
2. Speech_and_Video_Processing_Complete_Study_Guide.md (Comprehensive Markdown guide with 5M & 10M notes)
"""

import os, json, re, html
from tier_data import QUESTION_TIER_DATA
from keypoints_data import KEYPOINTS_DATA
from diagrams_data import DIAGRAMS_SVG
from eli5_data import ELI5_DATA
from data_unit1 import UNIT1_QUESTIONS
from data_unit2 import UNIT2_QUESTIONS
from data_unit3 import UNIT3_QUESTIONS
from data_unit4 import UNIT4_QUESTIONS
from data_unit5 import UNIT5_QUESTIONS

ALL_QUESTIONS = UNIT1_QUESTIONS + UNIT2_QUESTIONS + UNIT3_QUESTIONS + UNIT4_QUESTIONS + UNIT5_QUESTIONS

# Enrich each question with priority, tier, keypoints, eli5, and visual diagram
for q in ALL_QUESTIONS:
    qid = q['id']
    t_data = QUESTION_TIER_DATA.get(qid, {
        'rank': 99, 'tier': 3, 'tier_name': 'Standard',
        'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': ''
    })
    q.update(t_data)
    q['key_points'] = KEYPOINTS_DATA.get(qid, [])
    q['eli5'] = ELI5_DATA.get(qid, {})
    q['svg_diagram'] = DIAGRAMS_SVG.get(qid, '')

def inline_md(txt):
    txt = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', txt)
    txt = re.sub(r'\*(.+?)\*', r'<em>\1</em>', txt)
    txt = re.sub(r'`(.+?)`', r'<code>\1</code>', txt)
    txt = txt.replace(r'\mu', 'µ').replace(r'\text{', '').replace(r'}', '')
    txt = txt.replace(r'\times', '×').replace(r'\approx', '≈').replace(r'\le', '≤')
    txt = txt.replace(r'\ge', '≥').replace(r'\phi', 'φ').replace(r'\lambda', 'λ')
    txt = txt.replace(r'\nu', 'ν').replace(r'\circ', '°').replace(r'\Delta', 'Δ')
    txt = txt.replace(r'\sum', 'Σ').replace(r'\in', '∈').replace(r'\infty', '∞')
    txt = txt.replace(r'\\', '')
    txt = txt.replace('$', '')
    return txt

def md_to_html_simple(md_text):
    """Converts basic markdown formatting into HTML."""
    lines = md_text.split('\n')
    out = []
    in_table = False
    table_lines = []
    
    def process_table(tbl_lines):
        if not tbl_lines:
            return ""
        html_tbl = ['<div class="table-wrapper"><table>']
        headers = [c.strip() for c in tbl_lines[0].strip('|').split('|')]
        html_tbl.append('<thead><tr>' + ''.join(f'<th>{html.escape(h)}</th>' for h in headers) + '</tr></thead>')
        html_tbl.append('<tbody>')
        for row in tbl_lines[2:]:
            cols = [c.strip() for c in row.strip('|').split('|')]
            if any(cols):
                html_tbl.append('<tr>' + ''.join(f'<td>{inline_md(c)}</td>' for c in cols) + '</tr>')
        html_tbl.append('</tbody></table></div>')
        return '\n'.join(html_tbl)

    i = 0
    while i < len(lines):
        line = lines[i]
        trimmed = line.strip()

        if trimmed.startswith('|') and trimmed.endswith('|'):
            if not in_table:
                in_table = True
                table_lines = [trimmed]
            else:
                table_lines.append(trimmed)
            i += 1
            continue
        else:
            if in_table:
                out.append(process_table(table_lines))
                in_table = False
                table_lines = []

        if not trimmed:
            out.append('<div class="spacer"></div>')
            i += 1
            continue

        if trimmed.startswith('### '):
            out.append(f'<h4 class="sub-heading">{inline_md(trimmed[4:])}</h4>')
        elif trimmed.startswith('#### '):
            out.append(f'<h5 class="sub-sub-heading">{inline_md(trimmed[5:])}</h5>')
        elif trimmed.startswith('---'):
            out.append('<hr class="divider"/>')
        elif trimmed.startswith('* ') or trimmed.startswith('- '):
            out.append(f'<li class="bullet-item">{inline_md(trimmed[2:])}</li>')
        elif re.match(r'^\d+\.\s', trimmed):
            num = re.match(r'^\d+\.', trimmed).group(0)
            rest = trimmed[len(num):].strip()
            out.append(f'<li class="numbered-item"><strong>{num}</strong> {inline_md(rest)}</li>')
        else:
            out.append(f'<p class="para">{inline_md(trimmed)}</p>')
        i += 1

    if in_table:
        out.append(process_table(table_lines))

    return '\n'.join(out)

def generate_markdown_guide():
    md_parts = [
        "# SPEECH AND VIDEO PROCESSING (SVP) — COMPLETE MASTER STUDY GUIDE",
        "**Year/Sem:** B.Tech IV Year I Sem | **Branch:** AI & ML | **Regulation:** KGR23 | **Course Code:** KG23ACM408",
        "**Course Coordinator:** Dr. Sandeep Kumar M | **Academic Year:** 2026-27",
        "",
        "> [!IMPORTANT]",
        "> Scaled strictly by marks (**05 Marks vs 10 Marks**). Contains 100% of questions across **Mid-I and Mid-II (40 Questions Total)** covering all 5 units, with complete step-by-step solved numericals, mnemonics, analogies, and exam sketches.",
        "",
        "---",
        ""
    ]

    for q in ALL_QUESTIONS:
        md_parts.append(f"## {q['id']}: [{q['mid']} Q{q['qno']}] {q['title']}")
        md_parts.append(f"**Unit:** {q['unit']} | **Marks:** {q['marks']} | **Bloom:** {q['bloom']} | **CO:** {q['co']} | **Rank:** #{q['rank']} (Tier {q['tier']}: {q['tier_name']})")
        md_parts.append(f"**⚡ 30-Sec Anchor:** {q['punchline']}")
        md_parts.append(f"**🎯 Mnemonic:** `{q['mnemonic']}`")
        md_parts.append(f"**💡 Analogy:** *{q['analogy']}*")
        md_parts.append("")

        # ELI5 Block
        eli5 = q.get('eli5', {})
        if eli5:
            md_parts.append("### 👶 ELI5 (Explain Like I'm 5):")
            md_parts.append(f"- **In Plain English:** {eli5.get('plain', '')}")
            md_parts.append(f"- **Magic Exam Keywords:** `{eli5.get('keywords', '')}`")
            md_parts.append(f"- **What to Draw on Paper:** {eli5.get('draw', '')}")
            md_parts.append("")

        # Key Points
        kps = q.get('key_points', [])
        if kps:
            md_parts.append("### 🎯 High-Yield Key Points:")
            for kp in kps:
                md_parts.append(f"- {kp}")
            md_parts.append("")

        # Diagram
        md_parts.append("### 📝 Pen-and-Paper Exam Diagram Blueprint:")
        md_parts.append("```text")
        md_parts.append(q['diagram'].strip())
        md_parts.append("```")
        md_parts.append("")

        # Content
        md_parts.append("### 📖 Comprehensive Exam Notes:")
        md_parts.append(q['content'].strip())
        md_parts.append("")
        md_parts.append("---")
        md_parts.append("")

    full_md = '\n'.join(md_parts)
    out_path = os.path.join(r'svp_study_suite', 'Speech_and_Video_Processing_Complete_Study_Guide.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_md)
    print(f"Saved {out_path} successfully ({len(full_md)} bytes).")

def generate_html_handbook():
    tier_summary = {1: 0, 2: 0, 3: 0, 4: 0}
    for q in ALL_QUESTIONS:
        t = q.get('tier', 3)
        tier_summary[t] = tier_summary.get(t, 0) + 1

    html_parts = ["""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<meta name="theme-color" content="#090d16">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>Speech &amp; Video Processing • Master Handbook (KGR23 Regulation)</title>
<link rel="stylesheet" href="style.css">
</head>
<body class="theme-dark">

<header class="app-header">
  <div class="header-inner">
    <div class="brand-group">
      <div class="brand-badge">SVP • KGR23</div>
      <h1 class="brand-title">Speech &amp; Video Processing <span class="brand-sub">Master Exam Handbook</span></h1>
    </div>

    <!-- Dual-Mode Lo-Fi Audio Lounge Controller -->
    <div class="audio-hud" id="audioHud">
      <div class="audio-ctrl-group">
        <button class="audio-play-btn" id="audioPlayToggle" title="Play / Pause Lo-Fi Audio">
          <span id="audioPlayIcon">▶</span>
        </button>
        <select class="audio-channel-select" id="audioChannelSelect" title="Select Lo-Fi Channel">
          <optgroup label="📻 VERIFIED 24/7 ONLINE LIVE STREAMS">
            <option value="stream_chillhop" selected>☕ 24/7 Chillhop &amp; Lofi Radio</option>
            <option value="stream_fluxfm">🎧 FluxFM ChillHop (Berlin 24/7)</option>
            <option value="stream_radioco">📻 24/7 Lo-Fi Cafe Radio</option>
            <option value="stream_lautfm">🏙️ Berlin Lo-Fi Lounge</option>
          </optgroup>
          <optgroup label="🎮 NINTENDO &amp; VIDEO GAME LO-FI">
            <option value="stream_vgm_covers">🍄 Live: Nintendo &amp; Game Remixes</option>
            <option value="stream_vgm_all">🎮 Live: Video Game Lofi &amp; VGM</option>
            <option value="stream_vgm_ocremix">⚔️ Live: OverClocked ReMix (VGM)</option>
            <option value="stream_vgm_chiptune">👾 Live: 8-Bit Chiptune Radio</option>
          </optgroup>
          <optgroup label="🌌 VAPORWAVE &amp; DOWNTEMPO">
            <option value="stream_nightwave">🌌 Nightwave Plaza (Vaporwave &amp; Lofi)</option>
            <option value="stream_groovesalad">🥗 SomaFM Groove Salad (Downtempo)</option>
            <option value="stream_lush">🌸 SomaFM Lush (Mellow Vocals &amp; Chill)</option>
            <option value="stream_dronezone">🚀 SomaFM Drone Zone (Deep Space)</option>
            <option value="stream_chillout">🍃 Ambient Chillout Lounge</option>
          </optgroup>
          <optgroup label="🌧️ AMBIENT FOCUS SOUNDSCAPES (OFFLINE)">
            <option value="rain">🌧️ Rain on Window</option>
            <option value="binaural">🧠 40Hz Deep Focus (Gamma)</option>
            <option value="brown_noise">📻 Deep Brown Noise (Calming)</option>
            <option value="lofi_synth">🎹 Generative Jazz Piano</option>
            <option value="lofi_beats">🎧 Offline Lo-Fi Beats (Backup)</option>
          </optgroup>
        </select>
        <span class="audio-status-pill" id="audioStatusPill" title="Audio Status">Ready</span>
        <input type="range" class="audio-vol-slider" id="audioVolSlider" min="0" max="1" step="0.05" value="0.85" title="Volume">
        <button class="audio-layer-btn active" id="ambientVinylBtn" title="Vinyl Crackle (Toggle)">📻</button>
        <button class="audio-layer-btn" id="ambientRainBtn" title="Rain Layer (Toggle)">🌧️</button>
        <button class="yt-lounge-btn" id="ytLoungeToggleBtn" title="YouTube Lo-Fi Lounge Mini-Player">📺 YT</button>
        <audio id="liveRadioAudio" preload="none"></audio>
      </div>

      <div class="header-actions">
        <button class="btn-icon" id="themeToggle" title="Toggle Theme">🌓</button>
        <button class="btn-icon" id="expandToggle" title="Expand / Collapse All Cards">📖 Expand All</button>
        <button class="btn-icon" id="modeToggle" title="Quick Flashcard Mode">⚡ Punchlines</button>
        <button class="btn-icon" onclick="window.print()" title="Print / PDF">🖨️ PDF</button>
      </div>
    </div>
  </div>
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="searchInput" class="search-input" placeholder="Search: Source-Filter, MFCC, LPC, DTW, HMM, 2D-DCT, Optical Flow, Kalman, 5 Marks, 10 Marks..." autocomplete="off">
  </div>
</header>

<div class="filter-bar" id="filterBar">
  <button class="filter-chip active" data-filter="all">All (40)</button>
  <button class="filter-chip chip-important" data-filter="important">🔥 Free Marks &amp; Numericals</button>
  <button class="filter-chip chip-keypoints" data-filter="keypoints">🎯 Key Points Only (Shortest)</button>
  <button class="filter-chip" data-filter="5m">⚡ 5 Marks (20)</button>
  <button class="filter-chip" data-filter="10m">⚔️ 10 Marks (20)</button>
  <button class="filter-chip" data-filter="tier1">⚡ Tier 1: Free Marks (""" + str(tier_summary[1]) + """)</button>
  <button class="filter-chip" data-filter="tier2">⚔️ Tier 2: Core Scoring (""" + str(tier_summary[2]) + """)</button>
  <button class="filter-chip" data-filter="tier3">🛡️ Tier 3: High-Value 10M (""" + str(tier_summary[3]) + """)</button>
  <button class="filter-chip" data-filter="tier4">🧩 Tier 4: Deep Dive (""" + str(tier_summary[4]) + """)</button>
  <button class="filter-chip" data-filter="mid1">Mid-I (20)</button>
  <button class="filter-chip" data-filter="mid2">Mid-II (20)</button>
  <button class="filter-chip" data-filter="u1">Unit 1</button>
  <button class="filter-chip" data-filter="u2">Unit 2</button>
  <button class="filter-chip" data-filter="u3">Unit 3</button>
  <button class="filter-chip" data-filter="u4">Unit 4</button>
  <button class="filter-chip" data-filter="u5">Unit 5</button>
</div>

<div class="container">
  <!-- Emergency Triage Banner -->
  <div class="triage-banner">
    <div class="triage-header">
      <div class="triage-title">🚀 Cramming Triage: Disregard Units, Follow the Tiers!</div>
    </div>
    <div class="triage-desc">
      When short on time, do <strong>NOT</strong> study in syllabus order (Unit 1 to 5). Study in order of <strong>Rank 1 to 40</strong> below.
      Click <strong>"⚡ Tier 1: Free Marks"</strong> for direct scoring numericals, <strong>"🎯 Key Points Only"</strong> for 60-second essentials, or filter by <strong>"⚡ 5 Marks"</strong> / <strong>"⚔️ 10 Marks"</strong>!
    </div>
    <div class="tier-pills-grid">
      <div class="tier-summary-card t1" onclick="filterByTier('tier1')">
        <div class="tier-summary-title">
          <span style="color:#6ee7b7;">⚡ Tier 1: Free Marks</span>
          <span style="color:#a7f3d0;">10 Qs • ~25m</span>
        </div>
        <div class="tier-summary-desc">Pure numericals (BME, SAD, Framing, Kalman, Pole-Zero) &amp; core definitions.</div>
      </div>
      <div class="tier-summary-card t2" onclick="filterByTier('tier2')">
        <div class="tier-summary-title">
          <span style="color:#93c5fd;">⚔️ Tier 2: Core Scoring</span>
          <span style="color:#bfdbfe;">12 Qs • ~35m</span>
        </div>
        <div class="tier-summary-desc">FFT properties, 4-point DFT, Optical flow, Change detection, 2D-DFT.</div>
      </div>
      <div class="tier-summary-card t3" onclick="filterByTier('tier3')">
        <div class="tier-summary-title">
          <span style="color:#c4b5fd;">🛡️ Tier 3: High-Value 10M</span>
          <span style="color:#ddd6fe;">12 Qs • ~50m</span>
        </div>
        <div class="tier-summary-desc">HMM, GMM-EM, LPC equations, GOP video system, Evaluation metrics.</div>
      </div>
      <div class="tier-summary-card t4" onclick="filterByTier('tier4')">
        <div class="tier-summary-title">
          <span style="color:#fda4af;">🧩 Tier 4: Deep Dive</span>
          <span style="color:#fbcfe8;">6 Qs • ~25m</span>
        </div>
        <div class="tier-summary-desc">3D Structure from Motion (SfM), VQ LBG, Non-linear optimization, 2D LSI.</div>
      </div>
    </div>
  </div>

  <!-- HUD & Sort Strip -->
  <div class="hud-strip">
    <div>Showing: <strong id="visibleCount">40</strong> / 40 Questions</div>
    <div class="sort-group">
      <span>Sort by:</span>
      <button class="sort-btn active" id="sortRankBtn">Global Rank (1-40)</button>
      <button class="sort-btn" id="sortUnitBtn">Syllabus (Unit 1-5)</button>
    </div>
  </div>

  <!-- Question Cards Grid -->
  <div class="cards-grid" id="cardsGrid">
"""]

    # Render questions sorted by rank by default
    sorted_q = sorted(ALL_QUESTIONS, key=lambda x: x['rank'])
    for q in sorted_q:
        tier_class = f"t{q['tier']}"
        marks_num = "5" if "5" in q['marks'] else "10"
        unit_slug = q['unit'].lower().replace('-', '').replace(' ', '')
        mid_slug = q['mid'].lower().replace('-', '').replace(' ', '')
        is_imp = "true" if q['tier'] == 1 else "false"

        important_badge = '<span class="badge badge-important">🔥 Free Marks</span>' if q['tier'] == 1 else ''

        # Key points markup
        kps = q.get('key_points', [])
        key_points_html = "".join([f'<li class="keypoint-item">{inline_md(k)}</li>' for k in kps])

        # ELI5 markup
        eli5 = q.get('eli5', {})
        eli5_html = ""
        if eli5:
            eli5_html = f"""
        <div class="eli5-box">
          <div class="eli5-header">
            <span class="eli5-badge">👶 ELI5 Super Summary</span>
            <span class="eli5-sub">Explain Like I'm 5 • 3-Bullet Exam Lifesaver</span>
          </div>
          <div class="eli5-body">
            <div class="eli5-bullet"><strong>In Plain English:</strong> {html.escape(eli5.get('plain', ''))}</div>
            <div class="eli5-bullet"><strong>Magic Exam Keywords:</strong> <code>{html.escape(eli5.get('keywords', ''))}</code></div>
            <div class="eli5-bullet"><strong>What to Draw / Write:</strong> {html.escape(eli5.get('draw', ''))}</div>
          </div>
        </div>
"""

        html_parts.append(f"""
    <div class="card card-{tier_class}" 
         id="{q['id']}" 
         data-marks="{marks_num}" 
         data-tier="{q['tier']}" 
         data-rank="{q['rank']}" 
         data-unit="{unit_slug}" 
         data-mid="{mid_slug}" 
         data-important="{is_imp}">
      <div class="card-header" onclick="toggleCard('{q['id']}')">
        <div class="card-meta">
          {important_badge}
          <span class="badge badge-rank">Rank #{q['rank']}</span>
          <span class="badge badge-{tier_class}">Tier {q['tier']}: {q['tier_name']} ({q['time']})</span>
          <span class="badge badge-marks">{q['marks']}</span>
          <span class="badge badge-unit">{q['unit']}</span>
          <span class="badge badge-bloom">{q['bloom']}</span>
          <span class="badge badge-mid">{q['mid']} Q{q['qno']}</span>
        </div>
        <div class="card-title"><strong>{q['qno']}.</strong> {html.escape(q['title'])}</div>
        <div class="punchline-box">
          <strong>🧠 30-Sec Anchor:</strong> {html.escape(q['punchline'])}
        </div>
      </div>
      <div class="card-body" id="body-{q['id']}">
        <div class="notes-meta-bar" style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; align-items: center;">
          <span style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); padding: 3px 8px; border-radius: 6px; font-size: 0.76rem; font-weight: 700;">📝 {q['marks']} Exam Notes</span>
          <span style="background: rgba(148, 163, 184, 0.12); color: var(--text-muted); padding: 3px 8px; border-radius: 6px; font-size: 0.74rem;">⏱️ Est. Write Time: {q['time']}</span>
          {important_badge}
        </div>

        {eli5_html}

        <div class="keypoints-box">
          <div class="keypoints-header">🎯 High-Yield Key Points (Shortest Essentials):</div>
          <ul class="keypoints-list">
            {key_points_html}
          </ul>
        </div>

        <div class="diagram-box">
          <div class="diagram-header">
            <div class="diagram-title">
              <span>📊 Visual Exam Diagram &amp; Blueprint</span>
            </div>
            <span class="diagram-badge">Must Draw in Exam</span>
          </div>

          <div class="visual-diagram-wrap">
            {q.get('svg_diagram', '')}
          </div>

          <details class="sketch-blueprint-toggle">
            <summary>✍️ Click to view simplified pen-and-paper sketch (What to draw on paper)</summary>
            <pre class="ascii-pre">{html.escape(q['diagram'].strip())}</pre>
          </details>
        </div>

        <div class="content-section">
          {md_to_html_simple(q['content'])}
        </div>
      </div>
    </div>
""")

    html_parts.append("""
  </div>
</div>

<!-- Floating YouTube Lo-Fi Lounge -->
<div class="yt-mini-player" id="ytMiniPlayer">
  <div class="yt-mini-header">
    <span id="ytCurrentTitle">📺 Lofi Girl • 24/7 Live Stream</span>
    <button class="yt-mini-close" id="ytMiniCloseBtn" title="Close Lounge">✕</button>
  </div>
  <div class="yt-stream-chips" id="ytStreamChips">
    <button class="yt-chip active" data-vid="5qap5aO4i9A" data-title="Lofi Girl — 24/7 Study Beats">🎧 Lofi Girl</button>
    <button class="yt-chip" data-vid="zzpFiazS-Bk" data-title="Coffee Shop Radio — 24/7 Jazzy Lo-Fi">☕ Coffee Shop</button>
    <button class="yt-chip" data-vid="1fueZCTYkpA" data-title="Nintendo Lofi Beats — Zelda &amp; Mario">🍄 Nintendo</button>
    <button class="yt-chip" data-vid="x_7sXb_x228" data-title="Animal Crossing Lofi — 24/7 Study">🍃 Animal Crossing</button>
    <button class="yt-chip" data-vid="jfKfPfyJRdk" data-title="Chillhop Radio — Jazzy &amp; Lofi Hip Hop">🦝 Chillhop</button>
    <button class="yt-chip" data-vid="4xDzrJKXOOY" data-title="Synthwave Boy — Beats to Chill/Game">🌆 Synthwave</button>
    <button class="yt-chip" data-vid="lTRiuFIWV54" data-title="Cozy Rainy Cafe — Deep Ambient Focus">🌧️ Rainy Cafe</button>
  </div>
  <div class="yt-iframe-wrap">
    <iframe id="ytIframe" src="" title="YouTube Lofi Player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

<button id="backToTopBtn" class="fab-top" title="Back to Top" aria-label="Back to Top">↑</button>

<!-- SCRIPTS: Clean separation matching Deep Learning StudyMode -->
<script src="audio.js"></script>
<script src="app.js"></script>
</body>
</html>
""")

    full_html = "".join(html_parts)
    out_html = os.path.join(r'svp_study_suite', 'speech_video_processing_handbook.html')
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Saved {out_html} successfully ({len(full_html)} bytes).")

    out_index = os.path.join(r'svp_study_suite', 'index.html')
    with open(out_index, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Saved {out_index} successfully (for GitHub Pages / Web Serving).")

if __name__ == "__main__":
    generate_markdown_guide()
    generate_html_handbook()
    print("ALL SVP OUTPUTS GENERATED SUCCESSFULLY!")
