# -*- coding: utf-8 -*-
"""
Compiles complete SVP study guide:
1. Speech_and_Video_Processing_Complete_Study_Guide.md
2. speech_video_processing_handbook.html & index.html
"""

import os, re, html, shutil
from tier_data import QUESTION_TIER_DATA
from eli5_data import ELI5_DATA
from keypoints_data import KEYPOINTS_DATA
from diagrams_data import DIAGRAMS_SVG as SVG_DIAGRAMS

from data_unit1 import UNIT1_QUESTIONS
from data_unit2 import UNIT2_QUESTIONS
from data_unit3 import UNIT3_QUESTIONS
from data_unit4 import UNIT4_QUESTIONS
from data_unit5 import UNIT5_QUESTIONS

ALL_QUESTIONS = UNIT1_QUESTIONS + UNIT2_QUESTIONS + UNIT3_QUESTIONS + UNIT4_QUESTIONS + UNIT5_QUESTIONS

# Enrich each question with metadata
for q in ALL_QUESTIONS:
    qid = q['id']
    t_data = QUESTION_TIER_DATA.get(qid, {
        'rank': 99, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Medium', 'time': '5 min', 'prio': 'Normal', 'reason': ''
    })
    q['rank'] = t_data['rank']
    q['tier'] = t_data['tier']
    q['tier_name'] = t_data['tier_name']
    q['diff'] = t_data['diff']
    q['time'] = t_data['time']
    q['prio'] = t_data['prio']
    q['reason'] = t_data['reason']
    q['important'] = (t_data['tier'] == 1)
    q['eli5'] = ELI5_DATA.get(qid, {})
    q['key_points'] = KEYPOINTS_DATA.get(qid, [])
    q['svg_diagram'] = SVG_DIAGRAMS.get(qid, '')

def inline_md(txt):
    if not txt:
        return ""
    # Bold
    txt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', txt)
    # Italic
    txt = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', txt)
    # Code
    txt = re.sub(r'`(.*?)`', r'<code>\1</code>', txt)
    # Fix double-escaped arrows
    txt = txt.replace(r'(\\to)', r'($\rightarrow$)').replace(r'\\to', r'\rightarrow')
    return txt

