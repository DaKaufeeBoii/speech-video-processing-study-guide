# -*- coding: utf-8 -*-
"""
Unit 1: Fundamentals of Speech Production, Discrete-Time Speech Signals & Analysis
Questions: Mid-I Q1 to Q8
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408 | Dr. Sandeep Kumar M
Written in student-friendly, zero-jargon peer-tutor style with complete mathematical rigor.
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
        "punchline": "Speech production is like playing a trumpet: your lungs pump air, your vocal cords buzz (source E(z)), your throat and mouth shape the tone (filter H(z)), and your lips blast it into the room (radiation R(z)).",
        "mnemonic": "C-F-A (Think -> Word -> Speak) & S(z) = E(z) · H(z) · R(z)",
        "analogy": "Think of a synthesizer: the oscillator generates a raw buzzy sawtooth wave (vocal cords), the audio filter cuts and boosts certain frequencies to make it sound like a guitar or flute (vocal tract), and the speaker projects the sound into the room (lips).",
        "diagram": """[ Brain: Conceptualize -> Formulate ]
                  │
                  ▼
       [ 1. Respiratory: Lungs ] (Air compressor / Power supply)
                  │
                  ▼
       [ 2. Phonatory: Vocal Cords ] ──► Raw Source E(z) [Buzz or Hiss]
                  │
                  ▼
       [ 3. Resonatory & Articulatory ] ──► Vocal Tract Filter H(z) [Formants F1, F2]
         (Throat, Tongue, Lips, Teeth)
                  │
                  ▼
       [ 4. Radiation at Lips ] ──► Lip High-Pass R(z) ≈ 1 - z⁻¹
                  │
                  ▼
       [ Output Speech Wave s(t) ]""",
        "content": """### 1. The Big Picture (What is Speech Production?)
Speech production is basically a 3-step human factory that turns an abstract thought in your brain into an acoustic sound wave that somebody else's ear can hear. 

In college lectures, this is broken down into **3 hierarchical levels**:
1. **Conceptualization (Thinking):** You decide *what* you want to say. Ideas, memories, and emotions form in your mind.
   - *Brain zones:* **Wernicke's area** decodes and picks the right words; **Broca's area** organizes the sequence.
2. **Formulation (Language Building):** Your brain turns those ideas into grammatical sentences, picks vocabulary, and plans muscle movements.
3. **Articulation (Physical Action):** Motor cortex fires nerve signals to your vocal muscles. Your lungs blow, vocal cords vibrate, and tongue moves to create audible sound.

---

### 2. The 5 Biological Subsystems (The Hardware)
To remember the organs involved for exam marks, think of a 5-part audio studio:
* **1. Respiratory System (The Power Supply):** Lungs, diaphragm, and trachea pump steady airflow. Without air pressure from the lungs, no sound exists.
* **2. Phonatory System (The Raw Oscillator):** Larynx and vocal cords. When cords vibrate together, they produce a pitched buzz (**voiced sound**, like vowels). When wide open, rushing air creates friction noise (**unvoiced sound**, like /s/ or /f/).
* **3. Resonatory System (The Equalizer Chamber):** The pharynx (throat), mouth cavity, and nasal cavity act as acoustic pipes that boost specific resonant frequencies called **formants** ($F_1, F_2, F_3$).
* **4. Articulatory System (The Sound Sculptor):** Tongue, lips, teeth, palate, and jaw move dynamically to carve sound into precise letters and syllables.
* **5. Regulatory System (The Control Center):** The brain monitors your own voice through your ears (auditory feedback) and muscle feel (proprioception) to adjust pitch and volume in real-time.

---

### 3. The Mathematical Source-Filter Model
In DSP, Gunnar Fant's famous **Source-Filter Model** describes speech mathematically in the z-domain:
$$S(z) = E(z) \\cdot H(z) \\cdot R(z)$$

| Component | Physical Organs | DSP Role | Output Characteristics |
| :--- | :--- | :--- | :--- |
| **Excitation Source $E(z)$** | Lungs & Vocal Cords (Glottis) | Generates raw sound energy: <br>• Voiced = Periodic glottal pulse train with fundamental frequency (Pitch $F_0$). <br>• Unvoiced = Random white noise. | Controls pitch and voice volume. |
| **Vocal Tract Filter $H(z)$** | Throat, Oral Cavity, Tongue, Lips (~17.5 cm tube) | Acts as an all-pole acoustic filter: <br>$H(z) = \\frac{G}{1 - \\sum_{k=1}^p a_k z^{-k}}$ <br>Natural resonances are called **Formants** ($F_1, F_2$). | Shapes the sound into distinct vowels (/a/, /i/, /u/) and consonants. |
| **Radiation $R(z)$** | Lips & Mouth Opening | High-pass filter at lip boundary: $R(z) \\approx 1 - z^{-1}$. | Boosts high frequencies by $+6\\text{ dB/octave}$ as sound enters free air. |

