# -*- coding: utf-8 -*-
"""
Generates crisp, high-contrast, professional visual SVG diagrams for all 40 SVP questions.
Saves them into svp_study_suite/diagrams/ directory and produces diagrams_data.py for HTML inlining.
"""

import os, re, html

DIAGRAMS = {}

def svg_doc(w, h, inner):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="auto" class="flowchart-svg" style="max-width: {w}px; min-width: 580px; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="gradCard" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="gradCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="gradEmerald" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
    <linearGradient id="gradAmber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#d97706"/>
    </linearGradient>
    <linearGradient id="gradPurple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c084fc"/>
      <stop offset="100%" stop-color="#9333ea"/>
    </linearGradient>
    <linearGradient id="gradRose" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fb7185"/>
      <stop offset="100%" stop-color="#e11d48"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
    <marker id="arrCyan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrEmerald" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399"/>
    </marker>
    <marker id="arrAmber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#fbbf24"/>
    </marker>
  </defs>
  <rect width="{w}" height="{h}" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>
{inner}
</svg>'''

def box(x, y, w, h, title, sub="", stroke="#38bdf8", fill="#1e293b", badge="", badge_color="#38bdf8"):
    sub_lines = []
    if sub:
        raw_lines = sub.split('\\n') if '\\n' in sub else sub.split('\n')
        sub_lines = [l.strip() for l in raw_lines if l.strip()]

    if sub_lines:
        y_title = y + 18
        start_y = y_title + 16
        tspans = [f'<tspan x="{x + w/2}" y="{start_y + idx * 14}">{html.escape(l)}</tspan>' for idx, l in enumerate(sub_lines)]
        sub_text = f'<text font-size="11" fill="#cbd5e1" text-anchor="middle">{"".join(tspans)}</text>'
    else:
        y_title = y + h / 2 + 5
        sub_text = ''

    badge_markup = f'<rect x="{x + w - 75}" y="{y - 9}" width="70" height="18" rx="9" fill="{badge_color}" fill-opacity="0.25" stroke="{badge_color}" stroke-width="1"/><text x="{x + w - 40}" y="{y + 4}" font-size="9.5" font-weight="700" fill="{badge_color}" text-anchor="middle">{badge}</text>' if badge else ''
    return f'''  <g filter="url(#shadow)">
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>
    <text x="{x + w/2}" y="{y_title}" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">{html.escape(title)}</text>
    {sub_text}
    {badge_markup}
  </g>'''

def arrow(x1, y1, x2, y2, color="#38bdf8", label=""):
    lbl = f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2 - 6}" font-size="11" fill="{color}" font-weight="700" text-anchor="middle">{label}</text>' if label else ''
    marker = "arrCyan" if color == "#38bdf8" else ("arrEmerald" if color == "#34d399" else "arrAmber")
    return f'''  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2.5" marker-end="url(#{marker})"/>
  {lbl}'''

# --- UNIT 1: MID1-Q01 to MID1-Q08 ---

DIAGRAMS['MID1-Q01'] = svg_doc(740, 320, f'''
  <text x="370" y="32" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">SPEECH PRODUCTION: SOURCE-FILTER MECHANISM (FAN\\'S MODEL)</text>
  <rect x="20" y="55" width="220" height="235" rx="10" fill="#1e293b" fill-opacity="0.4" stroke="#fbbf24" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="130" y="78" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">EXCITATION SOURCE E(z)</text>
  {box(40, 95, 180, 50, "1. Lungs & Trachea", "Subglottal Air Pressure", "#fbbf24", "#0f172a")}
  {arrow(130, 145, 130, 185, "#fbbf24", "Airflow")}
  {box(40, 185, 180, 85, "2. Glottis / Vocal Cords", "Voiced: Pulses (Pitch F0)\\nUnvoiced: Turbulent Noise", "#fbbf24", "#0f172a", "Source", "#fbbf24")}

  {arrow(220, 225, 275, 225, "#38bdf8", "Raw Acoustic e(t)")}

  <rect x="275" y="55" width="260" height="235" rx="10" fill="#1e293b" fill-opacity="0.4" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="405" y="78" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOCAL TRACT FILTER H(z)</text>
  {box(295, 95, 220, 50, "Pharynx (Throat Cavity)", "Cross-section ~17.5 cm", "#38bdf8", "#0f172a")}
  {box(295, 155, 220, 55, "Oral & Nasal Cavities", "Resonances = Formants (F1, F2, F3)", "#38bdf8", "#0f172a", "Filter", "#38bdf8")}
  {box(295, 220, 220, 50, "Articulators (Tongue/Lips)", "Shaping Vowels & Consonants", "#38bdf8", "#0f172a")}

  {arrow(515, 225, 570, 225, "#34d399", "Acoustic Wave")}

  <rect x="570" y="55" width="150" height="235" rx="10" fill="#1e293b" fill-opacity="0.4" stroke="#34d399" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="645" y="78" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">OUTPUT s(t)</text>
  {box(580, 115, 130, 60, "Lip Radiation", "R(z) ≈ 1 - z^-1", "#34d399", "#0f172a")}
  {box(580, 195, 130, 75, "Radiated Speech", "S(z) = E·H·R\\nAudio Waveform", "#34d399", "#0f172a", "Speech", "#34d399")}
''')

DIAGRAMS['MID1-Q02'] = svg_doc(720, 280, f'''
  <text x="360" y="32" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">DISCRETE-TIME SPEECH SAMPLING &amp; NYQUIST RECONSTRUCTION</text>
  {box(20, 70, 140, 65, "Analog Speech s(t)", "Continuous Acoustic Wave", "#fbbf24")}
  {arrow(160, 102, 195, 102, "#fbbf24")}
  {box(195, 70, 150, 65, "Anti-Aliasing Filter", "Low-Pass LPF (fc = fs/2)", "#38bdf8", badge="Bandlimit")}
  {arrow(345, 102, 380, 102, "#38bdf8")}
  {box(380, 70, 145, 65, "ADC / Sampler", "Ts = 1/fs (8k / 16kHz)", "#c084fc", badge="Nyquist")}
  {arrow(525, 102, 560, 102, "#c084fc")}
  {box(560, 70, 140, 65, "Discrete Speech s[n]", "s[n] = s(n·Ts)", "#34d399", badge="Digital")}

  <path d="M 630 135 L 630 185 L 450 185" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#arrEmerald)"/>

  {box(300, 160, 150, 65, "D/A Converter", "Discrete Impulse Train", "#c084fc")}
  {arrow(300, 192, 250, 192, "#c084fc")}
  {box(100, 160, 150, 65, "Sinc Reconstruction", "Ideal Sinc LPF Filter", "#34d399", badge="Recover")}
  {arrow(100, 192, 40, 192, "#34d399")}
  <text x="25" y="196" font-size="12" font-weight="bold" fill="#34d399">s(t)</text>
  <rect x="40" y="240" width="640" height="28" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="360" y="258" font-size="11" fill="#f8fafc" text-anchor="middle">Nyquist Condition: fs ≥ 2·fmax | Undersampling causes overlapping spectral replicas (Aliasing)</text>
''')

DIAGRAMS['MID1-Q03'] = svg_doc(700, 310, f'''
  <text x="350" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">POLE-ZERO MODELING &amp; Z-PLANE STABILITY ANALYSIS</text>
  <!-- Z-plane Plot -->
  <g transform="translate(140, 170)">
    <circle cx="0" cy="0" r="85" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4 4"/>
    <text x="65" y="-65" font-size="11" fill="#cbd5e1">Unit Circle (|z|=1)</text>
    <line x1="-115" y1="0" x2="115" y2="0" stroke="#475569" stroke-width="1.5"/>
    <line x1="0" y1="-115" x2="0" y2="115" stroke="#475569" stroke-width="1.5"/>
    <text x="120" y="4" font-size="11" fill="#64748b">Re</text>
    <text x="4" y="-120" font-size="11" fill="#64748b">Im</text>
    <!-- Poles: x at (42.5, 0) and (34, 0) -->
    <text x="42.5" y="4" font-size="16" font-weight="bold" fill="#f43f5e" text-anchor="middle">×</text>
    <text x="42.5" y="-12" font-size="11" fill="#f43f5e" text-anchor="middle">p1=0.5</text>
    <text x="30" y="18" font-size="16" font-weight="bold" fill="#f43f5e" text-anchor="middle">×</text>
    <text x="25" y="32" font-size="11" fill="#f43f5e" text-anchor="middle">p2=0.4</text>
    <!-- Zeros: o at (0, 0) and (42.5, 0) -->
    <circle cx="0" cy="0" r="4" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="-12" y="-6" font-size="11" fill="#38bdf8">z1=0</text>
    <circle cx="42.5" cy="0" r="6" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="60" y="12" font-size="11" fill="#38bdf8">z2=0.5</text>
  </g>

  <!-- Right Details -->
  {box(310, 60, 370, 75, "System Transfer Function H(z)", "H(z) = [z(z - 0.5)] / [z² - 0.9z + 0.2] = z / (z - 0.4)", "#38bdf8", badge="Filter")}
  {box(310, 145, 370, 70, "Poles & Zeros Extraction", "Zeros (Numerator=0): z1 = 0, z2 = 0.5\\nPoles (Denominator=0): p1 = 0.5, p2 = 0.4", "#fbbf24")}
  {box(310, 225, 370, 65, "BIBO Stability Verdict: UNCONDITIONALLY STABLE", "All poles strictly INSIDE unit circle (|p1|=0.5 < 1, |p2|=0.4 < 1)", "#34d399", badge="Stable")}
''')

DIAGRAMS['MID1-Q04'] = svg_doc(720, 280, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">FAST FOURIER TRANSFORM (FFT) IN SPEECH RECOGNITION</text>
  {box(20, 65, 140, 60, "Speech Frame x[n]", "20 - 30 ms duration", "#fbbf24")}
  {arrow(160, 95, 195, 95, "#fbbf24")}
  {box(195, 65, 150, 60, "Hamming Window", "Prevents spectral leakage", "#38bdf8", badge="Window")}
  {arrow(345, 95, 380, 95, "#38bdf8")}
  {box(380, 65, 150, 60, "N-Point FFT", "O(N log N) Fast Engine", "#c084fc", badge="Cooley-Tukey")}
  {arrow(530, 95, 570, 75, "#34d399")}
  {arrow(530, 95, 570, 120, "#38bdf8")}
  {box(570, 45, 135, 50, "Magnitude |X[k]|", "Formant Peak Spectrum", "#34d399")}
  {box(570, 105, 135, 50, "Phase Spectrum", "∠X[k] Dispersion", "#38bdf8")}

  <rect x="20" y="175" width="685" height="85" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="198" font-size="12" font-weight="bold" fill="#fbbf24">6 Core Properties for Speech Recognition:</text>
  <text x="35" y="218" font-size="11" fill="#cbd5e1">1. Linearity: Preserves speech+noise superposition</text>
  <text x="35" y="235" font-size="11" fill="#cbd5e1">2. Conjugate Symmetry: Real speech -> X[N-k]=X*[k] (Save 50% compute)</text>
  <text x="35" y="252" font-size="11" fill="#cbd5e1">3. Time-Shift: Magnitude invariant to boundary offset</text>
  <text x="380" y="218" font-size="11" fill="#cbd5e1">4. Resolution: Δf = fs / N (Trade-off time vs frequency)</text>
  <text x="380" y="235" font-size="11" fill="#cbd5e1">5. Parseval's Theorem: Total energy preserved for VAD</text>
  <text x="380" y="252" font-size="11" fill="#cbd5e1">6. Periodicity: Rectangular window causes spectral leakage</text>
''')