def md_to_html_simple(md_text):
    """Converts markdown formatting into HTML with support for tables, headings, lists."""
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

        if trimmed.startswith('#### '):
            out.append(f'<h5 class="sub-sub-heading">{inline_md(trimmed[5:])}</h5>')
        elif trimmed.startswith('### '):
            out.append(f'<h4 class="sub-heading">{inline_md(trimmed[4:])}</h4>')
        elif trimmed.startswith('## '):
            out.append(f'<h3 class="section-heading">{inline_md(trimmed[3:])}</h3>')
        elif trimmed.startswith('# '):
            out.append(f'<h2 class="main-heading">{inline_md(trimmed[2:])}</h2>')
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
    print("Generating Speech_and_Video_Processing_Complete_Study_Guide.md ...")
    md_parts = [
        "# SPEECH AND VIDEO PROCESSING (SVP) — COMPLETE MASTER STUDY GUIDE",
        "**Year/Sem:** B.Tech IV Year I Sem | **Branch:** AI & ML | **Regulation:** KGR23 | **Course Code:** KG23ACM408",
        "**Course Coordinator:** Dr. Sandeep Kumar M | **Affiliation:** KG Reddy College of Engineering & Technology",
        "\n---\n",
        "## COURSE STRUCTURE & GRADING BREAKDOWN",
        "> Scaled strictly by marks (**05 Marks vs 10 Marks**). Contains 100% of questions across **Mid-I and Mid-II (40 Questions Total)**.",
        "> Includes full mathematical derivations, ASCII block blueprints, ELI5 summaries, high-yield bullet points, and 40 technical vector diagrams.",
        "\n---\n"
    ]

    current_unit = ""
    for q in sorted(ALL_QUESTIONS, key=lambda x: (x['mid'], x['qno'])):
        if q["unit"] != current_unit:
            current_unit = q["unit"]
            md_parts.append(f"\n# {current_unit.upper()} ({q['co']})\n")

        imp_tag = "🔥 [FREE MARKS / NUMERICAL]" if q['tier'] == 1 else ""
        md_parts.append(f"## {q['id']}: {q['title']} {imp_tag}")
        md_parts.append(f"**Mid:** {q['mid']} | **QNo:** {q['qno']} | **Unit:** {q['unit']} | **CO:** {q['co']} | **Bloom's:** {q['bloom']} | **Marks:** {q['marks']}")
        md_parts.append(f"**Cramming Priority:** Tier {q['tier']} ({q['tier_name']}) | **Global Rank:** #{q['rank']} of 40 | **Prep Time:** {q['time']}")
        md_parts.append(f"\n> 🧠 **30-Second Exam Anchor:** {q['punchline']}\n")

        eli5 = q.get('eli5', {})
        if eli5:
            md_parts.append(f"> 🐣 **In Plain English:** {eli5.get('plain', '')}")
            md_parts.append(f"> 🔑 **Magic Exam Keywords:** `{eli5.get('keywords', '')}`")
            md_parts.append(f"> 📝 **What to Draw / Write:** {eli5.get('draw', '')}\n")

        kps = q.get('key_points', [])
        if kps:
            md_parts.append("### 🎯 High-Yield Key Points (Shortest Essentials):")
            for kp in kps:
                md_parts.append(f"- {kp}")
            md_parts.append("")

        md_parts.append(f"### ✏️ Pen-and-Paper Exam Diagram Blueprint:\n```text\n{q['diagram']}\n```\n")
        md_parts.append("### 📝 Full Student Exam Notes & Derivations:")
        md_parts.append(q['content'])
        md_parts.append("\n---\n")

    out_path = os.path.join(os.path.dirname(__file__), "Speech_and_Video_Processing_Complete_Study_Guide.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_parts))
    print(f"Generated Markdown Guide: {len(md_parts)} parts written to {out_path}")

def generate_html_handbook():
    print("Generating speech_video_processing_handbook.html & index.html ...")

    tier_counts = {1: 0, 2: 0, 3: 0, 4: 0}
    for q in ALL_QUESTIONS:
        tier_counts[q['tier']] = tier_counts.get(q['tier'], 0) + 1

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<meta name="theme-color" content="#090d16">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>Speech &amp; Video Processing • Master Handbook (KGR23 Regulation)</title>
<link rel="stylesheet" href="style.css">
<!-- KaTeX Native LaTeX Rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}], throwOnError: false}});"></script>
</head>
<body class="theme-dark">

<header class="sticky-header">
  <div class="header-top">
    <div class="header-title">
      <h1>🎙️ Speech &amp; Video Processing Master Handbook</h1>
      <p>KGR23 • IV B.Tech I Sem • AI &amp; ML • 40 Questions Ranked by Priority &amp; Difficulty</p>
    </div>
    <div class="header-controls-wrap">
      <!-- Live Lo-Fi & Ambient Audio Lounge -->
      <div class="audio-widget" id="studyAudioWidget">
        <button class="audio-play-btn" id="audioPlayBtn" title="Play/Pause Lo-Fi Focus Music (M)">▶</button>
        <div class="audio-eq-bars" id="audioEqBars" title="Lo-Fi Soundscape Active">
          <div class="audio-eq-bar"></div>
          <div class="audio-eq-bar"></div>
          <div class="audio-eq-bar"></div>
        </div>
        <select class="audio-mode-select" id="audioModeSelect" title="Audio Soundscape / Live Radio">
          <optgroup label="☕ 24/7 LIVE LO-FI &amp; CHILLHOP">
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
          <optgroup label="🌧️ AMBIENT FOCUS SOUNDSCAPES">
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
        <a href="speedrun_trainer.html" class="btn-icon" style="background:#0284c7; color:#fff; text-decoration:none; display:inline-flex; align-items:center; font-weight:700;" title="Launch Speedrun Flashcard Trainer">⚡ Speedrun Drill</a>
        <button class="btn-icon" id="themeToggle" title="Toggle Theme">🌓</button>
        <button class="btn-icon" id="expandToggle" title="Expand / Collapse All Cards">📖 Expand All</button>
        <button class="btn-icon" id="modeToggle" title="Quick Flashcard Mode">⚡ Punchlines</button>
        <button class="btn-icon" onclick="window.print()" title="Print / PDF">🖨️ PDF</button>
      </div>
    </div>
  </div>
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="searchInput" class="search-input" placeholder="Search formulas, algorithms, topics (e.g. MFCC, LPC, Kalman)..." autocomplete="off">
  </div>