---

### 4. What to Write in Exam for Full Marks
- State the 3 levels: **Conceptualization $\\rightarrow$ Formulation $\\rightarrow$ Articulation**.
- Name the 5 subsystems: Respiratory, Phonatory, Resonatory, Articulatory, Regulatory.
- Write the core formula: **$S(z) = E(z) \\cdot H(z) \\cdot R(z)$**.
- Contrast **Voiced** (periodic pulses, vowels, pitch $F_0$) vs **Unvoiced** (random noise, fricatives /s/, no pitch)."""
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
        "punchline": "Computers can't store infinite continuous waves; they snap digital photos at rate fs. If fs < 2·fmax, high frequencies fold over as fake low frequencies (aliasing distortion) like a backwards-spinning car wheel on video.",
        "mnemonic": "Snap at fs >= 2·fmax; Filter with LPF before and after.",
        "analogy": "Like a movie camera filming a spinning helicopter rotor: if the camera takes too few frames per second, the blades look like they are standing still or spinning backwards (aliasing). You must shoot at least twice as fast as the rotor spins to see reality.",
        "diagram": """Continuous Speech s(t) ──► [ Anti-Aliasing LPF ] (Cuts frequencies above fs/2)
                                   │
                                   ▼
                            [ Sampler: fs ] (Snaps sample every T = 1/fs seconds)
                                   │
                                   ▼
                            Discrete Signal s[n] = s(nT)
                                   │
                                   ▼ (To Listen Back)
                            [ D/A Converter & Sinc Reconstruction LPF ]
                                   │
                                   ▼
                            Reconstructed Analog Speech s_r(t)""",
        "content": """### 1. The Big Picture (Continuous vs Discrete Speech)
Real-world human speech is an analog sound wave $s(t)$ — it's smooth and has infinite values every fraction of a microsecond. But computers only understand numbers and finite memory. 
To bring speech into a computer, we take snapshots of the sound wave at uniform intervals $T$:
$$s[n] = s(nT), \\quad n = 0, 1, 2, \\dots$$
where $T$ is the **sampling period** and $f_s = \\frac{1}{T}$ is the **sampling frequency** (how many numbers we save per second).

| Feature | Continuous Speech $s(t)$ | Discrete Speech $s[n]$ |
| :--- | :--- | :--- |
| **Domain** | Defined at every single time instant $t$ | Defined only at sample indices $n = 0, 1, 2, \\dots$ |
| **Values** | Infinite continuous voltages | A sequence of discrete digital numbers |
| **Processing** | Bulky analog circuits & resistors | Python code, DSP chips, AI neural nets |
| **Storage** | Degrades over time (cassette tape hiss) | Perfectly preserved as digital files (WAV, MP3) |

---

### 2. The Nyquist Sampling Criterion (The Golden Rule)
To capture a sound wave without losing any information, Harry Nyquist proved:
$$f_s \\ge 2 \\cdot f_{\\max}$$
Your sampling rate must be **at least twice the highest frequency** present in the speech!

#### Standard Real-World Sampling Rates:
* **8 kHz (Telephone standard):** Speech bandwidth is band-limited to 4 kHz ($f_{\\max} = 4\\text{ kHz} \\implies f_s = 2 \\times 4 = 8\\text{ kHz}$). Sounds like a phone call.
* **16 kHz (AI Speech Recognition / ASR standard):** Captures frequencies up to 8 kHz. Gives crisp consonants (/s/, /sh/, /t/) needed for Alexa/Siri to understand you.
* **44.1 kHz (CD Audio) / 48 kHz (Studio Video):** Captures up to 20 kHz (full range of human hearing).

---

### 3. What Happens If You Undersample? (Aliasing!)
If you sample too slowly ($f_s < 2 f_{\\max}$), disaster strikes:
- High-frequency sound waves fold over and masquerade as low-frequency sounds in the discrete signal.
- In audio, this produces harsh robotic chirps, screeching distortion, and muddy speech.
- **The Solution (Anti-Aliasing Filter):** Always pass speech through a sharp analog **Low-Pass Filter (LPF)** *before* the sampler, cutting off all frequencies above $\\frac{f_s}{2}$ (the Nyquist frequency).

---

### 4. Signal Reconstruction (Getting Sound Back to Your Ears)
To convert the numbers $s[n]$ back into continuous air pressure waves for a loudspeaker:
1. Each number is turned into an electrical pulse.
2. The pulses pass through an **ideal reconstruction low-pass filter** with a **Sinc impulse response**:
   $$s_r(t) = \\sum_{n=-\\infty}^{\\infty} s[n] \\, \\text{sinc}\\left( \\frac{t - nT}{T} \\right), \\quad \\text{where } \\text{sinc}(x) = \\frac{\\sin(\\pi x)}{\\pi x}$$
