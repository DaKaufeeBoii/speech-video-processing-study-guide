# -*- coding: utf-8 -*-
"""
Unit 1: Fundamentals of Speech Production, Discrete-Time Speech Signals & Analysis
Questions: Mid-I Q1 to Q8
Academic Year: 2026-27 | Regulation: KGR23 | Course Code: KG23ACM408 | Dr. Sandeep Kumar M
Aligned strictly with official lecture slides (Lectures 1-6) and Question Bank.
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
        "punchline": "Speech production operates across 3 levels (Conceptualization -> Formulation -> Articulation) and 5 subsystems, modeled as Source E(z) filtered by Vocal Tract H(z).",
        "content": """### 1. Definition of Speech Production Mechanism
Speech production is a complex, multi-step biological and cognitive process that converts thoughts and ideas into acoustic speech signals through the coordinated effort of the brain and vocal organs.

Speech production operates across **three hierarchical levels**:
1. **Conceptualization (First Stage - Thinking & Planning):**
   * Ideas and intentions are formed in the mind.
   * The brain determines what message to communicate, selects main points, and organizes them in a logical order using knowledge, memory, and emotions.
   * *Brain Involvement:* **Wernicke's area** helps in understanding and selecting words, while **Broca's area** plans and sequences speech.
2. **Formulation (Second Stage - Language Encoding):**
   * Converts mental ideas into linguistic structures (words, phrases, and grammatical sentences).
   * Brain selects appropriate vocabulary, applies grammatical rules, and works with the motor cortex to plan speech movements.
3. **Articulation (Final Stage - Physical Execution):**
   * The motor cortex sends neural commands to the speech muscles.
   * Physical sound is generated and shaped using the lungs, vocal cords, pharynx, tongue, lips, teeth, and jaw.

---

### 2. Speech Production Subsystems
The speech mechanism coordinates five interrelated physical subsystems:
* **Respiratory System (Air Supply System):** Lungs and trachea provide steady airflow and subglottal pressure, acting as the primary energy source.
* **Phonatory System (Sound Producing System):** Larynx and vocal cords convert steady airflow into acoustic energy (vibrating vocal cords produce voiced sound; stationary open cords produce unvoiced noise).
* **Resonatory System (Sound Booster System):** Throat (pharynx), oral cavity (mouth), and nasal cavities amplify and resonate specific frequencies (formants).
* **Articulatory System (Speech Shaping System):** Tongue, lips, teeth, palate, and jaw shape the resonating air into distinct phonemes, vowels, and consonants.
* **Regulatory System (Brain Control System):** The brain controls, coordinates, and continuously monitors speech through auditory and kinesthetic feedback.

---

### 3. Roles of Excitation Source and Vocal Tract System
Mathematically, the acoustic theory of speech production models speech generation as:
$$\\text{Output Speech } S(z) = E(z) \\cdot H(z) \\cdot R(z)$$

| Component | Biological Organs | Acoustic Role & Transfer Function | Speech Output Characteristics |
| :--- | :--- | :--- | :--- |
| **Excitation Source $E(z)$** | Lungs, Trachea, Larynx (Vocal Cords / Glottis) | Acts as the raw acoustic energy generator: <br>1. *Voiced Sound:* Vocal cords vibrate periodically, producing quasi-periodic pulse trains with fundamental frequency (Pitch $F_0$). <br>2. *Unvoiced Sound:* Vocal cords remain open; air passes through narrow constriction creating random turbulent noise. | Supplies fundamental frequency $F_0$ (pitch) and harmonic sound spectrum. |
| **Vocal Tract System $H(z)$** | Pharynx, Oral Cavity, Velum, Nasal Cavity, Tongue, Lips | Acts as an acoustic filter / resonant tube (~17.5 cm in adults) with time-varying cross-sectional area: <br>1. *Resonances (Formants):* Natural resonant frequencies ($F_1, F_2, F_3$) amplify sound energy. <br>2. *Articulators:* Tongue and lips alter cavity shapes to produce distinct vowels and consonants. | Imparts spectral envelope and phonemic identity. |
| **Radiation $R(z)$** | Lips & Mouth Opening | Lip radiation impedance $R(z) \\approx 1 - z^{-1}$, acting as a high-pass filter that boosts high frequencies by $+6\\text{ dB/octave}$. | Radiates acoustic wave into free air. |

