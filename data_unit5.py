# -*- coding: utf-8 -*-
"""
Unit 5: Video Segmentation, Object Tracking, Matting & Performance Evaluation
Questions: Mid-II Q13 to Q20
Academic Year: 2026-27 | Regulation: KGR23 | Course Code: KG23ACM408
Scaled strictly for exam success (05 Marks vs 10 Marks format).
"""

UNIT5_QUESTIONS = [
    {
        "id": "MID2-Q13",
        "mid": "Mid-II",
        "qno": 13,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K1",
        "marks": "05 Marks",
        "title": "Define image segmentation and classify its major categories based on region-based and boundary-based approaches.",
        "punchline": "Image segmentation partitions a scene into disjoint, semantically meaningful regions; classified into Region-Based (homogeneity, Region Growing, Split-and-Merge) and Boundary-Based (gradient discontinuities, Canny, Active Contours/Snakes).",
        "mnemonic": "R-B-G-S: Region growing, Boundary edge detection, Gradient operators, Snakes / active contours",
        "analogy": "Cutting up a political map: Region-based is coloring neighboring towns with the same political party until you reach a border; Boundary-based is tracing the rivers and mountain ranges that separate countries.",
        "diagram": """IMAGE SEGMENTATION PARADIGMS:

1. REGION-BASED (Similarity Criterion):
   - Region Growing: Seed Pixel ──► Expand to neighbors if |I_p - I_seed| < T
   - Split & Merge: Quadtree decomposition (Split if variance high; Merge if similar)
   ┌───────────┬───────────┐
   │ Region R1 │ Region R2 │   Condition: R1 ∩ R2 = ∅ (Disjoint)
   ├───────────┼───────────┤              ∪ Ri = Total Image
   │ Region R3 │ Region R4 │              P(Ri) = TRUE (Uniform within region)
   └───────────┴───────────┘              P(Ri ∪ Rj) = FALSE (Distinct across regions)

2. BOUNDARY-BASED (Discontinuity Criterion):
   - Gradient Operators : Sobel, Prewitt, Canny Edge Detector (Local maxima)
   - Active Contours    : Snakes minimizing Energy E_snake = E_internal + E_external
   - Hough Transform    : Parametric curve voting (Circles, Lines)""",
        "content": """### 1. Definition of Image Segmentation
Image segmentation is the foundational process of partitioning a digital image $I(x, y)$ into multiple disjoint, non-overlapping, and semantically meaningful regions or sets of pixels $\\{R_1, R_2, \\dots, R_N\\}$.

#### Formal Mathematical Definition:
1. **Completeness:** $\\bigcup_{i=1}^N R_i = I$ (The union of all regions equals the entire image).
2. **Disjointness:** $R_i \\cap R_j = \\emptyset, \\; \\forall i \\ne j$ (Regions do not overlap).
3. **Internal Homogeneity:** $P(R_i) = \\text{TRUE}$ for all $i$ (Pixels within each region share uniform properties such as color, texture, or intensity).
4. **External Distinctness:** $P(R_i \\cup R_j) = \\text{FALSE}$ for any adjacent $R_i, R_j$ (Adjacent regions are statistically distinct).

---

### 2. Major Categories of Image Segmentation

#### Category A: Region-Based Approaches (Similarity Criterion)
These methods identify regions based on pixel similarity (color, intensity, or texture homogeneity):

1. **Region Growing:**
   * *Mechanism:* Begins by selecting one or more \"seed pixels\" inside the target object. It iteratively inspects neighboring pixels and absorbs them into the region if they satisfy a similarity threshold:
     $$|I(x, y) - \\mu_{\\text{region}}| < T$$
   * *Strengths & Weaknesses:* Excellent for localized objects with clear contrast; sensitive to initial seed selection and noise (causes region leakage).
2. **Region Splitting and Merging (Quadtree Approach):**
   * *Mechanism:* Begins with the entire image. If the homogeneity predicate $P(R)$ is FALSE (high intensity variance), the region is split into 4 equal quadrants. This process recurses until all sub-blocks are homogeneous. Adjacent compatible sub-blocks are then merged.

#### Category B: Boundary-Based / Edge-Based Approaches (Discontinuity Criterion)
These methods identify regions by detecting abrupt local intensity discontinuities (edges):

1. **Gradient Operators (Differential Edge Detectors):**
   * *Mechanism:* Computes the magnitude of the 2D spatial gradient $\\|\\nabla I\\| = \\sqrt{I_x^2 + I_y^2}$ using convolution masks (Sobel, Prewitt).
   * *Canny Edge Detector:* The gold standard edge detector; executes Gaussian smoothing, gradient calculation, Non-Maximum Suppression (NMS) for thin 1-pixel ridges, and Hysteresis Thresholding to connect broken contours.
2. **Active Contours (Snakes) & Level Sets:**
   * *Mechanism:* Initializes an elastic parametric spline curve $\\mathbf{v}(s) = (x(s), y(s))$ near the object boundary that dynamically contracts and deforms to minimize an energy functional:
     $$E_{\\text{snake}} = \\int_0^1 \\left[ E_{\\text{internal}}(\\mathbf{v}(s)) + E_{\\text{external}}(\\mathbf{v}(s)) \\right] ds$$
     * $E_{\\text{internal}}$: Controls curve smoothness, elasticity (membrane tension), and bending rigidity.
     * $E_{\\text{external}}$: Attracts the snake toward strong image gradient edges ($-\\beta \\|\\nabla I\\|^2$).

---

### 3. Comparison Summary: Region-Based vs. Boundary-Based

| Attribute | Region-Based Approaches | Boundary-Based Approaches |
| :--- | :--- | :--- |
| **Guiding Principle** | Pixel homogeneity & similarity ($P(R_i) = \\text{TRUE}$) | Abrupt local intensity discontinuities ($\\nabla I$) |
| **Contour Closure** | **Guaranteed Closed:** Regions naturally form closed boundaries | **Open Edges:** Edges are often broken, requiring edge linking |
| **Noise Sensitivity** | Relatively robust (averaging over regions suppresses noise) | Highly sensitive (gradient operators amplify noise) |
| **Computational Basis**| Pixel grouping, tree decomposition, clustering | 2D convolution, differential equations, active splines |
| **Typical Algorithms** | Region Growing, Split-and-Merge, Otsu Thresholding, Watershed | Sobel, Canny, Active Contours (Snakes), Hough Transform |"""
    },
    {
        "id": "MID2-Q14",
        "mid": "Mid-II",
        "qno": 14,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Explain the principles of change detection in video sequences and interpret its role in dynamic scene analysis.",
        "punchline": "Change detection isolates moving foreground objects from static backgrounds; implemented via Temporal Differencing, Background Subtraction, and adaptive Gaussian Mixture Models (MoG) to handle illumination and swaying backgrounds.",
        "mnemonic": "T-B-M-S: Temporal differencing, Background subtraction, Mixture of Gaussians, Shadow removal",
        "analogy": "Spot-the-difference game between two consecutive photos: Subtracting the previous photo from the current one instantly erases the static living room and highlights the playful cat running across the rug.",
        "diagram": """CHANGE DETECTION IN VIDEO SEQUENCES:

1. TEMPORAL DIFFERENCING (Adjacent Frames):
   Frame(t) ──► ( - ) ◄── Frame(t-1)  ──► |Difference| > T ──► Motion Mask
   (Very fast, but suffers from aperture 'holes' inside uniform moving objects)

2. BACKGROUND SUBTRACTION (Background Model):
   Current Frame I(t) ──► ( - ) ◄── Background Model B(t)
                                 │
                                 ▼
                         |I(t) - B(t)| > Threshold
                                 │
                                 ▼
                     [ Raw Foreground Mask M(x, y) ]
                                 │
                                 ▼
                     [ Morphological Cleanup & Shadow Removal ]
                                 │
                                 ▼
                     [ Segmented Moving Objects ]

ADAPTIVE BACKGROUND UPDATE (GMM / Running Average):
   B(t+1) = α · I(t) + (1 - α) · B(t)  (Adapts to gradual sun changes)""",
        "content": """### 1. Principles of Change Detection
Change detection is the process of identifying pixels in a temporal video sequence $I(x, y, t)$ that exhibit significant motion or structural alterations compared to the reference scene. It is the initial step for automated surveillance, traffic monitoring, and action recognition.

---

### 2. Core Methodologies in Change Detection

#### 1. Temporal Frame Differencing
* **Principle:** Subtracts two consecutive video frames separated by time interval $\\Delta t$:
  $$D_t(x, y) = |I(x, y, t) - I(x, y, t - 1)|$$
* **Thresholding:**
  $$M_t(x, y) = \\begin{cases} 1 & \\text{if } D_t(x, y) > T \\\\ 0 & \\text{otherwise} \\end{cases}$$
* **Evaluation:**
  * Extremely fast and computationally lightweight.
  * Naturally adapts to sudden illumination changes.
  * **Critical Weaknesses:** Only detects leading and trailing edges of moving objects. The interior of uniformly colored objects produces zero difference ($D_t \\approx 0$), resulting in **\"ghosting\" and hollowed-out object masks**.

#### 2. Background Subtraction
* **Principle:** Compares the current frame $I(x, y, t)$ against a continuously maintained reference image of the background $B(x, y, t)$:
  $$|I(x, y, t) - B(x, y, t)| > T$$
* **Adaptive Running Average Update:**
  $$B(x, y, t + 1) = \\alpha I(x, y, t) + (1 - \\alpha) B(x, y, t)$$
  where $\\alpha \\in [0.001, 0.05]$ is the learning rate that gradually absorbs slow daylight changes and parked cars into the background.

#### 3. Mixture of Gaussians (MoG / Stauffer-Grimson Model)
* **Principle:** Models the intensity history of each individual pixel as a mixture of $K$ (typically $K = 3$ to $5$) Gaussians:
  $$P(I_t) = \\sum_{k=1}^K w_{k, t} \\mathcal{N}(I_t; \\mu_{k, t}, \\sigma_{k, t}^2)$$
* **Why MoG is Superior:** Real-world outdoor backgrounds are **multi-modal** (e.g. swaying tree branches, rippling water on lakes, flickering computer monitors). MoG assigns separate Gaussian components to tree leaves and blue sky, preventing false motion alarms.

---

### 3. Practical Challenges in Dynamic Scene Analysis
1. **Cast Shadows:** Moving objects cast dark shadows onto the ground that move along with them. Shadows pass intensity thresholds ($|I - B| > T$), distorting object bounding boxes.
   * *Mitigation:* Convert pixels to HSV/YCbCr color space; shadows cause a drop in luminance ($V$) while preserving hue ($H$) and saturation ($S$).
2. **Bootstrapping Problem:** Initializing a background model when moving objects are already present in the camera field of view from frame 0.
3. **Sudden Global Illumination (Light Switch):** Turning on a room light alters all pixels simultaneously. Solved via global histogram monitoring to trigger instant background re-initialization."""
    },
    {
        "id": "MID2-Q15",
        "mid": "Mid-II",
        "qno": 15,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "By Using Global Motion Detection  Frame differences (sum of absolute differences): Region A = 120  Region B = 45  Region C = 200  Threshold = 100  Identify regions with motion  Determine dominant motion region",
        "punchline": "Motion occurs where SAD > 100 -> Region A (120) and Region C (200) exhibit motion; Region C is the Dominant Motion Region with maximum SAD = 200.",
        "mnemonic": "T-C-D: Threshold comparison (SAD > T), Classify motion states, Determine dominant max",
        "analogy": "Security guards monitoring three warehouse rooms: Room A has 120 decibels of sound, Room B has 45, and Room C has 200. With a noise threshold of 100, alarms trigger in A and C, with C being the loudest hotspot.",
        "diagram": """GLOBAL MOTION DETECTION THRESHOLDING:

  Frame Difference (SAD)
  ▲
  │                     ■ Region C (SAD = 200)  ◄── DOMINANT MOTION REGION!
  │                     │                           (Max Activity: 200 > 100)
  │                     │
  │        ■ Region A   │
  │        │ (SAD = 120)│
200 ───────┼────────────┼──────────────────────────
  │        │            │
100 ───────┼────────────┼──────────────────────────◄ THRESHOLD T = 100
  │        │   ■ Region B
  │        │   │ (SAD = 45)  ◄── STATIC / NOISE (45 <= 100)
  └────────┴───┴────────┴──────────────────────────► Spatial Regions
           A   B        C

DECISION MATRIX:
  - Region A : 120 > 100 ──► MOTION DETECTED (Active)
  - Region B :  45 ≤ 100 ──► NO SIGNIFICANT MOTION (Static Background)
  - Region C : 200 > 100 ──► MOTION DETECTED (DOMINANT REGION)""",
        "content": """### 1. Given Data
* Frame difference measure: **Sum of Absolute Differences (SAD)**
* **Region A Difference:** $\\text{SAD}_A = 120$
* **Region B Difference:** $\\text{SAD}_B = 45$
* **Region C Difference:** $\\text{SAD}_C = 200$
* **Global Motion Detection Threshold ($T$):** **$100$**

---

### 2. Task 1: Identify Regions with Motion

#### Detection Criterion:
In global motion detection based on frame differencing:
* If $\\text{SAD} > T$: Significant temporal change has occurred $\\implies$ **Motion Detected**.
* If $\\text{SAD} \\le T$: Changes are within sensor noise tolerance $\\implies$ **No Significant Motion (Static Region)**.

#### Evaluation of Each Region:
1. **Region A:**
   $$\\text{SAD}_A = 120 > 100$$
   $$\\implies \\mathbf{Motion\\ Detected\\ in\\ Region\\ A}$$
2. **Region B:**
   $$\\text{SAD}_B = 45 \\le 100$$
   $$\\implies \\mathbf{No\\ Significant\\ Motion\\ in\\ Region\\ B} \\; \\text{(Classified as Static Background)}$$
3. **Region C:**
   $$\\text{SAD}_C = 200 > 100$$
   $$\\implies \\mathbf{Motion\\ Detected\\ in\\ Region\\ C}$$

$$\\mathbf{Answer\\ 1: } \\quad \\text{The regions exhibiting motion are } \\mathbf{Region\\ A} \\text{ and } \\mathbf{Region\\ C}.$$

---

### 3. Task 2: Determine the Dominant Motion Region

#### Criterion:
The **Dominant Motion Region** is defined as the region exhibiting the highest magnitude of frame difference (maximum SAD), indicating the largest physical object displacement or fastest moving entity across the video frame:
$$\\text{Dominant Region} = \\arg\\max_{R \\in \\{A, B, C\\}} \\{\\text{SAD}_R\\}$$

#### Evaluation:
$$\\max(120, 45, 200) = 200 \\quad (\\text{Region C})$$

$$\\mathbf{Answer\\ 2: } \\quad \\mathbf{Region\\ C} \\text{ is the Dominant Motion Region with } \\mathbf{SAD = 200}.$$

---

### 4. Summary Table for Full Exam Marks

| Region | Measured SAD | Threshold ($T$) | Comparison Result | Motion Status | Dominant Ranking |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Region A** | $120$ | $100$ | $120 > 100$ | **Motion Detected** | Rank 2 |
| **Region B** | $45$ | $100$ | $45 \\le 100$ | **No Motion (Static)**| Rank 3 (Inactive) |
| **Region C** | $200$ | $100$ | $200 > 100$ | **Motion Detected** | **Rank 1 (DOMINANT)** |"""
    },
    {
        "id": "MID2-Q16",
        "mid": "Mid-II",
        "qno": 16,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K4",
        "marks": "05 Marks",
        "title": "Implement motion tracking algorithms and demonstrate object trajectory estimation in a temporal video sequence.",
        "punchline": "Motion tracking associates detections over time into continuous trajectories (x(t), y(t)) using Point Tracking (Kalman/Particle filters), Kernel Tracking (Mean-Shift/CamShift), or Silhouette Tracking.",
        "mnemonic": "P-K-S-T: Point tracking, Kernel/Mean-Shift tracking, Silhouette tracking, Trajectory estimation",
        "analogy": "A spotlight operator following a dancer on stage: The operator centers the spotlight on the dancer's vibrant costume color (Mean-Shift kernel tracking) and anticipates where they will leap next (Kalman filter).",
        "diagram": """OBJECT MOTION TRACKING TAXONOMY:

1. POINT TRACKING:
   - Tracks sparse feature points (corners/centroids) across time
   - Deterministic: Kalman Filter (Linear Gaussian state updates)
   - Probabilistic: Particle Filter (Non-linear non-Gaussian sampling)

2. KERNEL / APPEARANCE TRACKING (Mean-Shift / CamShift):
   Frame t: Target Bounding Box ──► Color Histogram q
                                         │
   Frame t+1: Back-project Color Prob Map p(x)
              Mean Shift Vector m(x) iteratively climbs gradient to mode!

3. TRAJECTORY ESTIMATION:
   Temporal State: X_t = [ x, y, v_x, v_y ]^T
   Estimated Trajectory: Tr = { (x1, y1), (x2, y2), ..., (xT, yT) }
   Allows velocity and acceleration estimation & future path prediction!""",
        "content": """### 1. Conceptual Framework of Visual Motion Tracking
Visual tracking is the problem of estimating the continuous trajectory of one or more moving objects over time in an image sequence:
$$\\text{Trajectory } \\mathcal{T} = \\left\\{ \\mathbf{x}_t = (x_t, y_t) \\right\\}_{t=1}^T$$
It creates a temporal correspondence between detected target regions across successive video frames.

---

### 2. Major Tracking Paradigms

#### 1. Point Tracking
* **Mechanism:** Represents target objects as points (e.g. centroid or bounding box center). Association across frames is established using statistical state estimators:
  * **Kalman Filter:** Assumes linear object kinematics with additive Gaussian noise. Executes predict-update recursions for state $\\mathbf{x}_t = [x, y, v_x, v_y]^T$.
  * **Multiple Hypothesis Tracking (MHT):** Evaluates combinatorial associations across multiple future frames for multi-target tracking.

#### 2. Kernel / Appearance Tracking (Mean-Shift and CamShift)
* **Principle:** Uses an appearance model (typically a color histogram) inside an elliptical or rectangular kernel.
* **Mean-Shift Algorithm:**
  1. Represent the target by a reference color histogram $\\mathbf{q} = \\{q_u\\}_{u=1}^M$.
  2. In frame $t+1$, calculate a candidate histogram $\\mathbf{p}(\\mathbf{y})$ at location $\\mathbf{y}$.
  3. Formulate the similarity via the **Bhattacharyya Coefficient**:
     $$\\rho(\\mathbf{p}(\\mathbf{y}), \\mathbf{q}) = \\sum_{u=1}^M \\sqrt{p_u(\\mathbf{y}) q_u}$$
  4. Compute the **Mean-Shift Vector** $\\mathbf{m}(\\mathbf{y})$ that points toward the direction of maximum probability increase:
     $$\\mathbf{m}(\\mathbf{y}) = \\frac{\\sum_i \\mathbf{x}_i w_i g\\left(\\left\\| \\frac{\\mathbf{y} - \\mathbf{x}_i}{h} \\right\\|^2\\right)}{\\sum_i w_i g\\left(\\left\\| \\frac{\\mathbf{y} - \\mathbf{x}_i}{h} \\right\\|^2\\right)} - \\mathbf{y}$$
  5. Translate the kernel by $\\mathbf{m}(\\mathbf{y})$ and repeat until convergence ($|\\mathbf{m}| < \\epsilon$).
* **CamShift (Continuously Adaptive Mean Shift):** Dynamically scales and rotates the search window size to track objects zooming toward or away from the camera.

#### 3. Silhouette & Contour Tracking
* Tracks complex non-rigid object boundaries (e.g. walking humans) using Active Contours (Snakes) or Level Sets.

---

### 3. Trajectory Estimation & Practical Applications
* **Kinematic Parameter Extraction:**
  $$\\text{Instantaneous Velocity: } \\mathbf{v}_t = \\frac{\\mathbf{x}_t - \\mathbf{x}_{t-1}}{\\Delta t}$$
  $$\\text{Acceleration: } \\mathbf{a}_t = \\frac{\\mathbf{v}_t - \\mathbf{v}_{t-1}}{\\Delta t}$$
* **Trajectory Smoothing:** Applying spline interpolation or Kalman smoothing removes jitter caused by measurement noise.
* **Trajectory Prediction:** Projects object paths to anticipate collisions in Advanced Driver Assistance Systems (ADAS) and robot navigation."""
    },
    {
        "id": "MID2-Q17",
        "mid": "Mid-II",
        "qno": 17,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Analyze image and video matting techniques and evaluate their effectiveness in foreground extraction under complex backgrounds.",
        "punchline": "Digital matting solves the under-constrained composite equation I = αF + (1-α)B (7 unknowns, 3 equations); guided by a user Trimap; implemented via Sampling-based, Laplacian closed-form, and Deep Learning matting.",
        "mnemonic": "C-T-S-A-D: Composite equation, Trimap (F/B/U), Sampling, Affinity/Laplacian, Deep matting",
        "analogy": "Creating green-screen movie magic for wispy flyaway hair: Binary segmentation gives a jagged, fake plastic cutout; alpha matting calculates the fractional transparency (alpha) of every individual strand of hair.",
        "diagram": """DIGITAL MATTING COMPOSITION & TRIMAP:

1. THE MATTING EQUATION:
   I(x, y) = α(x, y) · F(x, y) + (1 - α(x, y)) · B(x, y)
   - I: Observed RGB pixel  (3 knowns: R, G, B)
   - F: True Foreground RGB (3 unknowns)
   - B: True Background RGB (3 unknowns)
   - α: Opacity Matte [0, 1] (1 unknown)
   Total: 3 Equations vs 7 Unknowns ──► Severely Under-Constrained!

2. USER-DEFINED TRIMAP:
   ┌──────────────────────────────────────────────┐
   │ Known Background (α = 0)                     │
   │            ╭───────────────────╮             │
   │            │ UNKNOWN BAND (0 < α < 1)        │
   │            │    ╭─────────╮    │             │
   │            │    │ KNOWN   │    │             │
   │            │    │ FORE-   │    │             │
   │            │    │ GROUND  │    │             │
   │            │    │ (α = 1) │    │             │
   │            │    ╰─────────╯    │             │
   │            ╰───────────────────╯             │
   └──────────────────────────────────────────────┘""",
        "content": """### 1. The Digital Matting Problem Formulation
Image and video matting is the technique of soft, fractional extraction of a foreground object from a background image. Unlike hard binary segmentation ($M \\in \\{0, 1\\}$), matting estimates continuous pixel opacity (**Alpha Matte $\\alpha \\in [0, 1]$**).

#### The Fundamental Matting Equation:
Every observed pixel color $\\mathbf{I} = [I_R, I_G, I_B]^T$ is modeled as a convex linear combination of an unknown foreground color $\\mathbf{F}$ and an unknown background color $\\mathbf{B}$:
$$\\mathbf{I} = \\alpha \\mathbf{F} + (1 - \\alpha) \\mathbf{B}$$
* **Mathematical Under-determination:**
  * **Knowns:** 3 observable values ($I_R, I_G, I_B$).
  * **Unknowns:** 7 variables ($\\alpha, F_R, F_G, F_B, B_R, B_G, B_B$).
  * Since there are 7 unknowns and only 3 equations at each pixel, matting is **severely ill-posed and under-constrained**.

---

### 2. The User-Guided Trimap
To constrain the solution, matting algorithms require a **Trimap** that segments the image into three distinct regions:
1. **Known Foreground ($\\\\Omega_F$):** $\\alpha = 1$ (definitely object).
2. **Known Background ($\\\\Omega_B$):** $\\alpha = 0$ (definitely background).
3. **Unknown Region ($\\\\Omega_U$):** $0 < \\alpha < 1$ (boundaries containing fine hair, fur, smoke, transparent glass, or motion blur). The matting algorithm only solves for $\\alpha$ inside $\\Omega_U$.

---

### 3. In-Depth Analysis of Major Matting Techniques

#### 1. Color Sampling-Based Matting (Bayesian / Robust Matting)
* **Mechanism:** For an unknown pixel $\\mathbf{I}$, collects neighboring known foreground samples $\\mathbf{F}_i \\in \\Omega_F$ and background samples $\\mathbf{B}_j \\in \\Omega_B$. Estimates the best pair $(\\hat{\\mathbf{F}}, \\hat{\\mathbf{B}})$ that explains $\\mathbf{I}$:
  $$\\alpha = \\frac{(\\mathbf{I} - \\hat{\\mathbf{B}})^T (\\hat{\\mathbf{F}} - \\hat{\\mathbf{B}})}{\\|\\hat{\\mathbf{F}} - \\hat{\\mathbf{B}}\\|^2}$$
* **Evaluation under Complex Backgrounds:**
  * Performs poorly when foreground and background colors overlap or when the background is heavily textured (causes incorrect sample pairing).

#### 2. Affinity-Based / Closed-Form Matting (Levin\\'s Matting Laplacian)
* **Theoretical Foundation:** Assumes that foreground $\\mathbf{F}$ and background $\\mathbf{B}$ are locally linear functions of spatial coordinates in a small $3 \\times 3$ window $w_k$.
* **Formulation:** Minimizes a quadratic cost function:
  $$J(\\boldsymbol{\\alpha}) = \\boldsymbol{\\alpha}^T \\mathbf{L} \\boldsymbol{\\alpha} + \\lambda (\\boldsymbol{\\alpha} - \\mathbf{b})^T \\mathbf{D} (\\boldsymbol{\\alpha} - \\mathbf{b})$$
  where $\\mathbf{L}$ is the **Matting Laplacian Matrix**:
  $$L_{ij} = \\sum_{k | (i, j) \\in w_k} \\left( \\delta_{ij} - \\frac{1}{|w_k|} \\left( 1 + (\\mathbf{I}_i - \\boldsymbol{\\mu}_k)^T \\left( \\mathbf{\\Sigma}_k + \\frac{\\epsilon}{|w_k|} \\mathbf{I}_3 \\right)^{-1} (\\mathbf{I}_j - \\boldsymbol{\\mu}_k) \\right) \\right)$$
* **Evaluation:**
  * **Globally Optimal:** Solved via a single sparse linear system $(\\mathbf{L} + \\lambda \\mathbf{D}) \\boldsymbol{\\alpha} = \\lambda \\mathbf{b}$.
  * Handles intricate semi-transparent hair and smoke with exceptional mathematical precision.

#### 3. Deep Learning Matting (Deep Image Matting - DIM / MODNet)
* **Mechanism:** Employs encoder-decoder convolutional networks with skip connections and attention modules.
* **Evaluation:** High-level semantic features allow trimap-free or rough-scribble matting on arbitrary complex backgrounds.

---

### 4. Video Matting & Temporal Coherence
In video sequences, applying frame-by-frame image matting produces severe temporal flickering. Video matting enforces **temporal smoothness** by adding an inter-frame optical flow consistency term:
$$J_{\\text{video}}(\\boldsymbol{\\alpha}) = \\sum_t J_t(\\boldsymbol{\\alpha}_t) + \\gamma \\sum_t \\|\\alpha_t(x + u, y + v) - \\alpha_{t+1}(x, y)\\|^2$$"""
    },
    {
        "id": "MID2-Q18",
        "mid": "Mid-II",
        "qno": 18,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "A)  Particle Weight Normalization Given particle weights: Tasks: Normalize weights  Identify most likely particle  Explain robustness to uncertainty  B)  State Update (Kalman Filter) Given: Predicted state  x−=50 Measurement  z=60 Kalman Gain  K=0.6  Compute updated state:  x=x−+K(z−x−) Interpret motion correction",
        "punchline": "Part A: Normalized weights W=[0.2, 0.3, 0.1, 0.4]; Particle 4 is most likely (40%); handles multimodal uncertainty. Part B: Kalman update x = 50 + 0.6(60 - 50) = 56; corrects state 60% toward sensor measurement.",
        "mnemonic": "N-M-K-U: Normalize weights, Max likely particle, Kalman innovation, Updated state",
        "analogy": "Part A is a four-person jury voting on a suspect's location; Part B is trusting a GPS reading (60) by 60% while trusting your car's internal speedometer prediction (50) by 40%, meeting at 56.",
        "diagram": """PART A: PARTICLE FILTER WEIGHT NORMALIZATION
  Particles:        [ P1 ]    [ P2 ]    [ P3 ]    [ P4 ]
  Raw Weights:       0.2       0.3       0.1       0.4
  Sum of Weights S = 0.2 + 0.3 + 0.1 + 0.4 = 1.0
  Normalized w~_i = w_i / S:
                    [ 0.20 ]  [ 0.30 ]  [ 0.10 ]  [ 0.40 ]
                                                     ▲
  Most Likely Particle ──────────────────────────────┘ (Max Weight = 0.4 / 40%)

PART B: KALMAN FILTER STATE UPDATE
  Predicted Prior State x^- = 50  ──────────┐
                                            ▼
  Sensor Measurement    z = 60    ──► Innovation = (z - x^-) = 60 - 50 = +10
                                            │
  Kalman Gain K = 0.6 ──────────────────────┼──► Correction = K · 10 = +6
                                            │
  Updated Posterior State x = 50 + 6 = 56 ◄─┘
  (60% trust in sensor, 40% trust in prediction)""",
        "content": """### PART A: Numerical Problem on Particle Weight Normalization

#### 1. Given Data
* Particle weights vector:
  $$\\mathbf{W} = [w_1, w_2, w_3, w_4] = [0.2, 0.3, 0.1, 0.4]$$

---

#### 2. Task 1: Normalize the Weights
In Particle Filtering (Sequential Importance Sampling), the weights represent unnormalized importance densities. The normalized weight $\\tilde{w}_i$ for each particle $i$ must sum to $1$:
$$\\tilde{w}_i = \\frac{w_i}{\\sum_{j=1}^N w_j}$$

**Step 1: Compute the Total Weight Sum ($S$):**
$$S = \\sum_{j=1}^4 w_j = 0.2 + 0.3 + 0.1 + 0.4 = \\mathbf{1.0}$$

**Step 2: Compute Individual Normalized Weights:**
* **Particle 1:** $\\tilde{w}_1 = \\frac{0.2}{1.0} = \\mathbf{0.20}$
* **Particle 2:** $\\tilde{w}_2 = \\frac{0.3}{1.0} = \\mathbf{0.30}$
* **Particle 3:** $\\tilde{w}_3 = \\frac{0.1}{1.0} = \\mathbf{0.10}$
* **Particle 4:** $\\tilde{w}_4 = \\frac{0.4}{1.0} = \\mathbf{0.40}$

$$\\mathbf{Normalized\\ Weights\\ Vector: } \\quad \\mathbf{\\tilde{W}} = \\mathbf{[0.20, 0.30, 0.10, 0.40]}$$
$$\\text{Verification: } \\sum_{i=1}^4 \\tilde{w}_i = 0.20 + 0.30 + 0.10 + 0.40 = 1.00 \\quad \\text{(Valid Probability Distribution)}$$

---

#### 3. Task 2: Identify the Most Likely Particle
The most likely particle corresponds to the particle index possessing the maximum normalized weight:
$$i^* = \\arg\\max_{i \\in \\{1, 2, 3, 4\\}} \\{\\tilde{w}_i\\}$$
$$\\max(0.20, 0.30, 0.10, 0.40) = 0.40 \\quad (\\text{Particle } 4)$$

$$\\mathbf{Answer: } \\quad \\mathbf{Particle\\ 4} \\text{ is the Most Likely Particle with probability weight } \\mathbf{0.40\\; (40\\%)}.$$

---

#### 4. Task 3: Explain Robustness to Uncertainty
Particle filtering is inherently robust to real-world visual tracking uncertainty because:
1. **Non-Gaussian & Multi-Modal State Representation:** Unlike Kalman filters (which track a single mean and covariance), particle filters maintain multiple discrete hypotheses simultaneously. If an object passes behind a pillar or tree, particles cluster on multiple possible exit paths without losing tracking lock.
2. **Resampling Survival of the Fittest:** During resampling, particles with low weights (Particle 3 with $\\tilde{w}_3 = 0.10$) are discarded, while particles with high weights (Particle 4 with $\\tilde{w}_4 = 0.40$) are replicated with slight perturbations, concentrating computational power on promising trajectories.

---

### PART B: Numerical Problem on Kalman Filter State Update

#### 1. Given Data
* Prior Predicted State estimate: $\\hat{x}^- = 50$
* Noisy Measurement from sensor: $z = 60$
* Kalman Gain: $K = 0.6$

---

#### 2. Task 1: Compute the Updated State ($\\hat{x}$)
The Kalman filter posterior state update equation is:
$$\\hat{x} = \\hat{x}^- + K \\left(z - \\hat{x}^-\\right)$$

**Step-by-Step Calculation:**
1. Compute the **Measurement Residual / Innovation** ($y$):
   $$y = z - \\hat{x}^- = 60 - 50 = +10$$
2. Scale the innovation by the **Kalman Gain** ($K$):
   $$K \\cdot y = 0.6 \\times 10 = +6$$
3. Compute the **Updated Posterior State** ($\\hat{x}$):
   $$\\hat{x} = 50 + 6 = \\mathbf{56}$$

$$\\mathbf{Final\\ Calculated\\ State: } \\quad \\mathbf{\\hat{x} = 56}$$

---

#### 3. Task 2: Interpret Motion Correction
1. **Innovation Interpretation ($z - \\hat{x}^- = +10$):**
   * The positive innovation value ($+10$) reveals that the actual measured physical position ($60$) is $10$ units ahead of where the internal dynamic motion model predicted the object would be ($50$). This indicates unexpected target acceleration or positive velocity deviation.
2. **Kalman Gain Weighting ($K = 0.6$):**
   * The Kalman gain $K = \\frac{P^-}{P^- + R} = 0.6$ represents the optimal relative trust placed in the sensor measurement versus the model prediction.
   * A value of $0.6$ means the filter places **$60\\%$ trust in the new sensor measurement** and **$40\\%$ trust in the internal model prediction**.
3. **Motion Correction Effect:**
   * Rather than blindly jumping all the way to $60$ (which would incorporate full sensor noise) or rigidly staying at $50$ (which would ignore sensor evidence), the filter pulls the state estimate **$60\\%$ of the distance towards the measurement**:
     $$\\hat{x} = (1 - K) \\hat{x}^- + K z = (0.4 \\times 50) + (0.6 \\times 60) = 20 + 36 = 56$$
   * This successfully suppresses $40\\%$ of high-frequency measurement noise while dynamically correcting the tracking trajectory toward real target motion."""
    },
    {
        "id": "MID2-Q19",
        "mid": "Mid-II",
        "qno": 19,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Design a video segmentation and tracking framework by integrating change detection and motion analysis for real-time applications.",
        "punchline": "An end-to-end framework integrates adaptive background subtraction (MoG), morphological filtering, multi-feature association via the Hungarian algorithm, and Kalman filtering for real-time multi-target tracking.",
        "mnemonic": "P-D-F-A-T-M: Preprocessing, Detection (MoG), Features, Association (Hungarian), Tracking (Kalman), Management",
        "analogy": "An air traffic control radar system: Radar pulses detect flying objects (change detection), cameras capture their size/type (feature extraction), and computer algorithms match signals to flight numbers while updating continuous flight paths (tracking).",
        "diagram": """INTEGRATED REAL-TIME VIDEO SEGMENTATION & TRACKING ARCHITECTURE:

Live Video Stream (30 fps)
       │
       ▼
┌─────────────────────────────────┐
│ 1. Spatio-Temporal Preprocessing │  Gaussian Blur G_σ (Noise reduction) + Resize
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 2. Change Detection & Segment   │  Mixture of Gaussians (MoG2) Background Subtraction
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 3. Morphological Post-Processing│  Opening (removes salt-pepper) + Closing (fills holes)
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 4. Feature Extraction           │  Bounding Boxes, Centroids, HSV Histograms, Deep Embed
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 5. Data Association Engine      │  Cost Matrix C = α·IoU_cost + (1-α)·Feature_dist
│    (Hungarian Algorithm)        │  Optimal matching between Existing Tracks & New Detections
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 6. State Estimation (Kalman)    │  Predict & Update kinematics: X = [x, y, vx, vy]^T
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ 7. Track Life-Cycle Management  │  Track Birth (New detection)
│    & Occlusion Handling         │  Track Maintenance (Matched)
└──────────────┬──────────────────┘  Track Termination (Missing for >30 frames)
               │
               ▼
[ Output Annotated Video Stream & Analytics Dashboard ]""",
        "content": """### 1. System Overview & Engineering Objectives
Real-time video segmentation and tracking is the core computational backbone for autonomous vehicles (Tesla/Waymo), intelligent surveillance, and robotic automation.
* **Core Goal:** Detect moving objects, distinguish them from dynamic background clutter, maintain persistent unique identities (Track IDs), and estimate continuous trajectories at **$\\ge 30\\text{ frames per second (fps)}$**.

---

### 2. Stage-by-Stage Framework Pipeline Design

#### Stage 1: Spatio-Temporal Preprocessing
* Input frames are scaled to standard processing resolution ($640 \\times 360$ or $1280 \\times 720$).
* A $3 \\times 3$ Gaussian smoothing filter is applied to attenuate high-frequency CMOS sensor noise without blurring structural edges.

#### Stage 2: Adaptive Change Detection (MoG2 Background Subtraction)
* Every pixel is modeled by $K = 3$ to $5$ adaptive Gaussians.
* Outputs a binary foreground mask:
  $$M(x, y, t) = \\begin{cases} 1 & \\text{if pixel deviates from background by } > 2.5\\sigma \\\\ 0 & \\text{otherwise} \\end{cases}$$
* Effectively handles dynamic outdoor swaying trees, rippling shadows, and slow ambient daylight shifts.

#### Stage 3: Morphological Post-Processing
* **Morphological Opening (Erosion followed by Dilation):** Using a $3 \\times 3$ structuring element eliminates isolated single-pixel noise spikes.
* **Morphological Closing (Dilation followed by Erosion):** Fills internal holes and bridges small fractures within detected objects.
* Connected Component Analysis extracts solid connected blobs with bounding boxes $B_k = [x, y, w, h]$.

#### Stage 4: Multi-Modal Feature Extraction
For each detected foreground blob:
1. **Spatial Features:** Centroid $(c_x, c_y)$, bounding box aspect ratio, and area.
2. **Appearance Features:** 16-bin Hue-Saturation color histogram $\\mathbf{h}$ and deep CNN Re-ID appearance embedding vector $\\mathbf{f} \\in \\mathbb{R}^{128}$.

#### Stage 5: Global Data Association via the Hungarian Algorithm
* Constructs a pairwise assignment cost matrix $\\mathbf{C}$ between $N$ existing active tracks and $M$ new detections:
  $$C_{ij} = w_1 \\cdot \\left(1 - \\text{IoU}(B_i, B_j)\\right) + w_2 \\cdot \\|\\mathbf{f}_i - \\mathbf{f}_j\\|$$
* The **Hungarian (Munkres) Algorithm** solves the global bipartite assignment in $O(N^3)$ operations, uniquely assigning detections to existing tracks without ambiguity.

#### Stage 6: Kinematic State Estimation via Kalman Filtering
* Each active track maintains an independent 2D Kalman filter:
  $$\\mathbf{x}_t = [x, y, v_x, v_y]^T$$
* **Predict Step:** Projects target position into frame $t$ based on estimated velocity.
* **Update Step:** Merges predicted state with matched detection measurement to smooth out sensor jitter.

#### Stage 7: Track Life-Cycle Management & Occlusion Handling
1. **Track Birth:** An unassociated detection appearing consistently across 3 consecutive frames initiates a new unique Track ID.
2. **Occlusion Handling:** If an object is temporarily occluded (passes behind a pillar or another vehicle), its Kalman filter continues predicting position based on velocity for up to 30 frames ($1\\text{ second}$).
3. **Track Death:** If no matching detection arrives for $>30$ consecutive frames, the track is terminated, freeing memory.

---

### 3. Real-Time Latency & Performance Optimization
1. **Parallel Multi-threading:** Pipeline stages (detection, association, tracking) run concurrently across separate CPU/GPU threads in a ring buffer.
2. **Region-of-Interest (ROI) Cropping:** Background subtraction is evaluated only within predicted motion bounding boxes rather than the entire frame, saving **$60\\%$ computational power**."""
    },
    {
        "id": "MID2-Q20",
        "mid": "Mid-II",
        "qno": 20,
        "unit": "Unit-5",
        "co": "CO5",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Develop and optimize a performance evaluation model for video segmentation and tracking using metrics such as IoU, precision, recall, and F1-score",
        "punchline": "Segmentation is evaluated pixel-wise via Confusion Matrix (TP, FP, FN), IoU (Jaccard Index), Precision, Recall, and F1-score; Tracking is evaluated via MOTA, MOTP, and ID Switches.",
        "mnemonic": "C-I-P-R-F-M: Confusion Matrix, IoU, Precision, Recall, F1-Score, MOTA",
        "analogy": "A medical test: Precision measures how many people flagged as sick are actually sick; Recall measures how many sick people the test caught; IoU measures the spatial overlap of an ultrasound tumor scan with surgical reality.",
        "diagram": """PERFORMANCE EVALUATION MODEL ARCHITECTURE:

1. SEGMENTATION SPATIAL OVERLAP (IoU / Jaccard Index):
   ┌──────────────────────┐
   │ Ground Truth Mask A  │
   │      ┌───────────────┼──────────────┐
   │      │ Intersection  │ Prediction   │
   │      │ (TP)          │ Mask B       │
   │      │               │ (FP)         │
   └──────┼───────────────┘              │
     (FN) └──────────────────────────────┘

               Area of Overlap (A ∩ B)             TP
   IoU = ────────────────────────────────── = ──────────────
         Area of Union (A ∪ B)                TP + FP + FN

2. EVALUATION METRICS FORMULAS:
   - Precision = TP / (TP + FP)         (Quality / Purity of detections)
   - Recall    = TP / (TP + FN)         (Completeness / Coverage)
   - F1-Score  = 2 · (P · R) / (P + R)  (Harmonic Mean)

3. MULTI-OBJECT TRACKING EVALUATION (CLEAR MOT):
   - MOTA = 1 - (FN + FP + ID_Switches) / Ground_Truth_Objects
   - MOTP = Total_Bounding_Box_Distance / Total_Matched_Detections""",
        "content": """### 1. Conceptual Framework of Performance Evaluation
A robust evaluation model quantifies how accurately an automated video segmentation and tracking algorithm matches human-annotated Ground Truth (GT). Evaluation operates at two levels:
1. **Spatial Segmentation Level (Pixel / Bounding Box accuracy)**
2. **Temporal Tracking Level (Identity continuity across video frames)**

---

### 2. Spatial Segmentation Evaluation Metrics

#### 1. The Confusion Matrix
At the pixel or detection level, comparisons between Prediction ($P$) and Ground Truth ($G$) fall into four categories:
* **True Positive ($TP$):** Moving foreground pixel correctly detected as foreground.
* **False Positive ($FP$):** Static background pixel incorrectly classified as foreground (**False Alarm**).
* **False Negative ($FN$):** Moving foreground pixel missed by the algorithm (**Missed Detection**).
* **True Negative ($TN$):** Static background pixel correctly classified as background.

#### 2. Intersection over Union (IoU / Jaccard Index)
The primary spatial overlap metric between predicted region $A$ and ground truth region $B$:
$$\\text{IoU} = \\frac{\\text{Area of Overlap}}{\\text{Area of Union}} = \\frac{|A \\cap B|}{|A \\cup B|} = \\frac{TP}{TP + FP + FN}$$
* **Threshold Convention:** In standard benchmarks (PASCAL VOC, COCO), an object detection is considered a True Positive if $\\text{IoU} \\ge 0.50$ (or $0.75$).

#### 3. Precision ($P$)
Measures the purity/accuracy of the positive detections:
$$\\text{Precision} = \\frac{TP}{TP + FP}$$
* High precision means when the algorithm claims an object is present, it is almost certainly correct (very few false alarms).

#### 4. Recall / Sensitivity ($R$)
Measures the completeness of foreground detection:
$$\\text{Recall} = \\frac{TP}{TP + FN}$$
* High recall means the algorithm caught almost all moving objects in the scene (very few missed detections).

#### 5. F1-Score (Dice Coefficient)
The harmonic mean of Precision and Recall, providing a single balanced metric:
$$F_1 = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2 TP}{2 TP + FP + FN}$$

---

### 3. Step-by-Step Numerical Worked Example
Consider a video surveillance evaluation where pixel-level testing yields:
* $TP = 800\\text{ pixels}$
* $FP = 100\\text{ pixels}$
* $FN = 200\\text{ pixels}$
* $TN = 98,900\\text{ pixels}$

#### Computations:
1. **Intersection over Union (IoU):**
   $$\\text{IoU} = \\frac{800}{800 + 100 + 200} = \\frac{800}{1100} = \\mathbf{0.727\\; (72.7\\%)}$$
2. **Precision ($P$):**
   $$P = \\frac{800}{800 + 100} = \\frac{800}{900} = \\mathbf{0.889\\; (88.9\\%)}$$
3. **Recall ($R$):**
   $$R = \\frac{800}{800 + 200} = \\frac{800}{1000} = \\mathbf{0.800\\; (80.0\\%)}$$
4. **F1-Score ($F_1$):**
   $$F_1 = 2 \\times \\frac{0.889 \\times 0.800}{0.889 + 0.800} = \\frac{1.4224}{1.689} = \\mathbf{0.842\\; (84.2\\%)}$$

---

### 4. Temporal Multi-Object Tracking Metrics (CLEAR MOT Standard)
For tracking sequences, spatial metrics are insufficient because they ignore track identity continuity. The CLEAR MOT benchmark introduces:

#### 1. Multiple Object Tracking Accuracy (MOTA)
Combines false positives, missed detections, and identity switches into a single composite score:
$$\\text{MOTA} = 1 - \\frac{\\sum_t (FN_t + FP_t + IDSW_t)}{\\sum_t GT_t}$$
* **IDSW (Identity Switches):** Number of times a tracking algorithm switches the persistent identity between two distinct objects (e.g. crossing pedestrians).
* **MOTA Range:** $(-\\infty, 100\\%]$. Values $>70\\%$ indicate state-of-the-art performance.

#### 2. Multiple Object Tracking Precision (MOTP)
Measures the average spatial localization error between matched detections and ground truth bounding boxes:
$$\\text{MOTP} = \\frac{\\sum_{t, i} d_{t, i}}{\\sum_t c_t}$$
where $d_{t, i}$ is the distance/overlap error for matched detection pair $i$ at frame $t$, and $c_t$ is the number of matches."""
    }
]