Each discrete sample spreads a smooth sinc wave; all the sinc waves add up to reconstruct the original continuous speech wave without any jagged stair-steps!"""
    },
    {
        "id": "MID1-Q03",
        "mid": "Mid-I",
        "qno": 3,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "A discrete-time speech system has transfer function H(z) = [z(z - 0.5)] / [z² - 0.9z + 0.2]. Find its poles and zeros, plot them on the z-plane, and determine if the system is stable.",
        "punchline": "Zeros make the system silent (roots of top = 0, 0.5); Poles make the system resonate (roots of bottom = 0.5, 0.4). Because both poles are strictly inside the unit circle (|p| < 1), the system is BIBO Stable!",
        "mnemonic": "Zeros = Numerator; Poles = Denominator. |Poles| < 1 means STABLE.",
        "analogy": "Imagine tuning a guitar: poles are the resonant frets that make the string ring out loud; zeros are your fingers muting the string. If a pole jumps outside the circle, the guitar squeals with endless ear-piercing feedback (unstable). If all poles stay inside, it plays a clean note that decays naturally (stable).",
        "diagram": """                  Im(z) ▲
                        │        Unit Circle (|z| = 1)
                     ┌──┼──┐
                  ┌──┘  │  └──┐
                 ┌┘     │     └┐
                 │      │      │
      ───────────┼──────┼──────o────x─────x─────┼──────────► Re(z)
                 │     (0,0)  0.4  0.5   0.5    │
                 └┐     │     [Pole 2] [Pole 1] ┘
                  └──┐  │  ┌──┘        [Zero 2]
                     └──┼──┘
                        │
       Zeros (o): z = 0,  z = 0.5
       Poles (x): p₁ = 0.5,  p₂ = 0.4
       Stability: Both poles inside |z| < 1  ==>  BIBO STABLE!""",
        "content": """### 1. The Given Transfer Function
We are handed the discrete-time speech system:
$$H(z) = \\frac{z(z - 0.5)}{z^2 - 0.9z + 0.2}$$

---

### 2. Step 1: Finding the Zeros (Roots of Numerator)
Zeros are the values of $z$ that make $H(z) = 0$ (they cancel out sound):
$$\\text{Numerator: } z(z - 0.5) = 0$$
$$\\implies z_1 = 0, \\quad z_2 = 0.5$$
- **Zeros:** Located at $z = 0$ and $z = 0.5$.

---

### 3. Step 2: Finding the Poles (Roots of Denominator)
Poles are the values of $z$ that make the denominator zero and blow $H(z) \\to \\infty$ (these represent vocal tract resonances / formants):
$$\\text{Denominator: } z^2 - 0.9z + 0.2 = 0$$

Using standard quadratic factoring: we need two numbers that multiply to $+0.2$ and add to $-0.9$. Those numbers are $-0.5$ and $-0.4$:
$$(z - 0.5)(z - 0.4) = 0$$
$$\\implies p_1 = 0.5, \\quad p_2 = 0.4$$
- **Poles:** Located at $p_1 = 0.5$ and $p_2 = 0.4$.

*(Notice: A zero at $z=0.5$ cancels the pole at $z=0.5$, leaving an effective first-order pole at $z=0.4$, but we plot all original poles and zeros as requested!)*

---

### 4. Step 3: Determining System Stability (BIBO Criterion)
A discrete-time LTI system is **Bounded-Input Bounded-Output (BIBO) Stable** if and only if **all its poles lie strictly inside the unit circle** in the complex z-plane:
$$|p_i| < 1 \\quad \\forall i$$

Let's test both poles:
* Pole 1: $|p_1| = |0.5| = 0.5 < 1$  (Strictly inside unit circle)
* Pole 2: $|p_2| = |0.4| = 0.4 < 1$  (Strictly inside unit circle)

### Final Verdict:
Since both poles ($0.5$ and $0.4$) have magnitude strictly less than $1$, **THE SYSTEM IS BIBO STABLE**. 
When excited by speech impulses, its impulse response $h[n]$ will naturally decay to zero rather than blowing up to infinity."""
    },
    {
        "id": "MID1-Q04",
        "mid": "Mid-I",
        "qno": 4,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "State the key properties of the Fast Fourier Transform (FFT) and explain their importance in speech spectral analysis.",
        "punchline": "The FFT is a supercharged algorithm that calculates the discrete Fourier spectrum in O(N log N) time instead of O(N²); its symmetry, shift invariance, and frequency resolution (Δf = fs/N) make real-time spectrograms possible.",
        "mnemonic": "L-S-S-R-E-P (Linearity, Symmetry, Shift, Resolution, Energy, Periodicity)",
        "analogy": "Like using a food processor instead of chopping onions by hand with a knife: brute-force DFT makes 65,000 slow cuts; FFT organizes cuts hierarchically and finishes in 2,000 quick chops, enabling live video and audio analysis in real time.",
        "diagram": """Speech Frame x[n] (N=512) ──► [ Hamming Window ] ──► [ FFT O(N log₂ N) ]
                                                            │
                                  ┌─────────────────────────┴─────────────────────────┐
                                  ▼                                                   ▼
                       Magnitude Spectrum |X[k]|                                Phase ∠X[k]
                     (Vocal Tract Formant Peaks)                              (Timing & Delays)""",
        "content": """### 1. The Big Picture (Why FFT Matters in Speech)