---

### 4. Summary & Practical Insight
* **Voiced Speech:** Periodic glottal pulse excitation $E(z)$ filtered by all-pole vocal tract $H(z)$ (e.g., vowels /a/, /e/, /i/).
* **Unvoiced Speech:** White noise excitation $E(z)$ filtered by vocal tract constriction (e.g., /s/, /f/, /t/).
* In Automatic Speech Recognition (ASR), articulation is the primary stage affecting clarity; poor articulation leads to mispronunciation and recognition errors."""
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
        "punchline": "Analog speech x(t) is discretized by sampling x[n] = x(nT). By Nyquist theorem fs >= 2fmax; undersampling causes aliasing distortion, prevented by anti-aliasing LPF.",
        "content": """### 1. Continuous vs. Discrete-Time Speech Signals
* **Continuous-Time Signal $x(t)$:** Naturally produced analog speech waveform defined for all continuous time instants $t$, containing infinite values between any two points.
* **Discrete-Time Signal $x[n]$:** Defined only at discrete time instances $n$, obtained by sampling the continuous signal at uniform time intervals $T$:
  $$x[n] = x(nT), \\quad n \\in \\mathbb{Z}$$
  where $T$ is the **sampling period** and $f_s = 1/T$ is the **sampling frequency**.

| Feature | Continuous-Time Speech $x(t)$ | Discrete-Time Speech $x[n]$ |
| :--- | :--- | :--- |
| **Definition** | Defined for all time $t$ | Defined only at discrete sample indices $n$ |
| **Values** | Infinite/uncountable values | Finite sequence of numbers |
| **Processing** | Analog circuits (amplifiers, analog filters) | Digital systems, DSP chips, microprocessors |
| **Storage & Transmission** | Prone to noise, degradation during transmission | Stored as digital bits (WAV, MP3), easily compressed and error-corrected |

---

### 2. Sampling Process & Nyquist Theorem
Sampling converts continuous acoustic pressure into a sequence of discrete numbers:
1. **Sampling Process:** Continuous signal $x(t)$ is sampled at uniform time intervals $T$ to create the sequence $x[n] = x[0], x[T], x[2T], x[3T], \\dots$.
2. **Nyquist Sampling Criterion:**
   $$f_s \\ge 2 \\cdot f_{\\max}$$
   To accurately capture and reconstruct a continuous signal without loss of information, the sampling frequency $f_s$ must be at least twice the maximum frequency component ($f_{\\max}$) present in the signal.
   * *Example:* For telephone-quality speech with $f_{\\max} = 4\\text{ kHz}$, the minimum Nyquist rate is $f_s = 2 \\times 4 = 8\\text{ kHz}$.
   * *Example:* For wideband speech recognition with $f_{\\max} = 8\\text{ kHz}$, minimum $f_s = 16\\text{ kHz}$.

---

### 3. Effects of Sampling on Signal Reconstruction
1. **Proper Sampling ($f_s \\ge 2 f_{\\max}$):**
   * Periodic spectral replicas in the frequency domain are spaced sufficiently far apart with no overlap.
   * The original continuous signal can be perfectly reconstructed using an ideal low-pass filter (Sinc interpolation):
     $$x_r(t) = \\sum_{n=-\\infty}^{\\infty} x[n] \\cdot \\text{sinc}\\left(\\frac{t - nT}{T}\\right)$$
2. **Undersampling & Aliasing ($f_s < 2 f_{\\max}$):**
   * When $f_s$ is too low, adjacent spectral replicas overlap (spectral folding).
   * High-frequency components fold back and masquerade as false low-frequency components.
   * *Impact on Speech:* Distorted, muffled audio; loss of high-frequency unvoiced consonants (such as /s/, /f/, /t/); severe degradation of speech intelligibility in speech recognition.
3. **Anti-Aliasing Filter:**
   * An analog low-pass filter (LPF) with cutoff $f_c \\le f_s/2$ is placed before the ADC to eliminate any frequency components above the Nyquist limit before sampling.

---

