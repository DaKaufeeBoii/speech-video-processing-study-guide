# -*- coding: utf-8 -*-
"""
Unit 2: Speech Feature Extraction, Pattern Matching & Acoustic Modeling
Questions: Mid-I Q9 to Q16
Academic Year: 2026-27 | Regulation: KGR23 | Course Code: KG23ACM408
Scaled strictly for exam success (05 Marks vs 10 Marks format).
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
        "punchline": "The pipeline converts raw audio into compact, decorrelated acoustic vectors through 7 sequential stages: Pre-emphasis -> Framing -> Windowing -> FFT -> Mel Filter Bank -> Log -> DCT.",
        "mnemonic": "P-F-W-F-M-L-D: Pre-emphasis, Framing, Windowing, FFT, Mel Filterbank, Logarithm, DCT",
        "analogy": "Like an automated coffee bean processor: Raw beans are sorted (framing), cleaned of debris (windowing), roasted into aroma profiles (FFT/Mel filters), and ground into compact espresso pucks (DCT cepstrum).",
        "diagram": """Raw Speech s(t) ──► [ ADC / Sampler (16 kHz) ]
                             │
                             ▼
                    [ 1. Pre-Emphasis Filter ]  (H(z) = 1 - 0.97 z^-1)
                             │
                             ▼
                    [ 2. Frame Blocking ]       (20-30 ms frames, 50% overlap)
                             │
                             ▼
                    [ 3. Windowing (Hamming) ]  (Eliminates edge leakage)
                             │
                             ▼
                    [ 4. FFT Spectral Analysis] (Magnitude Spectrum |X[k]|)
                             │
                             ▼
                    [ 5. Mel Filter Bank ]      (26-40 Triangular Filters)
                             │
                             ▼
                    [ 6. Log Energy ]           (Perceptual loudness compression)
                             │
                             ▼
                    [ 7. DCT / Cepstrum ]       (Orthogonal decorrelation -> MFCCs)
                             │
                             ▼
         [ Feature Vector: 13 Static + 13 Δ + 13 ΔΔ = 39 Dimensions ]""",
        "content": """### 1. Purpose of Feature Extraction
A raw speech waveform contains enormous redundant information (speaker pitch, background noise, phase details) alongside the essential phonetic content. The feature extraction pipeline extracts a compact, time-synchronous acoustic vector (e.g., MFCCs) every 10 ms that maximizes phonetic discriminability while minimizing speaker and channel variability.

---

### 2. The Seven Key Stages and Their Technical Purposes

#### Stage 1: Pre-Emphasis Filtering
* **Operation:** Pass speech through a first-order FIR high-pass filter:
  $$y[n] = x[n] - \\alpha x[n-1], \\quad \\alpha \\in [0.95, 0.98]$$
* **Purpose:** Glottal excitation and lip radiation introduce a $-6\\text{ dB/octave}$ spectral tilt. Pre-emphasis boosts the high-frequency formants (above 1 kHz), equalizing the dynamic range of the spectrum across all frequencies.

#### Stage 2: Frame Blocking / Segmentation
* **Operation:** Partition the continuous speech stream into overlapping short frames of $20-30\\text{ ms}$ (e.g., $N = 400$ samples at 16 kHz) with a frame shift / hop size of $10\\text{ ms}$ ($M = 160$ samples).
* **Purpose:** Speech is non-stationary globally, but quasi-stationary (statistically stationary) over $20-30\\text{ ms}$ intervals corresponding to single vocal tract articulatory configurations. Overlapping ensures smooth temporal continuity without missing transitions.

#### Stage 3: Windowing
* **Operation:** Multiply each speech frame by a tapered window, typically a **Hamming Window**:
  $$w[n] = 0.54 - 0.46 \\cos\\left(\\frac{2\\pi n}{N - 1}\\right), \\quad 0 \\le n \\le N - 1$$
* **Purpose:** Prevents **spectral leakage**. Truncating speech with a rectangular window creates sharp discontinuities at frame boundaries that introduce false high-frequency artifacts. The Hamming window smoothly tapers edges to near zero.

#### Stage 4: Fast Fourier Transform (FFT)
* **Operation:** Compute the $N$-point FFT of each windowed frame to obtain the complex spectrum $X[k]$, then compute the magnitude spectrum $|X[k]|$.
* **Purpose:** Converts the speech frame from the time domain to the frequency domain to expose the formant resonances and harmonic energy distribution.

#### Stage 5: Mel-Frequency Filter Bank Processing
* **Operation:** Pass the magnitude spectrum through a bank of $M$ (typically 26 to 40) overlapping triangular bandpass filters spaced linearly below 1 kHz and logarithmically above 1 kHz:
  $$\\text{Mel}(f) = 2595 \\log_{10}\\left(1 + \\frac{f}{700}\\right)$$
* **Purpose:** Mimics human auditory perception (tonotopic structure of the human cochlea / basilar membrane) and drastically reduces spectral dimensionality.

#### Stage 6: Logarithmic Energy Compression
* **Operation:** Take the natural or base-10 logarithm of each triangular filter bank energy output:
  $$Y[m] = \\ln\\left( \\sum_{k} |X[k]|^2 H_m[k] \\right)$$
* **Purpose:** Models human hearing's logarithmic perception of loudness (Weber-Fechner Law) and converts multiplicative convolutional effects (source × vocal tract) into simple additive terms.

#### Stage 7: Discrete Cosine Transform (DCT) & Dynamic Derivatives
* **Operation:** Apply DCT-II to decorrelate the log filter bank energies:
  $$c_n = \\sum_{m=1}^M Y[m] \\cos\\left[ \\frac{\\pi n}{M} \\left(m - 0.5\\right) \\right], \\quad n = 0, 1, \\dots, 12$$
