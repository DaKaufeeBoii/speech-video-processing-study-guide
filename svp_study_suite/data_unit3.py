# -*- coding: utf-8 -*-
"""
Unit 3: Multi-Dimensional Signals, Transforms, Sampling & Digital Video Representation
Questions: Mid-I Q17 to Q20 AND Mid-II Q1 to Q4
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408 | Dr. Sandeep Kumar M
Written in student-friendly, zero-jargon peer-tutor style with complete mathematical rigor.
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
        "punchline": "1D is audio (amplitude vs time); 2D is a photograph f(x,y); 3D is a video f(x,y,t) or medical CT scan f(x,y,z); M-D signals have non-causal spatial axes, intense pixel correlation, and require massive bandwidth.",
        "mnemonic": "S-T-V-M: Spatial 2D, Temporal 3D, Volumetric CT/MRI, Massive Bandwidth.",
        "analogy": "A single note played on a violin is 1D (sound wave over time); a painting on a wall is 2D (colors spread across width and height); a live theater performance is 3D (2D stage visual moving through time t).",
        "diagram": """DIMENSIONALITY TAXONOMY:
  1D Audio / Speech       : s(t)          ──► Amplitude vs 1D Time
  2D Still Image          : f(x, y)       ──► Brightness vs (X, Y) Coordinates
  3D Digital Video        : f(x, y, t)    ──► 2D Spatial Frames moving along Time t
  3D Medical CT / MRI     : f(x, y, z)    ──► 3D Voxel tissue density in space
  4D Dynamic Cardiac MRI  : f(x, y, z, t) ──► 3D Heart Volume beating over Time

KEY CHARACTERISTICS:
  1. Multi-axis dependency: f(x₁, x₂, ..., xₘ)
  2. Spatial Correlation  : Neighboring pixels are 90%+ identical (Redundancy!)
  3. Non-Causality        : Pixels in a photo exist everywhere simultaneously
  4. Massive Data Volume  : Raw 1080p video needs ~1.5 Gbps bandwidth without compression!""",
        "content": """### 1. The Big Picture (What is a Multi-Dimensional Signal?)
In basic DSP, signals only depend on 1 variable: time $t$ (like microphone voltage $s(t)$). 
A **Multi-Dimensional (M-D) signal** depends on two or more independent physical variables:
* **2D Signals (Still Images):** $f(x, y)$, where $x$ (horizontal) and $y$ (vertical) are spatial coordinates, and $f(x, y)$ represents optical brightness (luminance) or color $[R, G, B]^T$.
* **3D Signals (Digital Video):** $f(x, y, t)$, where 2D spatial frames move along continuous time $t$.
* **3D Volumetric Signals (Medical CT / MRI):** $f(x, y, z)$, representing physical tissue density at 3D spatial voxel coordinates $(x, y, z)$.
* **4D Signals (Dynamic Spatio-Temporal Volumes):** $f(x, y, z, t)$, such as a 3D ultrasound video capturing a beating baby heart over time.

---

### 2. The 4 Unique Characteristics of M-D Signals

#### 1. Spatial & Temporal Correlation (Massive Redundancy)
In a selfie, a blue sky has thousands of adjacent pixels with nearly identical blue values (**spatial redundancy**). In a video, 30 frames per second means $95\\%$ of the background stays completely unchanged between frames (**temporal redundancy**). Compression algorithms exploit this to shrink file sizes by $90\\%$.

#### 2. Non-Causality in Space (Looking in All Directions)
In 1D audio, time only flows forward — you cannot use a future sound to filter a past sound (strict causality). But in an image, **pixels exist simultaneously in all directions**! A pixel at $(x, y)$ can be filtered using neighbors to its left, right, top, bottom, and diagonals.

#### 3. Separability (The Computational Magic Trick)
An M-D signal or filter is **separable** if it can be factored into a multiplication of simple 1D functions:
$$f(x, y) = f_1(x) \\cdot f_2(y)$$
Separability lets us run fast 1D operations row-by-row, then column-by-column, slashing computation from $O(N^2)$ to $O(2N)$!

#### 4. Astronomical Data Bandwidth
Uncompressed 1080p video ($1920 \\times 1080$ pixels, 24-bit color, 30 frames/second) generates:
$$1920 \\times 1080 \\times 3\\text{ bytes} \\times 30\\text{ fps} \\approx 186.6\\text{ MB/second} = \\mathbf{1.49\\text{ Gbps}}$$
Without multi-dimensional compression, YouTube and Netflix would crash the global internet in 5 minutes!

---