### 4. Frame-Based Processing of Speech
* Speech is globally non-stationary, but its physical vocal tract shape changes slowly.
* Therefore, discrete speech is segmented into short, overlapping **frames of 20–30 ms** (assumed stationary within each frame) with a frame shift of 10 ms for short-time spectral analysis (STFT, MFCC)."""
    },
    {
        "id": "MID1-Q03",
        "mid": "Mid-I",
        "qno": 3,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "A system is described by: Find the zeros by solving the numerator. Find the poles by solving the denominator. Comment on stability",
        "punchline": "H(z) = [z(z - 0.5)] / [z^2 - 0.9z + 0.2]. Zeros at z=0, 0.5. Poles at p=0.5, 0.4. Because all poles lie inside the unit circle (|p| < 1), the system is BIBO Stable.",
        "content": """### 1. Given System Transfer Function
The system is modeled by the rational discrete-time transfer function:
$$H(z) = \\frac{B(z)}{A(z)} = \\frac{z(z - 0.5)}{z^2 - 0.9z + 0.2}$$

---

### 2. Task 1: Find Zeros by Solving the Numerator
The zeros of $H(z)$ are the roots of the numerator polynomial $B(z) = 0$:
$$B(z) = z(z - 0.5) = 0$$

Setting each factor to zero:
1. $z_1 = 0$
2. $z - 0.5 = 0 \\implies z_2 = 0.5$

$$\\mathbf{\\text{Zeros: }} z_1 = 0, \\quad z_2 = 0.5$$

*Physical Meaning in Speech:* Zeros represent **anti-resonances** where signal energy is trapped or cancelled (such as through nasal coupling in sounds like /m/, /n/ or vocal tract bifurcations). At $z = z_i$, $H(z_i) = 0$, producing sharp dips/notches in the frequency spectrum.

---

### 3. Task 2: Find Poles by Solving the Denominator
The poles of $H(z)$ are the roots of the denominator polynomial $A(z) = 0$:
$$A(z) = z^2 - 0.9z + 0.2 = 0$$

Factoring the quadratic equation:
$$(z - 0.5)(z - 0.4) = 0$$

Setting each factor to zero:
1. $z - 0.5 = 0 \\implies p_1 = 0.5$
2. $z - 0.4 = 0 \\implies p_2 = 0.4$

$$\\mathbf{\\text{Poles: }} p_1 = 0.5, \\quad p_2 = 0.4$$

*Note on Pole-Zero Cancellation:* The zero at $z = 0.5$ cancels the pole at $p = 0.5$, reducing the effective irreducible transfer function to:
$$H_{\\text{red}}(z) = \\frac{z}{z - 0.4}$$
with an active pole at $p = 0.4$ and zero at $z = 0$.

*Physical Meaning in Speech:* Poles represent natural **acoustic resonances (Formants)** of the vocal tract. Near a pole, $A(z) \\to 0$, causing $H(z)$ to peak sharply and amplify vocal energy (formants $F_1, F_2, F_3$).

---

### 4. Task 3: Comment on Stability
* **Stability Criterion:** A causal discrete-time LTI system is Bounded-Input Bounded-Output (**BIBO**) stable if and only if **all its poles strictly lie inside the unit circle** in the complex z-plane:
  $$|p_i| < 1 \\quad \\forall i$$
* **Evaluation:**
  * For $p_1 = 0.5$: $|p_1| = 0.5 < 1$ (inside unit circle)
  * For $p_2 = 0.4$: $|p_2| = 0.4 < 1$ (inside unit circle)

**Conclusion:** Since all poles have magnitude strictly less than 1, the Region of Convergence (ROC) includes the unit circle $|z| = 1$. Therefore, the system is **BIBO Stable**."""
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
        "punchline": "FFT reduces DFT computation from O(N^2) to O(N log N). Key properties: Linearity, Conjugate Symmetry, Time-Shift, Frequency Resolution, Parsevals Energy, and Periodicity/Windowing.",
        "content": """### 1. Role of Fast Fourier Transform (FFT) in Speech Processing
Speech signals are non-stationary, time-varying signals. To recognize speech, smartphones and ASR systems must identify frequency components (pitch, formants, harmonic distribution).
* Direct computation of the Discrete Fourier Transform (DFT) requires $O(N^2)$ complex operations.
* The **Fast Fourier Transform (FFT)** is an efficient algorithm that computes the exact DFT in **$O(N \\log_2 N)$** operations. For a 1024-point frame, FFT is $\\approx 100\\times$ faster than direct DFT, enabling real-time voice analysis.