Raw speech in time domain looks like a confusing squiggly line. To find vowels, formants, and pitches, we must look at the **frequency spectrum**. 
The Discrete Fourier Transform (DFT) does this, but brute-force calculation requires $N^2$ complex multiplications. For a small 1024-sample frame, that's over **1,000,000 multiplications**!
The **Fast Fourier Transform (FFT)** (Cooley-Tukey algorithm) divides the problem into even and odd halves recursively, slashing complexity to $O(N \\log_2 N)$ (just ~10,000 operations — **over 100 times faster!**).

---

### 2. The 6 Core Properties to Write in Exam (Dr. Sandeep Kumar M Slides)

#### 1. Linearity:
If you mix two sounds $x_1[n]$ and $x_2[n]$, their spectrum is the simple sum of their individual FFTs:
$$\\text{FFT}\\{a x_1[n] + b x_2[n]\\} = a X_1[k] + b X_2[k]$$
*Why it matters:* In speech enhancement, speech and background noise add linearly in the frequency domain.

#### 2. Conjugate Symmetry (Hermitian Property):
For any real-valued speech signal, the negative frequencies are the complex conjugates of the positive frequencies:
$$X[N - k] = X^*[k] \\implies |X[N - k]| = |X[k]|$$
*Why it matters:* The second half of the FFT spectrum is a mirror reflection of the first half. We only need to store and compute $\\frac{N}{2} + 1$ bins, saving half the RAM!

#### 3. Time-Shift $\\leftrightarrow$ Phase Change:
Shifting a speech frame in time does **not** change its magnitude spectrum; it only rotates the phase:
$$x[n - n_0] \\stackrel{\\mathcal{F}}{\\longleftrightarrow} X[k] \\cdot e^{-j \\frac{2\\pi}{N} k n_0} \\implies |X_{\\text{shifted}}[k]| = |X[k]|$$
*Why it matters:* A vowel sounds like the same vowel whether you speak it at second 1 or second 2.

#### 4. Frequency Resolution:
The spacing between adjacent frequency bins in an $N$-point FFT is:
$$\\Delta f = \\frac{f_s}{N}\\text{ Hz/bin}$$
*Why it matters:* To resolve individual pitch harmonics (typically 100–200 Hz apart), we must choose a sufficiently large frame size $N$.

#### 5. Parseval's Energy Conservation Theorem:
Total energy in the time domain equals total energy in the frequency domain:
$$\\sum_{n=0}^{N-1} |x[n]|^2 = \\frac{1}{N} \\sum_{k=0}^{N-1} |X[k]|^2$$
*Why it matters:* Voice activity detectors (VAD) can calculate frame loudness and silence directly from FFT bins.

#### 6. Periodicity & Windowing:
The FFT implicitly assumes the $N$-point frame repeats forever. Abrupt frame chops create artificial edge jumps (spectral leakage). Multiplying by a smooth **Hamming window** fixes this completely."""
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
        "punchline": "Convolution is how the vocal tract tube imprints its resonant formants onto glottal buzz pulses; in real-time DSP, the Overlap-Add (OLA) algorithm uses FFT multiplication to filter continuous speech without lag.",
        "mnemonic": "F-S-M-S: Flip, Shift, Multiply, Sum. Time convolution = Frequency multiplication.",
        "analogy": "Like singing inside an empty tiled bathroom: your vocal cords produce the input sound $x[n]$, the bathroom tiles and walls produce echoes called the impulse response $h[n]$, and what you hear is their convolution $y[n] = x[n] \\ast h[n]$.",
        "diagram": """Lungs & Cords Excitation e[n] ──► [ Vocal Tract LTI System: h[n] ] ──► Speech s[n] = e[n] * h[n]
(Periodic Pulses or Noise)         (Vocal Tract Impulse Response)

TIME DOMAIN:
s[n] = Σ e[k] · h[n - k]  (Computationally heavy for long files!)

FREQUENCY DOMAIN EQUIVALENT:
S(ω) = E(ω) · H(ω)  (Simple point-by-point multiplication!)

REAL-TIME FILTERING VIA OVERLAP-ADD (OLA):
Long Speech ──► Chop into blocks L ──► Zero-pad to N ──► FFT ──► Multiply by H[k] ──► IFFT ──► Add overlapping tails!""",
        "content": """### 1. The Big Picture (What is Convolution in Speech?)