### 3. Real-World Applications (Exam Marks)
- **Computer Vision & Self-Driving Cars:** Analyzing $f(x, y, t)$ to track pedestrians and detect lane markers.
- **Medical Imaging:** 3D CT/MRI scans allow surgeons to rotate and view internal organs before surgery.
- **Satellite Remote Sensing:** Multi-spectral satellite cameras ($f(x, y, \\lambda)$) monitor crop drought and forest fires from orbit.
- **Video Streaming:** H.264/HEVC codecs compress video from 1.5 Gbps down to 5 Mbps for seamless mobile playback."""
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
        "punchline": "The 2D-DFT turns a spatial image into a 2D frequency grid; its row-column separability lets you compute it using fast 1D-FFTs in O(N² log N) time, packing 90% of image energy into the central DC peak.",
        "mnemonic": "S-S-C-E: Separable (Row-Col), Symmetric (Hermitian), Shift = Phase, Energy compaction.",
        "analogy": "Like shining white sunlight through a prism: the prism separates the white beam into individual rainbow wavelengths; the 2D-DFT separates a flat photo into slow, smooth background waves (low frequencies) and sharp, crisp edge ripples (high frequencies).",
        "diagram": """SPATIAL DOMAIN IMAGE f[m, n] (N x N)          FREQUENCY SPECTRUM |F[u, v]|
┌───────────────────────────────┐              ┌───────────────────────────────┐
│                               │              │ \\       High Frequencies    / │
│      Smooth Backgrounds       │   2D-DFT     │  \\   (Edges, fine texture) /  │
│     (Slow spatial changes)    │ ──────────►  │   \\      • (u, v)         /   │
│                               │              │    • Central DC Peak (0,0)    │
│      Sharp Object Borders     │              │   /  (90%+ total energy!) \\   │
│     (Fast spatial changes)    │              │  /                         \\  │
│                               │              │ /                           \\ │
└───────────────────────────────┘              └───────────────────────────────┘
  Row-by-Row 1D-FFT  ──►  Column-by-Column 1D-FFT  ==> Blazingly Fast O(N² log₂ N)!""",
        "content": """### 1. Mathematical Formulation of the 2D-DFT
The **2D Discrete Fourier Transform (2D-DFT)** converts a 2D digital image $f[m, n]$ of size $M \\times N$ into a 2D frequency spectrum $F[u, v]$:
$$F[u, v] = \\sum_{m=0}^{M-1} \\sum_{n=0}^{N-1} f[m, n] \\, e^{-j 2\\pi \\left( \\frac{um}{M} + \\frac{vn}{N} \\right)}$$
where $u$ is the horizontal spatial frequency and $v$ is the vertical spatial frequency.

The **2D Inverse DFT (2D-IDFT)** perfectly puts the image back together:
$$f[m, n] = \\frac{1}{M N} \\sum_{u=0}^{M-1} \\sum_{v=0}^{N-1} F[u, v] \\, e^{j 2\\pi \\left( \\frac{um}{M} + \\frac{vn}{N} \\right)}$$

---

### 2. The 4 Big Properties to Write in Exam

#### 1. Row-Column Separability (The Speedup Trick):
The 2D exponential kernel factors into two independent 1D kernels:
$$e^{-j 2\\pi \\left( \\frac{um}{M} + \\frac{vn}{N} \\right)} = e^{-j 2\\pi \\frac{um}{M}} \\cdot e^{-j 2\\pi \\frac{vn}{N}}$$
*How to compute:* 
- Step 1: Run a 1D-FFT on every horizontal row ($M$ rows).
- Step 2: Run a 1D-FFT on every vertical column of the result ($N$ columns).
*Result:* Slashes computation from brute-force $O(M^2 N^2)$ down to **$O(M N \\log_2(M N))$**!

#### 2. Energy Compaction (The DC Component):
In natural photos, pixels change slowly. Therefore, **over $90\\%$ of the total image energy is packed into the DC component $F[0, 0]$** (which represents the average image brightness) and the low frequencies immediately around it. High frequencies (fine noise) have tiny amplitudes.

#### 3. Conjugate Symmetry (Hermitian Property):
For real-valued image pixels:
$$F[-u, -v] = F^*[u, v] \\implies |F[-u, -v]| = |F[u, v]|$$
The frequency spectrum is completely symmetric around the center.

#### 4. Spatial Shift $\\leftrightarrow$ Phase Modulation:
Moving an object across the camera view shifts its spatial coordinates $(m - m_0, n - n_0)$, but its frequency magnitude $|F[u, v]|$ remains **completely unchanged**! Only the phase angles rotate.

---

### 3. Practical Applications in Image Processing
- **Low-Pass Filtering (Image Smoothing / Denoising):** Multiply $F[u, v]$ by a mask that keeps only central low frequencies and sets outer high frequencies to zero. The reconstructed image is smooth and noise-free.
- **High-Pass Filtering (Edge Detection):** Zero out the central DC component and pass only outer high frequencies. The reconstructed image shows only sharp object outlines and borders!"""
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
        "punchline": "2D Linear Shift-Invariant (LSI) systems filter images via 2D convolution; BIBO stability requires absolute summability of the impulse response, but 2D stability is uniquely tricky because 2-variable polynomials cannot be factored into simple isolated poles.",
        "mnemonic": "L-S-C-S: Linearity, Shift-Invariance, 2D Convolution, Stability non-factorability.",
        "analogy": "Like looking through a frosted bathroom window or a camera lens: every single sharp pinpoint of light in the real world is smeared out by the glass into a small circular blur spot called the Point Spread Function (2D impulse response h[m,n]). The final blurry view is the 2D convolution of the scene with the blur spot.",
        "diagram": """SPATIAL DOMAIN:
Input Image x[m, n] ──► [ 2D LSI System: h[m, n] ] ──► Output Image y[m, n] = x ** h
                          (Point Spread Function)
                          y[m, n] = Σ Σ x[k, l] · h[m-k, n-l]

FREQUENCY DOMAIN EQUIVALENT:
X(ω₁, ω₂) ────────────► [ Transfer Function H(ω₁, ω₂) ] ──► Y(ω₁, ω₂) = X · H

THE 2D STABILITY DILEMMA (Huang's Theorem):
1D System: H(z) = 1 / (z - p₁) (Easy! Factor denominator into isolated poles; check |p| < 1)
2D System: H(z₁, z₂) = 1 / A(z₁, z₂) (Cannot factor! Roots form continuous algebraic curves;
                                      must test the entire unit bidisc {|z₁|≤1, |z₂|≤1})""",
        "content": """### 1. The Big Picture (What is a 2D LSI System?)
In image processing, an optical lens, camera motion blur, or digital sharpening filter is modeled as a **2D Linear Shift-Invariant (LSI) System**.
If you shift the input image by $(m_0, n_0)$, the output image simply shifts by the exact same amount without changing shape:
$$\\mathcal{T}\\{x[m - m_0, n - n_0]\\} = y[m - m_0, n - n_0]$$

---

### 2. Mathematical Formulation: 2D Convolution
Let $\\delta[m, n]$ be a 2D unit impulse (a single bright white pixel at the origin). The system's response to this impulse is called the **Point Spread Function (PSF)** $h[m, n]$.
Any input image $x[m, n]$ can be represented as an array of shifted impulses. Therefore, the system output is governed by the **2D Discrete Convolution Sum**:
$$y[m, n] = x[m, n] * * h[m, n] = \\sum_{k=-\\infty}^{\\infty} \\sum_{l=-\\infty}^{\\infty} x[k, l] \\, h[m - k, n - l]$$

#### Spatio-Temporal 3D Video Extension:
For video, we add a temporal axis $t$:
$$y[m, n, t] = \\sum_k \\sum_l \\sum_\\tau x[k, l, \\tau] \\, h[m - k, n - l, t - \\tau]$$
*Notice:* Spatial axes $(k, l)$ are non-causal (can look left, right, up, down), but the temporal axis $\\tau$ must be **strictly causal** ($h[m, n, \\tau] = 0$ for $\\tau < 0$, because future frames cannot affect past frames!).

---

### 3. Evaluating Multi-Dimensional Stability (The 2D Pole Dilemma)
In 1D systems, checking BIBO stability is trivial: factor the denominator polynomial into poles, and check if all poles lie inside the unit circle ($|p_i| < 1$).
**Why 2D Stability is Much Harder (Exam Trap!):**
* By the **Fundamental Theorem of Algebra**, a polynomial in two variables $A(z_1, z_2)$ **CANNOT in general be factored into simple roots**!
* Zeros of $A(z_1, z_2)$ form continuous algebraic manifolds and surfaces in 4D complex space, not isolated dots.
* **Huang's Theorem for 2D Stability:** A causal 2D recursive filter is BIBO stable if and only if the denominator has no zeros inside or on the boundary of the **unit bidisc**:
  1. $A(z_1, \\infty) \\ne 0$ for $|z_1| \\ge 1$
  2. $A(z_1, z_2) \\ne 0$ for $|z_1| = 1$ and $|z_2| \\ge 1$
* In spatial domain, this simplifies to **absolute summability**:
  $$\\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} |h[m, n]| < \\infty$$

---

### 4. Real-World Applications of 2D System Models
1. **Camera Defocus & Deblurring:** When a photo is out of focus, the optical lens convolves the scene with a pillbox or Gaussian PSF $h[m, n]$. Image restoration uses Wiener deconvolution to recover sharp detail.
2. **Medical CT Reconstruction (Radon Transform):** CT scanners project X-ray line integrals through human bodies, reconstructed using 2D filtered backprojection LSI models.
3. **Motion Compensation in Video:** Video codecs filter previous frames along motion trajectories to predict future frames with near-zero error."""
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
        "punchline": "An end-to-end framework captures, cleans, transforms, quantizes, and compresses multi-dimensional video; using HVS perceptual models and in-loop deblocking filters, it compresses data by 95% while boosting visual SNR.",
        "mnemonic": "A-P-T-Q-E-R-P: Acquisition -> Pre-filtering -> Transform -> Quantize -> Encode -> Reconstruct -> Post-process.",
        "analogy": "Like an automated fruit juice packaging line: fresh oranges are picked from trees (acquisition), washed of dirt and debris (pre-filtering), squeezed into pure liquid essence (transform), concentrated into frozen syrup (quantization), vacuum-sealed in small cans (entropy coding), shipped over trucks (streaming), and mixed with clean water at your kitchen table (reconstruction & post-processing).",
        "diagram": """+-------------------------------------------------------------------------------+