</header>

<div class="filter-bar" id="filterBar">
  <button class="filter-chip active" data-filter="all">All (40)</button>
  <button class="filter-chip chip-unit" data-filter="u1">📚 Unit 1 (8)</button>
  <button class="filter-chip chip-unit" data-filter="u2">📚 Unit 2 (8)</button>
  <button class="filter-chip chip-unit" data-filter="u3">📚 Unit 3 (8)</button>
  <button class="filter-chip chip-unit" data-filter="u4">📚 Unit 4 (8)</button>
  <button class="filter-chip chip-unit" data-filter="u5">📚 Unit 5 (8)</button>
  <button class="filter-chip" data-filter="mid1">Mid-I (20)</button>
  <button class="filter-chip" data-filter="mid2">Mid-II (20)</button>
  <button class="filter-chip chip-important" data-filter="important">🔥 Free Marks &amp; Numericals (10)</button>
  <button class="filter-chip chip-keypoints" data-filter="keypoints">🎯 Key Points Only (Shortest)</button>
  <button class="filter-chip" data-filter="5m">⚡ 5 Marks (20)</button>
  <button class="filter-chip" data-filter="10m">⚔️ 10 Marks (20)</button>
  <button class="filter-chip" data-filter="tier1">⚡ Tier 1: Free Marks ({tier_counts[1]})</button>
  <button class="filter-chip" data-filter="tier2">⚔️ Tier 2: Core Scoring ({tier_counts[2]})</button>
  <button class="filter-chip" data-filter="tier3">🛡️ Tier 3: High-Value 10M ({tier_counts[3]})</button>
  <button class="filter-chip" data-filter="tier4">🧩 Tier 4: Deep Dive ({tier_counts[4]})</button>
</div>

