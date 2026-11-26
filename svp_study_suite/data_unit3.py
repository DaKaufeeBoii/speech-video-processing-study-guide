# -*- coding: utf-8 -*-
"""
Unit 3: Multi-Dimensional Signals, Transforms, Sampling & Digital Video Representation
Questions: Mid-I Q17 to Q20 AND Mid-II Q1 to Q4
Academic Year: 2026-27 | Regulation: KGR23 | Course Code: KG23ACM408
Scaled strictly for exam success (05 Marks vs 10 Marks format).
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
        "punchline": "Multi-dimensional (M-D) signals depend on 2 or more independent spatial/temporal variables (e.g. 2D image f(x,y), 3D video f(x,y,t)); characterized by spatial correlation, non-causality, and massive data volume.",
        "mnemonic": "S-T-V-M: Spatial 2D, Temporal 3D, Volumetric CT/MRI, Massive dimensionality",
        "analogy": "A single note on a guitar is 1D (sound vs time); an oil painting is 2D (color vs horizontal/vertical position); a 3D movie is 3D (2D frames moving through time).",
        "diagram": """MULTI-DIMENSIONAL SIGNAL TAXONOMY:
  1D Signal (Speech)      : s(t)          ──► [ Amplitude vs Time ]
  2D Signal (Still Image) : f(x, y)       ──► [ Intensity vs (Horizontal, Vertical) ]
  3D Signal (Digital Video): f(x, y, t)   ──► [ 2D Spatial Frames over Time t ]
  3D Signal (Medical CT)  : f(x, y, z)    ──► [ Volumetric Voxel Grid in 3D Space ]
  4D Signal (Dynamic MRI) : f(x, y, z, t) ──► [ Beating Heart Volume over Time ]

CORE CHARACTERISTICS:
  1. Spatial Correlation  (Neighboring pixels are highly similar)
  2. Non-Causal Nature    (Pixels exist simultaneously in all spatial directions)
  3. Massive Data Bandwidth (HD Video requires Gbps without compression)""",
        "content": """### 1. Definition and Mathematical Representation
A **Multi-Dimensional (M-D) signal** is a physical quantity whose value depends on two or more independent variables:
1. **2D Signals (Still Images):**
   * Represented as a continuous 2D function $f(x, y)$, or a discrete matrix $I[m, n]$, where $x, y$ are spatial coordinates and $f(x, y)$ represents optical brightness (luminance) or color vector $[R, G, B]^T$.
2. **3D Signals:**
   * **Digital Video:** $f(x, y, t)$, where $x, y$ are spatial coordinates and $t$ is continuous time.
   * **Volumetric Medical Imaging (CT / MRI):** $f(x, y, z)$, representing 3D spatial tissue attenuation / density.
3. **4D Signals (Dynamic Spatio-Temporal Volumes):**
   * Functional MRI / 4D Ultrasound: $f(x, y, z, t)$ (e.g., observing a beating 3D heart volume over time).

---

### 2. Key Characteristics of Multi-Dimensional Signals

#### 1. High Spatial & Temporal Correlation
* Adjacent pixels in an image possess nearly identical grayscale or color values.
* Adjacent video frames have $>95\\%$ identical content, with differences restricted to small moving objects (**temporal redundancy**).

#### 2. Non-Causality in Spatial Dimensions
* In 1D speech processing, time is strictly **causal** ($t$ only moves forward; a system cannot depend on future samples $t+1$ without delay).
* In 2D images, space is **non-causal**: pixel $(m, n)$ is surrounded on all sides (left, right, top, bottom). Filtering can access all directions simultaneously (e.g., zero-phase symmetric filters).

#### 3. Separability
* An M-D signal or filter $f(x, y)$ is **separable** if it can be factored into a product of 1D functions:
  $$f(x, y) = f_1(x) \\cdot f_2(y)$$
* Separability reduces computational complexity from $O(N^2)$ to $O(2N)$.

#### 4. Massive Data Volume
* A single second of uncompressed Full HD video ($1920 \\times 1080$, 60 fps, 24-bit color) requires:
  $$1920 \\times 1080 \\times 3 \\times 60 \\approx 373\\text{ MB/second} \\approx 3.0\\text{ Gbps!}$$

---

### 3. Significance in Advanced Signal Processing Applications
1. **Digital Video Compression (H.264, HEVC, AV1):** Eliminates spatial and temporal redundancies to stream 4K video over broadband.
2. **Autonomous Vehicles & Robotics:** 3D LiDAR point clouds and stereo camera streams processed for real-time obstacle detection and path planning.
3. **Medical Imaging (Radiology):** 3D volume reconstruction from 2D X-ray projection angles via Radon transform (Filtered Back-Projection).
4. **Satellite & Remote Sensing:** Hyperspectral imaging ($f(x, y, \\lambda)$) measuring surface reflectance across hundreds of spectral wavelengths."""
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
        "punchline": "2D-DFT decomposes an image into 2D spatial sinusoidal frequencies; separable into 1D row-column DFTs; center DC represents average brightness, while high-frequency axes correspond to vertical and horizontal edges.",
        "mnemonic": "R-C-C-E: Row-Column separability, Center DC shift, Edge orthogonality",
        "analogy": "An architectural blueprint analyzer: Instead of inspecting every brick (pixel), the 2D-DFT tells you the repeating horizontal beam spacings and vertical column rhythms in the building.",
        "diagram": """2D-DFT SEPARABLE COMPUTATION (Row-Column Decomposition):
   Input Image f(x, y) [M x N]
            │
            ▼  Step 1: Apply 1D-DFT along every Row
   Intermediate Matrix G(u, y)
            │
            ▼  Step 2: Apply 1D-DFT along every Column
   2D-DFT Spectrum F(u, v)