|         END-TO-END MULTI-DIMENSIONAL SIGNAL PROCESSING FRAMEWORK              |
+-------------------------------------------------------------------------------+

 [ Real-World Scene ]
          │
          ▼
 [ 1. Acquisition & Digitization ] ──► CMOS Sensor: 2D Spatial & Temporal Sampling
          │
          ▼
 [ 2. Pre-Filtering & Denoising ]  ──► Optical Anti-Aliasing LPF + Bilateral Denoising
          │
          ▼
 [ 3. 2D/3D Transform ]           ──► 2D-DCT / DWT / Motion Vectors (Energy Compaction)
          │
          ▼
 [ 4. Perceptual Quantization ]    ──► HVS Q-Matrix (Discards unnoticeable high frequencies)
          │
          ▼
 [ 5. Entropy Encoding ]           ──► Huffman / CABAC Lossless Compression
          │
          ▼
 [ 6. Transmission / Storage ]     ──► Compact Bitstream (MP4, JPEG, H.264)
          │
          ▼
 [ 7. Inverse Transform & Synth ]  ──► IDCT / IDWT + Motion Compensation
          │
          ▼
 [ 8. Post-Processing & Display ]  ──► In-loop Deblocking Filter + HDR Tone Mapping
          │
          ▼
 [ High-Quality Display Output ]""",
        "content": """### 1. The Big Picture (The Video Processing Machinery)
To stream an HD movie from a Netflix server to your mobile phone over cellular data, a multi-dimensional signal processing framework must perform high-speed mathematical operations at every stage of the pipeline.

---

### 2. Constructing the Framework (Stage-by-Stage Breakdown)

#### Stage 1: Acquisition & Digitization
- **Spatial Sampling:** Camera CMOS sensor grid converts incoming photons into an array of $1920 \\times 1080$ discrete pixels.
- **Temporal Sampling:** Shutter captures frames at 30 or 60 frames per second.
- **A/D Quantization:** Light intensity at each pixel is converted into an 8-bit or 10-bit digital value.

#### Stage 2: Pre-Filtering & Denoising
- **Optical Low-Pass Filter (OLPF):** Prevents spatial aliasing and moiré patterns on the sensor.
- **Bilateral Filtering:** Smooths out sensor thermal grain in dark rooms while keeping sharp object edges crisp.

#### Stage 3: Multi-Dimensional Transform (Energy Compaction)
- Applies **2D-DCT (Discrete Cosine Transform)** or **DWT (Discrete Wavelet Transform)**.
- *Magic trick:* Packs $90\\%$ of spatial pixel energy into a tiny cluster of low-frequency coefficients, making compression easy.

#### Stage 4: Perceptual Quantization (HVS Optimization)
- Divides transform coefficients by the **Human Visual System (HVS) Quantization Matrix**:
  $$Q[u, v] = \\text{round}\\left( \\frac{F[u, v]}{q[u, v]} \\right)$$
- The human eye is blind to high-frequency fine noise; this stage rounds those invisible frequencies straight to zero!

#### Stage 5: Entropy Encoding (Lossless Packing)
- Converts non-zero coefficients and motion vectors into compact binary streams using **Huffman Coding** or **CABAC (Context-Adaptive Binary Arithmetic Coding)**.

#### Stage 6: Decoding & Inverse Reconstruction
- The receiver performs entropy decoding, dequantization, and runs the **2D-IDCT** to reconstruct the visual frames.

#### Stage 7: Post-Processing & Quality Enhancement
- **In-Loop Deblocking Filter:** Smooths artificial grid seam lines along $8 \\times 8$ block borders.
- **Super-Resolution & HDR Tone-Mapping:** Expands dynamic range for vivid OLED phone screens.

---

### 3. How the Framework Enhances Signal Quality (Exam Scorecard)
1. **Boosts PSNR (Peak Signal-to-Noise Ratio):** Pre-filtering and wavelet thresholding remove camera sensor grain, improving PSNR by $3\\text{ to }6\\text{ dB}$.
2. **Eliminates Compression Artifacts:** Adaptive in-loop deblocking filters prevent blocky pixelation during fast action scenes.
3. **95% Bandwidth Savings:** Compresses 1.5 Gbps raw video down to 5–10 Mbps with zero noticeable loss in visual clarity!"""
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
        "punchline": "Multi-dimensional sampling turns continuous scenes f(x,y) into pixel grids via 2D Dirac comb multiplication; to avoid moiré aliasing, the sampling rate must exceed twice the highest frequency in every direction (fsx >= 2fx, fsy >= 2fy, fst >= 2ft).",
        "mnemonic": "Dirac Comb Picker: fsx >= 2fx, fsy >= 2fy, fst >= 2ft.",
        "analogy": "Looking through a fine window screen at a brick wall: if the screen mesh spacing (sampling rate) is too close to the brick mortar lines (spatial frequency), your eyes see swirling wavy zebra stripes that don't actually exist on the wall (moiré aliasing).",
        "diagram": """Continuous Image f(x, y)          2D Dirac Comb δ_s(x, y)         Sampled Pixel Grid f_s(x, y)
