# -*- coding: utf-8 -*-
"""
Generates speedrun_trainer.html with Priority Tiers and Student Exam Notes (5M & 10M).
"""

import os, json, re, html
from tier_data import QUESTION_TIER_DATA
from data_unit1 import UNIT1_QUESTIONS
from data_unit2 import UNIT2_QUESTIONS
from data_unit3 import UNIT3_QUESTIONS
from data_unit4 import UNIT4_QUESTIONS
from data_unit5 import UNIT5_QUESTIONS

ALL_QUESTIONS = UNIT1_QUESTIONS + UNIT2_QUESTIONS + UNIT3_QUESTIONS + UNIT4_QUESTIONS + UNIT5_QUESTIONS

# Enrich each question with tier metadata, then sort by global rank (1-40)
for q in ALL_QUESTIONS:
    qid = q['id']
    t_data = QUESTION_TIER_DATA.get(qid, {
        'rank': 99, 'tier': 3, 'tier_name': 'Standard',
        'diff': 'Moderate', 'time': '4 min', 'prio': 'Medium', 'reason': ''
    })
    q.update(t_data)
    q['important'] = (q.get('tier') == 1)

ALL_QUESTIONS.sort(key=lambda x: x['rank'])

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

    def inline_md(txt):
        txt = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', txt)
        txt = re.sub(r'\*(.+?)\*', r'<em>\1</em>', txt)
        txt = re.sub(r'`(.+?)`', r'<code>\1</code>', txt)
        txt = txt.replace(r'(\\to)', r'($\rightarrow$)').replace(r'\\to', r'\rightarrow')
        return txt

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
            i += 1
            continue

        if trimmed.startswith('#### '):
            out.append(f'<h5>{inline_md(trimmed[5:])}</h5>')
        elif trimmed.startswith('### '):
            out.append(f'<h4>{inline_md(trimmed[4:])}</h4>')
        elif trimmed.startswith('## '):
            out.append(f'<h3>{inline_md(trimmed[3:])}</h3>')
        elif trimmed.startswith('# '):
            out.append(f'<h2>{inline_md(trimmed[2:])}</h2>')
        elif trimmed.startswith('---'):
            out.append('<hr class="divider"/>')
        elif trimmed.startswith('* ') or trimmed.startswith('- '):
            list_items = []
            while i < len(lines) and (lines[i].strip().startswith('* ') or lines[i].strip().startswith('- ')):
                list_items.append(f'<li>{inline_md(lines[i].strip()[2:])}</li>')
                i += 1
            out.append('<ul>' + ''.join(list_items) + '</ul>')
            continue
        elif re.match(r'^\d+\.\s', trimmed):
            list_items = []
            while i < len(lines) and re.match(r'^\d+\.\s', lines[i].strip()):
                m = re.match(r'^\d+\.\s(.*)', lines[i].strip())
                list_items.append(f'<li>{inline_md(m.group(1))}</li>')
                i += 1
            out.append('<ol>' + ''.join(list_items) + '</ol>')
            continue
        else:
            out.append(f'<p>{inline_md(trimmed)}</p>')

        i += 1

    if in_table:
        out.append(process_table(table_lines))

    return '\n'.join(out)

# Precompute HTML content for each question
processed_questions = []
for q in ALL_QUESTIONS:
    processed_q = dict(q)
    processed_q['html_content'] = md_to_html_simple(q['content'])
    processed_questions.append(processed_q)