In speech processing, **convolution** is the mathematical operation that describes what happens when a sound signal passes through an acoustic filter or physical space.
Whenever you talk, your vocal cords create raw excitation pulses $e[n]$. As this air travels up your 17.5 cm throat and mouth cavity (which has impulse response $h[n]$), every pulse generates a ringing resonance. The resulting spoken speech $s[n]$ is the **convolution** of excitation and vocal tract:
$$s[n] = e[n] \\ast h[n] = \\sum_{k=-\\infty}^{\\infty} e[k] \\, h[n - k]$$

---

### 2. The 4 Steps of Discrete Convolution (F-S-M-S)
If an examiner asks you to explain the mechanics of convolution, write these 4 mechanical steps:
1. **Flip:** Take the impulse response $h[k]$ and reverse it in time to get $h[-k]$.
2. **Shift:** Slide it along the time axis by offset $n$ to get $h[n - k]$.
3. **Multiply:** Multiply the input signal $x[k]$ by the shifted impulse response point-by-point.
4. **Sum:** Add up all the products to produce the single output sample $y[n]$.

---

### 3. Key Role in Speech Filtering Mechanisms

#### A. The Convolution Theorem (The Magic Shortcut):
Convolution in the time domain is equivalent to **simple multiplication** in the frequency domain:
$$y[n] = x[n] \\ast h[n] \\stackrel{\\mathcal{F}}{\\longleftrightarrow} Y(\\omega) = X(\\omega) \\cdot H(\\omega)$$
Instead of doing thousands of slow slide-and-sum additions in Python, we simply take the FFT of the speech, multiply by the filter spectrum, and take the IFFT!

#### B. Pre-Emphasis High-Pass Filtering:
Natural speech has a biological problem: human glottal pulses roll off at $-6\\text{ dB/octave}$, making high-frequency consonants (/s/, /t/, /k/) very quiet.
We convolve the speech with a simple 2-tap FIR filter:
$$h[n] = \\delta[n] - 0.97 \\delta[n-1] \\implies y[n] = s[n] - 0.97 s[n-1]$$
This boosts high frequencies by $+6\\text{ dB/octave}$, balancing the spectrum and boosting recognition accuracy!

#### C. Room Reverberation & Echo Modeling:
When speaking in an auditorium, sound bounces off walls before reaching the microphone:
$$x_{\\text{mic}}[n] = s[n] \\ast h_{\\text{room}}[n]$$
Denoising and speech dereverberation algorithms use inverse filtering (deconvolution) to remove room echoes.

---

### 4. Real-Time Overlap-Add (OLA) Block Convolution
You cannot wait for a person to finish a 1-hour speech before running an FFT! Real-time systems use the **Overlap-Add (OLA)** method:
1. Divide continuous incoming speech into short blocks of length $L$ (e.g., 20 ms).
2. For an FIR filter of length $M$, pad each speech block with zeros up to size $N \\ge L + M - 1$.
3. Compute $N$-point FFT of the block, multiply by filter $H[k]$, and compute inverse FFT.
4. Because the filter rings out for $M-1$ samples, add the overlapping trailing tails to the next block!
This delivers continuous real-time audio output with zero latency and zero boundary clicks."""
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
        "punchline": "Linear filter banks split sound like an inflexible ruler with equal Hz everywhere (wasting data on highs); non-linear Mel filter banks mimic the human ear cochlea, offering laser-sharp resolution at low formant frequencies and broad pooling at highs.",
        "mnemonic": "Linear = Uniform STFT (Equal bandwidth). Mel = Human Ear (Dense below 1kHz, Log above 1kHz).",
        "analogy": "Imagine shopping for clothes: a linear system offers sizes every 1 inch from size 0 to size 100 (half of which nobody buys); a non-linear human system offers lots of fine sizes where most people fit (Small, Medium, Large) and bundles the extreme ends together.",
        "diagram": """1. LINEAR FILTER BANK (Uniform STFT Bins):
   Δf = Constant (e.g., 100 Hz everywhere)
   ▲ Gain
   │ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐
   └─┴──┴─┴──┴─┴──┴─┴──┴─┴──┴─┴──┴─┴──┴─┴──┴─┴──┴──────► Frequency (Hz)
     0    100  200  300  400  500  600  700  800

2. NON-LINEAR MEL FILTER BANK (Human Ear Cochlea):
   Dense triangles below 1 kHz; Logarithmically wider above 1 kHz
   ▲ Gain
   │  /\\  /\\  /\\   /──\\     /────\\       /──────\\
   └─┴──┴─┴──┴─┴──┴────┴───┴──────┴─────┴────────┴─────► Frequency (Hz)
     0   200  400 700 1000   2000        4000          8000
     <-- High Resolution --> <---- Low Resolution / Broad Pooling ---->""",
        "content": """### 1. The Big Picture (Why Filter Banks?)
