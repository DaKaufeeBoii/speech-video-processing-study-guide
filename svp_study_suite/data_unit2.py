# -*- coding: utf-8 -*-
"""
Unit 2: Speech Feature Extraction, Pattern Matching & Acoustic Modeling
Questions: Mid-I Q9 to Q16
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408 | Dr. Sandeep Kumar M
Written in student-friendly, zero-jargon peer-tutor style with complete mathematical rigor.
"""

UNIT2_QUESTIONS = [
    {
        "id": "MID1-Q09",
        "mid": "Mid-I",
        "qno": 9,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K1",
        "marks": "05 Marks",
        "title": "Identify the key stages of a speech feature extraction pipeline and the purpose of each stage in converting speech signals into feature representations.",
        "punchline": "The pipeline turns raw audio waveforms into compact 39-D vectors through 6 logical stages: Pre-emphasis -> Framing -> Windowing -> FFT -> Cepstral extraction -> Dynamic Deltas.",
        "mnemonic": "P-F-W-F-C-D ('Please Filter Waves For Clean Data')",
        "analogy": "Like making espresso from fresh coffee beans: you roast the beans to bring out aroma (pre-emphasis), measure them into small doses (framing), smooth off the excess (windowing), extract the flavor profile (FFT), condense into a compact shot of espresso (cepstral features), and check how fast it flows into the cup (dynamic deltas).",
        "diagram": """Raw Speech s[n] ──► [ 1. Pre-Emphasis ]  (H(z) = 1 - 0.97 z⁻¹: Boosts quiet highs)
                            │
                            ▼
                     [ 2. Framing ]       (Chops speech into 20-30 ms stationary chunks)
                            │
                            ▼
                     [ 3. Windowing ]     (Hamming window tapers edges; stops leakage)
                            │
                            ▼
                     [ 4. FFT ]           (Converts time frame into magnitude spectrum |X[k]|)
                            │
                            ▼
                     [ 5. Feature Extr. ] (Mel Filterbank + DCT -> 13 Static MFCCs)
                            │
                            ▼
                     [ 6. Dynamic Deltas] (Calculates 13 Δ Velocity + 13 Δ² Acceleration)
                            │
                            ▼
                 Final Acoustic Vector: [ 13 Static + 13 Δ + 13 Δ² = 39-D Vector ]""",
        "content": """### 1. The Big Picture (Why Can't AI Just Listen to Raw Audio?)
A raw audio file is massive (16,000 numbers every second!) and filled with useless junk like background fan hiss, microphone clicks, and speaker pitch variations. 
The **feature extraction pipeline** cleans the audio, throws away the noise, and extracts a tidy **39-dimensional vector** every 10 milliseconds that tells speech AI (like Siri or Alexa) exactly what phoneme was just spoken.

---

### 2. The 6 Key Stages (Lecture 8 Breakdown)

#### Stage 1: Pre-Emphasis (Boosting the Quiet Highs)
* **What it does:** Runs speech through a simple first-order high-pass digital filter:
  $$y[n] = s[n] - 0.97 s[n-1] \\implies H(z) = 1 - 0.97 z^{-1}$$
* **Why we do it:** Human vocal cords naturally lose volume at high frequencies at a rate of $-6\\text{ dB/octave}$. Pre-emphasis boosts high frequencies by $+6\\text{ dB/octave}$, balancing the spectrum and preventing quiet consonants (/s/, /th/, /t/) from getting drowned out.

#### Stage 2: Framing (Chopping into Small Bites)
* **What it does:** Slices continuous speech into short overlapping chunks called **frames** of **20 to 30 ms** (e.g., 25 ms frame with 10 ms step).
* **Why we do it:** Over several seconds, human speech is wild and non-stationary. But within 20–30 ms, your physical mouth and tongue literally cannot move! Over that short instant, speech is **quasi-stationary**, making Fourier math valid.

#### Stage 3: Windowing (Tapering the Rough Edges)
* **What it does:** Multiplies each frame by a smooth bell-shaped **Hamming Window**:
  $$w[n] = 0.54 - 0.46 \\cos\\left(\\frac{2\\pi n}{N-1}\\right)$$
* **Why we do it:** Slicing speech abruptly creates sharp, unnatural cliff-edges at the borders. In frequency space, cliffs create fake ghost frequencies called **spectral leakage**. The Hamming window tapers the edges smoothly down to zero.

#### Stage 4: Fast Fourier Transform (FFT)
* **What it does:** Converts the windowed time samples into a discrete frequency spectrum $|X[k]|$.
* **Why we do it:** Speech meaning lives in the frequency domain (the formant resonance peaks), not the time domain squiggles.

#### Stage 5: Feature Extraction (Cepstral Analysis)
* **What it does:** Passes the spectrum through a bank of triangular Mel filters, takes the logarithm of energy, and runs a Discrete Cosine Transform (DCT) to get **13 static MFCCs** (or LPCs).
* **Why we do it:** It separates the vocal tract shape (what vowel was said) from the glottal pitch (who said it).

#### Stage 6: Dynamic Features (Deltas & Delta-Deltas)
* **What it does:** Calculates the first derivative ($\\Delta$, velocity) and second derivative ($\\Delta^2$, acceleration) across neighboring frames.
* **Why we do it:** Static features only capture a frozen photo; dynamic features capture how your mouth moves between words (transitions and coarticulation).

---

### 3. Quick Exam Summary Table
| Stage | Operation / Formula | What It Accomplishes |
| :--- | :--- | :--- |
| **1. Pre-emphasis** | $y[n] = s[n] - 0.97 s[n-1]$ | Boosts quiet high-frequency consonants |
| **2. Framing** | 20–30 ms chunks with 10 ms shift | Guarantees quasi-stationarity for FFT math |
| **3. Windowing** | Hamming window $w[n]$ | Eliminates frame boundary jumps & spectral leakage |
| **4. FFT** | Fast Fourier Transform | Converts time domain into frequency spectrum $|X[k]|$ |
| **5. Cepstrum** | Mel filterbank + Log + DCT | Generates 13 static MFCCs representing vocal tract shape |
| **6. Dynamics** | Delta ($\\Delta$) and Delta-Delta ($\\Delta^2$) | Adds speed and acceleration of vocal articulators |"""
    },
    {
        "id": "MID1-Q10",
        "mid": "Mid-I",
        "qno": 10,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Discuss the role of static and dynamic features in speech processing.",
        "punchline": "Static features are a single snapshot of mouth shape at one instant (13 numbers); dynamic features are the speed and acceleration of mouth muscles moving between frames (26 numbers). Concatenating both gives a 39-D vector.",
        "mnemonic": "Static = Snapshot of Shape; Dynamic = Direction & Drive over time.",
        "analogy": "Like sports photography: a still photo of a basketball player frozen mid-air (static feature) tells you who the player is; but consecutive frame differences showing jump speed and ball acceleration (dynamic features) tell you if they are taking a shot or landing from a rebound.",
        "diagram": """Frame t-1                    Frame t                    Frame t+1
┌──────────────┐             ┌──────────────┐             ┌──────────────┐
│ c[t-1]       │             │ c[t]         │             │ c[t+1]       │
└──────┬───────┘             └──────┬───────┘             └──────┬───────┘
       │                            │                            │
       └────────────────────────────┼────────────────────────────┘
                                    │
                  ┌─────────────────┴─────────────────┐
                  ▼                                   ▼
        STATIC FEATURES c[t]                 DYNAMIC FEATURES
        • 13 MFCC coefficients               • 13 Velocity Deltas (Δc)
        • Instant vocal tract shape          • 13 Acceleration Deltas (Δ²c)
        • Identifies vowels                  • Captures transitions & coarticulation
                  │                                   │
                  └─────────────────┬─────────────────┘
                                    ▼
         Combined 39-D Acoustic Vector: [ c[t] | Δc[t] | Δ²c[t] ]""",
        "content": """### 1. The Big Picture (Why One Frame is Not Enough)
When people speak, they don't produce isolated robotic beeps. Sounds blend smoothly into each other — a phenomenon called **coarticulation**. 
For an AI to transcribe continuous speech, it needs to know two distinct things:
1. **What does the mouth shape look like right now?** $\\implies$ **Static Features**
2. **How fast and in what direction is the mouth moving?** $\\implies$ **Dynamic Features**

---

### 2. Static Features (The Instantaneous Snapshot)
* **What they are:** Features extracted from a single, isolated 20–30 ms frame (like MFCCs or LPCs).
* **What they represent:** The physical shape of the vocal tract (where the tongue and lips are positioned right at this millisecond) and the formant resonances.
* **Size:** Typically **12 to 13 coefficients** ($c_1, c_2, \\dots, c_{13}$).
* **Limitation:** Static features alone are deaf to motion. A vowel /u/ looks identical whether the speaker is transitioning into it or out of it.

---

### 3. Dynamic Features (The Velocity & Acceleration)
* **What they are:** Time derivatives calculated across a small window of neighboring frames:
  1. **Delta ($\\Delta$) Features (First Derivative / Velocity):**
     Measures the **rate of change** of static coefficients over time:
     $$\\Delta c_t = \\frac{\\sum_{\\tau=1}^M \\tau (c_{t+\\tau} - c_{t-\\tau})}{2 \\sum_{\\tau=1}^M \\tau^2}$$
  2. **Delta-Delta ($\\Delta^2$) Features (Second Derivative / Acceleration):**
     Measures the **acceleration** of spectral change by taking the derivative of the deltas:
     $$\\Delta^2 c_t = \\frac{\\sum_{\\tau=1}^M \\tau (\\Delta c_{t+\\tau} - \\Delta c_{t-\\tau})}{2 \\sum_{\\tau=1}^M \\tau^2}$$
* **Why they are amazing:** They capture phonetic transitions (like going from a stop /t/ to a vowel /a/) and filter out static microphone background hum!

---

### 4. Cheat Sheet Comparison Table (Lecture 7)
| Feature Property | Static Features | Dynamic Features ($\\Delta$ and $\\Delta^2$) |
| :--- | :--- | :--- |
| **Meaning** | Instantaneous mouth shape & formant envelope | Velocity and acceleration of moving vocal organs |
| **Scope** | Single isolated time frame (25 ms) | Temporal trajectory across multiple frames |
| **Information** | *What* sound is being made | *How* the sound is changing over time |
| **Dimensions** | 13 dimensions ($c_0$ to $c_{12}$) | 26 dimensions ($13\\ \\Delta + 13\\ \\Delta^2$) |
| **Noise Vulnerability** | Sensitive to constant microphone / channel bias | Highly robust (time-differentiation cancels constant DC offsets) |
| **Combined Total** | \\multicolumn{2}{c|}{\\textbf{13 Static + 13 Velocity + 13 Acceleration = 39-D Acoustic Vector}} |"""
    },
    {
        "id": "MID1-Q11",
        "mid": "Mid-I",
        "qno": 11,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "A signal has 1600 samples, frame size = 400 samples, overlap = 200 samples. Find the number of frames.",
        "punchline": "Frame shift is S = 400 - 200 = 200 samples. Total frames = floor((1600 - 400)/200) + 1 = 6 + 1 = exactly 7 frames!",
        "mnemonic": "Frames = [(Total - Length) / Shift] + 1",
        "analogy": "Like laying 400-meter track carpets on a 1600-meter straightaway where every new carpet starts 200 meters after the last one: Carpet 1 covers 0-400m, Carpet 2 covers 200-600m... and Carpet 7 perfectly lands at 1200-1600m. Exactly 7 carpets!",
        "diagram": """Sample Scale:
0          200        400        600        800        1000       1200       1400       1600
├─── 200 ───┼─── 200 ───┼─── 200 ───┼─── 200 ───┼─── 200 ───┼─── 200 ───┼─── 200 ───┼─── 200 ───┤
[=== Frame 1: 0 - 400 ===]
            [=== Frame 2: 200 - 600 ===]
                        [=== Frame 3: 400 - 800 ===]
                                    [=== Frame 4: 600 - 1000 ===]
                                                [=== Frame 5: 800 - 1200 ===]
                                                            [=== Frame 6: 1000 - 1400 ===]
                                                                        [=== Frame 7: 1200 - 1600 ===]

Hop Size (Shift S) = 200 samples
Total Frames = 7 (Perfect integer fit!)""",
        "content": """### 1. The Given Numbers
* Total number of samples ($N$): $1600\\text{ samples}$
* Frame size / Frame length ($L$): $400\\text{ samples}$
* Overlap between adjacent frames ($O$): $200\\text{ samples}$

---

### 2. Step 1: Calculate the Frame Shift (Hop Size $S$)
The **frame shift** $S$ is how many new, non-overlapping samples we jump forward to start the next frame:
$$S = L - O$$
$$S = 400 - 200 = \\mathbf{200\\text{ samples}}$$

---

### 3. Step 2: Use the Standard Framing Formula
The formula for the total number of frames extracted from a discrete signal is:
$$N_{\\text{frames}} = \\left\\lfloor \\frac{N - L}{S} \\right\\rfloor + 1$$

Substitute the given numbers:
$$N_{\\text{frames}} = \\left\\lfloor \\frac{1600 - 400}{200} \\right\\rfloor + 1$$
$$N_{\\text{frames}} = \\left\\lfloor \\frac{1200}{200} \\right\\rfloor + 1$$
$$N_{\\text{frames}} = 6 + 1 = \\mathbf{7\\text{ frames}}$$

---

### 4. Frame-by-Frame Proof (Show This in Exam for Guaranteed 5/5)
| Frame Number | Sample Range (0-indexed) | Sample Range (1-indexed) | Samples Covered |
| :---: | :---: | :---: | :---: |
| **Frame 1** | $0$ to $399$ | $1$ to $400$ | $400\\text{ samples}$ |
| **Frame 2** | $200$ to $599$ | $201$ to $600$ | $400\\text{ samples}$ |
| **Frame 3** | $400$ to $799$ | $401$ to $800$ | $400\\text{ samples}$ |
| **Frame 4** | $600$ to $999$ | $601$ to $1000$ | $400\\text{ samples}$ |
| **Frame 5** | $800$ to $1199$ | $801$ to $1200$ | $400\\text{ samples}$ |
| **Frame 6** | $1000$ to $1399$ | $1001$ to $1400$ | $400\\text{ samples}$ |
| **Frame 7** | $1200$ to $1599$ | $1201$ to $1600$ | $400\\text{ samples}$ |

### Final Answer:
$$\\mathbf{Total\\ Number\\ of\\ Frames = 7}$$"""
    },
    {
        "id": "MID1-Q12",
        "mid": "Mid-I",
        "qno": 12,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Compare LPCC and MFCC features in terms of spectral representation and robustness for speech recognition applications.",
        "punchline": "LPCC models speech like a rigid mechanical throat pipe (fragile in background noise); MFCC models speech like the human ear (super robust to noise and the world standard for speech recognition).",
        "mnemonic": "LPCC = Production & Poles; MFCC = Perception & Mel Filters.",
        "analogy": "LPCC is like trying to guess what a flute sounds like by measuring the wooden tube dimensions with calipers; MFCC is like recording the sound and analyzing how human eardrum hair cells actually vibrate.",
        "diagram": """LPCC PIPELINE (Speech Production Model)
Speech ──► Autocorrelation ──► LPC Predictor (ak) ──► Cepstral Recursion ──► LPCC
           (Linear frequency scale, sensitive to noise & pitch harmonics)

MFCC PIPELINE (Human Auditory Model)
Speech ──► FFT Spectrum ──► Mel Filterbank (26-40) ──► Logarithm ──► DCT ──► MFCC
           (Non-linear Mel scale, noise-robust, decorrelated features)""",
        "content": """### 1. The Big Picture (Two Different Philosophies)
In speech AI, researchers tried two completely different paths to represent sound:
1. **LPCC (Linear Predictive Cepstral Coefficients):** Based on the **Speech Production System** (vocal tract acoustics).
2. **MFCC (Mel-Frequency Cepstral Coefficients):** Based on the **Human Auditory Perception System** (how the human ear hears).

---

### 2. Spectral Representation Differences
* **LPCC Representation:**
  - Assumes the vocal tract is an all-pole linear acoustic filter $H(z) = \\frac{G}{1 - \\sum a_k z^{-k}}$.
  - Treats all frequencies equally on a **uniform linear scale**.
  - Derives cepstral coefficients recursively from LPC coefficients $a_k$:
    $$c_n = a_n + \\sum_{k=1}^{n-1} \\left(\\frac{k}{n}\\right) c_k a_{n-k}$$
* **MFCC Representation:**
  - Uses the non-linear **Mel scale**: $\\text{Mel}(f) = 2595 \\log_{10}(1 + f/700)$.
  - Groups frequencies using overlapping triangular filters (narrow at low frequencies, wide at high frequencies).
  - Applies a Discrete Cosine Transform (DCT) to produce completely decorrelated orthogonal features.

---

### 3. Robustness in Speech Recognition (Why MFCC Won the War)
* **Noise Sensitivity:**
  - **LPCC is terrible in noise:** Background noise ruins the autocorrelation matrix, causing the LPC all-pole filter to hallucinate fake formant peaks that aren't there.
  - **MFCC is highly robust:** Integrating energy over triangular filterbanks smooths out narrowband microphone noise spikes.
* **Pitch Dependency:**
  - LPCC gets easily confused by high-pitched female or child voices because pitch harmonics ($F_0$) interfere with vocal tract poles.
  - MFCC smooths over individual pitch harmonics, leaving only the phoneme identity.

---

### 4. Cheat Sheet Comparison Table (Lecture 9)
| Parameter | LPCC | MFCC |
| :--- | :--- | :--- |
| **Core Inspiration** | **Speech Production:** Acoustic tube physics | **Speech Perception:** Human cochlea / auditory system |
| **Frequency Scale** | Strict **linear scale** everywhere | **Mel scale:** Dense below 1 kHz, log above 1 kHz |
| **Noise Robustness** | **Poor:** Autocorrelation fails in noise | **High:** Filterbank integration suppresses noise |
| **Pitch Sensitivity** | High (High pitch harmonics distort poles) | Low (Bandpass smoothing eliminates pitch bias) |
| **Coefficients** | Correlated LPC cepstral recursion | Decorrelated via Discrete Cosine Transform (DCT) |
| **Primary Use Today**| Low-bitrate vocoders & speech synthesis | **Modern Speech Recognition (ASR), Alexa, Siri** |"""
    },
    {
        "id": "MID1-Q13",
        "mid": "Mid-I",
        "qno": 13,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K4",
        "marks": "10 Marks",
        "title": "Discuss different distance measures (Euclidean, Mahalanobis, and DTW) and evaluate their role in speech pattern matching and recognition systems.",
        "punchline": "Euclidean is straight-line distance (fast but dumb); Mahalanobis scales by feature spread and correlation (smart but heavy); DTW warps time on a dynamic grid to match fast and slow talkers.",
        "mnemonic": "E-M-D: Euclidean for speed, Mahalanobis for covariance, DTW for time warping.",
        "analogy": "Comparing two singers singing 'Hello': Euclidean compares them frame-by-frame and fails if one singer holds the 'o' a split-second longer; Mahalanobis checks if their vocal textures match statistically; DTW stretches and squeezes the audio timeline like an elastic rubber band so every syllable syncs up perfectly.",
        "diagram": """1. EUCLIDEAN DISTANCE (Straight Line):
   d(x, y) = √[ Σ (x_i - y_i)² ]
   Fast O(D), but assumes all features are independent and equally spread out.

2. MAHALANOBIS DISTANCE (Covariance-Weighted):
   d_M(x, y) = √[ (x - y)ᵀ Σ⁻¹ (x - y) ]
   Weighs distance inversely by feature variance and cancels inter-feature correlation.

3. DYNAMIC TIME WARPING (DTW Non-linear Time Alignment):
   Template J ▲                       Warping Path W(k)
              │                                   ┌───• (I, J)
              │                           ┌───────┘
              │                   ┌───────┘  • Stretches fast syllables
              │           ┌───────┘          • Squeezes slow syllables
           1  │  •────────┘                  • Solves isolated word recognition!
              └──────────────────────────────►
                 1                         I   Input Speech Frames""",
        "content": """### 1. The Big Picture (How Speech Pattern Matching Works)
In speech recognition, after extracting feature vectors (like MFCCs), we need to compare an unknown spoken word against a stored template. 
Because human voices have different volumes, correlations, and speaking speeds, choosing the right **distance metric** makes or breaks the system.

---

### 2. Euclidean Distance (The Straight-Line Metric)
* **Formula:**
  $$d_E(\\mathbf{x}, \\mathbf{y}) = \\sqrt{\\sum_{i=1}^D (x_i - y_i)^2}$$
* **Role in Speech:** Used in **Vector Quantization (VQ)** and fast nearest-neighbor codebook searches.
* **Evaluation:**
  - *Pros:* Super simple and blazing fast ($O(D)$ time complexity). Perfect for low-power microcontrollers.
  - *Cons:* Assumes all feature dimensions are independent and have equal variance. If one feature has huge numbers (like energy) and another has tiny numbers (like high cepstral coefficients), energy completely bullies the other features!

---

### 3. Mahalanobis Distance (The Statistically Smart Metric)
* **Formula:**
  $$d_M(\\mathbf{x}, \\mathbf{y}) = \\sqrt{(\\mathbf{x} - \\mathbf{y})^T \\mathbf{\\Sigma}^{-1} (\\mathbf{x} - \\mathbf{y})}$$
  where $\\mathbf{\\Sigma}$ is the feature covariance matrix.
* **Role in Speech:** Fundamental metric in **Gaussian Mixture Models (GMMs)** and statistical classifiers.
* **Evaluation:**
  - *Pros:* **Scale-invariant** (normalizes features with large vs small variances) and **decorrelates axes** (ignores redundant shared information).
  - *Cons:* Requires calculating and inverting a $D \\times D$ covariance matrix ($O(D^3)$ time), which can become unstable if you don't have enough training data.

---

### 4. Dynamic Time Warping (DTW - The Time-Bender)
* **Why it's needed:** If you say "STOP" in 0.5 seconds and I say "STOOOP" in 1.2 seconds, Euclidean distance fails completely because the vectors don't line up.
* **How it works:** DTW creates a 2D grid between Input frames ($1 \\dots I$) and Template frames ($1 \\dots J$). It uses dynamic programming to find the optimal winding path that minimizes cumulative distance:
  $$D(i, j) = d(x_i, y_j) + \\min \\begin{cases} D(i-1, j) & (\\text{Time expansion}) \\\\ D(i-1, j-1) & (\\text{Diagonal step}) \\\\ D(i, j-1) & (\\text{Time compression}) \\end{cases}$$
* **Evaluation:**
  - *Pros:* Handles speaking speed differences seamlessly. Gold standard for small-vocabulary isolated word recognition.
  - *Cons:* Computationally heavy ($O(I \\cdot J \\cdot D)$). Doesn't scale well to 100,000-word continuous speech.

---

### 5. Cheat Sheet Comparison Table (Lecture 11)
| Property | Euclidean Distance | Mahalanobis Distance | Dynamic Time Warping (DTW) |
| :--- | :--- | :--- | :--- |
| **Operates On** | Single frame vector | Single frame vector | Sequence of temporal frames |
| **Handles Feature Spread?**| No (assumes equal variance) | **Yes** (normalizes by variance) | Depends on underlying local metric |
| **Handles Time Variations?**| No (lengths must be identical) | No | **Yes** (non-linear warping alignment) |
| **Complexity** | $O(D)$ — Fastest | $O(D^2)$ to $O(D^3)$ | $O(I \\cdot J \\cdot D)$ — Computationally heavy |
| **Best Speech Use** | VQ codebook clustering | GMM acoustic modeling | Isolated voice commands & word matching |"""
    },
    {
        "id": "MID1-Q14",
        "mid": "Mid-I",
        "qno": 14,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Evaluate the performance of vector quantization models in speech recognition and justify codebook optimization strategies.",
        "punchline": "VQ compresses millions of continuous feature vectors into a finite dictionary of 256 codewords; the Linde-Buzo-Gray (LBG) centroid-splitting algorithm optimizes this codebook to minimize distortion.",
        "mnemonic": "L-S-T-D-S-I-A (LBG, Size, Training data, Distance metric, Split/merge, Initialization, Adaptive).",
        "analogy": "Think of a 256-color palette in an old video game: instead of storing 16 million complex colors, every pixel is snapped to the nearest color in the palette. If the palette is optimized using clustering (LBG), the picture stays crisp and memory drops 90%.",
        "diagram": """CONTINUOUS FEATURE SPACE               DISCRETE CODEBOOK C = {y₁, y₂, y₃, y₄}
      x₂ ▲                                   ┌───────────────────────────┐
         │    • x (Input vector)             │ Codeword y₁: [0.24, 0.81] │
         │     \\                             │ Codeword y₂: [0.72, 0.35] │
         │      \\ Euclidean distance         │ Codeword y₃: [-0.4, 0.12] │
         │   ┌───▼───┐                       │ Codeword y₄: [0.15, -0.6] │
         │   │  y₁   │ (Nearest Centroid)    └───────────────────────────┘
         │   └───┬───┘                                     ▲
         │       ▼                                         │
         │    Index 1 transmitted                          │
         └────────────────────────► x₁                     │
                                                           │
 LINDE-BUZO-GRAY (LBG) CENTROID-SPLITTING:                 │
 [ 1 Centroid ] ──► Split y ± ε ──► [ 2 Centroids ] ───────┘
       │
       ▼
 Voronoi Partitioning & Re-centering until ΔDistortion < Threshold""",
        "content": """### 1. The Big Picture (What is Vector Quantization?)
In speech recognition, an audio file produces thousands of continuous 39-D feature vectors. Storing and searching through all of them is slow and eats up memory.
**Vector Quantization (VQ)** compresses this continuous cloud of vectors into a small, discrete dictionary called a **codebook** $\\mathcal{C} = \\{\\mathbf{y}_1, \\mathbf{y}_2, \\dots, \\mathbf{y}_K\\}$. Each representative prototype vector is called a **codeword**.
Whenever a new feature vector $\\mathbf{x}$ arrives, we simply look up its nearest codeword and transmit its integer index:
$$\\mathbf{y}^* = \\arg\\min_{\\mathbf{y}_k \\in \\mathcal{C}} \\|\\mathbf{x} - \\mathbf{y}_k\\|^2$$

---

### 2. Comprehensive Performance Evaluation of VQ (Lecture 10)
* **a) Recognition Accuracy:** Works well for small vocabularies (e.g., 10 isolated digits) and single-speaker systems ($>95\\%$ accuracy). However, accuracy drops on large vocabularies because discrete codewords discard fine spectral nuances.
* **b) Computational Efficiency:** Blazingly fast! Matching only requires simple Euclidean distance checks. Ideal for embedded microcontrollers and wearable tech.
* **c) Memory Footprint:** Requires saving only the $K$ codebook vectors (e.g., 128 vectors $\\times$ 13 numbers $\\approx$ a few kilobytes of RAM).
* **d) Noise Sensitivity:** Sensitive to noise. A small amount of static noise can push a feature vector across a Voronoi boundary, causing a completely wrong codeword lookup.
* **e) Limitations:** VQ performs **hard clustering** (no probability scores) and has **zero temporal modeling** (it treats speech like an unordered bag of vectors).

---

### 3. Codebook Optimization Strategies (How to Make VQ Great)

#### 1. The Linde-Buzo-Gray (LBG) Algorithm (The Gold Standard)
LBG is an iterative clustering algorithm that builds an optimal codebook of size $K = 2^B$ starting from a single centroid:
1. **Initialize:** Compute the single global centroid $\\mathbf{c}_0$ of the entire training dataset.
2. **Split:** Double the codebook size by splitting each centroid into two: $\\mathbf{c}_k^+ = \\mathbf{c}_k(1 + \\epsilon)$ and $\\mathbf{c}_k^- = \\mathbf{c}_k(1 - \\epsilon)$.
3. **Classify:** Assign every training vector to its nearest centroid (Voronoi partitioning).
4. **Update:** Recalculate each centroid as the average of all vectors assigned to it.
5. **Iterate:** Repeat until distortion reduction $\\frac{D_{\\text{old}} - D_{\\text{new}}}{D_{\\text{old}}} < \\delta$.

#### 2. Optimal Codebook Size Selection ($K$)
- Too small ($K=16$): High distortion, sounds muddy.
- Too large ($K=1024$): Huge memory, slow search, overfits to noise.
- Sweet spot: $K = 64$ to $256$ for speech recognition.

#### 3. Training Data Diversity
Train on diverse accents, male/female speakers, and noisy conditions so codewords generalize well.

#### 4. K-Means++ Smart Initialization
Instead of random initial guesses, K-means++ spreads initial seeds far apart probabilistically, speeding up convergence and avoiding local traps.

#### 5. Adaptive Codebooks
Dynamically update codewords on the fly using running averages as a user speaks, adapting to microphone drift."""
    },
    {
        "id": "MID1-Q15",
        "mid": "Mid-I",
        "qno": 15,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Design a Gaussian Mixture Model (GMM) for speech feature distribution and explain how the Expectation-Maximization (EM) algorithm is used for parameter estimation.",
        "punchline": "A GMM models complex speech feature distributions as a weighted sum of M smooth Gaussian bell curves; the Expectation-Maximization (EM) algorithm iterates between calculating soft responsibilities (E-step) and updating weights, means, and variances (M-step).",
        "mnemonic": "GMM = Weights, Means, Variances (W-M-V). EM = E-step (Responsibilities), M-step (Update parameters).",
        "analogy": "Imagine mapping the altitude of a mountain range with multiple peaks: instead of trying to draw one crazy complex formula, you represent the mountains as a blend of 3 smooth bell-shaped hills (Gaussians) of different heights (weights), peak positions (means), and widths (variances).",
        "diagram": """MULTI-MODAL SPEECH DISTRIBUTION p(x|λ):
       ▲ Probability Density
       │                    Component 2: w₂ N(x|μ₂, Σ₂)
       │                              /---\\
       │       Component 1: w₁ N(μ₁,Σ₁)│     │
       │                  /---\\        │     │
       │                 /     \\       │     │        Component 3: w₃ N(μ₃,Σ₃)
       │   ---\\         /       \\      /     \\                 /---\\
       └──┴────┴───────┴─────────┴────┴───────┴───────────────┴─────┴──────► x

THE EM ALGORITHM LOOP:
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. INITIALIZE: K-means clustering provides initial weights w_k, μ_k, Σ_k    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 2. E-STEP (Expectation):                                                    │
│    Calculate soft responsibility γ_tk:                                      │
│    What is the probability that Gaussian k produced sample x_t?             │
│    γ_tk = [ w_k N(x_t | μ_k, Σ_k) ] / Σ_j [ w_j N(x_t | μ_j, Σ_j) ]         │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ 3. M-STEP (Maximization):                                                   │
│    Update parameters using responsibilities as weights:                     │
│    • Weight:  ŵ_k = (1/T) Σ γ_tk                                            │
│    • Mean:    μ̂_k = [ Σ γ_tk · x_t ] / [ Σ γ_tk ]                           │
│    • Variance: σ̂_kd² = [ Σ γ_tk · (x_td - μ̂_kd)² ] / [ Σ γ_tk ]             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                Check Convergence: Δ Log-Likelihood < ε?
                        │ No                           │ Yes
                        └──────────────────────────────┴──► Optimal GMM!""",
        "content": """### 1. The Big Picture (Why GMMs in Speech?)
In speech, the acoustic features of a phoneme (like vowel /a/) don't follow a simple single bell curve because different people say it with different vocal tract lengths and emotional tones.
A **Gaussian Mixture Model (GMM)** solves this by modeling the probability density as a **weighted blend of $M$ smooth Gaussian bell curves**:
$$p(\\mathbf{x}|\\lambda) = \\sum_{k=1}^M w_k \\, \\mathcal{N}(\\mathbf{x} | \\boldsymbol{\\mu}_k, \\mathbf{\\Sigma}_k)$$

---

### 2. The GMM Parameters (The Trio $\\lambda$)
Every GMM is defined by three parameter sets:
$$\\lambda = \\{w_k, \\boldsymbol{\\mu}_k, \\mathbf{\\Sigma}_k\\}_{k=1}^M$$
1. **$w_k$ (Mixture Weights):** The prior probability or importance of each Gaussian. Must satisfy $\\sum_{k=1}^M w_k = 1$ and $w_k \\ge 0$.
2. **$\\boldsymbol{\\mu}_k$ (Mean Vector):** The 39-D center point of each Gaussian peak.
3. **$\\mathbf{\\Sigma}_k$ (Covariance Matrix):** The spread and shape of each peak. In speech ASR, we universally use **diagonal covariance matrices** (assuming cepstral dimensions are decorrelated by DCT).

Each Gaussian component formula is:
$$\\mathcal{N}(\\mathbf{x} | \\boldsymbol{\\mu}_k, \\mathbf{\\Sigma}_k) = \\frac{1}{(2\\pi)^{D/2} |\\mathbf{\\Sigma}_k|^{1/2}} \\exp\\left( -\\frac{1}{2}(\\mathbf{x} - \\boldsymbol{\\mu}_k)^T \\mathbf{\\Sigma}_k^{-1} (\\mathbf{x} - \\boldsymbol{\\mu}_k) \\right)$$

---

### 3. The Expectation-Maximization (EM) Algorithm (Step-by-Step)
We want to find parameters $\\lambda$ that maximize the total training log-likelihood $\\sum_t \\log p(\\mathbf{x}_t|\\lambda)$. But because the sum is inside the logarithm, direct calculus fails!
The **EM algorithm** solves this iteratively:

#### Step 1: Initialization
Use K-means clustering on training vectors to set initial cluster centers $\\boldsymbol{\\mu}_k$, variances $\\mathbf{\\Sigma}_k$, and weights $w_k$.

#### Step 2: The E-Step (Expectation / Guessing Responsibilities)
For every training vector $\\mathbf{x}_t$ and every Gaussian $k$, calculate the **posterior responsibility** $\\gamma_{tk}$ (the probability that Gaussian $k$ is responsible for generating sample $\\mathbf{x}_t$):
$$\\gamma_{tk} = \\frac{w_k \\mathcal{N}(\\mathbf{x}_t | \\boldsymbol{\\mu}_k, \\mathbf{\\Sigma}_k)}{\\sum_{j=1}^M w_j \\mathcal{N}(\\mathbf{x}_t | \\boldsymbol{\\mu}_j, \\mathbf{\\Sigma}_j)}$$
*(This is a "soft assignment" between 0.0 and 1.0).*

#### Step 3: The M-Step (Maximization / Updating Parameters)
Re-estimate the GMM parameters using the soft responsibility weights:
* **New Weight:**
  $$\\hat{w}_k = \\frac{1}{T} \\sum_{t=1}^T \\gamma_{tk}$$
* **New Mean:**
  $$\\hat{\\boldsymbol{\\mu}}_k = \\frac{\\sum_{t=1}^T \\gamma_{tk} \\mathbf{x}_t}{\\sum_{t=1}^T \\gamma_{tk}}$$
* **New Variance (Diagonal):**
  $$\\hat{\\sigma}_{kd}^2 = \\frac{\\sum_{t=1}^T \\gamma_{tk} (x_{td} - \\hat{\\mu}_{kd})^2}{\\sum_{t=1}^T \\gamma_{tk}}$$

#### Step 4: Check Convergence
Calculate total log-likelihood $\\mathcal{L} = \\sum_t \\log p(\\mathbf{x}_t | \\lambda)$. If the improvement $\\Delta \\mathcal{L} < 10^{-4}$, stop! Otherwise, loop back to the E-Step.
*Dempster, Laird, and Rubin proved mathematically that every EM iteration is guaranteed to increase or maintain likelihood without oscillating!*"""
    },
    {
        "id": "MID1-Q16",
        "mid": "Mid-I",
        "qno": 16,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Construct a Hidden Markov Model (HMM) for continuous speech recognition and assess its capability in modeling temporal variability of speech signals.",
        "punchline": "An HMM is a doubly stochastic model: a hidden Markov chain transitions between phonetic mouth states over time, while output GMMs generate acoustic spectra; self-loops absorb fast and slow speech speeds effortlessly.",
        "mnemonic": "HMM = (A, B, π). Solved via: Forward (Eval), Viterbi (Decode), Baum-Welch (Train).",
        "analogy": "Like an underground subway train moving through 3 stations: Onset -> Middle -> End. You can't see the tracks (hidden states), but at each station the conductor rings a bell (emission probability). Fast trains stay 1 second at each station; slow trains stay 5 seconds (self-loops), but both visit the exact same stations in order!",
        "diagram": """3-STATE LEFT-TO-RIGHT (BAKIS) HMM TOPOLOGY:
               a₁₁                     a₂₂                     a₃₃
             ┌─────┐                 ┌─────┐                 ┌─────┐
             │  ▼  │                 │  ▼  │                 │  ▼  │
           ┌─┴─────┴─┐     a₁₂     ┌─┴─────┴─┐     a₂₃     ┌─┴─────┴─┐
   π₁=1.0  │         │────────────►│         │────────────►│         │ ──► To Next
  ────────►│ State 1 │             │ State 2 │             │ State 3 │     Phoneme
           │ (Onset) │────────────►│(Nucleus)│             │ (Coda)  │
           └────┬────┘    a₁₃      └────┬────┘             └────┬────┘
                │                       │                       │
                ▼ b₁(x_t)               ▼ b₂(x_t)               ▼ b₃(x_t)
            [  GMM  ]               [  GMM  ]               [  GMM  ]
                │                       │                       │
           Acoustic Vector         Acoustic Vector         Acoustic Vector
              x₁, x₂                  x₃, x₄, x₅               x₆, x₇

 ABSORBING TEMPORAL VARIABILITY:
 • Fast talker:  Spends 1 frame per state (transitions immediately via a₁₂, a₂₃).
 • Slow talker:  Dwells 5+ frames in each state (absorbed seamlessly by self-loops a₁₁, a₂₂, a₃₃).""",
        "content": """### 1. The Big Picture (What is an HMM in Speech?)
Human speech has two random things happening at once (a **doubly stochastic process**):
1. **The Hidden Layer:** A sequence of physical articulatory states (moving from phone onset $\\to$ steady vowel $\\to$ coda). You cannot directly see this state.
2. **The Observable Layer:** The acoustic sound wave (MFCC vectors) produced at each state, which we measure with a microphone.

---

### 2. Constructing the HMM Model Elements: $\\lambda = (\\mathbf{A}, \\mathbf{B}, \\boldsymbol{\\pi})$
To construct an HMM for continuous speech, define 5 components:
1. **Hidden States $S = \\{S_1, S_2, S_3\\}$:**
   In speech, every phoneme is modeled using a **3-state Left-to-Right (Bakis) topology**:
   - $S_1$: Phone **onset** (transition from previous sound).
   - $S_2$: Phone **nucleus** (steady-state core vowel sound).
   - $S_3$: Phone **coda** (transition to next sound).
2. **Transition Probability Matrix $\\mathbf{A} = \\{a_{ij}\\}$:**
   Probability of moving from state $S_i$ to $S_j$:
   $$a_{ij} = P(q_{t+1} = S_j | q_t = S_i)$$
   Because human speech only moves forward in time, $a_{ij} = 0$ for all $j < i$ (no backward time travel!).
3. **Emission Probability Distribution $\\mathbf{B} = \\{b_j(\\mathbf{x}_t)\\}$:**
   Probability that state $S_j$ generates the observed acoustic vector $\\mathbf{x}_t$, modeled using a GMM:
   $$b_j(\\mathbf{x}_t) = \\sum_{k=1}^M w_{jk} \\mathcal{N}(\\mathbf{x}_t | \\boldsymbol{\\mu}_{jk}, \\mathbf{\\Sigma}_{jk})$$
4. **Initial State Distribution $\\boldsymbol{\\pi}$:**
   $$\\boldsymbol{\\pi} = [1.0, 0, 0]^T \\quad (\\text{Speech always starts at State 1!})$$
5. **Continuous Speech Concatenation:**
   Sentence HMMs are built by stringing phoneme HMMs together:
   $$\\text{Word HMM} = \\text{Phone}_1 \\circ \\text{Phone}_2 \\circ \\text{Phone}_3$$

---

### 3. The 3 Fundamental HMM Problems (Exam Gold!)
| Problem | Goal | Algorithm Used | Complexity |
| :--- | :--- | :--- | :--- |
| **1. Evaluation** | Given audio $\\mathbf{O}$ and model $\\lambda$, compute likelihood $P(\\mathbf{O}|\\lambda)$ | **Forward-Backward Algorithm** | $O(N^2 T)$ |
| **2. Decoding** | Given audio $\\mathbf{O}$, find the best hidden state sequence $Q^*$ (word spoken) | **Viterbi Algorithm** (Dynamic Programming) | $O(N^2 T)$ |
| **3. Training** | Given lots of speech recordings, train parameters $(\\mathbf{A}, \\mathbf{B}, \\boldsymbol{\\pi})$ | **Baum-Welch Algorithm** (EM for HMMs) | Monotonic convergence |

---

### 4. How HMMs Master Temporal Variability (Why It Works So Well)
People speak fast when excited and slow when bored. How does an HMM handle this without crashing?
1. **Self-Loops ($a_{ii}$):** Each state has a self-transition probability $a_{ii}$. The time spent in state $S_i$ follows a geometric distribution with mean duration $\\bar{d} = \\frac{1}{1 - a_{ii}}$. A slow speaker simply loops on $a_{ii}$ for 8 frames, while a fast speaker loops for 2 frames!
2. **Non-Linear Viterbi Alignment:** The Viterbi trellis dynamically warps the time axis to find the highest-probability path regardless of speaking speed.
3. **Triphone Context Modeling:** To handle coarticulation, we build context-dependent triphones ($l-eh+f$ means vowel /eh/ with /l/ on the left and /f/ on the right)."""
    }
]