* **Purpose:** Decorrelates the filter bank energies so that acoustic models (GMMs/HMMs) can assume diagonal covariance matrices, saving computation. Append Delta and Delta-Delta coefficients to capture velocity and acceleration."""
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
        "punchline": "Static features (13-D MFCCs) capture instantaneous vocal tract geometry at frame t; Dynamic features (13-D Delta + 13-D Delta-Delta) capture transitional velocity and acceleration, forming a 39-D vector.",
        "mnemonic": "S-D-DD: Static (Posture), Delta (Velocity), Delta-Delta (Acceleration) -> 13 + 13 + 13 = 39D",
        "analogy": "Like a movie of a sprinter: Static features describe the runner's pose in a single still photograph; dynamic features capture their running speed and acceleration between consecutive movie frames.",
        "diagram": """TEMPORAL SPEECH EVOLUTION (Frame by Frame):
   Frame t-2       Frame t-1        Frame t        Frame t+1       Frame t+2
  ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
  │ c(t-2)  │     │ c(t-1)  │     │  c(t)   │     │ c(t+1)  │     │ c(t+2)  │
  └─────────┘     └─────────┘     └─────────┘     └─────────┘     └─────────┘
                                       │
                                       ├─► STATIC: Instantaneous Spectrum c(t) [13-D]
                                       │
                                       ├─► DELTA (Δ): Velocity / Spectral Slope [13-D]
                                       │              Δc(t) = Σ n·(c(t+n) - c(t-n)) / 2Σn^2
                                       │
                                       └─► DELTA-DELTA (ΔΔ): Acceleration [13-D]
                                                      ΔΔc(t) = Δ(Δc(t))
   COMBINED FEATURE VECTOR: [ c(t) | Δc(t) | ΔΔc(t) ] ──► 39-Dimensional Vector""",
        "content": """### 1. Concept of Static Features
Static features represent the **instantaneous spectral characteristics** of the speech signal at a specific, frozen window in time (frame $t$):
* **What they capture:** The physical shape, geometry, and cross-sectional area of the vocal tract (tongue position, lip rounding, jaw opening).
* **Composition:** Typically 13 coefficients per frame:
  * $c_1$ to $c_{12}$: Lower-order Mel-Frequency Cepstral Coefficients (MFCCs).
  * $c_0$ or $\\log E$: Frame logarithmic energy.
* **Limitation of Static Features:** Human speech is inherently continuous and dynamic. Articulators do not jump instantaneously; they move smoothly between phonemes (**Co-articulation**). Static features evaluate frames in isolation and completely miss the direction and rate of articulatory movement.

---

### 2. Concept of Dynamic Features (Velocity & Acceleration)
Dynamic features capture the **temporal trajectory and transitional dynamics** across neighboring speech frames:

#### 1. First-Order Derivatives (Delta / Velocity Features, $\\Delta c_t$)
* **Definition:** Represents the instantaneous rate of spectral change (velocity of the articulators).
* **Mathematical Formula (Regression formula over a symmetric window of size $K$, typically $K=2$):**
  $$\\Delta c_t = \\frac{\\sum_{n=1}^K n \\left(c_{t+n} - c_{t-n}\\right)}{2 \\sum_{n=1}^K n^2}$$
* **Role in Speech:** Crucial for identifying dynamic speech sounds like diphthongs (e.g., /aɪ/, /oʊ/), glides (/w/, /j/), and plosive transition bursts.

#### 2. Second-Order Derivatives (Delta-Delta / Acceleration Features, $\\Delta^2 c_t$)
* **Definition:** Computed by applying the regression formula to the delta coefficients:
  $$\\Delta^2 c_t = \\frac{\\sum_{n=1}^K n \\left(\\Delta c_{t+n} - \\Delta c_{t-n}\\right)}{2 \\sum_{n=1}^K n^2}$$
* **Role in Speech:** Measures articulatory acceleration (forces driving the vocal tract muscles) and transitions between vowels and consonants.

---

### 3. The Standard 39-Dimensional Feature Vector in ASR
In modern Automatic Speech Recognition (ASR) systems, each 10 ms frame is represented by a concatenated 39-dimensional vector:
$$X_t = \\Big[ \\underbrace{c_0, c_1, \\dots, c_{12}}_{\\text{13 Static MFCCs}}, \\quad \\underbrace{\\Delta c_0, \\dots, \\Delta c_{12}}_{\\text{13 Delta Features}}, \\quad \\underbrace{\\Delta^2 c_0, \\dots, \\Delta^2 c_{12}}_{\\text{13 Delta-Delta Features}} \\Big]^T \\in \\mathbb{R}^{39}$$

---

### 4. Summary: Static vs. Dynamic Features

| Attribute | Static Features | Dynamic Features (Delta & Delta-Delta) |
| :--- | :--- | :--- |
| **Dimension** | 13 coefficients | 26 coefficients (13 Delta + 13 Delta-Delta) |
| **Information** | Instantaneous vocal tract posture | Articulatory speed and acceleration |
| **Scope** | Single frame (20-30 ms) | Multi-frame temporal context (50-90 ms) |
| **Speech Phenomena** | Steady-state vowels (/a/, /i/, /u/) | Diphthongs, plosives, co-articulation |
| **Noise Sensitivity** | Highly affected by static channel bias | Robust (time-differencing removes constant channel noise) |"""
    },
    {
        "id": "MID1-Q11",
        "mid": "Mid-I",
        "qno": 11,
        "unit": "Unit-2",
        "co": "CO2",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "A signal has 1600 samples, frame size = 400 samples, overlap = 200 samples. Q1: Find the number of frames",
        "punchline": "Using the framing equation $K = \\lfloor\\frac{L - N}{R}\\rfloor + 1$, with hop size $R = N - M = 200$, the signal yields exactly 7 frames.",
        "mnemonic": "L-N-R: Length minus Frame size, divided by Hop size, plus One",
        "analogy": "Like placing 400-meter track runners on a 1600-meter course, with each runner starting 200 meters ahead of the previous one: exactly 7 runners fit on the track.",
        "diagram": """Total Signal Length L = 1600 Samples
|-------------------------------------------------------------------------------|
0                     400                   800                  1200          1600