---

### 2. Six Key Properties of FFT for Speech Systems
The official curriculum highlights six fundamental properties:

1. **Property 1 — Linearity:**
   * *Definition:* If $x_1[n] \\leftrightarrow X_1[k]$ and $x_2[n] \\leftrightarrow X_2[k]$, then:
     $$a x_1[n] + b x_2[n] \\longleftrightarrow a X_1[k] + b X_2[k]$$
   * *Speech Relevance:* Preserves linear superposition of speech and background noise, allowing noise estimation, spectral subtraction, and multi-speaker separation.
2. **Property 2 — Conjugate Symmetry (Real-Valued Signals):**
   * *Definition:* For real-valued speech samples $x[n] \\in \\mathbb{R}$:
     $$X[N - k] = X^*[k]$$
   * *Speech Relevance:* The negative frequency spectrum is a redundant mirror image of positive frequencies. Only the first $N/2 + 1$ bins (from $0$ to $f_s/2$) need to be computed and stored, cutting memory and computation in half for MFCC extraction.
3. **Property 3 — Time-Shifting:**
   * *Definition:* Shifting speech in time by $n_0$ samples introduces only a phase shift:
     $$x[n - n_0] \\longleftrightarrow X[k] \\cdot e^{-j \\frac{2\\pi}{N} k n_0}$$
   * *Speech Relevance:* The **magnitude spectrum $|X[k]|$ is invariant to time delays**. This ensures that the extracted spectral envelope of a phoneme is robust to minor alignment offsets in speech segmentation.
4. **Property 4 — Frequency Resolution:**
   * *Definition:* The frequency spacing between adjacent FFT bins is:
     $$\\Delta f = \\frac{f_s}{N}$$
   * *Speech Relevance:* Finer resolution (larger $N$) resolves individual pitch harmonics, while coarser resolution (smaller $N$) smooths harmonics into vocal tract formant envelopes.
