# -*- coding: utf-8 -*-
"""
Unit 4: Image Formation, Motion Models, Motion Estimation & 3D Structure
Questions: Mid-II Q5 to Q12
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408 | Dr. Sandeep Kumar M
Written in student-friendly, zero-jargon peer-tutor style with complete mathematical rigor.
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
        "punchline": "Image formation models describe how a 3D world turns into 2D camera pixels through Geometric, Photometric, Optical, and Sampling models; they stop motion algorithms from confusing a passing shadow or lens blur with real movement.",
        "mnemonic": "G-P-O-S: Geometric (perspective), Photometric (lighting), Optical (lens blur), Sampling (pixels).",
        "analogy": "Like an automated speed-trap camera: it must know the camera angle and distance (geometric), ignore headlight glare and streetlamp flickers (photometric), handle rain on the lens (optical), and account for sensor pixel resolution (sampling) to calculate a speeder's true velocity.",
        "diagram": """THE 4 IMAGE FORMATION MODELS:
  1. Geometric Model   ──► 3D-to-2D Perspective: P(X, Y, Z) ──► (x, y) on sensor
  2. Photometric Model ──► Lighting & Surface Reflectance: I(x, y) = ρ(x, y) · E(x, y)
  3. Optical Model     ──► Lens distortion, aperture diffraction, and motion blur
  4. Sampling & Quant  ──► Continuous light ──► Discrete pixel grid & 8-bit values

ROLE IN MOTION ESTIMATION:
  [ Frame t ] & [ Frame t+1 ]
         │
         ▼
  [ 1. Image Formation Analysis ] ──► Normalizes lighting shifts & corrects lens blur
         │
         ▼
  [ 2. Feature Extraction ]       ──► Detects invariant corners & keypoints (SIFT / ORB)
         │
         ▼
  [ 3. Correspondence Matching ]  ──► Tracks corresponding points across frames
         │
         ▼
  [ 4. Motion Estimation ]        ──► Block matching / Optical flow calculates displacement
         │
         ▼
  [ Output Motion Vectors ]       ──► Generates true (u, v) trajectory vectors!""",
        "content": """### 1. The Big Picture (How Real Light Becomes Digital Pixels)
Before a computer can track moving objects in a video, it has to understand how real-world 3D objects turned into a flat 2D grid of numbers in the first place. 
An **image formation model** is the mathematical bridge connecting the 3D physical world to digital pixels.

---

### 2. Categorizing the 4 Fundamental Models (Unit 4 Notes)

#### 1. Geometric Model (Perspective Projection)
* **What it does:** Describes how 3D real-world coordinates $(X, Y, Z)$ are projected onto the 2D camera sensor plane $(x, y)$ through a lens of focal length $f$:
  $$x = f \\frac{X}{Z}, \\quad y = f \\frac{Y}{Z}$$
* **Role in Motion:** Explains perspective scaling and motion parallax (e.g., an approaching car appears to grow larger on screen because depth $Z$ decreases).