Frame 1: [  0  ───  399  ]
Frame 2:       [  200  ───  599  ]
Frame 3:             [  400  ───  799  ]
Frame 4:                   [  600  ───  999  ]
Frame 5:                         [  800  ───  1199 ]
Frame 6:                               [  1000 ─── 1399 ]
Frame 7:                                     [  1200 ─── 1599 ]  <-- EXACT END!

Total Frames = 7 (Hop size R = 200 samples, 50% Overlap)""",
        "content": """### 1. Given Data
* Total number of samples in the speech signal ($L$): **$1600\\text{ samples}$**
* Frame size / window length ($N$): **$400\\text{ samples}$**
* Overlap between consecutive frames ($M$): **$200\\text{ samples}$**

---

### 2. Step 1: Compute Hop Size / Frame Shift ($R$)
The hop size (frame shift $R$) is the number of new, non-overlapping samples advanced between the starts of consecutive frames:
$$R = N - M$$

Substituting the given values:
$$R = 400 - 200 = \\mathbf{200\\text{ samples}}$$
*(This corresponds to a standard $50\\%$ frame overlap).*

---

### 3. Step 2: Compute Total Number of Frames ($K$)
The mathematical formula for the number of complete frames $K$ that can be extracted from a signal of length $L$ with window length $N$ and frame shift $R$ is:
$$K = \\left\\lfloor \\frac{L - N}{R} \\right\\rfloor + 1$$

Substituting the given values:
$$K = \\left\\lfloor \\frac{1600 - 400}{200} \\right\\rfloor + 1$$
$$K = \\left\\lfloor \\frac{1200}{200} \\right\\rfloor + 1 = 6 + 1 = \\mathbf{7\\text{ frames}}$$

$$\\mathbf{Final\\ Answer: } \\quad \\text{The total number of frames is } \\mathbf{7}.$$

---

### 4. Step 3: Complete Frame Boundary Mapping Table
To verify the calculation and provide full exam detail, the exact sample boundaries for all 7 frames are:

| Frame Index ($k$) | Start Sample Index | End Sample Index | Total Samples in Frame |
| :---: | :---: | :---: | :---: |
| **Frame 1** | $0$ | $399$ | $400$ |
| **Frame 2** | $200$ | $599$ | $400$ |
| **Frame 3** | $400$ | $799$ | $400$ |
| **Frame 4** | $600$ | $999$ | $400$ |
| **Frame 5** | $800$ | $1199$ | $400$ |
| **Frame 6** | $1000$ | $1399$ | $400$ |
| **Frame 7** | $1200$ | $1599$ | $400$ |

*Notice that Frame 7 ends exactly at sample index 1599, perfectly covering the full 1600-sample signal without any discarded samples.*

---

### 5. Practical Physical Interpretation
If the audio signal was recorded at a standard sampling rate of $f_s = 16\\text{ kHz} = 16000\\text{ samples/sec}$:
* **Signal Duration:** $T_{\\text{total}} = \\frac{1600}{16000} = 0.1\\text{ s} = 100\\text{ ms}$.
* **Frame Duration:** $T_{\\text{frame}} = \\frac{400}{16000} = 0.025\\text{ s} = 25\\text{ ms}$ (ideal quasi-stationary speech frame).
* **Frame Shift:** $T_{\\text{shift}} = \\frac{200}{16000} = 0.0125\\text{ s} = 12.5\\text{ ms}$ (hop time)."""
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
        "punchline": "LPCC relies on an all-pole linear vocal tract model (sensitive to noise and unvoiced sounds); MFCC uses a psychoacoustic Mel filter bank (robust to noise and universal standard in ASR).",
        "mnemonic": "L-M-P-R: Linear vocal model vs Mel psychoacoustic model; MFCC dominates in Robustness",
        "analogy": "LPCC is like a rigid mathematical formula of vocal cord tubes; MFCC is like an audiologist simulating how the human cochlea actually perceives speech sounds.",
        "diagram": """LPCC PIPELINE (Acoustic Tube Model):
  Speech ──► [ LPC Analysis ] ──► [ Predictor ak ] ──► [ Recursive Formula ] ──► LPCCs
                                  (All-Pole Model)

MFCC PIPELINE (Human Auditory Model):
  Speech ──► [ FFT ] ──► [ Mel Filter Bank ] ──► [ Log ] ──► [ DCT-II ] ──► MFCCs
                          (Cochlear Tonotopy)""",
        "content": """### 1. Conceptual Foundations
* **Linear Prediction Cepstral Coefficients (LPCC):** Derived from Linear Predictive Coding (LPC). It models speech production through an all-pole linear filter representing the resonant cavities of the vocal tract. Cepstral coefficients are computed recursively from the LPC predictor coefficients $a_k$.
* **Mel-Frequency Cepstral Coefficients (MFCC):** Derived from the Short-Time Fourier Transform (STFT) combined with human auditory perception. It applies overlapping triangular filters spaced according to the non-linear **Mel scale**, followed by logarithmic compression and DCT.

---

### 2. In-Depth Comparison Table

| Attribute | LPCC (Linear Prediction Cepstrum) | MFCC (Mel-Frequency Cepstrum) |
| :--- | :--- | :--- |
| **Theoretical Model** | Source-Filter all-pole acoustic tube | Human cochlea / auditory psychoacoustics |
| **Spectral Modeling** | Models only spectral envelope peaks (all-pole) | Models both spectral shape and critical bands |
| **Zeros / Nasal Modeling** | **Poor:** Cannot model nasal anti-resonances | **Good:** Filter bank easily captures dips |
| **Noise Robustness** | **Low:** Additive noise distorts all-pole roots | **High:** Wide filter averaging suppresses noise |
| **Computational Basis** | Autocorrelation & Levinson-Durbin | FFT, Triangular Mel Filter Bank, DCT |
| **Formant Resolution** | Extremely sharp formant peaks | Smooth formant clusters (broad at high freqs) |
| **Channel Robustness** | Sensitive to microphone and transmission bias | Robust; simple CMVN removes channel bias |
| **Primary Applications** | Low-bitrate vocoders (LPC-10), speaker ID | State-of-the-art ASR (Whisper, Kaldi), NLP |