┌──────────────────────┐          ┌──────────────────────┐        ┌──────────────────────┐
│                      │          │ •    •    •    •   T₂│        │ •    •    •    •     │
│   Smooth Landscape   │    x     │                      │   ==►  │  (Sampled Pixels)    │
│                      │          │ •    •    •    •     │        │ •    •    •    •     │
│                      │          │  T₁                  │        │                      │
└──────────────────────┘          └──────────────────────┘        └──────────────────────┘
                                  δ_s(x, y) = Σ Σ δ(x - mT₁, y - nT₂)

2D FREQUENCY SPECTRUM (NYQUIST CHECK):
          v ▲                                  v ▲
            │   (No Aliasing: fsx ≥ 2fx)         │   (ALIASING: fsx < 2fx)
   -fsy/2   │    fsy/2                  -fsy/2   │    fsy/2
   ───┬─────┼─────┬───                   ───┬───┼───┬───
      │  /---\\  │                          │/---\\-+---/---\\│  <-- Spectra Overlap
 ─────┼─(  •  )─┼─────► u            ───────┼(  • X •  )┼──────► u (Moiré distortion!)
      │  \\---/  │                          │\\---/-+---\\---/│
   ───┴─────┼─────┴───                   ───┴───┼───┴───
            │                                    │""",
        "content": """### 1. The Big Picture (Sampling in Multiple Dimensions)
In 1D audio, sampling only happens along time $t$. But an image exists along horizontal $x$ and vertical $y$, and video adds time $t$.
**Multi-dimensional sampling theory** explains how continuous physical light $f(x, y)$ is turned into a grid of discrete pixels without losing detail or creating distorted visual artifacts.

---

### 2. The 2D Sampling Math & The Dirac Comb
To sample a continuous 2D image $f(x, y)$, we multiply it by a **2D Dirac Comb (impulse train)**:
$$\\delta_s(x, y) = \\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} \\delta(x - m T_1, \\ y - n T_2)$$
where $T_1$ is the horizontal pixel spacing and $T_2$ is the vertical pixel spacing.

The sampled image is:
$$f_s(x, y) = f(x, y) \\cdot \\delta_s(x, y) = \\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} f(m T_1, n T_2) \\, \\delta(x - m T_1, y - n T_2)$$
Each discrete spike picks the exact brightness value at grid coordinate $(m T_1, n T_2)$, creating a digital **pixel**!

---

### 3. The Multi-Dimensional Nyquist Criterion
Sampling causes the continuous 2D frequency spectrum to replicate infinitely across a grid with intervals $f_{sx} = \\frac{1}{T_1}$ and $f_{sy} = \\frac{1}{T_2}$.
To prevent adjacent spectral copies from overlapping (**aliasing**):
1. **For 2D Still Images:**
   $$f_{sx} \\ge 2 f_{x,\\max} \\implies T_1 \\le \\frac{1}{2 f_{x,\\max}}$$
   $$f_{sy} \\ge 2 f_{y,\\max} \\implies T_2 \\le \\frac{1}{2 f_{y,\\max}}$$
   *(Sampling rate in both horizontal and vertical directions must exceed twice the highest spatial frequency).*
2. **For 3D Digital Video:**
   We must also satisfy the temporal frame rate:
   $$f_{st} \\ge 2 f_{t,\\max}$$
   *(Frame rate must exceed twice the fastest motion speed to prevent stroboscopic temporal aliasing, like car wheels spinning backwards).*

---

### 4. Sampling Lattices: Rectangular vs Hexagonal
* **Rectangular Grid:** Standard square pixel matrix used in computer screens and cameras. Simple to index ($m, n$).
* **Hexagonal Grid (Honeycomb):** Points are arranged like beehive hexagons. **$13.4\\%$ more efficient** than rectangular grids because circular bandlimited signals pack tightly with zero wasted space!

---

### 5. What Happens If Sampling Fails? (Moiré Patterns)
If $f_{sx} < 2 f_x$, high-frequency textures fold into the low frequencies, producing **Moiré patterns** (wavy rainbow bands on striped shirts or brick walls) and jagged diagonal edges. Cameras place an **optical low-pass filter (OLPF)** in front of the sensor to blur out frequencies above Nyquist before sampling."""
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
        "punchline": "The transformation pipeline converts real-world analog signals into frequency space (DFT/DCT) to make filtering simple, compact energy, and isolate noise before reconstructing the continuous output.",
        "mnemonic": "C-S-Q-T-P-I-D-C: CT Input -> Sample -> Quantize -> Transform -> Process -> Inverse Transform -> DAC -> CT Output.",
        "analogy": "Like packing clothes into a suitcase for travel: you measure your clothes (sampling), fold them into neat squares (quantization), vacuum-compress them into tiny travel pouches (transform), throw out worn-out socks (processing/filtering), unpack them at the hotel (inverse transform), and iron them smooth to wear (reconstruction filter).",
        "diagram": """[ CT Input Signal ] ──► Real-world continuous optical scene f(x, y, t)
        │
        ▼