DIAGRAMS['MID1-Q05'] = svg_doc(720, 300, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONVOLUTION OPERATIONS &amp; REAL-TIME OVERLAP-ADD (OLA)</text>
  {box(25, 60, 150, 60, "Glottal Excitation e[n]", "Pulse train / Noise source", "#fbbf24")}
  {arrow(175, 90, 230, 90, "#fbbf24", "Input")}
  {box(230, 60, 200, 60, "Vocal Tract Filter h[n]", "Resonances (Formants v[n] * r[n])", "#38bdf8", badge="LTI System")}
  {arrow(430, 90, 485, 90, "#34d399", "Convolution")}
  {box(485, 60, 200, 60, "Radiated Speech s[n]", "s[n] = e[n] * h[n] = Σ e[k]h[n-k]", "#34d399", badge="Output")}

  <rect x="25" y="140" width="665" height="145" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="162" font-size="12" font-weight="bold" fill="#38bdf8">Real-Time Streaming Speech Convolution (Overlap-Add Method):</text>
  {box(45, 175, 150, 50, "1. Split Stream", "Blocks of length L", "#c084fc")}
  {arrow(195, 200, 230, 200, "#c084fc")}
  {box(230, 175, 150, 50, "2. Fast FFT & Mult", "Y_i[k] = X_i[k] · H[k]", "#38bdf8")}
  {arrow(380, 200, 415, 200, "#38bdf8")}
  {box(415, 175, 140, 50, "3. Inverse IFFT", "Length L + M - 1", "#fbbf24")}
  {arrow(555, 200, 580, 200, "#34d399")}
  {box(580, 175, 95, 50, "4. Overlap & Add", "Stream Assembly", "#34d399")}
  <text x="45" y="265" font-size="11" fill="#cbd5e1">Avoids time-aliasing by zero-padding to N ≥ L + M - 1 | Eliminates infinite convolution latency</text>
''')

DIAGRAMS['MID1-Q06'] = svg_doc(720, 290, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">LINEAR VS. NON-LINEAR FILTER BANKS IN SPEECH DECOMPOSITION</text>
  
  <!-- Linear Filter Bank -->
  <g transform="translate(30, 60)">
    <rect width="315" height="150" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="157" y="25" font-size="13" font-weight="bold" fill="#38bdf8" text-anchor="middle">LINEAR FILTER BANK (Uniform STFT)</text>
    <!-- Uniform Filters -->
    <path d="M 25 120 L 45 60 L 65 120 M 65 120 L 85 60 L 105 120 M 105 120 L 125 60 L 145 120 M 145 120 L 165 60 L 185 120 M 185 120 L 205 60 L 225 120 M 225 120 L 245 60 L 265 120 M 265 120 L 285 60 L 305 120" fill="none" stroke="#38bdf8" stroke-width="2"/>
    <text x="157" y="140" font-size="11" fill="#cbd5e1" text-anchor="middle">Constant Bandwidth Δf (e.g. 100 Hz everywhere)</text>
  </g>

  <!-- Non-Linear Mel Filter Bank -->
  <g transform="translate(375, 60)">
    <rect width="315" height="150" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="157" y="25" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">NON-LINEAR MEL FILTER BANK (Human Hearing)</text>
    <!-- Non-uniform Filters -->
    <path d="M 20 120 L 35 60 L 50 120 M 45 120 L 65 60 L 85 120 M 80 120 L 110 60 L 140 120 M 130 120 L 175 60 L 220 120 M 205 120 L 260 60 L 305 120" fill="none" stroke="#34d399" stroke-width="2"/>
    <text x="157" y="140" font-size="11" fill="#cbd5e1" text-anchor="middle">Dense &lt;1 kHz (Fine Res) ──► Wide &gt;1 kHz (Coarse Res)</text>
  </g>

  <rect x="30" y="225" width="660" height="50" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="360" y="246" font-size="11" fill="#f8fafc" text-anchor="middle">Mel Scale: Mel(f) = 2595·log10(1 + f/700) | Models Cochlear Tonotopy &amp; Critical Bands</text>
  <text x="360" y="264" font-size="11" fill="#cbd5e1" text-anchor="middle">Linear: Invertible waveform resynthesis | Mel: Maximizes phoneme discriminability for ASR (MFCC)</text>
''')

DIAGRAMS['MID1-Q07'] = svg_doc(720, 310, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">PART A: 4-POINT DFT &amp; PART B: FREQUENCY RESOLUTION</text>

  <!-- Left: 4-Point DFT -->
  <g transform="translate(25, 55)">
    <rect width="320" height="235" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="160" y="26" font-size="13" font-weight="bold" fill="#fbbf24" text-anchor="middle">PART A: 4-Point DFT of x[n]=[2, 1, 0, 1]</text>
    <text x="20" y="55" font-size="11" fill="#cbd5e1">Twiddle Matrix Multiply [W4] · [x]:</text>
    <text x="20" y="75" font-size="11" fill="#f8fafc">X[0] = 2 + 1 + 0 + 1 = <tspan fill="#34d399" font-weight="bold">4</tspan> (DC Component)</text>
    <text x="20" y="95" font-size="11" fill="#f8fafc">X[1] = 2 - j + 0 + j = <tspan fill="#38bdf8" font-weight="bold">2</tspan> (Dominant AC)</text>
    <text x="20" y="115" font-size="11" fill="#f8fafc">X[2] = 2 - 1 + 0 - 1 = <tspan fill="#cbd5e1" font-weight="bold">0</tspan></text>
    <text x="20" y="135" font-size="11" fill="#f8fafc">X[3] = 2 + j + 0 - j = <tspan fill="#38bdf8" font-weight="bold">2</tspan> (Dominant AC)</text>
    
    <!-- Magnitude Bars -->
    <text x="20" y="165" font-size="11" font-weight="bold" fill="#fbbf24">Magnitude Spectrum |X[k]|:</text>
    <rect x="35" y="180" width="35" height="40" fill="#34d399" rx="3"/>
    <text x="52" y="205" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">4.0</text>
    <rect x="85" y="200" width="35" height="20" fill="#38bdf8" rx="3"/>
    <text x="102" y="215" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">2.0</text>
    <rect x="135" y="219" width="35" height="1" fill="#cbd5e1"/>
    <text x="152" y="215" font-size="11" fill="#cbd5e1" text-anchor="middle">0</text>
    <rect x="185" y="200" width="35" height="20" fill="#38bdf8" rx="3"/>
    <text x="202" y="215" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">2.0</text>
    <text x="52" y="232" font-size="9" fill="#cbd5e1" text-anchor="middle">k=0</text>
    <text x="102" y="232" font-size="9" fill="#cbd5e1" text-anchor="middle">k=1</text>
    <text x="152" y="232" font-size="9" fill="#cbd5e1" text-anchor="middle">k=2</text>
    <text x="202" y="232" font-size="9" fill="#cbd5e1" text-anchor="middle">k=3</text>
  </g>

  <!-- Right: Frequency Resolution -->
  <g transform="translate(370, 55)">
    <rect width="325" height="235" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="162" y="26" font-size="13" font-weight="bold" fill="#34d399" text-anchor="middle">PART B: FREQUENCY RESOLUTION</text>
    <text x="20" y="58" font-size="11" fill="#cbd5e1">Given: fs = 8 kHz = 8000 Hz, Frame N = 256</text>
    
    <rect x="20" y="75" width="285" height="55" rx="6" fill="#090d16" stroke="#34d399"/>
    <text x="30" y="95" font-size="11" font-weight="bold" fill="#34d399">Task 1: Frequency Resolution (Δf)</text>
    <text x="30" y="115" font-size="12" fill="#f8fafc">Δf = fs / N = 8000 / 256 = <tspan fill="#34d399" font-weight="bold">31.25 Hz/bin</tspan></text>

    <rect x="20" y="145" width="285" height="55" rx="6" fill="#090d16" stroke="#38bdf8"/>
    <text x="30" y="165" font-size="11" font-weight="bold" fill="#38bdf8">Task 2: Frequency for Bin k = 10</text>
    <text x="30" y="185" font-size="12" fill="#f8fafc">f10 = k · Δf = 10 × 31.25 = <tspan fill="#38bdf8" font-weight="bold">312.5 Hz</tspan></text>

    <text x="20" y="222" font-size="11" fill="#cbd5e1">Falls in female/child pitch &amp; closed vowel F1 formant range</text>
  </g>
''')

DIAGRAMS['MID1-Q08'] = svg_doc(720, 310, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">LINEAR PREDICTIVE CODING (LPC) ANALYSIS &amp; SYNTHESIS</text>
  
  <!-- LPC Analysis -->
  <g transform="translate(25, 55)">
    <rect width="670" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="335" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">LPC ENCODER (ANALYSIS): All-Pole Autoregressive Prediction</text>
    {box(40, 38, 120, 50, "Speech s[n]", "Past p samples", "#fbbf24")}
    {arrow(160, 63, 215, 63, "#fbbf24")}
    {box(215, 38, 180, 50, "LPC Predictor ak", "Yule-Walker / Levinson", "#38bdf8", badge="O(p²)")}
    {arrow(395, 63, 450, 63, "#38bdf8", "s^[n]")}
    {box(450, 38, 90, 50, "Difference", "e[n]=s - s^", "#c084fc")}
    {arrow(540, 63, 580, 63, "#34d399")}
    {box(580, 38, 100, 50, "Residual e[n]", "Pitch / Gain G", "#34d399")}
  </g>

  <!-- LPC Synthesis -->
  <g transform="translate(25, 175)">
    <rect width="670" height="115" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="335" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">LPC DECODER (SYNTHESIS): Vocal Tract Resynthesis</text>
    {box(40, 38, 150, 55, "Excitation Source", "Pitch pulses (Voiced)\\nNoise (Unvoiced)", "#fbbf24")}
    {arrow(190, 65, 250, 65, "#fbbf24", "Gain G")}
    {box(250, 38, 230, 55, "All-Pole Synthesis Filter", "H(z) = G / (1 - Σ ak z^-k)", "#34d399", badge="Resonator")}
    {arrow(480, 65, 540, 65, "#34d399")}
    {box(540, 38, 140, 55, "Reconstructed Speech", "Natural Audio 2.4 kbps", "#34d399", badge="LPC-10")}
  </g>
''')

# --- UNIT 2: MID1-Q09 to MID1-Q16 ---

DIAGRAMS['MID1-Q09'] = svg_doc(740, 270, f'''
  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">SPEECH FEATURE EXTRACTION PIPELINE (MFCC)</text>
  {box(15, 55, 90, 55, "1. Pre-emp", "1 - 0.97z^-1", "#fbbf24")}
  {arrow(105, 82, 120, 82, "#fbbf24")}
  {box(120, 55, 90, 55, "2. Framing", "25ms, 10ms", "#38bdf8")}
  {arrow(210, 82, 225, 82, "#38bdf8")}
  {box(225, 55, 95, 55, "3. Window", "Hamming", "#38bdf8")}
  {arrow(320, 82, 335, 82, "#38bdf8")}
  {box(335, 55, 85, 55, "4. FFT", "|X[k]| Mag", "#c084fc")}
  {arrow(420, 82, 435, 82, "#c084fc")}
  {box(435, 55, 95, 55, "5. Mel Filter", "26-40 Banks", "#34d399")}
  {arrow(530, 82, 545, 82, "#34d399")}
  {box(545, 55, 85, 55, "6. Log E", "Loudness", "#fbbf24")}
  {arrow(630, 82, 645, 82, "#fbbf24")}
  {box(645, 55, 80, 55, "7. DCT-II", "13 MFCC", "#34d399", badge="Static")}

  {arrow(685, 110, 685, 145, "#34d399")}
  <rect x="15" y="145" width="710" height="105" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="170" font-size="12" font-weight="bold" fill="#34d399">Dynamic Derivative Augmentation (Final 39-D Vector):</text>
  {box(35, 185, 205, 50, "13 Static MFCCs (c0 - c12)", "Instantaneous Vocal Posture", "#38bdf8")}
  <text x="255" y="215" font-size="18" fill="#cbd5e1" font-weight="bold">+</text>
  {box(275, 185, 200, 50, "13 Delta Features (Δc)", "Spectral Velocity / Transitions", "#fbbf24")}
  <text x="490" y="215" font-size="18" fill="#cbd5e1" font-weight="bold">+</text>
  {box(510, 185, 200, 50, "13 Delta-Delta (Δ²c)", "Articulatory Acceleration", "#c084fc")}
''')