---

### 3. Spectral Representation Differences
1. **Low-Frequency vs High-Frequency Modeling:**
   * LPCC allocates equal mathematical weight to all frequency bands across the linear scale.
   * MFCC allocates high frequency resolution to low frequencies (<1 kHz) where formants $F_1, F_2$ lie, and broad integration to high frequencies, directly reflecting human speech intelligibility.
2. **Handling Unvoiced Speech:**
   * LPCC fails for unvoiced fricatives (/s/, /sh/, /f/) because turbulent noise cannot be accurately modeled by an all-pole filter without high error.
   * MFCC handles voiced, unvoiced, and silence regions with equal stability.

---

### 4. Conclusion on Robustness in ASR
In automatic speech recognition, **MFCC is overwhelmingly superior to LPCC**. Its non-linear auditory frequency warping and energy averaging provide high immunity to environmental background noise, room reverberation, and speaker variations."""
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
        "punchline": "Euclidean treats all features equally; Mahalanobis weights features by covariance to handle variance and correlation; DTW solves variable-length temporal misalignment via dynamic programming.",
        "mnemonic": "E-M-D: Euclidean (Point), Mahalanobis (Statistical Covariance), DTW (Temporal Warping)",
        "analogy": "Euclidean is measuring distance as the crow flies; Mahalanobis accounts for rough terrain (feature variance); DTW is synchronizing two video clips of people speaking at different speeds.",
        "diagram": """DYNAMIC TIME WARPING (DTW) OPTIMAL WARPING PATH:
   Test Utterance j (Length M)
   ▲
 M │                      ╭──── (N, M) [End]
   │                   ╭──╯
   │                ╭──╯   Optimal Warping Path
   │             ╭──╯      W = [w1, w2, ..., wK]
   │          ╭──╯
 1 │ (1,1) ───╯
   └─┴──────────────────────────────►
     1                             N   Reference Template i (Length N)

LOCAL SLOPE CONSTRAINTS:
     D(i, j) = d(xi, yj) + min { D(i-1, j), D(i, j-1), D(i-1, j-1) }""",
        "content": """### 1. The Role of Distance Measures in Speech Recognition
Speech pattern matching compares an unknown test speech utterance against stored reference patterns or models. Because speech varies in both **feature space** (acoustic variability) and **time space** (speaking rate variability), specialized distance metrics are required:
1. **Point-to-Point Acoustic Distances:** Euclidean and Mahalanobis distances compare two feature vectors of the same dimension.
2. **Sequence Alignment Distances:** Dynamic Time Warping (DTW) aligns and compares two speech utterances of unequal temporal lengths.

---

### 2. Euclidean Distance

#### 1. Mathematical Formula
For two $D$-dimensional feature vectors $\\mathbf{x} = [x_1, \\dots, x_D]^T$ and $\\mathbf{y} = [y_1, \\dots, y_D]^T$:
$$d_E(\\mathbf{x}, \\mathbf{y}) = \\sqrt{\\sum_{k=1}^D (x_k - y_k)^2} = \\sqrt{(\\mathbf{x} - \\mathbf{y})^T (\\mathbf{x} - \\mathbf{y})}$$

#### 2. Evaluation in Speech Systems
* **Assumptions:** Assumes all feature dimensions are completely uncorrelated and have identical variance (spherical distribution).
* **Strength:** Extremely fast to compute ($O(D)$ operations).
* **Major Weakness in Speech:** Lower-order MFCCs have much larger energy and numerical variance than higher-order MFCCs. Euclidean distance is dominated by low-order coefficients, completely ignoring high-frequency nuances.

---

### 3. Mahalanobis Distance

#### 1. Mathematical Formula
Incorporates the covariance matrix $\\mathbf{\\Sigma}$ of the feature distribution:
$$d_M(\\mathbf{x}, \\mathbf{y}) = \\sqrt{(\\mathbf{x} - \\mathbf{y})^T \\mathbf{\\Sigma}^{-1} (\\mathbf{x} - \\mathbf{y})}$$
where $\\mathbf{\\Sigma}$ is the $D \\times D$ covariance matrix estimated from training speech data.

#### 2. Evaluation in Speech Systems
* **Key Advantages:**
  1. **Scale Invariance:** Normalizes each feature dimension by its variance $\\sigma_k^2$, preventing high-variance energy terms from dominating.
  2. **Decorrelation:** Off-diagonal covariance elements account for statistical correlations between adjacent spectral bands.
* **In Speech Models:** Forms the core distance metric in Gaussian Mixture Models (GMMs) and Vector Quantization (VQ) codebook clustering.

---

### 4. Dynamic Time Warping (DTW)

#### 1. The Time Alignment Problem in Speech
No speaker utters the same word with identical duration twice. For example, the word *\"speech\"* may take $400\\text{ ms}$ in one utterance ($N = 40$ frames) and $650\\text{ ms}$ in another ($M = 65$ frames). A simple Euclidean distance between frames cannot compare them because $N \\ne M$.

#### 2. DTW Algorithm Formulation
Let the reference template be $X = [\\mathbf{x}_1, \\mathbf{x}_2, \\dots, \\mathbf{x}_N]$ and the test utterance be $Y = [\\mathbf{y}_1, \\mathbf{y}_2, \\dots, \\mathbf{y}_M]$.
DTW constructs an $N \\times M$ grid where each cell $(i, j)$ has a local distance $d(\\mathbf{x}_i, \\mathbf{y}_j)$ (Euclidean or Mahalanobis).

The optimal warping path $W = \\{w_1, w_2, \\dots, w_K\\}$ minimizes the cumulative distance:
$$D_{\\text{DTW}}(X, Y) = \\min_{W} \\frac{1}{K} \\sum_{k=1}^K d(w_k)$$