<div class="container">
  <!-- Unit-Wise Preparation Hub -->
  <div class="unit-hub-container" id="unitHubContainer" style="margin-bottom: 18px;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; flex-wrap:wrap; gap:8px;">
      <div style="font-size:0.95rem; font-weight:800; color:#38bdf8; display:flex; align-items:center; gap:6px;">
        <span>📚</span> <span>Syllabus Unit-Wise Preparation (8 Questions Each):</span>
      </div>
      <div style="font-size:0.78rem; color:#94a3b8;">Click any unit to isolate its 8 questions in syllabus order (Q1 → Q8)</div>
    </div>
    <div class="unit-pills-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap:10px;">
      <div class="unit-hub-card" onclick="filterByTier('u1')" style="cursor:pointer; background:#1e293b; border:1px solid #334155; border-left:4px solid #38bdf8; border-radius:8px; padding:10px 12px; transition:all 0.15s;">
        <div style="font-weight:700; font-size:0.86rem; color:#f8fafc; display:flex; justify-content:space-between;">
          <span>Unit 1</span> <span style="color:#38bdf8; font-size:0.75rem; font-weight:bold;">8 Qs</span>
        </div>
        <div style="font-size:0.74rem; color:#94a3b8; margin-top:3px;">Speech Production &amp; Acoustics</div>
        <div style="font-size:0.68rem; color:#64748b; margin-top:2px;">Mid-I Q1 – Q8</div>
      </div>
      <div class="unit-hub-card" onclick="filterByTier('u2')" style="cursor:pointer; background:#1e293b; border:1px solid #334155; border-left:4px solid #34d399; border-radius:8px; padding:10px 12px; transition:all 0.15s;">
        <div style="font-weight:700; font-size:0.86rem; color:#f8fafc; display:flex; justify-content:space-between;">
          <span>Unit 2</span> <span style="color:#34d399; font-size:0.75rem; font-weight:bold;">8 Qs</span>
        </div>
        <div style="font-size:0.74rem; color:#94a3b8; margin-top:3px;">Feature Extraction &amp; MFCC/LPC</div>
        <div style="font-size:0.68rem; color:#64748b; margin-top:2px;">Mid-I Q9 – Q16</div>
      </div>
      <div class="unit-hub-card" onclick="filterByTier('u3')" style="cursor:pointer; background:#1e293b; border:1px solid #334155; border-left:4px solid #fbbf24; border-radius:8px; padding:10px 12px; transition:all 0.15s;">
        <div style="font-weight:700; font-size:0.86rem; color:#f8fafc; display:flex; justify-content:space-between;">
          <span>Unit 3</span> <span style="color:#fbbf24; font-size:0.75rem; font-weight:bold;">8 Qs</span>
        </div>
        <div style="font-size:0.74rem; color:#94a3b8; margin-top:3px;">2D Signals, DFT &amp; 2D-DCT</div>
        <div style="font-size:0.68rem; color:#64748b; margin-top:2px;">Mid-I Q17-20 &amp; Mid-II Q1-4</div>
      </div>
      <div class="unit-hub-card" onclick="filterByTier('u4')" style="cursor:pointer; background:#1e293b; border:1px solid #334155; border-left:4px solid #f43f5e; border-radius:8px; padding:10px 12px; transition:all 0.15s;">
        <div style="font-weight:700; font-size:0.86rem; color:#f8fafc; display:flex; justify-content:space-between;">
          <span>Unit 4</span> <span style="color:#f43f5e; font-size:0.75rem; font-weight:bold;">8 Qs</span>
        </div>
        <div style="font-size:0.74rem; color:#94a3b8; margin-top:3px;">Video Motion &amp; Optical Flow</div>
        <div style="font-size:0.68rem; color:#64748b; margin-top:2px;">Mid-II Q5 – Q12</div>
      </div>
      <div class="unit-hub-card" onclick="filterByTier('u5')" style="cursor:pointer; background:#1e293b; border:1px solid #334155; border-left:4px solid #c084fc; border-radius:8px; padding:10px 12px; transition:all 0.15s;">
        <div style="font-weight:700; font-size:0.86rem; color:#f8fafc; display:flex; justify-content:space-between;">
          <span>Unit 5</span> <span style="color:#c084fc; font-size:0.75rem; font-weight:bold;">8 Qs</span>
        </div>
        <div style="font-size:0.74rem; color:#94a3b8; margin-top:3px;">Segmentation &amp; Video Tracking</div>
        <div style="font-size:0.68rem; color:#64748b; margin-top:2px;">Mid-II Q13 – Q20</div>
      </div>
    </div>
  </div>

  <!-- Emergency Triage Banner -->
  <div class="triage-banner">
    <div class="triage-header">
      <div class="triage-title">🚀 Fast Cramming Triage: Score-Ranked Priority Pathway</div>
    </div>
    <div class="triage-desc">
      When short on time, do <strong>NOT</strong> study in syllabus order (Unit 1 to 5). Study in order of <strong>Rank 1 to 40</strong> below.
      Click <strong>"⚡ Tier 1: Free Marks"</strong> for direct scoring numericals, <strong>"🎯 Key Points Only"</strong> for 60-second essentials, or filter by <strong>"⚡ 5 Marks"</strong> / <strong>"⚔️ 10 Marks"</strong>!
    </div>
    <div class="tier-pills-grid">
      <div class="tier-summary-card" style="border-left: 4px solid #ef4444; background: rgba(239, 68, 68, 0.08);" onclick="filterByTier('important')">
        <div class="tier-summary-title">
          <span style="color:#fca5a5;">🔥 Free Marks &amp; Numericals</span>
          <span style="color:#fde047;">Passing Gun</span>
        </div>
        <div class="tier-summary-desc">Top 10 scoring numericals &amp; core definitions. Guarantees pass!</div>
      </div>
      <div class="tier-summary-card t1" onclick="filterByTier('tier1')">
        <div class="tier-summary-title">
          <span style="color:#6ee7b7;">⚡ Tier 1: Free Marks</span>
          <span style="color:#a7f3d0;">10 Qs • ~25m</span>
        </div>
        <div class="tier-summary-desc">Pure numericals (BME, SAD, Framing, Kalman, Pole-Zero) &amp; definitions.</div>
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
      <span>Sort Order:</span>
      <select id="sortSelect" class="sort-select">
        <option value="unit" selected>📚 Unit Order (Syllabus 1 to 5)</option>
        <option value="priority">🚀 Priority &amp; Difficulty (Cramming Order)</option>
        <option value="marks">⭐ Marks (10M First)</option>
        <option value="fastest">⚡ Fastest to Learn (2m -> 6m)</option>
      </select>
    </div>
    <button class="toggle-all-btn" id="toggleAllBtn">Expand All</button>
  </div>

  <!-- Questions Container -->
  <div id="questionsContainer">