questions_json = json.dumps(processed_questions)

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">
<meta name="theme-color" content="#090d16">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>SVP Speedrun Drill • Simple Human Notes (5M & 10M Ranked)</title>
<!-- KaTeX Native Math Rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="if(window.renderMath){{window.renderMath();}}"></script>
<style>
:root {{
  --sat: env(safe-area-inset-top, 0px);
  --sab: env(safe-area-inset-bottom, 0px);
  --sal: env(safe-area-inset-left, 0px);
  --sar: env(safe-area-inset-right, 0px);
  --bg: #090d16;
  --surface: #111827;
  --card-bg: #1f2937;
  --card-border: #374151;
  --accent-cyan: #06b6d4;
  --accent-gold: #f59e0b;
  --accent-green: #10b981;
  --accent-rose: #f43f5e;
  --accent-purple: #8b5cf6;
  --text-main: #f9fafb;
  --text-muted: #9ca3af;
  --radius-lg: 16px;
  --radius-sm: 8px;
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}
html, body {{
  overflow-x: hidden;
  width: 100%;
  -webkit-text-size-adjust: 100%;
}}
body {{
  background: var(--bg);
  color: var(--text-main);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding-bottom: calc(16px + var(--sab));
}}
button, select, input {{
  font-family: inherit;
  touch-action: manipulation;
}}

/* Header HUD */
header {{
  background: rgba(17, 24, 39, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid #1f2937;
  padding: calc(10px + var(--sat)) calc(16px + var(--sar)) 10px calc(16px + var(--sal));
  position: sticky;
  top: 0;
  z-index: 50;
}}

.hud-container {{
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}}

.brand-section {{
  display: flex;
  align-items: center;
  gap: 10px;
}}

.brand-title {{
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #38bdf8, #818cf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.stats-bar {{
  display: flex;
  gap: 14px;
  align-items: center;
}}

.stat-pill {{
  background: rgba(31, 41, 55, 0.8);
  border: 1px solid #374151;
  padding: 5px 12px;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 400;
  display: flex;
  align-items: center;
  gap: 6px;
}}

.stat-pill.streak {{
  border-color: #f59e0b;
  color: #fbbf24;
}}

.stat-pill.xp {{
  border-color: #10b981;
  color: #34d399;
}}

.controls-top {{
  display: flex;
  gap: 8px;
}}

.btn-icon {{
  background: #1f2937;
  border: 1px solid #374151;
  color: var(--text-main);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 0.82rem;
  font-weight: 400;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}}

.btn-icon:hover {{
  background: #374151;
  border-color: #4b5563;
}}

.btn-icon.active-mode {{
  background: #f59e0b !important;
  color: #0f172a !important;
  border-color: #d97706 !important;
  font-weight: 800;
}}

/* Lo-Fi & Ambient Audio Player Widget */
.audio-widget {{
  display: flex;
  align-items: center;
  background: rgba(31, 41, 55, 0.85);
  border: 1px solid #374151;
  border-radius: 10px;
  padding: 4px 8px;
  gap: 6px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  flex-shrink: 0;
}}
.audio-play-btn {{
  background: linear-gradient(135deg, #0284c7, #38bdf8);
  color: #fff;
  border: none;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
  transition: transform 0.15s, background 0.2s, box-shadow 0.2s;
  flex-shrink: 0;
  box-shadow: 0 2px 5px rgba(56, 189, 248, 0.3);
}}
.audio-play-btn:hover {{
  transform: scale(1.08);
}}
.audio-play-btn.playing {{
  background: linear-gradient(135deg, #059669, #10b981);
  animation: audio-pulse 2s infinite;
}}
@keyframes audio-pulse {{
  0% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.6); }}
  70% {{ box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }}
  100% {{ box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }}
}}
.audio-mode-select {{
  background: transparent;
  color: var(--text-main);
  border: none;
  font-size: 0.76rem;
  font-weight: 400;
  cursor: pointer;
  outline: none;
  max-width: 155px;
  text-overflow: ellipsis;
  white-space: nowrap;
}}
.audio-mode-select option, .audio-mode-select optgroup {{
  background: #0f172a;
  color: #f1f5f9;
}}
.audio-vol-slider {{
  width: 45px;
  accent-color: #38bdf8;
  cursor: pointer;
  height: 4px;
}}
.audio-layer-btn {{
  background: #1f2937;
  border: 1px solid #374151;
  color: var(--text-muted);
  height: 26px;
  width: 26px;
  padding: 0;
  border-radius: 6px;
  font-size: 0.72rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
  flex-shrink: 0;
}}
.audio-layer-btn:hover {{
  background: #374151;
  color: var(--text-main);
}}
.audio-layer-btn.active {{
  background: rgba(56, 189, 248, 0.18);
  border-color: #38bdf8;
  color: #38bdf8;
}}

/* Filter Bar */
.filter-strip {{
  background: #0f172a;
  border-bottom: 1px solid #1e293b;
  padding: 8px 16px;
  overflow-x: auto;
  white-space: nowrap;
}}

.filter-strip-inner {{
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  gap: 8px;
  align-items: center;
}}

.filter-btn {{
  background: transparent;
  border: 1px solid #334155;
  color: var(--text-muted);
  padding: 5px 13px;
  border-radius: 20px;
  font-size: 0.78rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s;
}}

.filter-btn:hover {{
  border-color: #64748b;
  color: #fff;
}}

.filter-btn.active {{
  background: #2563eb;
  border-color: #3b82f6;
  color: #ffffff;
}}

.filter-btn[data-filter="tier1"] {{ border-color: #059669; color: #6ee7b7; }}
.filter-btn[data-filter="tier1"].active {{ background: #059669; color: #fff; }}

.filter-btn[data-filter="tier2"] {{ border-color: #2563eb; color: #93c5fd; }}
.filter-btn[data-filter="tier2"].active {{ background: #2563eb; color: #fff; }}

.filter-btn[data-filter="tier3"] {{ border-color: #7c3aed; color: #c4b5fd; }}
.filter-btn[data-filter="tier3"].active {{ background: #7c3aed; color: #fff; }}

.filter-btn[data-filter^="u"] {{ border-color: #0284c7; color: #7dd3fc; }}
.filter-btn[data-filter^="u"].active {{ background: #0284c7; color: #fff; }}

/* Main Arena */
main {{
  flex: 1;
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
  padding: 16px 16px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}}

/* Timer Bar */
.timer-container {{
  width: 100%;
  background: #1f2937;
  height: 8px;
  border-radius: 4px;
  overflow: hidden;
  position: relative;
}}

.timer-fill {{
  height: 100%;
  width: 100%;
  background: #10b981;
  transition: width 1s linear, background-color 0.5s ease;
}}

.timer-fill.warn {{ background: #f59e0b; }}
.timer-fill.danger {{
  background: #f43f5e;
  animation: pulse-danger 0.6s infinite alternate;
}}

@keyframes pulse-danger {{
  from {{ opacity: 1; }}
  to {{ opacity: 0.4; }}
}}

/* Card Container */
.drill-card {{
  background: var(--surface);
  border: 1px solid var(--card-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  position: relative;
}}

.card-top {{
  padding: 14px 18px;
  background: rgba(31, 41, 55, 0.4);
  border-bottom: 1px solid #1f2937;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}}

.card-badges {{
  display: flex;
  gap: 6px;
  align-items: center;
  flex-wrap: wrap;
}}

.badge {{
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  letter-spacing: 0.4px;
}}

.badge-rank {{ background: #0f172a; color: #38bdf8; border: 1px solid #0284c7; }}
.badge-tier1 {{ background: rgba(16, 185, 129, 0.15); color: #6ee7b7; border: 1px solid rgba(16, 185, 129, 0.4); }}
.badge-tier2 {{ background: rgba(59, 130, 246, 0.15); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.4); }}
.badge-tier3 {{ background: rgba(139, 92, 246, 0.15); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4); }}
.badge-tier4 {{ background: rgba(244, 63, 94, 0.15); color: #fda4af; border: 1px solid rgba(244, 63, 94, 0.4); }}
.badge-unit {{ background: #1e3a8a; color: #93c5fd; }}
.badge-marks {{ background: #064e3b; color: #6ee7b7; }}
.badge-bloom {{ background: #581c87; color: #d8b4fe; }}

.badge-important {{
  background: linear-gradient(135deg, #ef4444, #f59e0b) !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  border: 1px solid #fca5a5 !important;
  box-shadow: 0 0 8px rgba(239, 68, 68, 0.4);
}}

.filter-btn.filter-btn-important {{
  border-color: #f59e0b;
  color: #fbbf24;
  font-weight: 800;
}}
.filter-btn.filter-btn-important.active {{
  background: linear-gradient(135deg, #ef4444, #f59e0b) !important;
  color: #ffffff !important;
  border-color: #f59e0b !important;
}}

.card-index {{
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--text-muted);
}}

.card-question-box {{
  padding: 20px 20px 16px 20px;
}}

.question-title {{
  font-size: 1.25rem;
  font-weight: 700;
  line-height: 1.4;
  color: #f3f4f6;
  margin-bottom: 12px;
}}

.prompt-tip {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: var(--accent-cyan);
  background: rgba(6, 182, 212, 0.08);
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  border: 1px dashed rgba(6, 182, 212, 0.3);
}}

/* Unrevealed Cover */
.reveal-curtain {{
  padding: 36px 20px;
  text-align: center;
  background: linear-gradient(180deg, rgba(17, 24, 39, 0.4), rgba(31, 41, 55, 0.4));
  border-top: 1px dashed #374151;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: all 0.2s;
}}

.reveal-curtain:hover {{
  background: rgba(31, 41, 55, 0.7);
}}

.big-flip-btn {{
  background: linear-gradient(135deg, #2563eb, #4f46e5);
  color: white;
  border: none;
  font-size: 1.05rem;
  font-weight: 700;
  padding: 12px 26px;
  border-radius: 9999px;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
  transition: transform 0.1s;
  display: flex;
  align-items: center;
  gap: 10px;
}}

.big-flip-btn:hover {{
  transform: scale(1.03);
}}

.flip-kbd-hint {{
  font-size: 0.8rem;
  color: var(--text-muted);
}}

kbd {{
  background: #374151;
  border: 1px solid #4b5563;
  border-radius: 4px;
  padding: 2px 6px;
  font-family: inherit;
  font-size: 0.72rem;
  color: #e5e7eb;
}}

/* Revealed Secret Section */
.revealed-content {{
  display: none;
  border-top: 1px solid #1f2937;
  padding: 18px 20px;
  animation: fadeIn 0.2s ease-out;
}}

@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(6px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}

.hook-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-bottom: 18px;
}}

.hook-box {{
  border-radius: var(--radius-sm);
  padding: 10px 14px;
}}

.hook-punchline {{
  background: rgba(6, 182, 212, 0.1);
  border-left: 4px solid var(--accent-cyan);
}}

.hook-punchline h5 {{
  color: var(--accent-cyan);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 3px;
}}

.hook-punchline p {{
  font-size: 0.95rem;
  font-weight: 400;
  color: #e0f2fe;
}}

.hook-mnemonic {{
  background: rgba(245, 158, 11, 0.1);
  border-left: 4px solid var(--accent-gold);
}}

.hook-mnemonic h5 {{
  color: var(--accent-gold);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 3px;
}}

.hook-mnemonic p {{
  font-size: 0.92rem;
  font-weight: 700;
  color: #fef3c7;
}}

.hook-analogy {{
  background: rgba(139, 92, 246, 0.1);
  border-left: 4px solid var(--accent-purple);
}}

.hook-analogy h5 {{
  color: var(--accent-purple);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 3px;
}}

.hook-analogy p {{
  font-size: 0.88rem;
  color: #ede9fe;
}}

.diagram-toggle-btn {{
  width: 100%;
  background: #1f2937;
  border: 1px solid #374151;
  color: #93c5fd;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  font-weight: 400;
  font-size: 0.82rem;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}}

.diagram-block {{
  display: none;
  background: #090d16;
  border: 1px solid #1e293b;
  border-radius: var(--radius-sm);
  padding: 12px;
  margin-bottom: 14px;
  overflow-x: auto;
  max-width: 100%;
  -webkit-overflow-scrolling: touch;
}}

.diagram-block pre {{
  color: #38bdf8;
  font-family: ui-monospace, "SFMono-Regular", Consolas, monospace;
  font-size: 0.78rem;
  line-height: 1.35;
  white-space: pre;
}}

.katex-display {{
  overflow-x: auto !important;
  overflow-y: hidden !important;
  max-width: 100% !important;
  padding: 6px 0;
  -webkit-overflow-scrolling: touch;
}}

.answer-content {{
  font-size: 0.88rem;
  line-height: 1.55;
  color: #d1d5db;
  max-height: 380px;
  overflow-y: auto;
  padding-right: 8px;
}}

.answer-content h2, .answer-content h3, .answer-content h4 {{
  color: #f9fafb;
  margin-top: 12px;
  margin-bottom: 6px;
}}

.answer-content ul, .answer-content ol {{
  padding-left: 18px;
  margin-bottom: 8px;
}}

.answer-content li {{ margin-bottom: 3px; }}

.answer-content table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  margin: 10px 0;
}}

.answer-content th, .answer-content td {{
  border: 1px solid #374151;
  padding: 6px 8px;
}}

.answer-content th {{
  background: #1f2937;
  color: #93c5fd;
}}

/* Grading Bar */
.grading-bar {{
  display: none;
  grid-template-columns: 1fr 1fr 1.2fr;
  gap: 10px;
  margin-top: 16px;
}}

.btn-grade {{
  padding: 12px 10px;
  border-radius: var(--radius-sm);
  border: none;
  font-size: 0.9rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  transition: all 0.15s;
}}

.btn-grade span.key-hint {{
  font-size: 0.72rem;
  font-weight: normal;
  opacity: 0.8;
}}

.btn-grade-miss {{
  background: rgba(244, 63, 94, 0.15);
  color: #fda4af;
  border: 1px solid rgba(244, 63, 94, 0.4);
}}

.btn-grade-miss:hover {{
  background: rgba(244, 63, 94, 0.3);
}}

.btn-grade-mid {{
  background: rgba(245, 158, 11, 0.15);
  color: #fcd34d;
  border: 1px solid rgba(245, 158, 11, 0.4);
}}

.btn-grade-mid:hover {{
  background: rgba(245, 158, 11, 0.3);
}}

.btn-grade-perfect {{
  background: rgba(16, 185, 129, 0.2);
  color: #6ee7b7;
  border: 1px solid rgba(16, 185, 129, 0.5);
}}

.btn-grade-perfect:hover {{
  background: rgba(16, 185, 129, 0.35);
}}

/* Victory Screen */
.victory-screen {{
  display: none;
  text-align: center;
  padding: 50px 20px;
  background: var(--surface);
  border: 1px solid var(--accent-green);
  border-radius: var(--radius-lg);
  flex-direction: column;
  align-items: center;
  gap: 18px;
}}

.victory-title {{
  font-size: 1.8rem;
  font-weight: 800;
  color: #34d399;
}}

/* Cheat Sheet Modal */
html.modal-open, body.modal-open {{
  overflow: hidden !important;
  height: 100vh !important;
}}

.modal-overlay {{
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 100;
  align-items: center;
  justify-content: center;
  padding: 16px;
}}

.modal-content {{
  background: #111827;
  border: 1px solid #374151;
  border-radius: var(--radius-lg);
  max-width: 950px;
  width: 100%;
  max-height: 85vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}}

.modal-header {{
  padding: 14px 18px;
  border-bottom: 1px solid #1f2937;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.modal-search {{
  padding: 10px 18px;
  border-bottom: 1px solid #1f2937;
}}

.modal-search input {{
  width: 100%;
  background: #1f2937;
  border: 1px solid #374151;
  color: white;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
}}

.modal-body {{
  padding: 14px 18px;
  overflow-y: auto;
}}

.cheat-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
}}

.cheat-table th, .cheat-table td {{
  border: 1px solid #1f2937;
  padding: 8px 10px;
  text-align: left;
}}

.cheat-table th {{
  background: #1e293b;
  position: sticky;
  top: 0;
}}

/* Card Navigation Bar */
.card-nav-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4px 6px;
}}

.btn-nav {{
  background: var(--surface);
  border: 1px solid var(--card-border);
  color: var(--text-muted);
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  font-size: 0.82rem;
  font-weight: 400;
  cursor: pointer;
  transition: all 0.15s;
  min-height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}}

.btn-nav:hover, .btn-nav:active {{
  color: #ffffff;
  background: #1f2937;
  border-color: #4b5563;
}}

.nav-hint-text {{
  font-size: 0.76rem;
  color: var(--text-muted);
  opacity: 0.8;
}}

/* Mobile Responsive Media Queries */
@media (max-width: 768px) {{
  html, body {{
    overflow-x: hidden !important;
    width: 100%;
    max-width: 100vw;
  }}
  header {{
    padding: calc(8px + var(--sat)) calc(12px + var(--sar)) 8px calc(12px + var(--sal));
  }}
  .hud-container {{
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
  }}
  .brand-section {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .brand-title {{
    font-size: 0.98rem;
  }}
  .audio-widget {{
    width: 100%;
    justify-content: space-between;
    padding: 6px 8px;
    box-sizing: border-box;
  }}
  .audio-mode-select {{
    flex: 1;
    min-width: 0;
    max-width: none;
    font-size: 0.74rem;
  }}
  .audio-vol-slider,
  .audio-layer-btn {{
    display: none !important;
  }}
  .controls-top {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
    width: 100%;
  }}
  .controls-top .btn-icon {{
    justify-content: center;
    padding: 6px 4px;
    font-size: 0.72rem;
    min-height: 36px;
  }}
  .stats-bar {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    width: 100%;
  }}
  .stat-pill {{
    justify-content: center;
    padding: 5px 6px;
    font-size: 0.75rem;
    gap: 4px;
  }}
  .filter-strip {{
    padding: 8px calc(10px + var(--sar)) 8px calc(10px + var(--sal));
  }}
  .filter-btn {{
    padding: 6px 12px;
    font-size: 0.75rem;
    min-height: 34px;
  }}
  main {{
    padding: 10px calc(10px + var(--sar)) 16px calc(10px + var(--sal));
    gap: 10px;
    max-width: 100vw;
    box-sizing: border-box;
    overflow-x: hidden;
  }}
  .drill-card {{
    border-radius: 12px;
    max-width: 100%;
    overflow: hidden;
  }}
  .card-top {{
    padding: 10px 12px;
  }}
  .card-question-box {{
    padding: 14px 14px 12px 14px;
  }}
  .question-title {{
    font-size: 1.05rem;
    line-height: 1.4;
    margin-bottom: 8px;
  }}
  .prompt-tip {{
    font-size: 0.78rem;
    padding: 8px 10px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
  }}
  .reveal-curtain {{
    padding: 24px 16px;
  }}
  .big-flip-btn {{
    width: 100%;
    justify-content: center;
    min-height: 50px;
    font-size: 0.98rem;
  }}
  .revealed-content {{
    padding: 14px 12px;
    max-width: 100%;
    box-sizing: border-box;
  }}
  .hook-grid {{
    gap: 8px;
    margin-bottom: 14px;
  }}
  .hook-box {{
    padding: 8px 12px;
  }}
  .hook-punchline p {{
    font-size: 0.88rem;
  }}
  .hook-mnemonic p {{
    font-size: 0.86rem;
  }}
  .hook-analogy p {{
    font-size: 0.84rem;
  }}
  .diagram-block {{
    max-width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    padding: 8px;
  }}
  .diagram-block pre, #diagramContent {{
    max-width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    font-size: 0.70rem;
    line-height: 1.25;
  }}
  .katex-display {{
    display: block !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    text-align: left !important;
    -webkit-overflow-scrolling: touch;
    padding: 6px 0 !important;
  }}
  .katex-display > .katex {{
    text-align: left !important;
    max-width: none !important;
  }}
  .answer-content {{
    max-height: none !important;
    overflow-y: visible !important;
    padding-right: 0 !important;
  }}
  .answer-content p, .answer-content li {{
    word-break: break-word;
    overflow-wrap: break-word;
  }}
  .answer-content table {{
    display: block !important;
    width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
  }}
  .grading-bar {{
    grid-template-columns: 1fr 1fr 1.15fr;
    gap: 6px;
    margin-top: 14px;
  }}
  .btn-grade {{
    min-height: 52px;
    padding: 8px 4px;
    font-size: 0.82rem;
  }}
  .btn-grade span.key-hint {{
    display: none !important;
  }}
  
  /* Mobile Full-Screen Cheat Sheet Modal */
  .modal-overlay {{
    padding: 0;
  }}
  .modal-content {{
    max-height: 100vh;
    height: 100vh;
    border-radius: 0;
    border: none;
  }}
  .modal-header {{
    padding: calc(12px + var(--sat)) 14px 12px 14px;
  }}
  .modal-header h3 {{
    font-size: 0.92rem;
  }}
  .modal-search {{
    padding: 8px 14px;
  }}
  .modal-search input {{
    font-size: 16px; /* Prevents iOS auto-zoom */
    padding: 10px 12px;
  }}
  .modal-body {{
    padding: 10px 12px calc(24px + var(--sab)) 12px;
  }}
  .cheat-table thead {{
    display: none;
  }}
  .cheat-table, .cheat-table tbody, .cheat-table tr, .cheat-table td {{
    display: block;
    width: 100%;
  }}
  .cheat-table tr {{
    background: #1f2937;
    border: 1px solid #374151;
    border-radius: 10px;
    margin-bottom: 10px;
    padding: 12px;
  }}
  .cheat-table td {{
    border: none;
    padding: 3px 0;
  }}
  .cheat-table td:nth-child(1) {{
    display: inline-block;
    width: auto;
    margin-right: 8px;
  }}
  .cheat-table td:nth-child(2) {{
    display: inline-block;
    width: auto;
  }}
  .cheat-table td:nth-child(3) {{
    margin-top: 4px;
    font-size: 0.88rem;
    color: #f3f4f6;
  }}
  .cheat-table td:nth-child(4) {{
    font-size: 0.82rem;
    color: #fef08a;
    margin-top: 4px;
  }}
  .cheat-table td:nth-child(5) {{
    font-size: 0.8rem;
    color: #fde047;
    margin-top: 2px;
  }}
}}

@media (max-width: 380px) {{
  .controls-top {{
    grid-template-columns: repeat(2, 1fr);
  }}
  .grading-bar {{
    grid-template-columns: 1fr;
    gap: 8px;
  }}
  .audio-vol-slider {{
    display: none;
  }}
}}
</style>
</head>
<body>

<header>
  <div class="hud-container">
    <div class="brand-section">
      <div class="brand-title">⚡ SVP SPEEDRUN (PRIORITY RANKED)</div>
    </div>
    
    <div class="stats-bar">
      <div class="stat-pill">
        <span>Cards:</span>
        <span id="hudProgress">1 / 40</span>
      </div>
      <div class="stat-pill streak">
        <span id="streakFire">🔥</span>
        <span id="hudStreak">0 Streak</span>
      </div>
      <div class="stat-pill xp">
        <span>XP:</span>
        <span id="hudXP">0</span>
      </div>
    </div>

    <!-- Live Lo-Fi & Ambient Audio Player -->
    <div class="audio-widget" id="studyAudioWidget">
      <button class="audio-play-btn" id="audioPlayBtn" title="Play/Pause Live Lo-Fi Focus Music (M)">▶</button>
      <select class="audio-mode-select" id="audioModeSelect" title="Audio Soundscape / Live Radio">
        <optgroup label="🎮 NINTENDO &amp; VIDEO GAME LO-FI">
          <option value="stream_vgm_all">🎮 Live: Video Game Lofi &amp; VGM</option>
          <option value="stream_vgm_covers">🍄 Live: Nintendo &amp; Game Remixes</option>
          <option value="stream_vgm_ocremix">⚔️ Live: OverClocked ReMix (VGM)</option>
          <option value="stream_vgm_chiptune">👾 Live: 8-Bit Chiptune Radio</option>
        </optgroup>
        <optgroup label="🌐 24/7 LIVE LO-FI STREAMS">
          <option value="stream_chillhop" selected>☕ 24/7 Chillhop &amp; Lofi</option>
          <option value="stream_anime">🌸 Anime &amp; Cozy Lofi</option>
          <option value="stream_cafe">☕ Cafe Lofi Beats</option>
          <option value="stream_berlin">🏙️ Berlin Lofi Radio</option>
          <option value="stream_nightwave">🌌 Nightwave Plaza (Vaporwave)</option>
          <option value="stream_chillout">🍃 Ambient Chillout Lounge</option>
        </optgroup>
        <optgroup label="🎹 OFFLINE GENERATIVE SOUNDSCAPES">
          <option value="lofi_synth">🎹 Generative Jazz Piano Beats</option>
          <option value="rain">🌧️ Rain on Window</option>
          <option value="binaural">🧠 40Hz Deep Focus</option>
          <option value="brown_noise">📻 Brown Noise</option>
        </optgroup>
      </select>
      <input type="range" class="audio-vol-slider" id="audioVolSlider" min="0" max="1" step="0.05" value="0.65" title="Volume">
      <button class="audio-layer-btn active" id="ambientVinylBtn" title="Vinyl Crackle (Toggle)">📻</button>
      <button class="audio-layer-btn" id="ambientRainBtn" title="Rain Layer (Toggle)">🌧️</button>
    </div>

    <div class="controls-top">
      <a href="index.html" class="btn-icon" style="text-decoration:none; color:#38bdf8; border:1px solid #0284c7; background:rgba(2,132,199,0.15);" title="Back to Master Handbook">📖 Handbook</a>
      <button class="btn-icon" id="btnSoundToggle" title="Audio Sound Effects">🔊 Sound</button>
      <button class="btn-icon" id="btnTimerToggle" title="Card Timer">⏱️ 45s</button>
      <button class="btn-icon" id="btnCheatSheet" title="Cheat Sheet">📋 Sheet</button>
    </div>
  </div>
</header>

<div class="filter-strip">
  <div class="filter-strip-inner">
    <button class="filter-btn active" data-filter="all">All 40 (Ranked)</button>
    <button class="filter-btn" data-filter="u1" style="border-color:#38bdf8; color:#7dd3fc; font-weight:700;">📚 Unit 1 (8)</button>
    <button class="filter-btn" data-filter="u2" style="border-color:#38bdf8; color:#7dd3fc; font-weight:700;">📚 Unit 2 (8)</button>
    <button class="filter-btn" data-filter="u3" style="border-color:#38bdf8; color:#7dd3fc; font-weight:700;">📚 Unit 3 (8)</button>
    <button class="filter-btn" data-filter="u4" style="border-color:#38bdf8; color:#7dd3fc; font-weight:700;">📚 Unit 4 (8)</button>
    <button class="filter-btn" data-filter="u5" style="border-color:#38bdf8; color:#7dd3fc; font-weight:700;">📚 Unit 5 (8)</button>
    <button class="filter-btn" data-filter="mid1">Mid-I (20)</button>
    <button class="filter-btn" data-filter="mid2">Mid-II (20)</button>
    <button class="filter-btn filter-btn-important" data-filter="important">🔥 Free Marks (10)</button>
    <button class="filter-btn" data-filter="5m">⚡ 5M Questions (20)</button>
    <button class="filter-btn" data-filter="10m">⚔️ 10M Questions (20)</button>
    <button class="filter-btn" data-filter="tier1">⚡ Tier 1: Free Marks (10)</button>
    <button class="filter-btn" data-filter="tier2">⚔️ Tier 2: Core Scoring (12)</button>
    <button class="filter-btn" data-filter="tier3">🛡️ Tier 3: High-Value 10M (12)</button>
    <button class="filter-btn" data-filter="tier4">🧩 Tier 4: Deep Dive (6)</button>
    <button class="filter-btn" data-filter="missed" id="btnFilterMissed" style="display:none; border-color:#f43f5e; color:#fda4af;">Weak Spots (0)</button>
  </div>
</div>

<main>
  <div class="timer-container" id="timerBar">
    <div class="timer-fill" id="timerFill"></div>
  </div>

  <div class="drill-card" id="drillCard">
    <div class="card-top">
      <div class="card-badges">
        <span class="badge badge-important" id="cardImportantBadge" style="display:none;">🔥 MOST IMPORTANT</span>
        <span class="badge badge-rank" id="cardRankBadge">Rank #1</span>
        <span class="badge badge-tier1" id="cardTierBadge">Tier 1: Free Marks (2 min)</span>
        <span class="badge badge-marks" id="cardMarksBadge">5 Marks</span>
        <span class="badge badge-unit" id="cardUnitBadge">Unit 1</span>
        <span class="badge badge-bloom" id="cardBloomBadge">K2</span>
      </div>
      <div class="card-index" id="cardIndexLabel">Card 1 of 40</div>
    </div>

    <div class="card-question-box">
      <h2 class="question-title" id="cardTitle">Loading Question...</h2>
      <div class="prompt-tip">
        <span>⚡ Cramming Anchor:</span>
        <span id="promptText">Predict the core points before flipping!</span>
      </div>
    </div>

    <div class="reveal-curtain" id="revealCurtain">
      <button class="big-flip-btn" id="btnFlip">
        <span>👀 REVEAL EXAM NOTES</span>
      </button>
      <div class="flip-kbd-hint">Press <kbd>Space</kbd> or Tap to Flip</div>
    </div>

    <div class="revealed-content" id="revealedContent">

      <div class="hook-grid">
        <div class="hook-box hook-punchline">
          <h5>🎯 1-Sentence Exam Punchline</h5>
          <p id="cardPunchline">Punchline text...</p>
        </div>
        <div class="hook-box hook-mnemonic">
          <h5>🧠 Memory Mnemonic Acronym</h5>
          <p id="cardMnemonic">Mnemonic text...</p>
        </div>
        <div class="hook-box hook-analogy">
          <h5>💡 Real-World Analogy</h5>
          <p id="cardAnalogy">Analogy text...</p>
        </div>
      </div>

      <button class="diagram-toggle-btn" id="btnToggleDiagram" style="display:none;">
        <span>📐 View ASCII Diagram Blueprint</span>
        <span id="diagramIcon">▼</span>
      </button>
      <div class="diagram-block" id="diagramBlock">
        <pre id="diagramContent"></pre>
      </div>

      <div class="answer-content" id="cardFullContent">
      </div>

      <div class="grading-bar" id="gradingBar">
        <button class="btn-grade btn-grade-miss" id="btnGradeMiss">
          <span>❌ Missed / Re-queue</span>
          <span class="key-hint">[Press 1 or ←]</span>
        </button>
        <button class="btn-grade btn-grade-mid" id="btnGradeMid">
          <span>⚡ Partial (+100 XP)</span>
          <span class="key-hint">[Press 2 or ↓]</span>
        </button>
        <button class="btn-grade btn-grade-perfect" id="btnGradePerfect">
          <span>🔥 Nailed It! (+200 XP)</span>
          <span class="key-hint">[Press 3 or →]</span>
        </button>
      </div>
    </div>
  </div>

  <div class="card-nav-bar">
    <button class="btn-nav" id="btnPrevCard">◀ Prev</button>
    <span class="nav-hint-text">👆 Tap or Swipe to Flip</span>
    <button class="btn-nav" id="btnNextCard">Skip ▶</button>
  </div>

  <div class="victory-screen" id="victoryScreen">
    <div style="font-size: 3rem;">🏆</div>
    <h2 class="victory-title">TIER COMPLETE!</h2>
    <p style="color: var(--text-muted); max-width: 500px;">
      You just crushed this tier! Review your weak spots or move to the next priority tier.
    </p>
    <div style="display: flex; gap: 12px; flex-wrap: wrap; justify-content: center;">
      <button class="big-flip-btn" id="btnRestartDeck">🔄 Run Tier Again</button>
      <button class="btn-icon" id="btnReviewMissedFromVictory" style="display:none;">⚡ Review Weak Spots (<span id="victoryMissedCount">0</span>)</button>
    </div>
  </div>
</main>

<div class="modal-overlay" id="modalCheatSheet">
  <div class="modal-content">
    <div class="modal-header">
      <h3 style="font-weight: 700; color: #38bdf8;">📋 Master 40-Question Cheat Sheet (Priority Ranked)</h3>
      <button class="btn-icon" id="btnCloseModal">✕ Close [Esc]</button>
    </div>
    <div class="modal-search">
      <input type="text" id="cheatSearchInput" placeholder="🔍 Search formulas, algorithms, topics...">
    </div>
    <div class="modal-body">
      <table class="cheat-table">
        <thead>
          <tr>
            <th style="width: 55px;">Rank</th>
            <th style="width: 80px;">Tier</th>
            <th>Question</th>
            <th>Core Exam Anchor</th>
            <th>Mnemonic</th>
          </tr>
        </thead>
        <tbody id="cheatTableBody">
        </tbody>
      </table>
    </div>
  </div>
</div>

<script>
const RAW_QUESTIONS = {questions_json};

class SoundFX {{
  constructor() {{
    this.ctx = null;
    this.enabled = true;
  }}

  init() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }}
  }}

  playFlip() {{
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(350, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(550, this.ctx.currentTime + 0.08);
    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.08);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.08);
  }}

  playSuccess() {{
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [523.25, 783.99].forEach((freq, idx) => {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, now + idx * 0.06);
      gain.gain.setValueAtTime(0.15, now + idx * 0.06);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.06 + 0.25);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + idx * 0.06);
      osc.stop(now + idx * 0.06 + 0.25);
    }});
  }}

  playMiss() {{
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    [220, 180].forEach((freq, idx) => {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(freq, now + idx * 0.08);
      gain.gain.setValueAtTime(0.1, now + idx * 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.15);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + idx * 0.08);
      osc.stop(now + idx * 0.08 + 0.15);
    }});
  }}

  playFanfare() {{
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const notes = [440, 554.37, 659.25, 880];
    const now = this.ctx.currentTime;
    notes.forEach((freq, idx) => {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, now + idx * 0.09);
      gain.gain.setValueAtTime(0.18, now + idx * 0.09);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.09 + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now + idx * 0.09);
      osc.stop(now + idx * 0.09 + 0.35);
    }});
  }}
}}

const sfx = new SoundFX();

let currentFilter = 'all';
let deck = [];
let missedDeck = [];
let currentIndex = 0;
let streak = 0;
let xp = 0;
let isRevealed = false;

const TIMER_OPTIONS = [45, 40, 90, 0];
let timerOptionIndex = 0;
let timerSeconds = 45;
let timerRemaining = 45;
let timerInterval = null;

const hudProgress = document.getElementById('hudProgress');
const hudStreak = document.getElementById('hudStreak');
const streakFire = document.getElementById('streakFire');
const hudXP = document.getElementById('hudXP');
const btnSoundToggle = document.getElementById('btnSoundToggle');
const btnTimerToggle = document.getElementById('btnTimerToggle');
const btnCheatSheet = document.getElementById('btnCheatSheet');
const timerBar = document.getElementById('timerBar');
const timerFill = document.getElementById('timerFill');
const drillCard = document.getElementById('drillCard');
const cardRankBadge = document.getElementById('cardRankBadge');
const cardTierBadge = document.getElementById('cardTierBadge');
const cardUnitBadge = document.getElementById('cardUnitBadge');
const cardMarksBadge = document.getElementById('cardMarksBadge');
const cardBloomBadge = document.getElementById('cardBloomBadge');
const cardIndexLabel = document.getElementById('cardIndexLabel');
const cardTitle = document.getElementById('cardTitle');
const revealCurtain = document.getElementById('revealCurtain');
const btnFlip = document.getElementById('btnFlip');
const revealedContent = document.getElementById('revealedContent');

const cardPunchline = document.getElementById('cardPunchline');
const cardMnemonic = document.getElementById('cardMnemonic');
const cardAnalogy = document.getElementById('cardAnalogy');
const btnToggleDiagram = document.getElementById('btnToggleDiagram');
const diagramBlock = document.getElementById('diagramBlock');
const diagramContent = document.getElementById('diagramContent');
const cardFullContent = document.getElementById('cardFullContent');
const gradingBar = document.getElementById('gradingBar');
const btnGradeMiss = document.getElementById('btnGradeMiss');
const btnGradeMid = document.getElementById('btnGradeMid');
const btnGradePerfect = document.getElementById('btnGradePerfect');
const victoryScreen = document.getElementById('victoryScreen');
const btnRestartDeck = document.getElementById('btnRestartDeck');
const btnFilterMissed = document.getElementById('btnFilterMissed');
const modalCheatSheet = document.getElementById('modalCheatSheet');
const btnCloseModal = document.getElementById('btnCloseModal');
const cheatSearchInput = document.getElementById('cheatSearchInput');
const cheatTableBody = document.getElementById('cheatTableBody');

function renderMath() {{
  if (window.renderMathInElement) {{
    window.renderMathInElement(document.body, {{
      delimiters: [
        {{left: '$$', right: '$$', display: true}},
        {{left: '$', right: '$', display: false}}
      ],
      throwOnError: false
    }});
  }}
}}

function buildDeck(filter) {{
  let list = [];
  if (filter === 'all') {{
    list = [...RAW_QUESTIONS];
  }} else if (filter === 'important') {{
    list = RAW_QUESTIONS.filter(q => q.important || q.tier === 1);
  }} else if (filter === 'tier1') {{
    list = RAW_QUESTIONS.filter(q => q.tier === 1);
  }} else if (filter === 'tier2') {{
    list = RAW_QUESTIONS.filter(q => q.tier === 2);
  }} else if (filter === 'tier3') {{
    list = RAW_QUESTIONS.filter(q => q.tier === 3);
  }} else if (filter === 'tier4') {{
    list = RAW_QUESTIONS.filter(q => q.tier === 4);
  }} else if (filter === '5m') {{
    list = RAW_QUESTIONS.filter(q => q.marks.includes('05') || q.marks.includes('5'));
  }} else if (filter === '10m') {{
    list = RAW_QUESTIONS.filter(q => q.marks.includes('10'));
  }} else if (filter === 'mid1') {{
    list = RAW_QUESTIONS.filter(q => q.mid === 'Mid-I');
  }} else if (filter === 'mid2') {{
    list = RAW_QUESTIONS.filter(q => q.mid === 'Mid-II');
  }} else if (filter === 'u1') {{
    list = RAW_QUESTIONS.filter(q => (q.unit || '').includes('1')).sort((a,b) => a.qno - b.qno);
  }} else if (filter === 'u2') {{
    list = RAW_QUESTIONS.filter(q => (q.unit || '').includes('2')).sort((a,b) => a.qno - b.qno);
  }} else if (filter === 'u3') {{
    list = RAW_QUESTIONS.filter(q => (q.unit || '').includes('3')).sort((a,b) => (a.mid === b.mid ? a.qno - b.qno : (a.mid === 'Mid-I' ? -1 : 1)));
  }} else if (filter === 'u4') {{
    list = RAW_QUESTIONS.filter(q => (q.unit || '').includes('4')).sort((a,b) => a.qno - b.qno);
  }} else if (filter === 'u5') {{
    list = RAW_QUESTIONS.filter(q => (q.unit || '').includes('5')).sort((a,b) => a.qno - b.qno);
  }} else if (filter === 'missed') {{
    list = [...missedDeck];
  }}
  return list;
}}

function initDeck(filter) {{
  currentFilter = filter;
  deck = buildDeck(filter);
  currentIndex = 0;
  isRevealed = false;
  victoryScreen.style.display = 'none';
  drillCard.style.display = 'flex';
  renderCurrentCard();
}}

function startTimer() {{
  clearInterval(timerInterval);
  if (timerSeconds === 0) {{
    timerBar.style.display = 'none';
    return;
  }}
  timerBar.style.display = 'block';
  timerRemaining = timerSeconds;
  updateTimerUI();

  timerInterval = setInterval(() => {{
    timerRemaining--;
    updateTimerUI();
    if (timerRemaining <= 0) {{
      clearInterval(timerInterval);
      if (!isRevealed) {{
        revealAnswer();
      }}
    }}
  }}, 1000);
}}

function updateTimerUI() {{
  const pct = Math.max(0, (timerRemaining / timerSeconds) * 100);
  timerFill.style.width = pct + '%';
  timerFill.classList.remove('warn', 'danger');
  if (pct <= 25) {{
    timerFill.classList.add('danger');
  }} else if (pct <= 50) {{
    timerFill.classList.add('warn');
  }}
}}

function renderCurrentCard() {{
  if (deck.length === 0 || currentIndex >= deck.length) {{
    showVictoryScreen();
    return;
  }}

  const q = deck[currentIndex];
  isRevealed = false;

  const cardImportantBadge = document.getElementById('cardImportantBadge');
  if (cardImportantBadge) {{
    cardImportantBadge.style.display = q.important ? 'inline-block' : 'none';
  }}

  cardRankBadge.textContent = 'Rank #' + q.rank;
  cardTierBadge.textContent = `Tier ${{q.tier}}: ${{q.tier_name}} (${{q.time}})`;
  cardTierBadge.className = `badge badge-tier${{q.tier}}`;
  cardUnitBadge.textContent = q.unit;
  cardMarksBadge.textContent = q.marks;
  cardBloomBadge.textContent = q.bloom;
  cardIndexLabel.textContent = `Card ${{currentIndex + 1}} of ${{deck.length}}`;
  cardTitle.textContent = q.title;

  cardPunchline.textContent = q.punchline || '';
  cardMnemonic.textContent = q.mnemonic || '';
  cardAnalogy.textContent = q.analogy || '';

  if (q.diagram && q.diagram.trim().length > 10) {{
    btnToggleDiagram.style.display = 'flex';
    diagramContent.textContent = q.diagram;
    diagramBlock.style.display = 'none';
    document.getElementById('diagramIcon').textContent = '▼';
  }} else {{
    btnToggleDiagram.style.display = 'none';
    diagramBlock.style.display = 'none';
  }}

  cardFullContent.innerHTML = q.html_content || '';

  revealCurtain.style.display = 'flex';
  revealedContent.style.display = 'none';
  gradingBar.style.display = 'none';

  hudProgress.textContent = `${{currentIndex + 1}} / ${{deck.length}}`;
  renderMath();
  startTimer();
}}

function revealAnswer() {{
  if (isRevealed) return;
  isRevealed = true;
  clearInterval(timerInterval);
  sfx.playFlip();

  revealCurtain.style.display = 'none';
  revealedContent.style.display = 'block';
  gradingBar.style.display = 'grid';
  cardFullContent.scrollTop = 0;
  renderMath();
}}

function handleGrade(grade) {{
  clearInterval(timerInterval);
  const q = deck[currentIndex];

  if (grade === 'miss') {{
    sfx.playMiss();
    streak = 0;
    if (!missedDeck.some(m => m.id === q.id)) {{
      missedDeck.push(q);
      updateMissedButton();
    }}
  }} else if (grade === 'mid') {{
    sfx.playSuccess();
    streak++;
    xp += 100 * Math.min(3, Math.max(1, Math.floor(streak / 3)));
  }} else if (grade === 'perfect') {{
    sfx.playSuccess();
    streak++;
    xp += 200 * Math.min(4, Math.max(1, Math.floor(streak / 2)));
    if (streak > 0 && streak % 5 === 0) {{
      sfx.playFanfare();
    }}
  }}

  updateHUD();
  currentIndex++;
  renderCurrentCard();
}}

function updateHUD() {{
  hudStreak.textContent = `${{streak}} Streak`;
  hudXP.textContent = xp;
  streakFire.textContent = streak >= 5 ? '🔥' : '⚡';
}}

function updateMissedButton() {{
  if (missedDeck.length > 0) {{
    btnFilterMissed.style.display = 'inline-block';
    btnFilterMissed.textContent = `Weak Spots (${{missedDeck.length}})`;
  }} else {{
    btnFilterMissed.style.display = 'none';
  }}
}}

function showVictoryScreen() {{
  clearInterval(timerInterval);
  timerBar.style.display = 'none';
  drillCard.style.display = 'none';
  victoryScreen.style.display = 'flex';
  sfx.playFanfare();

  if (missedDeck.length > 0) {{
    const victoryMissedBtn = document.getElementById('btnReviewMissedFromVictory');
    document.getElementById('victoryMissedCount').textContent = missedDeck.length;
    victoryMissedBtn.style.display = 'inline-flex';
    victoryMissedBtn.onclick = () => initDeck('missed');
  }}
}}

window.addEventListener('keydown', (e) => {{
  if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return;

  if (e.key === 'm' || e.key === 'M') {{
    e.preventDefault();
    if (audioPlayBtn) audioPlayBtn.click();
    return;
  }}

  if (modalCheatSheet.style.display === 'flex') {{
    if (e.key === 'Escape') closeModal();
    return;
  }}

  if (e.code === 'Space') {{
    e.preventDefault();
    if (!isRevealed) revealAnswer();
  }} else if (e.key === '1' || e.key === 'ArrowLeft') {{
    if (isRevealed) handleGrade('miss');
  }} else if (e.key === '2' || e.key === 'ArrowDown') {{
    if (isRevealed) handleGrade('mid');
  }} else if (e.key === '3' || e.key === 'ArrowRight') {{
    if (isRevealed) handleGrade('perfect');
  }} else if (e.key.toLowerCase() === 's') {{
    openModal();
  }}
}});

btnToggleDiagram.addEventListener('click', () => {{
  const isHidden = diagramBlock.style.display === 'none';
  diagramBlock.style.display = isHidden ? 'block' : 'none';
  document.getElementById('diagramIcon').textContent = isHidden ? '▲' : '▼';
}});

revealCurtain.addEventListener('click', revealAnswer);
btnGradeMiss.addEventListener('click', () => handleGrade('miss'));
btnGradeMid.addEventListener('click', () => handleGrade('mid'));
btnGradePerfect.addEventListener('click', () => handleGrade('perfect'));
btnRestartDeck.addEventListener('click', () => initDeck(currentFilter));

// Mobile Card Navigation Buttons
const btnPrevCard = document.getElementById('btnPrevCard');
const btnNextCard = document.getElementById('btnNextCard');

if (btnPrevCard) {{
  btnPrevCard.addEventListener('click', () => {{
    if (currentIndex > 0) {{
      currentIndex--;
      renderCurrentCard();
    }}
  }});
}}

if (btnNextCard) {{
  btnNextCard.addEventListener('click', () => {{
    if (currentIndex < deck.length - 1) {{
      currentIndex++;
      renderCurrentCard();
    }} else {{
      showVictoryScreen();
    }}
  }});
}}

// Tap anywhere on card to flip when unrevealed
drillCard.addEventListener('click', (e) => {{
  if (!isRevealed && !e.target.closest('button') && !e.target.closest('.card-badges')) {{
    revealAnswer();
  }}
}});

// Touch swipe gestures for mobile
let touchStartX = 0;
let touchStartY = 0;
drillCard.addEventListener('touchstart', (e) => {{
  touchStartX = e.changedTouches[0].screenX;
  touchStartY = e.changedTouches[0].screenY;
}}, {{ passive: true }});

drillCard.addEventListener('touchend', (e) => {{
  const touchEndX = e.changedTouches[0].screenX;
  const touchEndY = e.changedTouches[0].screenY;
  const dx = touchEndX - touchStartX;
  const dy = touchEndY - touchStartY;
  
  if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.4) {{
    if (dx < 0) {{
      // Swipe Left: reveal answer if hidden, or next card if revealed
      if (!isRevealed) {{
        revealAnswer();
      }} else if (currentIndex < deck.length - 1) {{
        currentIndex++;
        renderCurrentCard();
      }}
    }} else {{
      // Swipe Right: go back to previous card
      if (currentIndex > 0) {{
        currentIndex--;
        renderCurrentCard();
      }}
    }}
  }}
}}, {{ passive: true }});

btnSoundToggle.addEventListener('click', () => {{
  sfx.enabled = !sfx.enabled;
  btnSoundToggle.textContent = sfx.enabled ? '🔊 Audio ON' : '🔇 Audio OFF';
  if (sfx.enabled) sfx.playSuccess();
}});

btnTimerToggle.addEventListener('click', () => {{
  timerOptionIndex = (timerOptionIndex + 1) % TIMER_OPTIONS.length;
  timerSeconds = TIMER_OPTIONS[timerOptionIndex];
  btnTimerToggle.textContent = timerSeconds === 0 ? '⏱️ OFF' : `⏱️ ${{timerSeconds}}s`;
  startTimer();
}});

document.querySelectorAll('.filter-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    initDeck(btn.getAttribute('data-filter'));
  }});
}});

function openModal() {{
  modalCheatSheet.style.display = 'flex';
  document.documentElement.classList.add('modal-open');
  document.body.classList.add('modal-open');
  renderCheatTable();
  cheatSearchInput.focus();
}}

function closeModal() {{
  modalCheatSheet.style.display = 'none';
  document.documentElement.classList.remove('modal-open');
  document.body.classList.remove('modal-open');
}}

btnCheatSheet.addEventListener('click', openModal);
btnCloseModal.addEventListener('click', closeModal);

function renderCheatTable(query = '') {{
  const qLower = query.toLowerCase().trim();
  const rows = [];
  
  RAW_QUESTIONS.forEach(q => {{
    const titleMatch = q.title.toLowerCase().includes(qLower);
    const mnemMatch = (q.mnemonic || '').toLowerCase().includes(qLower);
    const punchMatch = (q.punchline || '').toLowerCase().includes(qLower);
    const tierMatch = `tier ${{q.tier}}`.includes(qLower);
    const impMatch = q.important && 'important faculty passing gun'.includes(qLower);
    
    if (!qLower || titleMatch || mnemMatch || punchMatch || tierMatch || impMatch) {{
      const plainText = q.punchline || '';
      const fireBadge = q.important ? ' <span style=\"color:#ef4444;\">🔥</span>' : '';
      rows.push(`
        <tr>
          <td><strong style="color: #38bdf8;">#${{q.rank}}</strong>${{fireBadge}}</td>
          <td><span class="badge badge-tier${{q.tier}}">T${{q.tier}}</span></td>
          <td><strong>${{q.title}}</strong></td>
          <td style="color: #fef08a;">${{plainText}}</td>
          <td style="color: #fde047; font-weight: 400;">${{q.mnemonic || ''}}</td>
        </tr>
      `);
    }}
  }});

  cheatTableBody.innerHTML = rows.join('');
  renderMath();
}}

cheatSearchInput.addEventListener('input', (e) => {{
  renderCheatTable(e.target.value);
}});

initDeck('all');

// --- LIVE LO-FI & AMBIENT AUDIO ENGINE ---
class StudyAudioManager {{
  constructor() {{
    this.ctx = null;
    this.masterGain = null;
    this.isPlaying = false;
    this.currentMode = 'stream_chillhop';
    
    // Ambient layers
    this.vinylActive = true;
    this.rainActive = false;
    
    // Generators & nodes
    this.lofiTimer = null;
    this.currentChordProgression = 0;
    this.rainSource = null;
    this.rainGain = null;
    this.vinylSource = null;
    this.vinylGain = null;
    this.brownSource = null;
    this.brownGain = null;
    this.binauralOscL = null;
    this.binauralOscR = null;
    this.binauralGain = null;
    
    // Online stream audio element
    this.streamAudio = new Audio();
    this.streamAudio.crossOrigin = "anonymous";
    this.streamAudio.preload = "none";
    
    // Live 24/7 Internet Radio Streams
    this.streamStations = {{
      'stream_chillhop': {{
        name: '☕ Live: 24/7 Chillhop & Lofi',
        url: 'https://streams.ilovemusic.de/iloveradio17.mp3'
      }},
      'stream_vgm_all': {{
        name: '🎮 Live: Video Game Lofi & VGM',
        url: 'https://relay.rainwave.cc/all.mp3'
      }},
      'stream_vgm_covers': {{
        name: '🍄 Live: Nintendo & Game Remixes',
        url: 'https://relay.rainwave.cc/covers.mp3'
      }},
      'stream_vgm_ocremix': {{
        name: '⚔️ Live: OverClocked ReMix (VGM)',
        url: 'https://relay.rainwave.cc/ocremix.mp3'
      }},
      'stream_vgm_chiptune': {{
        name: '👾 Live: 8-Bit Chiptune Radio',
        url: 'https://relay.rainwave.cc/chiptune.mp3'
      }},
      'stream_anime': {{
        name: '🌸 Live: Anime & Cozy Lofi',
        url: 'https://stream.zeno.fm/0r0xa792kwzuv'
      }},
      'stream_cafe': {{
        name: '☕ Live: Cafe Lofi Beats',
        url: 'https://play.streamafrica.net/lofiradio'
      }},
      'stream_berlin': {{
        name: '🏙️ Live: Berlin Lofi Radio',
        url: 'https://lofi.stream.laut.fm/lofi'
      }},
      'stream_nightwave': {{
        name: '🌌 Live: Nightwave Plaza (Vaporwave/Chill)',
        url: 'https://radio.plaza.one/mp3'
      }},
      'stream_chillout': {{
        name: '🍃 Live: Ambient Chillout Lounge',
        url: 'https://hirschmilch.de:7000/chillout.mp3'
      }}
    }};
    
    this.volume = 0.65;
  }}

  initContext() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {{
        this.ctx = new AudioCtx();
        this.masterGain = this.ctx.createGain();
        this.masterGain.gain.setValueAtTime(this.volume, this.ctx.currentTime);
        this.masterGain.connect(this.ctx.destination);
      }}
    }}
    if (this.ctx && this.ctx.state === 'suspended') {{
      this.ctx.resume();
    }}
  }}

  setVolume(val) {{
    this.volume = Math.max(0, Math.min(1, val));
    if (this.masterGain && this.ctx) {{
      this.masterGain.gain.setTargetAtTime(this.volume, this.ctx.currentTime, 0.05);
    }}
    if (this.streamAudio) {{
      this.streamAudio.volume = this.volume;
    }}
  }}

  togglePlay() {{
    this.initContext();
    if (this.isPlaying) {{
      this.stop();
      return false;
    }} else {{
      this.start();
      return true;
    }}
  }}

  setMode(mode) {{
    this.currentMode = mode;
    if (this.isPlaying) {{
      this.stopAllGenerators();
      this.startCurrentMode();
    }}
  }}

  start() {{
    this.initContext();
    this.isPlaying = true;
    this.startCurrentMode();
    if (this.vinylActive && (this.currentMode === 'lofi_synth' || this.currentMode.startsWith('stream_'))) {{
      this.startVinyl();
    }}
    if (this.rainActive) {{
      this.startRain();
    }}
  }}

  stop() {{
    this.isPlaying = false;
    this.stopAllGenerators();
    if (this.streamAudio) {{
      this.streamAudio.pause();
    }}
  }}

  startCurrentMode() {{
    if (this.currentMode.startsWith('stream_')) {{
      const station = this.streamStations[this.currentMode];
      if (station) {{
        this.startOnlineStream(station.url);
      }} else {{
        this.startOnlineStream(this.streamStations['stream_chillhop'].url);
      }}
      return;
    }}

    switch (this.currentMode) {{
      case 'lofi_synth':
        this.startLofiSynth();
        break;
      case 'rain':
        this.startRain(true);
        break;
      case 'binaural':
        this.startBinaural();
        break;
      case 'brown_noise':
        this.startBrownNoise();
        break;
      default:
        this.startOnlineStream(this.streamStations['stream_chillhop'].url);
        break;
    }}
  }}

  stopAllGenerators() {{
    if (this.lofiTimer) {{
      clearInterval(this.lofiTimer);
      this.lofiTimer = null;
    }}
    if (this.rainSource) {{
      try {{ this.rainSource.stop(); }} catch(e) {{}}
      this.rainSource = null;
    }}
    if (this.vinylSource) {{
      try {{ this.vinylSource.stop(); }} catch(e) {{}}
      this.vinylSource = null;
    }}
    if (this.brownSource) {{
      try {{ this.brownSource.stop(); }} catch(e) {{}}
      this.brownSource = null;
    }}
    if (this.binauralOscL) {{
      try {{ this.binauralOscL.stop(); }} catch(e) {{}}
      this.binauralOscL = null;
    }}
    if (this.binauralOscR) {{
      try {{ this.binauralOscR.stop(); }} catch(e) {{}}
      this.binauralOscR = null;
    }}
    if (this.streamAudio) {{
      this.streamAudio.pause();
    }}
  }}

  startOnlineStream(url) {{
    if (!this.streamAudio) {{
      this.streamAudio = new Audio();
      this.streamAudio.crossOrigin = "anonymous";
    }}
    this.streamAudio.pause();
    this.streamAudio.src = url;
    this.streamAudio.volume = this.volume;
    
    const playPromise = this.streamAudio.play();
    if (playPromise !== undefined) {{
      playPromise.catch(err => {{
        console.warn("Live stream network hiccup, gracefully falling back to offline Lo-Fi synth:", err);
        this.currentMode = 'lofi_synth';
        this.startLofiSynth();
        const sel = document.getElementById('audioModeSelect');
        if (sel) sel.value = 'lofi_synth';
      }});
    }}
  }}

  startLofiSynth() {{
    const progressions = [
      [
        [146.83, 220.00, 261.63, 329.63, 392.00],
        [196.00, 246.94, 293.66, 329.63, 349.23],
        [130.81, 196.00, 246.94, 293.66, 329.63],
        [220.00, 261.63, 329.63, 392.00, 493.88]
      ],
      [
        [174.61, 261.63, 329.63, 349.23, 440.00],
        [164.81, 246.94, 293.66, 329.63, 392.00],
        [146.83, 220.00, 261.63, 293.66, 349.23],
        [130.81, 196.00, 246.94, 329.63, 392.00]
      ],
      [
        [116.54, 174.61, 233.08, 293.66, 349.23],
        [110.00, 164.81, 220.00, 261.63, 329.63],
        [98.00, 146.83, 196.00, 246.94, 293.66],
        [87.31, 130.81, 174.61, 220.00, 261.63]
      ],
      [
        [130.81, 196.00, 246.94, 329.63, 392.00],
        [164.81, 246.94, 293.66, 329.63, 392.00],
        [174.61, 261.63, 329.63, 349.23, 440.00],
        [196.00, 261.63, 293.66, 349.23, 392.00]
      ]
    ];

    const currentProg = progressions[this.currentChordProgression % progressions.length];
    this.currentChordProgression++;

    let chordIndex = 0;
    const playNext = () => {{
      if (!this.isPlaying || this.currentMode !== 'lofi_synth') return;
      const notes = currentProg[chordIndex % currentProg.length];
      chordIndex++;
      this.playRhodesChord(notes, 4.0);
    }};

    playNext();
    this.lofiTimer = setInterval(playNext, 4200);
  }}

  playRhodesChord(freqs, duration) {{
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    freqs.forEach((freq, idx) => {{
      const osc1 = this.ctx.createOscillator();
      const osc2 = this.ctx.createOscillator();
      const noteGain = this.ctx.createGain();
      const filter = this.ctx.createBiquadFilter();

      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(850 + idx * 80, now);
      filter.frequency.exponentialRampToValueAtTime(320, now + duration);

      osc1.type = 'sine';
      osc2.type = 'triangle';

      const detune = (idx % 2 === 0 ? 1 : -1) * (2 + Math.random() * 3);
      osc1.frequency.setValueAtTime(freq, now);
      osc2.frequency.setValueAtTime(freq + detune, now);

      const stagger = idx * 0.045;
      const startTime = now + stagger;

      noteGain.gain.setValueAtTime(0.0001, startTime);
      noteGain.gain.linearRampToValueAtTime(0.07 / (1 + idx * 0.2), startTime + 0.08);
      noteGain.gain.exponentialRampToValueAtTime(0.0001, startTime + duration);

      osc1.connect(filter);
      osc2.connect(filter);
      filter.connect(noteGain);
      noteGain.connect(this.masterGain);

      osc1.start(startTime);
      osc2.start(startTime);
      osc1.stop(startTime + duration + 0.1);
      osc2.stop(startTime + duration + 0.1);
    }});
  }}

  startRain(isSolo = false) {{
    if (!this.ctx) return;
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {{
      data[i] = Math.random() * 2 - 1;
    }}

    this.rainSource = this.ctx.createBufferSource();
    this.rainSource.buffer = buffer;
    this.rainSource.loop = true;

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(800, this.ctx.currentTime);

    this.rainGain = this.ctx.createGain();
    this.rainGain.gain.setValueAtTime(isSolo ? 0.35 : 0.15, this.ctx.currentTime);

    this.rainSource.connect(filter);
    filter.connect(this.rainGain);
    this.rainGain.connect(this.masterGain);

    this.rainSource.start();
  }}

  startVinyl() {{
    if (!this.ctx) return;
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {{
      const isPop = Math.random() < 0.0025;
      data[i] = isPop ? (Math.random() * 2 - 1) * 0.8 : (Math.random() * 2 - 1) * 0.015;
    }}

    this.vinylSource = this.ctx.createBufferSource();
    this.vinylSource.buffer = buffer;
    this.vinylSource.loop = true;

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(2500, this.ctx.currentTime);
    filter.Q.setValueAtTime(1.5, this.ctx.currentTime);

    this.vinylGain = this.ctx.createGain();
    this.vinylGain.gain.setValueAtTime(0.12, this.ctx.currentTime);

    this.vinylSource.connect(filter);
    filter.connect(this.vinylGain);
    this.vinylGain.connect(this.masterGain);

    this.vinylSource.start();
  }}

  startBinaural() {{
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    
    this.binauralOscL = this.ctx.createOscillator();
    this.binauralOscR = this.ctx.createOscillator();
    this.binauralOscL.type = 'sine';
    this.binauralOscR.type = 'sine';
    this.binauralOscL.frequency.setValueAtTime(200, now);
    this.binauralOscR.frequency.setValueAtTime(240, now);

    const merger = this.ctx.createChannelMerger(2);
    this.binauralOscL.connect(merger, 0, 0);
    this.binauralOscR.connect(merger, 0, 1);

    this.binauralGain = this.ctx.createGain();
    this.binauralGain.gain.setValueAtTime(0.15, now);

    merger.connect(this.binauralGain);
    this.binauralGain.connect(this.masterGain);

    this.binauralOscL.start();
    this.binauralOscR.start();
  }}

  startBrownNoise() {{
    if (!this.ctx) return;
    const bufferSize = this.ctx.sampleRate * 2;
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    let lastOut = 0.0;
    for (let i = 0; i < bufferSize; i++) {{
      const white = Math.random() * 2 - 1;
      data[i] = (lastOut + (0.02 * white)) / 1.02;
      lastOut = data[i];
      data[i] *= 1.8;
    }}

    this.brownSource = this.ctx.createBufferSource();
    this.brownSource.buffer = buffer;
    this.brownSource.loop = true;

    this.brownGain = this.ctx.createGain();
    this.brownGain.gain.setValueAtTime(0.3, this.ctx.currentTime);

    this.brownSource.connect(this.brownGain);
    this.brownGain.connect(this.masterGain);

    this.brownSource.start();
  }}

  toggleVinyl() {{
    this.vinylActive = !this.vinylActive;
    if (this.vinylActive && this.isPlaying) {{
      this.startVinyl();
    }} else if (!this.vinylActive && this.vinylSource) {{
      try {{ this.vinylSource.stop(); }} catch(e){{}}
      this.vinylSource = null;
    }}
    return this.vinylActive;
  }}

  toggleRain() {{
    this.rainActive = !this.rainActive;
    if (this.rainActive && this.isPlaying) {{
      this.startRain(false);
    }} else if (!this.rainActive && this.rainSource && this.currentMode !== 'rain') {{
      try {{ this.rainSource.stop(); }} catch(e){{}}
      this.rainSource = null;
    }}
    return this.rainActive;
  }}
}}