SPECTRAL INTERPRETATION (Shifted Spectrum):
   ┌─────────────────────────────────────┐
   │ High Spatial Freq (Fine Texture)    │
   │                  ▲ v (Vertical Freq)│
   │                  │                  │
   │         Horizontal Edges            │
   │                  │                  │
   │ ── Vertical ────(DC)──── Edges ───► u (Horizontal Freq)
   │                  │ (Average Lum)    │
   │                  │                  │
   │                                     │
   └─────────────────────────────────────┘""",
        "content": """### 1. Mathematical Definition of 2D-DFT
For an $M \\times N$ digital image $f(x, y)$ (where $0 \\le x \\le M-1$ and $0 \\le y \\le N-1$), the 2D Discrete Fourier Transform (2D-DFT) is defined as:
$$F(u, v) = \\sum_{x=0}^{M-1} \\sum_{y=0}^{N-1} f(x, y) e^{-j 2\\pi \\left( \\frac{ux}{M} + \\frac{vy}{N} \\right)}$$
for spatial frequency indices $u = 0, 1, \\dots, M-1$ and $v = 0, 1, \\dots, N-1$.

#### Inverse 2D-DFT (Reconstruction):
$$f(x, y) = \\frac{1}{MN} \\sum_{u=0}^{M-1} \\sum_{v=0}^{N-1} F(u, v) e^{j 2\\pi \\left( \\frac{ux}{M} + \\frac{vy}{N} \\right)}$$

---

### 2. Application of Separability Property
The 2D transform kernel is **separable**:
$$e^{-j 2\\pi \\left( \\frac{ux}{M} + \\frac{vy}{N} \\right)} = e^{-j 2\\pi \\frac{ux}{M}} \\cdot e^{-j 2\\pi \\frac{vy}{N}}$$

This allows the 2D-DFT to be computed as two successive passes of 1D-DFTs (**Row-Column Algorithm**):
1. **Row Transform:** Compute the 1D-DFT of each of the $M$ rows of length $N$:
   $$G(x, v) = \\sum_{y=0}^{N-1} f(x, y) e^{-j 2\\pi \\frac{vy}{N}}$$
2. **Column Transform:** Compute the 1D-DFT of each of the $N$ columns of $G(x, v)$:
   $$F(u, v) = \\sum_{x=0}^{M-1} G(x, v) e^{-j 2\\pi \\frac{ux}{M}}$$
* **Computational Speedup:** Direct 2D-DFT requires $O(M^2 N^2)$ operations. Using 1D-FFTs reduces this to $O(MN \\log_2(MN))$ (**thousands of times faster**).

---

### 3. Spatial vs. Frequency Domain Representation

#### 1. DC Component ($F(0, 0)$)
Setting $u = 0, v = 0$:
$$F(0, 0) = \\sum_{x=0}^{M-1} \\sum_{y=0}^{N-1} f(x, y) = MN \\cdot \\bar{f}$$
The DC term equals the sum of all pixel values, directly proportional to the **average brightness** of the image.

#### 2. Spatial Frequency Axes & Edge Orientation
When the spectrum is centered (via `fftshift`, multiplying $f(x,y)$ by $(-1)^{x+y}$):
* **Horizontal Axis ($u$, with $v = 0$):** Corresponds to variations along the horizontal direction. A high value indicates sharp **vertical edges** in the spatial image.
* **Vertical Axis ($v$, with $u = 0$):** Corresponds to variations along the vertical direction. A high value indicates sharp **horizontal edges** in the spatial image.
* **Low Frequencies (Center):** Carry smooth illumination and gross object shapes (most image energy).
* **High Frequencies (Periphery):** Carry edges, boundaries, noise, and fine texture.

---

### 4. Practical Image Applications
1. **Low-Pass Filtering (Blurring / Denoising):** Multiply $F(u, v)$ by an ideal or Gaussian mask $H(u, v)$ that sets high frequencies to zero, suppressing high-frequency sensor noise.
2. **High-Pass Filtering (Edge Detection):** Suppress low frequencies and retain high frequencies to highlight contours and object boundaries.
3. **Periodic Noise Removal (Notch Filtering):** Periodic interference (e.g. electrical hum on video sensors) appears as bright isolated spikes in $F(u, v)$. Setting these specific spike coordinates to zero completely eliminates the artifact."""
    },
    {
        "id": "MID1-Q19",
        "mid": "Mid-I",
        "qno": 19,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Evaluate multi-dimensional system models by analyzing their input–output relationships using convolution and transform domain methods.",
        "punchline": "2D Linear Shift-Invariant (LSI) systems are completely characterized by their 2D impulse response h[m,n]; spatial 2D convolution y = x ** h maps to frequency-domain multiplication Y = X · H via 2D-DFT/Z-transform.",
        "mnemonic": "L-S-I-C: Linear Shift-Invariant, 2D Convolution, Frequency Multiplication, Separability",
        "analogy": "A camera lens with a dirty smear: The true scene x[m,n] is convolved with the point spread function h[m,n] of the lens smear, producing the blurred photograph y[m,n].",
        "diagram": """2D SPATIAL DOMAIN LSI SYSTEM:
  Input Image x[m, n] ──► [ 2D System h[m, n] ] ──► Output Image y[m, n]
                          (Impulse Response / PSF)    y[m, n] = x[m, n] ** h[m, n]

