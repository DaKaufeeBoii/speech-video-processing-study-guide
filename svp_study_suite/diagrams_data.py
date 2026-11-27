# -*- coding: utf-8 -*-
"""
Inlined SVG diagrams dictionary for all 40 SVP questions.
"""

DIAGRAMS_SVG = {
    "MID1-Q01": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 320" width="100%" height="auto" class="flowchart-svg" style="max-width: 740px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="740" height="320" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="370" y="32" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">SPEECH PRODUCTION: SOURCE-FILTER MECHANISM (FANT\'S ACOUSTIC MODEL)</text>
  <rect x="20" y="55" width="220" height="235" rx="10" fill="#1e293b" fill-opacity="0.4" stroke="#fbbf24" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="130" y="78" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">EXCITATION SOURCE E(z)</text>
    <g filter="url(#shadow)">
    <rect x="40" y="95" width="180" height="50" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="130.0" y="113" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Lungs &amp; Trachea</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="130.0" y="129">Subglottal Air Pressure</tspan></text>
    
  </g>
    <line x1="130" y1="145" x2="130" y2="185" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  <text x="130.0" y="159.0" font-size="11" fill="#fbbf24" font-weight="700" text-anchor="middle">Airflow</text>
    <g filter="url(#shadow)">
    <rect x="40" y="185" width="180" height="85" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="130.0" y="203" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. Glottis / Vocal Cords</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="130.0" y="219">Voiced: Pulses (Pitch F0)</tspan><tspan x="130.0" y="233">Unvoiced: Turbulent Noise</tspan></text>
    
  </g>

    <line x1="220" y1="225" x2="275" y2="225" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  <text x="247.5" y="219.0" font-size="11" fill="#38bdf8" font-weight="700" text-anchor="middle">Raw Acoustic e(t)</text>

  <rect x="275" y="55" width="260" height="235" rx="10" fill="#1e293b" fill-opacity="0.4" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="405" y="78" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">VOCAL TRACT FILTER H(z)</text>
    <g filter="url(#shadow)">
    <rect x="295" y="95" width="220" height="50" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="405.0" y="113" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Pharynx (Throat Cavity)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="405.0" y="129">Cross-section ~17.5 cm</tspan></text>
    
  </g>
    <g filter="url(#shadow)">
    <rect x="295" y="155" width="220" height="55" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="405.0" y="173" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Oral &amp; Nasal Cavities</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="405.0" y="189">Resonances = Formants (F1, F2, F3)</tspan></text>
    
  </g>
    <g filter="url(#shadow)">
    <rect x="295" y="220" width="220" height="50" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="405.0" y="238" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Articulators (Tongue/Lips)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="405.0" y="254">Shaping Vowels &amp; Consonants</tspan></text>
    
  </g>

    <line x1="515" y1="225" x2="570" y2="225" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  <text x="542.5" y="219.0" font-size="11" fill="#34d399" font-weight="700" text-anchor="middle">Acoustic Wave</text>

  <rect x="570" y="55" width="150" height="235" rx="10" fill="#1e293b" fill-opacity="0.4" stroke="#34d399" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="645" y="78" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">OUTPUT s(t)</text>
    <g filter="url(#shadow)">
    <rect x="580" y="115" width="130" height="60" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="645.0" y="133" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Lip Radiation</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="645.0" y="149">R(z) ≈ 1 - z^-1</tspan></text>
    
  </g>
    <g filter="url(#shadow)">
    <rect x="580" y="195" width="130" height="75" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.5"/>
    <text x="645.0" y="213" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Radiated Speech</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="645.0" y="229">S(z) = E·H·R</tspan><tspan x="645.0" y="243">Audio Waveform</tspan></text>
    
  </g>

</svg>""",
    "MID1-Q02": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="32" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">DISCRETE-TIME SPEECH SAMPLING &amp; NYQUIST RECONSTRUCTION</text>
    <g filter="url(#shadow)">
    <rect x="20" y="70" width="140" height="65" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="90.0" y="88" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Analog Speech s(t)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="90.0" y="104">Continuous Acoustic Wave</tspan></text>
    
  </g>
    <line x1="160" y1="102" x2="195" y2="102" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="195" y="70" width="150" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="270.0" y="88" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Anti-Aliasing Filter</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="270.0" y="104">Low-Pass LPF (fc = fs/2)</tspan></text>
    <rect x="270" y="61" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="305" y="74" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Bandlimit</text>
  </g>
    <line x1="345" y1="102" x2="380" y2="102" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="380" y="70" width="145" height="65" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="452.5" y="88" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">ADC / Sampler</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="452.5" y="104">Ts = 1/fs (8k / 16kHz)</tspan></text>
    <rect x="450" y="61" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="485" y="74" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Nyquist</text>
  </g>
    <line x1="525" y1="102" x2="560" y2="102" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="560" y="70" width="140" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="630.0" y="88" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Discrete Speech s[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="630.0" y="104">s[n] = s(n·Ts)</tspan></text>
    <rect x="625" y="61" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="660" y="74" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Digital</text>
  </g>

  <path d="M 630 135 L 630 185 L 450 185" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#arrEmerald)"/>

    <g filter="url(#shadow)">
    <rect x="300" y="160" width="150" height="65" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="375.0" y="178" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">D/A Converter</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="375.0" y="194">Discrete Impulse Train</tspan></text>
    
  </g>
    <line x1="300" y1="192" x2="250" y2="192" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="100" y="160" width="150" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="175.0" y="178" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Sinc Reconstruction</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="175.0" y="194">Ideal Sinc LPF Filter</tspan></text>
    <rect x="175" y="151" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="210" y="164" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Recover</text>
  </g>
    <line x1="100" y1="192" x2="40" y2="192" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
  <text x="25" y="196" font-size="12" font-weight="bold" fill="#34d399">s(t)</text>
  <rect x="40" y="240" width="640" height="28" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="360" y="258" font-size="11" fill="#f8fafc" text-anchor="middle">Nyquist Condition: fs ≥ 2·fmax | Undersampling causes overlapping spectral replicas (Aliasing)</text>

</svg>""",
    "MID1-Q03": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 310" width="100%" height="auto" class="flowchart-svg" style="max-width: 700px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="700" height="310" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="310" y="60" width="370" height="75" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="495.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">System Transfer Function H(z)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="495.0" y="94">H(z) = [z(z - 0.5)] / [z² - 0.9z + 0.2] = z / (z - 0.4)</tspan></text>
    <rect x="605" y="51" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="64" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Filter</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="310" y="145" width="370" height="70" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="495.0" y="163" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Poles &amp; Zeros Extraction</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="495.0" y="179">Zeros (Numerator=0): z1 = 0, z2 = 0.5</tspan><tspan x="495.0" y="193">Poles (Denominator=0): p1 = 0.5, p2 = 0.4</tspan></text>
    
  </g>
    <g filter="url(#shadow)">
    <rect x="310" y="225" width="370" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="495.0" y="243" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">BIBO Stability Verdict: UNCONDITIONALLY STABLE</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="495.0" y="259">All poles strictly INSIDE unit circle (|p1|=0.5 &lt; 1, |p2|=0.4 &lt; 1)</tspan></text>
    <rect x="605" y="216" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="229" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Stable</text>
  </g>

</svg>""",
    "MID1-Q04": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">FAST FOURIER TRANSFORM (FFT) IN SPEECH RECOGNITION</text>
    <g filter="url(#shadow)">
    <rect x="20" y="65" width="140" height="60" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="90.0" y="83" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Speech Frame x[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="90.0" y="99">20 - 30 ms duration</tspan></text>
    
  </g>
    <line x1="160" y1="95" x2="195" y2="95" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="195" y="65" width="150" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="270.0" y="83" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Hamming Window</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="270.0" y="99">Prevents spectral leakage</tspan></text>
    <rect x="270" y="56" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="305" y="69" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Window</text>
  </g>
    <line x1="345" y1="95" x2="380" y2="95" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="380" y="65" width="150" height="60" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="455.0" y="83" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">N-Point FFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="455.0" y="99">O(N log N) Fast Engine</tspan></text>
    <rect x="455" y="56" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="490" y="69" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Cooley-Tukey</text>
  </g>
    <line x1="530" y1="95" x2="570" y2="75" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
    <line x1="530" y1="95" x2="570" y2="120" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="570" y="45" width="135" height="50" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="637.5" y="63" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Magnitude |X[k]|</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="637.5" y="79">Formant Peak Spectrum</tspan></text>
    
  </g>
    <g filter="url(#shadow)">
    <rect x="570" y="105" width="135" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="637.5" y="123" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Phase Spectrum</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="637.5" y="139">∠X[k] Dispersion</tspan></text>
    
  </g>

  <rect x="20" y="175" width="685" height="85" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="198" font-size="12" font-weight="bold" fill="#fbbf24">6 Core Properties for Speech Recognition:</text>
  <text x="35" y="218" font-size="11" fill="#cbd5e1">1. Linearity: Preserves speech+noise superposition</text>
  <text x="35" y="235" font-size="11" fill="#cbd5e1">2. Conjugate Symmetry: Real speech -> X[N-k]=X*[k] (Save 50% compute)</text>
  <text x="35" y="252" font-size="11" fill="#cbd5e1">3. Time-Shift: Magnitude invariant to boundary offset</text>
  <text x="380" y="218" font-size="11" fill="#cbd5e1">4. Resolution: Δf = fs / N (Trade-off time vs frequency)</text>
  <text x="380" y="235" font-size="11" fill="#cbd5e1">5. Parseval's Theorem: Total energy preserved for VAD</text>
  <text x="380" y="252" font-size="11" fill="#cbd5e1">6. Periodicity: Rectangular window causes spectral leakage</text>

</svg>""",
    "MID1-Q05": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 300" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="300" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">CONVOLUTION OPERATIONS &amp; REAL-TIME OVERLAP-ADD (OLA)</text>
    <g filter="url(#shadow)">
    <rect x="25" y="60" width="150" height="60" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="100.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Glottal Excitation e[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="100.0" y="94">Pulse train / Noise source</tspan></text>
    
  </g>
    <line x1="175" y1="90" x2="230" y2="90" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  <text x="202.5" y="84.0" font-size="11" fill="#fbbf24" font-weight="700" text-anchor="middle">Input</text>
    <g filter="url(#shadow)">
    <rect x="230" y="60" width="200" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="330.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Vocal Tract Filter h[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="330.0" y="94">Resonances (Formants v[n] * r[n])</tspan></text>
    <rect x="355" y="51" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="390" y="64" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">LTI System</text>
  </g>
    <line x1="430" y1="90" x2="485" y2="90" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  <text x="457.5" y="84.0" font-size="11" fill="#34d399" font-weight="700" text-anchor="middle">Convolution</text>
    <g filter="url(#shadow)">
    <rect x="485" y="60" width="200" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="585.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Radiated Speech s[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="585.0" y="94">s[n] = e[n] * h[n] = Σ e[k]h[n-k]</tspan></text>
    <rect x="610" y="51" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="645" y="64" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Output</text>
  </g>

  <rect x="25" y="140" width="665" height="145" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="162" font-size="12" font-weight="bold" fill="#38bdf8">Real-Time Streaming Speech Convolution (Overlap-Add Method):</text>
    <g filter="url(#shadow)">
    <rect x="45" y="175" width="150" height="50" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="120.0" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Split Stream</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="120.0" y="209">Blocks of length L</tspan></text>
    
  </g>
    <line x1="195" y1="200" x2="230" y2="200" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="230" y="175" width="150" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="305.0" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. Fast FFT &amp; Mult</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="305.0" y="209">Y_i[k] = X_i[k] · H[k]</tspan></text>
    
  </g>
    <line x1="380" y1="200" x2="415" y2="200" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="415" y="175" width="140" height="50" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="485.0" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. Inverse IFFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="485.0" y="209">Length L + M - 1</tspan></text>
    
  </g>
    <line x1="555" y1="200" x2="580" y2="200" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
    <g filter="url(#shadow)">
    <rect x="580" y="175" width="95" height="50" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="627.5" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. Overlap &amp; Add</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="627.5" y="209">Stream Assembly</tspan></text>
    
  </g>
  <text x="45" y="265" font-size="11" fill="#cbd5e1">Avoids time-aliasing by zero-padding to N ≥ L + M - 1 | Eliminates infinite convolution latency</text>

</svg>""",
    "MID1-Q06": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="290" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID1-Q07": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 310" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="310" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID1-Q08": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 310" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="310" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">LINEAR PREDICTIVE CODING (LPC) ANALYSIS &amp; SYNTHESIS</text>
  
  <!-- LPC Analysis -->
  <g transform="translate(25, 55)">
    <rect width="670" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="335" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">LPC ENCODER (ANALYSIS): All-Pole Autoregressive Prediction</text>
      <g filter="url(#shadow)">
    <rect x="40" y="38" width="120" height="50" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="100.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Speech s[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="100.0" y="72">Past p samples</tspan></text>
    
  </g>
      <line x1="160" y1="63" x2="215" y2="63" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
      <g filter="url(#shadow)">
    <rect x="215" y="38" width="180" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="305.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">LPC Predictor ak</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="305.0" y="72">Yule-Walker / Levinson</tspan></text>
    <rect x="320" y="29" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="355" y="42" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">O(p²)</text>
  </g>
      <line x1="395" y1="63" x2="450" y2="63" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  <text x="422.5" y="57.0" font-size="11" fill="#38bdf8" font-weight="700" text-anchor="middle">s^[n]</text>
      <g filter="url(#shadow)">
    <rect x="450" y="38" width="90" height="50" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="495.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Difference</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="495.0" y="72">e[n]=s - s^</tspan></text>
    
  </g>
      <line x1="540" y1="63" x2="580" y2="63" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="580" y="38" width="100" height="50" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="630.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Residual e[n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="630.0" y="72">Pitch / Gain G</tspan></text>
    
  </g>
  </g>

  <!-- LPC Synthesis -->
  <g transform="translate(25, 175)">
    <rect width="670" height="115" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="335" y="22" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">LPC DECODER (SYNTHESIS): Vocal Tract Resynthesis</text>
      <g filter="url(#shadow)">
    <rect x="40" y="38" width="150" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="115.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Excitation Source</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="115.0" y="72">Pitch pulses (Voiced)</tspan><tspan x="115.0" y="86">Noise (Unvoiced)</tspan></text>
    
  </g>
      <line x1="190" y1="65" x2="250" y2="65" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  <text x="220.0" y="59.0" font-size="11" fill="#fbbf24" font-weight="700" text-anchor="middle">Gain G</text>
      <g filter="url(#shadow)">
    <rect x="250" y="38" width="230" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="365.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">All-Pole Synthesis Filter</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="365.0" y="72">H(z) = G / (1 - Σ ak z^-k)</tspan></text>
    <rect x="405" y="29" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="440" y="42" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Resonator</text>
  </g>
      <line x1="480" y1="65" x2="540" y2="65" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="540" y="38" width="140" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="610.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Reconstructed Speech</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="610.0" y="72">Natural Audio 2.4 kbps</tspan></text>
    <rect x="605" y="29" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="42" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">LPC-10</text>
  </g>
  </g>

</svg>""",
    "MID1-Q09": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 740px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="740" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">SPEECH FEATURE EXTRACTION PIPELINE (MFCC)</text>
    <g filter="url(#shadow)">
    <rect x="15" y="55" width="90" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="60.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Pre-emp</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="60.0" y="89">1 - 0.97z^-1</tspan></text>
    
  </g>
    <line x1="105" y1="82" x2="120" y2="82" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="120" y="55" width="90" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="165.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. Framing</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="165.0" y="89">25ms, 10ms</tspan></text>
    
  </g>
    <line x1="210" y1="82" x2="225" y2="82" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="225" y="55" width="95" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="272.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. Window</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="272.5" y="89">Hamming</tspan></text>
    
  </g>
    <line x1="320" y1="82" x2="335" y2="82" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="335" y="55" width="85" height="55" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="377.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. FFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="377.5" y="89">|X[k]| Mag</tspan></text>
    
  </g>
    <line x1="420" y1="82" x2="435" y2="82" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="435" y="55" width="95" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="482.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">5. Mel Filter</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="482.5" y="89">26-40 Banks</tspan></text>
    
  </g>
    <line x1="530" y1="82" x2="545" y2="82" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
    <g filter="url(#shadow)">
    <rect x="545" y="55" width="85" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="587.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">6. Log E</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="587.5" y="89">Loudness</tspan></text>
    
  </g>
    <line x1="630" y1="82" x2="645" y2="82" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="645" y="55" width="80" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="685.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">7. DCT-II</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="685.0" y="89">13 MFCC</tspan></text>
    <rect x="650" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="685" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Static</text>
  </g>

    <line x1="685" y1="110" x2="685" y2="145" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
  <rect x="15" y="145" width="710" height="105" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="170" font-size="12" font-weight="bold" fill="#34d399">Dynamic Derivative Augmentation (Final 39-D Vector):</text>
    <g filter="url(#shadow)">
    <rect x="35" y="185" width="205" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="137.5" y="203" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">13 Static MFCCs (c0 - c12)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="137.5" y="219">Instantaneous Vocal Posture</tspan></text>
    
  </g>
  <text x="255" y="215" font-size="18" fill="#cbd5e1" font-weight="bold">+</text>
    <g filter="url(#shadow)">
    <rect x="275" y="185" width="200" height="50" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="375.0" y="203" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">13 Delta Features (Δc)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="375.0" y="219">Spectral Velocity / Transitions</tspan></text>
    
  </g>
  <text x="490" y="215" font-size="18" fill="#cbd5e1" font-weight="bold">+</text>
    <g filter="url(#shadow)">
    <rect x="510" y="185" width="200" height="50" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="610.0" y="203" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">13 Delta-Delta (Δ²c)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="610.0" y="219">Articulatory Acceleration</tspan></text>
    
  </g>

</svg>""",
    "MID1-Q10": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="30" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">STATIC VS. DYNAMIC SPEECH FEATURES (39-D ASR VECTOR)</text>
  
  <!-- Temporal Frame Evolution -->
  <g transform="translate(40, 60)">
      <g filter="url(#shadow)">
    <rect x="0" y="0" width="100" height="50" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="50.0" y="18" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame t-2</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="50.0" y="34">c(t-2)</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="130" y="0" width="100" height="50" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="180.0" y="18" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame t-1</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="180.0" y="34">c(t-1)</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="260" y="0" width="120" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="320.0" y="18" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame t</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="320.0" y="34">c(t) [CURRENT]</tspan></text>
    <rect x="305" y="-9" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="340" y="4" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Target</text>
  </g>
      <g filter="url(#shadow)">
    <rect x="410" y="0" width="100" height="50" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="460.0" y="18" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame t+1</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="460.0" y="34">c(t+1)</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="540" y="0" width="100" height="50" rx="8" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <text x="590.0" y="18" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame t+2</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="590.0" y="34">c(t+2)</tspan></text>
    
  </g>
  </g>

  <!-- Hierarchy -->
  <path d="M 360 115 L 360 145 M 360 145 L 140 145 L 140 170 M 360 145 L 360 170 M 360 145 L 580 145 L 580 170" fill="none" stroke="#94a3b8" stroke-width="2"/>

    <g filter="url(#shadow)">
    <rect x="30" y="170" width="220" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="140.0" y="188" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. STATIC FEATURES (13-D)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="140.0" y="204">c0 to c12 MFCCs</tspan><tspan x="140.0" y="218">Represents instantaneous vocal tract posture at frame t</tspan></text>
    <rect x="175" y="161" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="210" y="174" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Static</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="270" y="170" width="200" height="85" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="370.0" y="188" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. DELTA (13-D)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="370.0" y="204">Δc(t) = Velocity</tspan><tspan x="370.0" y="218">Rate of spectral change across neighboring frames</tspan></text>
    <rect x="395" y="161" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="430" y="174" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Delta</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="490" y="170" width="200" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="590.0" y="188" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. DELTA-DELTA (13-D)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="590.0" y="204">Δ²c(t) = Acceleration</tspan><tspan x="590.0" y="218">Second-order derivative of articulatory transitions</tspan></text>
    <rect x="615" y="161" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="650" y="174" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Delta-Delta</text>
  </g>

</svg>""",
    "MID1-Q11": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="290" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID1-Q12": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">LPCC VS. MFCC ARCHITECTURAL COMPARISON</text>
  
  <!-- LPCC Path -->
  <g transform="translate(30, 50)">
    <rect width="660" height="90" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="330" y="20" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">LPCC: Acoustic All-Pole Tube Model (Noise-Sensitive, No Zeros)</text>
      <g filter="url(#shadow)">
    <rect x="30" y="32" width="100" height="45" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="80.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Raw Speech</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="80.0" y="66">Linear scale</tspan></text>
    
  </g>
      <line x1="130" y1="54" x2="170" y2="54" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
      <g filter="url(#shadow)">
    <rect x="170" y="32" width="130" height="45" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="235.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">LPC Analysis</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="235.0" y="66">Yule-Walker / Levinson</tspan></text>
    
  </g>
      <line x1="300" y1="54" x2="340" y2="54" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
      <g filter="url(#shadow)">
    <rect x="340" y="32" width="120" height="45" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="400.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Predictor ak</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="400.0" y="66">All-pole filter</tspan></text>
    
  </g>
      <line x1="460" y1="54" x2="500" y2="54" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
      <g filter="url(#shadow)">
    <rect x="500" y="32" width="130" height="45" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="565.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">LPCCs</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="565.0" y="66">Recursive Cepstrum</tspan></text>
    <rect x="555" y="23" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="590" y="36" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Low Bitrate</text>
  </g>
  </g>

  <!-- MFCC Path -->
  <g transform="translate(30, 155)">
    <rect width="660" height="95" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="330" y="20" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">MFCC: Human Auditory Cochlea Model (Highly Robust to Noise, ASR Standard)</text>
      <g filter="url(#shadow)">
    <rect x="30" y="32" width="85" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="72.5" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Raw Speech</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="72.5" y="66">Pre-emphasized</tspan></text>
    
  </g>
      <line x1="115" y1="54" x2="140" y2="54" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="140" y="32" width="80" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="180.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">FFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="180.0" y="66">|X[k]| Mag</tspan></text>
    
  </g>
      <line x1="220" y1="54" x2="245" y2="54" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="245" y="32" width="120" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="305.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Mel Filterbank</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="305.0" y="66">Critical bands</tspan></text>
    
  </g>
      <line x1="365" y1="54" x2="390" y2="54" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="390" y="32" width="80" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="430.0" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Log E</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="430.0" y="66">Loudness</tspan></text>
    
  </g>
      <line x1="470" y1="54" x2="495" y2="54" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="495" y="32" width="135" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="562.5" y="50" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">13 MFCCs</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="562.5" y="66">DCT-II Decorrelation</tspan></text>
    <rect x="555" y="23" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="590" y="36" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">ASR Standard</text>
  </g>
  </g>

</svg>""",
    "MID1-Q13": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" width="100%" height="auto" class="flowchart-svg" style="max-width: 700px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="700" height="300" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="330" y="55" width="335" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="497.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Euclidean Distance d_E</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="497.5" y="89">d = √Σ(xi - yi)² | Assumes equal variance &amp; no correlation</tspan></text>
    <rect x="590" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="625" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Fast O(D)</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="330" y="135" width="335" height="65" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="497.5" y="153" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. Mahalanobis Distance d_M</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="497.5" y="169">d = √[(x - y)ᵀ Σ⁻¹ (x - y)] | Accounts for feature covariance</tspan></text>
    <rect x="590" y="126" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="625" y="139" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Scale-Inv</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="330" y="215" width="335" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="497.5" y="233" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. Dynamic Time Warping (DTW)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="497.5" y="249">D(i,j) = d + min{D(i-1,j), D(i,j-1), D(i-1,j-1)}</tspan></text>
    <rect x="590" y="206" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="625" y="219" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Temporal</text>
  </g>

</svg>""",
    "MID1-Q14": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="350" y="55" width="335" height="45" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="517.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Initial Global Centroid (K=1)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="517.5" y="89">Average of all training speech vectors</tspan></text>
    
  </g>
    <line x1="517" y1="100" x2="517" y2="115" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="350" y="115" width="335" height="45" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="517.5" y="133" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. Centroid Splitting (K ──► 2K)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="517.5" y="149">y+ = y(1 + ε), y- = y(1 - ε)</tspan></text>
    <rect x="610" y="106" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="645" y="119" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Split</text>
  </g>
    <line x1="517" y1="160" x2="517" y2="175" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="350" y="175" width="335" height="45" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="517.5" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. K-Means Nearest Assignment</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="517.5" y="209">Classify vectors into Voronoi cells R_i</tspan></text>
    
  </g>
    <line x1="517" y1="220" x2="517" y2="235" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="350" y="235" width="335" height="45" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="517.5" y="253" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. Iterate until Distortion Converges</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="517.5" y="269">Generates optimal codebook (K=64-256)</tspan></text>
    <rect x="610" y="226" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="645" y="239" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Done</text>
  </g>

</svg>""",
    "MID1-Q15": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="290" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="360" y="55" width="320" height="90" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="520.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">E-STEP (Expectation)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="520.0" y="89">Compute posterior responsibilities:</tspan><tspan x="520.0" y="103">γm(xt) = wm·N(xt; μm, Σm) / Σ wj·N(xt; μj, Σj)</tspan></text>
    <rect x="605" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">E-Step</text>
  </g>
  <path d="M 520 145 L 520 175" fill="none" stroke="#34d399" stroke-width="2" marker-end="url(#arrEmerald)"/>
  <path d="M 360 215 L 340 215 L 340 100 L 360 100" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="325" y="155" font-size="9" fill="#c084fc" transform="rotate(-90 325 155)">Iterate until ΔL &lt; ε</text>
    <g filter="url(#shadow)">
    <rect x="360" y="175" width="320" height="95" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="520.0" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">M-STEP (Maximization)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="520.0" y="209">Re-estimate mixture parameters:</tspan><tspan x="520.0" y="223">wm = (1/T) Σ γm(xt)</tspan><tspan x="520.0" y="237">μm = Σ γm(xt)·xt / Σ γm(xt)</tspan><tspan x="520.0" y="251">Σm = Σ γm(xt)·(xt - μm)(xt - μm)ᵀ / Σ γm</tspan></text>
    <rect x="605" y="166" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="179" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">M-Step</text>
  </g>

</svg>""",
    "MID1-Q16": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 740px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="740" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID1-Q17": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">MULTI-DIMENSIONAL SIGNALS TAXONOMY &amp; PROPERTIES</text>
    <g filter="url(#shadow)">
    <rect x="25" y="60" width="150" height="85" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="100.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1D Signal: Speech</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="100.0" y="94">s(t) = Amplitude vs Time</tspan><tspan x="100.0" y="108">Strictly Causal</tspan><tspan x="100.0" y="122">Bandwidth: ~64 kbps</tspan></text>
    
  </g>
    <line x1="175" y1="102" x2="205" y2="102" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="205" y="60" width="150" height="85" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="280.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2D Signal: Image</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="280.0" y="94">f(x, y) = 2D Spatial Grid</tspan><tspan x="280.0" y="108">Non-causal in space</tspan><tspan x="280.0" y="122">Bandwidth: ~5 MB/img</tspan></text>
    
  </g>
    <line x1="355" y1="102" x2="385" y2="102" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="385" y="60" width="150" height="85" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="460.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3D Signal: Video</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="460.0" y="94">f(x, y, t) = Space + Time</tspan><tspan x="460.0" y="108">Temporal correlation</tspan><tspan x="460.0" y="122">Bandwidth: ~3.0 Gbps</tspan></text>
    
  </g>
    <line x1="535" y1="102" x2="565" y2="102" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="565" y="60" width="130" height="85" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="630.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3D/4D Medical</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="630.0" y="94">f(x, y, z, t)</tspan><tspan x="630.0" y="108">Volumetric CT/MRI</tspan></text>
    
  </g>

  <rect x="25" y="165" width="670" height="85" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="190" font-size="12" font-weight="bold" fill="#38bdf8">Key Multi-Dimensional Signal Characteristics:</text>
  <text x="45" y="210" font-size="11" fill="#cbd5e1">1. High Spatial Correlation: Adjacent pixels have &gt;90% similar intensity</text>
  <text x="45" y="228" font-size="11" fill="#cbd5e1">2. Non-Causal Space: Processing accesses left, right, top, and bottom simultaneously</text>
  <text x="380" y="210" font-size="11" fill="#cbd5e1">3. Separability: f(x, y) = f1(x) · f2(y) (Saves O(N²) ops)</text>
  <text x="380" y="228" font-size="11" fill="#cbd5e1">4. Massive Data Rates: Demands transform-domain compression</text>

</svg>""",
    "MID1-Q18": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">2D-DFT ROW-COLUMN COMPUTATION &amp; SPECTRAL INTERPRETATION</text>
  
  <!-- Row-Column Algorithm -->
  <g transform="translate(30, 55)">
    <rect width="320" height="205" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Row-Column Separable Algorithm</text>
      <g filter="url(#shadow)">
    <rect x="20" y="38" width="120" height="50" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="80.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Image f(x, y)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="80.0" y="72">Size M x N</tspan></text>
    
  </g>
      <line x1="140" y1="63" x2="175" y2="63" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
      <g filter="url(#shadow)">
    <rect x="175" y="38" width="125" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="237.5" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1D-FFT on Rows</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="237.5" y="72">G(x, v)</tspan></text>
    
  </g>
    
    <path d="M 237 88 L 237 115 L 80 115 L 80 135" fill="none" stroke="#c084fc" stroke-width="2" marker-end="url(#arrEmerald)"/>
      <g filter="url(#shadow)">
    <rect x="20" y="135" width="125" height="50" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="82.5" y="153" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1D-FFT on Cols</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="82.5" y="169">Applied to G(x, v)</tspan></text>
    
  </g>
      <line x1="145" y1="160" x2="180" y2="160" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
      <g filter="url(#shadow)">
    <rect x="180" y="135" width="120" height="50" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="240.0" y="153" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2D-DFT F(u, v)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="240.0" y="169">Total O(MN log MN)</tspan></text>
    <rect x="225" y="126" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="260" y="139" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Done</text>
  </g>
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

</svg>""",
    "MID1-Q19": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">2D LINEAR SHIFT-INVARIANT (LSI) SYSTEMS &amp; CONVOLUTION</text>
    <g filter="url(#shadow)">
    <rect x="25" y="55" width="140" height="60" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="95.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Input Image x[m, n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="95.0" y="89">Spatial Domain</tspan></text>
    
  </g>
    <line x1="165" y1="85" x2="215" y2="85" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="215" y="55" width="180" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="305.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2D LSI System h[m, n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="305.0" y="89">Point Spread Function (PSF)</tspan></text>
    <rect x="320" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="355" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">LSI</text>
  </g>
    <line x1="395" y1="85" x2="445" y2="85" stroke="#34d399" stroke-width="2.5" marker-end="url(#arrEmerald)"/>
  
    <g filter="url(#shadow)">
    <rect x="445" y="55" width="250" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="570.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Output Image y[m, n]</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="570.0" y="89">y[m, n] = Σ Σ x[k, l] h[m-k, n-l]</tspan></text>
    <rect x="620" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="655" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Output</text>
  </g>

  <rect x="25" y="135" width="670" height="125" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="160" font-size="12" font-weight="bold" fill="#38bdf8">Transform Domain &amp; Separable Fast Computation:</text>
    <g filter="url(#shadow)">
    <rect x="45" y="175" width="280" height="65" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="185.0" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frequency Domain Multiplication</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="185.0" y="209">Y(ω1, ω2) = X(ω1, ω2) · H(ω1, ω2)</tspan><tspan x="185.0" y="223">Zero-phase required to prevent edge distortion</tspan></text>
    
  </g>
    <g filter="url(#shadow)">
    <rect x="355" y="175" width="320" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="515.0" y="193" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Separable 2D Filter Speedup</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="515.0" y="209">h[m, n] = h1[m] · h2[n]</tspan><tspan x="515.0" y="223">Reduces operations from O(K²) to O(2K) per pixel!</tspan></text>
    <rect x="600" y="166" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="635" y="179" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Fast</text>
  </g>

</svg>""",
    "MID1-Q20": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 740px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="740" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">MULTI-DIMENSIONAL IMAGE COMPRESSION FRAMEWORK (JPEG / MPEG)</text>
    <g filter="url(#shadow)">
    <rect x="15" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="62.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Color Conv</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="62.5" y="89">RGB -&gt; YCbCr</tspan></text>
    
  </g>
    <line x1="110" y1="85" x2="130" y2="85" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="130" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="177.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. 4:2:0 Sub</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="177.5" y="89">Saves 50% data</tspan></text>
    
  </g>
    <line x1="225" y1="85" x2="245" y2="85" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="245" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="292.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. 8x8 Blocks</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="292.5" y="89">Local stats</tspan></text>
    
  </g>
    <line x1="340" y1="85" x2="360" y2="85" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="360" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="407.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. 2D-DCT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="407.5" y="89">Energy pack</tspan></text>
    <rect x="380" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="415" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">DCT</text>
  </g>
    <line x1="455" y1="85" x2="475" y2="85" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="475" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="522.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">5. Quantize</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="522.5" y="89">HVS Matrix Q</tspan></text>
    <rect x="495" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="530" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Lossy</text>
  </g>
    <line x1="570" y1="85" x2="590" y2="85" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="590" y="55" width="135" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="657.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">6. Zig-Zag &amp; Encode</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="657.5" y="89">Huffman / CABAC</tspan></text>
    <rect x="650" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="685" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Compressed</text>
  </g>

  <rect x="15" y="135" width="710" height="115" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="160" font-size="12" font-weight="bold" fill="#34d399">Why 2D-DCT Outperforms 2D-DFT in Video/Image Frameworks:</text>
  <text x="35" y="182" font-size="11" fill="#cbd5e1">✓ Even-Symmetric Reflection: Eliminates artificial boundary discontinuity &amp; blocking artifacts</text>
  <text x="35" y="200" font-size="11" fill="#cbd5e1">✓ Superior Energy Compaction: Packs &gt;90% energy into top-left 3-5 coefficients (near-KLT optimal)</text>
  <text x="35" y="218" font-size="11" fill="#cbd5e1">✓ Real Arithmetic: Only cosine operations (no complex imaginary parts, halving memory &amp; ALU ops)</text>
  <text x="35" y="236" font-size="11" fill="#38bdf8">Universal Industry Standard: Powers JPEG, MPEG-1/2/4, H.264/AVC, and HEVC codecs</text>

</svg>""",
    "MID2-Q01": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID2-Q02": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 260" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="260" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">THE TRANSFORMATION PROCESS BLOCK DIAGRAM</text>
    <g filter="url(#shadow)">
    <rect x="20" y="60" width="115" height="65" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="77.5" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. 8x8 Partition</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="77.5" y="94">Localized stats</tspan></text>
    
  </g>
    <line x1="135" y1="92" x2="160" y2="92" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="160" y="60" width="115" height="65" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="217.5" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. 2D-DCT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="217.5" y="94">Decorrelation</tspan></text>
    <rect x="200" y="51" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="235" y="64" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Energy</text>
  </g>
    <line x1="275" y1="92" x2="300" y2="92" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="300" y="60" width="115" height="65" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="357.5" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. Quantize</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="357.5" y="94">HVS Matrix</tspan></text>
    <rect x="340" y="51" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="375" y="64" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Lossy</text>
  </g>
    <line x1="415" y1="92" x2="440" y2="92" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="440" y="60" width="115" height="65" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="497.5" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. Zig-Zag</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="497.5" y="94">Zero-run order</tspan></text>
    
  </g>
    <line x1="555" y1="92" x2="580" y2="92" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="580" y="60" width="120" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="640.0" y="78" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">5. Huffman</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="640.0" y="94">Entropy Coding</tspan></text>
    <rect x="625" y="51" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="660" y="64" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Output</text>
  </g>

  <rect x="20" y="145" width="680" height="95" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="170" font-size="11" font-weight="bold" fill="#38bdf8">Justification of Transformation Steps:</text>
  <text x="35" y="190" font-size="11" fill="#cbd5e1">1. Partition: Limits computation and adapts to non-stationary image regions.</text>
  <text x="35" y="208" font-size="11" fill="#cbd5e1">2. 2D-DCT: Packs 90% energy into top-left coefficients; completely decorrelates pixels.</text>
  <text x="35" y="226" font-size="11" fill="#cbd5e1">3. Quantize: Exploits HVS blindness to high spatial frequencies, zeroing out insignificant terms.</text>

</svg>""",
    "MID2-Q03": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="290" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
      <g filter="url(#shadow)">
    <rect x="20" y="38" width="270" height="42" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="155.0" y="56" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Rods (120M) vs Cones (6M)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="155.0" y="72">Eye is far more sensitive to Light than Color</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="20" y="90" width="270" height="48" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="155.0" y="108" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">YCbCr Color Transform</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="155.0" y="124">Y = Luminance (Keep high bandwidth)</tspan><tspan x="155.0" y="138">Cb, Cr = Chroma (Downsample by 2)</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="20" y="148" width="270" height="48" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="155.0" y="166" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4:2:0 Chroma Subsampling</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="155.0" y="182">Discards 50% raw video data with ZERO visible loss!</tspan></text>
    <rect x="215" y="139" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="250" y="152" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">50% Save</text>
  </g>
  </g>

</svg>""",
    "MID2-Q04": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 290" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="290" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">DIGITAL VIDEO REPRESENTATION &amp; GROUP OF PICTURES (GOP)</text>
  
  <!-- GOP Timeline -->
  <g transform="translate(30, 55)">
    <rect width="660" height="125" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="330" y="22" font-size="12" font-weight="bold" fill="#38bdf8" text-anchor="middle">Group of Pictures (GOP) Frame Structure</text>
    
    <!-- Frames -->
      <g filter="url(#shadow)">
    <rect x="30" y="40" width="75" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="67.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">I-Frame</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="67.5" y="74">Intra (Key)</tspan></text>
    <rect x="30" y="31" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="65" y="44" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Anchor</text>
  </g>
      <g filter="url(#shadow)">
    <rect x="130" y="40" width="65" height="55" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="162.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">B1</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="162.5" y="74">Bi-dir</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="215" y="40" width="65" height="55" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="247.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">B2</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="247.5" y="74">Bi-dir</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="300" y="40" width="75" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="337.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">P-Frame</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="337.5" y="74">Forward</tspan></text>
    <rect x="300" y="31" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="335" y="44" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Pred</text>
  </g>
      <g filter="url(#shadow)">
    <rect x="395" y="40" width="65" height="55" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="427.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">B3</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="427.5" y="74">Bi-dir</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="480" y="40" width="65" height="55" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="512.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">B4</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="512.5" y="74">Bi-dir</tspan></text>
    
  </g>
      <g filter="url(#shadow)">
    <rect x="565" y="40" width="75" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="602.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">I-Frame</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="602.5" y="74">Next GOP</tspan></text>
    <rect x="565" y="31" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="600" y="44" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Anchor</text>
  </g>

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

</svg>""",
    "MID2-Q05": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
      <g filter="url(#shadow)">
    <rect x="25" y="40" width="265" height="42" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="157.5" y="58" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Illumination L(x, y)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="157.5" y="74">Light from Sun / Lamp source</tspan></text>
    
  </g>
    <text x="157" y="98" font-size="14" fill="#cbd5e1" font-weight="bold" text-anchor="middle">×</text>
      <g filter="url(#shadow)">
    <rect x="25" y="105" width="265" height="42" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="157.5" y="123" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Surface Reflectance R(x, y)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="157.5" y="139">Material properties (0 ≤ R ≤ 1)</tspan></text>
    
  </g>
    <text x="157" y="162" font-size="14" fill="#cbd5e1" font-weight="bold" text-anchor="middle">=</text>
    <text x="157" y="182" font-size="12" font-weight="bold" fill="#34d399" text-anchor="middle">Image Irradiance I(x, y) = L · R</text>
  </g>

</svg>""",
    "MID2-Q06": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">PARAMETRIC 2D MOTION MODELS (2, 6, AND 8 DEGREES OF FREEDOM)</text>
    <g filter="url(#shadow)">
    <rect x="20" y="55" width="210" height="110" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="125.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. TRANSLATIONAL (2 DOF)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="125.0" y="89">[x&#x27;] = [x] + [dx]</tspan><tspan x="125.0" y="103">[y&#x27;]   [y]   [dy]</tspan><tspan x="125.0" y="117">Rigid shift; standard in Block Matching Algorithms</tspan></text>
    <rect x="155" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="190" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">2 DOF</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="255" y="55" width="210" height="110" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="360.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. AFFINE MODEL (6 DOF)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="360.0" y="89">[x&#x27;] = [a11 a12][x] + [dx]</tspan><tspan x="360.0" y="103">[y&#x27;]   [a21 a22][y]   [dy]</tspan><tspan x="360.0" y="117">Rotation, Scale, Shear, Translation; Parallel lines preserved</tspan></text>
    <rect x="390" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="425" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">6 DOF</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="490" y="55" width="210" height="110" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="595.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. HOMOGRAPHY (8 DOF)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="595.0" y="89">x&#x27; = (h11x + h12y + h13) / D</tspan><tspan x="595.0" y="103">y&#x27; = (h21x + h22y + h23) / D</tspan><tspan x="595.0" y="117">Full 3D planar tilt &amp; perspective projection</tspan></text>
    <rect x="625" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="660" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">8 DOF</text>
  </g>

  <rect x="20" y="180" width="680" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="202" font-size="11" font-weight="bold" fill="#34d399">The 3 Fundamental Real-World Motion Assumptions:</text>
  <text x="35" y="222" font-size="11" fill="#cbd5e1">1. Brightness Constancy: I(x+dx, y+dy, t+dt) = I(x, y, t) (Violated by shadows &amp; lighting changes)</text>
  <text x="35" y="238" font-size="11" fill="#cbd5e1">2. Small Motion: Displacements are small between frames | 3. Spatial Coherence: Neighbor pixels move smoothly</text>

</svg>""",
    "MID2-Q07": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 290" width="100%" height="auto" class="flowchart-svg" style="max-width: 700px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="700" height="290" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="370" y="50" width="310" height="68" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="525.0" y="68" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Task 1: Motion Vector d</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="525.0" y="84">Δx = 23 - 20 = +3 (Right)</tspan><tspan x="525.0" y="98">Δy = 30 - 25 = +5 (Down)</tspan><tspan x="525.0" y="112">d = (3, 5)</tspan></text>
    <rect x="605" y="41" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="54" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Vector</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="370" y="122" width="310" height="64" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="525.0" y="140" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Task 2: Magnitude ||d||</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="525.0" y="156">||d|| = √(3² + 5²) = √34</tspan><tspan x="525.0" y="170">||d|| ≈ 5.831 pixels</tspan></text>
    <rect x="605" y="113" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="126" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Length</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="370" y="192" width="310" height="64" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="525.0" y="210" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Task 3: Direction θ</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="525.0" y="226">θ = arctan(5/3) = arctan(1.667)</tspan><tspan x="525.0" y="240">θ ≈ 59.04° (Down-Right)</tspan></text>
    <rect x="605" y="183" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="640" y="196" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Angle</text>
  </g>

</svg>""",
    "MID2-Q08": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="370" y="55" width="320" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="530.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Lucas-Kanade Method (Local)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="89">Assumes constant flow in small 3x3 window</tspan><tspan x="530.0" y="103">Solves overdetermined: v = (Aᵀ A)⁻¹ Aᵀ b</tspan><tspan x="530.0" y="117">Reliable only at corners (large eigenvalues)</tspan></text>
    <rect x="615" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="650" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Local</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="370" y="160" width="320" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="530.0" y="178" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Horn-Schunck Method (Global)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="194">Adds global spatial smoothness regularizer α²</tspan><tspan x="530.0" y="208">Minimizes energy PDE via Gauss-Seidel iterations</tspan><tspan x="530.0" y="222">Produces dense optical flow across the entire frame</tspan></text>
    <rect x="615" y="151" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="650" y="164" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Global</text>
  </g>

</svg>""",
    "MID2-Q09": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID2-Q10": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">NONLINEAR OPTIMIZATION IN MOTION ESTIMATION</text>
    <g filter="url(#shadow)">
    <rect x="25" y="55" width="210" height="110" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="130.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Gradient Descent</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="130.0" y="89">p^(k+1) = p^(k) - η·Jᵀ r</tspan><tspan x="130.0" y="103">Linear convergence</tspan><tspan x="130.0" y="117">Safe when far from minimum</tspan><tspan x="130.0" y="131">Zigzags in narrow valleys</tspan></text>
    <rect x="160" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="195" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Linear</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="255" y="55" width="210" height="110" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="360.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. Gauss-Newton</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="360.0" y="89">Δp = -(Jᵀ J)⁻¹ Jᵀ r</tspan><tspan x="360.0" y="103">Quadratic convergence near min</tspan><tspan x="360.0" y="117">Can diverge if Hessian Jᵀ J is singular or ill-conditioned</tspan></text>
    <rect x="390" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="425" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Quadratic</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="485" y="55" width="210" height="110" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="590.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. Levenberg-Marquardt</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="590.0" y="89">Δp = -(Jᵀ J + λ·I)⁻¹ Jᵀ r</tspan><tspan x="590.0" y="103">Adaptive damping factor λ</tspan><tspan x="590.0" y="117">Blends Gradient Descent + Gauss-Newton optimally</tspan></text>
    <rect x="620" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="655" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Optimal</text>
  </g>

  <rect x="25" y="180" width="670" height="75" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="45" y="202" font-size="11" font-weight="bold" fill="#38bdf8">Overcoming Local Minima via Multi-Resolution Gaussian Pyramids:</text>
  <text x="45" y="222" font-size="11" fill="#cbd5e1">Level 2 (Coarse 1/4 Res) ──► Level 1 (Medium 1/2 Res) ──► Level 0 (Full Native Resolution)</text>
  <text x="45" y="238" font-size="11" fill="#cbd5e1">Coarse levels smooth away high-frequency error ripples and shrink large displacements into Taylor range.</text>

</svg>""",
    "MID2-Q11": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">TRANSFORM-DOMAIN MOTION ESTIMATION: PHASE CORRELATION</text>
    <g filter="url(#shadow)">
    <rect x="25" y="55" width="130" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="90.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame f1(x, y)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="90.0" y="89">Reference Frame</tspan></text>
    
  </g>
    <line x1="155" y1="82" x2="185" y2="82" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="185" y="55" width="100" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="235.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2D-FFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="235.0" y="89">F1(u, v)</tspan></text>
    
  </g>
  
    <g filter="url(#shadow)">
    <rect x="25" y="125" width="130" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="90.0" y="143" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Frame f2(x, y)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="90.0" y="159">f1(x - x0, y - y0)</tspan></text>
    
  </g>
    <line x1="155" y1="152" x2="185" y2="152" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="185" y="125" width="100" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="235.0" y="143" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2D-FFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="235.0" y="159">F2(u, v)</tspan></text>
    
  </g>

    <line x1="285" y1="82" x2="325" y2="115" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <line x1="285" y1="152" x2="325" y2="115" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  

    <g filter="url(#shadow)">
    <rect x="325" y="75" width="190" height="80" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="420.0" y="93" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Cross-Power Spectrum</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="420.0" y="109">R(u,v) = (F1·F2*) / |F1·F2*|</tspan><tspan x="420.0" y="123">= e^-j2π(ux0 + vy0)</tspan></text>
    <rect x="440" y="66" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="475" y="79" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Normalized</text>
  </g>
    <line x1="515" y1="115" x2="550" y2="115" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="550" y="75" width="145" height="80" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="622.5" y="93" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Inverse 2D-FFT</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="622.5" y="109">r(x, y) = δ(x-x0, y-y0)</tspan><tspan x="622.5" y="123">Sharp Dirac Spike!</tspan></text>
    <rect x="620" y="66" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="655" y="79" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Delta Peak</text>
  </g>

  <rect x="25" y="195" width="670" height="60" rx="6" fill="#1e293b" stroke="#334155"/>
  <text x="360" y="218" font-size="11" fill="#f8fafc" text-anchor="middle">100% Robust to Illumination Changes (Magnitude normalization removes lighting variations)</text>
  <text x="360" y="236" font-size="11" fill="#cbd5e1" text-anchor="middle">Sub-pixel displacement estimation via 2D parabolic peak interpolation around the Dirac delta peak</text>

</svg>""",
    "MID2-Q12": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 740px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="740" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">3D STRUCTURE FROM MOTION (SfM) PIPELINE</text>
    <g filter="url(#shadow)">
    <rect x="15" y="55" width="100" height="55" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="65.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. SIFT / ORB</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="65.0" y="89">Feature Points</tspan></text>
    
  </g>
    <line x1="115" y1="82" x2="135" y2="82" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="135" y="55" width="105" height="55" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="187.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. RANSAC</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="187.5" y="89">Outlier Filter</tspan></text>
    <rect x="165" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="200" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Consensus</text>
  </g>
    <line x1="240" y1="82" x2="260" y2="82" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="260" y="55" width="115" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="317.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. 8-Point SVD</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="317.5" y="89">Essential Matrix E</tspan></text>
    <rect x="300" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="335" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">E=[t]xR</text>
  </g>
    <line x1="375" y1="82" x2="395" y2="82" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="395" y="55" width="105" height="55" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="447.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. Pose (R, t)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="447.5" y="89">Camera Motion</tspan></text>
    
  </g>
    <line x1="500" y1="82" x2="520" y2="82" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="520" y="55" width="95" height="55" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="567.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">5. Triangulate</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="567.5" y="89">3D Points P</tspan></text>
    
  </g>
    <line x1="615" y1="82" x2="635" y2="82" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="635" y="55" width="90" height="55" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="680.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">6. Bundle Adj</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="680.0" y="89">Levenberg-M</tspan></text>
    <rect x="650" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="685" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Optimized</text>
  </g>

  <rect x="15" y="130" width="710" height="135" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="155" font-size="12" font-weight="bold" fill="#38bdf8">Epipolar Geometry Fundamentals:</text>
  <text x="35" y="178" font-size="11" fill="#cbd5e1">• Essential Matrix: E = [t]× R (5 DOF for calibrated cameras: x2ᵀ E x1 = 0)</text>
  <text x="35" y="198" font-size="11" fill="#cbd5e1">• Fundamental Matrix: F = K2⁻ᵀ E K1⁻¹ (7 DOF for uncalibrated cameras)</text>
  <text x="35" y="218" font-size="11" fill="#cbd5e1">• Bundle Adjustment: Minimizes 2D re-projection error: min Σ ||p_ij - π(K, R, t, P_j)||²</text>
  <text x="35" y="238" font-size="11" fill="#34d399">Recovers both 3D sparse scene point cloud and 3D camera motion trajectory!</text>

</svg>""",
    "MID2-Q13": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID2-Q14": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="360" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">CHANGE DETECTION: DIFFERENCING VS. BACKGROUND SUBTRACTION</text>
  
  <!-- Frame Differencing -->
  <g transform="translate(30, 55)">
    <rect width="320" height="195" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="160" y="22" font-size="12" font-weight="bold" fill="#fbbf24" text-anchor="middle">1. Temporal Frame Differencing</text>
    <text x="160" y="45" font-size="11" fill="#cbd5e1" text-anchor="middle">|Frame(t) - Frame(t-1)| &gt; Threshold T</text>
    <!-- Hollow Ghost Person -->
    <ellipse cx="160" cy="85" rx="12" ry="12" fill="none" stroke="#fbbf24" stroke-width="2"/>
    <path d="M 160 97 L 160 145 M 140 115 L 180 115 M 160 145 L 145 175 M 160 145 L 175 175" stroke="#fbbf24" stroke-width="2" fill="none" stroke-dasharray="3 3"/>
    <text x="160" y="170" font-size="11" fill="#f43f5e" font-weight="bold" text-anchor="middle">Hollow "Ghost" Holes inside!</text>
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

</svg>""",
    "MID2-Q15": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 700px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="700" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="390" y="55" width="280" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="530.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Region A: MOTION DETECTED</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="89">120 &gt; 100 -&gt; Active object displacement</tspan></text>
    <rect x="595" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="630" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Active</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="390" y="125" width="280" height="60" rx="8" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
    <text x="530.0" y="143" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Region B: NO MOTION (STATIC)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="159">45 ≤ 100 -&gt; Sensor noise / background</tspan></text>
    <rect x="595" y="116" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="630" y="129" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Static</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="390" y="195" width="280" height="65" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="530.0" y="213" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Region C: DOMINANT REGION</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="229">200 &gt; 100 -&gt; MAXIMUM ACTIVITY!</tspan><tspan x="530.0" y="243">Rank 1 Dominant Motion Region</tspan></text>
    <rect x="595" y="186" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="630" y="199" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">DOMINANT</text>
  </g>

</svg>""",
    "MID2-Q16": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID2-Q17": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <g filter="url(#shadow)">
    <rect x="375" y="55" width="310" height="65" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="530.0" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">The Fundamental Matting Equation</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="89">I = α·F + (1 - α)·B</tspan><tspan x="530.0" y="103">3 Known RGB Equations vs 7 Unknowns (Ill-posed!)</tspan></text>
    <rect x="610" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="645" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Equation</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="375" y="125" width="310" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="530.0" y="143" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Closed-Form Matting (Levin)</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="159">Minimizes αᵀ L α via Matting Laplacian</tspan><tspan x="530.0" y="173">Exact global sparse linear solution</tspan></text>
    <rect x="610" y="116" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="645" y="129" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Laplacian</text>
  </g>
    <g filter="url(#shadow)">
    <rect x="375" y="190" width="310" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="530.0" y="208" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">Video Matting &amp; Coherence</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="530.0" y="224">Optical flow consistency penalty prevents alpha flickering across frames</tspan></text>
    <rect x="610" y="181" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="645" y="194" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Video</text>
  </g>

</svg>""",
    "MID2-Q18": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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

</svg>""",
    "MID2-Q19": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 270" width="100%" height="auto" class="flowchart-svg" style="max-width: 740px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="740" height="270" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <text x="370" y="28" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">REAL-TIME VIDEO SEGMENTATION &amp; TRACKING FRAMEWORK</text>
    <g filter="url(#shadow)">
    <rect x="15" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
    <text x="62.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">1. Video In</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="62.5" y="89">30 fps Camera</tspan></text>
    
  </g>
    <line x1="110" y1="85" x2="130" y2="85" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="130" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="177.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">2. MoG2 Detect</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="177.5" y="89">Background Sub</tspan></text>
    
  </g>
    <line x1="225" y1="85" x2="245" y2="85" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="245" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="292.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">3. Morphology</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="292.5" y="89">Open / Close</tspan></text>
    
  </g>
    <line x1="340" y1="85" x2="360" y2="85" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrCyan)"/>
  
    <g filter="url(#shadow)">
    <rect x="360" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="1.5"/>
    <text x="407.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">4. Features</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="407.5" y="89">Centroid, Hist</tspan></text>
    
  </g>
    <line x1="455" y1="85" x2="475" y2="85" stroke="#c084fc" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="475" y="55" width="95" height="60" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="522.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">5. Hungarian</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="522.5" y="89">Data Assoc O(N³)</tspan></text>
    <rect x="495" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="530" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Match</text>
  </g>
    <line x1="570" y1="85" x2="590" y2="85" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrAmber)"/>
  
    <g filter="url(#shadow)">
    <rect x="590" y="55" width="135" height="60" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
    <text x="657.5" y="73" font-size="12.5" font-weight="700" fill="#f8fafc" text-anchor="middle">6. Kalman Track</text>
    <text font-size="11" fill="#cbd5e1" text-anchor="middle"><tspan x="657.5" y="89">Predict &amp; Smooth</tspan></text>
    <rect x="650" y="46" width="70" height="18" rx="9" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1"/><text x="685" y="59" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">Tracks</text>
  </g>

  <rect x="15" y="135" width="710" height="115" rx="8" fill="#1e293b" stroke="#334155"/>
  <text x="35" y="160" font-size="12" font-weight="bold" fill="#34d399">Track Life-Cycle Management &amp; Real-Time Optimizations:</text>
  <text x="35" y="182" font-size="11" fill="#cbd5e1">• Track Birth: Consistent detection across 3 consecutive frames initiates a unique Track ID</text>
  <text x="35" y="198" font-size="11" fill="#cbd5e1">• Occlusion Handling: Kalman filter velocity coasts trajectory through pillars/trees for up to 30 frames</text>
  <text x="35" y="214" font-size="11" fill="#cbd5e1">• Track Termination: Missing for &gt;30 frames deletes track and releases memory</text>
  <text x="35" y="234" font-size="11" fill="#38bdf8">Parallel GPU multi-threading delivers &gt;30 fps throughput for self-driving and security surveillance</text>

</svg>""",
    "MID2-Q20": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 280" width="100%" height="auto" class="flowchart-svg" style="max-width: 720px; width: 100%; height: auto; display: block; margin: 0 auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <rect width="100%" height="100%" fill="#0b1120" rx="8" stroke="#1e293b" stroke-width="1"/>
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
  <rect width="720" height="280" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

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
    <text x="20" y="45" font-size="11" fill="#cbd5e1">Given: TP=80, FP=20, FN=20, TN=80</text>
    
    <text x="20" y="75" font-size="11" fill="#cbd5e1">1. IoU = 80 / (80+20+20) = 80/120 = <tspan fill="#34d399" font-weight="bold">66.7%</tspan></text>
    <text x="20" y="105" font-size="11" fill="#cbd5e1">2. Precision = TP/(TP+FP) = 80/100 = <tspan fill="#38bdf8" font-weight="bold">80.0%</tspan></text>
    <text x="20" y="135" font-size="11" fill="#cbd5e1">3. Recall = TP/(TP+FN) = 80/100 = <tspan fill="#fbbf24" font-weight="bold">80.0%</tspan></text>
    <text x="20" y="165" font-size="11" fill="#cbd5e1">4. F1-Score = 2PR/(P+R) = <tspan fill="#34d399" font-weight="bold">80.0%</tspan></text>

    <text x="20" y="195" font-size="11" fill="#c084fc">Meets &gt;50% threshold for successful detection</text>
  </g>

</svg>""",
}