DIAGRAMS['MID1-Q10'] = svg_doc(720, 280, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">STATIC VS. DYNAMIC SPEECH FEATURES (39-D ASR VECTOR)</text>
  
  <!-- Temporal Frame Evolution -->
  <g transform="translate(40, 60)">
    {box(0, 0, 100, 50, "Frame t-2", "c(t-2)", "#475569")}
    {box(130, 0, 100, 50, "Frame t-1", "c(t-1)", "#475569")}
    {box(260, 0, 120, 50, "Frame t", "c(t) [CURRENT]", "#38bdf8", badge="Target")}
    {box(410, 0, 100, 50, "Frame t+1", "c(t+1)", "#475569")}
    {box(540, 0, 100, 50, "Frame t+2", "c(t+2)", "#475569")}
  </g>

  <!-- Hierarchy -->
  <path d="M 360 115 L 360 145 M 360 145 L 140 145 L 140 170 M 360 145 L 360 170 M 360 145 L 580 145 L 580 170" fill="none" stroke="#94a3b8" stroke-width="2"/>

  {box(30, 170, 220, 85, "1. STATIC FEATURES (13-D)", "c0 to c12 MFCCs\\nRepresents instantaneous vocal tract posture at frame t", "#38bdf8", badge="Static")}
  {box(270, 170, 200, 85, "2. DELTA (13-D)", "Δc(t) = Velocity\\nRate of spectral change across neighboring frames", "#fbbf24", badge="Delta")}
  {box(490, 170, 200, 85, "3. DELTA-DELTA (13-D)", "Δ²c(t) = Acceleration\\nSecond-order derivative of articulatory transitions", "#34d399", badge="Delta-Delta")}
''')

DIAGRAMS['MID1-Q11'] = svg_doc(720, 290, f'''
  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">SPEECH FRAMING NUMERICAL: 1600 SAMPLES ──► 7 FRAMES</text>
  
  <!-- Signal Ruler -->
  <rect x="40" y="55" width="640" height="20" rx="4" fill="#1e293b" stroke="#64748b"/>
  <text x="40" y="50" font-size="11" fill="#cbd5e1">Sample 0</text>
  <text x="200" y="50" font-size="11" fill="#cbd5e1">400</text>
  <text x="360" y="50" font-size="11" fill="#cbd5e1">800</text>
  <text x="520" y="50" font-size="11" fill="#cbd5e1">1200</text>
  <text x="660" y="50" font-size="11" fill="#34d399" font-weight="bold">1600 Total</text>

  <!-- 7 Frames Overlap -->
  <g transform="translate(40, 85)">
    <!-- Frame 1 -->
    <rect x="0" y="0" width="160" height="18" rx="3" fill="#38bdf8" fill-opacity="0.8"/>
    <text x="80" y="13" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 1: [0 - 399]</text>
    <!-- Frame 2 -->
    <rect x="80" y="22" width="160" height="18" rx="3" fill="#38bdf8" fill-opacity="0.8"/>
    <text x="160" y="35" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 2: [200 - 599]</text>
    <!-- Frame 3 -->
    <rect x="160" y="44" width="160" height="18" rx="3" fill="#38bdf8" fill-opacity="0.8"/>
    <text x="240" y="57" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 3: [400 - 799]</text>
    <!-- Frame 4 -->
    <rect x="240" y="66" width="160" height="18" rx="3" fill="#38bdf8" fill-opacity="0.8"/>
    <text x="320" y="79" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 4: [600 - 999]</text>
    <!-- Frame 5 -->
    <rect x="320" y="88" width="160" height="18" rx="3" fill="#38bdf8" fill-opacity="0.8"/>
    <text x="400" y="101" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 5: [800 - 1199]</text>
    <!-- Frame 6 -->
    <rect x="400" y="110" width="160" height="18" rx="3" fill="#38bdf8" fill-opacity="0.8"/>
    <text x="480" y="123" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 6: [1000 - 1399]</text>
    <!-- Frame 7 -->
    <rect x="480" y="132" width="160" height="18" rx="3" fill="#34d399"/>
    <text x="560" y="145" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">Frame 7: [1200 - 1599] (END)</text>
  </g>

  <rect x="40" y="245" width="640" height="35" rx="6" fill="#1e293b" stroke="#34d399"/>
  <text x="360" y="267" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Formula: K = ⌊(L - N)/R⌋ + 1 = ⌊(1600 - 400)/200⌋ + 1 = 6 + 1 = 7 Frames (Hop R = 200)</text>
''')

DIAGRAMS['MID1-Q12'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">LPCC VS. MFCC ARCHITECTURAL COMPARISON</text>
  
  <!-- LPCC Path -->
  <g transform="translate(30, 50)">
    <rect width="660" height="90" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="330" y="20" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">LPCC: Acoustic All-Pole Tube Model (Noise-Sensitive, No Zeros)</text>
    {box(30, 32, 100, 45, "Raw Speech", "Linear scale", "#fbbf24")}
    {arrow(130, 54, 170, 54, "#fbbf24")}
    {box(170, 32, 130, 45, "LPC Analysis", "Yule-Walker / Levinson", "#fbbf24")}
    {arrow(300, 54, 340, 54, "#fbbf24")}
    {box(340, 32, 120, 45, "Predictor ak", "All-pole filter", "#fbbf24")}
    {arrow(460, 54, 500, 54, "#fbbf24")}
    {box(500, 32, 130, 45, "LPCCs", "Recursive Cepstrum", "#fbbf24", badge="Low Bitrate")}
  </g>

  <!-- MFCC Path -->
  <g transform="translate(30, 155)">
    <rect width="660" height="95" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="330" y="20" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">MFCC: Human Auditory Cochlea Model (Highly Robust to Noise, ASR Standard)</text>
    {box(30, 32, 85, 45, "Raw Speech", "Pre-emphasized", "#34d399")}
    {arrow(115, 54, 140, 54, "#34d399")}
    {box(140, 32, 80, 45, "FFT", "|X[k]| Mag", "#34d399")}
    {arrow(220, 54, 245, 54, "#34d399")}
    {box(245, 32, 120, 45, "Mel Filterbank", "Critical bands", "#34d399")}
    {arrow(365, 54, 390, 54, "#34d399")}
    {box(390, 32, 80, 45, "Log E", "Loudness", "#34d399")}
    {arrow(470, 54, 495, 54, "#34d399")}
    {box(495, 32, 135, 45, "13 MFCCs", "DCT-II Decorrelation", "#34d399", badge="ASR Standard")}
  </g>
''')

DIAGRAMS['MID1-Q13'] = svg_doc(700, 300, f'''
  <text x="350" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">DISTANCE MEASURES &amp; DYNAMIC TIME WARPING (DTW)</text>
  
  <!-- Left: DTW Grid -->
  <g transform="translate(40, 55)">
    <rect width="260" height="225" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="130" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">DTW Grid &amp; Optimal Warping Path</text>
    <line x1="40" y1="195" x2="230" y2="195" stroke="#475569" stroke-width="1.5"/>
    <line x1="40" y1="195" x2="40" y2="40" stroke="#475569" stroke-width="1.5"/>
    <text x="135" y="212" font-size="11" fill="#cbd5e1">Reference Template i (Length N)</text>
    <text x="25" y="115" font-size="11" fill="#cbd5e1" transform="rotate(-90 25 115)">Test Utterance j (M)</text>
    <!-- Warping Path -->
    <path d="M 40 195 L 70 170 L 95 160 L 130 120 L 160 100 L 180 80 L 220 50" fill="none" stroke="#34d399" stroke-width="3"/>
    <circle cx="40" cy="195" r="4" fill="#fbbf24"/>
    <text x="48" y="190" font-size="9" fill="#fbbf24">(1, 1)</text>
    <circle cx="220" cy="50" r="4" fill="#fbbf24"/>
    <text x="210" y="42" font-size="9" fill="#fbbf24">(N, M)</text>
    <!-- Sakoe-Chiba constraint band -->
    <path d="M 40 165 L 190 40 M 70 195 L 220 70" fill="none" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/>
  </g>

  <!-- Right: 3 Measures Comparison -->
  {box(330, 55, 335, 65, "1. Euclidean Distance d_E", "d = √Σ(xi - yi)² | Assumes equal variance & no correlation", "#38bdf8", badge="Fast O(D)")}
  {box(330, 135, 335, 65, "2. Mahalanobis Distance d_M", "d = √[(x - y)ᵀ Σ⁻¹ (x - y)] | Accounts for feature covariance", "#fbbf24", badge="Scale-Inv")}
  {box(330, 215, 335, 65, "3. Dynamic Time Warping (DTW)", "D(i,j) = d + min{D(i-1,j), D(i,j-1), D(i-1,j-1)}", "#34d399", badge="Temporal")}
''')

DIAGRAMS['MID1-Q14'] = svg_doc(720, 280, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">VECTOR QUANTIZATION (VQ) &amp; LBG ALGORITHM</text>
  
  <!-- Voronoi Cells -->
  <g transform="translate(40, 55)">
    <rect width="280" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="140" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Voronoi Tessellation of Feature Space</text>
    <!-- Voronoi lines -->
    <line x1="40" y1="40" x2="140" y2="105" stroke="#475569" stroke-width="1.5"/>
    <line x1="140" y1="105" x2="240" y2="60" stroke="#475569" stroke-width="1.5"/>
    <line x1="140" y1="105" x2="130" y2="195" stroke="#475569" stroke-width="1.5"/>
    <!-- Centroids -->
    <circle cx="85" cy="70" r="5" fill="#38bdf8"/>
    <text x="95" y="70" font-size="11" fill="#38bdf8" font-weight="bold">y1 (R1)</text>
    <circle cx="190" cy="80" r="5" fill="#34d399"/>
    <text x="200" y="80" font-size="11" fill="#34d399" font-weight="bold">y2 (R2)</text>
    <circle cx="80" cy="155" r="5" fill="#fbbf24"/>
    <text x="90" y="155" font-size="11" fill="#fbbf24" font-weight="bold">y3 (R3)</text>
    <circle cx="195" cy="155" r="5" fill="#c084fc"/>
    <text x="205" y="155" font-size="11" fill="#c084fc" font-weight="bold">y4 (R4)</text>
    <text x="140" y="195" font-size="9" fill="#cbd5e1" text-anchor="middle">Maps 39-D vector x to nearest codevector y_k</text>
  </g>

  <!-- LBG Flowchart -->
  {box(350, 55, 335, 45, "1. Initial Global Centroid (K=1)", "Average of all training speech vectors", "#fbbf24")}
  {arrow(517, 100, 517, 115, "#fbbf24")}
  {box(350, 115, 335, 45, "2. Centroid Splitting (K ──► 2K)", "y+ = y(1 + ε), y- = y(1 - ε)", "#c084fc", badge="Split")}
  {arrow(517, 160, 517, 175, "#c084fc")}
  {box(350, 175, 335, 45, "3. K-Means Nearest Assignment", "Classify vectors into Voronoi cells R_i", "#38bdf8")}
  {arrow(517, 220, 517, 235, "#38bdf8")}
  {box(350, 235, 335, 45, "4. Iterate until Distortion Converges", "Generates optimal codebook (K=64-256)", "#34d399", badge="Done")}
''')

DIAGRAMS['MID1-Q15'] = svg_doc(720, 290, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">GAUSSIAN MIXTURE MODEL (GMM) &amp; EM ESTIMATION CYCLE</text>
  
  <!-- Left: Multi-modal curve -->
  <g transform="translate(40, 55)">
    <rect width="290" height="215" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="145" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Multi-modal Speech Density p(x|λ)</text>
    <!-- Component 1 -->
    <path d="M 25 180 Q 75 40 125 180" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="75" y="75" font-size="9" fill="#fbbf24">Comp 1 (w1)</text>
    <!-- Component 2 -->
    <path d="M 100 180 Q 170 20 240 180" fill="none" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3 3"/>
    <text x="170" y="55" font-size="9" fill="#34d399">Comp 2 (w2)</text>
    <!-- Composite Envelope -->
    <path d="M 25 180 C 65 50 110 80 160 30 C 200 40 230 120 265 180" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <line x1="20" y1="180" x2="270" y2="180" stroke="#64748b" stroke-width="1.5"/>
    <text x="145" y="200" font-size="11" fill="#cbd5e1" text-anchor="middle">Composite: p(x) = Σ wm·N(x; μm, Σm)</text>
  </g>

  <!-- Right: EM Cycle -->
  {box(360, 55, 320, 90, "E-STEP (Expectation)", "Compute posterior responsibilities:\\nγm(xt) = wm·N(xt; μm, Σm) / Σ wj·N(xt; μj, Σj)", "#fbbf24", badge="E-Step")}
  <path d="M 520 145 L 520 175" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#arrEmerald)"/>
  <path d="M 360 215 L 340 215 L 340 100 L 360 100" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="325" y="155" font-size="9" fill="#c084fc" transform="rotate(-90 325 155)">Iterate until ΔL &lt; ε</text>
  {box(360, 175, 320, 95, "M-STEP (Maximization)", "Re-estimate mixture parameters:\\nwm = (1/T) Σ γm(xt)\\nμm = Σ γm(xt)·xt / Σ γm(xt)\\nΣm = Σ γm(xt)·(xt - μm)(xt - μm)ᵀ / Σ γm", "#34d399", badge="M-Step")}
''')