TRANSFORM DOMAIN (2D-DFT / 2D Z-Transform):
  X(ω1, ω2) ────────────► [ Frequency Response H(ω1, ω2) ] ──► Y(ω1, ω2) = X · H

SEPARABLE 2D CONVOLUTION (Speedup from O(M^2 N^2) to O(2MNK)):
  Input x[m, n] ──► [ 1D Row Filter h1[m] ] ──► [ 1D Col Filter h2[n] ] ──► Output y[m, n]""",
        "content": """### 1. Multi-Dimensional Linear Shift-Invariant (LSI) Systems
A 2D discrete system $\\mathcal{T}\\{\\cdot\\}$ maps an input image $x[m, n]$ to an output image $y[m, n]$. It is **Linear Shift-Invariant (LSI)** if:
1. **Linearity (Superposition):**
   $$\\mathcal{T}\\{a x_1[m, n] + b x_2[m, n]\\} = a \\mathcal{T}\\{x_1[m, n]\\} + b \\mathcal{T}\\{x_2[m, n]\\}$$
2. **Shift-Invariance (Spatial Invariance):**
   $$\\text{If } \\mathcal{T}\\{x[m, n]\\} = y[m, n], \\quad \\text{then } \\mathcal{T}\\{x[m - m_0, n - n_0]\\} = y[m - m_0, n - n_0]$$

---

### 2. Input-Output Relationship: 2D Spatial Convolution
An LSI system is uniquely and completely characterized by its **2D Unit Impulse Response** $h[m, n] = \\mathcal{T}\\{\\delta[m, n]\\}$ (also called the **Point Spread Function - PSF** in optical imaging).

#### 2D Discrete Convolution Formula:
$$y[m, n] = x[m, n] ** h[m, n] = \\sum_{k=-\\infty}^{\\infty} \\sum_{l=-\\infty}^{\\infty} x[k, l] \\, h[m - k, n - l]$$

#### Computational Procedure:
1. **Spatial Flip:** Reflect $h[k, l]$ around both axes to obtain $h[-k, -l]$.
2. **Spatial Shift:** Translate $h[-k, -l]$ by offsets $m$ and $n$ to form $h[m - k, n - l]$.
3. **Point-wise Multiplication:** Multiply $x[k, l]$ by $h[m - k, n - l]$.
4. **Double Summation:** Sum all products over the support of the filter.

---

### 3. Transform-Domain Analysis: 2D Z-Transform & 2D-DFT

#### 1. 2D Z-Transform & Transfer Function
The 2D Z-Transform of sequence $x[m, n]$ is:
$$X(z_1, z_2) = \\sum_{m=-\\infty}^{\\infty} \\sum_{n=-\\infty}^{\\infty} x[m, n] z_1^{-m} z_2^{-n}$$
Applying the 2D Z-transform to the convolution equation:
$$Y(z_1, z_2) = X(z_1, z_2) \\cdot H(z_1, z_2)$$
where $H(z_1, z_2) = \\frac{Y(z_1, z_2)}{X(z_1, z_2)}$ is the **2D System Transfer Function**.

#### 2. Frequency Response
Evaluating $H(z_1, z_2)$ on the unit bi-circle ($z_1 = e^{j \\omega_1}, z_2 = e^{j \\omega_2}$):
$$H(\\omega_1, \\omega_2) = |H(\\omega_1, \\omega_2)| e^{j \\theta(\\omega_1, \\omega_2)}$$
* $|H(\\omega_1, \\omega_2)|$: Magnitude response (amplification/attenuation of spatial frequencies).
* $\\theta(\\omega_1, \\omega_2)$: Phase response (spatial displacement). In image processing, **zero-phase or linear-phase filters** are strictly required to avoid phase distortion (which destroys edges and creates ghosting).

---

### 4. Evaluation of Spatial vs. Transform Domain Filtering

| Feature | Spatial Domain Convolution | Transform Domain Multiplication (2D-FFT) |
| :--- | :--- | :--- |
| **Operation** | Direct double sliding sum | $y = \\text{IFFT2}\\{\\text{FFT2}(x) \\cdot \\text{FFT2}(h)\\}$ |
| **Complexity (Kernel $K \\times K$)** | $O(M N K^2)$ | $O(M N \\log_2(MN))$ |
| **Best Suited For** | Small kernels ($3 \\times 3, 5 \\times 5$) like Sobel, Laplacian | Large kernels ($K > 15$) or global blurring filters |
| **Boundary Effects** | Handled by zero-padding, replicate, or reflect | Circular convolution wrap-around (requires zero-padding) |
| **Memory Consumption** | Minimal (operates in-place on sliding window) | High (requires full complex floating-point matrices) |

---