"""]

    # Render questions sorted by unit then question number in syllabus order
    def sort_key(item):
        u_str = str(item.get('unit', '')).lower().replace('unit-', '').replace('unit', '').strip()
        u_num = int(u_str) if u_str.isdigit() else 9
        mid_num = 1 if item.get('mid') == 'Mid-I' else 2
        return (u_num, mid_num, item.get('qno', 0))

    sorted_q = sorted(ALL_QUESTIONS, key=sort_key)
    for q in sorted_q:
        mid_class = "mid1" if q["mid"] == "Mid-I" else "mid2"
        unit_num = str(q['unit']).lower().replace('unit-', '').replace('unit', '').strip()
        unit_class = f"u{unit_num}"
        marks_class = "5m" if ("05" in q["marks"] or "5" in q["marks"]) else "10m"
        tier_class = f"tier{q['tier']}"
        time_clean = str(q['time']).replace(' min', '').replace('m', '').strip()
        is_important = "yes" if q['tier'] == 1 else "no"

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
    <div class="question-card"
         id="{q['id']}"
         data-mid="{mid_class}"
         data-unit="{unit_class}"
         data-marks="{marks_class}"
         data-tier="{tier_class}"
         data-rank="{q['rank']}"
         data-qno="{q['qno']}"
         data-time="{time_clean}"
         data-orig="{q['mid']}-{q['qno']:02d}"
         data-important="{is_important}">
      <div class="card-header" onclick="toggleCard('{q['id']}')">
        <div class="badge-row">
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
              <span>📐 Visual Architecture Diagram (Vector SVG)</span>
            </div>
            <span class="diagram-badge">Must Draw in Exam</span>
          </div>

          <div class="visual-diagram-wrap">
            {q.get('svg_diagram', '')}
          </div>

          <details class="sketch-blueprint-toggle">
            <summary>✏️ Click to view simplified pen-and-paper sketch (What to draw on paper)</summary>
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
<script src="audio.js?v=20261127_02"></script>
<script src="app.js?v=20261127_02"></script>
</body>
</html>
""")

    out_file = os.path.join(os.path.dirname(__file__), "speech_video_processing_handbook.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("".join(html_parts))
    print(f"Generated Handbook: {out_file} ({os.path.getsize(out_file):,} bytes)")

    # Copy to index.html for direct GitHub Pages access
    idx_file = os.path.join(os.path.dirname(__file__), "index.html")
    shutil.copyfile(out_file, idx_file)
    print(f"Copied to index.html ({os.path.getsize(idx_file):,} bytes)")

if __name__ == "__main__":
    generate_markdown_guide()
    generate_html_handbook()
