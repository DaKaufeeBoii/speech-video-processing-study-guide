# -*- coding: utf-8 -*-
"""
Unit 4: Image Formation, Motion Models, Motion Estimation & 3D Structure
Questions: Mid-II Q5 to Q12
Course Coordinator: Dr. Sandeep Kumar M (CSE AI & ML)
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408
Strictly aligned with unit 4.docx lecture notes and official Question Bank.
"""

UNIT4_QUESTIONS = [
    {
        "id": "MID2-Q05",
        "mid": "Mid-II",
        "qno": 5,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Categorize various image formation models and examine their role in motion estimation.",
        "punchline": "Image formation models describe how 3D real-world scenes convert into digital pixels through Geometric, Photometric, Optical, and Sampling models; they enable motion estimation to differentiate true physical movement from lighting shifts, blur, and sensor quantization.",
        "mnemonic": "G-P-O-S: Geometric (projection), Photometric (light), Optical (lens blur), Sampling (pixels).",
        "analogy": "Like investigating a car accident recorded on a dashcam: you must account for camera angle/perspective (geometric), streetlamp reflections (photometric), windshield rain blur (optical), and camera sensor pixel resolution (sampling) to calculate the car's true speed.",
        "diagram": """+-------------------------------------------------------------------------------+
|             IMAGE FORMATION PRINCIPLES & MOTION ESTIMATION PIPELINE           |
+-------------------------------------------------------------------------------+

 IMAGE FORMATION MODELS:
  1. Geometric Model    ──► 3D-to-2D Perspective projection: (X, Y, Z) ──► (x, y)
  2. Photometric Model  ──► Irradiance & surface reflectance: I(x, y) = R(x, y) · L(x, y)
  3. Optical Model      ──► Lens focus, depth-of-field, lens distortion, motion blur
  4. Sampling & Quant   ──► Spatial grid sampling (pixels) + intensity quantization

 MOTION ESTIMATION FRAMEWORK:
  [ Frame t ] & [ Frame t+1 ]
         │
         ▼
  [ 1. Image Formation Analysis ] ──► Isolates lighting changes, lens blur & sensor noise
         │
         ▼
  [ 2. Feature Extraction ]       ──► Detects corners, edges, robust keypoints (SIFT/ORB)
         │
         ▼
  [ 3. Correspondence Matching ]  ──► Establishes spatial correspondence between frames
         │
         ▼
  [ 4. Motion Estimation ]        ──► Block matching / Optical flow calculates displacement
         │
         ▼
  [ Output Motion Vectors ]       ──► Generates (u, v) trajectory for video compression/tracking""",
        "content": """### 1. Fundamental Principles of Image Formation Models (Unit 4 Notes)
An **image formation model** mathematically describes how a physical 3D scene is projected, illuminated, focused, and converted into a 2D digital image matrix by an optical camera system. In video processing, understanding these models is vital for motion estimation algorithms to identify true object displacement between consecutive frames without being deceived by lighting or sensor artifacts.

The four fundamental models are:
1. **Geometric Model:**
   - **Principle:** Describes the mathematical 3D-to-2D perspective projection of real-world coordinates $(X, Y, Z)$ onto the 2D camera image plane $(x, y)$. Governed by focal length $f$, camera position, orientation, and vanishing points:
     $$x = f \\frac{X}{Z}, \\quad y = f \\frac{Y}{Z}$$
   - **Role:** Explains scale changes and perspective distortions (e.g., an approaching vehicle appears larger as depth $Z$ decreases).
2. **Photometric / Illumination Model:**
   - **Principle:** Models how ambient lighting interacts with object surface reflectance properties to produce image irradiance:
     $$I(x, y) = \\rho(x, y) \\cdot E(x, y)$$
     where $\\rho$ is surface reflectance and $E$ is incident illumination.
   - **Role:** Enables motion estimation algorithms to distinguish true object movement from brightness variations caused by passing clouds or shadows.
3. **Optical Model:**
   - **Principle:** Accounts for physical lens properties, aperture diffraction, depth-of-field, radial distortion, and optical blur.
   - **Role:** Fast-moving objects undergo motion blur; optical models allow algorithms to model blurred point spread functions (PSF) rather than failing feature matches.
4. **Sampling and Quantization Model:**
   - **Principle:** Converts continuous optical irradiance into discrete spatial pixels $(m \\Delta x, n \\Delta y)$ and quantizes intensity into finite digital levels (e.g., 8-bit integers $0\\dots255$).
   - **Role:** Accounts for spatial resolution limits and quantization noise that can destabilize gradient calculations in small-displacement motion estimation.

---

### 2. Role of Image Formation Models in Motion Estimation Frameworks
Motion estimation calculates the displacement vectors $\\mathbf{d} = (u, v)$ between consecutive frames $F_t$ and $F_{t+1}$. Image formation analysis acts as the foundation of the 5-stage motion estimation framework:
1. **Frame Capture ($F_t, F_{t+1}$):** Ingests sequential video frames separated by temporal interval $\\Delta t$.
2. **Image Formation Normalization:** Uses photometric models to normalize global illumination changes and optical models to correct for lens radial distortion.
3. **Feature Extraction & Matching:** Extracts salient, scale-invariant features (corners, edges, SIFT/ORB) that remain invariant under perspective projection.
4. **Displacement Computation:** Applies Block Matching Algorithms (BMA) or differential Optical Flow to derive spatial displacements $(u, v)$.
5. **Output Motion Vectors:** Outputs vector fields utilized for temporal motion compensation (H.264/HEVC) or object trajectory tracking."""
    },
    {
        "id": "MID2-Q06",
        "mid": "Mid-II",
        "qno": 6,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Discuss different motion models and the assumptions underlying motion estimation in video processing.",
        "punchline": "Motion models mathematically describe how object coordinates shift across frames via Translation, Rotation, Affine, and Optical Flow models; they rely on assumptions of constant velocity, rigidity, brightness constancy, and limited occlusion.",
        "mnemonic": "T-R-A-O: Translation, Rotation, Affine, Optical Flow. Assumptions: C-R-B-L (Constant velocity, Rigidity, Brightness constancy, Limited occlusion).",
        "analogy": "Like predicting the path of a hockey puck across ice: you assume the ice is smooth (constant velocity), the puck stays intact (rigidity), the stadium lights don't flicker (brightness constancy), and other players don't block the camera view (limited occlusion).",
        "diagram": """+-------------------------------------------------------------------------------+
|                    MOTION MODELS & PHYSICAL ASSUMPTIONS                       |
+-------------------------------------------------------------------------------+

 1. TRANSLATION MODEL:               2. ROTATION MODEL:
    x' = x + u                          x' = x cos θ - y sin θ
    y' = y + v                          y' = x sin θ + y cos θ
    (Pure 2D shifting)                  (In-plane rotation around center)

 3. AFFINE MODEL (6-Parameters):     4. DIFFERENTIAL OPTICAL FLOW:
    x' = a₁₁ x + a₁₂ y + t_x            I_x · u + I_y · v + I_t = 0
    y' = a₂₁ x + a₂₂ y + t_y            (Dense pixel-level velocity field)
    (Translation + Scale + Shear)

 UNDERLYING ASSUMPTIONS IN VIDEO PROCESSING:
  ┌──────────────────────┬─────────────────────────────────────────────────────┐
  │ Assumption           │ Physical Meaning & Vulnerability                    │
  ├──────────────────────┼─────────────────────────────────────────────────────┤
  │ Constant Velocity    │ Velocity is constant over short Δt (fails on shock) │
  │ Rigid Objects        │ Shape does not deform (fails for cloth/faces)       │
  │ Brightness Constancy │ Pixel intensity stays constant (fails in shadows)   │
  │ Limited Occlusion    │ Object remains visible (fails behind obstacles)     │
  └──────────────────────┴─────────────────────────────────────────────────────┘""",
        "content": """### 1. Mathematical Representation of Motion Models (Unit 4 Notes)
A motion model describes how the spatial coordinates $(x, y)$ of an object at time $t$ map to new coordinates $(x', y')$ in the subsequent frame at time $t+1$:

#### a) Translation Model (2 Parameters)
- **Equation:**
  $$x' = x + u, \\quad y' = y + v$$
  where $\\mathbf{d} = (u, v)$ is the 2D displacement vector.
- **Characteristics:** Assumes all pixels within an object or block shift by an identical distance without rotation or scale change (e.g., a car driving along a straight highway). Universally used in block-matching video compression (MPEG, H.264).

#### b) Rotation Model
- **Equation:**
  $$x' = x \\cos\\theta - y \\sin\\theta$$
  $$y' = x \\sin\\theta + y \\cos\\theta$$
  where $\\theta$ is the rotation angle around a reference origin.
- **Characteristics:** Models in-plane rotational motion (e.g., spinning wheels, rotating drone cameras).

#### c) Affine Motion Model (6 Parameters)
- **Equation:**
  $$\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = \\begin{bmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} + \\begin{bmatrix} t_x \\\\ t_y \\end{bmatrix}$$
- **Characteristics:** Captures translation, rotation, scaling (zoom), and shear. Highly effective for camera pan/tilt/zoom modeling.

#### d) Optical Flow Model (Dense Pixel Model)
- **Equation:**
  $$I_x u + I_y v + I_t = 0$$
  where $I_x = \\frac{\\partial I}{\\partial x}, I_y = \\frac{\\partial I}{\\partial y}, I_t = \\frac{\\partial I}{\\partial t}$, and $(u, v) = \\left( \\frac{dx}{dt}, \\frac{dy}{dt} \\right)$.
- **Characteristics:** Provides an individual motion vector for every single pixel in the image.

---

### 2. Underlying Assumptions in Real-World Dynamic Scenes (Unit 4 Notes)
Motion estimation algorithms rely on four foundational physical assumptions:

1. **Brightness Constancy Assumption:**
   - *Premise:* The apparent intensity of a moving surface point remains unchanged between consecutive frames:
     $$I(x + u, y + v, t + \\Delta t) = I(x, y, t)$$
   - *Real-world Failure:* Breaks down under sudden lighting variations, specular reflections on metallic/glass surfaces, or passing shadows.
2. **Rigid Object Assumption:**
   - *Premise:* Objects are structurally rigid; the distance between any two surface points on the object remains constant during motion.
   - *Real-world Failure:* Breaks down for non-rigid articulated objects (human body movement, flapping clothing, facial expressions, water waves).
3. **Constant Motion / Velocity Assumption:**
   - *Premise:* The acceleration of moving objects is negligible over the small time interval $\\Delta t$ between frames (typically $33\\text{ ms}$ at 30 fps). Motion is assumed linear.
   - *Real-world Failure:* Breaks down during sudden impacts, vibrations, or rapid direction reversals.
4. **Limited Occlusion Assumption:**
   - *Premise:* Moving objects remain continuously visible and are not obscured by background elements or foreground obstacles.
   - *Real-world Failure:* Breaks down when objects pass behind poles, enter tunnels, or exit the camera frame boundary."""
    },
    {
        "id": "MID2-Q07",
        "mid": "Mid-II",
        "qno": 7,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "A block in Frame 1 is at (20, 25). The best match in Frame 2 is found at (23, 30). 1. Calculate the motion vector. 2. Determine the direction of motion.",
        "punchline": "The motion vector is MV = (3, 5); positive horizontal displacement u = +3 indicates motion to the right, and positive vertical displacement v = +5 indicates motion downward in image coordinates, yielding diagonally downward and rightward movement.",
        "mnemonic": "MV = (x2 - x1, y2 - y1) = (23-20, 30-25) = (3, 5). Down & Right.",
        "analogy": "Like tracking a chess piece moving on a board from square (20, 25) to (23, 30): it shifted 3 squares east and 5 squares south.",
        "diagram": """+-------------------------------------------------------------------------------+
|                    BLOCK MOTION VECTOR DISPLACEMENT GRID                      |
+-------------------------------------------------------------------------------+

  Standard Image Coordinates: Origin (0,0) at Top-Left
  X-axis: Increases to the Right (Horizontal)
  Y-axis: Increases Downward     (Vertical)

  x = 20           x = 23
  ┌────────────────┬────────────────► X (Horizontal)
  │
y=25  • (20, 25) [Frame 1 Block]
  │    \\
  │     \\  u = +3 pixels (Right)
  │      \\
  │       \\  v = +5 pixels (Down)
  │        \\
y=30        ▼ (23, 30) [Frame 2 Best Match]
  │
  ▼
  Y (Vertical)

  Motion Vector: MV = (Δx, Δy) = (23 - 20, 30 - 25) = (3, 5)
  Magnitude    : ||MV|| = √(3² + 5²) = √34 ≈ 5.83 pixels
  Angle        : θ = arctan(5/3) ≈ 59.04° below positive X-axis""",
        "content": """### 1. Problem Statement & Given Coordinates (Unit 4 Notes)
In Block-Based Motion Estimation (BMA), the displacement of an image block between two consecutive video frames is tracked across the spatial coordinate grid.
- **Reference position in Frame 1 ($F_1$):**
  $$(x_1, y_1) = (20, 25)$$
- **Best matching position in Frame 2 ($F_2$):**
  $$(x_2, y_2) = (23, 30)$$

---

### 2. Part 1: Motion Vector Calculation
The motion vector $\\mathbf{MV} = (u, v)$ represents the spatial displacement along the horizontal and vertical axes:
$$u = \\Delta x = x_2 - x_1$$
$$v = \\Delta y = y_2 - y_1$$

Substituting the given coordinate values:
1. **Horizontal Displacement ($u$):**
   $$u = 23 - 20 = +3\\text{ pixels}$$
2. **Vertical Displacement ($v$):**
   $$v = 30 - 25 = +5\\text{ pixels}$$

Therefore, the resulting motion vector is:
$$\\mathbf{MV} = (u, v) = (3, 5)$$

---

### 3. Part 2: Determination & Interpretation of Motion Direction
In standard digital image processing and video display systems:
- The **origin $(0, 0)$** is located at the **top-left corner** of the display.
- The **horizontal axis ($x$)** increases positively from **left to right**.
- The **vertical axis ($y$)** increases positively from **top to bottom**.

#### Directional Analysis:
1. **Horizontal Component ($u = +3$):**
   Since $u > 0$, the positive displacement indicates movement to the **right**.
2. **Vertical Component ($v = +5$):**
   Since $v > 0$, the positive displacement in image coordinates indicates movement **downward**.

#### Comprehensive Directional Verdict:
The block moves **diagonally downward and to the right**.

#### Vector Magnitude and Angle (Additional Rigor):
- **Displacement Magnitude:**
  $$\\|\\mathbf{MV}\\| = \\sqrt{u^2 + v^2} = \\sqrt{3^2 + 5^2} = \\sqrt{9 + 25} = \\sqrt{34} \\approx 5.831\\text{ pixels}$$
- **Displacement Angle:**
  $$\\theta = \\arctan\\left(\\frac{v}{u}\\right) = \\arctan\\left(\\frac{5}{3}\\right) = \\arctan(1.6667) \\approx 59.04^\\circ$$
  *(oriented at $59.04^\\circ$ below the horizontal axis towards the bottom-right).*"""
    },
    {
        "id": "MID2-Q08",
        "mid": "Mid-II",
        "qno": 8,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K4",
        "marks": "05 Marks",
        "title": "Evaluate the performance of differential methods for motion estimation and analyze their sensitivity to noise and illumination changes.",
        "punchline": "Differential methods estimate dense motion via the Optical Flow Constraint equation (Ix·u + Iy·v + It = 0); Lucas-Kanade uses local constancy while Horn-Schunck imposes global smoothness; both are highly sensitive to noise and lighting shifts, requiring Gaussian pre-smoothing and gradient normalization.",
        "mnemonic": "OFC: Ix u + Iy v + It = 0. LK = Local least squares; HS = Global smoothness.",
        "analogy": "Like estimating wind speed by observing how clouds shift: differential methods measure how fast cloud brightness changes across small distances, but if a lightning flash occurs (illumination change) or the camera shakes (noise), the formula falsely reports hurricane-force winds.",
        "diagram": """+-------------------------------------------------------------------------------+
|               DIFFERENTIAL MOTION ESTIMATION & THE APERTURE PROBLEM           |
+-------------------------------------------------------------------------------+

 OPTICAL FLOW CONSTRAINT EQUATION:
   I_x · u + I_y · v + I_t = 0
   [ 1 equation, 2 unknowns (u, v) ==> APERTURE PROBLEM! ]
   (Can only measure motion perpendicular to object edge)

 1. LUCAS-KANADE METHOD (Local):        2. HORN-SCHUNCK METHOD (Global):
    Assumes (u, v) is constant in           Minimizes global energy functional:
    small local window Ω (e.g., 3x3)        E = ∬ [(I_x u + I_y v + I_t)²
    A^T A [u; v] = A^T b                       + α² (|∇u|² + |∇v|²)] dx dy
    Solved via 2x2 matrix inversion         Solved iteratively across full image

 SENSITIVITY & MITIGATION:
  • Sensor Noise ──────► Gaussian smoothing filter G_σ * I
  • Lighting Shifts ───► Illumination normalization / Gradient-based matching
  • Flat Regions ──────► Eigenvalue thresholding (Harris corner check: λ₂ > τ)""",
        "content": """### 1. Principles of Differential Motion Estimation (Unit 4 Notes)
Differential methods (optical flow) estimate motion between consecutive frames by analyzing spatial and temporal image intensity gradients. They are based on the **Brightness Constancy Assumption**:
$$I(x + u, y + v, t + 1) = I(x, y, t)$$

Applying a first-order Taylor series expansion:
$$I(x, y, t) + \\frac{\\partial I}{\\partial x} u + \\frac{\\partial I}{\\partial y} v + \\frac{\\partial I}{\\partial t} \\approx I(x, y, t)$$
Subtracting $I(x, y, t)$ yields the fundamental **Optical Flow Constraint (OFC) Equation**:
$$I_x u + I_y v + I_t = 0$$
where $I_x = \\frac{\\partial I}{\\partial x}, I_y = \\frac{\\partial I}{\\partial y}$ are spatial gradients, $I_t = \\frac{\\partial I}{\\partial t}$ is the temporal gradient, and $(u, v)$ is the motion vector.

#### The Aperture Problem
The OFC provides only **one linear equation for two unknowns $(u, v)$** at each pixel. It can compute motion only in the direction perpendicular to local edge contours (normal flow). Motion parallel to the edge is fundamentally ambiguous.

---

### 2. Differential Methods: Lucas-Kanade vs Horn-Schunck

#### a) Lucas-Kanade Method (Local Technique)
- **Principle:** Assumes that the motion vector $\\mathbf{u} = [u, v]^T$ is constant across a small local spatial neighborhood $\\Omega$ of size $N \\times N$ (e.g., $3 \\times 3$ or $5 \\times 5$ pixels).
- **Formulation:** For $n$ pixels in $\\Omega$:
  $$\\begin{bmatrix} I_{x1} & I_{y1} \\\\ I_{x2} & I_{y2} \\\\ \\vdots & \\vdots \\\\ I_{xn} & I_{yn} \\end{bmatrix} \\begin{bmatrix} u \\\\ v \\end{bmatrix} = - \\begin{bmatrix} I_{t1} \\\\ I_{t2} \\\\ \\vdots \\\\ I_{tn} \\end{bmatrix} \\implies \\mathbf{A} \\mathbf{u} = \\mathbf{b}$$
- **Least-Squares Solution:**
  $$\\mathbf{u} = (\\mathbf{A}^T \\mathbf{A})^{-1} \\mathbf{A}^T \\mathbf{b}$$
- **Condition for Solvability:** The structure tensor $\\mathbf{A}^T \\mathbf{A} = \\begin{bmatrix} \\sum I_x^2 & \\sum I_x I_y \\\\ \\sum I_x I_y & \\sum I_y^2 \\end{bmatrix}$ must be invertible, requiring two large eigenvalues (i.e., the region must be a corner or textured keypoint).

#### b) Horn-Schunck Method (Global Technique)
- **Principle:** Imposes a **global smoothness constraint** across the entire image plane, formulating motion estimation as an energy minimization problem:
  $$E = \\iint \\left[ (I_x u + I_y v + I_t)^2 + \\alpha^2 \\left( \\left(\\frac{\\partial u}{\\partial x}\\right)^2 + \\left(\\frac{\\partial u}{\\partial y}\\right)^2 + \\left(\\frac{\\partial v}{\\partial x}\\right)^2 + \\left(\\frac{\\partial v}{\\partial y}\\right)^2 \\right) \\right] dx \\, dy$$
  where $\\alpha^2$ is a regularization weight controlling flow smoothness.
- **Solution:** Solved iteratively using Gauss-Seidel relaxation. Yields a dense, smooth motion field across all pixels.

---

### 3. Sensitivity Analysis to Noise and Illumination Variations (Unit 4 Notes)

| Environmental Factor | Effect on Motion Estimation | Algorithmic Solution / Mitigation |
| :--- | :--- | :--- |
| **Image Noise (Sensor Grain)** | Numerical derivative operators amplify high-frequency noise, creating corrupt gradients $I_x, I_y$ and erroneous vectors. | Pre-filter frames using a **2D Gaussian smoothing kernel** ($G_\\sigma * I$). |
| **Illumination Changes** | Violates the core Brightness Constancy assumption, generating large artificial temporal gradients $I_t$ and false motion. | Apply **illumination normalization** (histogram equalization) or evaluate gradients of gradient/Laplacian fields. |
| **Low-Texture / Flat Regions** | Spatial gradients $I_x \\approx 0, I_y \\approx 0$, making $\\mathbf{A}^T \\mathbf{A}$ singular and motion undetermined. | Use **spatial regularization** (Horn-Schunck smoothness) or track only Harris corner features. |
| **Large Displacements** | Taylor series approximation fails when object displacement exceeds 1–2 pixels between frames. | Implement **Hierarchical Coarse-to-Fine Gaussian Image Pyramids**. |"""
    },
    {
        "id": "MID2-Q09",
        "mid": "Mid-II",
        "qno": 9,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K4",
        "marks": "10 Marks",
        "title": "Analyze the principles of matching-based motion estimation and compare different search strategies used in block matching algorithms.",
        "punchline": "Matching-based motion estimation tracks macroblocks by minimizing matching criteria like SAD; while Full Search tests all (2p+1)² candidates for optimal accuracy at extreme computational cost, fast search algorithms like TSS and Diamond Search prune evaluations by up to 90%.",
        "mnemonic": "BMA: Full Search (Exhaustive), TSS (Coarse-to-fine), Diamond Search (Shape-adaptive). Cost: SAD, MAD, MSE.",
        "analogy": "Finding a lost shoe in a stadium: Full Search inspects every single seat one by one; Three-Step Search checks seat clusters at major aisles and zooms in; Diamond Search checks immediate neighbors in a diamond pattern until the shoe is spotted.",
        "diagram": """+-------------------------------------------------------------------------------+
|               BLOCK MATCHING ALGORITHMS & SEARCH STRATEGIES                   |
+-------------------------------------------------------------------------------+

 CURRENT FRAME (Frame t)                     REFERENCE FRAME (Frame t-1)
 ┌──────────────────────┐                     ┌───────────────────────────┐
 │                      │                     │      Search Window (±p)   │
 │   ┌──────┐           │                     │      ┌─────────────┐      │
 │   │Block │           │                     │      │  •   •   •  │      │
 │   │16x16 │           │ ──────────────────► │      │  • [Match] •│      │
 │   └──────┘           │                     │      │  •   •   •  │      │
 │    (x, y)            │                     │      └─────────────┘      │
 └──────────────────────┘                     └───────────────────────────┘
                                                Motion Vector: (dx, dy)
 SEARCH STRATEGIES COMPARED:
 1. FULL SEARCH (Exhaustive):
    Tests all (2p+1)² grid points ──► Optimal accuracy, O((2p+1)²) cost.

 2. THREE-STEP SEARCH (TSS):
    Step 1: Check 9 points at step size S=4  ──► Best point becomes center
    Step 2: Check 8 points at step size S=2  ──► Best point becomes center
    Step 3: Check 8 points at step size S=1  ──► Best point is final MV!

 3. DIAMOND SEARCH (DS):
    Large Diamond Pattern (LDSP, 9 points) until center is minimum ──► Small Diamond (SDSP, 5 points)""",
        "content": """### 1. Principles of Matching-Based Motion Estimation (Unit 4 Notes)
Matching-based motion estimation assumes that a moving image region in current frame $F_t$ retains similar pixel intensity in reference frame $F_{t-1}$. In **Block Matching Algorithms (BMA)**, the current frame is partitioned into non-overlapping macroblocks of size $N \\times N$ (typically $8 \\times 8$ or $16 \\times 16$ pixels). For each block at $(x, y)$, the algorithm searches a defined displacement window of size $\\pm p$ in the reference frame to locate candidate position $(x + dx, y + dy)$ that minimizes a distortion cost metric.

#### Matching Distortion Criteria:
1. **Sum of Absolute Differences (SAD):**
   $$\\text{SAD}(dx, dy) = \\sum_{m=0}^{N-1} \\sum_{n=0}^{N-1} |F_t(x+m, y+n) - F_{t-1}(x+m+dx, y+n+dy)|$$
   *(Preferred in hardware codecs because it requires only additions and subtractions, zero multiplications).*
2. **Mean Absolute Difference (MAD):**
   $$\\text{MAD}(dx, dy) = \\frac{1}{N^2} \\text{SAD}(dx, dy)$$
3. **Mean Squared Error (MSE):**
   $$\\text{MSE}(dx, dy) = \\frac{1}{N^2} \\sum_{m=0}^{N-1} \\sum_{n=0}^{N-1} [F_t(x+m, y+n) - F_{t-1}(x+m+dx, y+n+dy)]^2$$

---

### 2. Analysis of Search Strategies (Unit 4 Notes)

#### a) Full Search (Exhaustive Search - FS)
- **Mechanism:** Evaluates the distortion cost at **every single integer candidate location** within the $(2p + 1) \\times (2p + 1)$ search window.
- **Computational Complexity:**
  $$C_{\\text{FS}} = (2p + 1)^2 \\text{ block comparisons per macroblock}$$
  For search parameter $p = 7$, each block requires $(2(7) + 1)^2 = 15^2 = 225$ block evaluations.
- **Performance:** Guarantees locating the **global minimum distortion** within the search window. However, computational latency is prohibitive for real-time HD encoding.

#### b) Three-Step Search (TSS)
- **Mechanism:** A coarse-to-fine search strategy relying on the unimodal error surface assumption:
  - **Step 1:** Set initial step size $S = \\lfloor p/2 \\rfloor = 4$. Test the center $(0,0)$ and 8 surrounding points at distance $S$. Locate candidate with minimum SAD.
  - **Step 2:** Center a new $3 \\times 3$ grid on the best candidate, halve step size ($S = 2$), and test 8 surrounding points.
  - **Step 3:** Halve step size again ($S = 1$), test 8 surrounding points. The minimum point is the final motion vector.
- **Computational Complexity:**
  $$C_{\\text{TSS}} = 9 + 8 + 8 = 25\\text{ block evaluations}$$
  *(Achieves an $89\\%$ reduction in computation compared to Full Search).*

#### c) Diamond Search (DS)
- **Mechanism:** Uses diamond-shaped search patterns matching the circular/isotropic distribution of real-world motion vectors:
  - **Large Diamond Search Pattern (LDSP):** Consists of 9 candidate points (1 center + 8 perimeter points at distance 2). The pattern is shifted until the minimum SAD point occurs at the center point.
  - **Small Diamond Search Pattern (SDSP):** Once the center is selected in LDSP, switch to SDSP (5 points: 1 center + 4 perimeter points at distance 1). The best point in SDSP is the final motion vector.
- **Performance:** Highly efficient; converges in 15–20 evaluations for typical video motion.

---

### 3. Comprehensive Comparison Table of Search Strategies (Unit 4 Notes)

| Search Method | Computational Complexity | Number of Search Points ($p=7$) | Accuracy / Matching Quality | Risk of Local Minima |
| :--- | :--- | :--- | :--- | :--- |
| **Full Search (FS)** | High ($O((2p+1)^2)$) | Exactly **225 points** | **Optimal** (Global minimum) | **None** (Exhaustive check) |
| **Three-Step Search (TSS)** | Low ($O(\\log p)$) | Exactly **25 points** | Good for moderate, linear motion | Moderate (trapped if error non-monotonic) |
| **Diamond Search (DS)** | Very Low | Typically **13 to 21 points** | Superior to TSS for small-to-medium motion | Low for small motion |
| **Hierarchical Search** | Moderate | Multiresolution pyramid | Excellent for large displacements | Low |

---

### 4. Accuracy and Complexity Trade-Offs (Unit 4 Notes)
1. **Block Size Trade-off:**
   - *Small blocks ($4 \\times 4$ or $8 \\times 8$):* Higher prediction accuracy and sharp motion boundary preservation, but multiplies the number of motion vectors transmitted (high bitrate overhead).
   - *Large blocks ($16 \\times 16$ or $32 \\times 32$):* Low motion vector overhead, but causes prediction errors along moving object boundaries.
2. **Sub-Pixel Motion Precision (Half-Pel / Quarter-Pel):**
   - Real-world motion is not quantized to integer pixel grids. Modern codecs (H.264/HEVC) interpolate reference frames using FIR filters to test half-pel and quarter-pel positions, improving prediction accuracy by $2\\text{ to }3\\text{ dB}$ PSNR at the cost of additional interpolation complexity."""
    },
    {
        "id": "MID2-Q10",
        "mid": "Mid-II",
        "qno": 10,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Formulate the nonlinear optimization problem for motion estimation and examine the techniques used to solve it.",
        "punchline": "Motion estimation is formulated as a nonlinear least-squares problem minimizing intensity residuals; Gradient Descent provides low-cost first-order updates, Gauss-Newton accelerates quadratic convergence, and Levenberg-Marquardt adaptively damps updates to balance speed and global stability.",
        "mnemonic": "G-G-L-N: Gradient Descent, Gauss-Newton, Levenberg-Marquardt, Newton's Method.",
        "analogy": "Like hiking down a foggy mountain to find the lowest valley: Gradient Descent takes small steps straight downhill; Newton's method calculates the 3D bowl shape of the valley; Levenberg-Marquardt acts like an experienced guide who takes careful small steps on steep cliffs (damping) and sprints when entering the smooth valley floor.",
        "diagram": """+-------------------------------------------------------------------------------+
|             NONLINEAR OPTIMIZATION FOR PARAMETRIC MOTION ESTIMATION           |
+-------------------------------------------------------------------------------+

 OBJECTIVE FUNCTION:
   E(p) = Σ [ I₂(x_i + u(x_i; p)) - I₁(x_i) ]² = Σ r_i(p)²
          i                                       i
   Nonlinear with respect to motion parameter vector p = [t_x, t_y, θ, s]ᵀ

 OPTIMIZATION TECHNIQUES COMPARED:
 ┌──────────────────────┬─────────────────────────────────────────────────────┐
 │ Method               │ Parameter Update Equation                           │
 ├──────────────────────┼─────────────────────────────────────────────────────┤
 │ Gradient Descent     │ p^(k+1) = p^(k) - α ∇E(p)                           │
 │ Gauss-Newton         │ Δp = - (Jᵀ J)⁻¹ Jᵀ r                                │
 │ Levenberg-Marquardt  │ Δp = - (Jᵀ J + λ I)⁻¹ Jᵀ r                          │
 │ Newton's Method      │ Δp = - H⁻¹ ∇E(p)                                    │
 └──────────────────────┴─────────────────────────────────────────────────────┘

 CONVERGENCE BEHAVIOR OF LEVENBERG-MARQUARDT:
   Large λ (Far from optimum)  ──► Behaves like Gradient Descent (Guaranteed descent)
   Small λ (Near optimum)      ──► Behaves like Gauss-Newton (Fast quadratic convergence)""",
        "content": """### 1. Mathematical Formulation of Nonlinear Motion Estimation (Unit 4 Notes)
In parametric motion estimation (such as affine camera tracking, optical flow, and direct image registration), the displacement of pixel $\\mathbf{x}_i = (x_i, y_i)^T$ is governed by a parameter vector $\\mathbf{p} = [p_1, p_2, \\dots, p_K]^T$ (e.g., translation, rotation angle, scaling factors):
$$\\mathbf{x}'_i = \\mathbf{x}_i + \\mathbf{u}(\\mathbf{x}_i; \\mathbf{p})$$

The objective is to estimate optimal parameters $\\mathbf{p}^*$ that minimize the nonlinear sum of squared intensity residuals (SSD) between reference frame $I_1$ and transformed current frame $I_2$:
$$E(\\mathbf{p}) = \\sum_{i=1}^N \\left[ I_2(\\mathbf{x}_i + \\mathbf{u}(\\mathbf{x}_i; \\mathbf{p})) - I_1(\\mathbf{x}_i) \\right]^2 = \\sum_{i=1}^N r_i(\\mathbf{p})^2 = \\|\\mathbf{r}(\\mathbf{p})\\|_2^2$$
where $r_i(\\mathbf{p}) = I_2(\\mathbf{x}_i + \\mathbf{u}(\\mathbf{x}_i; \\mathbf{p})) - I_1(\\mathbf{x}_i)$ is the intensity residual at pixel $i$.

Because the image intensity function $I_2(\\cdot)$ is a complex, non-convex spatial surface, $E(\\mathbf{p})$ is inherently **nonlinear with respect to $\\mathbf{p}$**, requiring iterative nonlinear optimization.

---

### 2. Examination of Optimization Techniques (Unit 4 Notes)

#### a) Gradient Descent Method (First-Order)
- **Update Rule:** Updates motion parameters in the negative direction of the cost gradient:
  $$\\mathbf{p}^{(k+1)} = \\mathbf{p}^{(k)} - \\alpha \\nabla E(\\mathbf{p}^{(k)})$$
  where $\\nabla E(\\mathbf{p}) = 2 \\mathbf{J}^T \\mathbf{r}$, and $\\mathbf{J} = \\frac{\\partial \\mathbf{r}}{\\partial \\mathbf{p}}$ is the $N \\times K$ Jacobian matrix.
- **Evaluation:**
  - *Advantages:* Low computational complexity per iteration; requires minimal memory; guaranteed descent for sufficiently small learning rate $\\alpha$.
  - *Limitations:* Exhibits slow linear convergence near the minimum; prone to zigzagging in narrow error valleys; highly sensitive to step size $\\alpha$.

#### b) Gauss-Newton Method (Nonlinear Least Squares)
- **Principle:** Linearizes the residual vector via first-order Taylor expansion: $\\mathbf{r}(\\mathbf{p} + \\Delta \\mathbf{p}) \\approx \\mathbf{r}(\\mathbf{p}) + \\mathbf{J} \\Delta \\mathbf{p}$.
- **Update Rule:**
  $$\\Delta \\mathbf{p} = -(\\mathbf{J}^T \\mathbf{J})^{-1} \\mathbf{J}^T \\mathbf{r}$$
  $$\\mathbf{p}^{(k+1)} = \\mathbf{p}^{(k)} + \\Delta \\mathbf{p}$$
  *(Approximates the true Hessian as $\\mathbf{H} \\approx 2 \\mathbf{J}^T \\mathbf{J}$, avoiding costly second derivatives).*
- **Evaluation:**
  - *Advantages:* Achieves fast quadratic convergence near the optimum when residuals are small.
  - *Limitations:* Fails or diverges if $\\mathbf{J}^T \\mathbf{J}$ is ill-conditioned or rank-deficient (e.g., in low-texture image regions).

#### c) Levenberg-Marquardt (LM) Algorithm (Damped Least Squares)
- **Principle:** Dynamically bridges Gradient Descent and Gauss-Newton by introducing an adaptive damping parameter $\\lambda$:
  $$(\\mathbf{J}^T \\mathbf{J} + \\lambda \\mathbf{I}) \\Delta \\mathbf{p} = -\\mathbf{J}^T \\mathbf{r}$$
- **Adaptive Damping Strategy:**
  1. If an iteration reduces error $E(\\mathbf{p} + \\Delta \\mathbf{p}) < E(\\mathbf{p})$: Accept update $\\mathbf{p} \\leftarrow \\mathbf{p} + \\Delta \\mathbf{p}$, and decrease damping $\\lambda \\leftarrow \\lambda / 10$ (moves toward fast Gauss-Newton).
  2. If error increases: Reject update, increase damping $\\lambda \\leftarrow \\lambda \\times 10$ (moves toward robust Gradient Descent), and resolve.
- **Evaluation:** The industry standard for optical flow, camera pose tracking, and bundle adjustment due to its unmatched balance of speed and stability.

#### d) Newton's Method (Full Second-Order)
- **Update Rule:**
  $$\\Delta \\mathbf{p} = -\\mathbf{H}^{-1} \\nabla E(\\mathbf{p})$$
  where $\\mathbf{H} = \\nabla^2 E(\\mathbf{p})$ is the full $K \\times K$ Hessian matrix.
- **Evaluation:** Quadratic convergence, but computing and inverting the exact second-derivative Hessian is computationally prohibitive for high-dimensional models.

---

### 3. Critical Comparison of Optimization Techniques (Unit 4 Notes)

| Optimization Technique | Convergence Speed | Computational Cost per Iteration | Robustness to Poor Initialization | Primary Application in Vision |
| :--- | :--- | :--- | :--- | :--- |
| **Gradient Descent** | Slow (Linear) | Very Low ($O(NK)$) | Moderate (slowly descends) | Neural network optical flow training |
| **Gauss-Newton** | Fast near optimum | Medium ($O(NK^2 + K^3)$) | Poor (diverges if initial guess is far) | Direct image alignment (Lucas-Kanade) |
| **Levenberg-Marquardt**| Fast & Stable | Medium-to-High | **Excellent** (Adaptive damping) | 3D Camera tracking, Bundle Adjustment |
| **Newton's Method** | Very Fast | High (Computes exact $\\nabla^2 E$) | Sensitive to non-positive definite $\\mathbf{H}$ | Offline parametric surface registration |

---

### 4. Justification of Convergence Behavior (Unit 4 Notes)
The convergence behavior of nonlinear motion estimation depends directly on:
1. **Initial Parameter Estimate:** A coarse initial match (from feature matching or image pyramids) prevents trapping in false local minima.
2. **Error Surface Smoothness:** Well-textured scenes create convex error basins; untextured regions produce flat eigenvalues and divergence.
3. **Adaptive Damping:** The Levenberg-Marquardt algorithm is justified as the superior technique because its dynamic damping factor guarantees monotonic error reduction $\\Delta E \\le 0$ at every step."""
    },
    {
        "id": "MID2-Q11",
        "mid": "Mid-II",
        "qno": 11,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Design a motion estimation algorithm using transform-domain techniques and justify the optimization techniques used.",
        "punchline": "Transform-domain motion estimation operates directly on DCT, DFT, or DWT coefficients; DFT phase correlation isolates global translation via cross-power Dirac delta peaks, while DWT multiresolution wavelet search prunes candidate comparisons across subbands.",
        "mnemonic": "D-D-D: DCT coefficient matching, DFT Phase Correlation, DWT Multiresolution search.",
        "analogy": "Instead of comparing two photos by inspecting millions of individual blades of grass (spatial pixels), you compare the frequency histogram peaks (transform domain); shifting an image simply shifts the phase angles without changing frequencies.",
        "diagram": """+-------------------------------------------------------------------------------+
|             TRANSFORM-DOMAIN MOTION ESTIMATION ARCHITECTURE                   |
+-------------------------------------------------------------------------------+

 Current Frame F_t                    Reference Frame F_{t-1}
        │                                     │
        ▼                                     ▼
 [ 2D-DFT / DCT / DWT ]               [ 2D-DFT / DCT / DWT ]
        │                                     │
   F_t(u, v)                            F_{t-1}(u, v)
        │                                     │
        └──────────────────┬──────────────────┘
                           │
                           ▼
          [ 1. DFT PHASE CORRELATION ]
          Normalized Cross-Power Spectrum:
          R(u, v) = [ F_t · F*_{t-1} ] / | F_t · F*_{t-1} | = e^(-j 2π (u dx + v dy))
                           │
                           ▼
          [ 2. 2D Inverse Fourier Transform ]
          r(x, y) = IDFT{ R(u, v) } = δ(x - dx, y - dy)
                           │
                           ▼
          [ 3. Peak Detection ] ──► Sharp Delta Peak Location = Motion Vector (dx, dy)!""",
        "content": """### 1. Architectural Design of Transform-Domain Motion Estimation (Unit 4 Notes)
Transform-domain motion estimation estimates the displacement between consecutive video frames using transformed mathematical coefficients (frequency/wavelet subbands) rather than spatial pixel arrays.
**Core Objectives:**
1. Drastically reduce computational complexity by eliminating spatial pixel loops.
2. Exploit transform energy compaction to match low-dimensional coefficient subsets.
3. Decouple illumination variations from spatial motion.

---

### 2. Design of the Three Core Transform Algorithms (Unit 4 Notes)

#### A. DFT-Based Phase Correlation (Global Translation Estimation)
- **Theoretical Basis (Fourier Shift Property):**
  If Frame 2 is a shifted version of Frame 1:
  $$f_2(x, y) = f_1(x - d_x, y - d_y)$$
  Their 2D-DFTs satisfy:
  $$F_2(u, v) = F_1(u, v) \\, e^{-j 2\\pi \\left( \\frac{u d_x}{M} + \\frac{v d_y}{N} \\right)}$$
- **Algorithm Steps:**
  1. Compute 2D-FFT of current frame $F_2(u, v)$ and reference frame $F_1(u, v)$.
  2. Compute the **Normalized Cross-Power Spectrum**:
     $$R(u, v) = \\frac{F_2(u, v) \\cdot F_1^*(u, v)}{|F_2(u, v) \\cdot F_1^*(u, v)|} = e^{-j 2\\pi \\left( \\frac{u d_x}{M} + \\frac{v d_y}{N} \\right)}$$
     *(Normalizing by magnitude removes all image structural content, retaining only pure phase displacement information).*
  3. Compute the 2D Inverse FFT of $R(u, v)$:
     $$r(x, y) = \\mathcal{F}^{-1}\\{R(u, v)\\} = \\delta(x - d_x, y - d_y)$$
  4. **Peak Detection:** Locate the single prominent Dirac delta peak in the correlation surface $r(x, y)$:
     $$(d_x, d_y) = \\arg\\max_{(x, y)} r(x, y)$$
- **Advantage:** Computes exact global camera translation with $O(N^2 \\log N)$ complexity, completely independent of displacement distance $p$.

#### B. DCT-Based Motion Estimation (Local Block Matching)
- **Algorithm Steps:**
  1. Partition frames into $8 \\times 8$ macroblocks and apply 2D-DCT.
  2. Because the 2D-DCT compacts $>90\\%$ of block energy into the top-left low-frequency coefficients, discard high-frequency coefficients.
  3. Compute coefficient matching error over reduced frequency set $\\mathcal{S}$:
     $$E_{\\text{DCT}}(dx, dy) = \\sum_{(u, v) \\in \\mathcal{S}} |C_t(u, v) - C_{t-1}(u, v; dx, dy)|$$
- **Advantage:** Evaluates only 8–10 DCT coefficients instead of 64 spatial pixels, speeding up matching by $80\\%$.

#### C. DWT-Based Multiresolution Wavelet Motion Estimation
- **Algorithm Steps:**
  1. Apply 2-level 2D Discrete Wavelet Transform (DWT), decomposing frames into $LL_2, LH_2, HL_2, HH_2$ subbands.
  2. **Coarse Scale Search:** Estimate large displacements in the low-resolution $LL_2$ subband (search space is decimated by $16\\times$).
  3. **Fine Scale Refinement:** Propagate vectors down to higher-resolution detail subbands ($LH_1, HL_1$), searching only small $\\pm 1$ refinement windows.

---

### 3. Performance Optimization Techniques & Justifications (Unit 4 Notes)

| Optimization Technique | Performance Benefit | Mathematical Justification |
| :--- | :--- | :--- |
| **FFT Phase Correlation** | Ultra-fast global motion estimation | Replaces spatial search with point-wise spectral multiplications ($O(N^2 \\log N)$). |
| **Low-Frequency DCT Selection** | Reduces matching operations by $>75\\%$ | Exploits DCT energy compaction; high frequencies contain negligible motion energy. |
| **Multiresolution Wavelet Search** | Eliminates local minima for large motion | Hierarchical search bounds large motion vectors at coarse scales before local refinement. |
| **Rate-Distortion Optimization (RDO)**| Optimizes video compression quality | Minimizes combined cost $J = D + \\lambda_{\\text{mode}} R$, balancing prediction error $D$ against bitrate $R$. |"""
    },
    {
        "id": "MID2-Q12",
        "mid": "Mid-II",
        "qno": 12,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Construct a comprehensive framework for 3D motion and structure estimation from 2D video sequences and assess its performance in real-world scenarios.",
        "punchline": "The framework integrates geometric models (camera projection, epipolar geometry, triangulation) with statistical models (Kalman filter, RANSAC, Bundle Adjustment) across 8 sequential stages to reconstruct metric 3D point clouds and track 6-DOF camera trajectories.",
        "mnemonic": "A-F-M-C-S-M-O-R: Acquisition, Features, Matching, Calibration, Structure, Motion, Optimization, Reconstruction.",
        "analogy": "Like human stereo vision and brain processing: your two eyes take flat 2D pictures from slightly different angles (geometric projection); your brain matches corresponding landmarks (epipolar triangulation), filters out optical illusions and blinks (RANSAC/Kalman filter), and perceives a solid 3D world in which you navigate safely.",
        "diagram": """+-------------------------------------------------------------------------------+
|         3D MOTION AND STRUCTURE ESTIMATION FRAMEWORK (SfM / SLAM)             |
+-------------------------------------------------------------------------------+

 [ Input 2D Video Frames ] ──► Monocular / Stereo Video Stream (F_t, F_{t+1})
           │
           ▼
 [ 1. Feature Extraction ] ──► Detects scale-invariant keypoints (SIFT, ORB)
           │
           ▼
 [ 2. Correspondence Match]──► Matches descriptors across frames
           │
           ▼
 [ 3. Epipolar & RANSAC ]  ──► Robust Essential Matrix E = [t]_x R (Rejects outliers!)
           │
           ▼
 [ 4. Triangulation ]      ──► 3D Point Reconstruction: X = (X, Y, Z)^T
           │
           ▼
 [ 5. 3D Motion Estimation]──► 6-DOF Camera Pose: Rotation R and Translation t
           │
           ▼
 [ 6. Kalman Filter ]      ──► Predicts & smooths dynamic object velocities over time
           │
           ▼
 [ 7. Bundle Adjustment ]  ──► Joint nonlinear minimization: min Σ ||x_ij - π(K, R_i, t_i, X_j)||²
           │
           ▼
 [ 8. 3D Scene Output ]    ──► Metric 3D Point Cloud + Camera Trajectory for Self-Driving""",
        "content": """### 1. Conceptual Framework Architecture (Unit 4 Notes)
**3D Motion and Structure Estimation (Structure from Motion - SfM / Visual SLAM)** is an advanced computer vision technique that reconstructs the three-dimensional (3D) geometric structure of a scene and tracks the 6-Degrees-of-Freedom (6-DOF) trajectory of a camera or moving objects from 2D video sequences.

Reliable real-world estimation requires a seamless fusion of:
1. **Geometric Models:** Enforce rigid mathematical projection constraints between 3D world points and 2D camera images.
2. **Statistical Models:** Filter out sensor noise, resolve correspondence outliers, and track dynamic states over time.

---

### 2. The 8 Stages of the Comprehensive Framework (Unit 4 Notes)

#### Stage 1: Video Ingestion & Camera Calibration
- Captures sequential frames $F_1, F_2, \\dots, F_T$.
- Determines the **Intrinsic Camera Matrix $\\mathbf{K}$** (focal length $f_x, f_y$, principal point $c_x, c_y$):
  $$\\mathbf{K} = \\begin{bmatrix} f_x & 0 & c_x \\\\ 0 & f_y & c_y \\\\ 0 & 0 & 1 \\end{bmatrix}$$

#### Stage 2: Feature Detection & Extraction
- Detects salient, illumination-invariant visual keypoints using SIFT, SURF, or ORB detectors.

#### Stage 3: Feature Matching & Epipolar Geometry
- Establishes correspondence between point $\\mathbf{x}$ in Frame 1 and point $\\mathbf{x}'$ in Frame 2.
- The two views are constrained by the **Fundamental Matrix $\\mathbf{F}$** and **Essential Matrix $\\mathbf{E}$**:
  $$\\mathbf{x}'^T \\mathbf{F} \\mathbf{x} = 0, \\quad \\mathbf{E} = \\mathbf{K}^T \\mathbf{F} \\mathbf{K} = [\\mathbf{t}]_\\times \\mathbf{R}$$
- **RANSAC (Statistical):** Selects random 8-point subsets to fit $\\mathbf{E}$ while discarding false feature matches (outliers caused by reflections or moving pedestrians).

#### Stage 4: 3D Motion Estimation (Camera Pose Recovery)
- Decomposes the Essential Matrix $\\mathbf{E}$ using Singular Value Decomposition (SVD) into the camera's relative 3D rotation matrix $\\mathbf{R} \\in SO(3)$ and translation vector $\\mathbf{t} \\in \\mathbb{R}^3$.

#### Stage 5: 3D Structure Estimation (Triangulation)
- Given camera poses and corresponding rays, triangulates the 3D world coordinates $\\mathbf{X} = (X, Y, Z)^T$ by minimizing the geometric intersection distance.

#### Stage 6: Dynamic Object Tracking via Kalman Filtering
- Models moving dynamic objects in the scene using a linear state-space Kalman Filter:
  - *State Prediction:* $\\hat{\\mathbf{x}}_k^- = \\mathbf{A} \\hat{\\mathbf{x}}_{k-1} + \\mathbf{B} \\mathbf{u}_k$
  - *Measurement Update:* $\\hat{\\mathbf{x}}_k = \\hat{\\mathbf{x}}_k^- + \\mathbf{K}_k (\\mathbf{z}_k - \\mathbf{H} \\hat{\\mathbf{x}}_k^-)$
- Tracks velocity and predicts object trajectories during momentary occlusions.

#### Stage 7: Statistical Optimization (Bundle Adjustment)
- Refines all camera poses $(\\mathbf{R}_i, \\mathbf{t}_i)$ and 3D point coordinates $\\mathbf{X}_j$ simultaneously by minimizing the total non-linear **reprojection error**:
  $$\\min_{\\{\\mathbf{R}_i, \\mathbf{t}_i, \\mathbf{X}_j\\}} \\sum_{i=1}^M \\sum_{j=1}^N v_{ij} \\left\\| \\mathbf{x}_{ij} - \\pi\\left(\\mathbf{K}, \\mathbf{R}_i, \\mathbf{t}_i, \\mathbf{X}_j\\right) \\right\\|^2$$
  where $\\pi(\\cdot)$ is the perspective projection function, and $v_{ij} = 1$ if point $j$ is visible in frame $i$.

#### Stage 8: 3D Scene Reconstruction & Output
- Outputs a dense 3D metric point cloud map and continuous 6-DOF camera trajectory.

---

### 3. Integration Matrix of Geometric and Statistical Models (Unit 4 Notes)

| Geometric Model | Statistical Model Partner | Purpose in the Integrated Framework |
| :--- | :--- | :--- |
| **Perspective Camera Projection** | **Maximum Likelihood Estimation (MLE)** | Estimates 3D point coordinates under Gaussian sensor noise. |
| **Epipolar Geometry ($x'^T F x = 0$)**| **RANSAC Algorithm** | Identifies true inlier matches; rejects up to $50\\%$ false correspondence outliers. |
| **Multi-View Triangulation** | **Extended Kalman Filter (EKF)** | Filters depth jitter; tracks 3D velocities of moving vehicles. |
| **6-DOF Camera Motion Model** | **Bundle Adjustment (Levenberg-Marquardt)** | Eliminates cumulative drift error over extended video sequences. |

---

### 4. Real-World Autonomous Vehicle Performance Assessment (Unit 4 Notes)
In self-driving vehicle systems (e.g., Tesla Vision, Waymo):
- **Scenario:** The vehicle navigates an urban street with moving traffic, stationary lampposts, and pedestrians.
- **Performance:**
  1. *Ego-Motion Estimation:* Front-facing cameras compute the car's millimeter-accurate velocity and steering heading without GPS.
  2. *Obstacle Depth Mapping:* Triangulates distances to leading vehicles and lane barriers.
  3. *Kalman Trajectory Prediction:* Predicts whether a crossing pedestrian will intersect the car's braking path within 2.5 seconds.
  4. *Robustness:* RANSAC prevents passing shadows from corrupting the vehicle's spatial map, enabling safe, autonomous collision-free navigation."""
    }
]