[ 1. Sampling ]    ──► Discretizes space & time (Nyquist: fs ≥ 2f_max)
        │
        ▼
[ 2. Quantization] ──► Converts continuous light intensities to discrete 8-bit integers
        │
        ▼
[ 3. Transform ]   ──► Core stage: 2D-DFT / DCT converts spatial pixels into frequencies
        │
        ▼
[ 4. Processing ]  ──► Point-by-point multiplication filtering, noise removal & compression
        │
        ▼
[ 5. Inverse Trans]──► IDFT / IDCT reconstructs discrete spatial pixel matrix
        │
        ▼
[ 6. Reconstruction]─► DAC + Analog Reconstruction Low-Pass Filter removes mirror replicas
        │
        ▼
[ CT Output Signal]──► Continuous real-world viewable output!""",
        "content": """### 1. The Big Picture (Why Transform?)
Real-world visual signals are complex continuous phenomena. Operating on them directly in spatial coordinates is slow and mathematically difficult (e.g., 2D spatial convolution takes a painful $O(N^4)$ steps).
The **transformation process** maps signals into the frequency/transform domain where complex convolution turns into fast point-by-point multiplication and signal energy gets packed into a few compact coefficients.

---

### 2. Functional Significance of Each Stage (Unit 3 Notes)

#### Stage 1: Continuous-Time / Spatial Input (CT Input)
* **What it is:** Real-world continuous optical light $f(x, y)$ or analog video $f(x, y, t)$ before digital measurement.

#### Stage 2: Sampling
* **What it does:** Samples continuous coordinates at discrete intervals $(m T_1, n T_2)$.
* **Significance:** Must satisfy the **Nyquist criterion** ($f_s \\ge 2 f_{\\max}$) along all axes to avoid aliasing and moiré distortions.

#### Stage 3: Quantization
* **What it does:** Rounds continuous sample amplitudes into finite digital levels (e.g., 8-bit values $0$ to $255$).
* **Significance:** Enables storage in digital computer memory and GPU buffers.

#### Stage 4: Transformation Block (Core Stage)
* **What it does:** Applies linear mathematical transforms like the **2D-DFT, 2D-DCT, or Wavelet Transform (DWT)**.
* **Significance:** Decomposes complex spatial pixel patterns into orthogonal frequency basis functions. Concentrates $>90\\%$ of image energy into the top-left coefficients (**energy compaction**).

#### Stage 5: Processing in Transform Domain
* **What it does:** Performs targeted filtering, noise suppression, or perceptual quantization.
* **Significance:** Replaces brutal 2D convolution ($O(N^4)$) with instantaneous point-by-point multiplication ($O(N^2)$):
  $$Y[u, v] = X[u, v] \\cdot H[u, v]$$

#### Stage 6: Inverse Transformation
* **What it does:** Applies the Inverse Transform (2D-IDFT or 2D-IDCT).
* **Significance:** Converts frequency coefficients back into recognizable 2D spatial pixel rows and columns.

#### Stage 7: Dequantization & Reconstruction Filter (DAC Stage)
* **What it does:** Passes discrete samples through a Digital-to-Analog Converter (DAC) and an analog low-pass anti-imaging filter.
* **Significance:** Removes high-frequency mirror replicas, producing a smooth, continuous analog output for displays.

---

### 3. Cheat Sheet: Why Do We Transform?
1. **Computational Speed:** Multi-dimensional convolution becomes simple multiplication.
2. **Energy Compaction:** DCT packs almost all energy into low frequencies (basis of JPEG/MPEG).
3. **Selective Filtering:** Separates high-frequency noise spikes from structural image edges."""
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
        "punchline": "Human eyes have 120 million brightness rods but only 6 million color cones, and are blind to high-frequency fine noise; codecs exploit this via YCbCr 4:2:0 chroma subsampling (50% instant savings) and coarse DCT quantization.",
        "mnemonic": "L-C-C-P: Luminance sensitivity, Contrast sensitivity, Color perception, Perceptual quantization.",
        "analogy": "Printing a novel with microscopic ink that requires an electron microscope to read: nobody can see those tiny details anyway, so spending millions of bits encoding invisible high-frequency details is pure waste. HVS compression simply throws away what human biology cannot see!",
        "diagram": """1. LUMINANCE VS CHROMINANCE SENSITIVITY:
   Human Eye: ~120 Million Rods (Luminance Y) vs ~6-7 Million Cones (Color Cb, Cr)
   RGB Image (100% data) ──► YCbCr Conversion ──► 4:2:0 Chroma Subsampling (50% Data Cut!)
   [ Y: Full Res 1920x1080 ] + [ Cb: Half Res 960x540 ] + [ Cr: Half Res 960x540 ]

