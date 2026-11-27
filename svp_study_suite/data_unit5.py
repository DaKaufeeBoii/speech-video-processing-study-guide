# -*- coding: utf-8 -*-
"""
Unit 5: Video Segmentation, Change Detection, Object Tracking & Performance Evaluation
Questions: Mid-II Q13 to Q20
Course Coordinator: Dr. Sandeep Kumar M (CSE AI & ML)
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408
Strictly aligned with Unit 5.docx lecture notes and official Question Bank.
"""

UNIT5_QUESTIONS = [
    {
        "id": "MID2-Q13",
        "mid": "Mid-II",
        "qno": 13,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Compare region-based and boundary-based image segmentation methods and analyze their suitability for video processing.",
        "punchline": "Region-based segmentation groups pixels with homogeneous color/intensity (growing, splitting, merging), whereas boundary-based segmentation detects sudden spatial gradient changes (Sobel, Canny, Laplacian); hybrid approaches combining both are essential for robust video object tracking.",
        "mnemonic": "Region = Grouping Homogeneity; Boundary = Detecting Discontinuity.",
        "analogy": "Coloring a coloring book: region-based segmentation fills entire areas with the same crayon shade (inside the lines); boundary-based segmentation takes a black pen and traces only the sharp ink borders.",
        "diagram": """+-------------------------------------------------------------------------------+
|               REGION-BASED VS BOUNDARY-BASED IMAGE SEGMENTATION               |
+-------------------------------------------------------------------------------+

 1. REGION-BASED SEGMENTATION:          2. BOUNDARY-BASED SEGMENTATION:
    Groups pixels with similar             Detects sharp gradient discontinuities:
    properties (Homogeneity condition)     ∇I = [∂I/∂x, ∂I/∂y]ᵀ
    ┌──────────────────────┐               ┌──────────────────────┐
    │  Region R₁ (Green)   │               │   /────────────────\\ │
    │  • Seed  ──► Grows   │               │  /  Canny / Sobel   \\│
    │                      │               │ │   Edge Contours    ││
    │  Region R₂ (Blue)    │               │  \\                  /│
    └──────────────────────┘               └──────────────────────┘
    Techniques: Growing, Split & Merge     Techniques: Sobel, Canny, Laplacian

 VIDEO PROCESSING SUITABILITY:
  • Region-based provides solid foreground object masks (great for background subtraction).
  • Boundary-based detects moving silhouettes but is vulnerable to broken edges and noise.
  • Practical video systems fuse both: Canny edges bound the Region-growing seeds!""",
        "content": """### 1. Definition and Objective of Image Segmentation (Unit 5 Notes)
**Image segmentation** is the process of partitioning a digital image into multiple meaningful, non-overlapping regions or sets of pixels based on shared physical attributes such as color, intensity, texture, or geometric boundaries.
- **Objective:** To simplify image representation, isolate foreground objects from background clutter, and prepare visual data for higher-level computer vision tasks (object detection, classification, and motion tracking).

---

### 2. Major Categories of Image Segmentation

#### A. Region-Based Segmentation (Homogeneity Approach)
- **Principle:** Groups neighboring pixels that exhibit similar statistical characteristics (color, luminance, or texture variance).
- **Core Techniques:**
  1. **Region Growing:** Selects initial seed pixels and recursively appends adjacent neighboring pixels if their intensity difference satisfies $|I(x, y) - I_{\\text{seed}}| < T$.
  2. **Region Splitting:** Recursively splits an inhomogeneous image block into four sub-quadrants (quadtree decomposition) until all child blocks are uniform.
  3. **Region Merging:** Evaluates adjacent quadrants and merges them if their combined variance falls below a predefined homogeneity threshold.
- **Example:** Segmenting a green agricultural crop leaf from soil background based on chromatic thresholding.

#### B. Boundary-Based Segmentation (Discontinuity Approach)
- **Principle:** Identifies object boundaries by detecting sudden, sharp spatial transitions in image intensity or color.
- **Core Techniques:**
  1. **Sobel Operator:** Computes first-order spatial intensity gradients using $3 \\times 3$ directional convolution masks ($G_x, G_y$).
  2. **Canny Edge Detector:** A multi-stage optimal edge operator that performs Gaussian smoothing $\\rightarrow$ gradient magnitude/angle computation $\\rightarrow$ Non-Maximum Suppression (NMS) $\\rightarrow$ Hysteresis thresholding.
  3. **Laplacian Operator:** Uses second-order spatial derivatives (zero-crossings of $\\nabla^2 I$) to locate rapid intensity inflection points.
- **Example:** Tracing the metallic boundary contour of a moving car in highway traffic surveillance.

---

### 3. Comprehensive Comparison Table (Unit 5 Notes)

| Comparison Factor | Region-Based Segmentation | Boundary-Based Segmentation |
| :--- | :--- | :--- |
| **Fundamental Mechanism** | Groups neighboring pixels based on **similarity / homogeneity** | Identifies object borders based on **gradient discontinuity** |
| **Input Information** | Pixel intensity, color distributions, texture statistics | First- and second-order spatial derivatives ($\\nabla I, \\nabla^2 I$) |
| **Nature of Output** | Closed, solid connected 2D spatial regions (masks) | Edge segments, outlines, and contour curves |
| **Sensitivity to Noise** | Relatively robust; averaging smooths random noise | **Highly sensitive;** derivative operators amplify sensor grain |
| **Common Failure Mode** | Over-segmentation; bleeding across weak boundaries | Broken, disconnected edges; false edge fragments |
| **Representative Methods**| Region Growing, Split-and-Merge, Watershed | Sobel, Prewitt, Canny Edge Detector, Laplacian of Gaussian |

---

### 4. Analysis of Suitability for Video Processing
1. **Region-Based Suitability:**
   - *Advantage:* Produces solid, contiguous binary masks ($M(x, y) \\in \\{0, 1\\}$) required for background subtraction, optical flow masking, and area measurement.
   - *Challenge:* Computationally intensive to re-seed and grow regions for every video frame at 30 fps.
2. **Boundary-Based Suitability:**
   - *Advantage:* Extremely fast and easily accelerated on GPUs; effective for tracking sharp rigid silhouettes.
   - *Challenge:* Edge gaps cause contour tracking to leak into background textures; sensitive to lighting shifts.
3. **The Modern Hybrid Paradigm:**
   Real-time video tracking systems deploy **hybrid approaches**: boundary operators (Canny) detect candidate moving edges, which subsequently act as impenetrable barrier walls for fast region-growing and active contour (snake) models."""
    },
    {
        "id": "MID2-Q14",
        "mid": "Mid-II",
        "qno": 14,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Explain the principles of change detection in video sequences and discuss its importance in video surveillance.",
        "punchline": "Change detection identifies dynamic scene variations via Frame Differencing (D = |I_t - I_{t-1}|), Background Subtraction (D = |I_t - B|), Thresholding, and Optical Flow; it serves as the frontline trigger for automated video surveillance alarms.",
        "mnemonic": "F-B-T-O: Frame Differencing, Background Subtraction, Thresholding, Optical Flow.",
        "analogy": "Like a security guard watching a bank vault: rather than staring intensely at every inch of concrete wall all night, the guard's motion detector alerts only when something enters or moves across the field of view.",
        "diagram": """+-------------------------------------------------------------------------------+
|                 PRINCIPLES OF CHANGE DETECTION IN SURVEILLANCE                |
+-------------------------------------------------------------------------------+

 1. FRAME DIFFERENCING:
    Current Frame I_t ──► [ - ] ◄── Previous Frame I_{t-1} ──► D(x, y) = |I_t - I_{t-1}|
                           │
 2. BACKGROUND SUBTRACTION:│
    Current Frame I_t ──► [ - ] ◄── Static Background B(x, y) ──► D(x, y) = |I_t - B|
                           │
                           ▼
 3. THRESHOLDING:
    Binary Motion Mask M(x, y) = 1 if D(x, y) > T else 0
                           │
                           ▼
 4. SURVEILLANCE APPLICATIONS:
    • Parking Lot Security: Triggers recording when vehicle enters empty stall
    • Perimeter Intrusion: Sounds alarm when pedestrian crosses fence line
    • Traffic Congestion: Detects stopped vehicles blocking intersections""",
        "content": """### 1. Conceptual Principles of Change Detection (Unit 5 Notes)
**Change detection** is a fundamental low-level computer vision technique that detects temporal variations in pixel values between consecutive video frames or between an incoming frame and a reference background model.
- **Primary Objective:** To isolate moving objects, detect environmental alterations, and discard redundant stationary background pixels for real-time video surveillance.

---

### 2. The Four Core Principles of Change Detection (Unit 5 Notes)

#### A. Frame Differencing
- **Principle:** Subtracts pixel intensities between two immediately consecutive video frames:
  $$D(x, y) = |I_t(x, y) - I_{t-1}(x, y)|$$
- **Characteristics:**
  - Extremely fast and computationally lightweight.
  - Automatically adapts to gradual daytime lighting changes.
  - *Limitation:* Generates the "aperture interior hole" problem (homogeneous interiors of large moving objects produce zero frame difference, leaving only leading and trailing edges).

#### B. Background Subtraction
- **Principle:** Compares current frame $I_t(x, y)$ against an estimated, long-term statistical background model $B(x, y)$:
  $$D(x, y) = |I_t(x, y) - B(x, y)|$$
  where $B(x, y)$ is updated adaptively over time using running Gaussian averages:
  $$B_t(x, y) = (1 - \\alpha) B_{t-1}(x, y) + \\alpha I_t(x, y), \\quad 0 < \\alpha < 1$$
- **Characteristics:** Recovers complete, solid foreground silhouettes of moving objects.

#### C. Thresholding (Binarization)
- **Principle:** Converts the continuous difference map $D(x, y)$ into a clean binary motion mask $M(x, y)$:
  $$M(x, y) = \\begin{cases} 1 & \\text{if } D(x, y) > T \\quad (\\text{Motion / Change Detected}) \\\\ 0 & \\text{if } D(x, y) \\le T \\quad (\\text{Stationary Background}) \\end{cases}$$
  where $T$ is an experimentally tuned or adaptive noise threshold.

#### D. Optical Flow
- **Principle:** Computes apparent spatio-temporal velocity vectors $(u, v)$ for each pixel based on gradient constraints $I_x u + I_y v + I_t = 0$.
- **Characteristics:** Distinguishes the specific speed and direction of moving objects from background camera vibration.

---

### 3. Importance in Video Surveillance Systems (Unit 5 Notes)
In modern automated CCTV security and smart city surveillance:
1. **Intrusion Detection:** Detects unauthorized human or vehicular entry across geofenced perimeter boundaries outside authorized hours.
2. **Bandwidth & Storage Conservation:** Prevents 24/7 video storage of empty static rooms; systems record at high framerates only when change detection flags activity.
3. **Traffic Surveillance & Incident Detection:** Identifies stalled vehicles on highways, illegal wrong-way driving, and lane blockages.
4. **Parking Lot Monitoring (Practical Example):**
   - *Frame 1:* Parking stall is completely empty (recorded into background model $B$).
   - *Frame 2:* An automobile enters the stall.
   - *Frame 3:* Frame differencing and background subtraction detect large pixel intensity differences ($D > T$).
   - *Outcome:* The system automatically logs the vehicle's arrival timestamp and marks the parking stall as occupied."""
    },
    {
        "id": "MID2-Q15",
        "mid": "Mid-II",
        "qno": 15,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "In a video sequence, global motion is analyzed across three regions with SAD values: Region A = 120, Region B = 45, Region C = 200, Threshold = 100. 1. Identify regions containing motion. 2. Identify regions without motion. 3. Determine the region with the most dominant motion.",
        "punchline": "Comparing SAD values against threshold T = 100 reveals that Regions A and C contain motion (120 > 100, 200 > 100), Region B has no motion (45 < 100), and Region C exhibits the most dominant motion (max SAD = 200).",
        "mnemonic": "Check SAD > T: A (120>100 YES), B (45<100 NO), C (200>100 YES). Dominant = max(120, 45, 200) = C.",
        "analogy": "Like checking three security motion sensors calibrated to trigger at 100 decibels of sound: Room A registers 120 dB (alarm), Room B registers 45 dB (quiet), and Room C registers 200 dB (deafening alarm and loudest source).",
        "diagram": """+-------------------------------------------------------------------------------+
|                    GLOBAL MOTION DETECTION & THRESHOLD CHECK                  |
+-------------------------------------------------------------------------------+

  SAD Value ▲
        200 │                                          █ Region C = 200
            │                                          █ (DOMINANT MOTION!)
        150 │
        120 │             █ Region A = 120             █
            │             █ (Motion Detected)          █
  ══════100 ╞═════════════╪════════════════════════════╪════════════════════════►
            │  Threshold  │                            │   THRESHOLD = 100
         50 │             │        █ Region B = 45     │
            │             │        █ (NO MOTION)       │
          0 └─────────────┴────────┴───────────────────┴───────────────────────
                       Region A  Region B            Region C

 RESULTS SUMMARY:
  • Regions WITH motion   : Region A (120 > 100) and Region C (200 > 100)
  • Regions WITHOUT motion: Region B (45 < 100)
  • Dominant Motion Region: Region C (Max SAD = 200)""",
        "content": """### 1. Problem Statement & Given Data (Unit 5 Notes)
In video sequence motion detection, frame differences across spatial regions are quantified using the **Sum of Absolute Differences (SAD)**:
- **Region A:** $\\text{SAD}_A = 120$
- **Region B:** $\\text{SAD}_B = 45$
- **Region C:** $\\text{SAD}_C = 200$
- **Global Motion Detection Threshold ($T$):** $T = 100$

---

### 2. Decision Criteria
For any region $R$:
$$\\text{If } \\text{SAD}_R > T \\implies \\text{Motion is detected}$$
$$\\text{If } \\text{SAD}_R \\le T \\implies \\text{No significant motion is detected (Stationary / Noise)}$$

---

### 3. Step-by-Step Evaluation

#### 1. Identification of Regions Containing Motion:
- **Region A:**
  $$\\text{SAD}_A = 120 > 100 \\implies \\mathbf{Motion\\ Detected}$$
- **Region B:**
  $$\\text{SAD}_B = 45 < 100 \\implies \\text{No Significant Motion}$$
- **Region C:**
  $$\\text{SAD}_C = 200 > 100 \\implies \\mathbf{Motion\\ Detected}$$
- **Verdict for Part 1:** **Regions A and C** contain significant motion.

#### 2. Identification of Regions Without Motion:
- **Region B:**
  $$\\text{SAD}_B = 45 < 100 \\implies \\mathbf{No\\ Motion\\ Detected}$$
- **Verdict for Part 2:** **Region B** is the region without significant motion.

#### 3. Determination of the Most Dominant Motion Region:
The dominant motion region corresponds to the highest frame difference intensity:
$$\\text{Dominant Motion} = \\max(\\text{SAD}_A, \\text{SAD}_B, \\text{SAD}_C) = \\max(120, 45, 200) = 200$$
- **Verdict for Part 3:** **Region C** has the most dominant motion because $\\text{SAD}_C = 200$ represents the largest temporal change across the entire video frame.

---

### 4. Tabular Summary of Results (Unit 5 Notes)

| Region | Measured SAD Value | Comparison with Threshold ($T=100$) | Motion Status | Dominance Ranking |
| :---: | :---: | :---: | :---: | :---: |
| **Region A** | $120$ | $120 > 100$ | **Motion Detected** | 2nd Highest |
| **Region B** | $45$ | $45 < 100$ | **No Motion (Static)**| Lowest |
| **Region C** | $200$ | $200 > 100$ | **Motion Detected** | **1st (Dominant Motion)** |

---

### 5. Final Technical Interpretation
Region C exhibits the highest intensity of frame-to-frame temporal change ($\text{SAD} = 200$), indicating the presence of a fast-moving, high-contrast, or large foreground object. Region A contains moderate movement ($120$), while Region B falls safely below the noise threshold ($45$), confirming it as stationary background scenery."""
    },
    {
        "id": "MID2-Q16",
        "mid": "Mid-II",
        "qno": 16,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "Illustrate the concept of motion tracking and explain how trajectory calculation is performed across video frames.",
        "punchline": "Motion tracking associates detected objects across consecutive frames using Optical Flow, Kalman Filters, or Particle Filters; the object trajectory is calculated as the ordered chronological sequence of centroid coordinates T = {P_1, P_2, ..., P_K}.",
        "mnemonic": "Track = Detect -> Associate -> Predict. Trajectory = Chronological coordinate set T = {(x_t, y_t)}.",
        "analogy": "Like tracing footsteps left in wet sand: tracking identifies each footstep as belonging to the same hiker, and connecting the footprints in order forms the hiker's continuous path (trajectory).",
        "diagram": """+-------------------------------------------------------------------------------+
|                    OBJECT TRAJECTORY CALCULATION ACROSS FRAMES                |
+-------------------------------------------------------------------------------+

 Spatial Trajectory Plot:
   Y-axis ▲
       35 │                                              • F₄ (25, 35)
          │                                            /
       30 │                               • F₃ (20, 30)
          │                             /   MV = (5, 5)
       25 │                  • F₂ (15, 25)
          │                /   MV = (5, 5)
       20 │   • F₁ (10, 20)
          │     MV = (5, 5)
          └─┴──────────────┴──────────────┴──────────────┴──────────────► X-axis
            10             15             20             25

  Trajectory Representation:
  T = { (10, 20), (15, 25), (20, 30), (25, 35) }
  Constant Motion Vector: MV = (Δx, Δy) = (5, 5) pixels/frame
  Direction: Uniform linear diagonal movement in positive X and Y directions.""",
        "content": """### 1. Concept of Motion Tracking (Unit 5 Notes)
**Motion tracking** is the computer vision process of locating, identifying, and following one or more moving objects continuously across consecutive frames of a temporal video sequence.
- **Trajectory Estimation:** Establishes the spatial movement history of an object over time by recording its centroid coordinates $(x_t, y_t)$ at every time instant $t$.

---

### 2. Major Motion Tracking Algorithms (Unit 5 Notes)
1. **Optical Flow Tracking (Lucas-Kanade):** Tracks distinctive corner features frame-to-frame based on spatial/temporal intensity gradients.
2. **Kalman Filter Tracking:** Predicts the object's next position using linear kinematic models (position, velocity) and corrects the estimate when noisy measurements arrive.
3. **Particle Filter Tracking (Sequential Monte Carlo):** Maintains multiple spatial hypotheses (particles) to track objects undergoing abrupt non-linear motion or temporary occlusions.

---

### 3. Step-by-Step Demonstration of Trajectory Calculation (Unit 5 Notes)
Consider a moving vehicle tracked across **four consecutive video frames ($F_1, F_2, F_3, F_4$)** with recorded centroid coordinates:

| Frame Number | Temporal Index ($t$) | Horizontal Coordinate ($X$) | Vertical Coordinate ($Y$) |
| :---: | :---: | :---: | :---: |
| **$F_1$** | $t = 1$ | $x_1 = 10$ | $y_1 = 20$ |
| **$F_2$** | $t = 2$ | $x_2 = 15$ | $y_2 = 25$ |
| **$F_3$** | $t = 3$ | $x_3 = 20$ | $y_3 = 30$ |
| **$F_4$** | $t = 4$ | $x_4 = 25$ | $y_4 = 35$ |

#### Step 1: Inter-Frame Displacement (Motion Vector) Calculation
The inter-frame displacement vector $\\mathbf{MV}_k = (\\Delta x_k, \\Delta y_k)$ between frames $F_k$ and $F_{k+1}$ is:
$$\\Delta x_k = x_{k+1} - x_k, \\quad \\Delta y_k = y_{k+1} - y_k$$

- **Displacement from Frame 1 to Frame 2:**
  $$\\mathbf{MV}_1 = (x_2 - x_1, \\ y_2 - y_1) = (15 - 10, \\ 25 - 20) = (5, 5)$$
- **Displacement from Frame 2 to Frame 3:**
  $$\\mathbf{MV}_2 = (x_3 - x_2, \\ y_3 - y_2) = (20 - 15, \\ 30 - 25) = (5, 5)$$
- **Displacement from Frame 3 to Frame 4:**
  $$\\mathbf{MV}_3 = (x_4 - x_3, \\ y_4 - y_3) = (25 - 20, \\ 35 - 30) = (5, 5)$$

#### Step 2: Trajectory Formulation
The complete object trajectory $\\mathcal{T}$ over the time interval is formally represented as an ordered set of time-stamped 2D spatial coordinate vectors:
$$\\mathcal{T} = \\left\\{ (x_t, y_t) \\right\\}_{t=1}^4 = \\left\\{ (10, 20), \\ (15, 25), \\ (20, 30), \\ (25, 35) \\right\\}$$

#### Step 3: Trajectory Velocity and Directional Interpretation
- **Velocity Vector:** Since $\\mathbf{MV} = (5, 5)$ is constant across all frames, the object moves with a uniform velocity of $\\Delta x = 5\\text{ pixels/frame}$ horizontally and $\\Delta y = 5\\text{ pixels/frame}$ vertically.
- **Speed (Magnitude):**
  $$v = \\sqrt{\\Delta x^2 + \\Delta y^2} = \\sqrt{5^2 + 5^2} = \\sqrt{50} \\approx 7.071\\text{ pixels/frame}$$
- **Direction:** The object travels along a straight line oriented at $\\theta = \\arctan(5/5) = 45^\\circ$ diagonally in the positive X and positive Y directions."""
    },
    {
        "id": "MID2-Q17",
        "mid": "Mid-II",
        "qno": 17,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K4",
        "marks": "10 Marks",
        "title": "Analyze the principles of image and video matting and evaluate the performance of different matting techniques.",
        "punchline": "Matting decomposes image pixels into foreground, background, and continuous alpha opacity (I = αF + (1-α)B, α ∈ [0,1]) to capture fine semi-transparent structures like hair and glass; deep learning and optical flow video matting deliver state-of-the-art temporal consistency under complex backgrounds.",
        "mnemonic": "Matting Equation: I = αF + (1-α)B. Types: Chroma, Bayesian, Closed-Form, Deep Learning.",
        "analogy": "Image segmentation is like cutting out an actor with scissors (hard jagged edge, cuts off individual hairs); image matting is like creating a photographic transparency slide where hair strands and glass reflections seamlessly blend onto any new background.",
        "diagram": """+-------------------------------------------------------------------------------+
|               IMAGE AND VIDEO MATTING ARCHITECTURE & EQUATION                 |
+-------------------------------------------------------------------------------+

 COMPOSITING EQUATION:
   I(x, y) = α(x, y) · F(x, y) + [ 1 - α(x, y) ] · B(x, y)
   • α = 1.0  ──► 100% Solid Foreground (Actor body)
   • α = 0.0  ──► 100% Background (Studio wall)
   • 0 < α < 1──► Semi-transparent transition (Hair, fur, smoke, glass)

 MATTING TECHNIQUES TAXONOMY:
 ┌──────────────────────────────────┬──────────────────────────────────────────┐
 │ Image Matting                    │ Video Matting (Temporal Extension)       │
 ├──────────────────────────────────┼──────────────────────────────────────────┤
 │ • Chroma Keying (Green Screen)   │ • Background Subtraction Matting         │
 │ • Bayesian Matting (Probabilistic)│ • Optical Flow Matting (Alpha warped)   │
 │ • Closed-Form Matting (Laplacian)│ • Deep Learning Video Matting (Attention)│
 └──────────────────────────────────┴──────────────────────────────────────────┘

 EVALUATION METRICS:
  SAD = Σ |α - α*|  │  MSE = (1/N) Σ (α - α*)²  │  Gradient Error  │  Temporal Consistency""",
        "content": """### 1. Conceptual Principles of Image and Video Matting (Unit 5 Notes)
**Matting** is the soft-segmentation process of accurately extracting foreground objects from complex backgrounds by estimating the continuous opacity (**alpha matte** $\\alpha$) of each pixel.
- **Difference from Hard Segmentation:** Conventional binary segmentation assigns a discrete label $\\{0, 1\\}$ to each pixel, producing artificial staircasing (aliasing) and destroying delicate semi-transparent details (fine hair, animal fur, translucent glass, water splashes). Matting calculates fractional alpha values $\\alpha \\in [0, 1]$.

---

### 2. The Fundamental Matting Equation (Unit 5 Notes)
An observed pixel color $\\mathbf{I}(x, y)$ is modeled as a convex linear combination of a true foreground color $\\mathbf{F}(x, y)$ and a background color $\\mathbf{B}(x, y)$:
$$\\mathbf{I}(x, y) = \\alpha(x, y) \\mathbf{F}(x, y) + [1 - \\alpha(x, y)] \\mathbf{B}(x, y)$$
where:
- $\\alpha(x, y) = 1$: The pixel belongs entirely to the solid foreground.
- $\\alpha(x, y) = 0$: The pixel belongs entirely to the background.
- $0 < \\alpha(x, y) < 1$: The pixel contains a mixed, semi-transparent boundary.

#### The Under-Constrained Inverse Problem
In a standard 3-channel RGB image, each pixel yields **3 known values** $(I_R, I_G, I_B)$ but **7 unknown variables**: three foreground colors $(F_R, F_G, F_B)$, three background colors $(B_R, B_G, B_B)$, and the scalar opacity $\\alpha$. To solve this severely ill-posed problem, matting algorithms rely on user-provided **trimaps** (classifying pixels into definite foreground, definite background, and unknown regions) or specialized priors.

---

### 3. Examination of Image Matting Techniques (Unit 5 Notes)

#### A. Chroma Key Matting (Color Differencing)
- **Principle:** Places the foreground subject before a solid, uniform saturated green or blue backdrop.
- **Performance:** Ultra-fast, real-time broadcast standard; fails completely when foreground subjects wear clothes matching the screen color or under screen spill (green reflection on skin).

#### B. Bayesian Matting (Probabilistic Framework)
- **Principle:** Models foreground and background color distributions in local windows as Gaussian probability densities $\\mathcal{N}(\\boldsymbol{\\mu}_F, \\mathbf{\\Sigma}_F)$ and $\\mathcal{N}(\\boldsymbol{\\mu}_B, \\mathbf{\\Sigma}_B)$. Solves for $(\\mathbf{F}, \\mathbf{B}, \\alpha)$ via Maximum A Posteriori (MAP) estimation.
- **Performance:** Exceptional accuracy for fine hair strands; computationally expensive and depends heavily on high-quality trimaps.

#### C. Closed-Form Matting (Spectral Affinity)
- **Principle:** Assumes foreground and background colors follow local linear models within small windows. Derives the **Matting Laplacian Matrix $\\mathbf{L}$** to minimize a quadratic cost function:
  $$E(\\alpha) = \\boldsymbol{\\alpha}^T \\mathbf{L} \\boldsymbol{\\alpha} + \\lambda (\\boldsymbol{\\alpha} - \\mathbf{b})^T (\\boldsymbol{\\alpha} - \\mathbf{b})$$
- **Performance:** Mathematically elegant closed-form solution; struggles with complex textured backgrounds having overlapping colors.

#### D. Deep Learning-Based Matting
- **Principle:** Employs Convolutional Neural Networks (CNNs) with encoder-decoder architectures (e.g., Deep Image Matting, MODNet) to predict alpha mattes directly from raw images without requiring user trimaps (trimap-free matting).

---

### 4. Video Matting Techniques (Unit 5 Notes)
Video matting extends single-image matting across temporal frame sequences, with the paramount requirement of preserving **temporal consistency** (preventing frame-to-frame alpha flickering):
1. **Background Subtraction Video Matting:** Compares frames against a pre-recorded clean background plate; highly sensitive to camera jitter and changing sunlight.
2. **Optical Flow Video Matting:** Estimates inter-frame motion vectors $(u, v)$ to warp and propagate the alpha matte $\\alpha_{t-1}$ into frame $t$, enforcing temporal smoothness along motion trajectories.
3. **Deep Learning Video Matting (Temporal Attention / Recurrent Networks):** Uses recurrent convolutional units (ConvLSTM) and temporal attention layers to model temporal context across multi-frame windows.

---

### 5. Performance Comparison Matrix (Unit 5 Notes)

| Matting Technique | Accuracy on Fine Hair | Computational Complexity | Sensitivity to Illumination / Noise | Requirement for User Input |
| :--- | :--- | :--- | :--- | :--- |
| **Chroma Keying** | High (in studio) | **Very Low** (Real-time) | Sensitive to color spill & shadows | Requires dedicated green screen |
| **Bayesian Matting** | High | High ($O(N)$ local MAP) | Moderate | Requires accurate 3-region Trimap |
| **Closed-Form Matting**| Very High | High (Large linear solve) | Sensitive to complex background textures | Requires user Trimap or scribble cues |
| **Optical Flow Matting**| Moderate-to-High | Medium-to-High | Sensitive to fast motion & occlusions | Video motion vectors |
| **Deep Learning Matting**| **Highest** | High (GPU inference) | **Robust** (Trained on diverse datasets) | **Trimap-free** / fully automated |

---

### 6. Quantitative Evaluation Metrics (Unit 5 Notes)
1. **Sum of Absolute Differences (SAD):** $\\text{SAD} = \\sum_{x, y} |\\alpha(x, y) - \\alpha^*(x, y)|$ (Lower is better).
2. **Mean Squared Error (MSE):** $\\text{MSE} = \\frac{1}{N} \\sum_{i=1}^N (\\alpha_i - \\alpha_i^*)^2$.
3. **Gradient Error:** Measures edge difference $\\|\\nabla \\alpha - \\nabla \\alpha^*\\|$, assessing fine hair sharpness.
4. **Temporal Fluctuation (dtSSD):** Evaluates mean squared differences of alpha derivatives between frames to penalize flickering."""
    },
    {
        "id": "MID2-Q18",
        "mid": "Mid-II",
        "qno": 18,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K4",
        "marks": "10 Marks",
        "title": "A) In a particle filter tracking system, four particles have weights: [0.2, 0.3, 0.1, 0.4]. 1. Check if normalized. 2. Identify the most likely particle. 3. Explain how this choice improves tracking robustness. B) A Kalman filter has predicted position x̂⁻ = 50, measurement z = 60, Kalman gain K = 0.6. 1. Calculate the updated position estimate. 2. Interpret how the Kalman gain influences the updated state.",
        "punchline": "Part A: Particle weights sum to 1.0 (already normalized); Particle 4 is most likely with weight 0.4 (40%), providing multi-hypothesis robustness against occlusion. Part B: Updated Kalman position is x̂ = 50 + 0.6(60 - 50) = 56; the gain of 0.6 balances 60% measurement confidence against 40% predicted model confidence.",
        "mnemonic": "Part A: Sum = 1.0 (Normalized), Max = P4 (40%). Part B: x̂ = x⁻ + K(z - x⁻) = 50 + 0.6(10) = 56.",
        "analogy": "Part A: Four scouts search a forest for a lost hiker; Scout 4 has a 40% confidence clue, but keeping all four scouts prevents getting tricked by false footprints. Part B: You predict a bus is at mile 50, GPS says mile 60; with 60% GPS trust (K=0.6), you conclude the bus is at mile 56.",
        "diagram": """+-------------------------------------------------------------------------------+
|                    STATE ESTIMATION NUMERICAL CALCULATIONS                    |
+-------------------------------------------------------------------------------+

 PART A: PARTICLE FILTER WEIGHTS
   Particles:    P₁       P₂       P₃       P₄
   Weights  :   [0.2,    0.3,     0.1,     0.4]
   Sum      :   0.2 + 0.3 + 0.1 + 0.4 = 1.00  ==> PERFECTLY NORMALIZED!
   Winner   :   Particle 4 (Highest probability: 0.4 or 40%)

 PART B: KALMAN FILTER STATE UPDATE
   State Axis:
   0                 x̂⁻ = 50        x̂ = 56              z = 60
   |────────────────────•──────────────•───────────────────•──────────────────►
                     Predicted      UPDATED             Measurement
                     Position       STATE               (GPS / Detector)
                        │              ▲                   │
                        └──────────────┴───────────────────┘
                           Innovation / Error = (60 - 50) = 10
                           Correction = K · Error = 0.6 · 10 = +6
                           Updated State x̂ = 50 + 6 = 56""",
        "content": """### PART A: Particle Filter Weight Normalization & Robustness (Unit 5 Notes)

#### 1. Given Data
A particle filter maintains $N = 4$ discrete hypotheses (particles) with importance weights:
$$\\mathbf{W} = [W_1, W_2, W_3, W_4] = [0.2, \\ 0.3, \\ 0.1, \\ 0.4]$$

---

#### 2. Task 1: Check and Normalize Particle Weights
The mathematical condition for normalized particle probability weights is:
$$\\sum_{i=1}^N W_i = 1.0$$

- **Step 1: Compute the sum of given weights:**
  $$\\sum_{i=1}^4 W_i = W_1 + W_2 + W_3 + W_4 = 0.2 + 0.3 + 0.1 + 0.4 = 1.00$$
- **Step 2: Calculate normalized weights ($W'_i = \\frac{W_i}{\\sum W_i}$):**
  $$W'_1 = \\frac{0.2}{1.0} = 0.2, \\quad W'_2 = \\frac{0.3}{1.0} = 0.3, \\quad W'_3 = \\frac{0.1}{1.0} = 0.1, \\quad W'_4 = \\frac{0.4}{1.0} = 0.4$$
- **Verdict:** The particle weights are **already perfectly normalized** ($\sum W_i = 1.0$).

---

#### 3. Task 2: Identify the Most Likely Particle
The most likely particle corresponds to the maximum importance weight:
$$i^* = \\arg\\max_{i} W'_i = \\max(0.2, 0.3, 0.1, 0.4) = 0.4 \\implies \\mathbf{Particle\\ 4}$$
- **Result:** **Particle 4** is the most likely state hypothesis, holding **$40\\%$ ($0.4$) probability**.

---

#### 4. Task 3: Explanation of Robustness to Uncertainty
Maintaining a distribution of particles rather than a single deterministic coordinate enhances tracking robustness:
1. **Multi-Modal State Representation:** Unlike Kalman filters which model only unimodal Gaussian distributions, particle filters maintain multiple spatial hypotheses simultaneously.
2. **Resilience to Occlusion & Clutter:** If an object is temporarily obscured behind a tree or lamppost, the dominant particle's measurement may drop; surviving particles in adjacent regions maintain track lock without losing the target.
3. **Handling Non-Linear & Non-Gaussian Dynamics:** Provides stable tracking during sudden direction reversals or erratic motion.

---

### PART B: Kalman Filter State Update & Motion Correction (Unit 5 Notes)

#### 1. Given Data
- **Prior Predicted State Estimate ($\\hat{x}^-$):** $50$
- **New Sensor Measurement ($z$):** $60$
- **Kalman Gain ($K$):** $0.6$

---

#### 2. Task 1: Calculate the Updated Position Estimate
The standard discrete Kalman Filter measurement update equation is:
$$\\hat{x} = \\hat{x}^- + K \\left( z - \\hat{x}^- \\right)$$

- **Step 1: Compute the measurement residual (Innovation):**
  $$\\text{Innovation} = z - \\hat{x}^- = 60 - 50 = 10$$
- **Step 2: Scale the innovation by the Kalman Gain:**
  $$\\text{Correction Term} = K \\cdot (z - \\hat{x}^-) = 0.6 \\times 10 = 6$$
- **Step 3: Compute the posterior updated state estimate:**
  $$\\hat{x} = 50 + 6 = \\mathbf{56}$$

---

#### 3. Task 2: Technical Interpretation of Kalman Gain Influence
The Kalman gain $K \\in [0, 1]$ represents the optimal weighting factor between the physical prediction model and new sensor measurements:
$$\\hat{x} = (1 - K) \\hat{x}^- + K z = (1 - 0.6)(50) + 0.6(60) = 0.4(50) + 0.6(60) = 20 + 36 = 56$$
1. **Balanced Trust:** Because $K = 0.6$, the filter assigns **$60\\%$ statistical weight to the new measurement $z$** and **$40\\%$ statistical weight to the prior motion model $\\hat{x}^-$**.
2. **Motion Correction:** The filter corrects the initial prediction of $50$ by adding $6$ units towards the measured observation $60$. This prevents noisy sensor spikes from violently throwing off the trajectory while ensuring responsive tracking."""
    },
    {
        "id": "MID2-Q19",
        "mid": "Mid-II",
        "qno": 19,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Construct a video segmentation and tracking framework and examine how motion analysis improves tracking accuracy.",
        "punchline": "An end-to-end framework integrates Change Detection, Background Subtraction, Morphological Filtering, Optical Flow, and Kalman Filtering across 9 stages; motion analysis provides predictive velocity vectors that prevent track loss during occlusions and illumination shifts.",
        "mnemonic": "A-D-B-T-M-O-K-T-T: Acquisition, Differencing, Background subtraction, Thresholding, Morphology, Optical flow, Kalman, Tracking, Trajectory.",
        "analogy": "Like an automated air traffic control radar: it detects new echoes (change detection), filters ground clutter (morphological background subtraction), calculates plane heading and speed (optical flow), and predicts future flight paths even when planes fly through clouds (Kalman filter tracking).",
        "diagram": """+-------------------------------------------------------------------------------+
|         VIDEO SEGMENTATION AND TRACKING FRAMEWORK ARCHITECTURE                |
+-------------------------------------------------------------------------------+

 [ Input Video Stream ] ──► Frame-by-Frame Acquisition (F_t, F_{t-1})
           │
           ▼
 [ 1. Change Detection ] ──► Frame differencing: D = |F_t - F_{t-1}|
           │
           ▼
 [ 2. Background Subtract]─► Adaptive Gaussian Mixture Model: D = |F_t - B_t|
           │
           ▼
 [ 3. Adaptive Threshold ]─► Binarization: M(x, y) = 1 if D > T
           │
           ▼
 [ 4. Morphological Ops ] ──► Opening (removes noise) + Closing (fills holes)
           │
           ▼
 [ 5. Optical Flow ]     ──► Calculates motion vector field (u, v) for moving blobs
           │
           ▼
 [ 6. Kalman Filter ]    ──► Predicts next centroid position x̂⁻_k = A x̂_{k-1}
           │
           ▼
 [ 7. Data Association ] ──► Hungarian Algorithm matches detections to active tracks
           │
           ▼
 [ 8. Trajectory Output ]──► Continuous vehicle path & speed analytics displayed""",
        "content": """### 1. Conceptual Framework Architecture (Unit 5 Notes)
A robust video segmentation and tracking framework integrates low-level spatio-temporal change detection, intermediate binary morphological segmentation, and high-level kinematic motion modeling into a unified real-time processing pipeline.

---

### 2. The 9 Integrated Framework Stages (Unit 5 Notes)

| Stage Number | Framework Module | Algorithmic Technique | Functional Role in Tracking Pipeline |
| :---: | :--- | :--- | :--- |
| **Stage 1** | **Video Ingestion** | Sensor capture ($30\\text{ fps}$) | Continuously ingests frames $F_t$ and maintains buffer memory. |
| **Stage 2** | **Change Detection** | Two-frame differencing | Computes $D(x, y) = |F_t(x, y) - F_{t-1}(x, y)|$ to detect moving regions. |
| **Stage 3** | **Background Subtraction**| Adaptive running average / GMM | Separates solid foreground objects from static backgrounds ($|F_t - B_t|$). |
| **Stage 4** | **Threshold Binarization**| Otsu's adaptive thresholding | Converts difference maps into binary foreground motion masks ($M(x, y)$). |
| **Stage 5** | **Morphological Cleanup**| Morphological Opening & Closing| Eliminates isolated noise pixels and fills interior holes in object blobs. |
| **Stage 6** | **Motion Estimation** | Dense/Sparse Optical Flow | Computes instantaneous velocity vectors $(u, v)$ for each segmented blob. |
| **Stage 7** | **State Prediction** | Linear Kalman Filter | Predicts next expected spatial position: $\\hat{\\mathbf{x}}_k^- = \\mathbf{A} \\hat{\\mathbf{x}}_{k-1}$. |
| **Stage 8** | **Data Association** | Hungarian Algorithm (IoU metric) | Matches predicted Kalman bounding boxes with newly segmented blobs. |
| **Stage 9** | **Trajectory Output** | Coordinate sequence logging | Draws smooth continuous trajectory paths $\\mathcal{T} = \\{(x_t, y_t)\\}$. |

---

### 3. Examination of How Motion Analysis Improves Tracking Accuracy
Relying solely on visual appearance (color, bounding boxes) causes tracking systems to fail when objects cross paths or lighting changes. Integrating **kinematic motion analysis (Optical Flow + Kalman Filtering)** provides transformative improvements:

1. **Overcoming Temporary Occlusion:**
   When a tracked car drives behind a highway sign or overhead bridge, segmentation detection is lost ($M(x, y) = 0$). The Kalman filter uses stored velocity vectors to **propagate the predicted trajectory blindly through the occlusion**, instantly re-associating the target when it emerges.
2. **Resolving ID Switches in Multi-Object Clutter:**
   When two pedestrians walking in opposite directions cross paths, appearance-based trackers frequently swap IDs. Motion analysis assigns opposite velocity vectors $(+u)$ and $(-u)$, ensuring unambiguous data association across the intersection.
3. **Filtering Out Sudden Illumination Spikes:**
   A sudden camera flash or headlight glare creates huge intensity differences ($D > T$). Optical flow verifies whether the difference exhibits coherent physical motion vectors; unphysical static flash regions are immediately rejected as false positives.
4. **Smoothing Tracking Jitter:**
   Raw sensor bounding boxes jitter due to pixel noise. The Kalman filter acts as a statistical low-pass filter, producing smooth, visually stable trajectories.

---

### 4. Real-World Traffic Surveillance Case Study (Unit 5 Notes)
In an automated smart highway monitoring system:
- **Operation:** CCTV cameras capture vehicles passing an intersection.
- **Workflow:** 
  1. Background subtraction isolates each vehicle.
  2. Morphological closing creates a solid bounding box.
  3. Optical flow calculates speed in km/h.
  4. Kalman tracking follows each car across camera blind spots.
- **Result:** Provides automated traffic flow analytics, red-light violation detection, and stopped-vehicle incident alerts in real time."""
    },
    {
        "id": "MID2-Q20",
        "mid": "Mid-II",
        "qno": 20,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Design a performance evaluation model for video segmentation and tracking systems and evaluate it using suitable metrics (IoU, Precision, Recall, and F1-Score).",
        "punchline": "A standardized performance evaluation model compares predicted masks against ground truth using a Confusion Matrix; IoU measures spatial bounding box overlap, Precision measures detection correctness, Recall measures detection completeness, and F1-Score provides the harmonic mean balance.",
        "mnemonic": "I-P-R-F: IoU = Overlap/Union, Precision = TP/(TP+FP), Recall = TP/(TP+FN), F1 = 2PR/(P+R).",
        "analogy": "Grading an exam: Precision measures how many of your written answers were actually correct (no wrong guesses); Recall measures how many of all possible questions you answered (didn't skip questions); F1 is your overall GPA score; IoU is how closely your answer matched the teacher's exact grading rubric.",
        "diagram": """+-------------------------------------------------------------------------------+
|         PERFORMANCE EVALUATION MODEL (IoU, PRECISION, RECALL, F1)             |
+-------------------------------------------------------------------------------+

 1. INTERSECTION OVER UNION (IoU):
    ┌────────────────────────┐
    │ Ground Truth B         │        Area of Overlap (A ∩ B)
    │        ┌───────────────┼────┐   IoU = ─────────────────────────
    │        │ Overlap A ∩ B │    │         Area of Union (A ∪ B)
    └────────┼───────────────┘    │
             │ Predicted Mask A   │   IoU = TP / (TP + FP + FN)
             └────────────────────┘

 2. CONFUSION MATRIX GRID:
                     Actual Positive (Foreground)  Actual Negative (Background)
  Predicted Positive │ True Positive (TP) = 80     │ False Positive (FP) = 20    │
  Predicted Negative │ False Negative (FN) = 20    │ True Negative (TN) = 80     │

 WORKED METRIC RESULTS:
  • Precision = 80 / (80 + 20) = 80.0%  │  Recall = 80 / (80 + 20) = 80.0%
  • F1-Score  = 2(0.8)(0.8)/(0.8 + 0.8) = 80.0%
  • IoU       = 80 / (80 + 20 + 20) = 80 / 120 = 66.7%""",
        "content": """### 1. Conceptual Design of the Performance Evaluation Model (Unit 5 Notes)
A rigorous performance evaluation model benchmarks the accuracy, robustness, and real-time computational throughput of video segmentation and object tracking algorithms by comparing predicted segmentations against human-annotated **ground-truth references**.

The evaluation framework consists of 6 structured stages:
1. **Video Ingestion:** Standard benchmark test sequences (e.g., MOTChallenge, CDnet).
2. **Ground-Truth Annotation:** Pixel-level binary masks ($B$) or bounding box coordinates.
3. **Automated Algorithm Execution:** Generates predicted candidate masks ($A$).
4. **Spatial Overlap & Confusion Matrix Mapping:** Classifies pixels into $TP, FP, FN, TN$.
5. **Metric Computation:** Evaluates IoU, Precision, Recall, and F1-Score.
6. **System Optimization:** Tunes hyperparameters (thresholds, filter sizes) based on quantitative scores.

---

### 2. Mathematical Definition of Core Evaluation Metrics (Unit 5 Notes)

#### A. Confusion Matrix Foundations
- **True Positive ($TP$):** Foreground pixels correctly classified as foreground.
- **False Positive ($FP$):** Background pixels incorrectly classified as foreground (false alarms).
- **False Negative ($FN$):** True foreground pixels missed by the detector (missed detections).
- **True Negative ($TN$):** Background pixels correctly classified as background.

#### B. Intersection over Union (IoU / Jaccard Index)
Measures the spatial overlap ratio between the predicted region $A$ and ground-truth region $B$:
$$\\text{IoU} = \\frac{|A \\cap B|}{|A \\cup B|} = \\frac{TP}{TP + FP + FN}$$
*(Scores range from $0$ [no overlap] to $1$ [perfect overlap]; $\\text{IoU} \\ge 0.5$ is standard benchmark threshold for a successful detection).*

#### C. Precision
Measures the proportion of detected foreground pixels that are genuinely correct:
$$\\text{Precision} = \\frac{TP}{TP + FP}$$

#### D. Recall (Sensitivity)
Measures the proportion of actual ground-truth foreground pixels that the system successfully detected:
$$\\text{Recall} = \\frac{TP}{TP + FN}$$

#### E. F1-Score
The harmonic mean of Precision and Recall, providing a single balanced metric:
$$F_1 = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2 TP}{2 TP + FP + FN}$$

---

### 3. Worked Numerical Problem (Unit 5 Notes)
Consider a video segmentation system evaluated on a benchmark video frame with the following pixel classification results:
- **True Positives ($TP$):** $80\\text{ pixels}$
- **False Positives ($FP$):** $20\\text{ pixels}$
- **False Negatives ($FN$):** $20\\text{ pixels}$
- **True Negatives ($TN$):** $80\\text{ pixels}$

#### Step-by-Step Calculations:
1. **Precision Calculation:**
   $$\\text{Precision} = \\frac{TP}{TP + FP} = \\frac{80}{80 + 20} = \\frac{80}{100} = 0.80 = \\mathbf{80.0\\%}$$
   *(Interpretation: $80\\%$ of all pixels flagged as foreground were correct).*

2. **Recall Calculation:**
   $$\\text{Recall} = \\frac{TP}{TP + FN} = \\frac{80}{80 + 20} = \\frac{80}{100} = 0.80 = \\mathbf{80.0\\%}$$
   *(Interpretation: The system successfully captured $80\\%$ of the true object).*

3. **F1-Score Calculation:**
   $$F_1 = 2 \\times \\frac{0.80 \\times 0.80}{0.80 + 0.80} = 2 \\times \\frac{0.64}{1.60} = 2 \\times 0.40 = 0.80 = \\mathbf{80.0\\%}$$
   *(Interpretation: The system exhibits an evenly balanced trade-off between false alarms and missed detections).*

4. **Intersection over Union (IoU) Calculation:**
   $$\\text{IoU} = \\frac{TP}{TP + FP + FN} = \\frac{80}{80 + 20 + 20} = \\frac{80}{120} = \\frac{2}{3} \\approx 0.6667 = \\mathbf{66.7\\%}$$
   *(Interpretation: The predicted segmentation mask overlaps $66.7\\%$ with ground truth, comfortably exceeding the standard $50\\%$ success threshold).*

---

### 4. Summary Table of Performance Results (Unit 5 Notes)

| Evaluation Metric | Mathematical Formula | Calculated Value | Benchmark Standard Verdict |
| :--- | :--- | :---: | :--- |
| **Precision** | $\\frac{TP}{TP + FP}$ | **$80.0\\%$** | High (Low false alarm rate) |
| **Recall** | $\\frac{TP}{TP + FN}$ | **$80.0\\%$** | High (Low missed detection rate) |
| **F1-Score** | $2 \\frac{P \\cdot R}{P + R}$ | **$80.0\\%$** | High balanced detection performance |
| **IoU (Jaccard Index)** | $\\frac{TP}{TP + FP + FN}$ | **$66.7\\%$** | **Excellent overlap** ($> 50\\%$ threshold) |

---

### 5. Optimization Strategies for Real-Time Performance (Unit 5 Notes)
To maximize these evaluation scores in real-time embedded surveillance systems:
1. **Adaptive Thresholding:** Replaces static thresholds with local Otsu or Gaussian mixtures to prevent false positives ($FP$) caused by lighting drift.
2. **Morphological Filtering:** Applying morphological opening removes isolated speckle noise ($FP$), while closing bridges small internal holes ($FN$), directly boosting IoU.
3. **Multi-Object Tracking Specific Metrics:** In continuous video tracking, the model is augmented with **IDF1** (ID F1-score measuring trajectory consistency) and **Frames Per Second (FPS)** to ensure real-time latency (< 33 ms/frame)."""
    }
]
