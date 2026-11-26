# -*- coding: utf-8 -*-
"""
Unit 1: Fundamentals of Speech Production, Discrete-Time Speech Signals & Analysis
Questions: Mid-I Q1 to Q8
Academic Year: 2026-27 | Regulation: KGR23 | Course Code: KG23ACM408
Scaled strictly for exam success (05 Marks vs 10 Marks format).
"""

UNIT1_QUESTIONS = [
    {
        "id": "MID1-Q01",
        "mid": "Mid-I",
        "qno": 1,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K1",
        "marks": "05 Marks",
        "title": "Define the speech production mechanism and identify the roles of excitation source and vocal tract system in speech generation.",
        "punchline": "Speech is produced by the Source-Filter Mechanism: Excitation Source generates raw acoustic energy, and Vocal Tract acts as a time-varying filter shaping formants.",
        "mnemonic": "L-G-V-A: Lungs generate pressure -> Glottis modulates excitation -> Vocal tract filters formants -> Articulators shape sounds",
        "analogy": "Like an acoustic trumpet or flute: The player's buzzing lips produce the raw acoustic buzz (excitation source), while the metallic pipe and valves resonate and shape distinct musical notes (vocal tract filter).",
        "diagram": """[ Lungs (Air Reservoir) ]
             │  Airflow Pressure
             ▼
     [ Glottis / Vocal Cords ]  <--- EXCITATION SOURCE (Voiced/Unvoiced)
             │
             ▼  Raw Acoustic Signal e(t)
     ┌────────────────────────────────────────┐
     │  Vocal Tract Acoustic Filter H(z)      │  <--- VOCAL TRACT SYSTEM
     │  - Pharynx (Throat Cavity)             │       (Acoustic Tube ~17.5 cm)
     │  - Oral Cavity (Mouth / Tongue / Teeth)│       Resonances = Formants
     │  - Nasal Cavity (Velum Open / Closed)  │       (F1, F2, F3)
     └────────────────────────────────────────┘
             │
             ▼  Radiation Filter R(z) (Lips)
     [ Radiated Speech Signal s(t) ]""",
        "content": """### 1. Definition of Speech Production Mechanism
The human speech production mechanism is modeled as a **Source-Filter System** (Gunnar Fant's Acoustic Theory of Speech Production). In this model:
* A sound **source** generates raw acoustic energy (either periodic pulses or turbulent random noise).
* The **vocal tract** behaves as an acoustic filter with frequency-dependent resonances that modulate this raw sound into distinct phonetic speech units (vowels, consonants).
* The mathematical relationship in the z-domain is:
  $$\\text{Speech Output } S(z) = E(z) \\cdot H(z) \\cdot R(z)$$
  where $E(z)$ is the excitation source, $H(z)$ is the vocal tract filter transfer function, and $R(z) \\approx 1 - z^{-1}$ is the lip radiation impedance.

---

### 2. Role of the Excitation Source
The excitation source provides the raw acoustic power generated from the lungs through the trachea and larynx (vocal cords):
1. **Voiced Sounds (Periodic Glottal Pulses):**
   * *Mechanism:* The vocal folds (cords) are brought together under lung air pressure. Aerodynamic forces (Bernoulli effect) cause them to rapidly open and snap shut in quasi-periodic cycles.
   * *Characteristics:* Periodic triangular airflow pulses with a fundamental frequency $F_0$ (Pitch). Men: $\\approx 100-150\\text{ Hz}$, Women: $\\approx 200-250\\text{ Hz}$, Children: $\\approx 300-400\\text{ Hz}$.
   * *Examples:* All English vowels (/a/, /e/, /i/, /o/, /u/) and voiced consonants (/m/, /n/, /b/, /d/, /z/).
2. **Unvoiced Sounds (Turbulent Noise):**
   * *Mechanism:* The vocal folds remain wide open (no vibration). Airflow passes through a narrow constriction in the oral tract (e.g., tongue against teeth or lips), creating high-velocity turbulent friction noise.
   * *Characteristics:* Aperiodic, continuous broad-spectrum random noise (resembling high-pass filtered white noise).
   * *Examples:* Fricatives like /s/, /sh/, /f/, /th/.
3. **Transient / Plosive Sounds (Pressure Burst):**
   * *Mechanism:* Complete closure of the vocal tract (lips or tongue on palate), building up intraoral pressure, followed by sudden explosive release.
   * *Examples:* /p/, /t/, /k/, /b/, /d/, /g/.

---

### 3. Role of the Vocal Tract System
The vocal tract is an acoustic resonant tube extending from the glottis to the lips (average length $\\approx 17.5\\text{ cm}$ in adult males):
1. **Acoustic Resonator:**
   * It amplifies certain frequencies while attenuating others based on its physical geometry.
   * The resonant frequencies of the vocal tract are called **Formants** ($F_1, F_2, F_3, \\dots$).
   * For a neutral uniform tube open at lips and closed at glottis ($L = 17.5\\text{ cm}$, speed of sound $c = 340\\text{ m/s}$):
     $$F_n = \\frac{(2n - 1) c}{4L} \\implies F_1 \\approx 500\\text{ Hz}, \\, F_2 \\approx 1500\\text{ Hz}, \\, F_3 \\approx 2500\\text{ Hz}$$
2. **Articulatory Modification:**
   * **Tongue height & position:** Alters oral cavity volume, controlling $F_1$ and $F_2$ to differentiate vowels (e.g., high-front /i/ vs low-back /a/).
   * **Velum (Soft Palate):** Lowers to open the nasal cavity, introducing nasal resonances and anti-resonances (spectral zeros for /m/, /n/).
   * **Lips:** Rounding/protrusion lengthens the vocal tract, lowering all formant frequencies.

---

### 4. Summary Table: Excitation Source vs. Vocal Tract

| Attribute | Excitation Source | Vocal Tract System |
| :--- | :--- | :--- |
| **Location** | Larynx / Glottis & Constrictions | Throat, Mouth, and Nose cavities |
| **Primary Function** | Generates raw acoustic energy | Shapes spectral envelope & timbre |
| **Speech Parameter** | Pitch ($F_0$), Voicing state, Energy | Formants ($F_1, F_2, F_3$), Phoneme identity |
| **Filter Model** | Input excitation $E(z)$ | All-pole / Pole-zero digital filter $H(z)$ |
| **Failure Effect** | Whispering (loss of pitch/voicing) | Mumbled/unintelligible sounds (loss of formants) |"""
    },
    {
        "id": "MID1-Q02",
        "mid": "Mid-I",
        "qno": 2,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Explain the discrete-time representation of speech signals and interpret the effects of sampling on signal reconstruction",
        "punchline": "Continuous speech $s(t)$ is discretized at interval $T_s$; sampling rate must satisfy Nyquist ($f_s \\ge 2 f_{\\max}$) to prevent aliasing distortion during reconstruction.",
        "mnemonic": "S-N-A-R: Sample at $T_s$, Nyquist condition, Anti-alias filtering, Sinc Reconstruction",
        "analogy": "Like recording a spinning car wheel on video: If the camera frame rate is too slow, the wheel appears to rotate backwards or freeze (aliasing). Only high frame rates reconstruct real motion.",
        "diagram": """Continuous Speech s(t) ──► [ Anti-Aliasing LPF ] ──► [ ADC / Sampler (Ts) ] ──► Discrete Speech s[n]
                                  (fc = fs / 2)               (fs = 1/Ts)
                                                                    │
                                                                    ▼
Reconstructed s(t) ◄── [ Reconstruction Filter ] ◄── [ D/A Converter ]
                           (Ideal Sinc LPF)""",
        "content": """### 1. Discrete-Time Representation of Speech Signals
Speech is naturally a continuous acoustic sound pressure wave $s(t)$. To process it digitally on microprocessors, DSPs, or computers:
1. **Sampling:** The continuous signal $s(t)$ is sampled at uniform time intervals $T_s = 1 / f_s$:
   $$s[n] = s(n T_s), \\quad n \\in \\mathbb{Z}$$
2. **Standard Speech Sampling Rates:**
   * **8 kHz ($T_s = 125\\,\\mu\\text{s}$):** Standard PSTN telephone speech. Captures band up to 3.4 kHz (sufficient for basic intelligibility).
   * **16 kHz ($T_s = 62.5\\,\\mu\\text{s}$):** Standard for Automated Speech Recognition (ASR) engines (Whisper, Siri, Google ASR) and VoIP. Captures up to 8 kHz.
   * **44.1 kHz / 48 kHz:** Studio audio and music production. Captures up to 20 kHz (full human audible range).

---

### 2. Mathematical Effect of Sampling (Frequency Domain)
Sampling in the time domain corresponds to periodic replication in the frequency domain:
$$S_s(\\Omega) = \\frac{1}{T_s} \\sum_{k=-\\infty}^{\\infty} S\\left(\\Omega - k \\Omega_s\\right), \\quad \\Omega_s = \\frac{2\\pi}{T_s} = 2\\pi f_s$$
* Spectral copies of the original baseband spectrum $S(\\Omega)$ are repeated at every multiple of the sampling angular frequency $\\Omega_s$.

---

### 3. Nyquist Sampling Theorem & Aliasing
* **Nyquist Criterion:** To reconstruct the continuous signal without distortion, the sampling frequency $f_s$ must be at least twice the highest frequency present in the speech signal ($f_{\\max}$):
  $$f_s \\ge 2 f_{\\max}$$
* **Effects of Undersampling ($f_s < 2 f_{\\max}$):**
  * When $f_s < 2 f_{\\max}$, adjacent spectral replicas overlap in the frequency domain.
  * This overlap is called **Aliasing Distortion**.
  * High-frequency components (such as unvoiced fricatives /s/, /sh/, /f/ at 5-8 kHz) fold down into lower frequencies (e.g., 1-3 kHz), masquerading as false low frequencies.
  * In speech recognition, aliasing corrupts formant peaks and ruins phoneme classification accuracy.

---

### 4. Signal Reconstruction Process
To recover the continuous speech signal $s(t)$ from discrete samples $s[n]$:
1. **Ideal Reconstruction (Whittaker-Shannon Interpolation):**
   * Pass the sampled impulse train through an ideal analog Low-Pass Filter (LPF) with cutoff frequency $f_c = f_s / 2$.
   * In time-domain, this corresponds to sinc interpolation:
     $$s(t) = \\sum_{n=-\\infty}^{\\infty} s[n] \\cdot \\text{sinc}\\left(\\frac{t - n T_s}{T_s}\\right) = \\sum_{n=-\\infty}^{\\infty} s[n] \\cdot \\frac{\\sin\\left(\\pi (t - n T_s) / T_s\\right)}{\\pi (t - n T_s) / T_s}$$
2. **Practical Solution in Speech Engineering:**
   * Always place an **Anti-Aliasing Filter** (sharp analog low-pass filter) before the ADC to eliminate any frequencies above $f_s / 2$."""
    },
    {
        "id": "MID1-Q03",
        "mid": "Mid-I",
        "qno": 3,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "A system is described by: Find the zeros by solving the numerator. Find the poles by solving the denominator. Comment on stability Note: Question based on Pole–Zero Modeling",
        "punchline": "Roots of Numerator = Zeros (spectral dips); Roots of Denominator = Poles (resonant formants). System is BIBO stable if and only if all poles lie strictly inside the unit circle ($|p_i| < 1$).",
        "mnemonic": "N-Z-D-P-U: Numerator = Zeros, Denominator = Poles, Unit circle determines stability",
        "analogy": "Poles are like resonance peaks in an acoustic bottle when blown; zeros are like damping pads absorbing specific frequencies. If a pole escapes outside the unit circle, the resonance explodes into infinite screeching feedback (instability).",
        "diagram": """           Im(z)
             │        Unit Circle (|z| = 1)
             │     ╭───────────╮
             │   ╭─            ─╮
             │  ╭       p1, p2    ╮
             │ │         ×   ×     │
     ────────┼─┼─────────●─────────┼──────────► Re(z)
             │ │        z1, z2     │
             │  ╰                 ╯
             │   ╰─            ─╮
             │     ╰───────────╯
             │
   Stable: All Poles (×) strictly INSIDE unit circle (|p| < 1)""",
        "content": """### 1. Problem Formulation
Consider the standard digital filter system function describing vocal tract pole-zero modeling:
$$H(z) = \\frac{1 - 0.5 z^{-1}}{1 - 0.9 z^{-1} + 0.2 z^{-2}}$$

To solve for poles and zeros, rewrite $H(z)$ with positive powers of $z$ by multiplying numerator and denominator by $z^2$:
$$H(z) = \\frac{z^2 (1 - 0.5 z^{-1})}{z^2 (1 - 0.9 z^{-1} + 0.2 z^{-2})} = \\frac{z(z - 0.5)}{z^2 - 0.9z + 0.2}$$

---

### 2. Step 1: Find Zeros by Solving the Numerator
The **zeros** of the system are the values of $z$ for which $H(z) = 0$ (roots of the numerator polynomial):
$$N(z) = z(z - 0.5) = 0$$

Solving the equation:
1. **First Zero ($z_1$):**
   $$z_1 = 0$$
2. **Second Zero ($z_2$):**
   $$z - 0.5 = 0 \\implies z_2 = 0.5$$

$$\\mathbf{Zeros: } \\quad z_1 = 0, \\quad z_2 = 0.5$$

---

### 3. Step 2: Find Poles by Solving the Denominator
The **poles** of the system are the values of $z$ for which $H(z) \\to \\infty$ (roots of the denominator polynomial):
$$D(z) = z^2 - 0.9z + 0.2 = 0$$

Factoring the quadratic equation:
* We need two numbers whose product is $+0.2$ and whose sum is $-0.9$. These numbers are $-0.5$ and $-0.4$.
$$(z - 0.5)(z - 0.4) = 0$$

Solving for $z$:
1. **First Pole ($p_1$):**
   $$p_1 = 0.5$$
2. **Second Pole ($p_2$):**
   $$p_2 = 0.4$$

$$\\mathbf{Poles: } \\quad p_1 = 0.5, \\quad p_2 = 0.4$$

*(Note on Pole-Zero Cancellation: Here $z = 0.5$ cancels between numerator and denominator, leaving an effective single-pole system $H(z) = \\frac{z}{z - 0.4}$.)*

---

### 4. Step 3: Comment on System Stability
* **BIBO Stability Criterion:** For a causal discrete-time LTI system to be Bounded-Input Bounded-Output (BIBO) stable, **all poles of $H(z)$ must strictly lie inside the unit circle** in the complex z-plane:
  $$|p_k| < 1 \\quad \\forall k$$
* **Evaluation:**
  * $|p_1| = |0.5| = 0.5 < 1$
  * $|p_2| = |0.4| = 0.4 < 1$
* **Conclusion:**
  Since both poles lie strictly inside the unit circle of the complex z-plane, the system is **Unconditionally BIBO Stable**. The impulse response $h[n]$ will decay exponentially to zero as $n \\to \\infty$.

---

### 5. Physical Significance in Speech Modeling
* **Poles:** Represent resonant frequencies (Formants) of the vocal tract. The angle of complex poles determines the formant frequency ($\\omega = \\angle p$), and radius $r$ determines bandwidth.
* **Zeros:** Represent spectral dips (anti-resonances) caused by nasal coupling (/m/, /n/) or constriction locations in fricatives."""
    },
    {
        "id": "MID1-Q04",
        "mid": "Mid-I",
        "qno": 4,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Explain the properties of the Fast Fourier Transform (FFT) relevant to speech signal analysis and recognition systems.",
        "punchline": "FFT reduces DFT computation from $O(N^2)$ to $O(N \\log_2 N)$; its properties (conjugate symmetry, energy conservation, linearity) enable real-time speech spectrograms and MFCC extraction.",
        "mnemonic": "L-S-T-R-P-W: Linearity, Symmetry, Time-shift, Resolution, Parseval energy, Windowing assumption",
        "analogy": "An optical prism that instantaneously refracts white light into individual color wavelengths in milliseconds, revealing pitch and formants from raw audio.",
        "diagram": """Speech Frame x[n] ──► [ Hamming Window ] ──► [ N-Point FFT ] ──► Complex X[k]
      (25 ms)             w[n]                 O(N log N)             │
                                                                       ├──► |X[k]| Magnitude (Spectrogram)
                                                                       └──► ∠X[k] Phase Spectrum""",
        "content": """### 1. Overview of FFT in Speech Processing
The Fast Fourier Transform (FFT) is an efficient algorithm to compute the Discrete Fourier Transform (DFT) of a windowed speech frame $x[n]$:
$$X[k] = \\sum_{n=0}^{N-1} x[n] W_N^{kn}, \\quad W_N = e^{-j \\frac{2\\pi}{N}}, \\quad k = 0, 1, \\dots, N-1$$
* While direct DFT requires $N^2$ complex operations, the Cooley-Tukey FFT algorithm requires only $\\frac{N}{2} \\log_2 N$ operations.
* For a 512-point speech frame, direct DFT requires 262,144 ops, whereas FFT requires only 2,304 ops (**>100x speedup**), making real-time ASR feasible.

---

### 2. Key FFT Properties Relevant to Speech

#### 1. Linearity (Superposition of Speech & Noise)
* **Property:** $\\text{FFT}\\{a x_1[n] + b x_2[n]\\} = a X_1[k] + b X_2[k]$.
* **Speech Relevance:** Allows additive noise models (Speech + Noise) to be decoupled and filtered in the spectral domain during speech enhancement and noise cancellation.

#### 2. Conjugate Symmetry (Hermitian Property for Real Speech)
* **Property:** Since speech $x[n]$ is real-valued, its spectrum satisfies:
  $$X[N - k] = X^*[k] \\implies |X[N - k]| = |X[k]|$$
* **Speech Relevance:** Redundant half of the spectrum can be discarded. We only need to store and process $\\frac{N}{2} + 1$ bins (from DC to Nyquist $f_s / 2$), saving 50% memory and compute in feature pipelines.

#### 3. Time-Shift Property (Invariance in Magnitude)
* **Property:** Shifting speech by $n_0$ samples introduces only a linear phase shift:
  $$\\text{FFT}\\{x[n - n_0]\\} = X[k] e^{-j \\frac{2\\pi k n_0}{N}} \\implies |\\text{FFT}\\{x[n - n_0]\\}| = |X[k]|$$
* **Speech Relevance:** The magnitude spectrum $|X[k]|$ (which carries phonetic formant information) is invariant to minor time delays in speech segmentation.

#### 4. Frequency Resolution vs. Time Resolution Trade-off
* **Property:** The frequency spacing between adjacent FFT bins is:
  $$\\Delta f = \\frac{f_s}{N}$$
* **Speech Relevance:**
  * **Narrowband Spectrogram (Large $N$, e.g., 512 at 8 kHz $\\to \\Delta f = 15.6\\text{ Hz}$):** High frequency resolution; resolves individual pitch harmonics (horizontal striations).
  * **Wideband Spectrogram (Small $N$, e.g., 128 at 8 kHz $\\to \\Delta f = 62.5\\text{ Hz}$):** High temporal resolution; resolves individual glottal pulses (vertical striations) and formant transitions.

#### 5. Parseval's Theorem (Energy Conservation)
* **Property:**
  $$\\sum_{n=0}^{N-1} |x[n]|^2 = \\frac{1}{N} \\sum_{k=0}^{N-1} |X[k]|^2$$
* **Speech Relevance:** Frame energy can be computed directly in the frequency domain. Used extensively for Voice Activity Detection (VAD) and speech endpoint detection.

#### 6. Periodicity Assumption & The Need for Windowing
* **Property:** FFT implicitly assumes the $N$-sample block is infinitely repeated.
* **Speech Relevance:** Truncating speech with a rectangular window creates sharp edge discontinuities, causing **Spectral Leakage**. Hence, speech frames must always be multiplied by smooth windows (Hamming / Hanning) before applying FFT."""
    },
    {
        "id": "MID1-Q05",
        "mid": "Mid-I",
        "qno": 5,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K4",
        "marks": "10 Marks",
        "title": "Analyze convolution operations in speech processing and examine their role in system response and filtering mechanisms.",
        "punchline": "Convolution mathematically expresses speech output as glottal excitation convolved with the vocal tract impulse response: $s[n] = e[n] * h[n]$; computed via Overlap-Add/Save for real-time streaming.",
        "mnemonic": "F-S-M-A: Flip, Shift, Multiply, Add -> Time domain convolution = Frequency domain multiplication",
        "analogy": "Talking in a cathedral: your vocal cord pulses are convolved with the acoustic impulse response of the cathedral architecture, producing a rich, reverberant echo.",
        "diagram": """Excitation e[n] ──► [ Vocal Tract LTI System h[n] ] ──► Radiated Speech s[n]
 (Glottal Pulse)               (Impulse Response)             s[n] = e[n] * h[n]

FREQUENCY DOMAIN EQUIVALENT:
           E(z) ──► [ Digital Filter H(z) ] ──► S(z) = E(z) · H(z)

REAL-TIME CONVOLUTION (Streaming Speech):
  Input Stream ──► [ Split into Blocks ] ──► [ FFT ] ──► [ Multiply H(k) ] ──► [ IFFT ] ──► [ Overlap-Add ]""",
        "content": """### 1. Mathematical Formulation of Convolution
Convolution is the fundamental mathematical operation governing Linear Time-Invariant (LTI) systems in speech processing.

#### 1. Discrete-Time Convolution Formula
If an input excitation signal $x[n]$ is applied to an LTI vocal tract system with unit impulse response $h[n]$, the output speech signal $y[n]$ is given by:
$$y[n] = x[n] * h[n] = \\sum_{k=-\\infty}^{\\infty} x[k] h[n - k]$$

#### 2. The Four Step Computational Procedure
1. **Folding / Inversion:** Reflect $h[k]$ across the origin to get $h[-k]$.
2. **Shifting:** Translate $h[-k]$ by $n$ units to get $h[n - k]$.
3. **Multiplication:** Form the product of sequences $w_n[k] = x[k] \\cdot h[n - k]$.
4. **Summation:** Sum all terms of $w_n[k]$ over all $k$ to yield the scalar output value $y[n]$.

---

### 2. Role of Convolution in the Speech Production Model
In digital speech processing, the continuous speech wave is modeled as a cascade of three LTI convolutions:
$$s[n] = e[n] * v[n] * r[n]$$
1. **Glottal Excitation $e[n]$:** The input source signal (train of impulses for voiced speech, white noise sequence for unvoiced speech).
2. **Vocal Tract Impulse Response $v[n]$:** Represents the acoustic resonances (formants) of the throat, mouth, and nasal cavities.
3. **Lip Radiation Impulse Response $r[n]$:** Models acoustic impedance matching at the lips (high-pass filter approximated as $r[n] = \\delta[n] - \\delta[n - 1]$).

By the associative property of convolution:
$$h[n] = v[n] * r[n] \\implies s[n] = e[n] * h[n]$$
The speech signal is entirely characterized by convolving the excitation with the composite vocal system impulse response $h[n]$.

---

### 3. Linear vs. Circular Convolution & The Convolution Theorem

| Parameter | Linear Convolution ($x[n] * h[n]$) | Circular Convolution ($x[n] \\circledast h[n]$) |
| :--- | :--- | :--- |
| **Output Length** | $L = N_1 + N_2 - 1$ | $N = \\max(N_1, N_2)$ (Periodic modulo $N$) |
| **Physical Reality** | True physical response of filters | Mathematical artifact of discrete FFT multiplication |
| **Time-Aliasing** | None | High risk of wrap-around distortion if $N < N_1 + N_2 - 1$ |

* **The Convolution Theorem:**
  $$\\mathcal{Z}\\{x[n] * h[n]\\} = X(z) \\cdot H(z) \\iff \\mathcal{F}\\{x[n] * h[n]\\} = X(\\omega) \\cdot H(\\omega)$$
  Convolution in the time domain is equivalent to simple point-wise multiplication in the frequency domain.

---

### 4. Real-Time Fast Convolution Algorithms for Streaming Speech
Direct time-domain convolution of long speech signals requires $O(N_1 N_2)$ operations. For real-time speech systems (hearing aids, noise cancellers, telephony), block convolution using FFT is executed via two standard algorithms:

#### 1. Overlap-Add (OLA) Method
1. The incoming speech stream is segmented into non-overlapping blocks of length $L$.
2. Each block is zero-padded to length $N = L + M - 1$ (where $M$ is filter length).
3. Compute $Y_i[k] = \\text{FFT}\\{x_i[n]\\} \\cdot \\text{FFT}\\{h[n]\\}$.
4. Compute $y_i[n] = \\text{IFFT}\\{Y_i[k]\\}$.
5. The trailing $M - 1$ samples of adjacent output blocks are overlapped and added together to assemble the continuous speech output.

#### 2. Overlap-Save (OLS) Method
1. Successive input speech blocks overlap by $M - 1$ samples.
2. Circular convolution of length $N$ is performed via FFT/IFFT.
3. The first $M - 1$ corrupted samples of each block (time-aliased region) are discarded (saved), and the remaining valid samples are concatenated directly.

---

### 5. Practical Filtering Mechanisms in Speech Systems
1. **Pre-Emphasis Filtering:** A first-order FIR high-pass filter ($y[n] = x[n] - \\alpha x[n - 1]$, with $\\alpha \\approx 0.95-0.97$) convolved with raw speech to counteract the $-6\\text{ dB/octave}$ glottal spectral tilt, boosting high-frequency formants for robust feature extraction.
2. **De-reverberation & Acoustic Echo Cancellation:** Adaptive filtering using LMS/NLMS algorithms to deconvolve room impulse responses from microphone audio.
3. **Speech Synthesis:** Convolving synthesized pitch pulses with estimated LPC vocal tract filter coefficients to generate natural-sounding voice."""
    },
    {
        "id": "MID1-Q06",
        "mid": "Mid-I",
        "qno": 6,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Evaluate the performance of linear and non-linear filter banks in speech signal decomposition with respect to frequency resolution and distortion.",
        "punchline": "Linear filter banks (uniform STFT) provide equal resolution everywhere; Non-linear filter banks (Mel/Bark) mimic human cochlear tonotopy (fine resolution <1 kHz, broad >1 kHz), achieving higher discriminability with lower distortion.",
        "mnemonic": "U-L-M-B: Uniform = Linear (STFT), Mel/Bark = Non-linear (Human Cochlea / Critical Bands)",
        "analogy": "A piano vs a scientific frequency generator: The human ear doesn't hear frequency linearly (100 Hz steps); it perceives musical intervals and octaves logarithmically (non-linear filter bank).",
        "diagram": """LINEAR FILTER BANK (Uniform Spacing & Constant Bandwidth):
   ▲ Gain
   │ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
   └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─► Frequency (Hz)
      Δf   Δf  Δf  Δf  Δf  Δf  Δf  Δf   (Constant Δf = 100 Hz everywhere)

NON-LINEAR FILTER BANK (Mel-Scale / Human Auditory Tonotopy):
   ▲ Gain
   │  /\   /\   /\    /  \     /    \       /      \
   └─/──\_/──\_/──\__/────\___/──────\_____/────────\─► Frequency (Hz)
     ◄── Fine Res (<1 kHz) ──► ◄── Coarse / Broad Res (>1 kHz) ──►""",
        "content": """### 1. Introduction to Filter Banks in Speech Processing
A filter bank is an array of bandpass filters that decomposes an input speech signal into multiple sub-band components. In speech engineering, filter banks are broadly categorized into:
1. **Linear (Uniform) Filter Banks:** Equal bandwidth and uniform spacing across the entire frequency range.
2. **Non-Linear (Auditory-Motivated) Filter Banks:** Variable bandwidths and non-uniform spacing that mirror the human auditory system's tonotopic organization.

---

### 2. Comprehensive Architectural & Performance Evaluation

#### 1. Linear (Uniform) Filter Banks
* **Structure:** Implemented via uniform digital bandpass filters or Short-Time Fourier Transform (STFT).
* **Center Frequencies:** $f_k = k \\cdot \\Delta f$, where $\\Delta f$ is constant (e.g., $100\\text{ Hz}$).
* **Bandwidth:** Constant bandwidth $B_k = B$ across all bands.
* **Performance Analysis:**
  * *Low-Frequency Region (<1 kHz):* Inadequate resolution. The fundamental pitch ($F_0$) and lower formants ($F_1$) are packed into too few filters, causing spectral smearing.
  * *High-Frequency Region (>1 kHz):* Wastes excessive filters and bandwidth resolving fine harmonic structures that the human ear cannot perceive.
  * *Phase & Waveform Distortion:* Minimal, perfectly invertible (allows exact waveform reconstruction).

#### 2. Non-Linear (Auditory-Motivated) Filter Banks
* **Structure:** Based on psychoacoustic experiments of the human basilar membrane (Mel scale, Bark scale, Equivalent Rectangular Bandwidth - ERB, Gammatone filters).
* **Mel-Scale Mapping:**
  $$M(f) = 2595 \\log_{10}\\left(1 + \\frac{f}{700}\\right)$$
* **Filter Geometry:** Overlapping triangular filters:
  * Linearly spaced with narrow bandwidth below $1\\text{ kHz}$ ($\\Delta f \\approx 100\\text{ Hz}$).
  * Logarithmically spaced with exponentially widening bandwidth above $1\\text{ kHz}$.
* **Performance Analysis:**
  * *Low-Frequency Region (<1 kHz):* High frequency resolution. Accurately resolves individual formant frequencies ($F_1, F_2$) critical for vowel identity.
  * *High-Frequency Region (>1 kHz):* Broad frequency integration. Smooths out irrelevant pitch harmonics while retaining general spectral energy shape.
  * *Noise Robustness:* High; wide high-frequency bands average out additive Gaussian white noise.
  * *Waveform Distortion:* Non-invertible without loss. Excellent for recognition features (MFCCs), but requires iterative algorithms (Griffin-Lim) for speech resynthesis.

---

### 3. Detailed Comparative Performance Matrix

| Evaluation Parameter | Linear Filter Banks (Uniform STFT) | Non-Linear Filter Banks (Mel / Bark Scale) |
| :--- | :--- | :--- |
| **Filter Spacing** | Constant linear spacing ($f_k = k \\Delta f$) | Linear below 1 kHz, Logarithmic above 1 kHz |
| **Bandwidth** | Constant for all channels ($B_k = \\text{const}$) | Increases exponentially with frequency |
| **Psychoacoustic Fidelity** | Poor; ignores human cochlear response | Excellent; models human critical band masking |
| **Low-Freq Resolution** | Coarse (cannot resolve close formants) | Very fine (superb $F_1, F_2$ distinction) |
| **High-Freq Resolution** | Excessively fine (redundant data) | Broad (captures spectral energy trends) |
| **Dimensionality** | High (typically 256 or 512 bins) | Compact (typically 26 to 40 triangular filters) |
| **Robustness to Noise** | Sensitive to narrowband and wideband noise | High robustness (averaging reduces noise variance) |
| **Reconstruction** | Exact, distortionless waveform synthesis | Lossy; designed for feature representation (MFCC) |
| **Primary Use Case** | Phase vocoders, audio compression (MP3) | Speech Recognition (ASR), Speaker Identification |

---

### 4. Critical Justification & Conclusion
For speech recognition and semantic perception tasks, **Non-Linear Filter Banks significantly outperform Linear Filter Banks**. They compact speech representation from hundreds of linear bins into 26-40 psychoacoustically salient filter energies, maximizing phonemic discriminability while drastically lowering computational burden and noise sensitivity."""
    },
    {
        "id": "MID1-Q07",
        "mid": "Mid-I",
        "qno": 7,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "A) A short speech frame is given as: Compute the 4-point DFT . Find the magnitude spectrum . Identify the dominant frequency component. Note: Problem based on Compute Discrete Fourier Transform (DFT) b) A speech signal is sampled at 8 kHz and frame size is 256 samples. Compute frequency resolution: Find the frequency corresponding to k = 10. Note: Problem based on Frequency Resolution.",
        "punchline": "Part A: 4-Point DFT computed via Twiddle Matrix gives DC=4, AC components magnitude |X[1]|=|X[3]|=2.0. Part B: Frequency resolution Δf = fs/N = 8000/256 = 31.25 Hz; bin k=10 corresponds to 312.5 Hz.",
        "mnemonic": "D-T-M-R-F: DFT Definition, Twiddle Matrix, Magnitude Spectrum, Resolution fs/N, Frequency k*Δf",
        "analogy": "Like an audio equalizer meter: The 4-point DFT tells you exactly which frequency bar jumps highest, while frequency resolution tells you the exact Hz spacing between each bar.",
        "diagram": """PART A: 4-POINT DFT & MAGNITUDE SPECTRUM
   Input x[n] = [2, 1, 0, 1]
           │
           ▼ Matrix Multiply by W4
   X[0] = 4 + j0      ──► |X[0]| = 4.000  (DC Component)
   X[1] = 2 + j0      ──► |X[1]| = 2.000  ◄── DOMINANT AC COMPONENT
   X[2] = 0 + j0      ──► |X[2]| = 0.000
   X[3] = 2 + j0      ──► |X[3]| = 2.000  ◄── DOMINANT AC COMPONENT

PART B: FREQUENCY RESOLUTION
   Sampling Rate fs = 8000 Hz, FFT Size N = 256
   Δf = fs / N = 8000 / 256 = 31.25 Hz/bin
   Bin k = 10 ──► f_10 = 10 × 31.25 Hz = 312.5 Hz (Voiced Pitch / Low Formant)""",
        "content": """### PART A: Numerical Problem on 4-Point DFT Computation

#### 1. Given Data
A short speech frame sequence of length $N = 4$ is given by:
$$x[n] = [2, 1, 0, 1] \\quad \\text{for } n = 0, 1, 2, 3$$

#### 2. Formula & Twiddle Factor Matrix
The $N$-point Discrete Fourier Transform (DFT) is defined as:
$$X[k] = \\sum_{n=0}^{N-1} x[n] W_N^{kn}, \\quad W_N = e^{-j \\frac{2\\pi}{N}}, \\quad k = 0, 1, \\dots, N-1$$

For $N = 4$:
$$W_4 = e^{-j \\frac{2\\pi}{4}} = e^{-j \\frac{\\pi}{2}} = -j$$
The twiddle factors are:
* $W_4^0 = 1$
* $W_4^1 = -j$
* $W_4^2 = (-j)^2 = -1$
* $W_4^3 = (-j)^3 = j$

The $4 \\times 4$ DFT transformation matrix is:
$$\\begin{bmatrix} X[0] \\\\ X[1] \\\\ X[2] \\\\ X[3] \\end{bmatrix} = \\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -j & -1 & j \\\\ 1 & -1 & 1 & -1 \\\\ 1 & j & -1 & -j \\end{bmatrix} \\begin{bmatrix} x[0] \\\\ x[1] \\\\ x[2] \\\\ x[3] \\end{bmatrix} = \\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -j & -1 & j \\\\ 1 & -1 & 1 & -1 \\\\ 1 & j & -1 & -j \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \\end{bmatrix}$$

#### 3. Step-by-Step Matrix Multiplication
1. **For $k = 0$ (DC Component):**
   $$X[0] = (1 \\cdot 2) + (1 \\cdot 1) + (1 \\cdot 0) + (1 \\cdot 1) = 2 + 1 + 0 + 1 = 4$$
2. **For $k = 1$:**
   $$X[1] = (1 \\cdot 2) + (-j \\cdot 1) + (-1 \\cdot 0) + (j \\cdot 1) = 2 - j + 0 + j = 2$$
3. **For $k = 2$:**
   $$X[2] = (1 \\cdot 2) + (-1 \\cdot 1) + (1 \\cdot 0) + (-1 \\cdot 1) = 2 - 1 + 0 - 1 = 0$$
4. **For $k = 3$:**
   $$X[3] = (1 \\cdot 2) + (j \\cdot 1) + (-1 \\cdot 0) + (-j \\cdot 1) = 2 + j + 0 - j = 2$$

*(Also, for alternate common textbook frame $x[n] = [1, 2, 3, 2]$:)*
* $X[0] = 1 + 2 + 3 + 2 = 8$
* $X[1] = 1(1) + 2(-j) + 3(-1) + 2(j) = 1 - 2j - 3 + 2j = -2$
* $X[2] = 1(1) + 2(-1) + 3(1) + 2(-1) = 1 - 2 + 3 - 2 = 0$
* $X[3] = 1(1) + 2(j) + 3(-1) + 2(-j) = 1 + 2j - 3 - 2j = -2$

#### 4. Magnitude Spectrum $|X[k]|$
For $x[n] = [2, 1, 0, 1]$:
* $|X[0]| = |4| = 4.0$
* $|X[1]| = |2| = 2.0$
* $|X[2]| = |0| = 0.0$
* $|X[3]| = |2| = 2.0$

#### 5. Identify the Dominant Frequency Component
* The overall maximum energy is at **$k = 0$** ($|X[0]| = 4.0$), representing the DC / zero-frequency average level.
* Excluding DC, the **dominant AC frequency components** are **$k = 1$ and $k = 3$** with magnitude $|X[1]| = |X[3]| = 2.0$.

---

### PART B: Frequency Resolution & Bin Frequency Computation

#### 1. Given Data
* Sampling frequency of speech signal: $f_s = 8\\text{ kHz} = 8000\\text{ Hz}$
* Frame size (FFT size): $N = 256\\text{ samples}$
* Target bin index: $k = 10$

#### 2. Task 1: Compute Frequency Resolution ($\\Delta f$)
Frequency resolution is the frequency spacing between two consecutive spectral bins in the discrete Fourier spectrum:
$$\\Delta f = \\frac{f_s}{N}$$

Substituting the given values:
$$\\Delta f = \\frac{8000\\text{ Hz}}{256} = \\mathbf{31.25\\text{ Hz/bin}}$$

#### 3. Task 2: Find the Frequency Corresponding to $k = 10$
The continuous analog frequency $f_k$ corresponding to discrete DFT bin index $k$ is given by:
$$f_k = k \\cdot \\Delta f = k \\cdot \\frac{f_s}{N}$$

For $k = 10$:
$$f_{10} = 10 \\times 31.25\\text{ Hz} = \\mathbf{312.5\\text{ Hz}}$$

#### 4. Engineering Interpretation
* A frequency of **$312.5\\text{ Hz}$** falls directly in the low-frequency acoustic band of human speech.
* It corresponds to the pitch range of children/female voices and the lower boundary of the first formant ($F_1$) of closed vowels such as /u/ and /i/."""
    },
    {
        "id": "MID1-Q08",
        "mid": "Mid-I",
        "qno": 8,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Analyze the formulation of Linear Predictive Coding (LPC) equations and evaluate its effectiveness in modeling speech signals for efficient parameter estimation.",
        "punchline": "LPC models speech as a linear combination of p past samples; minimizing mean squared error leads to the Yule-Walker equations solved in O(p^2) via the Levinson-Durbin algorithm.",
        "mnemonic": "P-E-Y-L: Predict from past, Error minimization, Yule-Walker matrix, Levinson-Durbin recursion",
        "analogy": "An auto-regressive forecaster: like predicting tomorrow's temperature based on a weighted sum of the last 10 days' temperatures plus today's weather shock.",
        "diagram": """LINEAR PREDICTIVE CODING (LPC) ANALYSIS & SYNTHESIS:

ANALYSIS (Encoder):
   Speech s[n] ──┬─────────────────────────────┐
                 │                             ▼
                 │        ┌─────────────────┐  -
                 └───────►│ LPC Predictor   ├──►(Σ)──► Residual Error e[n]
                          │ a1, a2, ..., ap │  +
                          └─────────────────┘

SYNTHESIS (Decoder):
   Excitation u[n] ──► [ Gain G ] ──► (Σ) ──► Synthesized Speech s^[n]
   (Pitch Pulses/Noise)                ▲
                                       │ Past Samples
                             ┌─────────┴─────────┐
                             │ All-Pole Filter   │
                             │ 1 / (1 - Σ ak z^-k│
                             └───────────────────┘""",
        "content": """### 1. Fundamental Principle of Linear Predictive Coding (LPC)
Linear Predictive Coding (LPC) is one of the most powerful and widely used techniques in speech processing. It is based on the **Source-Filter Model**, where the vocal tract is approximated by an **all-pole digital filter**:
$$H(z) = \\frac{S(z)}{U(z)} = \\frac{G}{1 - \\sum_{k=1}^p a_k z^{-k}} = \\frac{G}{A(z)}$$
where:
* $p$ is the prediction order (typically $p = 10$ to $16$ for $8-16\\text{ kHz}$ speech).
* $a_k$ are the LPC predictor coefficients.
* $G$ is the filter gain.

In the discrete-time domain, the current speech sample $s[n]$ is predicted as a linear combination of the past $p$ samples:
$$\\hat{s}[n] = \\sum_{k=1}^p a_k s[n - k]$$

---

### 2. Mathematical Formulation & Error Minimization

#### 1. Prediction Error (Residual)
The prediction error (residual) $e[n]$ is the difference between the actual sample $s[n]$ and the predicted sample $\\hat{s}[n]$:
$$e[n] = s[n] - \\hat{s}[n] = s[n] - \\sum_{k=1}^p a_k s[n - k]$$

#### 2. Mean Squared Error (MSE) Criterion
To determine the optimal filter coefficients $a_k$, we minimize the total squared prediction error $E$:
$$E = \\sum_{n} e^2[n] = \\sum_{n} \\left( s[n] - \\sum_{k=1}^p a_k s[n - k] \\right)^2$$

#### 3. Derivation of the Normal Equations (Yule-Walker Equations)
To find the coefficients $a_k$ that minimize $E$, take the partial derivative of $E$ with respect to each coefficient $a_i$ (for $i = 1, 2, \\dots, p$) and set it to zero:
$$\\frac{\\partial E}{\\partial a_i} = 0 \\implies \\sum_{n} 2 \\left( s[n] - \\sum_{k=1}^p a_k s[n - k] \\right) (-s[n - i]) = 0$$

Simplifying and rearranging terms:
$$\\sum_{k=1}^p a_k \\sum_{n} s[n - k] s[n - i] = \\sum_{n} s[n] s[n - i], \\quad \\text{for } i = 1, 2, \\dots, p$$

---

### 3. Autocorrelation Method vs. Covariance Method

#### 1. Autocorrelation Method
Assuming the windowed speech frame $s[n]$ is zero outside the window interval $[0, N-1]$, the term $\\sum_n s[n - k] s[n - i]$ reduces to the short-time autocorrelation function $R(|i - k|)$:
$$\\sum_{k=1}^p a_k R(|i - k|) = R(i), \\quad i = 1, 2, \\dots, p$$

In matrix form:
$$\\begin{bmatrix} R(0) & R(1) & R(2) & \\dots & R(p-1) \\\\ R(1) & R(0) & R(1) & \\dots & R(p-2) \\\\ R(2) & R(1) & R(0) & \\dots & R(p-3) \\\\ \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ R(p-1) & R(p-2) & R(p-3) & \\dots & R(0) \\end{bmatrix} \\begin{bmatrix} a_1 \\\\ a_2 \\\\ a_3 \\\\ \\vdots \\\\ a_p \\end{bmatrix} = \\begin{bmatrix} R(1) \\\\ R(2) \\\\ R(3) \\\\ \\vdots \\\\ R(p) \\end{bmatrix}$$
* **Symmetric Toeplitz Matrix:** The matrix has identical diagonals, allowing the system to be solved in $O(p^2)$ operations using the **Levinson-Durbin Recursion Algorithm**.
* **Guaranteed Stability:** The resulting all-pole filter $H(z)$ is **always minimum-phase and guaranteed stable** (all poles inside $|z| < 1$).

#### 2. Covariance Method
* The signal is not assumed to be zero outside the frame.
* Generates a symmetric positive-definite covariance matrix solved via Cholesky decomposition in $O(p^3)$ ops.
* Stability of the synthesis filter is not inherently guaranteed.

---

### 4. Efficient Parameter Estimation: Levinson-Durbin Algorithm
The Levinson-Durbin algorithm iteratively computes predictor coefficients of order $m$ from order $m-1$ ($m = 1, 2, \\dots, p$):
1. **Initialize:** $E^{(0)} = R(0)$
2. **For $m = 1, 2, \\dots, p$:**
   * Compute Reflection Coefficient (PARCOR coefficient) $k_m$:
     $$k_m = \\frac{R(m) - \\sum_{j=1}^{m-1} a_j^{(m-1)} R(m - j)}{E^{(m-1)}}$$
   * Update predictor coefficients:
     $$a_m^{(m)} = k_m$$
     $$a_j^{(m)} = a_j^{(m-1)} - k_m a_{m-j}^{(m-1)}, \\quad j = 1, 2, \\dots, m-1$$
   * Update error:
     $$E^{(m)} = E^{(m-1)} (1 - k_m^2)$$

---

### 5. Evaluation of LPC Effectiveness in Speech Systems

#### Advantages & Strengths:
1. **Enormous Data Compression:** Standard PCM speech requires $64\\text{ kbps}$ ($8\\text{ kHz} \\times 8\\text{ bits}$). LPC-10 transmits only pitch, voicing, gain, and 10 coefficients every $20\\text{ ms}$, operating at just **$2.4\\text{ kbps}$ (a 26x compression ratio)**.
2. **Accurate Formant Extraction:** The roots of $A(z) = 0$ give direct estimates of vocal tract formant frequencies and bandwidths.
3. **Source-Filter Separation:** Completely decouples vocal tract shape from glottal pitch.

#### Limitations:
1. **All-Pole Restriction:** Struggles to model nasalized vowels and fricatives that require spectral zeros (anti-formants).
2. **Background Noise Sensitivity:** Additive noise flattens spectral peaks, skewing LPC coefficients toward noise poles."""
    }
]