DIAGRAMS['MID1-Q16'] = svg_doc(740, 270, f'''
  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">3-STATE LEFT-TO-RIGHT (BAKIS) HMM FOR CONTINUOUS SPEECH</text>
  
  <!-- State 1 -->
  <g transform="translate(60, 75)">
    <circle cx="50" cy="50" r="42" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="50" y="45" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">State 1</text>
    <text x="50" y="60" font-size="11" fill="#38bdf8" text-anchor="middle">(Onset)</text>
    <!-- Self loop -->
    <path d="M 30 15 C 20 -15 80 -15 70 15" fill="none" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrCyan)"/>
    <text x="50" y="-18" font-size="11" fill="#38bdf8" font-weight="bold" text-anchor="middle">a11</text>
    <!-- Emission -->
    <line x1="50" y1="92" x2="50" y2="130" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrCyan)"/>
    <text x="50" y="145" font-size="11" fill="#38bdf8" font-weight="bold" text-anchor="middle">b1(ot) [MFCC]</text>
  </g>

  <!-- Transition a12 -->
  <line x1="152" y1="125" x2="225" y2="125" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrAmber)"/>
  <text x="188" y="118" font-size="11" fill="#fbbf24" font-weight="bold" text-anchor="middle">a12</text>

  <!-- State 2 -->
  <g transform="translate(230, 75)">
    <circle cx="50" cy="50" r="42" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
    <text x="50" y="45" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">State 2</text>
    <text x="50" y="60" font-size="11" fill="#fbbf24" text-anchor="middle">(Nucleus)</text>
    <!-- Self loop -->
    <path d="M 30 15 C 20 -15 80 -15 70 15" fill="none" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrAmber)"/>
    <text x="50" y="-18" font-size="11" fill="#fbbf24" font-weight="bold" text-anchor="middle">a22</text>
    <!-- Emission -->
    <line x1="50" y1="92" x2="50" y2="130" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrAmber)"/>
    <text x="50" y="145" font-size="11" fill="#fbbf24" font-weight="bold" text-anchor="middle">b2(ot) [MFCC]</text>
  </g>

  <!-- Transition a23 -->
  <line x1="322" y1="125" x2="395" y2="125" stroke="#34d399" stroke-width="2" marker-end="url(#arrEmerald)"/>
  <text x="358" y="118" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">a23</text>

  <!-- State 3 -->
  <g transform="translate(400, 75)">
    <circle cx="50" cy="50" r="42" fill="#1e293b" stroke="#34d399" stroke-width="2"/>
    <text x="50" y="45" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">State 3</text>
    <text x="50" y="60" font-size="11" fill="#34d399" text-anchor="middle">(Coda)</text>
    <!-- Self loop -->
    <path d="M 30 15 C 20 -15 80 -15 70 15" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#arrEmerald)"/>
    <text x="50" y="-18" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">a33</text>
    <!-- Emission -->
    <line x1="50" y1="92" x2="50" y2="130" stroke="#34d399" stroke-width="2" marker-end="url(#arrEmerald)"/>
    <text x="50" y="145" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">b3(ot) [MFCC]</text>
  </g>

  <!-- Right: 3 Problems Summary -->
  <g transform="translate(520, 65)">
    <rect width="190" height="155" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="95" y="22" font-size="11" font-weight="bold" fill="#c084fc" text-anchor="middle">The 3 HMM Problems:</text>
    <text x="15" y="50" font-size="11" fill="#f8fafc">1. Evaluation:</text>
    <text x="25" y="68" font-size="9" fill="#38bdf8">Forward Algorithm</text>
    <text x="15" y="90" font-size="11" fill="#f8fafc">2. Decoding:</text>
    <text x="25" y="108" font-size="9" fill="#fbbf24">Viterbi (Dynamic Prog)</text>
    <text x="15" y="130" font-size="11" fill="#f8fafc">3. Learning / Training:</text>
    <text x="25" y="148" font-size="9" fill="#34d399">Baum-Welch (EM)</text>
  </g>
''')

# --- UNIT 3: MID1-Q17 to MID1-Q20 & MID2-Q01 to MID2-Q04 ---

DIAGRAMS['MID1-Q17'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">MULTI-DIMENSIONAL SIGNALS TAXONOMY &amp; PROPERTIES</text>
  {box(25, 60, 150, 85, "1D Signal: Speech", "s(t) = Amplitude vs Time\\nStrictly Causal\\nBandwidth: ~64 kbps", "#fbbf24")}
  {arrow(175, 102, 205, 102, "#fbbf24")}
  {box(205, 60, 150, 85, "2D Signal: Image", "f(x, y) = 2D Spatial Grid\\nNon-causal in space\\nBandwidth: ~5 MB/img", "#38bdf8")}
  {arrow(355, 102, 385, 102, "#38bdf8")}
  {box(385, 60, 150, 85, "3D Signal: Video", "f(x, y, t) = Space + Time\\nTemporal correlation\\nBandwidth: ~3.0 Gbps", "#c084fc")}
  {arrow(535, 102, 565, 102, "#c084fc")}
  {box(565, 60, 130, 85, "3D/4D Medical", "f(x, y, z, t)\\nVolumetric CT/MRI", "#34d399")}

  <rect x="25" y="165" width="670" height="85" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="190" font-size="12" font-weight="bold" fill="#38bdf8">Key Multi-Dimensional Signal Characteristics:</text>
  <text x="45" y="210" font-size="11" fill="#cbd5e1">1. High Spatial Correlation: Adjacent pixels have &gt;90% similar intensity</text>
  <text x="45" y="228" font-size="11" fill="#cbd5e1">2. Non-Causal Space: Processing accesses left, right, top, and bottom simultaneously</text>
  <text x="380" y="210" font-size="11" fill="#cbd5e1">3. Separability: f(x, y) = f1(x) · f2(y) (Saves O(N²) ops)</text>
  <text x="380" y="228" font-size="11" fill="#cbd5e1">4. Massive Data Rates: Demands transform-domain compression</text>
''')

DIAGRAMS['MID1-Q18'] = svg_doc(720, 280, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">2D-DFT ROW-COLUMN COMPUTATION &amp; SPECTRAL INTERPRETATION</text>
  
  <!-- Row-Column Algorithm -->
  <g transform="translate(30, 55)">
    <rect width="320" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Row-Column Separable Algorithm</text>
    {box(20, 38, 120, 50, "Image f(x, y)", "Size M x N", "#fbbf24")}
    {arrow(140, 63, 175, 63, "#fbbf24")}
    {box(175, 38, 125, 50, "1D-FFT on Rows", "G(x, v)", "#38bdf8")}
    
    <path d="M 237 88 L 237 115 L 80 115 L 80 135" fill="none" stroke="#c084fc" stroke-width="2" marker-end="url(#arrEmerald)"/>
    {box(20, 135, 125, 50, "1D-FFT on Cols", "Applied to G(x, v)", "#c084fc")}
    {arrow(145, 160, 180, 160, "#34d399")}
    {box(180, 135, 120, 50, "2D-DFT F(u, v)", "Total O(MN log MN)", "#34d399", badge="Done")}
  </g>

  <!-- Centered Spectrum Diagram -->
  <g transform="translate(380, 55)">
    <rect width="310" height="205" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="155" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Centered 2D Frequency Spectrum</text>
    <line x1="25" y1="110" x2="285" y2="110" stroke="#475569" stroke-width="1.5"/>
    <line x1="155" y1="35" x2="155" y2="185" stroke="#475569" stroke-width="1.5"/>
    <text x="280" y="105" font-size="11" fill="#38bdf8">u</text>
    <text x="160" y="45" font-size="11" fill="#38bdf8">v</text>
    <!-- DC Center -->
    <circle cx="155" cy="110" r="14" fill="#fbbf24" fill-opacity="0.8"/>
    <text x="155" y="114" font-size="9" fill="#090d16" font-weight="bold" text-anchor="middle">DC</text>
    <text x="155" y="138" font-size="9" fill="#fbbf24" text-anchor="middle">Avg Brightness</text>
    <!-- Edges -->
    <text x="75" y="95" font-size="9" fill="#34d399">Vertical Edges</text>
    <text x="235" y="95" font-size="9" fill="#34d399">Vertical Edges</text>
    <text x="155" y="70" font-size="9" fill="#c084fc" text-anchor="middle">Horizontal Edges</text>
    <text x="155" y="165" font-size="9" fill="#c084fc" text-anchor="middle">Horizontal Edges</text>
  </g>
''')

