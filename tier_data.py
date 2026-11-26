# -*- coding: utf-8 -*-
"""
Priority Tiers, Difficulty, Time-to-learn, and Global Cramming Ranks (1-40)
for all 40 Speech and Video Processing (SVP) Examination Questions.
"""

QUESTION_TIER_DATA = {
    # --- TIER 1: Free Marks (High Priority / Easy to Learn / Guaranteed Score) ---
    'MID2-Q07': {'rank': 1, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '2 min', 'prio': 'Top', 'reason': 'Pure numerical: Block motion vector d=(3,5), mag=5.83, direction=59.04°'},
    'MID2-Q15': {'rank': 2, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '2 min', 'prio': 'Top', 'reason': 'Pure numerical: SAD thresholding (120,45,200 vs 100 -> A & C active, C dominant)'},
    'MID1-Q11': {'rank': 3, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '2 min', 'prio': 'Top', 'reason': 'Pure numerical: 1600 samples, 400 window, 200 overlap -> exactly 7 frames'},
    'MID2-Q18': {'rank': 4, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '4 min', 'prio': 'Top', 'reason': 'Double numerical: Particle weights [0.2,0.3,0.1,0.4] & Kalman state update 50+0.6(10)=56'},
    'MID1-Q03': {'rank': 5, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '3 min', 'prio': 'Top', 'reason': 'Pole-Zero numerical: zeros at 0, 0.5; poles at 0.5, 0.4; stable since |p| < 1'},
    'MID1-Q01': {'rank': 6, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '4 min', 'prio': 'High', 'reason': 'Fundamental definition: Gunnar Fant Source-Filter Model with 4-box diagram'},
    'MID1-Q12': {'rank': 7, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '4 min', 'prio': 'High', 'reason': 'Crisp comparison table: LPCC (all-pole tube) vs MFCC (human cochlea)'},
    'MID1-Q10': {'rank': 8, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '4 min', 'prio': 'High', 'reason': 'High-scoring concept: 13 static + 13 delta + 13 delta-delta = 39D vector'},
    'MID2-Q13': {'rank': 9, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '4 min', 'prio': 'High', 'reason': 'Classic classification: Region-based (growing, split-merge) vs Boundary-based (Canny, snakes)'},
    'MID2-Q02': {'rank': 10, 'tier': 1, 'tier_name': 'Free Marks', 'diff': 'Easy', 'time': '4 min', 'prio': 'High', 'reason': 'Clean 5-box flowchart: Partition -> 2D-DCT -> Quantize -> Zig-zag -> Entropy code'},

    # --- TIER 2: Core Scoring (Core Concepts, Algorithms & Medium Derivations) ---
    'MID1-Q07': {'rank': 11, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '6 min', 'prio': 'High', 'reason': 'High-yield numerical: 4-Point DFT twiddle matrix + Frequency resolution fs/N = 31.25 Hz'},
    'MID1-Q04': {'rank': 12, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'High', 'reason': '6 key FFT properties in speech: Linearity, Symmetry, Time-shift, Parseval'},
    'MID1-Q09': {'rank': 13, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'High', 'reason': 'Standard 7-stage speech feature extraction pipeline flowchart'},
    'MID1-Q02': {'rank': 14, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Sampling theorem, Nyquist rate fs >= 2fmax, and anti-aliasing sinc reconstruction'},
    'MID2-Q14': {'rank': 15, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Change detection: Frame differencing vs Background subtraction vs MoG model'},
    'MID2-Q06': {'rank': 16, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Motion models: Translational (2 DOF), Affine (6 DOF), Homography (8 DOF)'},
    'MID2-Q05': {'rank': 17, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Geometric projection (pinhole x=fX/Z) vs Photometric illumination-reflectance'},
    'MID2-Q08': {'rank': 18, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Optical flow equation Ix·u + Iy·v + It = 0, Aperture problem, Lucas-Kanade vs Horn-Schunck'},
    'MID1-Q17': {'rank': 19, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Multi-D signals taxonomy: 2D image f(x,y), 3D video f(x,y,t), 3D volumetric CT'},
    'MID2-Q16': {'rank': 20, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Tracking taxonomy: Point (Kalman), Kernel (Mean-Shift & CamShift), Silhouette'},
    'MID1-Q18': {'rank': 21, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': '2D-DFT separability (row-column algorithm), DC component, and spatial frequency axes'},
    'MID2-Q01': {'rank': 22, 'tier': 2, 'tier_name': 'Core Scoring', 'diff': 'Moderate', 'time': '5 min', 'prio': 'Medium', 'reason': 'Multi-D sampling lattices: Rectangular vs Hexagonal and 2D Nyquist conditions'},

    # --- TIER 3: High-Value 10M (Full Framework Designs & In-Depth Formulations) ---
    'MID2-Q20': {'rank': 23, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Moderate', 'time': '8 min', 'prio': 'Top', 'reason': 'Full 10M answer: Confusion matrix, IoU, Precision, Recall, F1 with worked numerical'},
    'MID1-Q13': {'rank': 24, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'Top', 'reason': 'Distance measures: Euclidean, Mahalanobis, and Dynamic Time Warping (DTW dynamic programming)'},
    'MID1-Q16': {'rank': 25, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'Top', 'reason': 'HMM continuous speech: Bakis topology & the 3 problems (Forward, Viterbi, Baum-Welch)'},
    'MID1-Q15': {'rank': 26, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'Top', 'reason': 'GMM mathematical formulation and full derivation of Expectation-Maximization (EM)'},
    'MID1-Q08': {'rank': 27, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'Top', 'reason': 'LPC derivation of Yule-Walker normal equations & Levinson-Durbin recursion algorithm'},
    'MID2-Q04': {'rank': 28, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Moderate', 'time': '8 min', 'prio': 'High', 'reason': 'Complete digital video architecture: Progressive scanning, YCbCr 4:2:0, and GOP (I, P, B)'},
    'MID2-Q03': {'rank': 29, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Moderate', 'time': '8 min', 'prio': 'High', 'reason': 'HVS properties: Luminance vs Chroma, Contrast Sensitivity Function (CSF), Weber law'},
    'MID2-Q09': {'rank': 30, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Moderate', 'time': '8 min', 'prio': 'High', 'reason': 'Block matching motion estimation: Full search vs Three-Step Search vs Diamond search'},
    'MID2-Q19': {'rank': 31, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'High', 'reason': 'Real-time video tracking framework: MoG detection + Hungarian matching + Kalman filters'},
    'MID2-Q17': {'rank': 32, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'High', 'reason': 'Image & video matting: Matting equation I=αF+(1-α)B, Trimap, Levin closed-form Laplacian'},
    'MID1-Q20': {'rank': 33, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Moderate', 'time': '8 min', 'prio': 'High', 'reason': 'Multi-D processing framework: JPEG/MPEG pipeline and DCT vs DFT justification'},
    'MID2-Q11': {'rank': 34, 'tier': 3, 'tier_name': 'High-Value 10M', 'diff': 'Challenging', 'time': '8 min', 'prio': 'High', 'reason': 'Phase correlation motion estimation: Fourier shift theorem & cross-power spectrum'},

    # --- TIER 4: Technical Deep Dive & Advanced Topics ---
    'MID1-Q06': {'rank': 35, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Challenging', 'time': '7 min', 'prio': 'Medium', 'reason': 'Linear (STFT) vs Non-linear (Mel/Bark) filter banks psychoacoustic evaluation'},
    'MID1-Q05': {'rank': 36, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Challenging', 'time': '7 min', 'prio': 'Medium', 'reason': 'Convolution in speech: Source-filter cascade, Overlap-Add (OLA) and Overlap-Save (OLS)'},
    'MID1-Q14': {'rank': 37, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Challenging', 'time': '7 min', 'prio': 'Medium', 'reason': 'Vector Quantization: Voronoi tessellation, LBG centroid splitting algorithm, codebook sizing'},
    'MID2-Q12': {'rank': 38, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Challenging', 'time': '8 min', 'prio': 'Medium', 'reason': '3D Structure from Motion (SfM): Epipolar geometry, Essential Matrix E=[t]xR, 8-Point SVD'},
    'MID1-Q19': {'rank': 39, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Challenging', 'time': '7 min', 'prio': 'Medium', 'reason': '2D LSI systems: 2D discrete convolution, 2D Z-transform, frequency response, separability'},
    'MID2-Q10': {'rank': 40, 'tier': 4, 'tier_name': 'Deep Dive', 'diff': 'Challenging', 'time': '8 min', 'prio': 'Medium', 'reason': 'Nonlinear optimization: Gradient descent, Gauss-Newton, Levenberg-Marquardt damping'}
}