#### 3. Dynamic Programming Recursion
The cumulative distance matrix $D(i, j)$ is computed iteratively using Bellman's principle of optimality:
$$D(i, j) = d(\\mathbf{x}_i, \\mathbf{y}_j) + \\min \\begin{cases} D(i - 1, j) & \\text{(Insertion / Horizontal stretch)} \\\\ D(i, j - 1) & \\text{(Deletion / Vertical stretch)} \\\\ D(i - 1, j - 1) & \\text{(Match / Diagonal step)} \\end{cases}$$

#### 4. Practical Constraints on DTW
1. **Boundary Condition:** Must start at $(1, 1)$ and terminate at $(N, M)$.
2. **Monotonicity:** $i_k \\ge i_{k-1}$ and $j_k \\ge j_{k-1}$ (time cannot run backwards).
3. **Continuity:** Steps are restricted to $(0, 1), (1, 0), (1, 1)$ (no skipped phonemes).
4. **Global Path Constraint (Sakoe-Chiba Band / Itakura Parallelogram):** Restricts the search path to a band $|i - j| \\le R$ to prevent unrealistic time compression/expansion.

---

### 5. Comparative Evaluation Summary

| Criterion | Euclidean Distance | Mahalanobis Distance | Dynamic Time Warping (DTW) |
| :--- | :--- | :--- | :--- |
| **Input Comparison** | Two vectors $\\mathbf{x}, \\mathbf{y} \\in \\mathbb{R}^D$ | Two vectors $\\mathbf{x}, \\mathbf{y} \\in \\mathbb{R}^D$ | Two time sequences of unequal lengths ($N \\ne M$) |
| **Statistical Weighting**| Uniform weight for all features | Weighted by inverse covariance $\\mathbf{\\Sigma}^{-1}$ | Uses local Euclidean/Mahalanobis in its cost grid |
| **Temporal Flexibility** | None (fixed vectors only) | None (fixed vectors only) | **Full non-linear temporal alignment** |
| **Computational Cost** | Very low: $O(D)$ | Moderate: $O(D^2)$ | High: $O(N \\times M \\times D)$ |
| **Speech Application** | Nearest-neighbor vector clustering | GMM acoustic scoring, Speaker verification | Isolated word recognition, keyword spotting |"""
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
        "punchline": "Vector Quantization maps high-dimensional continuous features into a compact discrete codebook using the LBG algorithm; optimal codebook size balances distortion and latency.",
        "mnemonic": "L-B-G-V: Linde-Buzo-Gray algorithm, Centroid Splitting, Voronoi Partitions, Distortion minimization",
        "analogy": "Like a digital color palette (e.g. 256 colors): Instead of saving millions of RGB shades, you represent every color in an image with the nearest palette index, saving 90% memory.",
        "diagram": """VECTOR QUANTIZATION FEATURE SPACE (Voronoi Tessellation):
   ▲ Feature Dimension 2 (MFCC 2)
   │     \      /
   │      \ y1 /         y1, y2, y3, y4 = Codevectors (Centroids)
   │   ────●────────     R1, R2, R3, R4 = Voronoi Partitions (Cells)
   │      / │ \
   │     /  │  \ y2
   │    /   │   ●
   │   / y3 │    \       Input vector x is mapped to nearest y_k:
   │  /  ●  │     \      Q(x) = y_k if d(x, y_k) <= d(x, y_j)
   └──┴─────┴──────┴──────────────────► Feature Dimension 1 (MFCC 1)

LBG ALGORITHM (Centroid Splitting):
  1 Centroid ──(Split ±ε)──► 2 Centroids ──(Split ±ε)──► 4 ──► ... ──► K Codevectors""",
        "content": """### 1. Vector Quantization (VQ) in Speech Recognition
Vector Quantization (VQ) is a lossy data compression technique that maps continuous high-dimensional speech vectors $\\mathbf{x} \\in \\mathbb{R}^D$ into a finite set of $K$ discrete representative vectors called **codevectors**:
$$C = \\{\\mathbf{y}_1, \\mathbf{y}_2, \\dots, \\mathbf{y}_K\\}, \\quad \\mathbf{y}_i \\in \\mathbb{R}^D$$
* The set $C$ is called the **Codebook**, and $K$ is the codebook size (typically $K = 64, 128, 256$).
* The feature space is partitioned into $K$ non-overlapping regions called **Voronoi Cells** ($R_i$):
  $$R_i = \\left\\{ \\mathbf{x} \\in \\mathbb{R}^D : d(\\mathbf{x}, \\mathbf{y}_i) \\le d(\\mathbf{x}, \\mathbf{y}_j), \\; \\forall j \\ne i \\right\\}$$
* **Quantizer Mapping:** $Q(\\mathbf{x}) = \\mathbf{y}_i$ if $\\mathbf{x} \\in R_i$.

---

### 2. Codebook Generation: The Linde-Buzo-Gray (LBG) Algorithm
The LBG algorithm is an iterative clustering technique that generalizes k-means to generate an optimal codebook from training speech vectors:

#### Step-by-Step LBG Procedure:
1. **Initialize ($K = 1$):**
   * Compute the global centroid $\\mathbf{y}_1^*$ of all $T$ training vectors:
     $$\\mathbf{y}_1^* = \\frac{1}{T} \\sum_{t=1}^T \\mathbf{x}_t$$
2. **Codebook Splitting ($K \\to 2K$):**
   * Double the number of codevectors by splitting each existing codevector $\\mathbf{y}_i$ using a small perturbation vector $\\boldsymbol{\\epsilon}$:
     $$\\mathbf{y}_i^+ = \\mathbf{y}_i (1 + \\boldsymbol{\\epsilon}), \\quad \\mathbf{y}_i^- = \\mathbf{y}_i (1 - \\boldsymbol{\\epsilon})$$
3. **Nearest Neighbor Classification (K-Means Iteration):**
   * Assign every training vector $\\mathbf{x}_t$ to its nearest codevector cell $R_i$:
     $$R_i = \\left\\{ \\mathbf{x}_t : d(\\mathbf{x}_t, \\mathbf{y}_i) < d(\\mathbf{x}_t, \\mathbf{y}_j), \\; \\forall j \\ne i \\right\\}$$