DIAGRAMS['MID1-Q19'] = svg_doc(720, 280, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">2D LINEAR SHIFT-INVARIANT (LSI) SYSTEMS &amp; CONVOLUTION</text>
  {box(25, 55, 140, 60, "Input Image x[m, n]", "Spatial Domain", "#fbbf24")}
  {arrow(165, 85, 215, 85, "#fbbf24")}
  {box(215, 55, 180, 60, "2D LSI System h[m, n]", "Point Spread Function (PSF)", "#38bdf8", badge="LSI")}
  {arrow(395, 85, 445, 85, "#34d399")}
  {box(445, 55, 250, 60, "Output Image y[m, n]", "y[m, n] = Σ Σ x[k, l] h[m-k, n-l]", "#34d399", badge="Output")}

  <rect x="25" y="135" width="670" height="125" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="160" font-size="12" font-weight="bold" fill="#38bdf8">Transform Domain &amp; Separable Fast Computation:</text>
  {box(45, 175, 280, 65, "Frequency Domain Multiplication", "Y(ω1, ω2) = X(ω1, ω2) · H(ω1, ω2)\\nZero-phase required to prevent edge distortion", "#c084fc")}
  {box(355, 175, 320, 65, "Separable 2D Filter Speedup", "h[m, n] = h1[m] · h2[n]\\nReduces operations from O(K²) to O(2K) per pixel!", "#34d399", badge="Fast")}
''')

DIAGRAMS['MID1-Q20'] = svg_doc(740, 270, f'''
  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">MULTI-DIMENSIONAL IMAGE COMPRESSION FRAMEWORK (JPEG / MPEG)</text>
  {box(15, 55, 95, 60, "1. Color Conv", "RGB -> YCbCr", "#fbbf24")}
  {arrow(110, 85, 130, 85, "#fbbf24")}
  {box(130, 55, 95, 60, "2. 4:2:0 Sub", "Saves 50% data", "#38bdf8")}
  {arrow(225, 85, 245, 85, "#38bdf8")}
  {box(245, 55, 95, 60, "3. 8x8 Blocks", "Local stats", "#38bdf8")}
  {arrow(340, 85, 360, 85, "#38bdf8")}
  {box(360, 55, 95, 60, "4. 2D-DCT", "Energy pack", "#c084fc", badge="DCT")}
  {arrow(455, 85, 475, 85, "#c084fc")}
  {box(475, 55, 95, 60, "5. Quantize", "HVS Matrix Q", "#f43f5e", badge="Lossy")}
  {arrow(570, 85, 590, 85, "#f43f5e")}
  {box(590, 55, 135, 60, "6. Zig-Zag & Encode", "Huffman / CABAC", "#34d399", badge="Compressed")}

  <rect x="15" y="135" width="710" height="115" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="160" font-size="12" font-weight="bold" fill="#34d399">Why 2D-DCT Outperforms 2D-DFT in Video/Image Frameworks:</text>
  <text x="35" y="182" font-size="11" fill="#cbd5e1">✓ Even-Symmetric Reflection: Eliminates artificial boundary discontinuity &amp; blocking artifacts</text>
  <text x="35" y="200" font-size="11" fill="#cbd5e1">✓ Superior Energy Compaction: Packs &gt;90% energy into top-left 3-5 coefficients (near-KLT optimal)</text>
  <text x="35" y="218" font-size="11" fill="#cbd5e1">✓ Real Arithmetic: Only cosine operations (no complex imaginary parts, halving memory &amp; ALU ops)</text>
  <text x="35" y="236" font-size="11" fill="#38bdf8">Universal Industry Standard: Powers JPEG, MPEG-1/2/4, H.264/AVC, and HEVC codecs</text>
''')

DIAGRAMS['MID2-Q01'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">MULTI-DIMENSIONAL SAMPLING: RECTANGULAR VS. HEXAGONAL LATTICES</text>
  
  <!-- Rectangular -->
  <g transform="translate(40, 55)">
    <rect width="290" height="145" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="145" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Rectangular Lattice (CCD/CMOS)</text>
    <!-- Dots -->
    <g fill="#38bdf8">
      <circle cx="50" cy="50" r="4"/><circle cx="110" cy="50" r="4"/><circle cx="170" cy="50" r="4"/><circle cx="230" cy="50" r="4"/>
      <circle cx="50" cy="90" r="4"/><circle cx="110" cy="90" r="4"/><circle cx="170" cy="90" r="4"/><circle cx="230" cy="90" r="4"/>
      <circle cx="50" cy="130" r="4"/><circle cx="110" cy="130" r="4"/><circle cx="170" cy="130" r="4"/><circle cx="230" cy="130" r="4"/>
    </g>
    <text x="145" y="115" font-size="9" fill="#cbd5e1" text-anchor="middle">V = diag(T1, T2) | Orthogonal lines</text>
  </g>

  <!-- Hexagonal -->
  <g transform="translate(390, 55)">
    <rect width="290" height="145" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="145" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Hexagonal Lattice (Optimal Packing)</text>
    <!-- Staggered Dots -->
    <g fill="#34d399">
      <circle cx="50" cy="50" r="4"/><circle cx="110" cy="50" r="4"/><circle cx="170" cy="50" r="4"/><circle cx="230" cy="50" r="4"/>
      <circle cx="80" cy="90" r="4"/><circle cx="140" cy="90" r="4"/><circle cx="200" cy="90" r="4"/>
      <circle cx="50" cy="130" r="4"/><circle cx="110" cy="130" r="4"/><circle cx="170" cy="130" r="4"/><circle cx="230" cy="130" r="4"/>
    </g>
    <text x="145" y="115" font-size="9" fill="#34d399" font-weight="bold" text-anchor="middle">Saves 13.4% samples for circular bandwidth!</text>
  </g>

  <rect x="40" y="215" width="640" height="40" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="360" y="238" font-size="11" fill="#f8fafc" text-anchor="middle">2D Nyquist: fsx ≥ 2·fmax,x and fsy ≥ 2·fmax,y | Aliasing causes Moiré patterns and spatial jaggies</text>
''')

DIAGRAMS['MID2-Q02'] = svg_doc(720, 260, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE TRANSFORMATION PROCESS BLOCK DIAGRAM</text>
  {box(20, 60, 115, 65, "1. 8x8 Partition", "Localized stats", "#fbbf24")}
  {arrow(135, 92, 160, 92, "#fbbf24")}
  {box(160, 60, 115, 65, "2. 2D-DCT", "Decorrelation", "#38bdf8", badge="Energy")}
  {arrow(275, 92, 300, 92, "#38bdf8")}
  {box(300, 60, 115, 65, "3. Quantize", "HVS Matrix", "#f43f5e", badge="Lossy")}
  {arrow(415, 92, 440, 92, "#f43f5e")}
  {box(440, 60, 115, 65, "4. Zig-Zag", "Zero-run order", "#c084fc")}
  {arrow(555, 92, 580, 92, "#c084fc")}
  {box(580, 60, 120, 65, "5. Huffman", "Entropy Coding", "#34d399", badge="Output")}

  <rect x="20" y="145" width="680" height="95" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="170" font-size="11" font-weight="bold" fill="#38bdf8">Justification of Transformation Steps:</text>
  <text x="35" y="190" font-size="11" fill="#cbd5e1">1. Partition: Limits computation and adapts to non-stationary image regions.</text>
  <text x="35" y="208" font-size="11" fill="#cbd5e1">2. 2D-DCT: Packs 90% energy into top-left coefficients; completely decorrelates pixels.</text>
  <text x="35" y="226" font-size="11" fill="#cbd5e1">3. Quantize: Exploits HVS blindness to high spatial frequencies, zeroing out insignificant terms.</text>
''')

DIAGRAMS['MID2-Q03'] = svg_doc(720, 290, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">HUMAN VISUAL SYSTEM (HVS) PROPERTIES &amp; COMPRESSION</text>
  
  <!-- Left: CSF Curve -->
  <g transform="translate(35, 55)">
    <rect width="310" height="210" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="155" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Contrast Sensitivity Function (CSF)</text>
    <!-- Axis -->
    <line x1="30" y1="180" x2="280" y2="180" stroke="#64748b" stroke-width="1.5"/>
    <line x1="30" y1="180" x2="30" y2="40" stroke="#64748b" stroke-width="1.5"/>
    <text x="155" y="198" font-size="9" fill="#cbd5e1" text-anchor="middle">Spatial Frequency (cycles/degree)</text>
    <!-- CSF Bandpass curve -->
    <path d="M 35 150 C 60 70 85 45 110 50 C 145 60 200 130 270 178" fill="none" stroke="#38bdf8" stroke-width="3"/>
    <text x="110" y="40" font-size="9" fill="#fbbf24" font-weight="bold" text-anchor="middle">Peak (3-5 cpd)</text>
    <!-- High Freq Dropoff -->
    <rect x="180" y="90" width="95" height="40" rx="4" fill="#f43f5e" fill-opacity="0.2" stroke="#f43f5e"/>
    <text x="227" y="106" font-size="8" fill="#f43f5e" font-weight="bold" text-anchor="middle">Drop-off to 0:</text>
    <text x="227" y="120" font-size="8" fill="#f43f5e" text-anchor="middle">Heavy Quantization!</text>
  </g>

  <!-- Right: Color Subsampling -->
  <g transform="translate(375, 55)">
    <rect width="310" height="210" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="155" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Luminance vs. Chrominance (4:2:0)</text>
    {box(20, 38, 270, 42, "Rods (120M) vs Cones (6M)", "Eye is far more sensitive to Light than Color", "#fbbf24")}
    {box(20, 90, 270, 48, "YCbCr Color Transform", "Y = Luminance (Keep high bandwidth)\\nCb, Cr = Chroma (Downsample by 2)", "#34d399")}
    {box(20, 148, 270, 48, "4:2:0 Chroma Subsampling", "Discards 50% raw video data with ZERO visible loss!", "#38bdf8", badge="50% Save")}
  </g>
''')

DIAGRAMS['MID2-Q04'] = svg_doc(720, 290, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">DIGITAL VIDEO REPRESENTATION &amp; GROUP OF PICTURES (GOP)</text>
  
  <!-- GOP Timeline -->
  <g transform="translate(30, 55)">
    <rect width="660" height="125" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="330" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Group of Pictures (GOP) Frame Structure</text>
    
    <!-- Frames -->
    {box(30, 40, 75, 55, "I-Frame", "Intra (Key)", "#34d399", badge="Anchor")}
    {box(130, 40, 65, 55, "B1", "Bi-dir", "#c084fc")}
    {box(215, 40, 65, 55, "B2", "Bi-dir", "#c084fc")}
    {box(300, 40, 75, 55, "P-Frame", "Forward", "#fbbf24", badge="Pred")}
    {box(395, 40, 65, 55, "B3", "Bi-dir", "#c084fc")}
    {box(480, 40, 65, 55, "B4", "Bi-dir", "#c084fc")}
    {box(565, 40, 75, 55, "I-Frame", "Next GOP", "#34d399", badge="Anchor")}

    <!-- Prediction arrows -->
    <path d="M 105 55 C 160 10 250 10 300 55" fill="none" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrAmber)"/>
    <text x="200" y="20" font-size="9" fill="#fbbf24">Forward Motion Prediction</text>

    <path d="M 105 75 L 130 75" fill="none" stroke="#c084fc" stroke-width="1.5" marker-end="url(#arrCyan)"/>
    <path d="M 300 75 L 280 75" fill="none" stroke="#c084fc" stroke-width="1.5" marker-end="url(#arrCyan)"/>
  </g>

  <rect x="30" y="195" width="660" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="50" y="218" font-size="11" font-weight="bold" fill="#34d399">Video Redundancy Reduction Mechanics:</text>
  <text x="50" y="238" font-size="11" fill="#cbd5e1">1. Progressive Scan: 1080p60 avoids interlaced comb distortion</text>
  <text x="50" y="254" font-size="11" fill="#cbd5e1">2. YCbCr 4:2:0: Cuts raw uncompressed pixels from 24 bpp to 12 bpp</text>
  <text x="380" y="238" font-size="11" fill="#cbd5e1">3. Motion Vectors: Transmits displacement (dx, dy) instead of pixels</text>
  <text x="380" y="254" font-size="11" fill="#cbd5e1">4. 100:1 Compression: Only small residuals e[x, y] are coded</text>
