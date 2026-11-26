# -*- coding: utf-8 -*-
"""
High-Yield Key Points (Shortest Essentials) for all 40 SVP Questions.
Ultra-concise bullet points designed for 60-second revision before entering the exam hall.
"""

KEYPOINTS_DATA = {
    # --- UNIT 1 (Mid-I Q1-Q8) ---
    'MID1-Q01': [
        "**Source-Filter Model:** Speech output is $S(z) = E(z) \\cdot H(z) \\cdot R(z)$ where $E(z)$ is glottal source, $H(z)$ is vocal tract filter, and $R(z) \\approx 1 - z^{-1}$ is lip radiation.",
        "**Excitation Source Roles:** Lungs generate airflow; glottis modulates voiced periodic pitch pulses ($F_0$), unvoiced turbulent noise (fricatives /s/), or transient bursts (plosives /p/).",
        "**Vocal Tract Roles:** Acoustic resonator tube of length $\\approx 17.5\\text{ cm}$ whose physical shape creates resonant frequencies called **Formants** ($F_1, F_2, F_3$) that identify phonemes.",
        "**Articulators:** Tongue position, jaw height, velum (nasal coupling), and lip rounding continuously alter formant positions."
    ],
    'MID1-Q02': [
        "**Discrete Representation:** Continuous speech $s(t)$ is sampled at discrete time intervals $T_s = 1/f_s$ to yield discrete sequence $s[n] = s(n T_s)$.",
        "**Standard Sampling Rates:** 8 kHz for PSTN telephone speech (captures up to 3.4 kHz); 16 kHz for modern ASR engines like Whisper/Siri (captures up to 8 kHz).",
        "**Nyquist Criterion:** $f_s \\ge 2 f_{\\max}$. If violated, high-frequency energy folds over into low frequencies as irreversible **Aliasing Distortion**.",
        "**Reconstruction:** Analog anti-aliasing low-pass filter must precede ADC; ideal continuous reconstruction is achieved via **Sinc Interpolation**."
    ],
    'MID1-Q03': [
        "**System Formulation:** Given $H(z) = \\frac{1 - 0.5z^{-1}}{1 - 0.9z^{-1} + 0.2z^{-2}} = \\frac{z(z - 0.5)}{(z - 0.5)(z - 0.4)}$.",
        "**Zeros Calculation:** Set numerator $N(z) = 0 \\implies z(z - 0.5) = 0 \\implies z_1 = 0, z_2 = 0.5$.",
        "**Poles Calculation:** Set denominator $D(z) = 0 \\implies (z - 0.5)(z - 0.4) = 0 \\implies p_1 = 0.5, p_2 = 0.4$.",
        "**BIBO Stability Comment:** A causal LTI system is unconditionally BIBO stable if all poles lie strictly inside the unit circle ($|p_k| < 1$). Since $|0.5| < 1$ and $|0.4| < 1$, the system is **Unconditionally Stable**."
    ],
    'MID1-Q04': [
        "**Computational Speedup:** FFT computes the $N$-point DFT in $O(N \\log_2 N)$ complex operations instead of direct DFT's $O(N^2)$ (over 100x faster for $N=512$).",
        "**Hermitian Symmetry:** For real speech $x[n]$, $X[N-k] = X^*[k]$. Only $\\frac{N}{2} + 1$ frequency bins (DC to Nyquist) need to be stored or processed.",
        "**Magnitude Invariance:** Time shifts $x[n - n_0]$ alter only spectral phase, leaving the phonetic magnitude spectrum $|X[k]|$ unchanged.",
        "**Parseval's Theorem:** Frame energy in time domain equals energy in frequency domain; used for Voice Activity Detection (VAD).",
        "**Periodicity & Windowing:** Rectangular truncation causes spectral leakage; windowing (Hamming) smooths boundaries before FFT."
    ],
    'MID1-Q05': [
        "**Discrete Convolution:** $y[n] = x[n] * h[n] = \\sum_{k=-\\infty}^\\infty x[k] h[n-k]$, executed via Flip, Shift, Multiply, and Sum.",
        "**Source-Filter Speech Convolution:** Speech output is glottal pulse $e[n]$ convolved with vocal tract impulse response $v[n]$ and radiation $r[n]$: $s[n] = e[n] * v[n] * r[n]$.",
        "**Convolution Theorem:** Time-domain convolution equals frequency-domain point-wise multiplication: $\\mathcal{F}\\{x[n] * h[n]\\} = X(\\omega) \\cdot H(\\omega)$.",
        "**Streaming Fast Convolution:** Computed via FFT using **Overlap-Add (OLA)** or **Overlap-Save (OLS)** to filter continuous speech without infinite latency."
    ],
    'MID1-Q06': [
        "**Linear Filter Banks:** Constant bandwidth and uniform spacing across all frequencies; implemented via uniform STFT; poor resolution at low frequencies (<1 kHz).",
        "**Non-Linear Mel Filter Banks:** Narrow linear bandwidth below 1 kHz ($\\\\Delta f \\approx 100\\text{ Hz}$); exponentially widening logarithmic bandwidth above 1 kHz.",
        "**Cochlear Tonotopy:** Human auditory system resolves frequencies along the Mel scale: $\\text{Mel}(f) = 2595 \\log_{10}(1 + f/700)$.",
        "**Acoustic Trade-off:** Linear filter banks preserve exact phase for audio resynthesis; Mel filter banks discard redundant phase and compact 256 FFT bins into 26-40 robust acoustic features."
    ],
    'MID1-Q07': [
        "**Part A (4-Point DFT):** For speech frame $x[n] = [2, 1, 0, 1]$, multiplying by $W_4$ matrix yields $X[0] = 4, X[1] = 2, X[2] = 0, X[3] = 2$.",
        "**Magnitude Spectrum:** $|X[0]| = 4.0$ (DC level); Dominant AC components are bins $k=1$ and $k=3$ with magnitude $|X[1]| = |X[3]| = 2.0$.",
        "**Part B (Frequency Resolution):** $\\Delta f = \\frac{f_s}{N} = \\frac{8000\\text{ Hz}}{256} = \\mathbf{31.25\\text{ Hz/bin}}$.",
        "**Bin Frequency ($k=10$):** $f_{10} = k \\cdot \\Delta f = 10 \\times 31.25\\text{ Hz} = \\mathbf{312.5\\text{ Hz}}$ (corresponds to female/child pitch or closed vowel $F_1$ formant)."
    ],
    'MID1-Q08': [
        "**All-Pole Model:** $H(z) = \\frac{G}{1 - \\sum_{k=1}^p a_k z^{-k}}$; current sample is predicted from past $p$ samples: $\\hat{s}[n] = \\sum_{k=1}^p a_k s[n-k]$.",
        "**MSE Minimization:** Minimizing total squared residual $E = \\sum e^2[n]$ yields the **Yule-Walker Normal Equations**: $\\sum_{k=1}^p a_k R(|i - k|) = R(i)$.",
        "**Toeplitz Matrix:** Autocorrelation matrix has identical diagonals, allowing solution in $O(p^2)$ operations via the **Levinson-Durbin Algorithm**.",
        "**Massive Compression:** Compresses 64 kbps PCM speech into 2.4 kbps (LPC-10), separating vocal tract formants from glottal pitch."
    ],

    # --- UNIT 2 (Mid-I Q9-Q16) ---
    'MID1-Q09': [
        "**Pre-emphasis ($1 - 0.97z^{-1}$):** Boosts high-frequency formants by compensating for the $-6\\text{ dB/octave}$ glottal spectral tilt.",
        "**Framing & Windowing:** Splits continuous audio into $20-30\\text{ ms}$ quasi-stationary frames; Hamming window prevents spectral leakage.",
        "**Mel Filter Bank:** 26 to 40 overlapping triangular bandpass filters spaced according to human cochlear critical bands.",
        "**Logarithm & DCT-II:** Logarithm compresses perceptual loudness; DCT-II decorrelates filter bank energies into 13 compact MFCCs."
    ],
    'MID1-Q10': [
        "**Static Features (13-D):** $c_0$ to $c_{12}$ MFCCs represent instantaneous vocal tract articulatory posture at single frame $t$.",
        "**Delta / Velocity Features (13-D):** $\\Delta c_t$ measures first-order temporal derivative (speed of spectral change) using linear regression.",
        "**Delta-Delta / Acceleration (13-D):** $\\Delta^2 c_t$ measures second-order temporal derivative (articulatory muscle acceleration).",
        "**Standard 39-D Vector:** Combining $[c_t \\mid \\Delta c_t \\mid \\Delta^2 c_t]$ captures co-articulation and transitional phonemes, boosting ASR accuracy."
    ],
    'MID1-Q11': [
        "**Given Parameters:** Total samples $L = 1600$, window size $N = 400$, overlap $M = 200$.",
        "**Hop Size ($R$):** $R = N - M = 400 - 200 = 200\\text{ samples}$ (50% overlap).",
        "**Framing Equation:** $K = \\lfloor\\frac{L - N}{R}\\rfloor + 1 = \\lfloor\\frac{1600 - 400}{200}\\rfloor + 1 = \\lfloor\\frac{1200}{200}\\rfloor + 1 = 6 + 1 = \\mathbf{7\\text{ frames}}$.",
        "**Boundary Verification:** Frame 1 (0 to 399) through Frame 7 (1200 to 1599) perfectly covers all 1600 samples."
    ],
    'MID1-Q12': [
        "**Theoretical Model:** LPCC is based on an all-pole linear acoustic tube; MFCC is based on human auditory cochlear perception.",
        "**Noise Robustness:** LPCC degrades severely under environmental noise and unvoiced consonants; MFCC is highly robust due to wide filter averaging.",
        "**Zeros / Anti-resonances:** LPCC cannot model nasal dips (/m/, /n/); MFCC captures arbitrary spectral shapes.",
        "**Industry Standard:** MFCC is universal standard for ASR and speaker ID; LPCC is restricted to low-bitrate military/telephony vocoders."
    ],
    'MID1-Q13': [
        "**Euclidean Distance:** $d(x, y) = \\sqrt{\\sum (x_i - y_i)^2}$; assumes features are uncorrelated with equal variance; dominated by low-order MFCCs.",
        "**Mahalanobis Distance:** $d_M = \\sqrt{(x - y)^T \\Sigma^{-1} (x - y)}$; normalizes features by inverse covariance matrix, achieving scale invariance.",
        "**Dynamic Time Warping (DTW):** Aligns variable-length speech sequences ($N \\ne M$) via dynamic programming grid $D(i, j)$ using local distance and slope constraints.",
        "**DTW Constraints:** Boundary conditions, monotonicity (time cannot flow backwards), continuity, and Sakoe-Chiba search bands."
    ],
    'MID1-Q14': [
        "**Vector Quantization (VQ):** Maps continuous high-dimensional vectors to a finite codebook $C = \\{y_1, \\dots, y_K\\}$ partitioned into Voronoi cells.",
        "**Linde-Buzo-Gray (LBG) Algorithm:** Iteratively generates codebooks by computing global centroid, splitting each centroid by $\\pm \\epsilon$, and running K-means clustering.",
        "**Codebook Sizing:** $K = 64$ to $128$ balances quantization distortion against memory and search latency.",
        "**Tree-Structured VQ (TSVQ):** Replaces linear $O(K)$ search with binary tree search in $O(\\log_2 K)$."
    ],
    'MID1-Q15': [
        "**GMM Formulation:** $p(x | \\lambda) = \\sum_{m=1}^M w_m \\mathcal{N}(x; \\mu_m, \\Sigma_m)$ with $\\sum w_m = 1$; diagonal covariance matrices used in ASR.",
        "**Expectation-Maximization (EM):** Solves intractable maximum likelihood estimation iteratively.",
        "**E-Step (Expectation):** Computes posterior component responsibilities $\\gamma_m(x_t)$ for each training vector.",
        "**M-Step (Maximization):** Updates mixture weights $\\hat{w}_m$, mean vectors $\\hat{\\mu}_m$, and covariance matrices $\\hat{\\Sigma}_m$.",
        "**Variance Flooring:** Enforces a minimum variance threshold to prevent singular probability spikes."
    ],
    'MID1-Q16': [
        "**HMM Architecture:** Doubly stochastic model $\\lambda = (A, B, \\pi)$ with hidden articulatory states and observable acoustic feature emissions.",
        "**Bakis Left-to-Right Topology:** States only loop to self ($a_{ii}$) or transition forward ($a_{i, i+1}$), mirroring the forward march of time.",
        "**Problem 1 (Evaluation):** Solved via **Forward Algorithm** in $O(N^2 T)$ operations.",
        "**Problem 2 (Decoding):** Solved via **Viterbi Algorithm** (dynamic programming) to find optimal hidden state sequence $Q^*$.",
        "**Problem 3 (Training):** Solved via **Baum-Welch Algorithm** (EM recursion) to estimate model parameters.",
        "**Temporal Flexibility:** State self-loops $a_{ii}$ absorb speaking rate variations naturally (expected duration $\\bar{d}_i = \\frac{1}{1 - a_{ii}}$)."
    ],

    # --- UNIT 3 (Mid-I Q17-Q20 & Mid-II Q1-Q4) ---
    'MID1-Q17': [
        "**Taxonomy:** 2D signals (images $f(x, y)$), 3D signals (video $f(x, y, t)$ or volumetric CT $f(x, y, z)$), 4D signals (dynamic MRI).",
        "**Spatial Correlation:** Neighboring pixels exhibit $>90\\%$ mutual statistical correlation; video frames exhibit massive temporal redundancy.",
        "**Non-Causality:** Unlike 1D time signals, spatial dimensions exist simultaneously in all directions, permitting zero-phase symmetric 2D filtering.",
        "**Massive Bandwidth:** Uncompressed Full HD video requires $>3.0\\text{ Gbps}$, necessitating aggressive transform-domain compression."
    ],
    'MID1-Q18': [
        "**2D-DFT Formulation:** $F(u, v) = \\sum_x \\sum_y f(x, y) e^{-j 2\\pi (ux/M + vy/N)}$; kernel is fully separable.",
        "**Row-Column Algorithm:** Computed by applying 1D-FFT to all rows, then 1D-FFT to all columns in $O(MN \\log_2(MN))$ ops.",
        "**DC Component:** Centered $F(0, 0)$ represents total spatial sum, directly proportional to average image brightness.",
        "**Edge Orthogonality:** Horizontal frequency axis ($u$) corresponds to vertical spatial edges; vertical frequency axis ($v$) corresponds to horizontal spatial edges."
    ],
    'MID1-Q19': [
        "**2D LSI Systems:** Characterized by 2D unit impulse response / Point Spread Function $h[m, n]$.",
        "**2D Spatial Convolution:** $y[m, n] = x[m, n] ** h[m, n] = \\sum_k \\sum_l x[k, l] h[m-k, n-l]$.",
        "**Transform Domain Equivalence:** Convolution in space corresponds to matrix multiplication in frequency domain: $Y(z_1, z_2) = X(z_1, z_2) \\cdot H(z_1, z_2)$.",
        "**Separable 2D Filters:** If $h[m, n] = h_1[m] \\cdot h_2[n]$, complexity drops from $O(K^2)$ to $O(2K)$ operations per pixel."
    ],
    'MID1-Q20': [
        "**Compression Pipeline:** Color Conversion (RGB to YCbCr) -> 4:2:0 Chroma Subsampling -> 8x8 Block Partition -> 2D-DCT -> Quantization -> Zig-zag -> Entropy Coding.",
        "**Why 2D-DCT over 2D-DFT:** DCT enforces even-symmetric boundary reflection (eliminates blocking artifacts and spectral leakage), packs $>90\\%$ energy into 3-5 coefficients, and uses purely real arithmetic.",
        "**Quantization:** Lossy step dividing DCT coefficients by HVS visibility threshold matrix $Q(u, v)$, driving high frequencies to zero.",
        "**Performance:** Delivers 10:1 to 25:1 visually lossless image compression, and 50:1 to 100:1 video compression."
    ],
    'MID2-Q01': [
        "**Sampling Lattices:** Discrete grid generated by sampling matrix $\\mathbf{V}$: $\\mathbf{x} = \\mathbf{V} \\mathbf{n}$.",
        "**Rectangular vs Hexagonal:** Hexagonal lattice packs circular bandlimited signals tighter, saving **13.4% samples** over rectangular grids.",
        "**Reciprocal Lattice:** Frequency domain spectral replication occurs on reciprocal matrix $\\mathbf{U} = 2\\pi \\mathbf{V}^{-T}$.",
        "**2D Nyquist Criterion:** $f_{sx} \\ge 2 f_{\\max,x}$ and $f_{sy} \\ge 2 f_{\\max,y}$. Undersampling causes overlapping spectral replicas, manifesting as **Moiré patterns** and spatial jaggies."
    ],
    'MID2-Q02': [
        "**Block Partitioning (8x8):** Exploits localized spatial correlation and reduces computation from global $O(N^2)$ to block-level parallel processing.",
        "**2D-DCT Transformation:** Orthogonally decorrelates the 64 spatial pixels and concentrates almost all block energy into the top-left DC and first 3 AC coefficients.",
        "**Quantization Matrix:** Divides coefficients by human visual contrast thresholds, converting imperceptible fine textures into exact zeros.",
        "**Zig-Zag & Entropy Coding:** Reorders matrix by increasing frequency into a 1D vector to produce long trailing zero-runs encoded via Huffman/CABAC."
    ],
    'MID2-Q03': [
        "**Luminance vs Chroma:** Human retina has 120M rods (brightness) and only 6M cones (color); justifies YCbCr 4:2:0 subsampling that discards 50% data without visible loss.",
        "**Contrast Sensitivity Function (CSF):** Bandpass response peaking at 3-5 cycles/degree and falling steeply to zero at high frequencies, justifying heavy high-frequency DCT quantization.",
        "**Weber-Fechner Law:** Perception of light intensity is logarithmic; relative contrast $\\Delta I / I \\approx \\text{const}$, governing gamma correction and adaptive quantization.",
        "**Spatial & Temporal Masking:** Busy textured backgrounds mask visual noise; rapid scene transitions temporarily blind human vision, allowing higher compression."
    ],
    'MID2-Q04': [
        "**Progressive Scanning:** Scans all lines sequentially in a single frame; eliminates motion comb artifacts common in interlaced video.",
        "**Color Subsampling (YCbCr 4:2:0):** 4 luminance pixels share 1 pair of chroma samples, cutting uncompressed data from 24 bpp to 12 bpp.",
        "**Group of Pictures (GOP):** Recurring sequence of I-frames (intra-coded anchors), P-frames (forward motion predicted), and B-frames (bi-directional motion predicted).",
        "**Motion Compensation:** Replaces full frames with motion vectors $\\vec{d} = (d_x, d_y)$ and near-zero prediction residuals, achieving 100:1 compression."
    ],

    # --- UNIT 4 (Mid-II Q5-Q12) ---
    'MID2-Q05': [
        "**Geometric Model:** Pinhole perspective projection ($x = f X/Z, y = f Y/Z$); distant objects appear smaller; establishes motion parallax (speed inversely proportional to depth $Z$).",
        "**Photometric Model:** Image irradiance $I(x, y) = L(x, y) \\cdot R(x, y)$ (Illumination $\\times$ Reflectance); explains when brightness constancy fails (shadows, lighting flickers).",
        "**Camera Parameters:** Extrinsics ($[R \\mid \\mathbf{t}]$) define 3D camera pose; Intrinsics ($K$) define focal length and lens distortion.",
        "**Role in Motion:** Enables motion estimation algorithms to separate true geometric 3D object motion from lighting fluctuations and camera egomotion."
    ],
    'MID2-Q06': [
        "**Translational Model (2 DOF):** $\\mathbf{x}' = \\mathbf{x} + \\mathbf{d}$; rigid shift; standard in block matching algorithms.",
        "**Affine Model (6 DOF):** $\\mathbf{x}' = \\mathbf{A} \\mathbf{x} + \\mathbf{d}$; captures translation, rotation, zoom/scale, and shear; preserves parallel lines.",
        "**Projective / Homography (8 DOF):** 8 parameters modeling full perspective distortion of rigid 3D planar surfaces.",
        "**Core Assumptions:** Brightness Constancy ($I(t+dt) = I(t)$), Small Motion (permits Taylor expansion), and Spatial Coherence (neighboring pixels move together)."
    ],
    'MID2-Q07': [
        "**Given Coordinates:** Frame 1 at $(x_1, y_1) = (20, 25)$; Frame 2 best match at $(x_2, y_2) = (23, 30)$.",
        "**Motion Vector:** $\\Delta x = 23 - 20 = +3\\text{ px}$, $\\Delta y = 30 - 25 = +5\\text{ px} \\implies \\vec{d} = (\\mathbf{3, 5})$.",
        "**Magnitude:** $|\\vec{d}| = \\sqrt{3^2 + 5^2} = \\sqrt{9 + 25} = \\sqrt{34} \\approx \\mathbf{5.83\\text{ pixels}}$.",
        "**Direction:** $\\theta = \\arctan(5/3) \\approx \\mathbf{59.04^\\circ}$; motion is directed **3 px Rightward and 5 px Downward** in image coordinates."
    ],
    'MID2-Q08': [
        "**Optical Flow Equation:** $I_x u + I_y v + I_t = 0$; derived from first-order Taylor expansion under brightness constancy.",
        "**Aperture Problem:** 1 linear equation with 2 unknowns ($u, v$); only motion perpendicular to image edges (normal flow) can be directly measured.",
        "**Lucas-Kanade:** Assumes constant flow in local $3 \\times 3$ window; solves overdetermined least squares $(A^T A)^{-1} A^T b$ at textured corners.",
        "**Horn-Schunck:** Global variational formulation adding a spatial smoothness regularizer; produces dense optical flow via iterative Gauss-Seidel updates.",
        "**Sensitivity:** Gradient operators amplify noise; lighting shifts violate brightness constancy; large motion requires Gaussian pyramids."
    ],
    'MID2-Q09': [
        "**Matching Criteria:** Sum of Absolute Differences (SAD) is computationally fastest (integer operations only); MSE requires costly multiplications.",
        "**Full Search (FS):** Tests all $(2p+1)^2$ candidate points in search window; optimal minimum distortion but massive computation ($225$ points for $p=7$).",
        "**Three-Step Search (TSS):** Checks 8 points at step 4, then step 2, then step 1; evaluates only **25 points (9x faster than FS)** with minimal loss.",
        "**Diamond Search:** Evaluates 15-20 points adaptively using large/small diamond patterns; state-of-the-art fast BMA in modern video encoders."
    ],
    'MID2-Q10': [
        "**Formulation:** Minimizes non-linear sum-of-squared residuals $\\min_{\\mathbf{p}} \\frac{1}{2} \\|\\mathbf{r}(\\mathbf{p})\\|^2$ for affine/homography models.",
        "**Gradient Descent:** First-order linear convergence; reliable globally but suffers from catastrophic slow zigzagging in narrow error valleys.",
        "**Gauss-Newton:** Second-order quadratic convergence near minimum via Hessian approximation $\\mathbf{H} \\approx \\mathbf{J}^T \\mathbf{J}$; unstable if Hessian is ill-conditioned.",
        "**Levenberg-Marquardt (LM):** Adaptively damps Hessian with $\\lambda \\mathbf{I}$; automatically shifts between Gradient Descent (far from minimum) and Gauss-Newton (near minimum).",
        "**Gaussian Pyramids:** Multi-resolution coarse-to-fine pyramids overcome local minima and handle large displacements."
    ],
    'MID2-Q11': [
        "**Fourier Shift Theorem:** Translation $(x_0, y_0)$ in space creates pure linear phase rotation in frequency domain: $F_2(u, v) = F_1(u, v) e^{-j 2\\pi (ux_0 + vy_0)}$.",
        "**Normalized Cross-Power Spectrum:** $R(u, v) = \\frac{F_1 \\cdot F_2^*}{|F_1 \\cdot F_2^*|} = e^{j 2\\pi (ux_0 + vy_0)}$; strips away all image magnitude and lighting bias.",
        "**Dirac Delta Peak:** Inverse 2D-FFT of $R(u, v)$ yields an impulse spike $\\delta(x + x_0, y + y_0)$ whose coordinate peak gives exact displacement.",
        "**Advantages:** Immune to uniform illumination changes; sub-pixel accuracy via parabolic peak interpolation; executed efficiently via 2D-FFT hardware."
    ],
    'MID2-Q12': [
        "**Epipolar Geometry:** Relates two camera views through Epipolar Plane, Epipoles, and Epipolar Lines.",
        "**Essential Matrix:** $\\mathbf{E} = [\\mathbf{t}]_\\times \\mathbf{R}$ (5 DOF); satisfies calibrated coplanarity constraint $\\mathbf{x}_2^T \\mathbf{E} \\mathbf{x}_1 = 0$.",
        "**Eight-Point SVD Algorithm:** Solves for $\\mathbf{E}$ from 8 point correspondences; enforces singular values $(\\sigma, \\sigma, 0)$ via SVD projection.",
        "**RANSAC:** Iteratively tests minimal 8-point subsets to eliminate false feature matches (outliers).",
        "**SfM Pipeline:** Features (SIFT) -> RANSAC -> Essential Matrix -> Pose Recovery $(R, \\mathbf{t})$ -> Triangulation -> Bundle Adjustment (Levenberg-Marquardt)."
    ],

    # --- UNIT 5 (Mid-II Q13-Q20) ---
    'MID2-Q13': [
        "**Segmentation Definition:** Partitions image into disjoint, complete, internally homogeneous, and externally distinct regions: $\\bigcup R_i = I, R_i \\cap R_j = \\emptyset$.",
        "**Region-Based:** Groups pixels by similarity. **Region Growing** expands from seeds based on intensity threshold; **Split-and-Merge** uses quadtree variance decomposition.",
        "**Boundary-Based:** Detects intensity discontinuities. **Gradient Operators** (Sobel, Canny) locate edges; **Active Contours (Snakes)** deform an elastic spline curve to minimize internal and external edge energies.",
        "**Key Contrast:** Region methods guarantee closed regions; boundary methods produce thin edge segments that often require linking."
    ],
    'MID2-Q14': [
        "**Temporal Differencing:** Subtracts adjacent frames ($|I_t - I_{t-1}| > T$); fast and adaptive, but leaves hollow \"ghost\" holes inside uniformly colored moving objects.",
        "**Background Subtraction:** Subtracts current frame from static background model ($|I_t - B_t| > T$); detects entire solid moving silhouette.",
        "**Running Average:** $B_{t+1} = \\alpha I_t + (1 - \\alpha) B_t$; slowly absorbs ambient lighting changes.",
        "**Mixture of Gaussians (MoG):** Models each pixel as 3-5 adaptive Gaussians; handles multi-modal dynamic clutter (swaying trees, water ripples, flickering monitors).",
        "**Shadow Suppression:** Evaluates HSV/YCbCr color space; shadows reduce luminance ($V$) without altering hue ($H$) or saturation ($S$)."
    ],
    'MID2-Q15': [
        "**Given Differences:** $\\text{SAD}_A = 120$, $\\text{SAD}_B = 45$, $\\text{SAD}_C = 200$, Threshold $T = 100$.",
        "**Motion Rule:** $\\text{SAD} > T \\implies$ Motion Detected; $\\text{SAD} \\le T \\implies$ Static Background.",
        "**Motion Identification:** Region A ($120 > 100$) and Region C ($200 > 100$) exhibit motion; Region B ($45 \\le 100$) has no motion.",
        "**Dominant Motion Region:** $\\max(120, 45, 200) = 200 \\implies$ **Region C is the Dominant Motion Region** (highest frame difference activity)."
    ],
    'MID2-Q16': [
        "**Point Tracking:** Tracks object centroids using **Kalman Filters** (linear Gaussian predict-update) or **Particle Filters** (non-linear multi-hypothesis sampling).",
        "**Kernel / Appearance Tracking (Mean-Shift):** Uses color histogram appearance models; iteratively computes Mean-Shift vector $\\mathbf{m}(\\mathbf{y})$ to climb probability gradients to the target mode.",
        "**CamShift:** Continuously Adaptive Mean Shift; dynamically scales and re-orients the bounding box as objects approach or recede.",
        "**Trajectory Extraction:** Connects sequence of centroids $\\{(x_t, y_t)\\}$ to compute velocity, acceleration, and predict future path collisions."
    ],
    'MID2-Q17': [
        "**Matting Equation:** $\\mathbf{I} = \\alpha \\mathbf{F} + (1 - \\alpha) \\mathbf{B}$; 3 color equations vs 7 unknowns (severely under-constrained).",
        "**Alpha Matte ($\\alpha$):** Continuous fractional opacity $\\alpha \\in [0, 1]$; critical for semi-transparent hair, fur, smoke, and motion blur.",
        "**User Trimap:** Partitions image into Known Foreground ($\\alpha = 1$), Known Background ($\\alpha = 0$), and Unknown Transition Band ($0 < \\alpha < 1$).",
        "**Levin's Closed-Form Matting:** Derives Matting Laplacian matrix $\\mathbf{L}$ assuming local color linearity; solves sparse linear system $(\\mathbf{L} + \\lambda \\mathbf{D}) \\boldsymbol{\\alpha} = \\lambda \\mathbf{b}$.",
        "**Video Matting:** Enforces temporal coherence across optical flow trajectories to eliminate inter-frame alpha matte flickering."
    ],
    'MID2-Q18': [
        "**Part A (Particle Normalization):** Given weights $W = [0.2, 0.3, 0.1, 0.4]$; sum $S = 0.2 + 0.3 + 0.1 + 0.4 = 1.0$.",
        "**Normalized Weights:** $\\tilde{W} = [0.20, 0.30, 0.10, 0.40]$; **Particle 4 is Most Likely** with highest probability weight $0.40$ (40%).",
        "**Uncertainty Robustness:** Particle filters maintain multiple non-Gaussian hypotheses simultaneously; resampling clones high-weight particles and discards weak ones.",
        "**Part B (Kalman State Update):** Prior $\\hat{x}^- = 50$, measurement $z = 60$, gain $K = 0.6$. Innovation is $60 - 50 = +10$.",
        "**Updated State Calculation:** $\\hat{x} = 50 + 0.6(60 - 50) = 50 + 6 = \\mathbf{56}$.",
        "**Motion Correction Interpretation:** Kalman gain of 0.6 means filter places 60% confidence in sensor measurement and 40% in internal model, pulling prior state upward by +6."
    ],
    'MID2-Q19': [
        "**Preprocessing & Detection:** Gaussian smoothing followed by adaptive MoG2 background subtraction extracts moving foreground pixels.",
        "**Morphology & Blobs:** Opening removes salt-and-pepper noise; closing fills cavities; connected components extract bounding boxes and centroids.",
        "**Feature Extraction:** Computes spatial coordinates, HSV color histograms, and deep Re-ID embedding vectors.",
        "**Data Association:** Pairwise cost matrix evaluated using **Hungarian (Munkres) Algorithm** to match tracks to detections in $O(N^3)$.",
        "**Kalman Filtering & Management:** Independent Kalman filters smooth trajectories; life-cycle handles track birth, occlusion coasting, and track termination."
    ],
    'MID2-Q20': [
        "**Confusion Matrix:** True Positives ($TP$), False Positives ($FP$, false alarms), False Negatives ($FN$, missed detections), True Negatives ($TN$).",
        "**Intersection over Union (IoU):** $\\text{IoU} = \\frac{TP}{TP + FP + FN}$; standard overlap threshold is $\\text{IoU} \\ge 0.50$.",
        "**Precision & Recall:** $\\text{Precision} = \\frac{TP}{TP + FP}$ (purity); $\\text{Recall} = \\frac{TP}{TP + FN}$ (completeness).",
        "**F1-Score:** $F_1 = 2 \\times \\frac{P \\cdot R}{P + R} = \\frac{2TP}{2TP + FP + FN}$ (harmonic mean balancing precision and recall).",
        "**Worked Example ($TP=800, FP=100, FN=200$):** $\\text{IoU} = 72.7\\%$, $\\text{Precision} = 88.9\\%$, $\\text{Recall} = 80.0\\%$, $F_1 = 84.2\\%$.",
        "**CLEAR MOT Metrics:** $\\text{MOTA} = 1 - \\frac{\\sum (FN + FP + IDSW)}{\\sum GT}$; $\\text{MOTP}$ measures average bounding box overlap precision."
    ]
}
