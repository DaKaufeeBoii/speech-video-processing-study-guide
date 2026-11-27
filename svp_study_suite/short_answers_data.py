# -*- coding: utf-8 -*-
"""
Compact short-answer snippets for each of the 40 SVP exam questions.
These are READABLE mini-answers — clear prose with key terms highlighted,
enough to revise a question in 60 seconds without opening the full answer.
"""

SHORT_ANSWERS = {

    # ── UNIT 1 ──────────────────────────────────────────────────────────────

    "MID1-Q01": """Speech is produced in three stages working together like a signal chain.

First, the EXCITATION SOURCE: your lungs push air up through your vocal cords (glottis). For voiced sounds (vowels, /z/, /v/), the cords vibrate rapidly to create a buzzing pulse train at your fundamental frequency (F₀ ≈ 85–255 Hz for humans). For unvoiced sounds (/s/, /f/), the cords stay open and airflow becomes random noise. For silence, there is no excitation at all.

Second, the VOCAL TRACT FILTER: the throat, mouth, and nasal cavity act like a resonance tube. This tube amplifies certain frequencies called formants (F1, F2, F3). The shape of the tube changes as you move your tongue, lips, and jaw — which is how you change which vowel or consonant you're making. Mathematically, the vocal tract is modelled as an all-pole filter H(z).

Third, the RADIATION: sound radiates out from your lips into the air. This adds a slight high-frequency boost modelled as R(z).

The full model is: Speech S(z) = Excitation E(z) × Vocal Tract H(z) × Radiation R(z). This source-filter model is the foundation of all speech coding (LPC, vocoders, etc.).""",

    "MID1-Q02": """When we record speech on a computer, we convert the continuous analog wave into a sequence of digital numbers by measuring ("sampling") the signal thousands of times per second.

The sampling rate fs tells you how many samples per second are taken. The standard for phone calls is 8,000 samples/sec (8 kHz); for music it's 44,100 (44.1 kHz).

The critical rule is the Nyquist Theorem: you must sample at least twice as fast as the highest frequency in the signal. If the signal has frequencies up to fmax Hz, then fs must be ≥ 2 × fmax. Human speech contains frequencies up to about 4 kHz, so 8 kHz is just enough.

If you sample too slowly (fs < 2 × fmax), a phenomenon called ALIASING occurs. High-frequency components "fold over" and appear as false low-frequency content — like how a spinning wheel on video sometimes looks like it's spinning backward. Once aliasing happens, you cannot recover the original signal.

To prevent aliasing, an anti-aliasing low-pass filter is applied to the analog signal before the ADC (analog-to-digital converter), cutting off everything above fs/2. After sampling, reconstruction uses a DAC (digital-to-analog converter) followed by a reconstruction filter.""",

    "MID1-Q03": """Given the transfer function H(z) = z(z − 0.5) / (z² − 0.9z + 0.2), we need to find poles, zeros, and check stability.

ZEROS are found by setting the numerator = 0:
  Numerator: z(z − 0.5) = 0  →  z = 0 and z = 0.5
So there are two zeros at z = 0 and z = 0.5.

POLES are found by setting the denominator = 0:
  Denominator: z² − 0.9z + 0.2 = 0
  Factor: (z − 0.5)(z − 0.4) = 0  →  z = 0.5 and z = 0.4
So there are two poles at z = 0.5 and z = 0.4.

Z-PLANE PLOT: Draw the unit circle. Mark zeros as open circles (○) at z=0 and z=0.5. Mark poles as crosses (×) at z=0.5 and z=0.4.

STABILITY CHECK: A system is BIBO Stable if and only if ALL poles lie strictly inside the unit circle (|pole| < 1).
  |0.5| = 0.5 < 1 ✓
  |0.4| = 0.4 < 1 ✓
Both poles are inside the unit circle, so the system IS BIBO Stable.""",

    "MID1-Q04": """The Discrete Fourier Transform (DFT) converts a time-domain sequence of N samples into its frequency-domain representation — but computing it directly takes N² multiplications, which is too slow for real signals.

The Fast Fourier Transform (FFT) is an algorithm that computes the exact same DFT result in only N·log₂(N) operations using a clever "divide and conquer" approach called the Cooley-Tukey butterfly. For N=1024 samples, that's the difference between 1,048,576 operations vs. 10,240 — roughly 100× faster.

Key properties of the FFT (and DFT) used in speech analysis:
• LINEARITY: DFT(ax + by) = a·DFT(x) + b·DFT(y) — you can process signals independently and combine.
• TIME SHIFT: Shifting a signal by k samples in time only adds a phase shift in frequency — the magnitude spectrum is unchanged.
• CONVOLUTION THEOREM: Convolution in time (which is slow O(N²)) becomes simple multiplication in frequency (O(N)) — this is how digital filters are applied efficiently.
• PARSEVAL'S THEOREM: Total energy is preserved between time and frequency domains — useful for spectral energy analysis.
• FREQUENCY RESOLUTION: Δf = fs / N. With 8 kHz sampling and N=256 samples, each frequency bin represents 31.25 Hz.

In speech processing, the FFT lets us compute spectrograms, formant frequencies, and MFCC features in real time.""",

    "MID1-Q05": """Convolution describes how a system (like a digital filter or the vocal tract) responds to an input signal. If x[n] is your input and h[n] is the system's impulse response, then the output is:
  y[n] = x[n] * h[n] = Σ x[k] · h[n−k]

This sum slides h over x — for every output sample, you multiply and sum all overlapping values. Direct convolution is O(N²) which is slow for long signals.

The CONVOLUTION THEOREM provides a shortcut: convolution in time = multiplication in frequency.
  Y(z) = X(z) · H(z)
So instead of sliding h over x, you just: FFT(x), FFT(h), multiply pointwise, then IFFT the result. This turns O(N²) into O(N log N).

For CONTINUOUS speech signals (which don't fit in memory at once), two block-processing algorithms handle this efficiently:

OVERLAP-ADD: Split the input into non-overlapping blocks of length L. FFT each block, multiply by H, IFFT, then add the overlapping tails of adjacent output blocks together.

OVERLAP-SAVE: Keep a "saved" overlap region from the previous block at the start of each new input block. Compute circular convolution, then discard the first P samples (which are circular aliasing artefacts) and keep only the valid output samples.

Both methods produce identical results to direct convolution but run in real time on streaming audio.""",

    "MID1-Q06": """Filter banks are collections of bandpass filters that split a signal into multiple frequency sub-bands simultaneously — like a graphic equaliser but for analysis.

LINEAR FILTER BANKS divide the frequency axis into equal-width bands (uniform spacing). For example, 20 filters each covering 200 Hz. This is simple but wasteful — it spends as many filters on the high-frequency range (4000–8000 Hz) as on the low-frequency range (0–200 Hz), even though human ears are far more sensitive to low frequencies.

NON-LINEAR (MEL) FILTER BANKS use a perceptual frequency scale called the Mel scale, defined as:
  Mel(f) = 2595 × log₁₀(1 + f/700)

On the Mel scale, filters are closely spaced at low frequencies (capturing fine details of vowel formants) and widely spaced at high frequencies (where the ear is less precise). This matches how the human cochlea actually works.

The result — Mel-scaled log filter bank energies — is then passed through a DCT (Discrete Cosine Transform) to produce MFCCs (Mel Frequency Cepstral Coefficients), which are the dominant feature for speech and speaker recognition.

In summary: Linear filter banks are mathematically uniform but perceptually misaligned. Mel filter banks are designed around human hearing and dramatically improve speech recognition accuracy.""",

    "MID1-Q07": """PART A — Compute the 4-point DFT of x[n] = [2, 1, 0, 1]:

The 4-point DFT formula is: X[k] = Σ(n=0 to 3) x[n] · e^(−j2πkn/4)

Computing each output:
  X[0] = 2 + 1 + 0 + 1 = 4         (DC component)
  X[1] = 2 + 1·(−j) + 0 + 1·(j) = 2 + 0j = 2
  X[2] = 2 + 1·(−1) + 0 + 1·(−1) = 0
  X[3] = 2 + 1·(j) + 0 + 1·(−j) = 2

Magnitudes: |X[0]|=4, |X[1]|=2, |X[2]|=0, |X[3]|=2
DOMINANT FREQUENCY: k=0 (DC), with the highest magnitude of 4. The signal has the most energy at zero frequency (steady component).

PART B — Sampling at 8 kHz, frame size = 256 samples:

Frequency Resolution: Δf = fs / N = 8000 / 256 = 31.25 Hz per bin

Frequency at k=10: f = k × Δf = 10 × 31.25 = 312.5 Hz

So bin k=10 in the DFT corresponds to a real-world frequency of 312.5 Hz.""",

    "MID1-Q08": """LPC (Linear Predictive Coding) is a technique for modeling the vocal tract by predicting each speech sample from the previous p samples.

The core idea: the current sample x[n] can be approximated as a weighted sum of the past p samples:
  x̂[n] = a₁x[n−1] + a₂x[n−2] + ... + aₚx[n−p]

The prediction error (residual) is: e[n] = x[n] − x̂[n]

We want to find the coefficients a₁...aₚ that minimise the total squared error Σe²[n].

This minimisation leads to the YULE-WALKER EQUATIONS, which form the matrix system R·a = r, where R is a Toeplitz autocorrelation matrix. The beautiful thing about Toeplitz matrices is that they can be solved with the LEVINSON-DURBIN ALGORITHM in O(p²) operations — much faster than general matrix inversion.

The LPC order p is typically 10–14 for speech (one pole per formant, plus extras for bandwidth and tilt). The resulting coefficients compactly describe the vocal tract shape.

APPLICATIONS:
• LPC-10 vocoder: compresses speech to just 2.4 kbps (20× compression)
• Pole-Zero speech synthesis
• Feature extraction for ASR (LPCC = LPC Cepstral Coefficients)
• Voice coding in mobile phones (CELP coders use LPC)""",

    # ── UNIT 2 ──────────────────────────────────────────────────────────────

    "MID1-Q09": """The speech feature extraction pipeline converts raw audio into compact numerical vectors (feature frames) that machine learning models can work with. There are 6 key stages:

STAGE 1 — PRE-EMPHASIS: Apply the filter y[n] = x[n] − 0.97·x[n−1]. This boosts high-frequency components, compensating for the natural roll-off in speech spectra and improving numerical conditioning of later stages.

STAGE 2 — FRAMING: Divide the continuous signal into short overlapping windows. Typical values: frame length = 25ms (200 samples at 8kHz), frame shift = 10ms (80 samples). Speech is considered quasi-stationary within a 20–30ms window, so this is safe.

STAGE 3 — WINDOWING: Multiply each frame by a Hamming window: w[n] = 0.54 − 0.46·cos(2πn/N). This tapers the edges of the frame to zero, preventing spectral leakage (sharp discontinuities at frame edges cause smearing in the DFT).

STAGE 4 — FFT: Compute the N-point FFT of the windowed frame to get the power spectrum |X[k]|².

STAGE 5 — MEL FILTER BANK + LOG + DCT: Apply M triangular Mel-scaled filters to the power spectrum, take the log (compresses dynamic range), then apply DCT to decorrelate the outputs → produces the static MFCC coefficients (typically 13).

STAGE 6 — DELTA FEATURES: Compute first derivatives (Δ = velocity) and second derivatives (ΔΔ = acceleration) of the MFCC trajectory across frames. Concatenating static + Δ + ΔΔ gives the standard 39-dimensional feature vector.""",

    "MID1-Q10": """In speech recognition, we need features that capture not just WHAT the vocal tract looks like at a given instant, but also HOW it's moving over time. That's where static and dynamic features come in.

STATIC FEATURES (13 MFCCs): Each frame produces 13 Mel Cepstral Coefficients that describe the shape of the vocal tract spectrum at that moment in time — like a snapshot of your mouth position.

DYNAMIC FEATURES — DELTA (Δ): These capture the frame-to-frame rate of change of the MFCCs — essentially the velocity of vocal tract movement. The delta formula over a context window of K frames is:
  Δcᵢ(t) = Σₖ k · [cᵢ(t+k) − cᵢ(t−k)] / (2·Σₖ k²)
This gives 13 more numbers, one for each MFCC.

DYNAMIC FEATURES — DELTA-DELTA (ΔΔ): These are the second derivative — the acceleration of movement — computed by applying the same delta formula to the Δ features. Another 13 numbers.

FINAL FEATURE VECTOR: Stacking [Static | Δ | ΔΔ] gives a 39-dimensional vector per frame.

WHY IT MATTERS: The delta features dramatically improve speech recognition accuracy because they encode the trajectory of articulation — the difference between a fast consonant stop (/b/, /p/) and a slow vowel glide (/a/ → /e/) shows up clearly in the velocity and acceleration features.""",

    "MID1-Q11": """This is a straightforward numerical calculation for counting the number of analysis frames in a signal.

GIVEN:
• Total signal length: N = 1600 samples
• Frame size (window length): L = 400 samples
• Overlap between consecutive frames: O = 200 samples

STEP 1 — Frame shift (hop size):
  S = L − O = 400 − 200 = 200 samples

The frame shift tells you how many samples you advance before starting the next frame.

STEP 2 — Number of frames:
  Total frames = floor((N − L) / S) + 1
                = floor((1600 − 400) / 200) + 1
                = floor(1200 / 200) + 1
                = floor(6) + 1
                = 6 + 1 = 7 FRAMES

INTUITION: Frame 1 covers samples 1–400. Frame 2 covers 201–600 (shifted by 200). Frame 3 covers 401–800. And so on. Frame 7 covers samples 1201–1600, which exactly reaches the end of the signal.

ANSWER: 7 frames.""",

    "MID1-Q12": """Both LPCC and MFCC are cepstral feature sets used for speech recognition, but they model speech very differently and have very different robustness characteristics.

LPCC (LPC Cepstral Coefficients):
• Derived from the LPC all-pole model of the vocal tract
• The LPC coefficients are converted to cepstral domain via a recursive formula: cₙ = aₙ + Σₖ (k/n) cₖ aₙ₋ₖ
• Models speech as a pure all-pole system — good for voiced speech, poor for fricatives
• Very sensitive to channel noise and microphone frequency response — if the channel changes, the cepstrum shifts and recognition fails
• Primarily used in low-bit-rate speech coders (vocoders)

MFCC (Mel Frequency Cepstral Coefficients):
• Derived from a Mel-scaled filter bank designed to mimic the human ear's frequency response
• Applies log compression (matches perceived loudness) + DCT (decorrelates the filter bank outputs)
• Robust to additive noise and channel distortions because the perceptual weighting de-emphasises artefacts
• Universally used in modern ASR systems (GMM-HMM, DNN, Transformer-based ASR)
• Can be made even more robust with Cepstral Mean Subtraction (CMS) to remove channel effects

BOTTOM LINE: Use MFCC for recognition tasks (noise-robust, perceptually meaningful). Use LPCC for coding tasks (compact vocal tract model for speech synthesis).""",

    "MID1-Q13": """When comparing two speech feature sequences (like query vs. reference), we need a distance measure to decide how "different" they are. Three measures are commonly used:

EUCLIDEAN DISTANCE:
  d(x, y) = √Σᵢ (xᵢ − yᵢ)²
Treats all features equally. Fast to compute. But it assumes features have equal variance and are independent — which is false for correlated MFCCs. It also cannot handle timing differences between speakers.

MAHALANOBIS DISTANCE:
  d(x, y) = √[(x−y)ᵀ Σ⁻¹ (x−y)]
Accounts for feature covariance and scale by normalising by the covariance matrix Σ. Features that vary a lot together are treated as one dimension. Much smarter but requires computing and inverting Σ.

DYNAMIC TIME WARPING (DTW):
Both Euclidean and Mahalanobis compare frame-by-frame at the same time index — which fails when one speaker says a word faster than another. DTW solves this by allowing the time axes of two sequences to be stretched and compressed to find the best alignment.
  DTW finds the minimum-cost path through a distance matrix D[i,j] where D[i,j] = local_dist(xᵢ, yⱼ) + min(D[i-1,j], D[i,j-1], D[i-1,j-1])
DTW is the standard method for isolated word recognition and was used before HMMs became dominant. The Sakoe-Chiba band constrains the warp path to prevent unrealistic alignments.""",

    "MID1-Q14": """Vector Quantisation (VQ) is a compression technique that replaces continuous feature vectors with the index of the nearest codeword from a pre-built codebook.

HOW IT WORKS: During training, the LBG (Linde-Buzo-Gray) algorithm clusters all training feature vectors into K groups and finds the centroid (average) of each group. These K centroids form the codebook. During recognition, each incoming feature vector is compared to all K codewords and the nearest one is selected (nearest-neighbour quantisation).

LBG ALGORITHM:
1. Start with 1 codeword (the mean of all data)
2. Split it into 2 by perturbing slightly
3. Run k-means to convergence
4. Split each codeword again → 4, then 8, 16... until you have K = 2ᵐ codewords
5. Final iteration of k-means to refine

PERFORMANCE METRICS:
• Average Distortion: mean squared distance from each training vector to its assigned codeword (lower = better fit)
• Codebook Utilisation: fraction of codewords that are actually used (want close to 100%)
• Hit Rate / Accuracy: fraction of test vectors correctly classified

IN SPEECH RECOGNITION: VQ maps continuous MFCC frames to discrete observation symbols, enabling the HMM to work with finite discrete observation alphabets instead of continuous distributions.""",

    "MID1-Q15": """A Gaussian Mixture Model (GMM) models the probability distribution of a feature vector as a weighted sum of K Gaussian (bell curve) components:

  p(x) = Σₖ wₖ · 𝒩(x; μₖ, Σₖ)

where wₖ are mixture weights (must sum to 1), μₖ are component means, and Σₖ are covariance matrices.

GMMs can approximate ANY continuous distribution by using enough components — a single Gaussian is too rigid, but a mixture of 8 or 16 can model complex multi-modal feature distributions.

TRAINING with the EM ALGORITHM (alternates between two steps until convergence):

E-Step (Expectation): For each training frame xᵢ, compute the posterior probability that it came from each component:
  γ(i,k) = wₖ · 𝒩(xᵢ; μₖ, Σₖ) / Σⱼ wⱼ · 𝒩(xᵢ; μⱼ, Σⱼ)
This is the "responsibility" of component k for data point i.

M-Step (Maximisation): Update the parameters using the weighted statistics:
  wₖ_new = (1/N) Σᵢ γ(i,k)
  μₖ_new = Σᵢ γ(i,k)·xᵢ / Σᵢ γ(i,k)
  Σₖ_new = Σᵢ γ(i,k)·(xᵢ−μₖ)(xᵢ−μₖ)ᵀ / Σᵢ γ(i,k)

IN SPEECH RECOGNITION: Each HMM state's emission probability is modelled as a GMM. GMM-HMM was the dominant ASR architecture from the 1990s until deep learning replaced it around 2012.""",

    "MID1-Q16": """A Hidden Markov Model (HMM) is a probabilistic model for time-series data where the system moves through a sequence of HIDDEN states, each producing an observable output according to some probability distribution.

HMM is defined by 5 elements (λ = {S, A, B, π, O}):
• S: Set of N hidden states (e.g., the phoneme /a/ has states for onset, steady-state, offset)
• A: Transition matrix — Aᵢⱼ = probability of moving from state i to state j
• B: Emission probability — B(j, oₜ) = probability of observing oₜ when in state j
• π: Initial state distribution — probability of starting in each state
• O: Sequence of observations (MFCC feature vectors)

The THREE fundamental problems and their solutions:

PROBLEM 1 — EVALUATION: "What is P(O|λ)?" — How likely is this observation sequence given the model?
  Solution: Forward Algorithm. Builds up probabilities incrementally: α(t,j) = P(O₁...Oₜ, state j at t | λ)

PROBLEM 2 — DECODING: "What is the most likely hidden state sequence?"
  Solution: Viterbi Algorithm. Dynamic programming finds the optimal path through the HMM grid. Used in recognition to identify which phoneme sequence was spoken.

PROBLEM 3 — LEARNING: "How do we train the model from data?"
  Solution: Baum-Welch (EM for HMMs). Re-estimates A, B, and π to maximise P(O|λ).

IN SPEECH: Each phoneme is modelled by a 3–5 state left-to-right HMM (no backwards transitions). A word is formed by concatenating phoneme HMMs. Recognition finds the most likely word sequence via Viterbi decoding.""",

    # ── UNIT 3 ──────────────────────────────────────────────────────────────

    "MID1-Q17": """While speech processing deals with 1D signals (time), images and video are 2D signals — described by both horizontal and vertical spatial coordinates f(x, y).

SAMPLING 2D SIGNALS: Just like 1D signals need Nyquist sampling, 2D signals need 2D Nyquist:
• Sample rate in x-direction: fsx ≥ 2 × fₓ_max (horizontal spatial frequency)
• Sample rate in y-direction: fsy ≥ 2 × fy_max (vertical spatial frequency)
In a digital image, the sampling rate = number of pixels per unit length (pixel density). Too few pixels causes spatial aliasing — the "jagged staircase" effect on diagonal edges (also called "jaggies").

2D DFT: Extends the 1D DFT to two dimensions:
  F(u,v) = Σₓ Σᵧ f(x,y) · e^(−j2π(ux/M + vy/N))
Here u is horizontal frequency and v is vertical frequency. The output F(u,v) tells you the amplitude and phase of the spatial frequency component (u,v) in the image.

SEPARABILITY: The 2D DFT can be computed as:
1. Apply 1D FFT to each row of the image
2. Apply 1D FFT to each column of the result
This reduces complexity from O(M²N²) to O(MN·log(MN)) — a massive speedup for large images.

The 2D DFT is used for image filtering (blurring, sharpening), compression (JPEG), texture analysis, and watermarking.""",

    "MID1-Q18": """The 2D DCT (Discrete Cosine Transform) is the mathematical backbone of JPEG image compression and MPEG video compression. It converts a spatial-domain image block into frequency coefficients.

THE 2D DCT FORMULA:
  F(u,v) = (2/√MN) · C(u) · C(v) · Σₓ Σᵧ f(x,y) · cos[(2x+1)uπ/2M] · cos[(2y+1)vπ/2N]
where C(0) = 1/√2 and C(k) = 1 for k > 0.

KEY ADVANTAGE — ENERGY COMPACTION: The DCT concentrates most of the image's energy into a small number of low-frequency coefficients in the top-left corner of the transformed block. For a typical 8×8 image block, over 95% of the energy sits in just 10–15 of the 64 coefficients. This is better than DFT for real images because the DCT uses only cosine basis functions (no imaginary parts) and avoids the "blocking" artefacts caused by the implicit periodicity assumption of the DFT.

HOW JPEG USES IT:
1. Divide image into 8×8 blocks
2. Apply 2D DCT to each block
3. Quantise the coefficients (divide by a quantisation table, round to integer) — this is where lossy compression happens
4. Zigzag scan the quantised coefficients (top-left to bottom-right)
5. Run-length encode the zeros, then Huffman encode the result

HOW MPEG USES IT: After motion compensation (predicting a frame from the previous one), the RESIDUAL (difference between predicted and actual) is small. The 2D DCT of this residual is sparse, compressing video at high ratios.""",

    "MID1-Q19": """2D convolution extends the 1D convolution operation to images. It's the fundamental operation behind image filtering (blur, sharpen, edge detect).

THE 2D CONVOLUTION FORMULA:
  y[m,n] = x[m,n] ** h[m,n] = Σₖ Σₗ x[k,l] · h[m−k, n−l]

This slides the filter kernel h over every position in the image x, computing a weighted sum at each location.

BORDER HANDLING: At the edges of the image, the kernel extends beyond the boundary. Common solutions:
• Zero-padding: treat pixels outside as 0
• Reflect: mirror the image at borders
• Wrap: treat the image as periodic

SEPARABLE FILTERS: If the 2D kernel can be written as the outer product of two 1D filters:
  h[m,n] = h₁[m] · h₂[n]
Then the 2D convolution reduces to two sequential 1D convolutions — first convolve all rows with h₁, then all columns with h₂. This reduces computation from O(N²K²) to O(N²K) — huge savings for large kernels.

COMMON SEPARABLE FILTERS:
• Gaussian blur: smooth image, reduce noise
• Sobel edge detector: find horizontal/vertical edges

FREQUENCY DOMAIN SHORTCUT: 2D convolution = element-wise multiplication in the 2D DFT domain:
  Y(u,v) = X(u,v) · H(u,v)
For large kernels, it's faster to FFT both, multiply, and IFFT back.""",

    "MID1-Q20": """When a 2D signal is SEPARABLE — meaning f(x,y) = f₁(x) · f₂(y) — its 2D DFT also separates into a product of two 1D DFTs:
  F(u,v) = F₁(u) · F₂(v)

This separability is extremely useful computationally: instead of one giant 2D transform, you do 1D transforms on rows then columns.

KEY PROPERTIES OF THE 2D DFT:

PERIODICITY: F(u,v) = F(u+M, v+N) — the DFT output repeats with period M horizontally and N vertically. This means the DFT implicitly assumes the image tiles infinitely.

CONJUGATE SYMMETRY: For real-valued images f(x,y), the DFT satisfies F(u,v) = F*(−u,−v). The spectrum is conjugate-symmetric, so you only need to compute half of it.

CONVOLUTION THEOREM: Convolution in spatial domain ↔ multiplication in frequency domain. This is used for fast image filtering.

ROTATION PROPERTY: If you rotate f(x,y) by angle θ, then F(u,v) rotates by the same angle θ. Useful for rotation-invariant texture analysis.

TRANSLATION PROPERTY: Shifting f(x,y) in space only changes the PHASE of F(u,v), not the magnitude. So |F(u,v)| is shift-invariant — the magnitude spectrum doesn't change when you move the image.

DC COMPONENT: F(0,0) = sum of all pixel values = average image intensity. It's always the highest-energy component for natural images.""",

    # ── UNIT 3 MID2 ──────────────────────────────────────────────────────────

    "MID2-Q01": """Optical flow describes how pixels appear to move from one video frame to the next — it gives every pixel a velocity vector (u, v) representing motion in the x and y directions.

THE FUNDAMENTAL CONSTRAINT (Brightness Constancy Assumption):
  Iₓu + Iᵧv + Iₜ = 0
Where Iₓ, Iᵧ are spatial image gradients and Iₜ is the temporal gradient (how brightness changes over time). This is ONE equation with TWO unknowns (u and v) — the APERTURE PROBLEM. Looking through a small window, you can only detect motion perpendicular to edges, not parallel. You need extra constraints to solve for both components.

LUCAS-KANADE (Sparse, Local):
Assumes the flow is constant within a small neighbourhood (typically 5×5 or 7×7 pixels). This gives enough equations to solve the overdetermined system Ax = b using weighted least squares:
  [u, v]ᵀ = (AᵀWA)⁻¹ AᵀWb
Works great at corners (high texture regions). Fails at smooth regions and for large displacements.

HORN-SCHUNCK (Dense, Global):
Instead of local patches, adds a global SMOOTHNESS CONSTRAINT — flow should vary smoothly across the whole image. Minimises:
  E = Σ(Iₓu + Iᵧv + Iₜ)² + λ·Σ(uₓ² + uᵧ² + vₓ² + vᵧ²)
Solved as a system of partial differential equations iteratively. Produces dense flow for every pixel but over-smooths motion boundaries.

COMPARISON: LK = fast, sparse, good for feature tracking. HS = slow, dense, good for full motion field estimation.""",

    "MID2-Q02": """Before computing optical flow, we need to detect KEYPOINTS — distinctive points in the image that can be reliably tracked over time (corners and blobs work well; flat regions and edges don't).

HARRIS CORNER DETECTOR:
Builds a structure tensor M for each pixel using the local gradient:
  M = Σ w(x,y) · [[Iₓ², IₓIᵧ], [IₓIᵧ, Iᵧ²]]
Then computes the corner response: R = det(M) − k·trace(M)²  (k ≈ 0.04–0.06)
• R >> 0: corner (both eigenvalues large → detected!)
• R << 0: edge (one large eigenvalue)
• |R| ≈ 0: flat region (both eigenvalues small)
Harris is rotation-invariant but NOT scale-invariant.

SHI-TOMASI (Good Features to Track):
Instead of R = det − k·trace², uses R = min(λ₁, λ₂). Select points where the smaller eigenvalue exceeds a threshold. More stable than Harris in practice. Used in OpenCV's goodFeaturesToTrack().

SIFT (Scale-Invariant Feature Transform):
Detects features across multiple scales using Difference of Gaussians (DoG). For each detected point, assigns a dominant orientation from the local gradient histogram. Describes the feature with a 128-dimensional vector of gradient histograms. SIFT is invariant to scale, rotation, and partially to illumination changes — making it powerful for matching features across very different views.""",

    "MID2-Q03": """The APERTURE PROBLEM and SMALL-MOTION ASSUMPTION limit standard optical flow: Lucas-Kanade fails when objects move more than a few pixels between frames (which happens with fast motion or low frame rates).

IMAGE PYRAMIDS solve this by processing the image at multiple resolutions.

GAUSSIAN PYRAMID:
• Level 0: original image
• Level 1: apply Gaussian blur then downsample by 2 (half width, half height)
• Level 2: repeat on Level 1 → quarter size
• Continue for 3–5 levels
Each level is a low-pass filtered, downsampled version of the previous. Fast objects that move many pixels at full resolution move only a FEW pixels at the coarsest pyramid level.

LAPLACIAN PYRAMID:
• Laplacian Level i = Gaussian Level i − upsample(Gaussian Level i+1)
• Each Laplacian level captures BAND-PASS details (edges and textures at a specific scale)
• The Laplacian pyramid is invertible — you can perfectly reconstruct the original image

PYRAMID OPTICAL FLOW (Bouguet's algorithm):
1. Compute LK optical flow at the COARSEST pyramid level (small displacements → LK works fine)
2. Upsample the motion estimate to the next finer level and use it as an initialisation
3. Compute RESIDUAL flow at that level
4. Repeat up to the finest level (original resolution)
Result: handles large displacements robustly. This is exactly what OpenCV's calcOpticalFlowPyrLK does.""",

    "MID2-Q04": """The Kalman filter is an optimal recursive estimator — it fuses noisy measurements with a motion model to produce the best possible estimate of an object's position (or any state).

THE STATE MODEL: We model the object's state as xₖ = A·xₖ₋₁ + B·uₖ + wₖ
where A is the transition matrix (e.g., constant velocity model), B·u is control input, and w is process noise with covariance Q.

The MEASUREMENT is: zₖ = H·xₖ + vₖ  (where v is measurement noise with covariance R)

PREDICT STEP (before seeing the new measurement):
  x̂ₖ⁻ = A·x̂ₖ₋₁             (predict state)
  Pₖ⁻  = A·Pₖ₋₁·Aᵀ + Q      (predict uncertainty)

UPDATE STEP (after receiving measurement zₖ):
  Kₖ  = Pₖ⁻·Hᵀ·(H·Pₖ⁻·Hᵀ + R)⁻¹   (Kalman gain)
  x̂ₖ = x̂ₖ⁻ + Kₖ·(zₖ − H·x̂ₖ⁻)    (corrected state)
  Pₖ  = (I − KₖH)·Pₖ⁻              (corrected uncertainty)

INTUITION OF KALMAN GAIN K:
• K → 0: trust the PREDICTION (measurement is noisy, ignore it)
• K → 1: trust the MEASUREMENT (prediction model is noisy, follow the sensor)
• In practice, K balances both based on relative noise levels Q and R

EXAMPLE: If predicted position x̂⁻ = 50, measurement z = 60, and K = 0.6:
  x̂ = 50 + 0.6·(60 − 50) = 50 + 6 = 56

USES: Kalman filtering is used in object tracking (SORT, DeepSORT), GPS navigation, robot localisation, and sensor fusion.""",

    # ── UNIT 4 ──────────────────────────────────────────────────────────────

    "MID2-Q05": """Background subtraction is a technique for detecting MOVING OBJECTS (foreground) by separating them from the stationary background in a video sequence.

BASIC METHOD: Maintain a background model B(x,y). For each new frame I(x,y,t), compute the foreground mask:
  Foreground: pixels where |I(x,y,t) − B(x,y)| > threshold θ

The challenge is that the background is NOT static — illumination changes, shadows move, trees sway. A fixed background model quickly becomes outdated.

RUNNING AVERAGE (simple adaptive model):
  Bₜ = (1−α)·Bₜ₋₁ + α·Iₜ
The background is updated continuously with learning rate α. Slow update (small α) = slow to adapt to lighting changes. Fast update (large α) = may accidentally absorb moving objects into the background.

MOG2 — MIXTURE OF GAUSSIANS (robust method):
Each pixel is modelled by K=3–5 Gaussian distributions, not just one. This handles multi-modal backgrounds like a flickering monitor or waving leaves. Each Gaussian has its own mean, variance, and weight, all updated online as new frames arrive. Background = Gaussians with high weight and low variance. Foreground = any pixel not explained by these background Gaussians.

POST-PROCESSING: After segmentation, apply morphological operations (erosion to remove noise, dilation to fill holes) then find contours and bounding boxes around detected foreground blobs.""",

    "MID2-Q06": """Frame differencing is the simplest possible motion detection method — just subtract two consecutive video frames and look at where they differ.

THE OPERATION:
  Difference image: D(x,y) = |I(x,y,t) − I(x,y,t−1)|
  Foreground mask: M(x,y) = 1 if D(x,y) > threshold θ, else 0

Pixels that changed significantly between frames are classified as motion regions. The threshold θ controls sensitivity — low θ detects subtle motion but adds noise, high θ only catches large movement.

ADVANTAGES:
• Extremely fast — just subtraction and comparison
• No model to build or maintain
• Needs only 2 frames of memory

LIMITATIONS:
• DOUBLE CONTOURING: When a solid object moves, you see ghost outlines at both the old position (now empty background) and new position (now covered). The object interior appears hollow.
• BLIND TO SLOW MOTION: Objects moving very slowly (e.g., parked car creeping forward) may produce D < θ and be missed entirely
• SENSITIVE TO CAMERA SHAKE: Any camera vibration causes the entire frame to light up

TYPICAL PIPELINE:
Frame diff → Threshold → Gaussian blur (reduce noise) → Morphological dilation (fill gaps) → Find contours → Draw bounding boxes""",

    "MID2-Q07": """Block matching is the standard technique used in video compression (MPEG, H.264) to find MOTION VECTORS — it figures out where each region of a frame came from in the previous frame.

THE CONCEPT: Divide the current frame into non-overlapping blocks (typically 16×16 macroblocks). For each block, search the previous frame to find the best-matching block within a search area of ±p pixels. The offset between the original block position and the best match is the motion vector.

MATCH QUALITY METRIC — SUM OF ABSOLUTE DIFFERENCES (SAD):
  SAD(m,n) = Σᵢ Σⱼ |Current_block(i,j) − Previous_block(i+m, j+n)|
Lower SAD = better match.

FULL SEARCH (Exhaustive):
Check ALL (2p+1)² candidate positions. For p=7: checks 15×15 = 225 positions. Finds the GLOBAL minimum (best possible match). Very accurate but slow — O(N² × (2p+1)²).

THREE-STEP SEARCH (TSS) — Fast approximation:
Step 1: Check 9 positions on a coarse grid (step = p/2). Move to best.
Step 2: Check 9 positions on half the grid. Move to best.
Step 3: Check 9 positions on 1-pixel grid. Final result.
Total: only 25 evaluations. 9× faster than full search, finds near-optimal motion vectors 98% of the time.

DIAMOND SEARCH: Uses a diamond-shaped search pattern — better for typical video where most motion is small.""",

    "MID2-Q08": """When you have two cameras looking at the same 3D scene from different positions, the EPIPOLAR GEOMETRY describes the geometric relationship between their views. This is essential for 3D reconstruction.

FUNDAMENTAL MATRIX F:
The fundamental matrix F relates corresponding points between two uncalibrated cameras. If x is a point in image 1 and x' is the corresponding point in image 2:
  x'ᵀ · F · x = 0

This constraint means: for any point x in image 1, its corresponding point in image 2 must lie on a specific LINE (the epipolar line) defined by F·x. This reduces the 2D search for correspondences to a 1D search along a line.

ESSENTIAL MATRIX E:
If the camera intrinsic parameters (focal length, principal point) are known (calibrated cameras), we use the essential matrix E instead of F:
  E = K'ᵀ · F · K   (where K, K' are the camera calibration matrices)
E encodes only the rotation R and translation t between cameras: E = [t]×R

8-POINT ALGORITHM (to compute F from correspondences):
1. Collect at least 8 point correspondences (xᵢ ↔ x'ᵢ)
2. Stack them into matrix A where each row encodes x'ᵀFx = 0
3. Solve Af = 0 using SVD (f is the vectorised F)
4. Enforce rank-2 constraint by zeroing the smallest singular value of F
5. RANSAC wrapper: randomly sample 8 points, compute F, count inliers — repeat until a robust F is found

USES: Stereo depth estimation, structure-from-motion (SfM), 3D scene reconstruction.""",

    "MID2-Q09": """Block matching algorithms (BMAs) are the standard approach for motion estimation in video compression. They find, for each block in the current frame, where that block came from in the reference (previous) frame.

SETUP:
• Partition current frame into M×M blocks (usually 16×16)
• For each block, search a p×p region in the previous frame
• Match quality: SAD (Sum of Absolute Differences) — lower = better

FULL SEARCH (FS):
Exhaustively checks every candidate position in the (2p+1)×(2p+1) search window.
• For p=7: checks 15×15 = 225 positions per block
• Finds the GLOBAL MINIMUM SAD — highest quality motion vectors
• Complexity: O(N² × (2p+1)²) — too slow for real-time HD video

THREE-STEP SEARCH (TSS):
A hierarchical search strategy:
• Step 1: Check 9 points at spacing = p/2 around the block centre. Move to best point.
• Step 2: Check 9 points at spacing = p/4 around the new centre. Move to best point.
• Step 3: Check 9 points at 1-pixel spacing. Final answer.
• Total: 25 evaluations (vs 225 for full search) — 9× speedup
• Quality: finds optimal or near-optimal motion vectors 95–98% of the time

DIAMOND SEARCH (DS):
Uses two patterns — Large Diamond (9 points) and Small Diamond (5 points):
• Start with large diamond; if the minimum is at the centre, switch to small diamond
• Preferred for MPEG-4 and H.264 encoders — better handles typical camera motion (which is predominantly small displacements)""",

    "MID2-Q10": """Motion estimation in its most general form is a nonlinear optimisation problem: find the displacement vector u = (u, v) that minimises the photometric error (difference in brightness) between a region in frame t and frame t+1.

THE OBJECTIVE FUNCTION:
  E(u) = Σᵢ [I(xᵢ + u, yᵢ + v, t+1) − I(xᵢ, yᵢ, t)]²

This is nonlinear because the image intensities are not linear functions of the displacement.

THREE OPTIMISATION APPROACHES:

GRADIENT DESCENT:
  uₖ₊₁ = uₖ − α · ∇E(uₖ)
Takes small steps in the direction of steepest descent. Learning rate α must be tuned carefully — too large = oscillates, too small = very slow. Guaranteed to converge to a local minimum. Simple but inefficient.

GAUSS-NEWTON:
Approximates the nonlinear problem as locally linear by expanding around the current estimate. Update:
  δu = −(JᵀJ)⁻¹Jᵀr   (where J is the Jacobian of residuals r)
Converges quadratically near the solution — much faster than gradient descent. Can diverge if the initial estimate is far from the answer.

LEVENBERG-MARQUARDT (LM):
Combines GD and GN adaptively:
  (JᵀJ + λI)δu = Jᵀr
When λ is large → behaves like gradient descent (safe, far from solution). When λ is small → behaves like Gauss-Newton (fast, near solution). λ is adjusted automatically based on whether the error decreased. LM is the workhorse of nonlinear least-squares — robust and efficient.""",

    "MID2-Q11": """Transform-domain motion estimation works in the frequency domain rather than pixel domain — it matches DCT or DFT coefficients between frames instead of raw pixel values.

WHY BOTHER? In standard video compression (MPEG, H.264), frames are already being transformed to DCT for compression. Performing motion estimation in the DCT domain avoids the expensive IDCT → motion search → DCT round-trip, saving significant computation.

PHASE CORRELATION METHOD (using DFT):
Given two image patches A and B, their relative displacement d can be found using:
  Result = IFFT[ (F_A · F_B*) / |F_A · F_B*| ]

The normalised cross-power spectrum produces a sharp Dirac delta spike at the displacement location. The position of this spike IS the motion vector.

ADVANTAGES:
• Robust to additive noise (noise has random phase, cancels in the normalised cross-power)
• Robust to illumination changes (uniform illumination change affects DC component only)
• Can detect sub-pixel displacements and rotational motion
• Computationally efficient via FFT

DCT-DOMAIN BLOCK MATCHING:
For MPEG encoders: compare DCT coefficients directly (using modified SAD in DCT domain). Avoids full IDCT for rejected candidates — only IDCT the final winning block. Saves 30–40% encoding time vs. pixel-domain matching.

WAVELET-DOMAIN MATCHING: Work on wavelet coefficients — natural multi-resolution approach, similar to pyramid matching but in frequency bands.""",

    "MID2-Q12": """Structure-from-Motion (SfM) is a technique for reconstructing a 3D scene (the "structure") and recovering camera positions and orientations (the "motion") from a sequence of 2D images.

THE 8-STAGE PIPELINE:

STAGE 1 — FEATURE DETECTION: Find distinctive keypoints in every image using SIFT or ORB.

STAGE 2 — FEATURE MATCHING: Match keypoints between pairs of images based on descriptor similarity.

STAGE 3 — RANSAC OUTLIER REJECTION: Randomly sample 8 correspondences, compute the essential matrix E, count inliers (points that fit E). Repeat many times and keep the best E. Removes false matches (outliers).

STAGE 4 — ESSENTIAL MATRIX: Compute E = [t]×R from inlier correspondences using the 8-point algorithm.

STAGE 5 — RELATIVE POSE: Decompose E into rotation R and translation t between camera pairs. This gives the camera positions relative to each other.

STAGE 6 — TRIANGULATION: Given a 3D point seen from two camera positions, project rays from each camera centre through the image points. The 3D point is at the intersection (or closest approach) of these rays.

STAGE 7 — BUNDLE ADJUSTMENT: The global refinement step. Jointly optimise ALL camera poses and ALL 3D point positions to minimise the total reprojection error:
  E = Σᵢ Σⱼ ||xᵢⱼ − π(Pᵢ, Xⱼ)||²
This is solved with Levenberg-Marquardt. Without BA, errors accumulate and the reconstruction drifts.

STAGE 8 — DENSE RECONSTRUCTION: Use stereo matching or Multi-View Stereo (MVS) to densify the sparse point cloud into a full 3D mesh.""",

    # ── UNIT 5 ──────────────────────────────────────────────────────────────

    "MID2-Q13": """Image segmentation partitions an image into meaningful regions — separating objects from each other and from the background. For video, it must also be temporally consistent.

REGION-BASED METHODS — group pixels that share similar properties:

THRESHOLDING: Classify pixels as foreground if intensity > threshold T. Otsu's method automatically finds the optimal T by maximising inter-class variance. Simple and fast but only works for images with bimodal histograms.

REGION GROWING: Start from seed points, grow regions by adding adjacent pixels that are similar (within a colour/intensity tolerance). Sensitive to seed point selection and noise.

WATERSHED ALGORITHM: Treats the image as a topographic surface (bright = high, dark = low). "Floods" from regional minima simultaneously; where different floods meet, watershed boundaries are drawn. Powerful but over-segments noisy images → needs marker-controlled watershed.

BOUNDARY-BASED METHODS — find edges where properties change abruptly:

CANNY EDGE DETECTOR (5 steps):
1. Gaussian blur: σ ≈ 1.4 to suppress noise
2. Compute gradient magnitude and direction using Sobel
3. Non-maximum suppression: thin edges to 1-pixel-wide ridges
4. Double thresholding: pixels above T_high = strong edge, between T_high & T_low = weak edge, below T_low = not edge
5. Edge hysteresis: keep weak edges only if connected to a strong edge

COMBINED APPROACH: Canny edges act as barriers, constraining region growing to prevent "leaking" across boundaries. This hybrid approach is used in many practical video segmentation systems.""",

    "MID2-Q14": """Change detection is the process of identifying which regions of a video frame have changed relative to a reference — either the previous frame or a background model. It's the foundation of all video surveillance systems.

FRAME DIFFERENCING:
  D(x,y,t) = |I(x,y,t) − I(x,y,t−1)| > θ
Compares each frame to the immediately previous frame. Fast and simple. Detects any motion. Problems: double-contouring, misses slow/stopped objects, sensitive to camera shake.

BACKGROUND SUBTRACTION:
  D(x,y,t) = |I(x,y,t) − B(x,y)| > θ
Compares each frame to a maintained background model B. Far more robust than frame differencing — can detect even a stationary intruder (who entered and stopped). The challenge is keeping B accurate as lighting changes, shadows move, and backgrounds evolve.

CHALLENGES IN REAL SURVEILLANCE:
• ILLUMINATION CHANGES: Sunrise/sunset gradually shifts all pixel values → adaptive background model (MOG2) needed
• SHADOWS: Cast shadows have similar motion as foreground objects → use colour models or shadow-invariant features
• CAMERA JITTER: Wind-blown camera causes false positives → electronic image stabilisation (EIS) or stabilisation pre-processing
• CAMOUFLAGE: Objects with similar colour to background → multi-cue detection (colour + texture + motion)

MORPHOLOGICAL POST-PROCESSING: After thresholding, apply erosion (remove small noise blobs) then dilation (fill holes in detected regions) to clean up the binary mask.""",

    "MID2-Q15": """This is a direct numerical calculation using the change detection threshold rule.

GIVEN:
• Region A: SAD = 120
• Region B: SAD = 45
• Region C: SAD = 200
• Motion threshold: θ = 100

RULE: A region is classified as MOTION if its SAD > θ; it is classified as STATIC if SAD ≤ θ.

APPLYING THE RULE:
• Region A: SAD = 120 > 100 → MOTION detected ✓
• Region B: SAD = 45 ≤ 100 → NO MOTION (static background) ✗
• Region C: SAD = 200 > 100 → MOTION detected ✓

ANSWERS:
1. Regions containing motion: A and C
2. Region without motion: B (SAD=45, well below threshold)
3. Most dominant motion: Region C — it has the highest SAD value (200), indicating the largest amount of pixel change, suggesting the fastest-moving or most rapidly changing region.

INTERPRETATION: Region B with SAD=45 is clearly static background. Region A is moderately active (120). Region C (200) is the primary area of interest for surveillance — highest priority alert region.""",

    "MID2-Q16": """Motion tracking follows a specific object (person, vehicle, ball) across multiple video frames, recording where it is at each moment in time.

THE TRAJECTORY:
  T = {P₁, P₂, P₃, ..., Pₖ}
where Pₜ = (x,y) is the centroid of the tracked object at frame t. The trajectory is the ordered history of positions over time.

HOW TRACKING WORKS — Key approaches:

OPTICAL FLOW TRACKING (LK-based):
Select feature points on the object (e.g., Harris corners). Use Lucas-Kanade optical flow to find where each feature moved in the next frame. The object centroid is the average of all tracked feature positions.

DETECTION-BASED TRACKING:
Run an object detector (Haar cascade, YOLO, background subtraction) on each frame to get bounding boxes. Associate detections to existing tracks using the HUNGARIAN ALGORITHM (minimum-cost bipartite matching based on IoU or distance). Creates a new track for unmatched detections, terminates tracks with no detection for N frames.

KALMAN FILTER INTEGRATION:
Between frames, the Kalman filter PREDICTS where the object will be next based on its velocity model. When a detection arrives, it UPDATES the estimate. This handles frames where the detector fails (occlusion, blur) — the Kalman keeps predicting a smooth trajectory through the gap. Without Kalman, tracks break every time detection fails.

TRAJECTORY SMOOTHING: Apply a moving average or spline interpolation to remove jitter from the centroid sequence.""",

    "MID2-Q17": """Video/image matting is the process of precisely separating a foreground subject (person, object) from its background, pixel by pixel, including semi-transparent regions like hair strands, glass, and motion blur.

THE COMPOSITING EQUATION:
  I(x,y) = α(x,y) · F(x,y) + (1 − α(x,y)) · B(x,y)
• I = composite image (what we see)
• F = foreground colour
• B = background colour
• α ∈ [0,1] = alpha matte (0 = fully background, 1 = fully foreground)

The goal: given only I and B (or just I), estimate both α and F.

TYPES OF MATTING:

TRIMAP-BASED: User provides a trimap — an image manually labelled as "definitely foreground", "definitely background", and "unknown". The algorithm only needs to solve for α in the unknown region. Closed-Form Matting uses local colour statistics to solve for α analytically.

DEEP LEARNING MATTING (IndexNet, MODNet, BackgroundMattingV2):
Directly predict α from a single image using neural networks. No trimap needed. Can run in real time (video conferencing backgrounds in Zoom/Meet use this). Trained on large datasets of RGBA images with known alpha mattes.

VIDEO MATTING CHALLENGE — TEMPORAL CONSISTENCY:
Frame-by-frame matting produces flickering α values at hair edges. Solution: enforce temporal smoothness using optical flow — warp the previous frame's α into the current frame as an initialisation constraint. This keeps hair edges stable and flicker-free across frames.""",

    "MID2-Q18": """PART A — Particle Filter Analysis:

A particle filter represents the probability distribution of the tracked object's state using N "particles" (hypotheses), each with a weight indicating how likely that hypothesis is.

Given particle weights: [0.2, 0.3, 0.1, 0.4]

CHECK IF NORMALISED: Sum = 0.2 + 0.3 + 0.1 + 0.4 = 1.0 ✓ Already normalised.

MOST LIKELY PARTICLE: Particle 4 with weight 0.4 — it has the highest probability and represents the best current hypothesis for where the object is.

WHY THIS IMPROVES TRACKING: Particle filters maintain MULTIPLE hypotheses simultaneously. When an object passes behind an obstacle (occlusion), traditional trackers lose it. Particle filters keep hypotheses for all plausible positions — when the object reappears, particles near its true position get high weights and dominate the estimate.

PART B — Kalman Filter Update:

Given: Predicted position x̂⁻ = 50, Measurement z = 60, Kalman gain K = 0.6

UPDATE EQUATION: x̂ = x̂⁻ + K·(z − x̂⁻)
  x̂ = 50 + 0.6·(60 − 50)
  x̂ = 50 + 0.6 × 10
  x̂ = 50 + 6 = 56

INTERPRETATION OF KALMAN GAIN K=0.6:
The updated estimate (56) is 60% pulled toward the measurement (60) and 40% stays near the prediction (50). K=0.6 means we trust the sensor more than the motion model. If K were 0.1, the estimate would stay at 51 (mostly ignoring the measurement).""",

    "MID2-Q19": """A complete video segmentation and tracking framework integrates multiple algorithms into a pipeline that can follow multiple objects simultaneously, even through occlusions.

THE 9-STAGE PIPELINE:

1. FRAME INPUT: Receive new video frame Iₜ
2. CHANGE DETECTION: Compute |Iₜ − Iₜ₋₁| > θ to flag active regions
3. BACKGROUND SUBTRACTION: MOG2 model produces binary foreground mask
4. MORPHOLOGICAL CLEANUP: Erosion removes noise pixels, dilation fills object holes, closing bridges small gaps
5. CONTOUR EXTRACTION: OpenCV findContours() extracts object boundaries from the binary mask
6. OPTICAL FLOW ESTIMATION: LK flow computed at detected keypoints to get per-pixel velocity vectors within each detected region
7. KALMAN PREDICT: For each active track, predict the next state: x̂ₖ⁻ = Ax̂ₖ₋₁
8. DATA ASSOCIATION + UPDATE: Hungarian algorithm matches new detections to existing Kalman tracks (by IoU overlap). Update matched tracks: x̂ₖ = x̂ₖ⁻ + K(z−Hx̂ₖ⁻). Create new tracks for unmatched detections. Terminate tracks with no detection for T frames.
9. TRAJECTORY UPDATE: Append new centroid to each track's trajectory

HOW MOTION ANALYSIS IMPROVES TRACKING: When two objects cross paths and occlude each other, optical flow provides velocity vectors for each track individually — the system predicts each track's trajectory independently through the occlusion gap, preventing ID swaps when they re-emerge.""",

    "MID2-Q20": """To evaluate how well a tracking or segmentation algorithm performs, we compare its output against ground truth (manually annotated bounding boxes or segmentation masks) using a standard set of metrics.

THE CONFUSION MATRIX — classifying every pixel/detection:
• TP (True Positive): correctly detected foreground/object
• FP (False Positive): detector says object, but it's background (false alarm)
• FN (False Negative): missed object (missed detection)
• TN (True Negative): correctly identified background

THE 4 KEY METRICS:

PRECISION = TP / (TP + FP)
"Of all the regions we detected, what fraction were real?"
High precision = few false alarms. Low precision = lots of false alarms.

RECALL = TP / (TP + FN)
"Of all the real objects, what fraction did we find?"
High recall = very few misses. Low recall = many objects missed.

F1-SCORE = 2 × Precision × Recall / (Precision + Recall)
Harmonic mean of Precision and Recall. Balances both — a system that finds everything (Recall=1) but also flags everything (Precision=low) gets a poor F1. The best F1=1.0 means perfect precision AND perfect recall.

IoU (INTERSECTION over UNION) = TP / (TP + FP + FN)
"What fraction of the total covered area (detected + ground truth combined) actually overlaps?"
IoU = 1.0 means perfect overlap. IoU = 0.5 is typically the threshold for "correct detection" in PASCAL VOC evaluation.

EXAMPLE: If you detect a bounding box that overlaps 75% with the ground truth box → IoU ≈ 0.75 → counted as a correct detection (since 0.75 > 0.5).""",
}