''')

# --- UNIT 4: MID2-Q05 to MID2-Q12 ---

DIAGRAMS['MID2-Q05'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">IMAGE FORMATION MODELS: GEOMETRIC &amp; PHOTOMETRIC</text>
  
  <!-- Geometric Projection -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Geometric Pinhole Model</text>
    <!-- Rays -->
    <circle cx="50" cy="80" r="6" fill="#fbbf24"/>
    <text x="50" y="65" font-size="9" fill="#fbbf24" font-weight="bold" text-anchor="middle">3D Point P(X,Y,Z)</text>
    <line x1="50" y1="80" x2="280" y2="150" stroke="#38bdf8" stroke-width="1.5"/>
    <!-- Pinhole lens -->
    <line x1="160" y1="45" x2="160" y2="185" stroke="#94a3b8" stroke-width="2"/>
    <text x="160" y="40" font-size="9" fill="#cbd5e1" text-anchor="middle">Lens Center (f)</text>
    <!-- Sensor plane -->
    <line x1="280" y1="65" x2="280" y2="185" stroke="#34d399" stroke-width="3"/>
    <circle cx="280" cy="150" r="4" fill="#34d399"/>
    <text x="280" y="165" font-size="9" fill="#34d399" text-anchor="middle">p(x, y)</text>
    <text x="160" y="178" font-size="11" fill="#cbd5e1" text-anchor="middle">Perspective: x = f·X/Z,  y = f·Y/Z</text>
  </g>

  <!-- Photometric Model -->
  <g transform="translate(375, 55)">
    <rect width="315" height="195" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="157" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">2. Photometric / Radiometric Model</text>
    {box(25, 40, 265, 42, "Illumination L(x, y)", "Light from Sun / Lamp source", "#fbbf24")}
    <text x="157" y="98" font-size="14" fill="#cbd5e1" font-weight="bold" text-anchor="middle">×</text>
    {box(25, 105, 265, 42, "Surface Reflectance R(x, y)", "Material properties (0 ≤ R ≤ 1)", "#38bdf8")}
    <text x="157" y="162" font-size="14" fill="#cbd5e1" font-weight="bold" text-anchor="middle">=</text>
    <text x="157" y="182" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Image Irradiance I(x, y) = L · R</text>
  </g>
''')

DIAGRAMS['MID2-Q06'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">PARAMETRIC 2D MOTION MODELS (2, 6, AND 8 DEGREES OF FREEDOM)</text>
  {box(20, 55, 210, 110, "1. TRANSLATIONAL (2 DOF)", "[x'] = [x] + [dx]\\n[y']   [y]   [dy]\\nRigid shift; standard in Block Matching Algorithms", "#fbbf24", badge="2 DOF")}
  {box(255, 55, 210, 110, "2. AFFINE MODEL (6 DOF)", "[x'] = [a11 a12][x] + [dx]\\n[y']   [a21 a22][y]   [dy]\\nRotation, Scale, Shear, Translation; Parallel lines preserved", "#38bdf8", badge="6 DOF")}
  {box(490, 55, 210, 110, "3. HOMOGRAPHY (8 DOF)", "x' = (h11x + h12y + h13) / D\\ny' = (h21x + h22y + h23) / D\\nFull 3D planar tilt & perspective projection", "#c084fc", badge="8 DOF")}

  <rect x="20" y="180" width="680" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="202" font-size="11" font-weight="bold" fill="#34d399">The 3 Fundamental Real-World Motion Assumptions:</text>
  <text x="35" y="222" font-size="11" fill="#cbd5e1">1. Brightness Constancy: I(x+dx, y+dy, t+dt) = I(x, y, t) (Violated by shadows &amp; lighting changes)</text>
  <text x="35" y="238" font-size="11" fill="#cbd5e1">2. Small Motion: Displacements are small between frames | 3. Spatial Coherence: Neighbor pixels move smoothly</text>
''')

DIAGRAMS['MID2-Q07'] = svg_doc(700, 290, f'''
  <text x="350" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">BLOCK MOTION ESTIMATION NUMERICAL SOLUTION</text>
  
  <!-- Coordinate Plane -->
  <g transform="translate(40, 55)">
    <rect width="320" height="215" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Block Displacement Geometry</text>
    <line x1="40" y1="40" x2="280" y2="40" stroke="#475569" stroke-width="1.5"/>
    <line x1="40" y1="40" x2="40" y2="190" stroke="#475569" stroke-width="1.5"/>
    <text x="270" y="32" font-size="11" fill="#cbd5e1">x (Right)</text>
    <text x="45" y="185" font-size="11" fill="#cbd5e1">y (Down)</text>

    <!-- Block 1 at (20, 25) -> mapped to (80, 80) -->
    <rect x="70" y="70" width="35" height="35" fill="#fbbf24" fill-opacity="0.3" stroke="#fbbf24" stroke-width="2"/>
    <circle cx="87.5" cy="87.5" r="4" fill="#fbbf24"/>
    <text x="70" y="62" font-size="11" fill="#fbbf24" font-weight="bold">Frame 1: (20, 25)</text>

    <!-- Block 2 at (23, 30) -> mapped to (155, 160) -->
    <rect x="137.5" y="142.5" width="35" height="35" fill="#34d399" fill-opacity="0.3" stroke="#34d399" stroke-width="2"/>
    <circle cx="155" cy="160" r="4" fill="#34d399"/>
    <text x="180" y="170" font-size="11" fill="#34d399" font-weight="bold">Frame 2: (23, 30)</text>

    <!-- Motion Vector Arrow -->
    <line x1="87.5" y1="87.5" x2="155" y2="160" stroke="#38bdf8" stroke-width="3" marker-end="url(#arrCyan)"/>
    <text x="135" y="115" font-size="11" font-weight="bold" fill="#38bdf8">d = (3, 5)</text>
  </g>

  <!-- Right: Computations -->
  {box(370, 50, 310, 68, "Task 1: Motion Vector d", "Δx = 23 - 20 = +3 (Right)\\nΔy = 30 - 25 = +5 (Down)\\nd = (3, 5)", "#fbbf24", badge="Vector")}
  {box(370, 122, 310, 64, "Task 2: Magnitude ||d||", "||d|| = √(3² + 5²) = √34\\n||d|| ≈ 5.831 pixels", "#38bdf8", badge="Length")}
  {box(370, 192, 310, 64, "Task 3: Direction θ", "θ = arctan(5/3) = arctan(1.667)\\nθ ≈ 59.04° (Down-Right)", "#34d399", badge="Angle")}
''')

DIAGRAMS['MID2-Q08'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">DIFFERENTIAL MOTION ESTIMATION &amp; THE APERTURE PROBLEM</text>
  
  <!-- Left: Aperture Problem -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#f43f5e" text-anchor="middle">The Aperture Problem</text>
    <!-- Aperture circle -->
    <circle cx="160" cy="110" r="55" fill="#090d16" stroke="#64748b" stroke-width="2"/>
    <!-- Edge line -->
    <line x1="110" y1="70" x2="210" y2="150" stroke="#fbbf24" stroke-width="3"/>
    <!-- Normal flow vector -->
    <line x1="160" y1="110" x2="195" y2="65" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
    <text x="210" y="65" font-size="9" fill="#34d399" font-weight="bold">v_normal (Measured)</text>
    <text x="160" y="185" font-size="9" fill="#cbd5e1" text-anchor="middle">Ix·u + Iy·v + It = 0 (1 Eq, 2 Unknowns!)</text>
  </g>

  <!-- Right: Comparison LK vs HS -->
  {box(370, 55, 320, 90, "Lucas-Kanade Method (Local)", "Assumes constant flow in small 3x3 window\\nSolves overdetermined: v = (Aᵀ A)⁻¹ Aᵀ b\\nReliable only at corners (large eigenvalues)", "#38bdf8", badge="Local")}
  {box(370, 160, 320, 90, "Horn-Schunck Method (Global)", "Adds global spatial smoothness regularizer α²\\nMinimizes energy PDE via Gauss-Seidel iterations\\nProduces dense optical flow across the entire frame", "#34d399", badge="Global")}
''')

DIAGRAMS['MID2-Q09'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">BLOCK MATCHING SEARCH STRATEGIES: FULL SEARCH VS. TSS</text>
  
  <!-- Left: Full Search -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">1. Full Search (Exhaustive)</text>
    <text x="160" y="45" font-size="11" fill="#cbd5e1" text-anchor="middle">Evaluates ALL (2p+1)² points in search area</text>
    <!-- Dense Grid of points -->
    <g fill="#fbbf24" opacity="0.6">
      <circle cx="80" cy="70" r="3"/><circle cx="120" cy="70" r="3"/><circle cx="160" cy="70" r="3"/><circle cx="200" cy="70" r="3"/><circle cx="240" cy="70" r="3"/>
      <circle cx="80" cy="100" r="3"/><circle cx="120" cy="100" r="3"/><circle cx="160" cy="100" r="3"/><circle cx="200" cy="100" r="3"/><circle cx="240" cy="100" r="3"/>
      <circle cx="80" cy="130" r="3"/><circle cx="120" cy="130" r="3"/><circle cx="160" cy="130" r="3"/><circle cx="200" cy="130" r="3"/><circle cx="240" cy="130" r="3"/>
      <circle cx="80" cy="160" r="3"/><circle cx="120" cy="160" r="3"/><circle cx="160" cy="160" r="3"/><circle cx="200" cy="160" r="3"/><circle cx="240" cy="160" r="3"/>
    </g>
    <text x="160" y="185" font-size="11" fill="#fbbf24" font-weight="bold" text-anchor="middle">225 Checks for p = 7 (Optimal, Heavy)</text>
  </g>

  <!-- Right: Three-Step Search -->
  <g transform="translate(370, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">2. Three-Step Search (TSS)</text>
    <text x="160" y="45" font-size="11" fill="#cbd5e1" text-anchor="middle">Step 1 (s=4) -> Step 2 (s=2) -> Step 3 (s=1)</text>
    <!-- Step 1 points -->
    <circle cx="80" cy="75" r="4" fill="#38bdf8"/><circle cx="160" cy="75" r="4" fill="#38bdf8"/><circle cx="240" cy="75" r="4" fill="#38bdf8"/>
    <circle cx="80" cy="125" r="4" fill="#38bdf8"/><circle cx="160" cy="125" r="4" fill="#38bdf8"/><circle cx="240" cy="125" r="4" fill="#38bdf8"/>
    <circle cx="80" cy="175" r="4" fill="#38bdf8"/><circle cx="160" cy="175" r="4" fill="#38bdf8"/><circle cx="240" cy="175" r="4" fill="#38bdf8"/>
    <!-- Best step 1 match converges to center -->
    <circle cx="160" cy="125" r="7" fill="none" stroke="#34d399" stroke-width="2"/>
    <text x="160" y="185" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">Only 25 Checks (9x Speedup!)</text>
  </g>
''')

DIAGRAMS['MID2-Q10'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">NONLINEAR OPTIMIZATION IN MOTION ESTIMATION</text>
  {box(25, 55, 210, 110, "1. Gradient Descent", "p^(k+1) = p^(k) - η·Jᵀ r\\nLinear convergence\\nSafe when far from minimum\\nZigzags in narrow valleys", "#fbbf24", badge="Linear")}
  {box(255, 55, 210, 110, "2. Gauss-Newton", "Δp = -(Jᵀ J)⁻¹ Jᵀ r\\nQuadratic convergence near min\\nCan diverge if Hessian Jᵀ J is singular or ill-conditioned", "#f43f5e", badge="Quadratic")}
  {box(485, 55, 210, 110, "3. Levenberg-Marquardt", "Δp = -(Jᵀ J + λ·I)⁻¹ Jᵀ r\\nAdaptive damping factor λ\\nBlends Gradient Descent + Gauss-Newton optimally", "#34d399", badge="Optimal")}

  <rect x="25" y="180" width="670" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="202" font-size="11" font-weight="bold" fill="#38bdf8">Overcoming Local Minima via Multi-Resolution Gaussian Pyramids:</text>
  <text x="45" y="222" font-size="11" fill="#cbd5e1">Level 2 (Coarse 1/4 Res) ──► Level 1 (Medium 1/2 Res) ──► Level 0 (Full Native Resolution)</text>
  <text x="45" y="238" font-size="11" fill="#cbd5e1">Coarse levels smooth away high-frequency error ripples and shrink large displacements into Taylor range.</text>
''')

