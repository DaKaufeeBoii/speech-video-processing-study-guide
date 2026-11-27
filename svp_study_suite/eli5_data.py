# -*- coding: utf-8 -*-
"""
Ultra-Simple (ELI5 - Explain Like I'm 5) Master Solutions for all 40 SVP Questions.
Formatted as 3 high-impact, zero-jargon bullets:
1. In Plain English (The concept in human words)
2. Magic Exam Keywords (The specific technical words that grant marks)
3. What to Draw / Write (The exact visual structure examiners look for)
"""

ELI5_DATA = {
    # --- UNIT 1 (Mid-I Q1-Q8) ---
    'MID1-Q01': {
        'plain': "Human speech is made like a trumpet: lungs and vocal cords make raw buzzy sound, and the mouth/throat tubes shape it into words.",
        'keywords': "Source-Filter Model, Gunnar Fant, Glottis/Vocal Cords, Fundamental Frequency (F0), Vocal Tract acoustic tube (17.5 cm), Formants (F1, F2, F3), S(z) = E(z)·H(z)·R(z)",
        'draw': "Flowchart: Lungs -> Glottis (Source E(z)) -> Vocal Tract Filter H(z) -> Lip Radiation R(z) -> Speech s(t)"
    },
    'MID1-Q02': {
        'plain': "Converting smooth sound into computer numbers by snapping photos of the wave at regular intervals, which must be twice the fastest frequency or sound gets ruined.",
        'keywords': "Uniform Sampling (Ts = 1/fs), Nyquist Rate (fs >= 2·fmax), Aliasing Distortion, Anti-Aliasing Low-Pass Filter, Sinc Interpolation Reconstruction, 8 kHz Telephone, 16 kHz ASR",
        'draw': "Block diagram: s(t) -> Anti-Aliasing LPF -> Sampler (fs) -> s[n] -> D/A Converter -> Sinc Reconstruction LPF -> s(t)"
    },
    'MID1-Q03': {
        'plain': "Solving numerator gives zeros (quiet dips); solving denominator gives poles (resonances); if all poles stay inside the circle of radius 1, sound stays stable.",
        'keywords': "Transfer Function H(z) = N(z)/D(z), Zeros (N(z)=0: z=0, 0.5), Poles (D(z)=0: p=0.5, 0.4), BIBO Stability (|p| < 1), Unit Circle, Vocal Tract Resonances (Formants)",
        'draw': "Complex z-plane circle of radius 1, showing poles (x) at 0.5 and 0.4 strictly inside the circle, and zeros (o) at 0 and 0.5"
    },
    'MID1-Q04': {
        'plain': "A high-speed prism that splits complex audio waves into individual rainbow frequency colors in a millisecond.",
        'keywords': "Cooley-Tukey algorithm, O(N log N) speedup, Conjugate Symmetry (Hermitian), Time-Shift phase invariance, Frequency Resolution (Δf = fs/N), Parseval's Energy Conservation, Windowing",
        'draw': "Box: Speech frame x[n] -> Hamming Window -> FFT -> Complex X[k] splitting into Magnitude |X[k]| (Spectrogram) and Phase ∠X[k]"
    },
    'MID1-Q05': {
        'plain': "Mathematically blending two signals together: glottal pulses sliding through vocal tract filters to create speech sound.",
        'keywords': "Discrete Convolution y[n] = x[n] * h[n], Flip-Shift-Multiply-Sum, Source-Filter cascade, Linear vs Circular Convolution, Overlap-Add (OLA), Overlap-Save (OLS), Pre-emphasis filter",
        'draw': "Impulse train e[n] entering Vocal Tract LTI System h[n] to produce speech s[n] = e[n] * h[n], plus Overlap-Add block diagram"
    },
    'MID1-Q06': {
        'plain': "Linear filters give equal spacing everywhere like a ruler; Mel filters give lots of detail to low pitches and bundle high pitches together, just like human ears.",
        'keywords': "Linear Filter Bank (Uniform STFT, constant Δf), Non-linear Mel Filter Bank (Mel(f) = 2595 log10(1 + f/700)), Human Cochlea tonotopy, Critical Bands, Formants F1/F2 resolution",
        'draw': "Two graphs: 1. Uniformly spaced rectangles (Linear); 2. Overlapping triangles that are narrow at low Hz and widen logarithmically at high Hz (Mel scale)"
    },
    'MID1-Q07': {
        'plain': "Part A: Multiplying 4 numbers by the twiddle factor matrix to get frequency energy. Part B: Dividing 8000 Hz by 256 samples gives 31.25 Hz per bar, so bin 10 is 312.5 Hz.",
        'keywords': "4-Point DFT, Twiddle Matrix W4 (1, -j, -1, j), Magnitude Spectrum |X[k]|, Dominant AC Component, Frequency Resolution Δf = fs/N = 31.25 Hz, fk = k·Δf = 312.5 Hz",
        'draw': "Matrix multiplication: [W4] · [2, 1, 0, 1]^T = [4, 2, 0, 2]^T, with frequency bar chart showing peak at DC (4) and AC peaks at k=1, 3"
    },
    'MID1-Q08': {
        'plain': "Predicting the next audio sample as a weighted sum of the last 10 samples, compressing voice data 26 times into tiny parameters.",
        'keywords': "All-pole model H(z) = G / (1 - Σ ak z^-k), Autoregressive prediction, Mean Squared Error minimization, Yule-Walker Normal Equations, Toeplitz Matrix, Levinson-Durbin recursion (O(p^2))",
        'draw': "Block diagram: Speech s[n] compared against LPC Predictor ak to produce Error e[n]; Synthesis filter 1/A(z) excited by pitch pulses"
    },

    # --- UNIT 2 (Mid-I Q9-Q16) ---
    'MID1-Q09': {
        'plain': "The 7-step recipe that converts raw microphone recordings into compact acoustic feature vectors for speech AI.",
        'keywords': "Pre-emphasis (1 - 0.97z^-1), Frame Blocking (20-30 ms), Hamming Windowing (prevents leakage), FFT, Mel-scale Filter Bank (26-40 filters), Log Compression, DCT-II decorrelation",
        'draw': "Sequential vertical pipe: Raw Audio -> Pre-emphasis -> Framing -> Hamming Window -> FFT -> Mel Filterbank -> Log -> DCT -> 39D Vector"
    },
    'MID1-Q10': {
        'plain': "Static features are a photo of the mouth shape right now (13 numbers); dynamic features are the speed and acceleration of the mouth moving between sounds (26 numbers).",
        'keywords': "Static MFCCs (13-D instantaneous posture), Delta / Velocity (13-D Δc), Delta-Delta / Acceleration (13-D ΔΔc), 39-Dimensional Feature Vector, Co-articulation, Regression formula",
        'draw': "Timeline of frames: Frame t gives Static c(t); arrows from neighbors t-1, t+1 give Delta Δc(t); combined into 39-D vector [c | Δc | ΔΔc]"
    },
    'MID1-Q11': {
        'plain': "With 1600 total samples, taking 400 at a time and jumping forward by 200 each step fits exactly 7 frames.",
        'keywords': "Total Samples L = 1600, Window Size N = 400, Overlap M = 200, Hop Size R = N - M = 200, Formula K = floor((L - N)/R) + 1 = floor(1200/200) + 1 = 7 frames",
        'draw': "Timeline ruler from 0 to 1600 showing 7 overlapping bars sliding by 200 samples each: Frame 1 (0-399) to Frame 7 (1200-1599)"
    },
    'MID1-Q12': {
        'plain': "LPCC models speech like a rigid mathematical pipe (breaks when noisy); MFCC models speech like the human ear (super robust to noise and world standard).",
        'keywords': "LPCC (Linear Prediction Cepstrum, all-pole model, noise-sensitive, no zeros), MFCC (Mel-Frequency Cepstrum, cochlear auditory filters, noise-robust, DCT decorrelation, ASR standard)",
        'draw': "Comparison table: LPCC (Acoustic Tube -> LPC -> Recursive Cepstrum) vs MFCC (Cochlea -> Mel Filterbank -> DCT)"
    },
    'MID1-Q13': {
        'plain': "Euclidean measures straight lines; Mahalanobis scales by feature spread; DTW warps time on a grid to match fast and slow speakers.",
        'keywords': "Euclidean distance (spherical, unweighted), Mahalanobis distance (inverse covariance Σ^-1 weighting), Dynamic Time Warping (DTW), Dynamic Programming grid D(i,j), Non-linear temporal alignment",
        'draw': "DTW grid (N x M) with non-linear warping path connecting bottom-left (1, 1) to top-right (N, M), constrained by Sakoe-Chiba band"
    },
    'MID1-Q14': {
        'plain': "Grouping thousands of speech sounds into a dictionary of 256 code words using the LBG algorithm so voice files shrink drastically.",
        'keywords': "Vector Quantization (VQ), Codebook (K=64-256), Codevectors, Voronoi Partitions, Linde-Buzo-Gray (LBG) algorithm, Centroid Splitting (±ε), Distortion minimization",
        'draw': "Voronoi tessellation diagram with 2D feature plane divided into polygon cells, each containing a central codevector dot y_k"
    },
    'MID1-Q15': {
        'plain': "Representing complex voice data as a blend of several bell curves (Gaussians); the EM algorithm tweaks weights, centers, and widths until the fit is perfect.",
        'keywords': "Gaussian Mixture Model (GMM), Mixture Weights (wm), Mean Vectors (μm), Covariance Matrices (Σm), Expectation-Maximization (EM), E-Step (Responsibilities γm), M-Step (Updates)",
        'draw': "A multi-modal curve made of 3 dashed Gaussian bell curves summing into one solid multi-peak probability envelope, alongside the EM loop"
    },
    'MID1-Q16': {
        'plain': "A statistical machine with hidden mouth states moving left-to-right that emit speech sounds over time; handles fast and slow talkers effortlessly.",
        'keywords': "Hidden Markov Model (HMM), Left-to-Right Bakis Topology, Hidden States (Onset, Nucleus, Coda), Transition Matrix A, Emission Distributions B, Forward Algorithm, Viterbi Algorithm, Baum-Welch",
        'draw': "3-state left-to-right chain (State 1 -> State 2 -> State 3) with self-loops a_ii and forward transitions a_ij, each state emitting acoustic vector o(t)"
    },

    # --- UNIT 3 (Mid-I Q17-Q20 & Mid-II Q1-Q4) ---
    'MID1-Q17': {
        'plain': "Signals with 2 or more coordinates: photos have (x,y), videos have (x,y,time), and MRI scans have (x,y,z); pixels are heavily correlated in all directions.",
        'keywords': "Multi-Dimensional Signals, 2D Still Images f(x, y), 3D Video f(x, y, t), 3D Volumetric CT/MRI f(x, y, z), Spatial/Temporal Correlation, Non-Causality, High Bandwidth (Gbps)",
        'draw': "Stacked diagrams: 1D wave s(t), 2D grid f(x,y), and 3D cube of video frames moving along time t"
    },
    'MID1-Q18': {
        'plain': "2D-DFT splits an image into horizontal and vertical wave ripples; can be computed by doing 1D-FFT on all rows, then on all columns.",
        'keywords': "2D-DFT, Row-Column Separability (O(MN log MN)), DC Component F(0,0) (Average Brightness), Spatial Frequency Axes, Horizontal/Vertical Edge Orientation, Low-pass blurring, High-pass edges",
        'draw': "Square 2D spectrum with DC bright spot at center (0,0), horizontal axis u (vertical edges), and vertical axis v (horizontal edges)"
    },
    'MID1-Q19': {
        'plain': "A 2D filter slides a small kernel over an image like a magnifying glass; in frequency space, this is just multiplying two matrices.",
        'keywords': "2D LSI System, 2D Unit Impulse Response / Point Spread Function (PSF h[m,n]), 2D Discrete Convolution, 2D Z-Transform, Frequency Response H(ω1, ω2), Separable 2D Filter (O(2K) vs O(K^2))",
        'draw': "2D image x[m,n] being convolved with 3x3 kernel h[m,n] to produce output y[m,n], alongside separable row-then-column filtering diagram"
    },
    'MID1-Q20': {
        'plain': "The JPEG/MPEG machine: chop image into 8x8 squares, run 2D-DCT to pack energy into corners, throw away invisible high frequencies, and zip-compress.",
        'keywords': "Image Compression Pipeline, YCbCr 4:2:0 subsampling, 8x8 Block Partitioning, 2D-DCT-II (Energy Compaction, no boundary discontinuity), Psychovisual Quantization Q(u,v), Zig-zag scan, Huffman/CABAC",
        'draw': "End-to-end flowchart: RGB -> YCbCr -> 8x8 Block -> 2D-DCT -> Quantization -> Zig-zag scan -> Huffman coding -> Bitstream"
    },
    'MID2-Q01': {
        'plain': "Sampling images on a grid: pixels can be laid out in squares or hexagons; sampling rate must be twice the highest spatial frequency to avoid wavy moiré patterns.",
        'keywords': "Multi-Dimensional Sampling, Sampling Lattice Matrix V, Rectangular Lattice vs Hexagonal Lattice (saves 13.4% samples), Reciprocal Lattice U, 2D Nyquist Criterion (fsx >= 2·fmax,x), Moiré Aliasing",
        'draw': "Two pixel grids: Rectangular grid (square dots) and Hexagonal grid (staggered honeycomb dots), with overlapping spectral circles illustrating 2D aliasing"
    },
    'MID2-Q02': {
        'plain': "Take 8x8 pixel blocks, convert them to frequencies via DCT, throw away fine textures with quantization, and compress the remaining numbers into a small file.",
        'keywords': "Block Partitioning (8x8), 2D-DCT (decorrelation & energy compaction), Quantization Matrix (lossy step based on HVS), Zig-Zag Scan (groups zeros), Entropy Coding (lossless Huffman)",
        'draw': "Flowchart: 8x8 Block -> 2D-DCT -> Quantization Matrix -> Zig-Zag Serialization -> Run-Length & Huffman Encoding"
    },
    'MID2-Q03': {
        'plain': "Human eyes are sharp for black-and-white brightness but fuzzy for colors, and blind to very fine patterns, letting us throw away 70% of image data safely.",
        'keywords': "Human Visual System (HVS), Rods vs Cones, Luminance vs Chrominance Sensitivity, YCbCr 4:2:0 Chroma Subsampling (50% saving), Weber-Fechner Law (logarithmic brightness), Contrast Sensitivity Function (CSF)",
        'draw': "HVS CSF curve peaking at 3-5 cycles/degree and dropping sharply at high frequencies, paired with RGB to YCbCr 4:2:0 color subsampling diagram"
    },
    'MID2-Q04': {
        'plain': "How MP4 video works: capture progressive frames, compress color to 4:2:0, and store only 1 full photo (I-frame) followed by motion-predicted sticky notes (P/B frames).",
        'keywords': "Digital Video System, Progressive Scanning (no interlace comb artifacts), YCbCr 4:2:0 (12 bpp), Group of Pictures (GOP), I-Frames (Intra), P-Frames (Forward predicted), B-Frames (Bi-directional), Motion Vectors",
        'draw': "Timeline of GOP frames: I ──► P ──► P with arrows pointing to B-frames in between, showing forward and backward prediction arrows"
    },

    # --- UNIT 4 (Mid-II Q5-Q12) ---
    'MID2-Q05': {
        'plain': "Geometric projection shrinks distant objects (3D to 2D); photometric illumination determines pixel brightness; motion estimation must separate real motion from lighting changes.",
        'keywords': "Image Formation Model, Geometric Projection (Pinhole x=fX/Z, y=fY/Z), Motion Parallax, Photometric Model (Illumination L × Reflectance R), Brightness Constancy, Camera Intrinsics/Extrinsics",
        'draw': "Pinhole camera model showing 3D point P(X, Y, Z) projecting through pinhole lens onto 2D image plane at (x, y)"
    },
    'MID2-Q06': {
        'plain': "Translational motion just shifts (2 parameters); Affine also rotates and zooms (6 parameters); Homography handles full 3D tilting (8 parameters).",
        'keywords': "Translational Model (2 DOF [dx, dy]), Affine Model (6 DOF: translation, rotation, scale, shear), Projective / Homography (8 DOF), Brightness Constancy (I(t+dt)=I(t)), Small Motion, Spatial Coherence",
        'draw': "Three transformed squares: 1. Translated box; 2. Rotated/sheared affine parallelogram; 3. Perspective trapezoid (homography)"
    },
    'MID2-Q07': {
        'plain': "From (20, 25) to (23, 30): Displacement is dx = 23-20 = +3, dy = 30-25 = +5; distance is √(3²+5²) = 5.83 pixels; direction is down-right at 59.04°.",
        'keywords': "Block Motion Estimation, Displacement Vector d = (Δx, Δy) = (3, 5), Magnitude ||d|| = √(3² + 5²) = √34 ≈ 5.83 pixels, Direction θ = arctan(5/3) ≈ 59.04°, Downward-Rightward motion",
        'draw': "Coordinate plot: Starting block at (20, 25) with an arrow pointing to best match at (23, 30), labeled dx=+3, dy=+5, θ=59.04°"
    },
    'MID2-Q08': {
        'plain': "Using brightness slope (gradients) to find pixel speed; looking through a small aperture hides parallel motion; Lucas-Kanade solves it in small windows.",
        'keywords': "Optical Flow Constraint Equation (Ix·u + Iy·v + It = 0), Aperture Problem (1 eq, 2 unknowns), Lucas-Kanade (local least squares (A^T A)^-1 A^T b), Horn-Schunck (global smoothness PDE), Noise sensitivity",
        'draw': "Aperture problem sketch: A straight edge moving diagonally seen through a circular hole appears to move only perpendicularly to the edge"
    },
    'MID2-Q09': {
        'plain': "Finding where a block moved: Full Search checks all 225 spots (slow but perfect); Three-Step Search checks 25 spots (9 times faster with almost the same quality).",
        'keywords': "Block Matching Algorithm (BMA), Matching Criteria (SAD/MAD, MSE), Full Search (O((2p+1)^2)), Three-Step Search (TSS, 25 points), Diamond Search, Computational Complexity vs Accuracy trade-off",
        'draw': "TSS 3-stage search grid: 8 points at step 4 around center, then 8 points at step 2, then 8 points at step 1, converging on target"
    },
    'MID2-Q10': {
        'plain': "Finding the best motion parameters using math optimization: Levenberg-Marquardt automatically blends safe small steps with fast giant leaps.",
        'keywords': "Nonlinear Optimization, Sum of Squared Residuals min ||r(p)||^2, Gradient Descent (linear, slow), Gauss-Newton (quadratic, unstable), Levenberg-Marquardt (adaptive damping λ), Gaussian Pyramids",
        'draw': "Error bowl surface showing Gradient descent taking small zigzag steps, Gauss-Newton taking a direct jump, and coarse-to-fine Gaussian pyramid"
    },
    'MID2-Q11': {
        'plain': "Transforming two frames with 2D-FFT and dividing their phases produces a single razor-sharp laser spike pointing to the exact motion offset.",
        'keywords': "Phase Correlation, Fourier Shift Theorem (F2 = F1·e^-j2π(ux0+vy0)), Normalized Cross-Power Spectrum R(u,v), Inverse FFT Dirac Delta Peak δ(x-x0, y-y0), Sub-pixel interpolation, Illumination invariance",
        'draw': "Flowchart: Frame 1 & 2 -> 2D-FFT -> Cross-Power Spectrum R(u,v) -> Inverse 2D-FFT -> 3D surface plot showing a sharp needle spike at displacement (x0, y0)"
    },
    'MID2-Q12': {
        'plain': "Reconstructing a 3D world from video photos: match feature points, compute camera angles via the Essential Matrix, triangulate 3D points, and polish the 3D model.",
        'keywords': "Structure from Motion (SfM), Epipolar Geometry, Essential Matrix (E = [t]× R, 5 DOF), Fundamental Matrix F, Eight-Point SVD Algorithm, RANSAC outlier rejection, Triangulation, Bundle Adjustment",
        'draw': "Two cameras looking at 3D point P with epipolar rays intersecting, plus the SfM pipeline flowchart (Features -> RANSAC -> E matrix -> 3D Point Cloud -> Bundle Adjustment)"
    },

    # --- UNIT 5 (Mid-II Q13-Q20) ---
    'MID2-Q13': {
        'plain': "Chopping an image into objects: Region methods group pixels that look alike (color/texture); Boundary methods draw lines where color changes abruptly (edges/snakes).",
        'keywords': "Image Segmentation, Region-Based (Homogeneity, Seeded Region Growing, Quadtree Split-and-Merge), Boundary-Based (Discontinuity, Sobel/Canny Gradients, Active Contours/Snakes, Hough Transform)",
        'draw': "Side-by-side comparison: Region growing spreading outward from a seed dot vs Boundary snake contracting around an object edge"
    },
    'MID2-Q14': {
        'plain': "Spotting motion by subtracting the background: simple frame difference creates hollow ghost holes; Mixture of Gaussians (MoG) models moving trees and shadows cleanly.",
        'keywords': "Change Detection, Temporal Differencing (ghosting/aperture holes), Background Subtraction (|I - B| > T), Running Average, Mixture of Gaussians (MoG / Stauffer-Grimson), Multimodal backgrounds, Shadow suppression",
        'draw': "Current frame minus Background frame passing through a threshold T to yield a clean binary silhouette mask of a moving pedestrian"
    },
    'MID2-Q15': {
        'plain': "Compare SAD against 100: Region A (120 > 100) and Region C (200 > 100) have motion; Region B (45 <= 100) is static; Region C has the most motion (SAD 200).",
        'keywords': "Global Motion Detection, Sum of Absolute Differences (SAD), Threshold T = 100, Condition (SAD > T -> Motion), Region A (120) & Region C (200) Active, Region B (45) Static, Region C Dominant (Max SAD = 200)",
        'draw': "Bar chart of Regions A (120), B (45), and C (200) with a horizontal dashed threshold line at 100; bars A and C rise above line, C is highest"
    },
    'MID2-Q16': {
        'plain': "Following a moving object across video: Point tracking uses Kalman filters; Mean-Shift climbs the color hill to keep the bounding box centered on the target.",
        'keywords': "Visual Motion Tracking, Point Tracking (Kalman Filter, state [x, y, vx, vy]^T), Kernel / Appearance Tracking (Mean-Shift & CamShift, Bhattacharyya coefficient, color histogram), Silhouette Tracking, Trajectory",
        'draw': "Mean-Shift vector climbing a 2D color density peak, accompanied by a multi-frame video trajectory curve connecting bounding box centroids"
    },
    'MID2-Q17': {
        'plain': "Extracting semi-transparent details like flying hair or smoke: solving I = αF + (1-α)B using a Trimap (known foreground, known background, and unknown blending band).",
        'keywords': "Digital Image Matting, Fundamental Matting Equation (I = αF + (1-α)B, 3 equations vs 7 unknowns), Alpha Matte α ∈ [0, 1], Trimap (Foreground α=1, Background α=0, Unknown 0<α<1), Levin Closed-Form Laplacian, Deep Matting",
        'draw': "Trimap diagram with 3 zones: White inner foreground (α=1), Black outer background (α=0), and Gray fuzzy boundary band (0<α<1)"
    },
    'MID2-Q18': {
        'plain': "Part A: Sum of [0.2, 0.3, 0.1, 0.4] is 1.0, so Particle 4 is most likely at 40%. Part B: Prediction is 50, sensor says 60; with gain 0.6, state moves 60% toward 60, landing at 56.",
        'keywords': "Particle Filter Weight Normalization (Σw=1.0, w~=[0.2,0.3,0.1,0.4], Most Likely Particle 4 at 40%, Multimodal robustness), Kalman Filter State Update (x = x^- + K(z - x^-) = 50 + 0.6(10) = 56, Innovation +10, 60% sensor trust)",
        'draw': "Two diagrams: 1. Bar graph of 4 normalized particle weights with Particle 4 highlighted; 2. Kalman update ruler showing prior 50 pulled to 56 toward measurement 60"
    },
    'MID2-Q19': {
        'plain': "Building a real-time self-driving vision pipeline: MoG finds moving cars, morphological filters clean the blobs, Hungarian algorithm assigns track IDs, and Kalman filters smooth paths.",
        'keywords': "Real-Time Tracking Framework, Spatio-Temporal Preprocessing, MoG2 Background Subtraction, Morphological Opening/Closing, Feature Extraction (Bounding Box, HSV Hist, Deep Re-ID), Hungarian Algorithm, Kalman Filtering, Track Life-Cycle",
        'draw': "Complete multi-stage pipeline flowchart: Camera -> Preprocess -> MoG2 -> Morphology -> Feature Extraction -> Hungarian Association -> Kalman State Filter -> Track Manager -> Analytics"
    },
    'MID2-Q20': {
        'plain': "Grading video AI: IoU measures mask overlap; Precision measures purity (no false alarms); Recall measures completeness (no misses); F1 is the balanced grade.",
        'keywords': "Performance Evaluation, Confusion Matrix (TP, FP, FN, TN), Intersection over Union (IoU = TP/(TP+FP+FN)), Precision (TP/(TP+FP)), Recall (TP/(TP+FN)), F1-Score (2PR/(P+R))",
        'draw': "Venn diagram of Prediction vs Ground Truth showing TP overlap, FP, and FN regions, with worked numerical formulas (IoU=66.7%, P=80.0%, R=80.0%, F1=80.0%)"
    }
}