2. CONTRAST SENSITIVITY FUNCTION (CSF):
   Contrast ▲               Peak Human Eye Sensitivity (3-5 cycles/degree)
   Sensitivity              /---\\
           │             /       \\
           │            /         \\    Eye is completely blind to high-frequency noise!
           │           /           \\   ==> HEAVILY QUANTIZE HIGH FREQUENCIES (Throw to 0)
           └──────────┴─────────────┴──────────► Spatial Frequency (cycles/degree)
                      Low          High

3. JPEG QUANTIZATION MATRIX Q[u, v]:
   Low Freq (Fine step size = High Precision) ──► High Freq (Coarse step = Rounded to ZERO!)""",
        "content": """### 1. The Big Picture (Engineering for Human Biology)
If an image compression algorithm preserves every single photon with $100\\%$ mathematical perfection, video files would be too gigantic to stream. 
The secret to modern video codecs (JPEG, H.264, HEVC) is **perceptual transparency**: using the biological limitations of the **Human Visual System (HVS)** to throw away data that human eyes literally cannot perceive.

---

### 2. The 3 Core HVS Properties & Their Engineering Exploitation

#### 1. Luminance Sensitivity vs Chrominance Sensitivity
* **Biological Fact:** 
  The human retina contains approximately **120 million rod cells** (which detect black-and-white brightness / luminance) but only **6 to 7 million cone cells** (which detect color / chrominance, clustered tightly in the fovea). Human eyes have razor-sharp acuity for brightness borders, but are blurry and clumsy when detecting color variations!
* **Engineering Impact:**
  1. We convert RGB images into decoupled **YCbCr** color space:
     $$Y = 0.299 R + 0.587 G + 0.114 B \\quad (\\text{Luminance / Brightness})$$
     $$Cb = -0.1687 R - 0.3313 G + 0.5 B + 128 \\quad (\\text{Blue-difference Chrominance})$$
     $$Cr = 0.5 R - 0.4187 G - 0.0813 B + 128 \\quad (\\text{Red-difference Chrominance})$$
  2. **Chroma Subsampling (4:2:0):** We keep full resolution for Luminance $Y$, but downsample $Cb$ and $Cr$ by $2\\times$ horizontally and $2\\times$ vertically. 
  3. **The Result:** Instantly cuts uncompressed video bitrate by **$50\\%$** with zero perceptible drop in visual quality!

#### 2. Contrast Perception & Contrast Sensitivity Function (CSF)
* **Biological Fact:**
  Humans do not perceive absolute light; we perceive relative contrast ($C = \\frac{\\Delta I}{I}$). Our sensitivity follows the **Contrast Sensitivity Function (CSF)**:
  - Peak sensitivity occurs at intermediate spatial frequencies (**3 to 5 cycles per degree** of visual angle).
  - Sensitivity drops off a cliff at high spatial frequencies (fine grain and microscopic noise are completely invisible at normal viewing distances).
* **Engineering Impact:**
  - After 2D-DCT, high-frequency coefficients are divided by huge step sizes in the **JPEG Quantization Matrix ($Q_{uv}$)**.
  - This forces subtle high-frequency numbers straight to zero, enabling massive run-length compression.

#### 3. Spatial & Temporal Masking
* **Biological Fact:**
  The human eye cannot spot compression artifacts in busy, highly textured regions (like rushing river rapids or grass fields), nor can it see fine details during fast camera pans.
* **Engineering Impact:** Codecs allocate fewer bits to textured or fast-moving macroblocks and divert bit-budgets to smooth areas (like skies or faces) where banding is easily spotted.

---

