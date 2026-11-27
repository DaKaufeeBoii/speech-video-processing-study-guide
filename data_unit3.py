# -*- coding: utf-8 -*-
"""
Unit 3: Multi-Dimensional Signals, Transforms, Sampling & Digital Video Representation
Questions: Mid-I Q17 to Q20 AND Mid-II Q1 to Q4
Course Coordinator: Dr. Sandeep Kumar M (CSE AI & ML)
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408
Strictly aligned with Unit 3.docx lecture notes and official Question Bank.
"""

UNIT3_QUESTIONS = [
    {
        "id": "MID1-Q17",
        "mid": "Mid-I",
        "qno": 17,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Interpret the characteristics and representation of multi-dimensional signals and examine their significance in advanced signal processing applications.",
        "punchline": "Multi-dimensional (M-D) signals depend on two or more independent spatial or temporal variables (e.g., 2D image f(x,y), 3D video f(x,y,t)); they are governed by spatial correlation, non-causality, and high data dimensionality.",
        "mnemonic": "S-T-V-M: Spatial 2D, Temporal 3D, Volumetric CT/MRI, Massive bandwidth.",
        "analogy": "A 1D audio recording is like a single thread of yarn passing through time; a 2D image is like a woven fabric sheet with width and height; a 3D video is a continuous stack of fabric sheets moving through a loom.",
        "diagram": """+-------------------------------------------------------------------------------+
|                    MULTI-DIMENSIONAL SIGNAL TAXONOMY                          |
+-------------------------------------------------------------------------------+
  1D Signal (Speech)         : s(t)          ──► Amplitude vs 1D Time
  2D Signal (Still Image)    : f(x, y)       ──► Brightness vs (X, Y) Spatial axes
  3D Signal (Digital Video)  : f(x, y, t)    ──► 2D Spatial frames across Time t
  3D Signal (Volumetric CT)  : f(x, y, z)    ──► 3D Voxel density in physical space
  4D Signal (Dynamic MRI)    : f(x, y, z, t) ──► Beating heart volume over Time

 CORE CHARACTERISTICS:
  1. Multi-axis dependency: f(x₁, x₂, ..., xₘ)
  2. Spatial/Temporal correlation: Neighboring samples share high mutual information
  3. Non-causality: Pixels in an image exist simultaneously in all directions
  4. Massive data volume: Uncompressed 1080p video requires ~1.5 Gbps bandwidth""",
        "content": """### 1. Definition and Mathematical Representation (Unit 3 Notes)
A **Multi-Dimensional (M-D) signal** is a physical phenomenon whose amplitude varies as a function of two or more independent spatial or temporal coordinates:
1. **2D Signals (Still Images):**
   Continuous representation $f(x, y)$ or sampled discrete matrix $f[m, n]$, where $x, y$ are orthogonal spatial coordinates and $f$ represents optical luminance or RGB color vectors $[R, G, B]^T$.
2. **3D Signals:**
   - **Digital Video:** $f(x, y, t)$, where $(x, y)$ are spatial coordinates and $t$ is continuous time.
   - **Volumetric Medical Imaging (CT / MRI):** $f(x, y, z)$, representing 3D tissue attenuation coefficients or proton densities.
3. **4D Signals (Dynamic Spatio-Temporal Volumes):**
   - Dynamic cardiac MRI: $f(x, y, z, t)$, capturing the structural deformation of a 3D organ volume over time.

---

### 2. Core Characteristics of Multi-Dimensional Signals
1. **Spatial & Temporal Correlation:**
   Adjacent spatial pixels share nearly identical grayscale and chromatic values (**spatial redundancy**). Successive frames in video sequences contain over $90\\%$ identical background pixels (**temporal redundancy**).
2. **Non-Causal Nature in Spatial Dimensions:**
   Unlike 1D audio signals where causality is strictly enforced (future depends on past), 2D spatial dimensions $(x, y)$ are **non-causal**. Pixels can be filtered using neighbors in all four directions (left, right, top, bottom) simultaneously.
3. **Separable Signals:**
   An $M$-D signal is separable if it can be factored into a product of 1D functions:
   $$f(x, y) = f_1(x) \\cdot f_2(y)$$
   Separability dramatically reduces computational complexity from $O(N^2)$ to $O(2N)$ for 2D transforms and filtering.
4. **Massive Bandwidth & Storage Demand:**
   An uncompressed full HD video ($1920 \\times 1080$ pixels, 24-bit color, 30 frames/sec) generates:
   $$1920 \\times 1080 \\times 3 \\times 30 \\approx 186.6\\text{ MB/s} = 1.49\\text{ Gbps}$$
   necessitating advanced multi-dimensional compression algorithms.

---

### 3. Significance in Advanced Signal Processing Applications
- **Computer Vision & Autonomous Navigation:** Object detection, semantic segmentation, and optical flow estimation rely on spatio-temporal gradient analysis across $f(x, y, t)$.
- **Medical Imaging:** 3D CT/MRI reconstruction, ultrasound beamforming, and tumor volume segmentation require 3D filtering and multi-planar reformatting.
- **Satellite Remote Sensing:** Multi-spectral and hyperspectral imaging ($f(x, y, \\lambda)$) capture multi-band surface reflectance for environmental and agricultural monitoring.
- **Broadcast & Streaming:** Standards such as H.264/AVC, H.265/HEVC, and AV1 exploit multi-dimensional redundancy to deliver ultra-high-definition streaming over consumer bandwidths."""
    },
    {
        "id": "MID1-Q18",
        "mid": "Mid-I",
        "qno": 18,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "Demonstrate the application of multi-dimensional transforms (2D-DFT) for analyzing signal representation in spatial and frequency domains.",
        "punchline": "The 2D-DFT decomposes a spatial image into orthogonal 2D sinusoidal plane waves; its separability enables efficient O(N² log N) computation, while its energy compaction concentrates image power into low-frequency DC/AC coefficients.",
        "mnemonic": "S-S-C-E: Separability, Shift property, Conjugate symmetry, Energy compaction.",
        "analogy": "Analyzing an image with 2D-DFT is like shining light through a prism to reveal the individual pure colors that create a composite sunset, where smooth sky corresponds to central low frequencies and sharp tree silhouettes correspond to outer high frequencies.",
        "diagram": """+-------------------------------------------------------------------------------+
|                    2D-DFT SPATIAL TO FREQUENCY MAPPING                        |
+-------------------------------------------------------------------------------+

  SPATIAL DOMAIN f[m, n] (N x N)              FREQUENCY SPECTRUM |F[u, v]|
  ┌────────────────────────────┐              ┌────────────────────────────┐
  │                            │              │ \\        High Freq       / │
  │       Smooth Regions       │              │  \\                      /  │
  │      (Low variations)      │   2D-DFT     │   \\    • (u, v)        /   │
  │                            │ ──────────►  │    • DC Center (0, 0) •    │
  │      Sharp Edges & Lines   │              │   /  (High Energy Peak)\\   │
  │      (High variations)     │              │  /                      \\  │
  │                            │              │ /        High Freq       \\ │
  └────────────────────────────┘              └────────────────────────────┘
   Row-by-Row 1D-FFT  ──►  Column-by-Column 1D-FFT  ==> O(N² log N) Efficiency""",
        "content": """### 1. Mathematical Formulation of the 2D-DFT
The **2D Discrete Fourier Transform (2D-DFT)** converts a 2D discrete spatial image $f[m, n]$ of size $M \\times N$ into a 2D discrete frequency spectrum $F[u, v]$:
$$F[u, v] = \\sum_{m=0}^{M-1} \\sum_{n=0}^{N-1} f[m, n] \\, e^{-j 2\\pi \\left( \\frac{um}{M} + \\frac{vn}{N} \\right)}, \\quad 0 \\le u \\le M-1, \\ 0 \\le v \\le N-1$$

The **2D Inverse Discrete Fourier Transform (2D-IDFT)** perfectly reconstructs the spatial signal:
$$f[m, n] = \\frac{1}{M N} \\sum_{u=0}^{M-1} \\sum_{v=0}^{N-1} F[u, v] \\, e^{j 2\\pi \\left( \\frac{um}{M} + \\frac{vn}{N} \\right)}$$

---

### 2. Key Properties in Spatial and Frequency Domains
1. **Separability:**
   The 2D Fourier kernel is the product of two 1D kernels:
   $$e^{-j 2\\pi \\left( \\frac{um}{M} + \\frac{vn}{N} \\right)} = e^{-j 2\\pi \\frac{um}{M}} \\cdot e^{-j 2\\pi \\frac{vn}{N}}$$
   This allows the 2D-DFT to be computed as:
   - **Step 1:** Compute 1D-FFT along every row ($M$ rows of size $N$).
   - **Step 2:** Compute 1D-FFT along every column of the result ($N$ columns of size $M$).
   - **Complexity:** Reduces computation from brute-force $O(M^2 N^2)$ to $O(M N \\log_2(M N))$.

2. **Conjugate Symmetry:**
   For real-valued image inputs ($f[m, n] \\in \\mathbb{R}$):
   $$F[-u, -v] = F^*[u, v] \\implies |F[-u, -v]| = |F[u, v]|$$
   The magnitude spectrum is symmetric about the DC origin $(0, 0)$.

3. **Spatial Shift $\\leftrightarrow$ Frequency Phase Shift:**
   $$f[m - m_0, n - n_0] \\stackrel{\\mathcal{F}}{\\longleftrightarrow} F[u, v] \\, e^{-j 2\\pi \\left( \\frac{u m_0}{M} + \\frac{v n_0}{N} \\right)}$$
   Translating an image in space alters only the phase spectrum, leaving the magnitude spectrum $|F[u, v]|$ completely invariant.

4. **Energy Compaction:**
   In natural images, pixel intensities change gradually. Consequently, over $90\\%$ of total signal energy is concentrated in the low-frequency DC component $F[0, 0]$ (average brightness) and low-order AC coefficients near the origin.

---

### 3. Application in Spatial & Frequency Domain Analysis
- **Magnitude vs Phase Interpretation:** The magnitude $|F[u, v]|$ indicates contrast and periodicity strength at specific orientations, while the phase $\\angle F[u, v]$ preserves structural edge geometry and object locations.
- **Frequency-Domain 2D Filtering:**
  $$G[u, v] = F[u, v] \\cdot H[u, v] \\implies g[m, n] = \\text{IDFT}\\{G[u, v]\\}$$
  - **Ideal / Gaussian Low-Pass Filter ($H_{LP}$):** Passes central frequencies, suppresses high frequencies $\\implies$ performs image smoothing and noise removal.
  - **High-Pass Filter ($H_{HP}$):** Attenuates DC, passes high spatial frequencies $\\implies$ detects sharp edges and object boundaries."""
    },
    {
        "id": "MID1-Q19",
        "mid": "Mid-I",
        "qno": 19,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K4",
        "marks": "10 Marks",
        "title": "Analyze the formulation of multi-dimensional system models and evaluate their performance in representing complex spatial and spatio-temporal signals.",
        "punchline": "Multi-dimensional Linear Shift-Invariant (LSI) systems model spatial and spatio-temporal signals via multi-dimensional convolution; their BIBO stability requires absolute summability of the impulse response, which is uniquely complex due to the non-factorability of multi-variable polynomials.",
        "mnemonic": "L-C-T-S: LSI linearity, 2D Convolution, Transform domain, Stability constraints.",
        "analogy": "A 1D audio filter is like a pipe that delays and dampens sound as it flows; a 2D optical system model is like a frosted camera lens whose Point Spread Function (2D impulse response) spreads every single point of incoming light into an overlapping blur circle across the entire sensor.",
        "diagram": """+-------------------------------------------------------------------------------+
|               MULTI-DIMENSIONAL LSI SYSTEM MODEL ARCHITECTURE                 |
+-------------------------------------------------------------------------------+

 SPATIAL DOMAIN:
   Input Image x[m, n] ──► [ 2D LSI System h[m, n] ] ──► Output y[m, n] = x ** h
                             (Point Spread Function)
                             y[m, n] = Σ Σ x[k, l] h[m-k, n-l]
                                       k l
 TRANSFORM (FREQUENCY) DOMAIN:
   X(ω₁, ω₂) ───────────► [ Transfer Function H(ω₁, ω₂) ] ──► Y(ω₁, ω₂) = X · H

 BIBO STABILITY CONDITION:
   Σ Σ |h[m, n]| < ∞   (Absolute summability of impulse response)
   m n
   Note: Cannot simply factor poles because 2-variable polynomials lack isolated roots!""",
        "content": """### 1. Multi-Dimensional Linear Shift-Invariant (LSI) Systems
An M-D system transforms an input signal $x[m, n]$ into an output signal $y[m, n] = \\mathcal{T}\\{x[m, n]\\}$. The system is classified as **Linear Shift-Invariant (LSI)** if it satisfies:
1. **Linearity (Superposition):**
   $$\\mathcal{T}\\{a x_1[m, n] + b x_2[m, n]\\} = a \\mathcal{T}\\{x_1[m, n]\\} + b \\mathcal{T}\\{x_2[m, n]\\}$$
2. **Shift Invariance:**
   $$\\mathcal{T}\\{x[m - m_0, n - n_0]\\} = y[m - m_0, n - n_0]$$

---

### 2. Mathematical Formulation: 2D Convolution
Let $\\delta[m, n]$ be the 2D discrete unit impulse. The **unit impulse response (Point Spread Function - PSF)** of the system is $h[m, n] = \\mathcal{T}\\{\\delta[m, n]\\}$.

By representing any arbitrary input $x[m, n]$ as an expansion of shifted impulses:
$$x[m, n] = \\sum_{k=-\\infty}^{\\infty} \\sum_{l=-\\infty}^{\\infty} x[k, l] \\, \\delta[m-k, n-l]$$

The system output is governed by the **2D Discrete Convolution Sum**:
$$y[m, n] = x[m, n] * * h[m, n] = \\sum_{k=-\\infty}^{\\infty} \\sum_{l=-\\infty}^{\\infty} x[k, l] \\, h[m-k, n-l]$$

#### Spatio-Temporal 3D Video Extension
For digital video signals with time index $t$, the 3D convolution model becomes:
$$y[m, n, t] = \\sum_{k} \\sum_{l} \\sum_{\\tau} x[k, l, \\tau] \\, h[m-k, n-l, t-\\tau]$$
where the temporal axis $\\tau$ must be strictly causal ($h[m, n, \\tau] = 0$ for $\\tau < 0$), whereas spatial coordinates $(k, l)$ are non-causal.

---

### 3. Transform Domain Formulation
Applying the 2D Discrete-Time Fourier Transform (2D-DTFT) or 2D Z-transform:
$$Y(\\omega_1, \\omega_2) = X(\\omega_1, \\omega_2) \\cdot H(\\omega_1, \\omega_2)$$
$$Y(z_1, z_2) = X(z_1, z_2) \\cdot H(z_1, z_2)$$
where $H(z_1, z_2) = \\frac{B(z_1, z_2)}{A(z_1, z_2)}$ is the rational 2D system transfer function.

---

### 4. Stability Evaluation of Multi-Dimensional Systems
A fundamental challenge in multi-dimensional systems is evaluating **Bounded-Input Bounded-Output (BIBO) stability**:
- **Spatial Domain Condition:** A 2D LSI system is BIBO stable if and only if its impulse response is absolutely summable:
  $$\\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} |h[m, n]| < \\infty$$
- **The Z-Domain Factorability Dilemma:**
  - In 1D systems, stability is evaluated by factoring the denominator polynomial $A(z)$ into distinct poles and verifying that all poles lie inside the unit circle ($|p_i| < 1$).
  - In 2D systems, by the **Fundamental Theorem of Algebra**, two-variable polynomials $A(z_1, z_2)$ **cannot, in general, be factored into isolated pole roots**. The zeros of $A(z_1, z_2)$ form continuous algebraic manifolds.
  - **Huang's Theorem for 2D Stability:** A causal recursive 2D filter is stable if and only if:
    1. $A(z_1, \\infty) \\ne 0$ for $|z_1| \\ge 1$
    2. $A(z_1, z_2) \\ne 0$ for $|z_1| = 1$ and $|z_2| \\ge 1$

---

### 5. Performance Evaluation in Representing Complex Signals
1. **Optical Lens & Blur Modeling:** Camera defocus, atmospheric turbulence, and camera shake are accurately modeled by convolving true scenes with Gaussian or motion blur PSFs $h[m, n]$.
2. **Medical Tomography (Radon Transform & Inverse LSI):** CT reconstruction models X-ray projections as multi-dimensional line integrals, reconstructed using 2D filtered back-projection.
3. **Motion-Compensated Video Prediction:** Spatio-temporal video models separate static background convolutions from non-linear motion trajectories, reducing predictive coding error."""
    },
    {
        "id": "MID1-Q20",
        "mid": "Mid-I",
        "qno": 20,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Construct a multi-dimensional signal processing framework for image and video systems and assess its role in enhancing signal quality.",
        "punchline": "An end-to-end multi-dimensional processing framework cascades Acquisition, Pre-filtering, 2D/3D Transform, Perceptual Quantization, Entropy Encoding, and Reconstruction to eliminate noise and maximize visual fidelity.",
        "mnemonic": "A-P-T-Q-E-R: Acquisition, Pre-filtering, Transform, Quantization, Encoding, Reconstruction.",
        "analogy": "Like an automated water filtration and bottling plant: raw river water is pumped in (acquisition), passed through sediment filters to remove debris (pre-filtering), distilled into pure vapor components (transform), concentrated into mineral tablets (quantization), packaged tightly in cartons (entropy coding), and rehydrated with clean water at the destination (reconstruction).",
        "diagram": """+-------------------------------------------------------------------------------+
|         END-TO-END MULTI-DIMENSIONAL SIGNAL PROCESSING FRAMEWORK              |
+-------------------------------------------------------------------------------+

 [ Real-World Scene ]
          │
          ▼
 [ 1. Acquisition & Digitization ] ──► CCD/CMOS Sensor: 2D Spatial & Temporal Sampling
          │
          ▼
 [ 2. Pre-Filtering & Denoising ]  ──► Anti-aliasing LPF + Bilateral noise suppression
          │
          ▼
 [ 3. 2D / 3D Transform ]         ──► 2D-DCT / DWT / Temporal Motion Estimation
          │
          ▼
 [ 4. Perceptual Quantization ]    ──► HVS Quantization Matrix (discards invisible HF)
          │
          ▼
 [ 5. Entropy Coding ]             ──► Huffman / CABAC lossless bitstream compression
          │
          ▼
 [ 6. Transmission / Storage ]     ──► Bandwidth-efficient bitstream (MP4, JPEG)
          │
          ▼
 [ 7. Inverse Transform & Synth ]  ──► IDCT / IDWT + Motion Compensation
          │
          ▼
 [ 8. Post-Processing / Enhance ]  ──► Deblocking filter, super-resolution, tone mapping
          │
          ▼
 [ High-Quality Display Output ]""",
        "content": """### 1. Conceptual Framework Architecture
A multi-dimensional signal processing framework is a structured cascade of hardware and software stages designed to capture, clean, compress, transmit, and enhance spatial (image) and spatio-temporal (video) signals.

---

### 2. Systematic Construction of Framework Stages

#### Stage 1: Acquisition and Multi-Dimensional Digitization
- **Physical Transduction:** Optical lenses focus incoming photons onto CMOS/CCD sensor arrays.
- **2D Spatial Sampling:** Continuous 2D scene $f(x, y)$ is sampled on a rectangular pixel grid $(m \\Delta x, n \\Delta y)$.
- **Temporal Sampling (Video):** Video shutter captures frames at continuous time intervals $t = k \\Delta t$ (e.g., 30 or 60 fps).
- **A/D Quantization:** Pixel intensities are quantized into 8-bit, 10-bit, or 12-bit digital levels per color channel.

#### Stage 2: Pre-Filtering and Noise Suppression
- **Anti-Aliasing Optical Filter:** Birefringent optical low-pass filters (OLPF) blur frequencies exceeding the sensor Nyquist rate to prevent moiré fringes.
- **Edge-Preserving Denoising:** 2D spatial bilateral filters or BM3D algorithms suppress sensor thermal noise while strictly preserving sharp object edges.

#### Stage 3: Multi-Dimensional Transform Decomposition
- Decomposes correlated pixel arrays into orthogonal, decorrelated frequency subbands:
  - **2D-DCT (JPEG / H.264):** Concentrates spatial energy into top-left low frequencies.
  - **2D Discrete Wavelet Transform (DWT - JPEG2000):** Multi-resolution octave decomposition into LL, LH, HL, and HH subbands.
  - **Temporal Motion Transform:** Block motion estimation derives displacement motion vectors $(dx, dy)$ between successive video frames.

#### Stage 4: Perceptual Quantization (HVS Optimization)
- Employs Human Visual System (HVS) contrast sensitivity thresholds:
  $$Q[u, v] = \\text{round}\\left( \\frac{F[u, v]}{q[u, v]} \\right)$$
- Coarse quantization step sizes are assigned to high spatial frequencies (where human eyes are insensitive to noise), while fine step sizes preserve low-frequency luminance.

#### Stage 5: Entropy Encoding
- Converts quantized transform coefficients and motion vectors into compact binary representations using lossless coding algorithms:
  - **Huffman Coding / Variable Length Coding (VLC)**
  - **Context-Adaptive Binary Arithmetic Coding (CABAC)**

#### Stage 6: Decoding, Inverse Transformation & Reconstruction
- Reverses encoding at the receiver: Entropy Decoding $\\rightarrow$ Dequantization $\\rightarrow$ 2D-IDCT / IDWT $\\rightarrow$ Motion Compensation synthesis:
  $$\\hat{F}_t(x, y) = \\hat{F}_{t-1}(x - dx, y - dy) + e_t(x, y)$$

#### Stage 7: Post-Processing & Quality Enhancement
- **In-Loop Deblocking Filter:** Smooths artificial grid discontinuities along $8 \\times 8$ or $16 \\times 16$ block boundaries.
- **High Dynamic Range (HDR) Tone Mapping:** Expands luminance contrast for modern OLED/mini-LED displays.

---

### 3. Assessment of Framework's Role in Enhancing Signal Quality
1. **Signal-to-Noise Ratio (SNR) Improvement:** Pre-filtering and subband thresholding eliminate Poisson sensor noise and thermal grain, boosting PSNR by $3\\text{ to }6\\text{ dB}$.
2. **Artifact Suppression:** Adaptive deblocking filters eliminate ringing and blocking artifacts characteristic of aggressive transform compression.
3. **Bandwidth Optimization:** Compresses uncompressed multi-dimensional video by over $95\\%$ (from 1.5 Gbps to 10 Mbps) without noticeable degradation in perceived visual quality.
4. **Resolution Enhancement:** Modern frameworks incorporate deep-learning super-resolution (ESRGAN, CNN post-filters) to hallucinate fine textures from lower-resolution sampled video."""
    },
    {
        "id": "MID2-Q01",
        "mid": "Mid-II",
        "qno": 1,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "Apply multi-dimensional sampling theory to determine minimum sampling rates required to avoid aliasing in spatial and spatio-temporal signals.",
        "punchline": "Multi-dimensional sampling converts continuous signals f(x,y) into discrete grids f(mT₁, nT₂) via 2D Dirac comb multiplication; preventing spatial and temporal aliasing requires sampling rates exceeding twice the highest frequency in every respective axis (fsx ≥ 2fx, fsy ≥ 2fy, fst ≥ 2ft).",
        "mnemonic": "Dirac Comb Picker: fsx ≥ 2fx, fsy ≥ 2fy, fst ≥ 2ft.",
        "analogy": "Like looking through a picket fence at a rotating bicycle wheel: if the vertical slats (spatial sampling) or your blinking rate (temporal sampling) are too slow, the wheel appears to rotate backward or warp into strange zigzag patterns (aliasing and moiré).",
        "diagram": """+-------------------------------------------------------------------------------+
|                    MULTI-DIMENSIONAL SAMPLING & ALIASING                      |
+-------------------------------------------------------------------------------+

 Continuous Image f(x, y)         2D Dirac Comb δ_s(x, y)        Sampled Grid f_s(x, y)
 ┌──────────────────────┐         ┌──────────────────────┐       ┌──────────────────────┐
 │                      │         │ •    •    •    •   T₂│       │ •    •    •    •     │
 │                      │    x    │                      │  ==>  │  (Sampled Pixels)    │
 │   Smooth Landscape   │         │ •    •    •    •     │       │ •    •    •    •     │
 │                      │         │  T₁                  │       │                      │
 └──────────────────────┘         └──────────────────────┘       └──────────────────────┘
                                  δ_s(x, y) = Σ Σ δ(x - mT₁, y - nT₂)

 2D FREQUENCY SPECTRUM (NYQUIST CHECK):
           v ▲                                  v ▲
             │   (No Aliasing: fsx ≥ 2fx)         │   (ALIASING: fsx < 2fx)
    -fsy/2   │    fsy/2                  -fsy/2   │    fsy/2
    ───┬─────┼─────┬───                   ───┬───┼───┬───
       │  /---\\  │                          │/---\\-+---/---\\│  <-- Spectra Overlap
  ─────┼─(  •  )─┼─────► u            ───────┼(  • X •  )┼──────► u (Moiré distortion)
       │  \\---/  │                          │\\---/-+---\\---/│
    ───┴─────┼─────┴───                   ───┴───┼───┴───
             │                                    │""",
        "content": """### 1. Concept of Multi-Dimensional Sampling Theory (Unit 3 Notes)
Multi-dimensional sampling theory extends 1D temporal sampling to signals defined across two or more dimensions (such as 2D still images, 3D video, and 3D volumetric medical scans). It establishes the mathematical conditions required to convert continuous multi-dimensional signals into discrete digital representations and reconstruct them perfectly without loss of information.

---

### 2. The 2D Sampling Process & Dirac Comb
In continuous 2D space, a continuous image $f(x, y)$ is sampled by multiplying it with a 2D sampling function $\\delta_s(x, y)$, known as a **2D Dirac comb (impulse train)**:
$$\\delta_s(x, y) = \\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} \\delta(x - m T_1, y - n T_2)$$
where:
- $m, n$ are integers $(\\dots, -2, -1, 0, 1, 2, \\dots)$
- $T_1$ is the sampling interval along the horizontal $x$-axis
- $T_2$ is the sampling interval along the vertical $y$-axis
- $\\delta(x, y)$ is the 2D Dirac delta function, which is zero everywhere except at the origin $(0, 0)$

The resulting sampled signal is:
$$f_s(x, y) = f(x, y) \\cdot \\delta_s(x, y) = \\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} f(m T_1, n T_2) \\, \\delta(x - m T_1, y - n T_2)$$
The continuous signal is converted into a discrete lattice of sample points, where each point represents a **pixel value** at coordinates $(m T_1, n T_2)$.

---

### 3. Multi-Dimensional Nyquist Sampling Criterion
In the frequency domain, sampling causes the continuous spectrum $F(u, v)$ to replicate periodically across an infinite 2D grid with periods $f_{sx} = \\frac{1}{T_1}$ and $f_{sy} = \\frac{1}{T_2}$:
$$F_s(u, v) = \\frac{1}{T_1 T_2} \\sum_{k=-\\infty}^{\\infty} \\sum_{l=-\\infty}^{\\infty} F(u - k f_{sx}, v - l f_{sy})$$

To prevent adjacent spectral replicas from overlapping (**aliasing**):
1. **For 2D Spatial Signals (Still Images):**
   If $f_x$ and $f_y$ represent the maximum spatial cut-off frequencies along the $x$ and $y$ axes:
   $$f_{sx} \\ge 2 f_x \\implies T_1 \\le \\frac{1}{2 f_x}$$
   $$f_{sy} \\ge 2 f_y \\implies T_2 \\le \\frac{1}{2 f_y}$$
2. **For 3D Spatio-Temporal Signals (Digital Video):**
   Video introduces a temporal axis $t$ with maximum motion temporal frequency $f_t$:
   $$f_{sx} \\ge 2 f_x, \\quad f_{sy} \\ge 2 f_y, \\quad f_{st} \\ge 2 f_t$$
   *(e.g., minimum frame rate $f_{st}$ must exceed twice the fastest motion bandwidth to avoid temporal aliasing/stroboscopic effects).*

---

### 4. Sampling Lattices (Grid Structures)
Multi-dimensional sampling can be arranged in different geometric grids:
1. **Rectangular Lattice:** Standard grid used in digital camera sensors, displays, and image matrices ($f[m, n]$). Simple to address and process with separable 1D algorithms.
2. **Hexagonal Lattice:** Samples points in a honeycomb structure. Provides **isotropic circular symmetry** and is **$13.4\\%$ more efficient** than rectangular grids, requiring fewer samples to represent circular bandlimited signals without aliasing.

---

### 5. Aliasing Distortion & Anti-Aliasing Filtering
If sampling rates fall below Nyquist limits ($f_{sx} < 2f_x$ or $f_{sy} < 2f_y$):
- High-frequency spatial details fold back into the low-frequency baseband.
- Generates severe visual distortions known as **Moiré patterns** (artificial wavy stripes on striped shirts or brick walls) and jagged staircasing along diagonal edges.
- **Remedy:** Optical anti-aliasing low-pass filters (OLPF) are placed directly before the image sensor to truncate spatial frequencies above $f_{sx}/2$ and $f_{sy}/2$ prior to sampling."""
    },
    {
        "id": "MID2-Q02",
        "mid": "Mid-II",
        "qno": 2,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Illustrate the transformation process in multi-dimensional systems through a block diagram and explain the functional significance of each stage.",
        "punchline": "The transformation pipeline converts real-world continuous signals into the digital transform domain (DFT/DCT) to simplify convolution into multiplication, compact energy, and isolate noise, before reconstructing the continuous output.",
        "mnemonic": "C-S-Q-T-P-I-D-C: CT Input -> Sampling -> Quantization -> Transform -> Processing -> Inverse Transform -> DAC/LPF -> CT Output.",
        "analogy": "Like packing luggage for international travel: continuous items are measured (sampling), boxed into standard sizes (quantization), vacuum-compressed into small bags (transform), inspected for excess weight (processing), unzipped at the hotel (inverse transform), and ironed smooth for wear (reconstruction filter).",
        "diagram": """+-------------------------------------------------------------------------------+
|           TRANSFORMATION PROCESS IN MULTI-DIMENSIONAL SYSTEMS                 |
+-------------------------------------------------------------------------------+

 [ CT Input Signal ] ──► Real-world continuous-time/spatial analog signal f(x, y, t)
         │
         ▼
 [ 1. Sampling ]    ──► Converts CT signal into discrete-time lattice (fs ≥ 2f_max)
         │
         ▼
 [ 2. Quantization] ──► Converts continuous amplitudes into finite binary bits (levels)
         │
         ▼
 [ 3. Transform ]   ──► Core stage: 2D-DFT / DCT / DWT converts space into frequency
         │
         ▼
 [ 4. Processing ]  ──► Efficient filtering, energy compaction, noise suppression, coding
         │
         ▼
 [ 5. Inverse Trans]──► IDFT / IDCT reconstructs discrete spatial/temporal domain signal
         │
         ▼
 [ 6. Reconstruction]─► DAC + Analog Low-Pass Filter eliminates high-frequency imaging
         │
         ▼
 [ CT Output Signal]──► Final continuous reconstructed output f_out(x, y, t)""",
        "content": """### 1. Overview of the Transformation Process (Unit 3 Notes)
The transformation process converts a signal from its original physical domain (spatial coordinates $(x, y)$ or time $t$) into a mathematical transform domain (frequency, subband, or cepstral domain). This transformation simplifies complex mathematical operations, isolates noise, compacts energy, and enables efficient signal compression and transmission.

---

### 2. Functional Significance of Each Stage (Unit 3 Notes)

#### Stage 1: Continuous-Time / Spatial Input (CT Input)
- **Signal Nature:** A continuous real-world physical signal such as a speech acoustic wave, optical image irradiance $f(x, y)$, or video sequence $f(x, y, t)$.
- **Significance:** Represents the analog truth before electronic measurement.

#### Stage 2: Sampling
- **Operation:** Evaluates the continuous signal at discrete intervals $T_1, T_2, T_t$, converting continuous coordinates into discrete indices $(m T_1, n T_2)$.
- **Significance:** Must strictly satisfy the **Nyquist criterion** ($f_s \\ge 2 f_{\\max}$) along all dimensions to prevent spectral aliasing.

#### Stage 3: Quantization
- **Operation:** Maps continuous sample amplitudes into a finite set of discrete digital levels (e.g., 8-bit integers $0\\dots255$).
- **Significance:** Enables storage and arithmetic processing in binary digital computers. Introduces controlled quantization noise.

#### Stage 4: Transformation Block (Core Stage)
- **Operation:** Applies mathematical linear transforms such as the **2D-DFT, 2D-DCT, or Wavelet Transform (DWT)**.
- **Significance:** 
  1. **Simplifies Analysis:** Complex spatial structures decompose into linear sums of sinusoidal or localized wave components.
  2. **Energy Compaction:** Concentrates signal power into a small subset of dominant transform coefficients.

#### Stage 5: Processing in Transform Domain
- **Operation:** Performs targeted operations such as frequency-domain filtering, spectral thresholding, feature extraction, or perceptual quantization.
- **Significance:** 
  - Converts computationally expensive 2D spatial convolution into point-by-point algebraic multiplication:
    $$Y[u, v] = X[u, v] \\cdot H[u, v]$$
  - Isolates high-frequency noise spikes from low-frequency structural formants.

#### Stage 6: Inverse Transformation
- **Operation:** Applies the Inverse Transform (e.g., 2D-IDFT, 2D-IDCT, IDWT) to map the processed coefficients back to the discrete spatial domain.
- **Significance:** Restores the recognizable 2D spatial pixel grid or audio frame.

#### Stage 7: Dequantization & Reconstruction Filter (DAC Stage)
- **Operation:** Digital-to-Analog Converter (DAC) followed by an analog reconstruction Low-Pass Filter (anti-imaging filter).
- **Significance:** Removes high-frequency mirror replicas generated by sampling, producing a smooth, continuous analog output $f_{\\text{out}}(x, y)$.

---

### 3. Summary of Justification for Transformation
| Justification Factor | Benefit in Multi-Dimensional Processing |
| :--- | :--- |
| **Computational Efficiency** | Multi-dimensional convolution ($O(N^4)$) becomes point-wise multiplication ($O(N^2)$). |
| **Energy Compaction** | Transforms like DCT pack $>90\\%$ energy into $<10\\%$ coefficients (basis of JPEG/MPEG). |
| **Perceptual Compression** | Allows selective discarding of visually imperceptible high frequencies. |
| **Noise Filtering** | Wideband noise is separated from dominant narrowband signal energy peaks. |"""
    },
    {
        "id": "MID2-Q03",
        "mid": "Mid-II",
        "qno": 3,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Evaluate the performance of image and video representations based on human visual system (HVS) characteristics and justify the selection of perceptual models.",
        "punchline": "Human visual perception is fundamentally non-uniform: the eye is far more sensitive to luminance than chrominance, and sensitive to mid-band spatial contrast over high-frequency fine noise; modern codecs exploit this via YCbCr color separation, chroma subsampling (4:2:0), and perceptual DCT quantization matrices.",
        "mnemonic": "L-C-C-P: Luminance sensitivity, Contrast sensitivity, Color perception, Perceptual quantization.",
        "analogy": "Designing an image compression codec without HVS models is like printing a paperback book with microscope-level microscopic ink: humans cannot see the tiny details anyway, so expending millions of bits to encode invisible high-frequency noise is pure waste.",
        "diagram": """+-------------------------------------------------------------------------------+
|               HUMAN VISUAL SYSTEM (HVS) PROPERTIES & IMPACT                   |
+-------------------------------------------------------------------------------+

 1. LUMINANCE VS CHROMINANCE SENSITIVITY:
    Human Retina: ~120 Million Rods (Luminance Y) vs ~6-7 Million Cones (Color Cb, Cr)
    RGB Image (100% data) ──► YCbCr Conversion ──► Chroma Subsampling 4:2:0 (50% savings!)
    [ Y: Full Res 1920x1080 ] + [ Cb: Half Res 960x540 ] + [ Cr: Half Res 960x540 ]

 2. CONTRAST SENSITIVITY FUNCTION (CSF):
    Contrast ▲                 Peak Sensitivity at 3-5 cycles/degree
    Sensitivity                /---\\
            │               /       \\
            │              /         \\    Eye is blind to high-frequency fine noise!
            │             /           \\   ==> HEAVILY QUANTIZE HIGH FREQUENCIES
            └────────────┴─────────────┴──────────► Spatial Frequency (cycles/degree)
                         Low          High

 3. PERCEPTUAL QUANTIZATION (JPEG Q-MATRIX):
    Low Freq (Fine Step Size, High Precision) ──► High Freq (Coarse Step, Rounded to 0)""",
        "content": """### 1. Conceptual Foundation of HVS in Video Processing (Unit 3 Notes)
Human visual system (HVS) characteristics strongly dictate how digital images and video sequences must be sampled, represented, and compressed. Because human sensory perception is non-linear and bandlimited, lossless mathematical preservation is unnecessary; the engineering goal is **perceptual transparency** (removing data that the human eye cannot perceive).

---

### 2. Influence of Core HVS Characteristics

#### 1. Luminance Sensitivity vs Chrominance Sensitivity
- **Biological Basis:** 
  The human retina contains approximately **120 million rod cells** (responsible for scotopic vision and brightness perception) but only **6 to 7 million cone cells** (responsible for photopic color vision, concentrated primarily in the fovea centralis). Consequently, human visual acuity for brightness variations is vastly superior to that for color nuances.
- **Impact on Image/Video Representation:**
  - Raw color images are converted from RGB into decoupled **luminance-chrominance spaces (YCbCr)**:
    $$Y = 0.299 R + 0.587 G + 0.114 B$$
    $$Cb = -0.1687 R - 0.3313 G + 0.5 B + 128$$
    $$Cr = 0.5 R - 0.4187 G - 0.0813 B + 128$$
  - Luminance $Y$ preserves fine structural details and contours with maximum spatial resolution.
- **Impact on Compression:**
  - **Chroma Subsampling (4:2:2 and 4:2:0):** 
    In 4:2:0 subsampling, chrominance channels ($Cb, Cr$) are downsampled by a factor of 2 horizontally and vertically. For every $4 \\times 2$ block of pixels, 8 luminance samples are retained but only 2 $Cb$ and 2 $Cr$ samples are stored.
  - **Data Reduction:** Instantly cuts raw uncompressed bitrate by **$50\\%$** with zero perceptible loss in visual quality.

#### 2. Contrast Perception & Contrast Sensitivity Function (CSF)
- **Biological Basis:**
  The HVS does not perceive absolute luminance; it perceives **relative contrast** ($C = \\frac{\\Delta L}{L}$). The eye's sensitivity to spatial contrast follows a bandpass characteristic known as the **Contrast Sensitivity Function (CSF)**:
  - Peak sensitivity occurs at intermediate spatial frequencies (**3 to 5 cycles per degree** of visual angle).
  - Sensitivity rolls off rapidly at high spatial frequencies (fine details and pixel noise are imperceptible at normal viewing distances).
  - Sensitivity also drops at very low frequencies (gradual background luminance shifts are ignored due to retinal adaptation).
- **Impact on Representation & Compression:**
  - Transforms like the 2D-DCT decompose spatial blocks into frequency coefficients.
  - High-frequency DCT coefficients are divided by large quantization step sizes in the **JPEG Quantization Matrix ($Q_{uv}$)**, forcing subtle high-frequency details to zero during run-length encoding.

#### 3. Color Interpretation & Spatial Masking
- **Biological Basis:**
  The human eye exhibits **spatial masking**: high-contrast visual textures (such as tree foliage or rushing water) mask human sensitivity to quantization distortion and noise in those regions.
- **Impact on Compression:**
  - Codecs allocate fewer bits to highly textured or fast-moving macroblocks, diverting bit-budget to smooth areas (like skies or faces) where human eyes are hyper-sensitive to banding artifacts.

---

### 3. Justification of Selected Perceptual Models
| Perceptual Model | Engineering Implementation | Justification & Performance Benefit |
| :--- | :--- | :--- |
| **YCbCr Color Model** | Decouples $Y$ from $Cb, Cr$ channels | Eliminates inter-color cross-correlation; enables independent color subsampling. |
| **Chroma Subsampling (4:2:0)**| Decimates $Cb, Cr$ resolution by $4\\times$ | Reduces transmission bandwidth by $50\\%$ without humanly visible blur. |
| **CSF-Weighted Quantization** | Custom $8 \\times 8$ JPEG/MPEG $Q$-matrices | Discards unnoticeable high frequencies; achieves $10:1$ to $20:1$ compression ratios. |
| **Temporal Motion Masking** | Just Noticeable Distortion (JND) models | Permits higher compression noise in rapid scene transitions and fast motion blocks. |

---

### 4. Conclusion
Integrating HVS characteristics transforms video processing from inefficient mathematical exactness to **perceptually optimal transmission**. Standards such as JPEG, MPEG-2, H.264/AVC, and H.265/HEVC owe their massive compression gains (up to $95\\%$) directly to HVS-guided perceptual models."""
    },
    {
        "id": "MID2-Q04",
        "mid": "Mid-II",
        "qno": 4,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Design and justify a digital video representation system, incorporating sampling theory, frame structure, and temporal redundancy reduction techniques.",
        "punchline": "A digital video representation system models video as a 3D signal f(x,y,t); it incorporates 2D spatial Nyquist sampling, temporal frame rate capture, an I/P/B GOP frame hierarchy, and block-matching motion-compensated temporal prediction to eliminate up to 90% of redundant data.",
        "mnemonic": "S-F-T-S: 3D Sampling, Frame structure (I/P/B), Temporal redundancy reduction, Standards (H.264/HEVC).",
        "analogy": "Transmitting video without temporal redundancy reduction is like re-mailing an entire 500-page book every day even if only a single sentence was revised on page 20; motion-compensated video coding simply texts the recipient: 'On page 20, replace line 4 with this new sentence' (motion vector + prediction error).",
        "diagram": """+-------------------------------------------------------------------------------+
|             DIGITAL VIDEO REPRESENTATION SYSTEM & GOP ARCHITECTURE            |
+-------------------------------------------------------------------------------+

 1. 3D SIGNAL SAMPLING:
    f(x, y, t) ──► Spatial: 1920x1080 pixels (fsx ≥ 2fx, fsy ≥ 2fy)
               ──► Temporal: 30 / 60 frames per second (fst ≥ 2ft)
               ──► Color: YCbCr 4:2:0 Chroma Subsampling

 2. HIERARCHICAL GROUP OF PICTURES (GOP) STRUCTURE:
           ┌────────────────────── Forward Prediction ──────────────────────┐
           │                                                                │
           ▼                                                                ▼
      ┌─────────┐         ┌─────────┐         ┌─────────┐              ┌─────────┐
      │ I-Frame │◄───┬───►│ B-Frame │◄───┬───►│ P-Frame │◄────────────►│ I-Frame │
      │ (Intra) │    │    │ (Bi-dir)│    │    │(Predict)│              │ (Intra) │
      └─────────┘    │    └─────────┘    │    └─────────┘              └─────────┘
          ▲          │                   │
          └──────────┴─── Bi-directional ┴─────────┘

 3. TEMPORAL REDUNDANCY REDUCTION PIPELINE:
    Current Frame F_t ──► [ Block Motion Estimation ] ◄── Reference Frame F_{t-1}
                                 │
                         Motion Vectors (dx, dy)
                                 │
                                 ▼
                         [ Motion Compensation ] ──► Predicted Frame F̂_t
                                 │
                                 ▼
                         Residual Error E_t = F_t - F̂_t (Transmitted via 2D-DCT)""",
        "content": """### 1. Architectural Design of a Digital Video Representation System (Unit 3 Notes)
A digital video system converts real-world continuous visual motion into a compact, bandwidth-efficient, and reconstructable digital bitstream. The end-to-end design encompasses three core pillars:
1. **Multi-Dimensional Sampling Theory (3D Signal Representation)**
2. **Hierarchical Frame Structure (Group of Pictures - GOP)**
3. **Temporal Redundancy Reduction Techniques (Motion Compensation)**

---

### 2. Component 1: Multi-Dimensional Sampling Theory in Video
Digital video is treated as a 3D spatio-temporal continuous signal $f(x, y, t)$, where $(x, y)$ represent 2D continuous spatial coordinates on the camera sensor and $t$ represents continuous time.

#### a) Spatial Sampling (Pixel Grid)
- Discretizes continuous spatial optical projections into an array of $M \\times N$ pixels at intervals $(T_x, T_y)$.
- Must satisfy the 2D Nyquist criterion:
  $$f_{sx} \\ge 2 f_{x,\\max} \\quad \\text{and} \\quad f_{sy} \\ge 2 f_{y,\\max}$$
- Common industry standards: Full HD ($1920 \\times 1080$), 4K UHD ($3840 \\times 2160$). Prevents spatial blur and moiré distortion.

#### b) Temporal Sampling (Frame Rate)
- Samples the continuous motion scene into discrete still image frames at rate $f_{st} = \\frac{1}{T_t}$ frames per second (fps).
- **Rate Selection:**
  - 24 fps: Cinematic standard.
  - 30 fps: Standard television broadcast.
  - 60 fps / 120 fps: High-speed sports and interactive gaming.
- Prevents temporal aliasing (stroboscopic effects, like wheels appearing to turn backwards).

#### c) Color Representation & Chroma Subsampling
- RGB signals are mapped into **YCbCr** color space.
- Applying **4:2:0 chroma subsampling** allocates full resolution to luminance $Y$ and quarter spatial resolution to $Cb$ and $Cr$, reducing raw data by $50\\%$ before compression.

---

### 3. Component 2: Frame Structure & Group of Pictures (GOP)
Video frames are organized into structured sequences called a **Group of Pictures (GOP)**, balancing compression efficiency with random access and error resilience:

1. **I-Frames (Intra-Coded Frames):**
   - Encoded completely independently of all other frames (similar to a standalone JPEG image).
   - Exploits only spatial redundancy; acts as an anchor for random seeking and channel switching.
   - Lowest compression ratio, largest file size.
2. **P-Frames (Predictive-Coded Frames):**
   - Encoded using motion-compensated forward prediction from the preceding I-frame or P-frame.
   - Stores only motion displacement vectors and residual prediction differences.
   - Achieves moderate-to-high compression.
3. **B-Frames (Bi-directionally Predictive Frames):**
   - Interpolated using motion vectors from both **past and future** reference frames.
   - Highest compression efficiency; cannot serve as reference frames for other frames.
4. **Standard GOP Pattern:**
   $$I \\; B \\; B \\; P \\; B \\; B \\; P \\; B \\; B \\; I$$
   *(GOP length typically 12 to 15 frames, providing random access points every 0.5 seconds at 30 fps).*

---

### 4. Component 3: Temporal Redundancy Reduction Techniques
Because successive frames in a video sequence are separated by only 33 ms (at 30 fps), background scenery and large object structures remain virtually unchanged (**temporal redundancy**).

#### a) Frame Differencing (Basic Baseline)
- Subtracts previous frame directly:
  $$D_t(x, y) = F_t(x, y) - F_{t-1}(x, y)$$
- Effective only for completely stationary static scenes; fails when camera or objects move.

#### b) Block-Based Motion Estimation (BMA)
- Divides current frame $F_t$ into non-overlapping macroblocks (e.g., $16 \\times 16$ pixels).
- Searches within a spatial window in reference frame $F_{t-1}$ to locate the best-matching block that minimizes the **Sum of Absolute Differences (SAD)**:
  $$\\text{SAD}(dx, dy) = \\sum_{m=0}^{15} \\sum_{n=0}^{15} |F_t(x+m, y+n) - F_{t-1}(x+m+dx, y+n+dy)|$$
- Output: A compact **Motion Vector** $\\mathbf{MV} = (dx, dy)$ for every block.

#### c) Motion Compensation & Residual Coding
- Forms predicted frame: $\\hat{F}_t(x, y) = F_{t-1}(x - dx, y - dy)$.
- Computes residual error: $E_t(x, y) = F_t(x, y) - \\hat{F}_t(x, y)$.
- Because motion compensation accounts for object shifts, the residual energy $E_t$ is near zero, allowing 2D-DCT and entropy coding to achieve over **$90\\%$ bitrate reduction**.

---

### 5. Justification of System Design Choices (Unit 3 Notes)
- **Sampling Theory:** Guarantees artifact-free capture and mathematically faithful reconstruction of continuous 3D scenes.
- **GOP Hierarchy:** Provides random access seeking (via I-frames) while maximizing compression throughput (via B/P-frames).
- **Motion Compensation:** Exploits the physical persistence of objects in real-world motion, compressing 1.5 Gbps uncompressed video down to 5–10 Mbps in modern H.264/AVC and H.265/HEVC streaming systems."""
    }
]