4. **Centroid Update:**
   * Recompute the centroid of each cell:
     $$\\mathbf{y}_i = \\frac{1}{|R_i|} \\sum_{\\mathbf{x}_t \\in R_i} \\mathbf{x}_t$$
5. **Convergence Check:**
   * Compute average quantization distortion:
     $$D = \\frac{1}{T} \\sum_{t=1}^T \\min_{1 \\le i \\le K} d(\\mathbf{x}_t, \\mathbf{y}_i)$$
   * If $\\frac{|D_{\\text{old}} - D|}{D} < \\delta$ (threshold, e.g. 0.001), repeat Step 2 until the desired codebook size $K$ is reached.

---

### 3. Justification of Codebook Optimization Strategies

#### 1. Codebook Size ($K$) Trade-off
* **Small Codebook ($K \\le 32$):** Low memory and fast search ($O(K)$), but high quantization distortion. Merges distinct phonetic sounds together, degrading recognition accuracy.
* **Large Codebook ($K \\ge 512$):** Low distortion, but risks overfitting to speaker-specific traits, reducing cross-speaker generalization. Drastically increases search latency.
* **Optimal Range:** $K = 64$ to $128$ for isolated digit / command recognition; $K = 256$ for speaker identification.

#### 2. Weighted / Mahalanobis Distortion Measures
* Replacing standard Euclidean distance with Mahalanobis distance weights feature dimensions by inverse variance, preventing noisy dimensions from skewing codevector centers.

#### 3. Tree-Structured Vector Quantization (TSVQ)
* Arranges codevectors into a binary tree.
* Reduces search complexity from linear $O(K)$ to logarithmic $O(\\log_2 K)$, enabling real-time mobile speech processing.

---

### 4. VQ Performance Evaluation in Speech Systems

| Metric | Strengths of VQ | Limitations of VQ |
| :--- | :--- | :--- |
| **Data Compression** | Massive: Replaces 39 continuous float values with a single 8-bit integer index ($\log_2 256 = 8$ bits) | Irreversible loss of fine acoustic detail (quantization noise) |
| **Computational Speed** | Fast acoustic scoring via lookup tables | Suffers from the curse of dimensionality if $D > 40$ |
| **Acoustic Modeling** | Highly effective for text-independent speaker verification | Discards temporal sequence information (requires HMM wrapper) |"""
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
        "punchline": "A GMM models complex multi-modal speech feature distributions as a weighted sum of M Gaussian densities; the EM algorithm iteratively maximizes data likelihood via posterior responsibilities.",
        "mnemonic": "E-M-G: Expectation (Posterior responsibilities), Maximization (Parameter updates), Gaussian mixture",
        "analogy": "A mountain range with multiple peaks: Rather than trying to describe the whole range with one simple bell curve, you model it as a sum of several individual hills (Gaussians), each with its own location, width, and height.",
        "diagram": """GAUSSIAN MIXTURE MODEL (GMM) ARCHITECTURE:
   Probability Density p(x)
   ▲                   _---_
   │                  /     \  Component 2 (Weight w2, Mean μ2, Cov Σ2)
   │        _---_    /       \
   │       /     \  /         \       Composite GMM Density:
   │      /  c1   \/           \      p(x) = w1·N(x; μ1, Σ1) + w2·N(x; μ2, Σ2)
   │     /         \            \
   └────┴───────────┴────────────┴─────► Feature Space x (MFCC)

EM ALGORITHM CYCLE:
  Initial Parameters λ = {wm, μm, Σm}
            │
            ▼
     ┌───────────────┐
 ┌──►│ E-STEP:       │  Compute Posterior Responsibilities:
 │   │               │  γm(xt) = wm·N(xt; μm, Σm) / Σ wj·N(xt; μj, Σj)
 │   └───────┬───────┘
 │           │
 │           ▼
 │   ┌───────────────┐
 │   │ M-STEP:       │  Re-estimate Parameters:
 │   │               │  w^m = (1/T) Σ γm(xt)
 │   │               │  μ^m = Σ γm(xt)·xt / Σ γm(xt)
 │   │               │  Σ^m = Σ γm(xt)·(xt - μ^m)(xt - μ^m)^T / Σ γm(xt)
 │   └───────┬───────┘
 │           │
 └── Check Convergence: Likelihood Increase < ε ──► Optimal GMM λ*""",
        "content": """### 1. Mathematical Design of a Gaussian Mixture Model (GMM)
In speech processing, speech feature vectors (MFCCs) for a given phoneme or speaker form a complex, multi-modal distribution that cannot be modeled by a single Gaussian. A **Gaussian Mixture Model (GMM)** approximates the probability density function as a linear superposition of $M$ multivariate Gaussian basis functions:
$$p(\\mathbf{x} | \\lambda) = \\sum_{m=1}^M w_m \\mathcal{N}(\\mathbf{x}; \\boldsymbol{\\mu}_m, \\mathbf{\\Sigma}_m)$$

#### Parameter Set $\\lambda$:
$$\\lambda = \\left\\{ w_m, \\boldsymbol{\\mu}_m, \\mathbf{\\Sigma}_m \\right\\}_{m=1}^M$$
1. **Mixture Weights ($w_m$):** The prior probability of component $m$, satisfying:
   $$\\sum_{m=1}^M w_m = 1, \\quad w_m \\ge 0$$