### 5. Separable 2D Systems (Computational Optimization)
A 2D filter kernel is **separable** if $h[m, n] = h_1[m] \\cdot h_2[n]$.
* Instead of performing a 2D convolution requiring $K^2$ multiplications per pixel, the image is filtered row-by-row with 1D kernel $h_1[m]$ ($K$ ops), then column-by-column with 1D kernel $h_2[n]$ ($K$ ops).
* **Speedup:** Reduces operations from $K^2$ to $2K$. For a $9 \\times 9$ Gaussian filter, operations drop from 81 to 18 (**4.5x faster**)."""
    },
    {
        "id": "MID1-Q20",
        "mid": "Mid-I",
        "qno": 20,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Design and formulate a multi-dimensional signal processing framework for applications such as image or video systems, and justify the choice of transforms and system models.",
        "punchline": "A complete image/video compression framework incorporates block partition, 2D-DCT transform, psycho-visual quantization, zig-zag reordering, and entropy coding, achieving 10:1 to 50:1 compression.",
        "mnemonic": "P-T-Q-Z-E: Partition (8x8), Transform (2D-DCT), Quantize (HVS matrix), Zig-zag scan, Entropy coding",
        "analogy": "Packing luggage for a flight: You group clothes into small cubes (8x8 blocks), fold and vacuum-seal them (DCT energy compaction), discard worn-out socks you don't need (quantization), and pack tight into the suitcase (entropy coding).",
        "diagram": """END-TO-END MULTI-DIMENSIONAL COMPRESSION FRAMEWORK (JPEG / MPEG Pipeline):

  Spatial Image/Frame f(x, y)
             │
             ▼
  ┌─────────────────────────────────┐
  │ 1. Color Space Conversion       │  RGB ──► YCbCr (Luminance + Chrominance)
  │    & Chroma Subsampling         │  4:4:4 ──► 4:2:0 (Discards 50% chroma data)
  └────────────────┬────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │ 2. Block Partitioning           │  Divide image into non-overlapping 8x8 blocks
  └────────────────┬────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │ 3. 2D-DCT Transform             │  Spatial domain ──► Frequency domain
  │    (Discrete Cosine Transform)  │  Compacts 90% energy into top-left coefficients
  └────────────────┬────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │ 4. Psycho-visual Quantization   │  Divide by Quantization Matrix Q(u, v) & Round
  │    (Lossy Step)                 │  High frequencies zeroed out based on HVS
  └────────────────┬────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │ 5. Zig-Zag Scan & Run-Length    │  Converts 2D matrix into 1D array;
  │    Encoding (RLE)               │  Groups long runs of trailing zeros
  └────────────────┬────────────────┘
                   │
                   ▼
  ┌─────────────────────────────────┐
  │ 6. Entropy Coding (Huffman/CABAC│  Assigns short codes to frequent symbols
  └────────────────┬────────────────┘
                   │
                   ▼
        [ Compressed Bitstream (.jpg / .mp4) ]""",
        "content": """### 1. Framework Architecture Overview
To process and compress multi-dimensional visual signals (still images and video frames), an end-to-end framework must eliminate three primary redundancies:
1. **Spatial Redundancy:** Correlation between neighboring pixels in a frame.
2. **Spectral / Psychovisual Redundancy:** Human eye is far less sensitive to fine color changes and high spatial frequencies than luminance.
3. **Coding Redundancy:** Non-uniform probability of occurrence of quantized symbols.

---

### 2. Stage-by-Stage Framework Design

#### Stage 1: Color Space Conversion & Chroma Subsampling
* Convert raw RGB image into **YCbCr**:
  $$Y = 0.299 R + 0.587 G + 0.114 B \\quad \\text{(Luminance)}$$
  $$Cb = -0.1687 R - 0.3313 G + 0.5 B + 128 \\quad \\text{(Blue Chroma)}$$
  $$Cr = 0.5 R - 0.4187 G - 0.0813 B + 128 \\quad \\text{(Red Chroma)}$$
* Apply **4:2:0 Chroma Subsampling**: Subsample Cb and Cr by a factor of 2 horizontally and vertically. This instantly cuts raw data size by **$50\\%$** with zero perceptible loss in visual quality.

#### Stage 2: Block Partitioning
* Divide the $Y, Cb, Cr$ planes into non-overlapping blocks of $8 \\times 8$ or $16 \\times 16$ pixels (Macroblocks).
* Limits computational complexity and accounts for local image statistics.

#### Stage 3: Transform Domain Representation (2D-DCT-II)
* Each $8 \\times 8$ block is transformed using the 2D Discrete Cosine Transform:
  $$F(u, v) = \\frac{1}{4} C(u) C(v) \\sum_{x=0}^7 \\sum_{y=0}^7 f(x, y) \\cos\\left[ \\frac{(2x + 1) u \\pi}{16} \\right] \\cos\\left[ \\frac{(2y + 1) v \\pi}{16} \\right]$$
  where $C(k) = \\frac{1}{\\sqrt{2}}$ for $k = 0$, and $C(k) = 1$ otherwise.

#### Stage 4: Psychovisual Quantization (The Core Lossy Step)
* Divide each DCT coefficient by an experimentally derived Quantization Matrix $Q(u, v)$ and round to the nearest integer:
  $$F_q(u, v) = \\text{round}\\left( \\frac{F(u, v)}{Q(u, v)} \\right)$$
* High-frequency entries in $Q(u, v)$ are very large, driving imperceptible high-frequency texture coefficients to **zero**.

#### Stage 5: Zig-Zag Scanning & Run-Length Encoding (RLE)
* Reorder the $8 \\times 8$ matrix into a 1D sequence of 64 elements via a **Zig-Zag Scan**.
* Groups low-frequency non-zero terms first, followed by long runs of trailing zeros encoded as `(run_length, value)` pairs terminated by an End-Of-Block (EOB) marker.

#### Stage 6: Lossless Entropy Coding (Huffman / CABAC)
* Variable-length coding assigns short binary codes to frequent symbols and long codes to rare symbols.

---

### 3. Rigorous Justification of Transform Selection: Why 2D-DCT over 2D-DFT?

| Evaluation Criteria | 2D-DFT | 2D-DCT (Chosen) |
| :--- | :--- | :--- |
| **Boundary Continuity** | Assumes periodic extension. If opposite borders differ, creates sharp discontinuities (**blocking artifacts & spectral leakage**). | Assumes **even-symmetric reflection** across boundaries, eliminating edge discontinuities. |
| **Energy Compaction** | Moderate; spreads energy across positive and negative frequencies. | **Superior:** Compares closely to optimal Karhunen-Loève Transform (KLT). Packs $>90\\%$ of block energy into top-left 3-5 coefficients. |
| **Arithmetic Type** | Complex numbers (real + imaginary parts), doubling storage. | **Purely real-valued arithmetic**, halving memory and computational hardware. |
| **Standard Adoption** | Used for filtering and optical analysis | Universal standard for JPEG, MPEG-1/2/4, H.264/AVC, HEVC |

---

### 4. Framework Performance Evaluation
* **Compression Ratio:** Typically achieves **$10:1$ to $25:1$** for visually lossless still images, and **$50:1$ to $100:1$** for video when coupled with inter-frame motion compensation.
* **Reconstruction Quality:** Evaluated objectively via Peak Signal-to-Noise Ratio (PSNR $\\ge 35\\text{ dB}$) and Structural Similarity Index (SSIM $\\ge 0.95$)."""
    },
    {
        "id": "MID2-Q01",
        "mid": "Mid-II",
        "qno": 1,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Explain the concept of multi-dimensional sampling theory.",
        "punchline": "M-D sampling converts continuous space-time signals into discrete grids via sampling matrices/lattices; Nyquist requires sampling rates along each axis to exceed twice the maximum directional bandwidth.",
        "mnemonic": "L-G-N-A: Sampling Lattice, Geometry (Rect vs Hex), Nyquist rates, Aliasing replication",
        "analogy": "Like laying down tiles in a bathroom: Rectangular tiles sample along square grid points; hexagonal tiles pack closer together, covering the floor with fewer tiles (optimal sampling).",
        "diagram": """MULTI-DIMENSIONAL SAMPLING GEOMETRIES:
  1. RECTANGULAR LATTICE:                2. HEXAGONAL LATTICE:
     ●   ●   ●   ●   (T1, 0)                ●     ●     ●
                                                   ●     ●     ●
     ●   ●   ●   ●   (0, T2)                ●     ●     ●
     Sample Matrix V = [ T1   0 ]               Optimal for circular bandlimited
                       [  0  T2 ]               signals (saves ~13.4% samples!)

SPECTRAL REPLICATION & 2D NYQUIST CONDITION:
  Continuous Spectrum F(ω1, ω2) ──► Replicated on Reciprocal Lattice U = 2π V^-T
  Condition to prevent spectral overlap (Aliasing):
       fsx ≥ 2 · f_max,x   AND   fsy ≥ 2 · f_max,y""",
        "content": """### 1. Fundamentals of Multi-Dimensional Sampling
Multi-dimensional sampling theory extends 1D sampling of continuous time signals to signals defined over two or more spatial/temporal dimensions (e.g. continuous 2D image $f(x, y)$ or 3D video $f(x, y, t)$):
* A continuous signal $f_c(\\mathbf{x})$ (where $\\mathbf{x} = [x_1, x_2, \\dots, x_D]^T \\in \\mathbb{R}^D$) is sampled on a discrete spatial **Lattice** $\\Lambda$.
* The discrete signal is:
  $$f[\\mathbf{n}] = f_c(\\mathbf{V} \\mathbf{n}), \\quad \\mathbf{n} = [n_1, n_2, \\dots, n_D]^T \\in \\mathbb{Z}^D$$
  where $\\mathbf{V} = [\\mathbf{v}_1, \\mathbf{v}_2, \\dots, \\mathbf{v}_D]$ is the $D \\times D$ **Sampling Matrix** whose column vectors define the basis of the sampling grid.

---

### 2. Sampling Lattices in 2D Space
1. **Rectangular Lattice (Standard Image Sensors - CCD/CMOS):**
   $$\\mathbf{V} = \\begin{bmatrix} T_1 & 0 \\\\ 0 & T_2 \\end{bmatrix}$$
   Pixels are arranged along orthogonal horizontal and vertical rows with sampling intervals $T_1$ and $T_2$.
2. **Hexagonal Lattice:**
   $$\\mathbf{V} = \\begin{bmatrix} T_1 & T_1 / 2 \\\\ 0 & \\frac{\\sqrt{3}}{2} T_1 \\end{bmatrix}$$
   * Mirrors the photoreceptor mosaic of the human retina.
   * For circularly bandlimited signals, hexagonal sampling requires **$13.4\\%$ fewer samples** than rectangular sampling to reconstruct the signal without aliasing.

---

### 3. Frequency-Domain Representation & The Reciprocal Lattice
Sampling in the spatial domain by matrix $\\mathbf{V}$ results in periodic replication of the continuous Fourier transform $F_c(\\boldsymbol{\\Omega})$ across a **Reciprocal Lattice** defined by matrix $\\mathbf{U}$:
$$\\mathbf{U} = 2\\pi \\mathbf{V}^{-T}, \\quad \\det(\\mathbf{U}) = \\frac{(2\\pi)^D}{|\\det(\\mathbf{V})|}$$
The Fourier transform of the sampled signal is:
$$F_s(\\boldsymbol{\\Omega}) = \\frac{1}{|\\det(\\mathbf{V})|} \\sum_{\\mathbf{k} \\in \\mathbb{Z}^D} F_c\\left(\\boldsymbol{\\Omega} - \\mathbf{U} \\mathbf{k}\\right)$$

---

### 4. Multi-Dimensional Nyquist Criterion & Aliasing
* **Nyquist Condition:** To achieve perfect, distortionless reconstruction, the spectral replicas $F_c(\\boldsymbol{\\Omega} - \\mathbf{U} \\mathbf{k})$ must not overlap in the frequency domain.
* For a 2D rectangular grid with bandlimited signal $|\\omega_x| \\le \\Omega_{x,\\max}$ and $|\\omega_y| \\le \\Omega_{y,\\max}$:
  $$\\omega_{s,x} = \\frac{2\\pi}{T_1} \\ge 2 \\Omega_{x,\\max} \\implies f_{s,x} \\ge 2 f_{\\max,x}$$
  $$\\omega_{s,y} = \\frac{2\\pi}{T_2} \\ge 2 \\Omega_{y,\\max} \\implies f_{s,y} \\ge 2 f_{\\max,y}$$
* **Effects of Aliasing Distortion:**
  * When sampling conditions are violated, high spatial frequencies fold back as low-frequency patterns.
  * In images, this causes **Moiré patterns** (e.g., false wavy stripes on striped shirts or brick walls) and jagged staircase edges (**spatial jaggies**)."""
    },
    {
        "id": "MID2-Q02",
        "mid": "Mid-II",
        "qno": 2,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "Illustrate with a block diagram and justify the transformation process.",
        "punchline": "The transformation process converts correlated spatial pixels into decorrelated frequency coefficients via 2D-DCT, concentrating signal energy into few low-frequency coefficients.",
        "mnemonic": "B-T-Q-E: Block partition, Transform (DCT), Quantize, Encode bitstream",
        "analogy": "Like converting a bulky speech transcript into a bulleted executive summary: The transformation isolates the critical key takeaways (DC and low AC coefficients) and drops filler words.",
        "diagram": """THE COMPLETE TRANSFORMATION PROCESS BLOCK DIAGRAM:

Spatial Image Input f(x, y)
       │
       ▼
┌───────────────────────────────┐
│ 1. 8x8 Block Partitioning     │  Splits image into local spatial blocks
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ 2. 2D-DCT Transformation      │  Decorrelates pixels & compacts energy into DC/AC
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ 3. Quantization Matrix Q(u, v)│  Lossy step: Divides by HVS visibility threshold
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ 4. Zig-Zag Serial Scanning    │  Converts 2D array into 1D sorted by frequency
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ 5. Entropy Encoder (Huffman)  │  Lossless binary compression
└──────────────┬────────────────┘
               │
               ▼
Compressed Output Bitstream""",
        "content": """### 1. Block Diagram of the Transformation Process
The transformation process is the heart of transform-based video and image compression standards (JPEG, MPEG, H.264). It maps spatial pixel blocks into the transform (frequency) domain to decouple statistical correlations and exploit human visual limitations.

---

### 2. Functional Justification of Each Block

#### 1. Block Partitioning (8x8 or 16x16)
* **Justification:** Pixel correlations in natural images are predominantly local (a pixel is highly correlated with its immediate neighbors within an 8-pixel radius, but uncorrelated with pixels 200 units away). Dividing the frame into local $8 \\times 8$ blocks reduces computation from $O(N^2)$ to $O(64 \\times \\text{blocks})$ and adapts to local texture statistics.

#### 2. Forward 2D-DCT Transformation
* **Justification:** Natural images have high mutual covariance between adjacent pixels ($r \\approx 0.95$). Direct quantization of raw pixels is inefficient. 2D-DCT acts as an orthogonal basis projection that **decorrelates** the 64 pixels, concentrating over **$90\\%$ of the total block energy into the top-left DC and first 3 AC coefficients**.

#### 3. Quantization Matrix Application (Lossy Step)
* **Justification:** The human eye cannot detect fine, high-frequency spatial luminance variations. Each DCT coefficient $F(u, v)$ is divided by a psychovisual weight $Q(u, v)$:
  $$F_q(u, v) = \\text{round}\\left( \\frac{F(u, v)}{Q(u, v)} \\right)$$
  Because $Q(u, v)$ increases steeply for high frequencies, most high-frequency coefficients become **exact zeros**, enabling massive data compression without perceptible distortion.

#### 4. Zig-Zag Scanning
* **Justification:** Reorders the 2D $8 \\times 8$ quantized matrix into a 1D sequence in ascending order of spatial frequency. This groups all non-zero low-frequency coefficients at the start and pools all zeros at the end into a single, contiguous zero run terminated by an End-Of-Block (EOB) code.

#### 5. Entropy Coding (Lossless Compression)
* **Justification:** Variable-length coding (Huffman or Arithmetic/CABAC) exploits coding redundancy by allocating short binary bitstrings to highly frequent symbols (like zero-runs) and longer bitstrings to rare values."""
    },
    {
        "id": "MID2-Q03",
        "mid": "Mid-II",
        "qno": 3,
        "unit": "Unit-3",
        "co": "CO3",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Evaluate the influence of human visual system properties such as luminance sensitivity, contrast perception, and color interpretation on image representation and compression techniques.",
        "punchline": "Human vision exhibits high luminance sensitivity but poor color acuity (enabling 4:2:0 subsampling), logarithmic contrast perception (Weber's Law), and bandpass frequency response (CSF justifying heavy high-frequency quantization).",
        "mnemonic": "L-C-C-M: Luminance over Chroma (4:2:0), Contrast Sensitivity (CSF), Color Opponent channels, Masking effects",
        "analogy": "Your eye is like a biological video camera with 120 million black-and-white rod sensors but only 6 million color cones: it notices the sharpest gray borders instantly, but barely notices if colors are blurred or compressed.",
        "diagram": """HUMAN CONTRAST SENSITIVITY FUNCTION (CSF):
  ▲ Sensitivity S(f) = 1 / Threshold
  │          ╭─────────╮
  │        ╭─           ─╮       Peak Sensitivity at 3 - 5 cycles/degree
  │       ╭               ╮
  │      ╭                 ╰╮    High Frequency Drop-off:
  │     ╭                    ╰╮  Eye CANNOT perceive fine spatial detail!
  │    ╭                       ╰──► HEAVY QUANTIZATION ALLOWED HERE
  └────┴───────────┴─────────────┴─────► Spatial Frequency (cycles/degree)
       0           4            30

COLOR OPPONENT MODEL IN HVS:
   Photoreceptors: [ L-Cone (Red) ] [ M-Cone (Green) ] [ S-Cone (Blue) ]
                          │                 │                 │
                          ▼                 ▼                 ▼
   Opponent Channels:  Y = Luminance (L + M) ────────► HIGH BANDWIDTH (Preserve)
                      Cb = Blue - Yellow     ────────► LOW BANDWIDTH  (Compress 4:2:0)
                      Cr = Red - Green       ────────► LOW BANDWIDTH  (Compress 4:2:0)""",
        "content": """### 1. Introduction to the Human Visual System (HVS)
Engineering visual compression algorithms (JPEG, H.264, HEVC) requires understanding the physiological and perceptual characteristics of the ultimate receiver: the human eye and visual cortex. The HVS is non-linear, non-uniform, and discards enormous amounts of physical light energy before transmitting signals to the brain.

---

### 2. Core HVS Properties and Their Direct Impact on Compression

#### 1. Luminance vs. Chrominance Sensitivity
* **Biological Mechanism:** The human retina contains two types of photoreceptors:
  * **Rods ($\\\\approx 120\\text{ million}$):** Highly sensitive to overall light intensity (Luminance $Y$).
  * **Cones ($\\\\approx 6-7\\text{ million}$):** Concentrated in the fovea, sensitive to color wavelengths ($R, G, B$).
* **Perceptual Result:** The human eye has **substantially lower spatial acuity for color changes** than for brightness variations. We can distinguish tiny grayscale edge shifts that would be completely invisible if made in color hue.
* **Impact on Compression:**
  * RGB color space is converted into opponent color space **YCbCr** (Luminance $Y$, Blue-chroma $Cb$, Red-chroma $Cr$).
  * **Chroma Subsampling (4:2:0):** The color planes $Cb$ and $Cr$ are downsampled by a factor of 2 horizontally and vertically, discarding **$50\\%$ of total pixel data** immediately with zero perceptible subjective degradation.

#### 2. Contrast Perception & Weber-Fechner Law
* **Biological Mechanism:** Human brightness perception is relative, not absolute.
* **Weber\\'s Law:** The just-noticeable difference in luminance $\\Delta I$ is proportional to the background luminance $I$:
  $$\\frac{\\Delta I}{I} = \\text{constant} \\approx 0.01-0.02$$
* **Impact on Compression:**
  * Human perception follows a logarithmic response to light intensity.
  * In dark regions, the eye is sensitive to small absolute changes; in bright regions, large variations go unnoticed.
  * Justifies non-linear **Gamma Correction** ($V = I^\\gamma$, with $\\gamma \\approx 2.2$) in display encoding and adaptive quantization in video encoders.

#### 3. Contrast Sensitivity Function (CSF)
* **Biological Mechanism:** The eye\\'s sensitivity to sinusoidal spatial gratings varies with spatial frequency ($f$ in cycles per degree of visual angle).
* **Characteristics:**
  * CSF is a bandpass curve peaking between **$3$ and $5\\text{ cycles/degree}$**.
  * Below 1 cycle/degree, sensitivity decreases due to lateral retinal inhibition.
  * **Above 10 cycles/degree, sensitivity drops off sharply** toward zero.
* **Impact on Compression:**
  * Forms the direct mathematical basis for the **JPEG/MPEG Quantization Matrix $Q(u, v)$**.
  * Low-frequency DCT coefficients (near peak CSF) are assigned small divisor values (high precision).
  * High-frequency DCT coefficients (where CSF drops to near zero) are assigned large divisor values (heavily quantized or discarded).

#### 4. Spatial and Temporal Masking
* **Spatial Masking:** High-contrast edges or busy textures (like foliage or grass) mask noise in neighboring pixels. The encoder can apply coarse quantization in textured areas without visible artifacts.
* **Temporal Masking:** Rapid scene cuts or fast-moving action temporarily blind the human eye to fine details for $100-200\\text{ ms}$. Video encoders save bitrate by encoding the frame immediately following a scene transition with lower resolution."""
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
        "punchline": "A comprehensive digital video system integrates progressive sampling lattices, YCbCr 4:2:0 subsampling, hierarchical GOP frame structures (I, P, B frames), and block motion compensation to achieve 100:1 video compression.",
        "mnemonic": "S-C-G-M: Sampling (Progressive), Color (YCbCr 4:2:0), GOP structure (I/P/B), Motion compensation",
        "analogy": "A flip-book cartoon: Instead of drawing every single character and tree in full detail on every page, you draw the background once (I-frame) and just write small sticky notes describing how the character moves on subsequent pages (P/B frames).",
        "diagram": """DIGITAL VIDEO REPRESENTATION & COMPRESSION ARCHITECTURE:

1. COLOR & SPATIAL SAMPLING:
   Input Video ──► [ YCbCr 4:2:0 Subsampling ] ──► Cuts raw bitrate by 50%

2. TEMPORAL GOP (Group of Pictures) STRUCTURE:
       Forward Prediction
     ┌───────────────────────┐
     │                       ▼
   ┌───┐       ┌───┐       ┌───┐       ┌───┐       ┌───┐
   │ I │◄─────►│ B │◄─────►│ P │◄─────►│ B │◄─────►│ I │  ...
   └───┘       └───┘       └───┘       └───┘       └───┘
     ▲                       ▲
     └───────────────────────┘
       Bidirectional Prediction

3. TEMPORAL REDUNDANCY REDUCTION (Motion Compensation):
   Target Block Frame(t) ──► [ Block Matching Search ] ──► Motion Vector (dx, dy)
                                    │
                                    ▼
                          [ Subtract Reference ]
                                    │
                                    ▼
                         Residual Error e[x, y]  (Near Zero Energy!)
                                    │
                                    ▼
                           [ 2D-DCT + Quant ] ──► Compressed Bitstream""",
        "content": """### 1. Architectural System Design
A digital video system represents continuous 3D spatio-temporal light $f(x, y, t)$ as a compressed, streamable digital bitstream. The design integrates three interconnected subsystems:
1. **Sampling Lattice & Frame Scanning Architecture**
2. **Color Representation & Spatial Redundancy Elimination**
3. **Temporal Redundancy Reduction & Group of Pictures (GOP) Structure**

---

### 2. Subsystem 1: Sampling Theory & Frame Structure

#### 1. Progressive vs. Interlaced Scanning
* **Interlaced Scanning (Legacy NTSC/PAL):** Splits each frame into two alternating odd/even fields (lines 1, 3, 5... and 2, 4, 6...). Causes severe comb artifacts and motion blur on modern LCD/OLED displays.
* **Progressive Scanning (Modern Standard - 1080p, 4K):** Captures and displays all scan lines sequentially in a single pass.
* **Justification:** Eliminates motion interlacing artifacts, simplifies block motion estimation algorithms, and delivers pristine visual sharpness.

#### 2. Frame Rate Selection
* **24 fps:** Cinematic motion standard (natural motion blur).
* **30 / 60 fps:** Broadcast television and smooth sports / action tracking.
* **120 fps:** Gaming and virtual reality (VR) to eliminate simulator sickness.

---

### 3. Subsystem 2: Color Space & Spatial Chroma Subsampling
* Raw sensor RGB data is transformed into **YCbCr** to decouple luminance $Y$ from chrominance $Cb, Cr$.
* **Chroma Subsampling Format Justification:**
  * **4:4:4:** Full fidelity (used only in medical imaging and VFX). Bitrate = $24\\text{ bits/pixel}$.
  * **4:2:2:** Horizontal color subsampling. Bitrate = $16\\text{ bits/pixel}$.
  * **4:2:0 (Selected Design):** Subsampled by a factor of 2 both horizontally and vertically. Four luminance pixels share a single pair of $(Cb, Cr)$ chroma samples.
  * **Bitrate Reduction:**
    $$\\text{Effective Bits per Pixel} = 8 + \\frac{8}{4} + \\frac{8}{4} = 12\\text{ bpp (a 50% immediate saving)}$$
    Because human vision has very low color acuity, visual quality remains indistinguishable from 4:4:4.

---

### 4. Subsystem 3: Temporal Redundancy Reduction (Motion Compensation)
In a 30 fps video stream, consecutive frames are separated by only $33\\text{ ms}$. Background landscapes and objects remain virtually identical, displaced only by small camera or object movements (**temporal redundancy**).

#### 1. Group of Pictures (GOP) Frame Structure
Video frames are classified into three functional types within a recurring GOP (e.g., $N = 12$ or $16$ frames):
1. **I-Frames (Intra-coded Frames):**
   * Encoded independently using still-image compression (like JPEG) without reference to any past or future frame.
   * Provide random access entry points for channel switching, seeking, and recovery from transmission bit-errors.
2. **P-Frames (Predicted Frames):**
   * Encoded via forward motion compensation from the previous I or P reference frame.
   * Transmits only **Motion Vectors** and small **Residual Errors**, requiring only $\\\\approx 20-30\\%$ the bits of an I-frame.
3. **B-Frames (Bi-directionally Predicted Frames):**
   * Predicted from both a past reference frame and a future reference frame (interpolated prediction).
   * Highest compression ratio (requires only $\\\\approx 5-10\\%$ of I-frame bitrate) and handles covered/uncovered background regions seamlessly.

#### 2. Motion Estimation & Compensation Pipeline
1. For each macroblock in the current target frame $t$, search within a window in reference frame $t-1$ for the best matching block using Minimum Sum of Absolute Differences (SAD).
2. Compute the displacement: $\\vec{d} = (\\Delta x, \\Delta y)$ (**Motion Vector**).
3. Compute the prediction residual:
   $$e[x, y] = I_t(x, y) - I_{t-1}(x + \\Delta x, y + \\Delta y)$$
4. Transform and quantize only the residual $e[x, y]$ using 2D-DCT. Because $e[x, y]$ is near zero across most pixels, the resulting DCT coefficients are overwhelmingly zero, achieving over **$100:1$ total video compression**."""
    }
]