#### 2. Photometric / Illumination Model (Light & Color)
* **What it does:** Models how ambient sunlight or lamps reflect off object surfaces into the camera lens:
  $$I(x, y) = \\rho(x, y) \\cdot E(x, y)$$
  where $\\rho(x, y)$ is the surface reflectance (the object's true color) and $E(x, y)$ is the incident light.
* **Role in Motion:** Helps algorithms separate **true physical movement** from brightness changes caused by clouds passing over the sun or flickering headlights.

#### 3. Optical Model (The Lens & Blur)
* **What it does:** Accounts for physical glass lens properties: focal depth, aperture diffraction, radial barrel distortion, and motion blur.
* **Role in Motion:** Fast-moving objects get blurred across several pixels. Optical models allow algorithms to model blurred Point Spread Functions (PSF) rather than failing to match sharp edges.

#### 4. Sampling & Quantization Model (Digital Pixels)
* **What it does:** Converts continuous optical light into discrete spatial pixels $(m \\Delta x, n \\Delta y)$ and quantizes intensity into finite digital levels (e.g., 8-bit integers $0\\dots255$).
* **Role in Motion:** Explains resolution limits and quantization noise that can destabilize sub-pixel motion vectors.

---

### 3. Step-by-Step Role in the Motion Estimation Pipeline
1. **Input Frames ($F_t, F_{t+1}$):** Ingests consecutive frames.
2. **Image Formation Analysis:** Uses photometric models to normalize global lighting changes and optical models to fix lens distortion.
3. **Feature Matching:** Extracts scale-invariant features (corners, edges, SIFT/ORB) that survive perspective projection.
4. **Motion Computation:** Applies block matching or optical flow to calculate spatial displacement vectors $(u, v)$.
5. **Output Motion Vectors:** Feeds motion trajectories to video encoders (H.264) or autonomous driving systems."""
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
        "punchline": "Motion models mathematically describe how coordinates move via Translation (2-DOF), Rotation, Affine (6-DOF), and Optical Flow; they rely on 4 physical assumptions: Constant Velocity, Rigidity, Brightness Constancy, and Limited Occlusion.",
        "mnemonic": "Models: T-R-A-O (Translation, Rotation, Affine, Optical Flow). Assumptions: C-R-B-L (Constant velocity, Rigidity, Brightness constancy, Limited occlusion).",
        "analogy": "Like predicting where a soccer ball lands: you assume the stadium floodlights don't turn off mid-kick (brightness constancy), the ball doesn't deflate or deform into a pancake (rigidity), gravity and wind are steady over half a second (constant velocity), and no other player blocks the camera view (limited occlusion).",
        "diagram": """1. TRANSLATION (2-DOF):              2. ROTATION:
   x' = x + u                           x' = x cos θ - y sin θ
   y' = y + v                           y' = x sin θ + y cos θ
   (Pure linear shift)                  (In-plane spin)

3. AFFINE MODEL (6-DOF):             4. OPTICAL FLOW (Dense):
   x' = a₁₁ x + a₁₂ y + t_x             I_x · u + I_y · v + I_t = 0
   y' = a₂₁ x + a₂₂ y + t_y             (Individual vector per pixel)
   (Translation + Scale + Shear)

THE 4 UNDERLYING ASSUMPTIONS:
┌──────────────────────┬─────────────────────────────────────────────────────┐
│ Physical Assumption  │ Meaning & Where It Fails in the Real World          │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ Brightness Constancy │ Moving pixels keep constant intensity (Fails in sun)│
│ Rigid Object         │ Objects don't deform (Fails for faces & clothing)   │
│ Constant Velocity    │ Speed stays steady over 33 ms (Fails on collisions) │
│ Limited Occlusion    │ Objects stay visible (Fails behind trees/pillars)   │
└──────────────────────┴─────────────────────────────────────────────────────┘""",
        "content": """### 1. The Big Picture (How We Model Motion)
A **motion model** is a mathematical formula that maps where a pixel was in Frame 1 $(x, y)$ to its new location in Frame 2 $(x', y')$. Depending on how complex the movement is, we choose between simple or high-dimensional models.

---

### 2. The 4 Major Motion Models (Unit 4 Notes)

#### a) Translation Model (2 Parameters / 2-DOF)
* **Formula:**
  $$x' = x + u, \\quad y' = y + v$$
* **What it means:** The simplest model. Assumes all pixels in a block shift by the exact same distance without spinning or changing size (e.g., a car driving along a straight road).
* **Where it's used:** Universally used in block-matching video compression (MPEG, H.264, HEVC).

#### b) Rotation Model (In-Plane Spin)
* **Formula:**
  $$x' = x \\cos\\theta - y \\sin\\theta, \\quad y' = x \\sin\\theta + y \\cos\\theta$$
* **What it means:** Rotates the image by angle $\\theta$ around a reference center point (e.g., a spinning drone propeller or wheel).

#### c) Affine Motion Model (6 Parameters / 6-DOF)
* **Formula:**
  $$\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = \\begin{bmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} + \\begin{bmatrix} t_x \\\\ t_y \\end{bmatrix}$$
* **What it means:** Handles translation ($t_x, t_y$), in-plane rotation, scaling (zoom in/out), and shear all at once. Great for camera pan/tilt/zoom tracking.

#### d) Differential Optical Flow Model (Dense Pixel Model)
* **Formula:**
  $$I_x u + I_y v + I_t = 0$$
* **What it means:** Computes an individual, unique motion vector $(u, v)$ for every single pixel in the video frame.

---

### 3. The 4 Critical Assumptions in Real-World Scenes (Unit 4 Notes)
Every motion estimation algorithm relies on 4 fundamental physical assumptions:
1. **Brightness Constancy:** 
   - *Assumption:* The color/brightness of a surface point does not change as it moves between frames: $I(x + u, y + v, t + \\Delta t) = I(x, y, t)$.
   - *Real-world Failure:* Fails under sudden cloud cover, metallic surface reflections, or streetlamp glare.
2. **Rigid Body Assumption:**
   - *Assumption:* The moving object maintains its physical shape and size.
   - *Real-world Failure:* Fails for non-rigid articulated objects like human facial expressions, walking pedestrians, or flapping cloth.
3. **Constant Velocity / Small Motion:**
   - *Assumption:* Acceleration is negligible over the small interval between frames (33 ms at 30 fps), so speed is constant.
   - *Real-world Failure:* Fails during sudden impacts, jolts, or rapid sports action.
4. **Limited Occlusion:**
   - *Assumption:* The target object remains visible across frames and is not hidden.
   - *Real-world Failure:* Fails when a car drives behind a tree, enters a tunnel, or passes another vehicle."""
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
        "punchline": "Motion vector is MV = (3, 5); positive horizontal displacement u = +3 means moving right, positive vertical displacement v = +5 means moving down in image coordinates, so the block moves diagonally downward and to the right.",
        "mnemonic": "MV = (x2 - x1, y2 - y1) = (23-20, 30-25) = (3, 5). Down & Right.",
        "analogy": "Like moving a checker on a board: you start on square (20, 25) and land on square (23, 30). You slid 3 squares to the right and 5 squares toward the bottom.",
        "diagram": """Image Display Coordinate System:
Origin (0,0) is at TOP-LEFT corner!
X-axis goes POSITIVE to the RIGHT
Y-axis goes POSITIVE DOWNWARD

   x = 20           x = 23
   ┌────────────────┬────────────────► X (Horizontal)
   │
y=25   • (20, 25) [Frame 1 Block]
   │    \\
   │     \\  u = +3 pixels (Right)
   │      \\
   │       \\  v = +5 pixels (Down)
   │        \\
y=30         ▼ (23, 30) [Frame 2 Best Match]
   │
   ▼
   Y (Vertical)

Displacement: MV = (Δx, Δy) = (23 - 20, 30 - 25) = (3, 5)
Magnitude   : ||MV|| = √(3² + 5²) = √34 ≈ 5.83 pixels
Angle       : θ = arctan(5/3) ≈ 59.04° below horizontal""",
        "content": """### 1. The Given Coordinates (Unit 4 Notes)
In Block Motion Estimation (BMA), we track a macroblock across consecutive video frames:
* **Position in Frame 1 ($F_1$):** $(x_1, y_1) = (20, 25)$
* **Best match in Frame 2 ($F_2$):** $(x_2, y_2) = (23, 30)$

---

### 2. Task 1: Calculate the Motion Vector
The motion vector $\\mathbf{MV} = (u, v)$ is the difference in coordinates:
$$u = \\Delta x = x_2 - x_1$$
$$v = \\Delta y = y_2 - y_1$$

Substitute the numbers:
$$u = 23 - 20 = \\mathbf{+3\\text{ pixels}}$$
$$v = 30 - 25 = \\mathbf{+5\\text{ pixels}}$$

Therefore, the motion vector is:
$$\\mathbf{MV} = (u, v) = \\mathbf{(3, \\ 5)}$$

---

### 3. Task 2: Determine the Direction of Motion
In digital video and screen coordinate systems:
* The **origin $(0, 0)$** is at the **top-left corner**.
* The **horizontal $x$-axis** increases to the **right**.
* The **vertical $y$-axis** increases **downward**.

#### Directional Analysis:
1. **Horizontal Component ($u = +3$):** Because $u > 0$, the block moved **3 pixels to the right**.
2. **Vertical Component ($v = +5$):** Because $v > 0$, the block moved **5 pixels downward**.

#### Final Directional Verdict:
The block moves **diagonally downward and to the right**.

#### Magnitude & Angle (Bonus Exam Points):
* **Distance traveled (Magnitude):**
  $$\\|\\mathbf{MV}\\| = \\sqrt{u^2 + v^2} = \\sqrt{3^2 + 5^2} = \\sqrt{9 + 25} = \\sqrt{34} \\approx \\mathbf{5.83\\text{ pixels}}$$
* **Angle of trajectory:**
  $$\\theta = \\arctan\\left(\\frac{v}{u}\\right) = \\arctan\\left(\\frac{5}{3}\\right) \\approx \\mathbf{59.04^\\circ}\\text{ below the positive x-axis}$$"""
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
        "punchline": "Differential optical flow uses intensity slopes via Ix·u + Iy·v + It = 0; Lucas-Kanade solves it in small windows while Horn-Schunck solves global smoothness; both hate noise and lighting flickers, requiring Gaussian smoothing and gradient normalization.",
        "mnemonic": "OFC: Ix·u + Iy·v + It = 0. LK = Local least squares; HS = Global smoothness.",
        "analogy": "Like trying to guess how fast a white cloud is drifting across the sky by measuring how its brightness changes: if the cloud moves smoothly, your formula works; but if a lightning bolt flashes (illumination change) or raindrops hit your camera (noise), the formula screams that the cloud is traveling at supersonic speed!",
        "diagram": """THE OPTICAL FLOW CONSTRAINT (OFC):
  I_x · u + I_y · v + I_t = 0
  [ 1 equation, 2 unknowns (u, v) ==> APERTURE PROBLEM! ]
  (Can only measure motion perpendicular to object edge)

LUCAS-KANADE (Local):                    HORN-SCHUNCK (Global):
Assumes (u, v) is constant in a          Minimizes total global error energy:
small 3x3 local window Ω                 E = ∬ [(I_x u + I_y v + I_t)² + α² (|∇u|² + |∇v|²)] dx dy
(Aᵀ A) [u; v] = Aᵀ b                     Dense, smooth optical flow across full image!
Fast, but needs textured corners.

SENSITIVITY & MITIGATION:
• Sensor Noise     ──► Pre-filter with 2D Gaussian smoothing kernel (G_σ * I)
• Lighting Shifts  ──► Illumination normalization / Gradient matching
• Flat Surfaces    ──► Track only Harris corners where structure tensor has 2 large eigenvalues""",
        "content": """### 1. The Big Picture (What are Differential Methods?)
Differential methods (optical flow) calculate motion by looking at how pixel brightness changes over time and space.
They start from the **Brightness Constancy Assumption**:
$$I(x + u, y + v, t + 1) = I(x, y, t)$$

Taking a first-order Taylor series expansion yields the famous **Optical Flow Constraint (OFC) Equation**:
$$I_x u + I_y v + I_t = 0$$
where $I_x, I_y$ are spatial brightness gradients, $I_t$ is temporal frame change, and $(u, v)$ is the pixel velocity.

#### The Aperture Problem (Why One Equation Isn't Enough):
We have **1 equation but 2 unknowns $(u, v)$** at every pixel! 
Looking through a small window (aperture), you can only see motion perpendicular to an edge (normal flow). Motion parallel to the edge is completely invisible.

---

### 2. Lucas-Kanade vs Horn-Schunck
* **Lucas-Kanade (Local Method):**
  - Assumes all pixels in a small $3 \\times 3$ window have the exact same motion vector $(u, v)$.
  - Stacks the equations into a matrix $\\mathbf{A} \\mathbf{u} = \\mathbf{b}$ and solves via least squares:
    $$\\mathbf{u} = (\\mathbf{A}^T \\mathbf{A})^{-1} \\mathbf{A}^T \\mathbf{b}$$
  - *Pros:* Fast and simple. Works great at sharp corners.
  - *Cons:* Fails on flat untextured surfaces where gradients are zero.
* **Horn-Schunck (Global Method):**
  - Adds a **global smoothness constraint** that forces neighboring pixels across the whole image to have similar motion:
    $$E = \\iint \\left[ (I_x u + I_y v + I_t)^2 + \\alpha^2 (\\|\\nabla u\\|^2 + \\|\\nabla v\\|^2) \\right] dx \\, dy$$
  - *Pros:* Generates a dense, beautiful vector field for every single pixel.
  - *Cons:* Computationally heavy; smooths over sharp object boundaries.

---

### 3. Sensitivity to Noise and Illumination Variations (Unit 4 Notes)

| Real-World Challenge | Bad Effect on Optical Flow | Engineering Solution |
| :--- | :--- | :--- |
| **Image Sensor Noise** | Derivative operators amplify noise, producing wild, erratic vectors. | Apply a **2D Gaussian smoothing filter** ($G_\\sigma \\ast I$) before calculating gradients. |
| **Illumination Changes** | Shadows or sun flashes violate brightness constancy, creating fake motion. | Apply **illumination normalization** (histogram equalization) or use gradient-based matching. |
| **Flat / Untextured Regions** | Gradients $I_x = 0, I_y = 0$, making $\\mathbf{A}^T \\mathbf{A}$ singular and dividing by zero! | Track only **Harris corner features** where both eigenvalues $\\lambda_1, \\lambda_2$ are large. |
| **Large Displacements** | Taylor approximation fails if motion is $>1$ pixel. | Build **Hierarchical Coarse-to-Fine Gaussian Pyramids** to track large moves."""
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
        "punchline": "Block matching algorithms partition frames into macroblocks and search for the lowest SAD error; Full Search checks all 225 spots (slow but perfect), while Three-Step Search checks only 25 spots (9x faster with 98% quality).",
        "mnemonic": "BMA: Full Search (Exhaustive), TSS (Coarse-to-fine), Diamond Search (Shape-adaptive). Cost: SAD, MAD, MSE.",
        "analogy": "Looking for your lost car in a massive parking lot: Full Search walks down every single row and checks every single parking spot (slow, exhausting, but guaranteed); Three-Step Search checks the main 4 corners of the lot, spots the right color cluster, and zooms into that sub-section in 3 quick hops.",
        "diagram": """CURRENT FRAME (Frame t)                     REFERENCE FRAME (Frame t-1)
┌──────────────────────┐                     ┌───────────────────────────┐
│                      │                     │      Search Window (±p)   │
│   ┌──────┐           │                     │      ┌─────────────┐      │
│   │Block │           │ ──────────────────► │      │  •   •   •  │      │
│   │16x16 │ (x, y)    │                     │      │  • [Match] •│      │
│   └──────┘           │                     │      │  •   •   •  │      │
└──────────────────────┘                     └──────┴─────────────┴──────┘
                                               Motion Vector: MV = (dx, dy)

SEARCH STRATEGIES COMPARED:
1. FULL SEARCH (Exhaustive):
   Evaluates all (2p + 1)² candidates ──► 225 evaluations for p=7 (Slow!)

2. THREE-STEP SEARCH (TSS):
   Step 1: Test 9 points at step S=4  ──► Find best minimum center
   Step 2: Test 8 points at step S=2  ──► Find best minimum center
   Step 3: Test 8 points at step S=1  ──► Best point is final MV! (Total: 25 points!)

3. DIAMOND SEARCH (DS):
   Large Diamond Pattern (9 points) ──► Shifts until center is minimum ──► Small Diamond (5 points)""",
        "content": """### 1. The Big Picture (How Block Matching Works)
In video compression (MPEG, H.264), we divide the current frame into non-overlapping squares called **macroblocks** (typically $16 \\times 16$ pixels).
For each block, we search a local window of size $\\pm p$ in the previous reference frame to find the best matching block that minimizes a distortion cost metric.

#### Matching Distortion Criteria (The Scorecards):
1. **Sum of Absolute Differences (SAD):**
   $$\\text{SAD}(dx, dy) = \\sum_{m=0}^{15} \\sum_{n=0}^{15} |F_t(x+m, y+n) - F_{t-1}(x+m+dx, y+n+dy)|$$
   *Why codecs love it:* Uses only additions and subtractions. Zero costly multiplications!
2. **Mean Squared Error (MSE):**
   $$\\text{MSE}(dx, dy) = \\frac{1}{256} \\sum_{m=0}^{15} \\sum_{n=0}^{15} [F_t - F_{t-1}]^2$$
   *Why it's slower:* Requires 256 hardware multiplications per candidate block.

---

### 2. Search Strategies (How We Find the Match Fast)

#### a) Full Search (Exhaustive Search - FS)
* **How it works:** Tests **every single possible integer location** in the $(2p + 1) \\times (2p + 1)$ search window.
* **Cost for $p = 7$:**
  $$N_{\\text{points}} = (2p + 1)^2 = (2(7) + 1)^2 = 15^2 = \\mathbf{225\\text{ block evaluations}}$$
* **Verdict:** Guarantees finding the absolute best global match. But doing 225 checks for thousands of blocks in 4K video melts CPU/battery in seconds!

#### b) Three-Step Search (TSS)
* **How it works (Coarse-to-Fine):**
  - **Step 1:** Set initial step size $S = 4$. Check the center $(0,0)$ and 8 surrounding points at distance 4. Pick the winner.
  - **Step 2:** Center a new grid on the winner, halve step size ($S = 2$), test 8 surrounding points. Pick the winner.
  - **Step 3:** Halve step size again ($S = 1$), test 8 surrounding points. The winner is your final motion vector!
* **Cost:** $9 + 8 + 8 = \\mathbf{25\\text{ evaluations}}$ (**$89\\%$ computational savings** over Full Search!).

#### c) Diamond Search (DS)
* **How it works:** Uses a diamond-shaped search pattern that matches the natural circular spread of real-world motion. Uses a Large Diamond (LDSP, 9 points) until the center wins, then switches to a Small Diamond (SDSP, 5 points) for final fine-tuning.
* **Cost:** Typically converges in **13 to 21 evaluations**, making it the modern standard for fast video encoders.

---

### 3. Cheat Sheet Comparison Table (Unit 4 Notes)

| Search Method | Search Points ($p=7$) | Computational Complexity | Matching Accuracy | Risk of Local Trap |
| :--- | :---: | :--- | :--- | :--- |
| **Full Search (FS)** | **225 points** | High ($O((2p+1)^2)$) | **$100\\%$ Optimal** (Global minimum) | None (Checks all) |
| **Three-Step Search (TSS)**| **25 points** | Low ($O(\\log p)$) | Very good for smooth linear motion | Moderate |
| **Diamond Search (DS)** | **13–21 points** | Very Low | Excellent for small-to-medium motion | Low |

---

### 4. Accuracy vs Complexity Trade-Offs
* **Block Size:** Smaller blocks ($4 \\times 4$) capture detailed motion but create millions of motion vectors that eat up bitrate. Larger blocks ($16 \\times 16$) save bitrate but fail around moving object boundaries.
* **Sub-Pixel Estimation (Half-Pel & Quarter-Pel):** Real objects don't move in integer pixel steps! Modern codecs interpolate reference frames with digital filters to test half-pixel and quarter-pixel offsets, boosting PSNR by $2\\text{ to }3\\text{ dB}$ at the cost of additional interpolation math."""
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
        "punchline": "Motion estimation is a nonlinear least-squares problem; Gradient Descent takes small safe steps, Gauss-Newton takes fast quadratic leaps, and Levenberg-Marquardt dynamically blends both with an adaptive damping factor λ.",
        "mnemonic": "G-G-L-N: Gradient Descent, Gauss-Newton, Levenberg-Marquardt, Newton's Method.",
        "analogy": "Hiking down a mountain in thick fog to find the lowest valley: Gradient Descent takes slow baby steps in the steepest downhill direction; Gauss-Newton calculates the 3D bowl shape and tries to jump straight to the bottom; Levenberg-Marquardt uses small cautious steps when the cliff is steep, and sprints directly to the bottom when the ground becomes smooth.",
        "diagram": """OBJECTIVE FUNCTION (Sum of Squared Residuals):
  E(p) = Σ [ I₂(x_i + u(x_i; p)) - I₁(x_i) ]² = Σ r_i(p)²
         i                                       i
  Find optimal motion parameters p = [t_x, t_y, θ, s]ᵀ that minimize E(p)!

THE LEVENBERG-MARQUARDT (LM) ADAPTIVE UPDATE:
  ( Jᵀ J + λ I ) Δp = - Jᵀ r
        ▲
        │
        ├── Large λ (Cliff edge / bad guess) ──► Behaves like Gradient Descent (Safe descent!)
        └── Small λ (Smooth valley floor)    ──► Behaves like Gauss-Newton (Fast quadratic sprint!)""",
        "content": """### 1. Formulating the Nonlinear Motion Problem (Unit 4 Notes)
In advanced video tracking (like estimating camera rotation or drone velocity), motion is controlled by a vector of parameters $\\mathbf{p} = [p_1, p_2, \\dots, p_K]^T$ (e.g., translation $t_x, t_y$, rotation angle $\\theta$, scale $s$).
We want to find optimal parameters $\\mathbf{p}^*$ that minimize the sum of squared intensity residuals between Frame 1 and Frame 2:
$$E(\\mathbf{p}) = \\sum_{i=1}^N \\left[ I_2(\\mathbf{x}_i + \\mathbf{u}(\\mathbf{x}_i; \\mathbf{p})) - I_1(\\mathbf{x}_i) \\right]^2 = \\sum_{i=1}^N r_i(\\mathbf{p})^2 = \\|\\mathbf{r}(\\mathbf{p})\\|_2^2$$
where $r_i(\\mathbf{p})$ is the intensity residual at pixel $i$.

**Why It's Nonlinear:** Because pixel values $I_2(\\cdot)$ jump around with complex textures, $E(\\mathbf{p})$ is a bumpy, non-convex mathematical landscape filled with local valleys.

---

### 2. The 4 Optimization Techniques Compared

#### 1. Gradient Descent (First-Order Method)
* **Update Rule:**
  $$\\mathbf{p}^{(k+1)} = \\mathbf{p}^{(k)} - \\alpha \\nabla E(\\mathbf{p}^{(k)})$$
* **Evaluation:**
  - *Pros:* Super cheap per step. Always goes downhill if step size $\\alpha$ is small.
  - *Cons:* Painfully slow linear convergence. Zigzags endlessly in narrow valleys.

#### 2. Gauss-Newton Method (Nonlinear Least Squares)
* **Update Rule:** Linearizes residuals via first-order Taylor series (approximating Hessian $\\mathbf{H} \\approx 2 \\mathbf{J}^T \\mathbf{J}$):
  $$\\Delta \\mathbf{p} = -(\\mathbf{J}^T \\mathbf{J})^{-1} \\mathbf{J}^T \\mathbf{r}$$
* **Evaluation:**
  - *Pros:* Fast quadratic convergence near the minimum.
  - *Cons:* If $\\mathbf{J}^T \\mathbf{J}$ is ill-conditioned (like in low-texture images), the matrix inversion blows up and optimization diverges!

#### 3. Levenberg-Marquardt (LM) Algorithm (The Gold Standard)
* **Update Rule:** Damps the matrix with adaptive parameter $\\lambda$:
  $$(\\mathbf{J}^T \\mathbf{J} + \\lambda \\mathbf{I}) \\Delta \\mathbf{p} = -\\mathbf{J}^T \\mathbf{r}$$
* **How the Adaptive Damping Works:**
  - If a step successfully lowers the error: Accept update, and **decrease $\\lambda$ by $10\\times$** (shifts toward fast Gauss-Newton).
  - If a step increases the error: Reject update, and **increase $\\lambda$ by $10\\times$** (shifts toward safe Gradient Descent).
* **Verdict:** The undisputed industry champion for 3D camera tracking and optical flow!

#### 4. Newton's Method (Full Second-Order)
* **Update Rule:** $\\Delta \\mathbf{p} = -\\mathbf{H}^{-1} \\nabla E(\\mathbf{p})$.
* **Evaluation:** Calculating the exact second-derivative Hessian matrix $\\mathbf{H}$ for thousands of pixels is computationally prohibitive.

---

### 3. Cheat Sheet Comparison Table (Unit 4 Notes)
| Technique | Convergence Speed | Computational Cost | Stability & Robustness |
| :--- | :--- | :--- | :--- |
| **Gradient Descent** | Slow (Linear) | Low | Depends heavily on learning rate |
| **Gauss-Newton** | Fast near minimum | Medium | Fragile (Diverges if initial guess is poor) |
| **Levenberg-Marquardt**| **Fast & Stable** | Medium-to-High | **Extremely Robust** (Guaranteed descent) |
| **Newton's Method** | Very Fast | Very High (Exact $\\nabla^2 E$) | Sensitive to non-positive definite Hessian |"""
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
        "punchline": "Transform-domain motion estimation matches DCT or DWT coefficients rather than raw pixels; DFT phase correlation calculates the normalized cross-power spectrum to produce a razor-sharp Dirac delta spike pointing to the exact motion displacement.",
        "mnemonic": "D-D-D: DCT energy matching, DFT Phase Correlation, DWT Multiresolution.",
        "analogy": "Comparing two songs: instead of comparing millions of raw microphone voltage samples, you look at the musical chord notes (transform domain). Shifting an entire photo simply changes the phase angle of the frequencies without changing the chord notes!",
        "diagram": """DFT-BASED PHASE CORRELATION ARCHITECTURE:
Frame 1 f₁(x, y) ──► [ 2D-FFT ] ──► F₁(u, v)
                                        │
                                        ├──► Cross-Power Spectrum R(u, v) = [ F₁ · F₂* ] / | F₁ · F₂* |
                                        │    (All magnitude stripped; only pure phase shift e^-j2π(udx+vdy)!)
Frame 2 f₂(x, y) ──► [ 2D-FFT ] ──► F₂(u, v)
                                        │
                                        ▼
                                 [ 2D-IFFT ]
                                        │
                                        ▼
                  Correlation Surface r(x, y) = δ(x - dx, y - dy)
                                        │
                                        ▼
                  Peak Location (x, y) = Exact Motion Vector (dx, dy)!""",
        "content": """### 1. The Big Picture (Why Estimate Motion in Transform Domain?)
Searching for matching blocks in spatial pixel grids takes millions of slide-and-compare operations. 
**Transform-domain motion estimation** operates directly on mathematical transform coefficients (DCT, DFT, or Wavelets), slashing computation and offering built-in immunity to lighting variations.

---

### 2. Design of the 3 Transform-Domain Algorithms (Unit 4 Notes)

#### A. DFT-Based Phase Correlation (Global Camera Motion)
* **The Fourier Shift Principle:**
  If Frame 2 is a shifted version of Frame 1: $f_2(x, y) = f_1(x - d_x, y - d_y)$, their Fourier transforms satisfy:
  $$F_2(u, v) = F_1(u, v) \\, e^{-j 2\\pi \\left( \\frac{u d_x}{M} + \\frac{v d_y}{N} \\right)}$$
* **The Step-by-Step Algorithm:**
  1. Compute 2D-FFT of Frame 1 and Frame 2.
  2. Compute the **Normalized Cross-Power Spectrum**:
     $$R(u, v) = \\frac{F_2(u, v) \\cdot F_1^*(u, v)}{|F_2(u, v) \\cdot F_1^*(u, v)|} = e^{-j 2\\pi \\left( \\frac{u d_x}{M} + \\frac{v d_y}{N} \\right)}$$
     *(Dividing by magnitude strips away all image content and illumination bias, leaving pure phase!)*
  3. Compute the 2D Inverse FFT of $R(u, v)$:
     $$r(x, y) = \\mathcal{F}^{-1}\\{R(u, v)\\} = \\delta(x - d_x, y - d_y)$$
  4. **Find the Spike:** The correlation surface $r(x, y)$ forms a razor-sharp Dirac delta impulse peak. The coordinate of that peak is your exact global motion vector $(d_x, d_y)$!
* **Advantage:** Runs in $O(N^2 \\log N)$ time, completely independent of how far the object moved!

#### B. DCT-Based Motion Estimation (Fast Macroblock Matching)
* **How it works:** Apply 2D-DCT on $8 \\times 8$ blocks. Because DCT compacts $>90\\%$ of energy into the top-left low frequencies, we evaluate matching error on **only 8 to 10 low-frequency coefficients** and discard the rest.
* **Advantage:** Cuts matching calculations by $75\\%$.

#### C. DWT-Based Multiresolution Wavelet Search
* **How it works:** Decomposes frames into Wavelet octave subbands ($LL, LH, HL, HH$).
  - Search coarse motion in the low-resolution $LL$ subband ($16\\times$ smaller search grid).
  - Propagate the vector down to full resolution and refine within a tiny $\\pm 1$ pixel window.

---

### 3. Optimization Techniques & Justifications Table
| Technique | Performance Benefit | Engineering Justification |
| :--- | :--- | :--- |
| **FFT Phase Correlation** | Ultra-fast global pan/tilt estimation | Replaces spatial search with point-wise multiplications |
| **Low-Frequency DCT Selection**| $75\\%$ reduction in matching operations | High frequencies contain negligible motion energy |
| **Multiresolution Wavelet Search**| Prevents local traps during huge motion | Coarse subband bounds large shifts before local tuning |
| **Rate-Distortion Optimization (RDO)**| Balances video quality against file size | Minimizes Lagrangian cost $J = D + \\lambda R$ |"""
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
        "punchline": "The framework reconstructs 3D point clouds and tracks 6-DOF camera trajectories across 8 stages by fusing Geometric models (Essential matrix, Triangulation) with Statistical models (RANSAC outlier rejection, Kalman filtering, Bundle Adjustment).",
        "mnemonic": "A-F-M-C-S-M-O-R: Acquisition, Features, Matching, Calibration, Structure, Motion, Optimization, Reconstruction.",
        "analogy": "Like human stereo vision: your two eyes take flat 2D pictures from slightly different angles (geometric projection); your brain matches landmarks (epipolar geometry), ignores optical illusions (RANSAC), and calculates 3D depth so you can catch a baseball without missing.",
        "diagram": """+-------------------------------------------------------------------------------+
|         3D MOTION AND STRUCTURE ESTIMATION FRAMEWORK (SfM / SLAM)             |
+-------------------------------------------------------------------------------+

 [ Input 2D Video Stream ] ──► Sequential frames (F_t, F_{t+1})
           │
           ▼
 [ 1. Feature Extraction ] ──► Detects scale-invariant keypoints (SIFT / ORB)
           │
           ▼
 [ 2. Correspondence Match]──► Matches descriptors across frames
           │
           ▼
 [ 3. Epipolar & RANSAC ]  ──► Essential Matrix E = [t]× R (Rejects false feature outliers!)
           │
           ▼
 [ 4. Triangulation ]      ──► 3D Point Reconstruction: X = (X, Y, Z)ᵀ
           │
           ▼
 [ 5. 3D Motion Estimation]──► Recovers 6-DOF Camera Pose: Rotation R and Translation t
           │
           ▼
 [ 6. Kalman Filter ]      ──► Predicts & smooths dynamic object velocities over time
           │
           ▼
 [ 7. Bundle Adjustment ]  ──► Minimizes total 2D reprojection error: min Σ ||x_ij - π(K, R, t, X_j)||²
           │
           ▼
 [ 8. 3D Scene Output ]    ──► Metric 3D Point Cloud + Vehicle Trajectory for Autonomous Driving""",
        "content": """### 1. The Big Picture (Structure from Motion / Visual SLAM)
How does a Tesla self-driving car or an augmented reality headset (Apple Vision Pro) look at flat 2D video frames and understand a 3D world with depth, buildings, and moving cars?
**3D Motion and Structure Estimation (Structure from Motion - SfM)** fuses rigid **Geometric Models** with noise-filtering **Statistical Models** across 8 sequential stages.

---

### 2. The 8 Stages of the Comprehensive Framework (Unit 4 Notes)
1. **Video Ingestion & Calibration:** Ingests video and determines the **Intrinsic Camera Matrix $\\mathbf{K}$** (focal length $f$, optical center $c_x, c_y$).
2. **Feature Detection:** Detects sharp, illumination-proof keypoints (SIFT, ORB).
3. **Feature Matching & Epipolar Geometry:** Matches keypoints between frames. Constrained by the **Essential Matrix $\\mathbf{E} = [\\mathbf{t}]_\\times \\mathbf{R}$** ($x'^T E x = 0$).
4. **RANSAC (Statistical Outlier Rejection):** Randomly samples 8-point sets to fit the Essential matrix while discarding false matches (like passing shadows or reflections).
5. **3D Motion Estimation (Pose Recovery):** Decomposes $\\mathbf{E}$ via SVD into the camera's 6-DOF 3D rotation $\\mathbf{R}$ and translation vector $\\mathbf{t}$.
6. **3D Structure Triangulation:** Intersects light rays from multiple camera poses to calculate exact 3D coordinates $(X, Y, Z)$ for every feature point.
7. **Kalman Filtering:** Smooths trajectory jitter and predicts moving vehicle positions during occlusions.
8. **Bundle Adjustment (Global Optimization):** Uses the Levenberg-Marquardt algorithm to refine all 3D points and camera angles simultaneously, minimizing total reprojection error:
   $$\\min_{\\{\\mathbf{R}_i, \\mathbf{t}_i, \\mathbf{X}_j\\}} \\sum_{i} \\sum_{j} \\|\\mathbf{x}_{ij} - \\pi(\\mathbf{K}, \\mathbf{R}_i, \\mathbf{t}_i, \\mathbf{X}_j)\\|^2$$

---

### 3. Integration Table: Geometric vs Statistical Models
| Geometric Model | Statistical Model Partner | Purpose in Framework |
| :--- | :--- | :--- |
| **Perspective Camera Projection** | **Maximum Likelihood Estimation (MLE)** | Reconstructs 3D coordinates under sensor noise |
| **Epipolar Constraint ($x'^T E x = 0$)**| **RANSAC Algorithm** | Rejects up to $50\\%$ false correspondence outliers |
| **Multi-View Triangulation** | **Kalman Filter** | Tracks 3D velocities of moving vehicles over time |
| **6-DOF Camera Motion Model** | **Bundle Adjustment (LM)** | Eliminates cumulative drift error over long routes |

---

### 4. Real-World Autonomous Vehicle Assessment (Unit 4 Notes)
In self-driving cars (Tesla Vision / Waymo):
- **Ego-Motion Recovery:** Front cameras calculate the car's millimeter-accurate speed and steering angle without needing wheel sensors or GPS.
- **3D Obstacle Mapping:** Triangulates distance to leading vehicles, curbs, and road debris.
- **Safety Tracking:** Kalman filtering predicts whether a pedestrian will cross into the car's braking path in the next 2.0 seconds, enabling collision-free navigation."""
    }
]
