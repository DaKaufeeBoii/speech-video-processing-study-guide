# -*- coding: utf-8 -*-
"""
Compact short-answer snippets for each of the 40 SVP exam questions.
Shown when the user activates "Compact Answer View" mode.
Each entry is 2–4 punchy sentences — exam-ready, formula-exact, no waffle.
"""

SHORT_ANSWERS = {

    # ── UNIT 1 ──────────────────────────────────────────────────────────────
    "MID1-Q01": (
        "Speech production = Source × Filter × Radiation: $S(z) = E(z) \\cdot H(z) \\cdot R(z)$. "
        "Vocal cords vibrate (pitch F₀ ≈ 85–255 Hz for voiced), glottal airflow excites the vocal tract tube, "
        "and the tube's resonant formants (F₁ F₂ F₃) shape the phoneme's spectral envelope. "
        "Unvoiced sounds use noise excitation; silence = zero input."
    ),

    "MID1-Q02": (
        "Continuous speech → sampled at $f_s$ → discrete sequence $x[n] = x_a(nT)$, $T = 1/f_s$. "
        "Nyquist: must have $f_s \\ge 2 f_{max}$ (8 kHz for phone, 44.1 kHz for CD). "
        "If undersampled, high-frequency aliases fold onto low frequencies (aliasing = distortion). "
        "Anti-aliasing LPF at $f_s/2$ applied before ADC to prevent this."
    ),

    "MID1-Q03": (
        "$H(z) = \\frac{z(z-0.5)}{z^2 - 0.9z + 0.2}$. "
        "Zeros: $z = 0, 0.5$ (numerator roots). "
        "Poles: factor denominator → $(z-0.5)(z-0.4)$, so poles at $z = 0.5, 0.4$. "
        "Both $|p| < 1$ ⟹ system is BIBO Stable. "
        "On z-plane: plot 2 zeros (circles) and 2 poles (×) inside the unit circle."
    ),

    "MID1-Q04": (
        "FFT computes DFT in $O(N \\log N)$ using Cooley-Tukey butterfly decimation-in-time. "
        "Key properties: Linearity, Time-shift ($x[n-k] ↔ e^{-j\\omega k}X(e^{j\\omega})$), "
        "Convolution ($x*h ↔ X \\cdot H$), Parseval's energy conservation. "
        "Frequency resolution $\\Delta f = f_s / N$; for $N=256$, $f_s=8$ kHz → $\\Delta f = 31.25$ Hz."
    ),

    "MID1-Q05": (
        "Convolution $y[n] = x[n] * h[n] = \\sum_k x[k]\\,h[n-k]$ convolves glottal source with vocal tract IR. "
        "In frequency domain: $Y(z) = X(z)\\cdot H(z)$ — multiplication instead of sum. "
        "Overlap-Add (OLA): split long signal into blocks, FFT each, multiply by $H$, IFFT, overlap-add adjacent blocks. "
        "Overlap-Save is the dual: saves overlapping input samples instead of output."
    ),

    "MID1-Q06": (
        "Linear filter banks: equal Hz bandwidth, uniform spacing — wastes resolution at low frequencies where ears are sensitive. "
        "Non-linear (Mel) filter banks: Mel scale $m = 2595\\log_{10}(1 + f/700)$ — triangular filters dense at low freq, sparse at high. "
        "Result: Mel spectrum captures perceptually relevant features matching the human cochlea. "
        "Non-linear wins for ASR; linear preferred for audio effects (EQ)."
    ),

    "MID1-Q07": (
        "Part A: 4-pt DFT of $x=[2,1,0,1]$: $X[k]=\\sum_n x[n]e^{-j2\\pi kn/4}$. "
        "Result: $X=[4, 2+0j, 0, 2-0j]$; magnitudes $[4, 2, 0, 2]$; dominant = DC ($k=0$, energy=4). "
        "Part B: Frequency resolution $\\Delta f = 8000/256 = 31.25$ Hz/bin. "
        "Bin $k=10$ → $f = 10 \\times 31.25 = 312.5$ Hz."
    ),

    "MID1-Q08": (
        "LPC predicts $\\hat{x}[n] = \\sum_{k=1}^{p} a_k x[n-k]$; residual error $e[n] = x[n] - \\hat{x}[n]$. "
        "Minimise $\\sum e^2[n]$ → Yule-Walker equations: $Ra = r$ (Toeplitz system). "
        "Solve with Levinson-Durbin recursion in $O(p^2)$ — far cheaper than direct inversion. "
        "LPC-10: $p=10$ coefficients compress speech to 2.4 kbps with ~20× compression ratio."
    ),

    # ── UNIT 2 ──────────────────────────────────────────────────────────────
    "MID1-Q09": (
        "6-stage speech feature pipeline: "
        "(1) Pre-emphasis: $y[n]=x[n]-0.97x[n-1]$ — boost high-freq; "
        "(2) Framing: 20–30 ms frames at 10 ms shift; "
        "(3) Windowing: Hamming window $w[n]=0.54-0.46\\cos(2\\pi n/N)$; "
        "(4) FFT → magnitude spectrum; "
        "(5) Mel filter bank + log → MFCC via DCT; "
        "(6) Delta + Delta-delta (velocity + acceleration) appended."
    ),

    "MID1-Q10": (
        "Static features: 13 MFCCs capturing vocal tract shape at one frame (snapshot). "
        "Dynamic features: $\\Delta$(delta) = frame-to-frame MFCC velocity; $\\Delta^2$ = acceleration of motion. "
        "$\\Delta c_i = \\frac{\\sum_{k=1}^{K} k(c_{i+k}-c_{i-k})}{2\\sum k^2}$ over context window. "
        "Concatenating [static|Δ|ΔΔ] gives 39-D vector — dramatically improves HMM/ASR accuracy."
    ),

    "MID1-Q11": (
        "Frame shift $S = \\text{Frame size} - \\text{Overlap} = 400 - 200 = 200$ samples. "
        "Total frames $= \\lfloor (N - L)/S \\rfloor + 1 = \\lfloor (1600-400)/200 \\rfloor + 1 = 6 + 1 = \\mathbf{7}$ frames. "
        "Each frame is 400 samples long, shifted by 200, covering the full 1600-sample signal."
    ),

    "MID1-Q12": (
        "LPCC: derived from LPC coefficients via cepstral recursion — models vocal tract as all-pole IIR; "
        "sensitive to channel noise and microphone mismatch. "
        "MFCC: Mel filter bank + DCT — perceptually motivated, decorrelated coefficients; "
        "robust to additive noise and spectral tilt. "
        "MFCC dominates ASR (GMM-HMM, DNN); LPCC used in low-bit-rate vocoders."
    ),

    "MID1-Q13": (
        "Euclidean: $d = \\sqrt{\\sum (x_i - y_i)^2}$ — fast, assumes equal feature variance. "
        "Mahalanobis: $d = \\sqrt{(\\mathbf{x}-\\mathbf{y})^T \\Sigma^{-1}(\\mathbf{x}-\\mathbf{y})}$ — accounts for feature correlations. "
        "DTW: warps the time axis by finding minimum-cost alignment path through the matrix — handles speed variation. "
        "DTW constraint: Sakoe-Chiba band limits warp path width for speed and monotonicity."
    ),

    "MID1-Q14": (
        "VQ clusters the feature space into $K$ codewords (codebook) via k-means or LBG algorithm. "
        "LBG: initialise 1 centroid → split → iterate until $K$ codewords stabilise; "
        "distortion $D = \\frac{1}{N}\\sum \\min_k ||x_i - c_k||^2$. "
        "Metrics: Average distortion (lower = better), Codebook utilisation, Hit Rate. "
        "Speech recognition maps each frame to its nearest codeword index (discrete observation)."
    ),

    "MID1-Q15": (
        "GMM: $p(x) = \\sum_{m=1}^{M} w_m \\mathcal{N}(x;\\mu_m, \\Sigma_m)$, $\\sum w_m=1$. "
        "EM algorithm: "
        "E-step: compute posterior $\\gamma_{im} = w_m p_m(x_i) / \\sum_k w_k p_k(x_i)$; "
        "M-step: update $w_m$, $\\mu_m$, $\\Sigma_m$ using weighted statistics. "
        "Repeat until log-likelihood converges. "
        "GMM-HMM models each HMM emission as a GMM — gold standard pre-DNN ASR."
    ),

    "MID1-Q16": (
        "HMM: 5-tuple $(S, A, B, \\pi, O)$ — States, Transition matrix $A$, Emission $B$, Initial $\\pi$, Observations $O$. "
        "Three problems: "
        "(1) Evaluation → Forward algorithm $P(O|\\lambda)$; "
        "(2) Decoding → Viterbi algorithm (most likely state path); "
        "(3) Learning → Baum-Welch (EM) re-estimation of $A$, $B$, $\\pi$. "
        "Speech: each phoneme modelled by a 3–5 state left-to-right HMM."
    ),

    # ── UNIT 3 ──────────────────────────────────────────────────────────────
    "MID1-Q17": (
        "2D signal $f(x,y)$ sampled at $(x_s, y_s)$ satisfies 2D Nyquist: "
        "$f_{sx} \\ge 2 f_{x,max}$, $f_{sy} \\ge 2 f_{y,max}$. "
        "2D DFT: $F(u,v) = \\sum_x \\sum_y f(x,y)e^{-j2\\pi(ux/M + vy/N)}$. "
        "Separable: 2D DFT = row-wise 1D FFT then column-wise 1D FFT → $O(MN\\log MN)$. "
        "Applications: image filtering, compression, watermarking."
    ),

    "MID1-Q18": (
        "2D DCT: $F(u,v) = \\frac{2}{\\sqrt{MN}} C(u)C(v) \\sum_x \\sum_y f(x,y) \\cos\\frac{(2x+1)u\\pi}{2M}\\cos\\frac{(2y+1)v\\pi}{2N}$. "
        "Energy compaction: >95% energy in top-left low-frequency coefficients. "
        "JPEG: 8×8 DCT → quantise → zigzag scan → Huffman encode. "
        "MPEG video: DCT applied to inter-frame residuals (after motion compensation)."
    ),

    "MID1-Q19": (
        "2D convolution: $y[m,n] = x[m,n] ** h[m,n] = \\sum_k \\sum_l x[k,l]\\,h[m-k,n-l]$. "
        "Separable filter: $h[m,n]=h_1[m]\\cdot h_2[n]$ → 2D conv = two 1D convolutions → $O(N^2 K)$ not $O(N^2 K^2)$. "
        "Applications: Gaussian blur (separable), Sobel edge detection, image sharpening. "
        "Frequency domain: 2D DFT multiplication $Y(u,v)=X(u,v)\\cdot H(u,v)$."
    ),

    "MID1-Q20": (
        "2D DFT of separable image $f(x,y)=f_1(x)\\cdot f_2(y)$: "
        "$F(u,v) = F_1(u) \\cdot F_2(v)$ — product of two 1D DFTs. "
        "Properties exploited: Separability, Periodicity ($F(u,v)=F(u+M,v+N)$), "
        "Conjugate symmetry for real signals, Convolution theorem, Rotation. "
        "Circular shift in frequency ↔ phase ramp in spatial domain."
    ),

    # ── UNIT 3 continued (MID2) ──────────────────────────────────────────────
    "MID2-Q01": (
        "Optical flow constraint: $I_x u + I_y v + I_t = 0$ — one equation, two unknowns (aperture problem). "
        "Lucas-Kanade assumes constant flow in a local $5\\times5$ window → overdetermined $Ax=b$ → solve via least squares. "
        "Horn-Schunck adds global smoothness regularisation $\\lambda\\iint(u_x^2+u_y^2+v_x^2+v_y^2)\\,dx\\,dy$. "
        "LK = sparse (feature points); HS = dense (whole frame)."
    ),

    "MID2-Q02": (
        "Harris corner detector: structure tensor $M = \\sum w \\begin{bmatrix}I_x^2 & I_xI_y\\\\ I_xI_y & I_y^2\\end{bmatrix}$. "
        "Corner response $R = \\det(M) - k\\cdot\\text{tr}(M)^2$; $R>0$ = corner, $R<0$ = edge, $|R|\\approx0$ = flat. "
        "Shi-Tomasi: $R = \\min(\\lambda_1, \\lambda_2)$ — simpler threshold. "
        "SIFT: scale-space DoG, orientation-normalised 128-D descriptor — rotation and scale invariant."
    ),

    "MID2-Q03": (
        "Image pyramid: Gaussian pyramid = repeated low-pass filter + down-sample (each level halved). "
        "Laplacian pyramid = Gaussian level $i$ − upsample(Gaussian $i+1$) → band-pass residuals. "
        "Optical flow pyramid (Bouguet): compute LK at coarsest level, propagate motion estimate upward. "
        "Handles large displacements that violate small-motion assumption of standard LK."
    ),

    "MID2-Q04": (
        "Kalman filter: 2-step recursive estimator for $\\mathbf{x}_k = A\\mathbf{x}_{k-1} + B\\mathbf{u}_k + \\mathbf{w}$ (process noise $Q$). "
        "Predict: $\\hat{x}^-_k = A\\hat{x}_{k-1}$, $P^-_k = AP_{k-1}A^T + Q$. "
        "Update: $K = P^-_k H^T(HP^-_k H^T + R)^{-1}$; $\\hat{x}_k = \\hat{x}^-_k + K(z_k - H\\hat{x}^-_k)$. "
        "Kalman gain $K$ blends prediction trust vs. measurement trust."
    ),

    # ── UNIT 4 ──────────────────────────────────────────────────────────────
    "MID2-Q05": (
        "Background subtraction: $D(x,y,t)=|I(x,y,t)-B(x,y)|>\\theta$ marks foreground. "
        "MOG2 (Mixture of Gaussians): each pixel modelled by $K=3$–5 Gaussians updated online. "
        "Background update: $\\mu_{new} = (1-\\alpha)\\mu_{old} + \\alpha x_t$; $\\sigma^2$ similarly. "
        "Handles gradual illumination changes, waving trees, and slow-moving objects via adaptive thresholding."
    ),

    "MID2-Q06": (
        "Frame differencing: $D = |I_t - I_{t-1}| > \\theta$ — detects regions that changed between consecutive frames. "
        "Pros: extremely fast ($O(N)$), simple. "
        "Cons: double-contouring (hollow object interiors), misses slow-moving or stopped objects. "
        "Chain: Frame diff → Threshold → Morphological open/close → Contour extraction → Bounding box."
    ),

    "MID2-Q07": (
        "Full Search block matching: for each $M\\times M$ macroblock in frame $t$, search all $(2p+1)^2$ candidate positions in frame $t-1$. "
        "Match criterion: $\\text{SAD} = \\sum |C_A(i,j) - C_B(i+m, j+n)|$; find $\\min$ SAD. "
        "Full search: $p=7$ → $225$ evaluations (accurate but slow). "
        "Three-Step Search: 25 evaluations — coarse-to-fine grid halving; 9× faster, 98% accuracy."
    ),

    "MID2-Q08": (
        "Fundamental matrix $F$: $\\mathbf{x}'^T F \\mathbf{x} = 0$ — encodes epipolar constraint for uncalibrated cameras. "
        "Essential matrix $E$: $\\mathbf{x}'^T E \\mathbf{x} = 0$ — same but for calibrated cameras; $E = K'^T F K$. "
        "8-point algorithm: stack 8 correspondences → solve $Af=0$ via SVD → enforce rank-2 constraint. "
        "RANSAC wrapper rejects outlier matches before 8-point solve."
    ),

    "MID2-Q09": (
        "Block matching: partition frame into $16\\times16$ macroblocks; find best-matching block in search area. "
        "Full Search (FS): checks all $(2p+1)^2$ positions — exhaustive but $O(p^2 MN)$. "
        "Three-Step Search (TSS): step 1 large grid, halve step, repeat 3 times → 25 evaluations. "
        "Diamond Search (DS): large/small diamond patterns; best for MPEG-4 / H.264 encoding."
    ),

    "MID2-Q10": (
        "Motion estimation = minimise $E(\\mathbf{u}) = \\sum_i (I(x_i + u, y_i + v, t+1) - I(x_i, y_i, t))^2$. "
        "Gradient Descent: $\\mathbf{u}_{k+1} = \\mathbf{u}_k - \\alpha \\nabla E$ — slow, safe. "
        "Gauss-Newton: $\\mathbf{u} \\mathrel{+}= -(J^TJ)^{-1}J^T\\mathbf{r}$ — quadratic convergence. "
        "Levenberg-Marquardt: $(J^TJ + \\lambda I)\\delta = J^T\\mathbf{r}$ — switches between GD and GN adaptively."
    ),

    "MID2-Q11": (
        "Transform-domain motion estimation: compute DFT/DCT of blocks, match in frequency space. "
        "Phase correlation: $\\hat{d} = \\arg\\max \\mathcal{F}^{-1}\\left[\\frac{F_1 \\cdot F_2^*}{|F_1 \\cdot F_2^*|}\\right]$ → Dirac delta at displacement. "
        "Advantages: robust to illumination, additive noise suppressed, handles rotational motion. "
        "DCT-domain matching avoids full IDCT in MPEG encoders — 30–40% faster than pixel domain."
    ),

    "MID2-Q12": (
        "SfM pipeline (8 stages): Feature detection (SIFT) → Matching → RANSAC outlier removal → "
        "Essential matrix $E$ → Relative pose $(R,t)$ → Triangulation → Bundle Adjustment (BA) → Dense reconstruction. "
        "Bundle Adjustment: minimise reprojection error $\\sum_i ||x_i - \\pi(P_i X_i)||^2$ jointly over all cameras and points. "
        "Kalman filter tracks camera state; RANSAC rejects mismatches."
    ),

    # ── UNIT 5 ──────────────────────────────────────────────────────────────
    "MID2-Q13": (
        "Region-based segmentation: Thresholding, Region Growing, Watershed — groups pixels by intensity similarity. "
        "Boundary-based: Sobel/Canny edge detection — traces intensity gradients. "
        "Canny: Gaussian smooth → gradient magnitude → NMS → double threshold (high $T_H$, low $T_L$) → hysteresis linking. "
        "Hybrid: Canny edges constrain region growing to prevent boundary leakage."
    ),

    "MID2-Q14": (
        "Change detection: $D(x,y,t) = |I(x,y,t) - I(x,y,t-1)| > \\theta$ (frame diff) or $|I(x,y,t) - B(x,y)| > \\theta$ (BG sub). "
        "Applications: intrusion detection, traffic monitoring, crowd analysis. "
        "Challenges: illumination changes, shadows (use color ratio models), camera jitter (EIS correction). "
        "Statistical BG model (GMM/MOG) adapts slowly to lighting drift while flagging fast-moving objects."
    ),

    "MID2-Q15": (
        "Given: Region A SAD=120, B=45, C=200; threshold $\\theta=100$. "
        "Motion if SAD $>\\theta$: A(120>100)=✓ motion, B(45<100)=✗ static, C(200>100)=✓ motion. "
        "Most dominant: Region C with SAD=200 (maximum). "
        "Without motion: Region B (SAD=45). "
        "Answer: Motion in A and C; static in B; dominant = C."
    ),

    "MID2-Q16": (
        "Optical flow tracking: LK sparse features tracked frame-to-frame → trajectory $T = \\{P_1, P_2, \\ldots, P_k\\}$. "
        "Kalman tracking: predict next position $\\hat{x}^- = A\\hat{x}$; update on detection measurement $z$. "
        "Trajectory: ordered centroid sequence stored over time; smoothed by Kalman to reduce jitter. "
        "SORT algorithm: Hungarian matching of detection bboxes to Kalman tracks each frame."
    ),

    "MID2-Q17": (
        "Compositing equation: $I = \\alpha F + (1-\\alpha)B$, $\\alpha \\in [0,1]$ per pixel. "
        "Closed-form matting: solve for $\\alpha$ using Matting Laplacian from local colour statistics. "
        "Video matting: enforce temporal coherence via optical flow — $\\alpha_t$ consistent with $\\alpha_{t-1}$. "
        "Deep learning matting (IndexNet, MODNet): predict $\\alpha$ matte end-to-end from single image."
    ),

    "MID2-Q18": (
        "Part A: Particle weights $[0.2, 0.3, 0.1, 0.4]$; sum $= 1.0$ → already normalised. "
        "Most likely particle: P4 with weight 0.4 → best hypothesis for object location. "
        "Part B: Updated position $\\hat{x} = \\hat{x}^- + K(z - H\\hat{x}^-) = 50 + 0.6(60-50) = \\mathbf{56}$. "
        "Gain $K=0.6$: 60% weight to measurement (60), 40% to prediction (50)."
    ),

    "MID2-Q19": (
        "9-stage video tracking framework: Frame input → Change detection → BG subtraction → "
        "Morphological cleanup → Contour extraction → Optical flow (LK) → Kalman predict/update → "
        "Hungarian data association → Trajectory update. "
        "Optical flow provides sub-pixel velocity vectors to predict object location during occlusion frames. "
        "Kalman prevents ID swaps when tracks cross by maintaining separate state estimates."
    ),

    "MID2-Q20": (
        "Confusion matrix: TP (correct foreground), FP (false alarm), FN (miss), TN (correct background). "
        "$\\text{Precision} = TP/(TP+FP)$; $\\text{Recall} = TP/(TP+FN)$; "
        "$F1 = 2 \\cdot P \\cdot R/(P+R)$; $\\text{IoU} = TP/(TP+FP+FN)$. "
        "Ideal tracker: IoU → 1, F1 → 1. "
        "Example: IoU=0.75 means predicted and ground-truth bboxes overlap 75%."
    ),
}