window.studyAudio = new StudyAudioManager();

// Audio DOM Elements Wiring
const audioPlayBtn = document.getElementById('audioPlayBtn');
const audioModeSelect = document.getElementById('audioModeSelect');
const audioVolSlider = document.getElementById('audioVolSlider');
const ambientVinylBtn = document.getElementById('ambientVinylBtn');
const ambientRainBtn = document.getElementById('ambientRainBtn');

if (audioPlayBtn) {{
  audioPlayBtn.addEventListener('click', () => {{
    if (!window.studyAudio) return;
    const isPlaying = window.studyAudio.togglePlay();
    audioPlayBtn.classList.toggle('playing', isPlaying);
    audioPlayBtn.textContent = isPlaying ? '❚❚' : '▶';
  }});
}}

if (audioModeSelect) {{
  audioModeSelect.addEventListener('change', (e) => {{
    if (window.studyAudio) {{
      window.studyAudio.setMode(e.target.value);
    }}
  }});
}}

if (audioVolSlider) {{
  audioVolSlider.addEventListener('input', (e) => {{
    if (window.studyAudio) {{
      window.studyAudio.setVolume(parseFloat(e.target.value));
    }}
  }});
}}

if (ambientVinylBtn) {{
  ambientVinylBtn.addEventListener('click', () => {{
    if (window.studyAudio) {{
      const active = window.studyAudio.toggleVinyl();
      ambientVinylBtn.classList.toggle('active', active);
    }}
  }});
}}

if (ambientRainBtn) {{
  ambientRainBtn.addEventListener('click', () => {{
    if (window.studyAudio) {{
      const active = window.studyAudio.toggleRain();
      ambientRainBtn.classList.toggle('active', active);
    }}
  }});
}}
</script>
</body>
</html>
'''

out_p = os.path.join(os.path.dirname(__file__), "speedrun_trainer.html")
with open(out_p, "w", encoding="utf-8") as f:
    f.write(html_template)

print("Saved speedrun_trainer.html successfully with Student Exam Notes.")