A filter bank is a collection of bandpass filters that chops an incoming speech wave into multiple frequency channels. In speech recognition (ASR), how you space these filters decides whether your AI can recognize words accurately or gets confused by background noise.

---

### 2. Linear Filter Banks (The Mathematical Ruler)
- **Design:** All filters have identical, fixed bandwidths uniformly spaced across the entire spectrum (e.g., standard Short-Time Fourier Transform bins where $\\Delta f = \\frac{f_s}{N} = 100\\text{ Hz}$ everywhere).
- **Frequency Resolution:** Equal resolution across all frequencies. It examines 100 Hz to 200 Hz with the exact same precision as 7100 Hz to 7200 Hz.
- **Why It's Inefficient for Speech:**
  - The human vocal tract places its most critical information — **Formants $F_1$ and $F_2$** (which differentiate vowels like /a/ from /i/) — in the low-frequency range below 2 kHz.
  - Linear filter banks waste massive computational bandwidth calculating microscopic details at 6 kHz or 7 kHz where human hearing cannot tell differences anyway!

---

### 3. Non-Linear Mel Filter Banks (The Human Ear Model)
- **Design:** Modeled after the **tonotopic organization of the human cochlea** (the basilar membrane in the inner ear).
- **The Mel Formula:**
  $$\\text{Mel}(f) = 2595 \\log_{10}\\left( 1 + \\frac{f}{700} \\right)$$
- **Structure:**
  - **Below 1000 Hz:** Filters are narrow and linearly spaced (~100 Hz apart). Gives razor-sharp frequency resolution to capture delicate formant shifts.
  - **Above 1000 Hz:** Filters widen logarithmically (exponentially wider spacing). It groups high frequencies together, just like human ears do.

---

### 4. Comprehensive Performance Evaluation Matrix

| Evaluation Criterion | Linear Filter Bank (STFT) | Non-Linear Mel Filter Bank (MFCC) |
| :--- | :--- | :--- |
| **Filter Spacing** | Uniform linear spacing ($\\Delta f = \\text{constant}$) | Non-linear: Linear below 1 kHz, logarithmic above 1 kHz |
| **Low-Frequency Resolution (< 1 kHz)**| Moderate / Suboptimal | **Extremely High** (Resolves formants $F_1, F_2$ clearly) |
| **High-Frequency Resolution (> 2 kHz)**| Excessively high (Wastes parameters) | Low resolution / Broad band integration |
| **Distortion & Noise Robustness** | **High Distortion:** Sharp spikes and microphone hiss directly corrupt narrow linear bins | **Low Distortion:** Triangular filter integration smooths out noise spikes |
| **Parameter Size** | 256 to 512 coefficients per frame | Compact: 26 to 40 triangular filterbanks |
| **Best Application** | Narrowband acoustic analysis, music pitch tracking | **Speech Recognition (ASR), Speaker Identification, Voice AI** |

### 5. Final Engineering Verdict
Mel-scale non-linear filter banks are vastly superior for speech AI because they throw away imperceptible high-frequency variations while maximizing the SNR and resolution of the vocal tract formants that carry human meaning."""
    },
    {
        "id": "MID1-Q07",
        "mid": "Mid-I",
        "qno": 7,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "A) A short speech frame is given as x[n] = [2, 1, 0, 1]. Compute the 4-point DFT, find the magnitude spectrum, and identify the dominant frequency component. B) A speech signal is sampled at 8 kHz and frame size is 256 samples. Compute frequency resolution and find the frequency corresponding to k = 10.",
        "punchline": "Part A: Multiplying by the 4-point DFT matrix gives X = [4, 2, 0, 2], with peak DC energy 4.0 at k=0 and AC energy 2.0 at k=1, 3. Part B: 8000 / 256 = 31.25 Hz per bin, so bin 10 represents 312.5 Hz.",
        "mnemonic": "DFT: X = [W4] · x. Bin Freq: f_k = k · (fs / N).",
        "analogy": "Part A is like breaking a secret 4-ingredient smoothie into its flavor percentages. Part B is reading a frequency speedometer where each notch tick mark represents 31.25 mph.",
        "diagram": """PART A: 4-POINT DFT MAGNITUDE SPECTRUM
|X[k]| ▲
   4.0 │      █ k = 0 (DC Peak: Average Signal Value = 4)
   3.0 │      █
   2.0 │      █         █ k = 1 (AC Peak = 2)               █ k = 3 (AC Peak = 2)
   1.0 │      █         █                                   █
   0.0 └───┴──┴─────────┴──┴───────────────────┴──┴─────────┴──┴──────► k
           k = 0        k = 1                  k = 2        k = 3