DIAGRAMS['MID2-Q11'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">TRANSFORM-DOMAIN MOTION ESTIMATION: PHASE CORRELATION</text>
  {box(25, 55, 130, 55, "Frame f1(x, y)", "Reference Frame", "#fbbf24")}
  {arrow(155, 82, 185, 82, "#fbbf24")}
  {box(185, 55, 100, 55, "2D-FFT", "F1(u, v)", "#38bdf8")}
  
  {box(25, 125, 130, 55, "Frame f2(x, y)", "f1(x - x0, y - y0)", "#fbbf24")}
  {arrow(155, 152, 185, 152, "#fbbf24")}
  {box(185, 125, 100, 55, "2D-FFT", "F2(u, v)", "#38bdf8")}

  {arrow(285, 82, 325, 115, "#38bdf8")}
  {arrow(285, 152, 325, 115, "#38bdf8")}

  {box(325, 75, 190, 80, "Cross-Power Spectrum", "R(u,v) = (F1·F2*) / |F1·F2*|\\n= e^-j2π(ux0 + vy0)", "#c084fc", badge="Normalized")}
  {arrow(515, 115, 550, 115, "#c084fc")}
  {box(550, 75, 145, 80, "Inverse 2D-FFT", "r(x, y) = δ(x-x0, y-y0)\\nSharp Dirac Spike!", "#34d399", badge="Delta Peak")}

  <rect x="25" y="195" width="670" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="360" y="218" font-size="11" fill="#f8fafc" text-anchor="middle">100% Robust to Illumination Changes (Magnitude normalization removes lighting variations)</text>
  <text x="360" y="236" font-size="11" fill="#cbd5e1" text-anchor="middle">Sub-pixel displacement estimation via 2D parabolic peak interpolation around the Dirac delta peak</text>
''')

DIAGRAMS['MID2-Q12'] = svg_doc(740, 280, f'''
  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">3D STRUCTURE FROM MOTION (SfM) PIPELINE</text>
  {box(15, 55, 100, 55, "1. SIFT / ORB", "Feature Points", "#fbbf24")}
  {arrow(115, 82, 135, 82, "#fbbf24")}
  {box(135, 55, 105, 55, "2. RANSAC", "Outlier Filter", "#f43f5e", badge="Consensus")}
  {arrow(240, 82, 260, 82, "#f43f5e")}
  {box(260, 55, 115, 55, "3. 8-Point SVD", "Essential Matrix E", "#38bdf8", badge="E=[t]xR")}
  {arrow(375, 82, 395, 82, "#38bdf8")}
  {box(395, 55, 105, 55, "4. Pose (R, t)", "Camera Motion", "#c084fc")}
  {arrow(500, 82, 520, 82, "#c084fc")}
  {box(520, 55, 95, 55, "5. Triangulate", "3D Points P", "#38bdf8")}
  {arrow(615, 82, 635, 82, "#38bdf8")}
  {box(635, 55, 90, 55, "6. Bundle Adj", "Levenberg-M", "#34d399", badge="Optimized")}

  <rect x="15" y="130" width="710" height="135" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="155" font-size="12" font-weight="bold" fill="#38bdf8">Epipolar Geometry Fundamentals:</text>
  <text x="35" y="178" font-size="11" fill="#cbd5e1">• Essential Matrix: E = [t]× R (5 DOF for calibrated cameras: x2ᵀ E x1 = 0)</text>
  <text x="35" y="198" font-size="11" fill="#cbd5e1">• Fundamental Matrix: F = K2⁻ᵀ E K1⁻¹ (7 DOF for uncalibrated cameras)</text>
  <text x="35" y="218" font-size="11" fill="#cbd5e1">• Bundle Adjustment: Minimizes 2D re-projection error: min Σ ||p_ij - π(K, R, t, P_j)||²</text>
  <text x="35" y="238" font-size="11" fill="#34d399">Recovers both 3D sparse scene point cloud and 3D camera motion trajectory!</text>
''')

# --- UNIT 5: MID2-Q13 to MID2-Q20 ---

DIAGRAMS['MID2-Q13'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">IMAGE SEGMENTATION: REGION-BASED VS. BOUNDARY-BASED</text>
  
  <!-- Region Based -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Region-Based (Similarity)</text>
    <rect x="40" y="45" width="100" height="60" rx="4" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8"/>
    <circle cx="90" cy="75" r="4" fill="#38bdf8"/>
    <text x="90" y="70" font-size="9" fill="#38bdf8" text-anchor="middle">Seed Point</text>
    <text x="90" y="95" font-size="9" fill="#f8fafc" text-anchor="middle">Region Growing</text>

    <rect x="170" y="45" width="100" height="60" rx="4" fill="#fbbf24" fill-opacity="0.2" stroke="#fbbf24"/>
    <line x1="220" y1="45" x2="220" y2="105" stroke="#fbbf24"/>
    <line x1="170" y1="75" x2="270" y2="75" stroke="#fbbf24"/>
    <text x="220" y="125" font-size="9" fill="#fbbf24" text-anchor="middle">Split &amp; Merge (Quadtree)</text>

    <text x="160" y="155" font-size="11" fill="#cbd5e1" text-anchor="middle">Guarantees fully CLOSED regions</text>
    <text x="160" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">Homogeneity predicate P(Ri)=TRUE</text>
  </g>

  <!-- Boundary Based -->
  <g transform="translate(370, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">2. Boundary-Based (Discontinuity)</text>
    <!-- Canny Edge -->
    <path d="M 50 100 Q 110 50 160 100 T 270 90" fill="none" stroke="#34d399" stroke-width="3"/>
    <text x="160" y="60" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">Canny / Sobel ∇I</text>
    <!-- Snake Spline -->
    <ellipse cx="160" cy="115" rx="60" ry="25" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="4 4"/>
    <text x="160" y="118" font-size="9" fill="#c084fc" text-anchor="middle">Active Contour (Snake)</text>

    <text x="160" y="155" font-size="11" fill="#cbd5e1" text-anchor="middle">Detects sharp gradient edges</text>
    <text x="160" y="175" font-size="9" fill="#cbd5e1" text-anchor="middle">Snakes minimize E_int + E_ext energy</text>
  </g>
''')

DIAGRAMS['MID2-Q14'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">CHANGE DETECTION: DIFFERENCING VS. BACKGROUND SUBTRACTION</text>
  
  <!-- Frame Differencing -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">1. Temporal Frame Differencing</text>
    <text x="160" y="45" font-size="11" fill="#cbd5e1" text-anchor="middle">|Frame(t) - Frame(t-1)| &gt; Threshold T</text>
    <!-- Hollow Ghost Person -->
    <ellipse cx="160" cy="85" rx="12" ry="12" fill="none" stroke="#fbbf24" stroke-width="2"/>
    <path d="M 160 97 L 160 145 M 140 115 L 180 115 M 160 145 L 145 175 M 160 145 L 175 175" stroke="#fbbf24" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
    <text x="160" y="170" font-size="11" fill="#f43f5e" font-weight="bold" text-anchor="middle">Hollow \"Ghost\" Holes inside!</text>
    <text x="160" y="185" font-size="9" fill="#cbd5e1" text-anchor="middle">Detects only leading &amp; trailing edges</text>
  </g>

  <!-- Background Subtraction -->
  <g transform="translate(370, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">2. Background Subtraction (MoG)</text>
    <text x="160" y="45" font-size="11" fill="#cbd5e1" text-anchor="middle">|Frame(t) - Background Model B(t)| &gt; T</text>
    <!-- Solid Silhouette -->
    <ellipse cx="160" cy="85" rx="12" ry="12" fill="#34d399"/>
    <path d="M 160 97 L 160 145 M 140 115 L 180 115 M 160 145 L 145 175 M 160 145 L 175 175" stroke="#34d399" stroke-width="5" stroke-linecap="round"/>
    <text x="160" y="170" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">Full Solid Object Mask!</text>
    <text x="160" y="185" font-size="9" fill="#cbd5e1" text-anchor="middle">Adaptive MoG handles moving trees/water</text>
  </g>
''')

DIAGRAMS['MID2-Q15'] = svg_doc(700, 280, f'''
  <text x="350" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">GLOBAL MOTION DETECTION THRESHOLDING NUMERICAL</text>
  
  <!-- Bar Chart -->
  <g transform="translate(40, 55)">
    <rect width="330" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">SAD Measured vs. Threshold T = 100</text>
    <line x1="40" y1="175" x2="290" y2="175" stroke="#64748b" stroke-width="1.5"/>
    
    <!-- Threshold Line -->
    <line x1="35" y1="105" x2="295" y2="105" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4 4"/>
    <text x="290" y="100" font-size="9" fill="#f43f5e" font-weight="bold" text-anchor="end">Threshold T = 100</text>

    <!-- Region A: 120 -->
    <rect x="65" y="91" width="45" height="84" rx="4" fill="#38bdf8"/>
    <text x="87" y="85" font-size="11" fill="#38bdf8" font-weight="bold" text-anchor="middle">120</text>
    <text x="87" y="190" font-size="11" fill="#f8fafc" text-anchor="middle">Region A</text>

    <!-- Region B: 45 -->
    <rect x="145" y="143" width="45" height="32" rx="4" fill="#64748b"/>
    <text x="167" y="138" font-size="11" fill="#cbd5e1" font-weight="bold" text-anchor="middle">45</text>
    <text x="167" y="190" font-size="11" fill="#f8fafc" text-anchor="middle">Region B</text>

    <!-- Region C: 200 -->
    <rect x="225" y="35" width="45" height="140" rx="4" fill="#34d399"/>
    <text x="247" y="30" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">200</text>
    <text x="247" y="190" font-size="11" fill="#f8fafc" text-anchor="middle">Region C</text>
  </g>

  <!-- Right: Decisions -->
  {box(390, 55, 280, 60, "Region A: MOTION DETECTED", "120 > 100 -> Active object displacement", "#38bdf8", badge="Active")}
  {box(390, 125, 280, 60, "Region B: NO MOTION (STATIC)", "45 ≤ 100 -> Sensor noise / background", "#64748b", badge="Static")}
  {box(390, 195, 280, 65, "Region C: DOMINANT REGION", "200 > 100 -> MAXIMUM ACTIVITY!\\nRank 1 Dominant Motion Region", "#34d399", badge="DOMINANT")}
''')

DIAGRAMS['MID2-Q16'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">VISUAL MOTION TRACKING: KALMAN FILTER &amp; MEAN-SHIFT</text>
  
  <!-- Left: Mean-Shift -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">1. Mean-Shift Kernel Mode Seeking</text>
    <!-- Hill contours -->
    <ellipse cx="170" cy="115" rx="90" ry="50" fill="none" stroke="#334155" stroke-width="1.5"/>
    <ellipse cx="170" cy="115" rx="60" ry="35" fill="none" stroke="#475569" stroke-width="1.5"/>
    <ellipse cx="170" cy="115" rx="30" ry="18" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <!-- Mean shift vector -->
    <circle cx="100" cy="140" r="4" fill="#fbbf24"/>
    <text x="100" y="155" font-size="9" fill="#fbbf24">Start y0</text>
    <line x1="100" y1="140" x2="140" y2="125" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrAmber)"/>
    <line x1="140" y1="125" x2="170" y2="115" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
    <circle cx="170" cy="115" r="5" fill="#34d399"/>
    <text x="170" y="105" font-size="9" fill="#34d399" font-weight="bold" text-anchor="middle">Mode Peak (Target)</text>
    <text x="160" y="180" font-size="9" fill="#cbd5e1" text-anchor="middle">Climbs color probability gradient via Bhattacharyya</text>
  </g>

  <!-- Right: Kalman Trajectory -->
  <g transform="translate(370, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">2. Kalman Trajectory Estimation</text>
    <!-- Trajectory curve -->
    <path d="M 40 160 Q 120 120 180 80 T 280 50" fill="none" stroke="#34d399" stroke-width="3"/>
    <circle cx="40" cy="160" r="4" fill="#38bdf8"/>
    <circle cx="110" cy="125" r="4" fill="#38bdf8"/>
    <circle cx="180" cy="80" r="4" fill="#38bdf8"/>
    <circle cx="280" cy="50" r="5" fill="#34d399"/>
    <!-- Measurement noise vs state -->
    <circle cx="195" cy="70" r="3" fill="#f43f5e"/>
    <line x1="180" y1="80" x2="195" y2="70" stroke="#f43f5e" stroke-width="1" stroke-dasharray="2 2"/>
    <text x="215" y="72" font-size="9" fill="#f43f5e">Sensor z</text>

    <text x="160" y="160" font-size="11" fill="#f8fafc" text-anchor="middle">State x = [x, y, vx, vy]ᵀ</text>
    <text x="160" y="180" font-size="9" fill="#cbd5e1" text-anchor="middle">Predict-Update loop filters measurement noise</text>
  </g>
''')