2. **Mean Vectors ($\\boldsymbol{\\mu}_m \\in \\mathbb{R}^D$):** Center of Gaussian component $m$.
3. **Covariance Matrices ($\\mathbf{\\Sigma}_m \\in \\mathbb{R}^{D \\times D}$):** Describes the dispersion and correlation of the features. In speech ASR, **diagonal covariance matrices** are universally used because DCT decorrelates MFCCs, reducing parameter count from $D^2$ to $D$.
4. **Multivariate Gaussian Density:**
   $$\\mathcal{N}(\\mathbf{x}; \\boldsymbol{\\mu}_m, \\mathbf{\\Sigma}_m) = \\frac{1}{(2\\pi)^{D/2} |\\mathbf{\\Sigma}_m|^{1/2}} \\exp\\left( -\\frac{1}{2} (\\mathbf{x} - \\boldsymbol{\\mu}_m)^T \\mathbf{\\Sigma}_m^{-1} (\\mathbf{x} - \\boldsymbol{\\mu}_m) \\right)$$

---

### 2. Parameter Estimation via Expectation-Maximization (EM)
Given a sequence of $T$ training feature vectors $X = \\{\\mathbf{x}_1, \\mathbf{x}_2, \\dots, \\mathbf{x}_T\\}$, we aim to find the parameters $\\lambda$ that maximize the total log-likelihood:
$$\\log p(X | \\lambda) = \\sum_{t=1}^T \\log \\left( \\sum_{m=1}^M w_m \\mathcal{N}(\\mathbf{x}_t; \\boldsymbol{\\mu}_m, \\mathbf{\\Sigma}_m) \\right)$$
Direct analytical optimization is intractable due to the sum inside the logarithm. The **Expectation-Maximization (EM)** algorithm solves this iteratively.

---

### 3. The Two Steps of the EM Algorithm

#### 1. The E-Step (Expectation / Posterior Probability)
Compute the posterior responsibility $\\gamma_m(\\mathbf{x}_t)$, which is the conditional probability that observation vector $\\mathbf{x}_t$ was generated by Gaussian component $m$, using current parameters $\\lambda$:
$$\\gamma_m(\\mathbf{x}_t) = P(m | \\mathbf{x}_t, \\lambda) = \\frac{w_m \\mathcal{N}(\\mathbf{x}_t; \\boldsymbol{\\mu}_m, \\mathbf{\\Sigma}_m)}{\\sum_{j=1}^M w_j \\mathcal{N}(\\mathbf{x}_t; \\boldsymbol{\\mu}_j, \\mathbf{\\Sigma}_j)}$$

#### 2. The M-Step (Maximization / Parameter Updates)
Using the soft responsibilities $\\gamma_m(\\mathbf{x}_t)$, re-estimate the mixture parameters to maximize the expected complete-data log-likelihood:
1. **Update Mixture Weights:**
   $$\\hat{w}_m = \\frac{1}{T} \\sum_{t=1}^T \\gamma_m(\\mathbf{x}_t)$$
2. **Update Mean Vectors:**
   $$\\hat{\\boldsymbol{\\mu}}_m = \\frac{\\sum_{t=1}^T \\gamma_m(\\mathbf{x}_t) \\mathbf{x}_t}{\\sum_{t=1}^T \\gamma_m(\\mathbf{x}_t)}$$
3. **Update Covariance Matrices (Diagonal Form):**
   $$\\hat{\\mathbf{\\Sigma}}_m = \\frac{\\sum_{t=1}^T \\gamma_m(\\mathbf{x}_t) \\left(\\mathbf{x}_t - \\hat{\\boldsymbol{\\mu}}_m\\right) \\left(\\mathbf{x}_t - \\hat{\\boldsymbol{\\mu}}_m\\right)^T}{\\sum_{t=1}^T \\gamma_m(\\mathbf{x}_t)}$$

#### 3. Convergence Guarantee
The EM algorithm is repeated iteratively:
$$\\lambda^{(0)} \\xrightarrow{\\text{EM}} \\lambda^{(1)} \\xrightarrow{\\text{EM}} \\dots \\xrightarrow{\\text{EM}} \\lambda^*$$
Each iteration is mathematically proven to increase or maintain the total log-likelihood:
$$\\log p(X | \\lambda^{(k+1)}) \\ge \\log p(X | \\lambda^{(k)})$$
Iteration stops when the log-likelihood gain falls below a small tolerance $\\epsilon$.

---

### 4. Practical Implementation Challenges & Solutions in Speech
1. **Variance Flooring:** If a Gaussian component has few assigned data points, its variance can collapse to zero ($\\sigma_{m,d}^2 \\to 0$), causing the likelihood to diverge to infinity. **Solution:** Enforce a minimum variance floor (e.g., $1\\%$ of global data variance).
2. **Initialization via K-Means:** Random initialization can get trapped in poor local maxima. Initializing component means $\\boldsymbol{\\mu}_m$ with K-means cluster centers guarantees rapid, stable convergence."""
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
        "punchline": "An HMM models doubly stochastic speech processes: hidden articulatory states transition over time while emitting observable acoustic MFCCs; solved via Forward, Viterbi, and Baum-Welch algorithms.",
        "mnemonic": "F-V-B: Forward (Evaluation), Viterbi (Decoding), Baum-Welch (Training)",
        "analogy": "Like guessing the weather outside (hidden states: sunny, rainy) by observing whether people entering a windowless office carry wet umbrellas, sunglasses, or coats (observable acoustic features).",
        "diagram": """3-STATE LEFT-TO-RIGHT (BAKIS) HMM TOPOLOGY FOR A PHONEME:
             a11                    a22                    a33
            ╭───╮                  ╭───╮                  ╭───╮
            ▼   │                  ▼   │                  ▼   │
         ┌─────────┐    a12     ┌─────────┐    a23     ┌─────────┐
  ────►  │ State 1 ├───────────►│ State 2 ├───────────►│ State 3 ├────► Exit
  Initial│ (Onset) │            │(Nucleus)│            │ (Coda)  │
  π1 = 1 └────┬────┘            └────┬────┘            └────┬────┘
              │                      │                      │
              ▼ b1(ot)               ▼ b2(ot)               ▼ b3(ot)
          Observation            Observation            Observation
          Vector o(t)            Vector o(t)            Vector o(t)
          (Acoustic MFCC)        (Acoustic MFCC)        (Acoustic MFCC)