### 3. Summary of Justified Perceptual Models
| Perceptual Model | Codec Implementation | Practical Benefit |
| :--- | :--- | :--- |
| **YCbCr Decoupling** | Decouples brightness from color | Eliminates inter-channel RGB correlation |
| **4:2:0 Chroma Subsampling**| Discards $75\\%$ of $Cb$ and $Cr$ samples | **$50\\%$ instant bandwidth reduction** with zero visible blur |
| **CSF Quantization Matrix**| Divides high DCT frequencies coarsely | Zeros out invisible details; drives $10:1$ to $20:1$ compression |
| **Temporal JND Masking** | Permits higher quantization noise during motion | Stabilizes bitrate during fast scene transitions |"""
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
        "punchline": "A digital video system treats video as a 3D signal f(x,y,t); it combines 2D spatial sampling, 30 fps capture, an I/P/B GOP frame structure, and motion-compensated prediction to eliminate up to 90% of redundant data.",
        "mnemonic": "S-F-T-S: 3D Sampling, Frame structure (I/P/B), Temporal redundancy reduction, Standards (H.264/HEVC).",
        "analogy": "Transmitting video without temporal redundancy reduction is like re-mailing an entire 500-page book every day even if you only changed one comma on page 42; motion-compensated video coding simply texts the recipient: 'On page 42, move sentence 3 right by 5 pixels' (motion vector + prediction residual).",
        "diagram": """1. 3D SIGNAL SAMPLING:
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
        "content": """### 1. Architectural Design of a Digital Video System (Unit 3 Notes)
A complete digital video representation system converts real-world optical motion into a compact, bandwidth-efficient digital bitstream. The architecture rests on three core pillars:
1. **Multi-Dimensional Sampling (3D Signal Representation)**
2. **Hierarchical Frame Structure (Group of Pictures - GOP)**
3. **Temporal Redundancy Reduction (Motion Compensation)**

---

### 2. Pillar 1: Multi-Dimensional Sampling Theory in Video
Video is treated as a continuous 3D spatio-temporal signal $f(x, y, t)$:
* **Spatial Sampling (The Pixel Grid):**
  Discretizes the optical image into pixels $(m \\Delta x, n \\Delta y)$. Must satisfy 2D Nyquist ($f_{sx} \\ge 2 f_{x,\\max}$ and $f_{sy} \\ge 2 f_{y,\\max}$) to avoid moiré fringes. Common standards: Full HD ($1920 \\times 1080$), 4K UHD ($3840 \\times 2160$).
* **Temporal Sampling (Frame Rate):**
  Snaps frames at uniform time intervals $T_t = \\frac{1}{f_{st}}$.
  - 24 fps: Cinematic standard.
  - 30 fps: Standard television broadcast.
  - 60 fps / 120 fps: Sports and gaming (prevents motion jitter).
* **Color Sampling:** Converts RGB to **YCbCr 4:2:0**, allocating full resolution to brightness $Y$ and quarter resolution to color $Cb, Cr$ (cutting data by $50\\%$).

---

### 3. Pillar 2: Frame Structure & Group of Pictures (GOP)
Video frames are organized into repeating clusters called a **Group of Pictures (GOP)**, balancing compression efficiency with random seeking:
1. **I-Frames (Intra-Coded Frames):**
   - Encoded completely independently (like a standalone JPEG photo).
   - Exploits only spatial redundancy.
   - Provides random access points for video seeking and channel switching.
   - Largest file size, lowest compression.
2. **P-Frames (Predictive-Coded Frames):**
   - Encoded using motion-compensated forward prediction from the previous I or P frame.
   - Stores only motion displacement vectors and residual prediction differences.
3. **B-Frames (Bi-directionally Predictive Frames):**
   - Interpolated using motion vectors from both **past and future** reference frames.
   - Highest compression efficiency of all frame types.
4. **Standard GOP Pattern:**
   $$I \\; B \\; B \\; P \\; B \\; B \\; P \\; B \\; B \\; I$$
   *(GOP length typically 12 to 15 frames, providing an anchor I-frame every 0.5 seconds at 30 fps).*

---

### 4. Pillar 3: Temporal Redundancy Reduction Techniques
Because video frames are captured every 33 ms, adjacent frames are $>90\\%$ identical. We eliminate this redundancy through:

#### a) Frame Differencing (Basic Baseline):
Subtracts the previous frame directly: $D_t(x, y) = F_t(x, y) - F_{t-1}(x, y)$. Fails if the camera or objects move.

#### b) Block-Based Motion Estimation (BMA):
Divides current frame $F_t$ into $16 \\times 16$ macroblocks. Searches the reference frame $F_{t-1}$ within a $\\pm p$ window to find the candidate block that minimizes the **Sum of Absolute Differences (SAD)**:
$$\\text{SAD}(dx, dy) = \\sum_{m=0}^{15} \\sum_{n=0}^{15} |F_t(x+m, y+n) - F_{t-1}(x+m+dx, y+n+dy)|$$
Output: A compact **Motion Vector** $\\mathbf{MV} = (dx, dy)$ for each block.

#### c) Motion Compensation & Residual Coding:
Forms predicted frame $\\hat{F}_t(x, y) = F_{t-1}(x - dx, y - dy)$ and subtracts it from the actual frame to get the **prediction residual**:
$$E_t(x, y) = F_t(x, y) - \\hat{F}_t(x, y)$$
Because motion compensation tracks object movement, the residual $E_t$ is near zero! Compressing this residual via 2D-DCT achieves over **$90\\%$ bitrate reduction**.

---

### 5. Final Justification of System Design
- **Sampling Theory:** Guarantees artifact-free capture and reconstruction of continuous 3D scenes.
- **GOP Structure:** Enables instant seeking and scrub-bar playback while maximizing compression via B/P frames.
- **Motion Compensation:** Slashes uncompressed 1.5 Gbps video down to 5–10 Mbps in modern H.264/AVC and H.265/HEVC streaming platforms."""
    }
]