PART B: FREQUENCY RESOLUTION RULER
0 Hz        31.25 Hz       62.5 Hz              312.5 Hz (k = 10)         4000 Hz (Nyquist)
├─── Notch 0 ──┼── Notch 1 ──┼── Notch 2 ── ... ──┼── Notch 10 ── ... ────┤
<-- Δf = 31.25 Hz/bin -->""",
        "content": """### PART A: 4-Point DFT Calculation

#### 1. Given Data:
$$x[n] = [2, 1, 0, 1], \\quad N = 4$$

#### 2. The 4-Point DFT Formula:
$$X[k] = \\sum_{n=0}^{N-1} x[n] \\, e^{-j \\frac{2\\pi}{N} k n} = \\sum_{n=0}^{3} x[n] W_4^{k n}, \\quad k = 0, 1, 2, 3$$
where the twiddle factor matrix for $N=4$ is:
$$\\mathbf{W}_4 = \\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -j & -1 & j \\\\ 1 & -1 & 1 & -1 \\\\ 1 & j & -1 & -j \\end{bmatrix}$$

#### 3. Step-by-Step Matrix Multiplication:
$$\\begin{bmatrix} X[0] \\\\ X[1] \\\\ X[2] \\\\ X[3] \\end{bmatrix} = \\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -j & -1 & j \\\\ 1 & -1 & 1 & -1 \\\\ 1 & j & -1 & -j \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \\end{bmatrix}$$

* **For $k = 0$ (DC component):**
  $$X[0] = 1(2) + 1(1) + 1(0) + 1(1) = 2 + 1 + 0 + 1 = \\mathbf{4}$$
* **For $k = 1$:**
  $$X[1] = 1(2) - j(1) - 1(0) + j(1) = 2 - j + 0 + j = \\mathbf{2}$$
* **For $k = 2$:**
  $$X[2] = 1(2) - 1(1) + 1(0) - 1(1) = 2 - 1 + 0 - 1 = \\mathbf{0}$$
* **For $k = 3$:**
  $$X[3] = 1(2) + j(1) - 1(0) - j(1) = 2 + j + 0 - j = \\mathbf{2}$$

$$\\mathbf{X[k] = [4, \\ 2, \\ 0, \\ 2]}$$

#### 4. Magnitude Spectrum Calculation:
The magnitude spectrum $|X[k]| = \\sqrt{\\text{Re}^2 + \\text{Im}^2}$:
* $|X[0]| = |4| = \\mathbf{4.0}$
* $|X[1]| = |2| = \\mathbf{2.0}$
* $|X[2]| = |0| = \\mathbf{0.0}$
* $|X[3]| = |2| = \\mathbf{2.0}$

#### 5. Identifying the Dominant Frequency Component:
- The **overall dominant component** is at $k = 0$ with magnitude $|X[0]| = 4.0$ (representing the DC / average energy).
- The **dominant AC (oscillating) frequency component** is at **$k = 1$ and $k = 3$** with magnitude **$2.0$**.

---

### PART B: Frequency Resolution Problem

#### 1. Given Parameters:
* Sampling Frequency: $f_s = 8\\text{ kHz} = 8000\\text{ Hz}$
* Frame Size (DFT Length): $N = 256\\text{ samples}$

#### 2. Formula 1: Compute Frequency Resolution ($\\Delta f$)
$$\\Delta f = \\frac{f_s}{N}$$
$$\\Delta f = \\frac{8000\\text{ Hz}}{256} = \\mathbf{31.25\\text{ Hz/bin}}$$

#### 3. Formula 2: Find Frequency for Bin $k = 10$
$$f_k = k \\cdot \\Delta f = k \\cdot \\frac{f_s}{N}$$
$$f_{10} = 10 \\times 31.25\\text{ Hz} = \\mathbf{312.5\\text{ Hz}}$$

### Final Answer Summary:
1. **4-Point DFT:** $X = [4, 2, 0, 2]$
2. **Magnitudes:** $|X| = [4.0, 2.0, 0.0, 2.0]$ (Dominant DC at $k=0$, Dominant AC at $k=1, 3$)
3. **Frequency Resolution:** $\\Delta f = 31.25\\text{ Hz/bin}$
4. **Frequency at $k=10$:** $f_{10} = 312.5\\text{ Hz}$"""
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
        "punchline": "LPC predicts the current speech sample as a weighted sum of the previous p samples; minimizing prediction error leads to Yule-Walker equations solved in O(p²) time by Levinson-Durbin to compress speech 20x.",
        "mnemonic": "P-E-Y-L: Predict sample -> Error minimization -> Yule-Walker matrix -> Levinson-Durbin recursion.",
        "analogy": "Like predictive auto-complete on your phone keyboard: based on the last 10 words you typed, the phone guesses the next word with 90% accuracy. Instead of sending the full audio waveform, you just send the 10 predictor weights and the tiny prediction error!",
        "diagram": """ANALYSIS (ENCODER):