5. **Property 5 — Energy Conservation (Parseval's Theorem):**
   * *Definition:* Total energy in time domain equals total energy in frequency domain:
     $$\\sum_{n=0}^{N-1} |x[n]|^2 = \\frac{1}{N} \\sum_{k=0}^{N-1} |X[k]|^2$$
   * *Speech Relevance:* Energy can be reliably measured in the spectral domain, forming the core basis for **Voice Activity Detection (VAD)** and frame energy thresholding.
6. **Property 6 — Periodicity Assumption & Windowing:**
   * *Definition:* FFT assumes the $N$-point finite frame repeats infinitely. Abrupt truncations at frame boundaries cause high-frequency spectral leakage.
   * *Speech Relevance:* Speech frames are multiplied by a smooth **tapering window (Hamming window)** before FFT, minimizing boundary discontinuities and enabling reliable **Short-Time Fourier Transform (STFT)**."""
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
        "punchline": "Speech is modeled as s[n] = e[n] * h[n]. Time convolution equals frequency multiplication S(z) = E(z)H(z). Real-time streaming is implemented via Overlap-Add (OLA).",
        "content": """### 1. Mathematical Formulation of Convolution
Convolution is the fundamental operation relating the input, impulse response, and output of a Linear Time-Invariant (LTI) system:
$$y[n] = x[n] * h[n] = \\sum_{k=-\\infty}^{\\infty} x[k] \\cdot h[n - k]$$

In the frequency/z-domain, time convolution translates to direct multiplication:
$$Y(z) = X(z) \\cdot H(z) \\iff Y(\\omega) = X(\\omega) \\cdot H(\\omega)$$

---

### 2. Role in Speech Generation: The Source-Filter Formulation
In speech acoustics, speech production is formulated directly as a convolution of the vocal cord excitation source with the vocal tract acoustic filter:
$$s[n] = e[n] * h[n] = e[n] * v[n] * r[n]$$
* $e[n]$: Glottal excitation source (periodic glottal pulse train for voiced speech, turbulent noise for unvoiced speech).
* $v[n]$: Impulse response of vocal tract tube (pharynx, oral, and nasal cavities) exhibiting resonant formants.
* $r[n]$: Lip radiation impulse response ($r[n] = \\delta[n] - \\delta[n-1]$).
* In frequency domain: $S(z) = E(z) \\cdot V(z) \\cdot R(z)$. The vocal tract acts as a spectral shaping filter on the excitation harmonics.

---

### 3. Role in Speech Filtering Mechanisms
1. **Pre-emphasis High-Pass Filtering:**
   * Natural voiced speech rolls off at $-6\\text{ dB/octave}$ due to glottal aerodynamics.
   * Applying FIR convolution $y[n] = x[n] - \\alpha x[n-1]$ (with $\\alpha \\approx 0.95 - 0.97$) boosts high-frequency formants and balances spectral energy.
2. **Anti-Aliasing Low-Pass Filtering:**
   * Convolving analog speech with a continuous LPF kernel before ADC bandlimits the spectrum to $f_s/2$, preventing destructive aliasing.
3. **Formant Filtering (Bandpass Filter Banks):**
   * Filter banks convolve speech with tuned bandpass filters to isolate individual formant bands ($F_1, F_2, F_3$) for speech recognition.

---

### 4. Real-Time Streaming Convolution: Overlap-Add (OLA) Method
Direct time-domain convolution of an ongoing speech stream is computationally intractable ($O(L \\cdot M)$). Practical DSP systems use block convolution via Fast Fourier Transform:

* **Problem:** Linear convolution of a speech block of length $L$ with filter of length $M$ produces an output of length $L + M - 1$. Direct FFT multiplication produces circular convolution with time-aliasing.
* **Overlap-Add (OLA) Algorithm:**
  1. Segment speech stream into non-overlapping blocks $x_i[n]$ of length $L$.
  2. Zero-pad each block to length $N \\ge L + M - 1$.
  3. Compute FFT: $X_i[k] = \\text{FFT}\\{x_i[n]\\}$ and multiply with filter spectrum: $Y_i[k] = X_i[k] \\cdot H[k]$.
  4. Compute IFFT: $y_i[n] = \\text{IFFT}\\{Y_i[k]\\}$ of length $L + M - 1$.
  5. The last $M - 1$ samples of block $i$ overlap with the first $M - 1$ samples of block $i+1$. Add overlapping tails to assemble the continuous real-time output.

---

### 5. Summary Table

| Convolution Domain | Implementation | Computational Complexity | Primary Role in Speech Systems |
| :--- | :--- | :--- | :--- |
| **Time-Domain FIR** | Direct difference equation | $O(L \\cdot M)$ | Short filters (pre-emphasis, simple smoothing) |
| **Frequency-Domain FFT** | Multiplication $X[k] \\cdot H[k]$ | $O(N \\log N)$ | Fast acoustic simulation, room reverberation modeling |
| **Overlap-Add (OLA)** | Block FFT with tail addition | $O((L+M) \\log(L+M))$ | Real-time streaming speech processing, VoIP noise cancellation |"""
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
        "punchline": "Linear filter banks use fixed FIR/IIR bands (predictable, good for formants). Non-linear filter banks (Mel/Wavelet/EMD) adapt to human hearing and speech non-stationarity.",
        "content": """### 1. Introduction to Filter Banks in Speech Processing
A filter bank is an array of bandpass filters that separates an input speech signal into multiple subband components.
Filter banks are evaluated using two critical criteria:
1. **Frequency Resolution:** Ability to separate closely spaced spectral components (harmonics, formants).
2. **Distortion (Signal Preservation):** The degree to which the filter bank preserves speech waveforms without introducing phase/amplitude errors or aliasing.

---

### 2. Frequency Resolution Analysis
1. **Linear Filter Banks (Uniform Bandwidth):**
   * *Design:* Divides the spectrum into uniformly spaced, fixed-bandwidth channels (e.g., uniform STFT filter banks where each filter has constant $\\Delta f = 100\\text{ Hz}$).
   * *Advantages:* Well-defined frequency bands, high control over passband ripple and stopband attenuation; excellent resolution at high frequencies.
   * *Limitations:* Fixed resolution cannot adapt to signal variations; poor resolution at low frequencies compared to the human ear; constrained by the time-frequency uncertainty principle ($\\Delta t \\cdot \\Delta f \\ge 1/4\\pi$).
2. **Non-Linear Filter Banks (Perceptual & Adaptive):**
   * *Design:* Bandwidths increase non-linearly with frequency, matching human cochlear perception (e.g., **Mel Filter Banks**, Bark scale, Wavelet packets, Empirical Mode Decomposition EMD).
   * *Characteristics:*
     * *Low Frequencies (< 1 kHz):* Narrow bandwidths with high frequency resolution, capturing fine pitch harmonics and lower formants ($F_1, F_2$).
     * *High Frequencies (> 1 kHz):* Broad bandwidths with high time resolution, capturing transient bursts, frication noise, and spectral energy envelopes.
   * *Advantages:* Aligns with human psychoacoustic tonotopy; captures non-stationary transients (plosives, stop bursts) far better than linear filters.
   * *Limitations:* Irregular frequency bands make perfect waveform reconstruction mathematically difficult.

---

### 3. Distortion Analysis (Signal Preservation)
1. **Linear Filter Banks:**
   * *Distortion Sources:* Filter design imperfections, transition band overlap, subband aliasing due to downsampling, and phase distortion in IIR filters.
   * *Performance:* If designed using linear-phase FIR filters or Perfect Reconstruction Quadrature Mirror Filters (PR-QMF), linear filter banks achieve **low distortion** and near-perfect waveform reconstruction.
2. **Non-Linear Filter Banks:**
   * *Distortion Sources:* Non-linear frequency warping, adaptive decomposition errors, and mode-mixing (in EMD).
   * *Performance:* May introduce phase and amplitude distortions. However, in Automatic Speech Recognition (ASR), waveform reconstruction is not required—the goal is **phoneme discriminability**, where non-linear Mel filter banks significantly outperform linear filters.

---

### 4. Comprehensive Comparison Table

| Performance Criterion | Linear Filter Banks (Uniform STFT / FIR) | Non-Linear Filter Banks (Mel Scale / Wavelets / EMD) |
| :--- | :--- | :--- |
| **Bandwidth Distribution** | Constant bandwidth across all frequencies ($\\Delta f = \\text{constant}$) | Logarithmic / Mel spacing: Narrow at low frequencies, wide at high frequencies |
| **Biological Alignment** | Mathematical grid; ignores human auditory perception | Directly models human cochlear critical bands |
| **Frequency Resolution** | Equal across entire spectrum; suboptimal for speech | High frequency resolution at low frequencies (< 1 kHz) |
| **Time Resolution** | Equal across entire spectrum | High temporal resolution at high frequencies (captures plosives/bursts) |
| **Signal Distortion** | Low distortion; supports perfect waveform reconstruction | Higher reconstruction distortion; mode-mixing possible in EMD |
| **Computational Complexity** | Highly efficient via uniform FFT algorithms ($O(N \\log N)$) | Moderate to high (filter bank weighting, DWT tree traversal) |
| **Primary Speech Applications** | Speech synthesis resynthesis, audio coding, echo cancellation | Speech recognition (MFCC), speaker identification, emotion detection |"""
    },
    {
        "id": "MID1-Q07",
        "mid": "Mid-I",
        "qno": 7,
        "unit": "Unit-1",
        "co": "CO1",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "A) A short speech frame is given as: Compute the 4-point DFT . Find the magnitude spectrum . Identify the dominant frequency component. b) A speech signal is sampled at 8 kHz and frame size is 256 samples. Compute frequency resolution: Find the frequency corresponding to k = 10.",
        "punchline": "Part A: x[n]=[2,1,0,1] -> X=[4, 2, 0, 2], Magnitudes=[4, 2, 0, 2], Dominant DC at k=0 and AC at k=1,3. Part B: fs=8kHz, N=256 -> Resolution df = 31.25 Hz/bin, f10 = 312.5 Hz.",
        "content": """### PART A: 4-Point DFT Computation

#### 1. Problem Statement & Given Data
A short speech frame is given as:
$$x[n] = [2, 1, 0, 1] \\quad \\text{for } n = 0, 1, 2, 3 \\quad (N = 4)$$

#### 2. Formula & Twiddle Factor Matrix
The $N$-point Discrete Fourier Transform (DFT) equation is:
$$X[k] = \\sum_{n=0}^{N-1} x[n] \\cdot W_N^{kn} = \\sum_{n=0}^{3} x[n] \\cdot e^{-j \\frac{2\\pi}{4} kn}$$

For $N = 4$, $W_4 = e^{-j \\frac{2\\pi}{4}} = e^{-j \\pi/2} = -j$.
The $4 \\times 4$ Twiddle factor matrix is:
$$\\begin{bmatrix} X[0] \\\\ X[1] \\\\ X[2] \\\\ X[3] \\end{bmatrix} = \\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -j & -1 & j \\\\ 1 & -1 & 1 & -1 \\\\ 1 & j & -1 & -j \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\\\ 1 \\end{bmatrix}$$

#### 3. Step-by-Step Computation
* **For $k = 0$ (DC Component):**
  $$X[0] = 2(1) + 1(1) + 0(1) + 1(1) = 2 + 1 + 0 + 1 = \\mathbf{4}$$
* **For $k = 1$:**
  $$X[1] = 2(1) + 1(-j) + 0(-1) + 1(j) = 2 - j + 0 + j = \\mathbf{2}$$
* **For $k = 2$:**
  $$X[2] = 2(1) + 1(-1) + 0(1) + 1(-1) = 2 - 1 + 0 - 1 = \\mathbf{0}$$
* **For $k = 3$:**
  $$X[3] = 2(1) + 1(j) + 0(-1) + 1(-j) = 2 + j + 0 - j = \\mathbf{2}$$

Resulting DFT sequence:
$$\\mathbf{X[k] = [4, 2, 0, 2]}$$

#### 4. Magnitude Spectrum $|X[k]|$
$$|X[k]| = \\sqrt{\\text{Re}\\{X[k]\\}^2 + \\text{Im}\\{X[k]\\}^2}$$
* $|X[0]| = |4| = \\mathbf{4.0}$
* $|X[1]| = |2| = \\mathbf{2.0}$
* $|X[2]| = |0| = \\mathbf{0.0}$
* $|X[3]| = |2| = \\mathbf{2.0}$

#### 5. Identification of Dominant Frequency Component
* The overall maximum energy is at **$k = 0$** with magnitude **$|X[0]| = 4.0$** (the DC / baseline average component).
* The dominant AC speech frequency components are at **$k = 1$** and **$k = 3$** with magnitude **$2.0$**. (Notice conjugate symmetry: $X[3] = X^*[1]$).

---

### PART B: Frequency Resolution Problem

#### 1. Given Data
* Sampling Frequency: $f_s = 8\\text{ kHz} = 8000\\text{ Hz}$
* Frame Size / FFT Length: $N = 256\\text{ samples}$

#### 2. Task 1: Compute Frequency Resolution ($\\Delta f$)
Frequency resolution is defined as the frequency spacing between adjacent DFT bins:
$$\\Delta f = \\frac{f_s}{N}$$
$$\\Delta f = \\frac{8000\\text{ Hz}}{256} = \\mathbf{31.25\\text{ Hz/bin}}$$

#### 3. Task 2: Find Frequency Corresponding to Bin $k = 10$
The continuous analog frequency $f_k$ represented by the $k$-th DFT bin is:
$$f_k = k \\cdot \\Delta f = k \\cdot \\frac{f_s}{N}$$
For $k = 10$:
$$f_{10} = 10 \\times 31.25\\text{ Hz} = \\mathbf{312.5\\text{ Hz}}$$

*Speech Interpretation:* A frequency of $312.5\\text{ Hz}$ falls within the first formant frequency ($F_1$) range of close vowels (such as /u/ and /i/) and corresponds to the pitch range of adult female and child speech."""
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
        "punchline": "LPC predicts s[n] as weighted sum of p past samples. Minimizing error gives Yule-Walker equations, solved via Levinson-Durbin O(p^2) to estimate all-pole vocal tract formants.",
        "content": """### 1. Fundamental Concept of LPC
Linear Predictive Coding (LPC) is a cornerstone speech processing technique that models a speech signal by estimating the current speech sample as a **linear combination of its past $p$ samples**.
Instead of storing or transmitting raw speech samples, LPC extracts and transmits a compact set of prediction coefficients ($a_k$) representing the vocal tract filter and a gain/pitch parameter representing excitation.

---

### 2. Mathematical Formulation of LPC
1. **Prediction Equation:**
   The predicted speech sample $\\hat{s}[n]$ is given by:
   $$\\hat{s}[n] = \\sum_{k=1}^{p} a_k \\cdot s[n - k]$$
   where $p$ is the **prediction order** (typically $p = 10-14$ for 8-16 kHz speech) and $a_k$ are the linear predictor coefficients.
2. **Prediction Error (Residual):**
   The prediction error $e[n]$ is the difference between the actual speech sample and the predicted value:
   $$e[n] = s[n] - \\hat{s}[n] = s[n] - \\sum_{k=1}^{p} a_k \\cdot s[n - k]$$
3. **Derivation of Yule-Walker Equations (Minimizing Error):**
   To find the optimal coefficients $a_k$, we minimize the total squared prediction error $E$:
   $$E = \\sum_{n} e^2[n] = \\sum_{n} \\left( s[n] - \\sum_{k=1}^{p} a_k s[n - k] \\right)^2$$
   Setting the partial derivative with respect to each coefficient $a_j$ to zero:
   $$\\frac{\\partial E}{\\partial a_j} = -2 \\sum_{n} \\left( s[n] - \\sum_{k=1}^{p} a_k s[n - k] \\right) s[n - j] = 0$$
   $$\\sum_{k=1}^{p} a_k \\left[ \\sum_{n} s[n - k] s[n - j] \\right] = \\sum_{n} s[n] s[n - j]$$
   Recognizing the autocorrelation function $R(|j - k|) = \\sum_{n} s[n - j] s[n - k]$, this yields the **Yule-Walker Equations**:
   $$\\sum_{k=1}^{p} a_k \\cdot R(|j - k|) = R(j), \\quad \\text{for } j = 1, 2, \\dots, p$$

4. **Matrix Representation & Solution:**
   $$\\begin{bmatrix} R(0) & R(1) & \\dots & R(p-1) \\\\ R(1) & R(0) & \\dots & R(p-2) \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ R(p-1) & R(p-2) & \\dots & R(0) \\end{bmatrix} \\begin{bmatrix} a_1 \\\\ a_2 \\\\ \\vdots \\\\ a_p \\end{bmatrix} = \\begin{bmatrix} R(1) \\\\ R(2) \\\\ \\vdots \\\\ R(p) \\end{bmatrix}$$
   The autocorrelation matrix is symmetric and Toeplitz, solved efficiently using the **Levinson-Durbin Recursion** in **$O(p^2)$** operations (compared to $O(p^3)$ for Gaussian elimination).

---

### 3. Speech Synthesis Filter Model
The speech production system is modeled as an **all-pole filter** excited by an excitation source $e[n]$ with gain $G$:
$$H(z) = \\frac{S(z)}{E(z)} = \\frac{G}{1 - \\sum_{k=1}^{p} a_k z^{-k}} = \\frac{G}{A(z)}$$
The roots of the denominator polynomial $A(z) = 0$ determine the poles, which directly correspond to the **formant frequencies** of the vocal tract.

---

### 4. Evaluation of LPC Effectiveness in Speech Modeling

| Aspect | Advantages & Strengths | Limitations & Constraints |
| :--- | :--- | :--- |
| **Parameter Efficiency** | Compresses speech to a small set of parameters ($p$ coefficients + gain + pitch), enabling low bitrates (e.g., 2.4 kbps in military LPC-10). | Assumes an all-pole model; fails to represent nasal sounds (/m/, /n/) and fricatives that require spectral zeros. |
| **Acoustic Modeling** | Highly accurate for voiced vowel segments; poles directly map to vocal tract resonances ($F_1, F_2, F_3$). | Assumes speech is stationary within each frame; degraded by fast pitch transitions. |
| **Computational Cost** | Levinson-Durbin solves the system in $O(p^2)$ operations; easily implemented in real-time embedded DSPs. | Sensitive to acoustic background noise and channel distortion; error energy increases under low SNR. |
| **Applications** | Cellular communications (GSM vocoders), text-to-speech (TTS) synthesis, formant extraction, speaker recognition. | Not optimal for unvoiced sounds or high-fidelity musical audio. |"""
    }
]