CONTINUOUS SPEECH: HMMs for phonemes are concatenated into Words, and Words into Sentences!""",
        "content": """### 1. Conceptual Architecture of an HMM for Speech
A Hidden Markov Model (HMM) is a doubly stochastic statistical process ideally suited for speech recognition:
1. **Underlying Hidden Process:** A discrete Markov chain representing the hidden sequence of articulatory vocal tract states ($S = \\{s_1, s_2, \\dots, s_N\\}$).
2. **Observable Process:** A continuous statistical distribution that emits the observable acoustic feature vectors $O = \\{\\mathbf{o}_1, \\mathbf{o}_2, \\dots, \\mathbf{o}_T\\}$ (e.g., 39-D MFCCs).

#### Complete Formal HMM Definition: $\\lambda = (A, B, \\boldsymbol{\\pi})$
1. **State Transition Probability Matrix $A = \\{a_{ij}\\}$:**
   $$a_{ij} = P(q_{t+1} = s_j | q_t = s_i), \\quad 1 \\le i, j \\le N$$
   * In speech recognition, a **Left-to-Right (Bakis) Topology** is strictly enforced: $a_{ij} = 0$ for $j < i$. States can only stay in place ($a_{ii}$) or transition forward ($a_{i, i+1}, a_{i, i+2}$). This naturally mirrors the forward flow of time in speech articulation.
2. **Observation Emission Probability Distribution $B = \\{b_j(\\mathbf{o}_t)\\}$:**
   $$b_j(\\mathbf{o}_t) = P(\\mathbf{o}_t | q_t = s_j)$$
   * Modeled using a Gaussian Mixture Model (GMM):
     $$b_j(\\mathbf{o}_t) = \\sum_{m=1}^M w_{jm} \\mathcal{N}(\\mathbf{o}_t; \\boldsymbol{\\mu}_{jm}, \\mathbf{\\Sigma}_{jm})$$
3. **Initial State Distribution $\\boldsymbol{\\pi} = \\{\\pi_i\\}$:**
   $$\\pi_i = P(q_1 = s_i), \\quad \\pi_1 = 1, \\; \\pi_i = 0 \\; (\\forall i > 1)$$

---

### 2. The Three Canonical Problems of HMM and Their Solutions

#### Problem 1: Evaluation / Likelihood (Forward-Backward Algorithm)
* **Goal:** Given model $\\lambda$ and observation sequence $O$, compute $P(O | \\lambda)$.
* **Solution:** The **Forward Algorithm** uses dynamic programming to sum probabilities across all possible hidden state sequences in $O(N^2 T)$ operations instead of $O(N^T)$ brute-force:
  1. *Initialization:* $\\alpha_1(i) = \\pi_i b_i(\\mathbf{o}_1)$
  2. *Induction:* $\\alpha_{t+1}(j) = \\left[ \\sum_{i=1}^N \\alpha_t(i) a_{ij} \\right] b_j(\\mathbf{o}_{t+1})$
  3. *Termination:* $P(O | \\lambda) = \\sum_{i=1}^N \\alpha_T(i)$

#### Problem 2: Decoding / Recognition (Viterbi Algorithm)
* **Goal:** Find the single optimal, most likely hidden state sequence $Q^* = (q_1^*, q_2^*, \\dots, q_T^*)$ that generated observation sequence $O$.
* **Solution:** The **Viterbi Algorithm** (Dynamic Programming):
  1. *Initialization:* $\\delta_1(i) = \\pi_i b_i(\\mathbf{o}_1), \\quad \\psi_1(i) = 0$
  2. *Recursion:*
     $$\\delta_t(j) = \\max_{1 \\le i \\le N} \\left[ \\delta_{t-1}(i) a_{ij} \\right] \\cdot b_j(\\mathbf{o}_t)$$
     $$\\psi_t(j) = \\arg\\max_{1 \\le i \\le N} \\left[ \\delta_{t-1}(i) a_{ij} \\right]$$
  3. *Backtracking:* Trace back pointers $\\psi_t(j)$ from $T$ down to $1$ to recover $Q^*$.

#### Problem 3: Learning / Training (Baum-Welch / EM Algorithm)
* **Goal:** Given training speech utterances $O$, adjust parameters $\\lambda = (A, B, \\boldsymbol{\\pi})$ to maximize $P(O | \\lambda)$.
* **Solution:** The **Baum-Welch Algorithm** (Expectation-Maximization) iteratively updates state transition probabilities $\\hat{a}_{ij}$ and emission Gaussian parameters $\\hat{\\boldsymbol{\\mu}}_{jm}, \\hat{\\mathbf{\\Sigma}}_{jm}$ until likelihood converges.

---

### 3. Assessment of Capability in Modeling Temporal Variability
HMMs are extraordinarily effective at modeling speech temporal variability due to two core capabilities:
1. **Non-Linear Time Warping via Self-Transitions:**
   * The self-transition probability $a_{ii}$ allows the model to remain in the same phonetic state for an arbitrary number of frames.
   * If a speaker speaks slowly and elongates a vowel, the system simply traverses self-loops $a_{ii} \\to a_{ii} \\to a_{ii}$ repeatedly without distortion.
   * Expected duration in state $i$ is mathematically modeled as:
     $$\\bar{d}_i = \\frac{1}{1 - a_{ii}}$$
2. **Sub-Phonemic Modeling (3-State Bakis Model):**
   * Every phoneme is split into 3 consecutive acoustic sub-states: **Onset** (transition into sound), **Nucleus** (stable center), and **Coda** (transition out of sound).
   * This handles co-articulation naturally by absorbing context effects into the onset and coda states.

---

### 4. Continuous Speech Recognition Architecture
In continuous speech recognition, individual phoneme HMMs are concatenated into word HMMs according to a pronunciation dictionary (lexicon). Word HMMs are further interconnected into a search graph guided by an **N-gram Language Model** ($P(w_k | w_{k-1}, w_{k-2})$). The Viterbi beam search decodes the globally optimal sentence hypothesis efficiently."""
    }
]