Speech s[n] ──► [ Delay Taps z⁻¹ ] ──► Linear Predictor ak ──► Predicted ŝ[n]
     │                                                               │
     └───────────────────────────────[ - ]◄──────────────────────────┘
                                       │
                                       ▼
                             Prediction Error e[n] (Compressed!)

SYNTHESIS (DECODER):
Pitch Pulses / Noise e[n] ──► [ All-Pole Filter: 1 / A(z) ] ──► Reconstructed Speech s[n]
                              (Controlled by 10-16 LPC weights ak)""",
        "content": """### 1. The Big Picture (What is LPC?)
**Linear Predictive Coding (LPC)** is one of the most powerful algorithms in speech history (used in cellphones, secure military radios, and voice synthesizers).
The core idea is simple: human speech has high inertia because your vocal organs cannot move instantly. Therefore, **the current speech sample $s[n]$ can be approximated as a linear combination of the past $p$ samples**:
$$\\hat{s}[n] = \\sum_{k=1}^p a_k \\, s[n - k]$$
where $p$ is the **prediction order** (typically $p = 10$ to $16$) and $a_k$ are the **LPC coefficients**.

---

### 2. Formulating the Error Minimization Equations
The prediction error (residual) between the real speech and predicted speech is:
$$e[n] = s[n] - \\hat{s}[n] = s[n] - \\sum_{k=1}^p a_k \\, s[n - k]$$

Our goal is to find the magical weights $a_k$ that minimize the **Total Mean Squared Error $E$**:
$$E = \\sum_n e[n]^2 = \\sum_n \\left( s[n] - \\sum_{k=1}^p a_k s[n-k] \\right)^2$$

To find the minimum, take the partial derivative with respect to each weight $a_i$ and set it to zero:
$$\\frac{\\partial E}{\\partial a_i} = 0, \\quad \\text{for } i = 1, 2, \\dots, p$$

This results in:
$$\\sum_n s[n - i] \\left( s[n] - \\sum_{k=1}^p a_k s[n-k] \\right) = 0$$
$$\\sum_{k=1}^p a_k \\sum_n s[n - k] s[n - i] = \\sum_n s[n] s[n - i]$$

Recognizing the **autocorrelation function** $R(i) = \\sum_n s[n] s[n - i]$, this becomes the celebrated **Yule-Walker Equations**:
$$\\sum_{k=1}^p a_k R(|i - k|) = R(i), \\quad i = 1, 2, \\dots, p$$

In matrix form:
$$\\begin{bmatrix} R(0) & R(1) & R(2) & \\dots & R(p-1) \\\\ R(1) & R(0) & R(1) & \\dots & R(p-2) \\\\ R(2) & R(1) & R(0) & \\dots & R(p-3) \\\\ \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\ R(p-1) & R(p-2) & R(p-3) & \\dots & R(0) \\end{bmatrix} \\begin{bmatrix} a_1 \\\\ a_2 \\\\ a_3 \\\\ \\vdots \\\\ a_p \\end{bmatrix} = \\begin{bmatrix} R(1) \\\\ R(2) \\\\ R(3) \\\\ \\vdots \\\\ R(p) \\end{bmatrix}$$

---

### 3. Solving via Levinson-Durbin Algorithm ($O(p^2)$)
The autocorrelation matrix above is a symmetric **Toeplitz matrix** (values along every diagonal are identical).
Normal matrix inversion takes slow $O(p^3)$ time. The **Levinson-Durbin Recursion** exploits the Toeplitz structure to solve for all $a_k$ in ultra-fast **$O(p^2)$ time**:
1. Initialize with zero error $E_0 = R(0)$.
2. For stage $m = 1$ to $p$:
   - Calculate reflection coefficient (PARCOR) $k_m$.
   - Update predictor coefficients: $a_m^{(m)} = k_m$, and $a_j^{(m)} = a_j^{(m-1)} - k_m a_{m-j}^{(m-1)}$.
   - Update error: $E_m = E_{m-1}(1 - k_m^2)$.

---

### 4. Evaluating LPC Effectiveness (Why is it so good?)
1. **Massive Data Compression:** Uncompressed 16-bit speech at 8 kHz takes $128\\text{ kbps}$. By sending only 10 LPC weights $a_k$, pitch period, and gain every 20 ms, LPC shrinks bitrate to just **$2.4\\text{ kbps}$ (over 50x compression!)**.
2. **Accurate Vocal Tract Formant Tracking:** The all-pole synthesis filter $H(z) = \\frac{G}{1 - \\sum a_k z^{-k}}$ matches the acoustic resonances of the human throat and mouth with near perfection.
3. **Low Computational Overhead:** Levinson-Durbin recursion runs easily on cheap, battery-powered microcontrollers in real time.
4. **Limitation:** LPC assumes speech is purely all-pole. It struggles to model nasal sounds (/m/, /n/) and unvoiced fricatives (/s/) that have acoustic zeros (spectral valleys)."""
    }
]