DIAGRAMS['MID2-Q17'] = svg_doc(720, 270, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">IMAGE &amp; VIDEO MATTING: TRIMAP &amp; ALPHA BLENDING</text>
  
  <!-- Left: Trimap -->
  <g transform="translate(40, 55)">
    <rect width="310" height="195" rx="8" fill="#090d16" stroke="#64748b" stroke-width="2"/>
    <text x="155" y="22" font-size="12" font-weight="bold" fill="#f8fafc" text-anchor="middle">User-Defined Trimap</text>
    <!-- Outer Background: Black -->
    <text x="45" y="55" font-size="9" fill="#cbd5e1">Background (α = 0)</text>
    <!-- Unknown Gray Band -->
    <path d="M 60 70 C 90 40 220 40 250 70 C 270 120 270 150 250 180 C 220 200 90 200 60 180 Z" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="155" y="85" font-size="11" fill="#fbbf24" font-weight="bold" text-anchor="middle">UNKNOWN BAND (0 &lt; α &lt; 1)</text>
    <!-- Known Foreground: White -->
    <path d="M 90 100 C 110 85 200 85 220 100 C 230 130 230 145 220 160 C 200 170 110 170 90 160 Z" fill="#f8fafc"/>
    <text x="155" y="130" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">FOREGROUND (α = 1)</text>
  </g>

  <!-- Right: Matting Equation & Laplacian -->
  {box(375, 55, 310, 65, "The Fundamental Matting Equation", "I = α·F + (1 - α)·B\\n3 Known RGB Equations vs 7 Unknowns (Ill-posed!)", "#fbbf24", badge="Equation")}
  {box(375, 125, 310, 60, "Closed-Form Matting (Levin)", "Minimizes αᵀ L α via Matting Laplacian\\nExact global sparse linear solution", "#38bdf8", badge="Laplacian")}
  {box(375, 190, 310, 60, "Video Matting & Coherence", "Optical flow consistency penalty prevents alpha flickering across frames", "#34d399", badge="Video")}
''')

DIAGRAMS['MID2-Q18'] = svg_doc(720, 280, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">PART A: PARTICLE NORMALIZATION &amp; PART B: KALMAN UPDATE</text>

  <!-- Left: Particle Normalization -->
  <g transform="translate(30, 55)">
    <rect width="320" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">PART A: Particle Weight Normalization</text>
    <text x="20" y="45" font-size="11" fill="#cbd5e1">Given W = [0.2, 0.3, 0.1, 0.4] | Sum S = 1.0</text>
    
    <!-- 4 Bars -->
    <rect x="35" y="125" width="45" height="40" rx="3" fill="#38bdf8"/>
    <text x="57" y="148" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">0.20</text>
    <text x="57" y="180" font-size="9" fill="#cbd5e1" text-anchor="middle">P1</text>

    <rect x="100" y="105" width="45" height="60" rx="3" fill="#38bdf8"/>
    <text x="122" y="138" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">0.30</text>
    <text x="122" y="180" font-size="9" fill="#cbd5e1" text-anchor="middle">P2</text>

    <rect x="165" y="145" width="45" height="20" rx="3" fill="#64748b"/>
    <text x="187" y="158" font-size="11" fill="#f8fafc" text-anchor="middle">0.10</text>
    <text x="187" y="180" font-size="9" fill="#cbd5e1" text-anchor="middle">P3</text>

    <rect x="230" y="85" width="45" height="80" rx="3" fill="#34d399"/>
    <text x="252" y="128" font-size="11" fill="#090d16" font-weight="bold" text-anchor="middle">0.40</text>
    <text x="252" y="180" font-size="9" fill="#34d399" font-weight="bold" text-anchor="middle">P4 (Max)</text>

    <text x="160" y="198" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">Most Likely: Particle 4 (Weight = 0.40 / 40%)</text>
  </g>

  <!-- Right: Kalman Filter Update -->
  <g transform="translate(370, 55)">
    <rect width="320" height="205" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">PART B: Kalman Filter State Update</text>
    <text x="20" y="45" font-size="11" fill="#cbd5e1">Prior x^- = 50, Measurement z = 60, Gain K = 0.6</text>
    
    <!-- State Ruler -->
    <line x1="30" y1="100" x2="290" y2="100" stroke="#64748b" stroke-width="2"/>
    <circle cx="50" cy="100" r="5" fill="#fbbf24"/>
    <text x="50" y="88" font-size="11" fill="#fbbf24" font-weight="bold" text-anchor="middle">x^- = 50</text>

    <circle cx="270" cy="100" r="5" fill="#f43f5e"/>
    <text x="270" y="88" font-size="11" fill="#f43f5e" font-weight="bold" text-anchor="middle">z = 60</text>

    <circle cx="182" cy="100" r="7" fill="#34d399"/>
    <text x="182" y="85" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">Updated x = 56</text>

    <!-- Arrow from 50 to 56 -->
    <path d="M 55 115 L 175 115" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#arrEmerald)"/>
    <text x="115" y="130" font-size="11" fill="#34d399" font-weight="bold" text-anchor="middle">+6 Correction (K·Innovation)</text>

    <text x="160" y="160" font-size="11" fill="#f8fafc" text-anchor="middle">x = 50 + 0.6(60 - 50) = 50 + 6 = 56</text>
    <text x="160" y="185" font-size="9" fill="#cbd5e1" text-anchor="middle">60% trust in sensor measurement, 40% in model</text>
  </g>
''')

DIAGRAMS['MID2-Q19'] = svg_doc(740, 270, f'''
  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">REAL-TIME VIDEO SEGMENTATION &amp; TRACKING FRAMEWORK</text>
  {box(15, 55, 95, 60, "1. Video In", "30 fps Camera", "#fbbf24")}
  {arrow(110, 85, 130, 85, "#fbbf24")}
  {box(130, 55, 95, 60, "2. MoG2 Detect", "Background Sub", "#38bdf8")}
  {arrow(225, 85, 245, 85, "#38bdf8")}
  {box(245, 55, 95, 60, "3. Morphology", "Open / Close", "#38bdf8")}
  {arrow(340, 85, 360, 85, "#38bdf8")}
  {box(360, 55, 95, 60, "4. Features", "Centroid, Hist", "#c084fc")}
  {arrow(455, 85, 475, 85, "#c084fc")}
  {box(475, 55, 95, 60, "5. Hungarian", "Data Assoc O(N³)", "#f43f5e", badge="Match")}
  {arrow(570, 85, 590, 85, "#f43f5e")}
  {box(590, 55, 135, 60, "6. Kalman Track", "Predict & Smooth", "#34d399", badge="Tracks")}

  <rect x="15" y="135" width="710" height="115" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="160" font-size="12" font-weight="bold" fill="#34d399">Track Life-Cycle Management &amp; Real-Time Optimizations:</text>
  <text x="35" y="182" font-size="11" fill="#cbd5e1">• Track Birth: Consistent detection across 3 consecutive frames initiates a unique Track ID</text>
  <text x="35" y="198" font-size="11" fill="#cbd5e1">• Occlusion Handling: Kalman filter velocity coasts trajectory through pillars/trees for up to 30 frames</text>
  <text x="35" y="214" font-size="11" fill="#cbd5e1">• Track Termination: Missing for &gt;30 frames deletes track and releases memory</text>
  <text x="35" y="234" font-size="11" fill="#38bdf8">Parallel GPU multi-threading delivers &gt;30 fps throughput for self-driving and security surveillance</text>
''')

DIAGRAMS['MID2-Q20'] = svg_doc(720, 280, f'''
  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">PERFORMANCE EVALUATION MODEL: IOU, PRECISION, RECALL, F1</text>
  
  <!-- Left: Venn Overlap -->
  <g transform="translate(35, 55)">
    <rect width="310" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="155" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Spatial Overlap (IoU / Jaccard)</text>
    <!-- Ground Truth Circle -->
    <circle cx="120" cy="115" r="50" fill="#fbbf24" fill-opacity="0.3" stroke="#fbbf24" stroke-width="2"/>
    <text x="90" y="115" font-size="11" fill="#fbbf24" font-weight="bold">FN</text>
    <!-- Prediction Circle -->
    <circle cx="180" cy="115" r="50" fill="#38bdf8" fill-opacity="0.3" stroke="#38bdf8" stroke-width="2"/>
    <text x="210" y="115" font-size="11" fill="#38bdf8" font-weight="bold">FP</text>
    <!-- Overlap TP -->
    <text x="150" y="118" font-size="12" fill="#34d399" font-weight="bold" text-anchor="middle">TP</text>

    <text x="155" y="180" font-size="11" fill="#f8fafc" text-anchor="middle">IoU = Area(A ∩ B) / Area(A ∪ B)</text>
    <text x="155" y="195" font-size="11" fill="#34d399" text-anchor="middle">= TP / (TP + FP + FN)</text>
  </g>

  <!-- Right: Metrics Table -->
  <g transform="translate(375, 55)">
    <rect width="310" height="205" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="155" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Worked Numerical Evaluation Example</text>
    <text x="20" y="45" font-size="11" fill="#cbd5e1">Given: TP=800, FP=100, FN=200, TN=98900</text>
    
    <text x="20" y="75" font-size="11" fill="#cbd5e1">1. IoU = 800 / (800+100+200) = <tspan fill="#34d399" font-weight="bold">72.7%</tspan></text>
    <text x="20" y="105" font-size="11" fill="#cbd5e1">2. Precision = TP/(TP+FP) = 800/900 = <tspan fill="#38bdf8" font-weight="bold">88.9%</tspan></text>
    <text x="20" y="135" font-size="11" fill="#cbd5e1">3. Recall = TP/(TP+FN) = 800/1000 = <tspan fill="#fbbf24" font-weight="bold">80.0%</tspan></text>
    <text x="20" y="165" font-size="11" fill="#cbd5e1">4. F1-Score = 2PR/(P+R) = <tspan fill="#34d399" font-weight="bold">84.2%</tspan></text>

    <text x="20" y="195" font-size="11" fill="#c084fc">CLEAR MOT: MOTA = 1 - (FN+FP+IDSW)/GT</text>
  </g>
''')

def generate_all_diagrams():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    diag_dir = os.path.join(base_dir, 'diagrams')
    os.makedirs(diag_dir, exist_ok=True)
    for qid, svg in DIAGRAMS.items():
        filepath = os.path.join(diag_dir, f'{qid}.svg')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg)
    print(f"Generated {len(DIAGRAMS)} SVG diagrams in {diag_dir}")

    # Generate diagrams_data.py
    data_lines = [
        "# -*- coding: utf-8 -*-",
        '"""',
        "Inlined SVG diagrams dictionary for all 40 SVP questions.",
        '"""',
        "",
        "DIAGRAMS_SVG = {"
    ]
    for qid, svg in DIAGRAMS.items():
        data_lines.append(f'    "{qid}": """{svg}""",')
    data_lines.append("}\n")

    out_file = os.path.join(base_dir, 'diagrams_data.py')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(data_lines))
    print(f"Generated {out_file} successfully!")

if __name__ == "__main__":
    generate_all_diagrams()
