# -*- coding: utf-8 -*-
"""
Unit 4: 2D & 3D Motion Estimation, Optical Flow & Video Analysis
Questions: Mid-II Q5 to Q12
Academic Year: 2026-27 | Regulation: KGR23 | Course Code: KG23ACM408
Scaled strictly for exam success (05 Marks vs 10 Marks format).
"""

UNIT4_QUESTIONS = [
    {
        "id": "MID2-Q05",
        "mid": "Mid-II",
        "qno": 5,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K1",
        "marks": "05 Marks",
        "title": "Classify the fundamental principles of image formation models and their role in motion estimation frameworks.",
        "punchline": "Image formation models describe how 3D dynamic scenes project onto a 2D sensor through Geometric (perspective projection) and Photometric (illumination-reflectance) models.",
        "mnemonic": "G-P-C-M: Geometric projection, Photometric lighting, Camera intrinsics, Motion framework",
        "analogy": "A shadow puppet show: The puppet's 3D motion is projected onto a 2D cloth screen (geometric model), while the torch's brightness and puppet's opacity determine how dark the shadow is (photometric model).",
        "diagram": """IMAGE FORMATION PRINCIPLES IN MOTION ESTIMATION:

1. GEOMETRIC MODEL (3D World ──► 2D Sensor):
   World Point P(X, Y, Z) ──► [ Perspective Projection ] ──► Image Point p(x, y)
                              x = f · (X / Z),   y = f · (Y / Z)
                              (Objects moving away appear smaller!)

2. PHOTOMETRIC / RADIOMETRIC MODEL (Scene Radiance ──► Pixel Intensity):
   Illumination L(x, y) ──► [ Surface Reflectance R(x, y) ] ──► Image Irradiance I(x, y)
                            I(x, y) = L(x, y) · R(x, y)

3. ROLE IN MOTION ESTIMATION:
   Motion Estimator must differentiate:
   - True Geometric Displacement (Moving object)  VS
   - Photometric Artifacts (Flickering light, casting shadow)""",
        "content": """### 1. Overview of Image Formation Models
An image formation model mathematically describes the physical process through which a 3D real-world scene is converted into a 2D digital image sequence $I(x, y, t)$ by an optical imaging sensor (camera). In video processing, understanding image formation is critical so that motion estimation algorithms can distinguish true physical object motion from lighting fluctuations.

---

### 2. Classification of Fundamental Principles

#### 1. The Geometric Projection Model
* **Principle:** Describes the spatial mapping of 3D real-world coordinates $(X, Y, Z)$ onto the 2D camera sensor plane $(x, y)$.
* **Pinhole Perspective Projection Model:**
  $$x = f \\frac{X}{Z}, \\quad y = f \\frac{Y}{Z}$$
  where $f$ is the camera focal length and $Z$ is the optical depth (distance from camera).
* **Role in Motion Estimation:**
  * Apparent motion in 2D image coordinates is inversely proportional to depth $Z$. Objects closer to the camera appear to move faster than distant objects even when moving at the same physical velocity (Motion Parallax).
  * As an object moves away from the camera ($Z$ increases), its apparent size shrinks geometrically.

#### 2. The Photometric / Radiometric Model
* **Principle:** Describes how incoming illumination interacts with surface materials to produce pixel intensity (irradiance):
  $$I(x, y) = L(x, y) \\cdot R(x, y)$$
  * $L(x, y)$: Illumination component (amount of incident light from the source).
  * $R(x, y)$: Reflectance component (fraction of light reflected by the physical material, $0 \\le R \\le 1$).
* **Role in Motion Estimation:**
  * Motion estimation algorithms rely on the **Brightness Constancy Assumption** (that pixel brightness is invariant under motion).
  * The photometric model reveals when this assumption breaks down—such as when a car drives under a streetlight, cast shadows move across a wall, or specular reflections glint on glossy metal.

#### 3. Camera Parameters (Extrinsic and Intrinsic)
* **Intrinsic Parameters ($K$):** Focal length ($f_x, f_y$), principal point $(c_x, c_y)$, and lens radial distortion.
* **Extrinsic Parameters ($[R | \\mathbf{t}]$):** 3D camera rotation matrix $R$ and 3D translation vector $\\mathbf{t}$ relative to the world coordinate system.
* **Role in Motion Estimation:** Essential in Structure from Motion (SfM) to decouple camera egomotion (pan, tilt, zoom) from independent object motion.

---

### 3. Summary of Roles in Motion Estimation

| Model | Primary Mechanism | Critical Contribution to Motion Estimation |
| :--- | :--- | :--- |
| **Geometric Model** | Perspective projection ($X/Z, Y/Z$) | Relates 2D optical flow to real 3D velocity and object depth |
| **Photometric Model** | Illumination $\\times$ Reflectance | Provides brightness conservation basis; models lighting changes |
| **Camera Model** | Intrinsic & Extrinsic matrices | Allows camera motion compensation and 3D scene reconstruction |"""
    },
    {
        "id": "MID2-Q06",
        "mid": "Mid-II",
        "qno": 6,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K2",
        "marks": "05 Marks",
        "title": "Explain the mathematical representation of motion models and interpret their assumptions in real-world dynamic scenes.",
        "punchline": "Motion models parameterize 2D pixel displacement via Translational (2 DOF), Affine (6 DOF), or Projective (8 DOF) transforms under Brightness Constancy and Spatial Coherence assumptions.",
        "mnemonic": "T-A-P-B-S: Translational, Affine, Projective; Brightness constancy, Spatial coherence",
        "analogy": "Manipulating a photo in graphic software: Translational is dragging the photo with your mouse; Affine is rotating, shearing, and stretching it; Projective is tilting it in 3D perspective.",
        "diagram": """PARAMETRIC 2D MOTION MODELS (Degrees of Freedom):

1. TRANSLATIONAL (2 DOF):
   [ x' ] = [ x ] + [ dx ]        (Rigid shift; uniform camera pan)
   [ y' ]   [ y ]   [ dy ]

2. AFFINE MODEL (6 DOF):
   [ x' ] = [ a11  a12 ] [ x ] + [ dx ]  (Translation, Rotation,
   [ y' ]   [ a21  a22 ] [ y ]   [ dy ]   Scale, and Shear)

3. PROJECTIVE / HOMOGRAPHY (8 DOF):
   x' = (h11·x + h12·y + h13) / (h31·x + h32·y + 1)   (Full 3D planar rotation
   y' = (h21·x + h22·y + h23) / (h31·x + h32·y + 1)    and perspective tilt)

CORE MOTION ASSUMPTIONS:
  1. Brightness Constancy : I(x+dx, y+dy, t+dt) = I(x, y, t)
  2. Small Motion         : Displacement ||d|| is small between adjacent frames
  3. Spatial Coherence    : Neighboring pixels move together with identical velocity""",
        "content": """### 1. Mathematical Representation of Motion Models
In video processing, motion estimation describes how pixel coordinates $(x, y)$ in frame $t$ map to new coordinates $(x', y')$ in frame $t + 1$:
$$x' = f(x, y; \\mathbf{p}), \\quad y' = g(x, y; \\mathbf{p})$$
where $\\mathbf{p}$ is the motion parameter vector.

#### 1. Translational Motion Model (2 Degrees of Freedom - DOF)
* **Equation:**
  $$\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = \\begin{bmatrix} x \\\\ y \\end{bmatrix} + \\begin{bmatrix} d_x \\\\ d_y \\end{bmatrix}$$
* **Parameters ($2$):** $\\mathbf{p} = [d_x, d_y]^T$ (horizontal and vertical translation).
* **Application:** Standard Block Matching Algorithms (MPEG, H.264). Assumes all pixels within a block undergo identical rigid translation.

#### 2. Affine Motion Model (6 Degrees of Freedom - DOF)
* **Equation:**
  $$\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = \\begin{bmatrix} a_{11} & a_{12} \\\\ a_{21} & a_{22} \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} + \\begin{bmatrix} d_x \\\\ d_y \\end{bmatrix}$$
* **Parameters ($6$):** $\\mathbf{p} = [a_{11}, a_{12}, a_{21}, a_{22}, d_x, d_y]^T$.
* **Capabilities:** Handles translation, 2D in-plane rotation, non-uniform scaling (zoom), and shear. Preserves parallel lines.

#### 3. Projective / Homography Model (8 Degrees of Freedom - DOF)
* **Equation:**
  $$x' = \\frac{h_{11} x + h_{12} y + h_{13}}{h_{31} x + h_{32} y + 1}, \\quad y' = \\frac{h_{21} x + h_{22} y + h_{23}}{h_{31} x + h_{32} y + 1}$$
* **Parameters ($8$):** Describes the exact perspective projection of a rigid planar surface moving arbitrarily in 3D space.

---

### 2. Core Assumptions in Real-World Dynamic Scenes

#### 1. Brightness Constancy Assumption (BCA)
* **Assumption:** The visual intensity of a physical scene point remains constant over time along its motion trajectory:
  $$I(x + d_x, y + d_y, t + \\Delta t) = I(x, y, t)$$
* **Real-World Violations:**
  * Changing lighting conditions (sun ducking behind clouds).
  * Specular non-Lambertian reflections on shiny metallic or water surfaces.
  * Moving shadows and occlusions.

#### 2. Small Motion Assumption
* **Assumption:** Temporal sampling is sufficiently fast such that frame-to-frame displacement $[d_x, d_y]^T$ is small (less than 1-2 pixels).
* **Engineering Justification:** Enables first-order Taylor series expansions for differential optical flow algorithms. Violated during fast sports or camera whip-pans (solved via multi-scale Gaussian pyramids).

#### 3. Spatial Coherence (Smoothness) Assumption
* **Assumption:** Real-world objects are spatially continuous; neighboring pixels belong to the same object surface and share smooth, similar motion vectors.
* **Real-World Violations:** Breaks down at **motion boundaries** (depth discontinuities where a moving foreground object slides past a static background)."""
    },
    {
        "id": "MID2-Q07",
        "mid": "Mid-II",
        "qno": 7,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K3",
        "marks": "05 Marks",
        "title": "By using  Block Motion Estimation A block in Frame 1 is at:  (20,25) Best match in Frame 2 is at: (23,30) Compute motion vector  Interpret direction of motion",
        "punchline": "Motion vector is $\\vec{d} = (\\Delta x, \\Delta y) = (3, 5)$; magnitude $|\\vec{d}| = \\sqrt{34} \\approx 5.83\\text{ pixels}$; moving rightward (+3) and downward (+5) at angle $59.04^\\circ$.",
        "mnemonic": "D-M-D: Difference of coordinates (Frame 2 - Frame 1), Magnitude via Pythagoras, Direction via Arctan",
        "analogy": "Checking GPS coordinates: If you started at coordinates (20, 25) and moved to (23, 30), your displacement vector is (+3 east, +5 south).",
        "diagram": """BLOCK MOTION ESTIMATION GEOMETRY:
   Frame 1 (t)                               Frame 2 (t+1)
   (0,0) ──────────────► x                  (0,0) ──────────────► x
     │                                        │
     │      (20, 25)                          │
  25 │───────■ [Block 1]                   25 │       · · · · ·
     │                                        │       ·       ·
  30 │                                     30 │───────·───────■ (23, 30) [Best Match]
     ▼ y                                      ▼ y            23

DISPLACEMENT VECTOR CALCULATION:
   Δx = x2 - x1 = 23 - 20 = +3 pixels (Rightward)
   Δy = y2 - y1 = 30 - 25 = +5 pixels (Downward in image coords)

   Motion Vector d = (3, 5)
   Magnitude ||d|| = √(3² + 5²) = √34 ≈ 5.83 pixels
   Direction θ = arctan(5/3) ≈ 59.04° (Down-Right)""",
        "content": """### 1. Given Data
* Position of the block center in **Frame 1 (Reference Frame, $t$)**:
  $$(x_1, y_1) = (20, 25)$$
* Position of the best matching block in **Frame 2 (Target Frame, $t+1$)**:
  $$(x_2, y_2) = (23, 30)$$

---

### 2. Task 1: Compute the Motion Vector ($\\vec{d}$)
The motion vector $\\vec{d} = (\\Delta x, \\Delta y)$ is defined as the spatial displacement from the initial position in Frame 1 to the matched position in Frame 2:
$$\\Delta x = x_2 - x_1$$
$$\\Delta y = y_2 - y_1$$

Substituting the given values:
$$\\Delta x = 23 - 20 = +3\\text{ pixels}$$
$$\\Delta y = 30 - 25 = +5\\text{ pixels}$$

$$\\mathbf{Motion\\ Vector: } \\quad \\vec{d} = (\\Delta x, \\Delta y) = \\mathbf{(3, 5)}$$

---

### 3. Task 2: Compute Magnitude of Motion ($|\\vec{d}|$)
The magnitude (Euclidean distance traveled by the block) is:
$$|\\vec{d}| = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2}$$

Substituting $\\Delta x = 3$ and $\\Delta y = 5$:
$$|\\vec{d}| = \\sqrt{3^2 + 5^2} = \\sqrt{9 + 25} = \\sqrt{34} \\approx \\mathbf{5.831\\text{ pixels}}$$

---

### 4. Task 3: Interpret Direction of Motion
In digital video and image processing, the standard coordinate system defines:
* The **horizontal $x$-axis** increases from left to right ($\\\\to$).
* The **vertical $y$-axis** increases from top to bottom ($\\downarrow$).

#### Interpretation:
1. **Horizontal Component ($\\Delta x = +3$):** The positive sign indicates that the block has moved **$3\\text{ pixels}$ to the RIGHT**.
2. **Vertical Component ($\\Delta y = +5$):** The positive sign indicates that the block has moved **$5\\text{ pixels}$ DOWNWARD**.
3. **Angular Direction ($\\theta$):**
   $$\\theta = \\arctan\\left(\\frac{\\Delta y}{\\Delta x}\\right) = \\arctan\\left(\\frac{5}{3}\\right) = \\arctan(1.6667) \\approx \\mathbf{59.04^\\circ}$$
   *(measured clockwise relative to the positive horizontal $x$-axis).*

$$\\mathbf{Final\\ Interpretation: } \\quad \\text{The block exhibits downward-right motion of } \\mathbf{5.83\\text{ pixels}} \\text{ at an angle of } \\mathbf{59.04^\\circ}.$$"""
    },
    {
        "id": "MID2-Q08",
        "mid": "Mid-II",
        "qno": 8,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K4",
        "marks": "05 Marks",
        "title": "Implement differential methods for motion estimation and analyze their sensitivity to noise and illumination variations.",
        "punchline": "Differential optical flow uses spatial/temporal image gradients: Optical Flow Constraint $I_x u + I_y v + I_t = 0$; suffers from the Aperture Problem; solved locally via Lucas-Kanade and globally via Horn-Schunck.",
        "mnemonic": "O-A-L-H: Optical Flow Constraint, Aperture problem, Lucas-Kanade local, Horn-Schunck global",
        "analogy": "Looking at a smooth white flagpole through a tiny round keyhole: When the pole moves up or down, you see zero change; only horizontal motion is visible (the classic Aperture Problem).",
        "diagram": """OPTICAL FLOW CONSTRAINT & APERTURE PROBLEM:
  Taylor Expansion: I(x+u, y+v, t+1) ≈ I(x, y, t) + Ix·u + Iy·v + It = I(x, y, t)
  ──► Optical Flow Equation: Ix · u + Iy · v + It = 0  (1 equation, 2 unknowns!)

THE APERTURE PROBLEM:
  ┌────────────────┐
  │      /         │  Only motion NORMAL (perpendicular) to the edge can be measured!
  │    /           │  Motion parallel to the edge is completely invisible.
  │  /  ──► v_norm │
  └────────────────┘

DIFFERENTIAL METHODS COMPARISON:
  1. LUCAS-KANADE (Local): Assumes constant velocity in 3x3 window -> Overdetermined least-squares
  2. HORN-SCHUNCK (Global): Adds global smoothness regularization -> Iterative Gauss-Seidel PDE""",
        "content": """### 1. The Optical Flow Constraint Equation (OFCE)
Differential methods estimate optical flow $(u, v) = \\left(\\frac{dx}{dt}, \\frac{dy}{dt}\\right)$ using spatial and temporal partial derivatives of image brightness.

#### Derivation:
Assuming the Brightness Constancy Assumption holds:
$$I(x + dx, y + dy, t + dt) = I(x, y, t)$$
Applying first-order 2D Taylor series expansion:
$$I(x + dx, y + dy, t + dt) \\approx I(x, y, t) + \\frac{\\partial I}{\\partial x} dx + \\frac{\\partial I}{\\partial y} dy + \\frac{\\partial I}{\\partial t} dt$$
Subtracting $I(x, y, t)$ and dividing by $dt$:
$$\\frac{\\partial I}{\\partial x} \\frac{dx}{dt} + \\frac{\\partial I}{\\partial y} \\frac{dy}{dt} + \\frac{\\partial I}{\\partial t} = 0$$

$$\\mathbf{I_x u + I_y v + I_t = 0 \\quad \\iff \\quad \\nabla I^T \\mathbf{v} + I_t = 0}$$
where $I_x = \\frac{\\partial I}{\\partial x}$, $I_y = \\frac{\\partial I}{\\partial y}$, and $I_t = \\frac{\\partial I}{\\partial t}$.

---

### 2. The Aperture Problem
* The optical flow equation is a **single linear equation with two unknowns ($u$ and $v$)**.
* It can only determine the component of velocity perpendicular to the image gradient (normal flow $v_\\perp$). The tangential component $v_\\parallel$ parallel to the edge is completely unconstrained.
* To solve for both $(u, v)$, an additional constraint is mathematically mandatory.

---

### 3. Implementation Approaches

#### 1. Lucas-Kanade Method (Local Least-Squares Constraint)
* **Assumption:** Optical flow is constant within a small local neighborhood (e.g. $3 \\times 3$ window of $N=9$ pixels).
* **System of Equations:**
  $$\\begin{bmatrix} I_{x1} & I_{y1} \\\\ I_{x2} & I_{y2} \\\\ \\vdots & \\vdots \\\\ I_{x9} & I_{y9} \\end{bmatrix} \\begin{bmatrix} u \\\\ v \\end{bmatrix} = - \\begin{bmatrix} I_{t1} \\\\ I_{t2} \\\\ \\vdots \\\\ I_{t9} \\end{bmatrix} \\implies \\mathbf{A} \\mathbf{v} = \\mathbf{b}$$
* **Least-Squares Solution:**
  $$\\mathbf{v} = \\left( \\mathbf{A}^T \\mathbf{A} \\right)^{-1} \\mathbf{A}^T \\mathbf{b}$$
  Solvable if $\\mathbf{A}^T \\mathbf{A}$ has two large eigenvalues (i.e. at textured corners).

#### 2. Horn-Schunck Method (Global Smoothness Constraint)
* **Formulation:** Minimizes a global energy functional combining brightness constancy error and a spatial smoothness regularization term:
  $$E(u, v) = \\iint \\left[ (I_x u + I_y v + I_t)^2 + \\alpha^2 \\left( \\left(\\frac{\\partial u}{\\partial x}\\right)^2 + \\left(\\frac{\\partial u}{\\partial y}\\right)^2 + \\left(\\frac{\\partial v}{\\partial x}\\right)^2 + \\left(\\frac{\\partial v}{\\partial y}\\right)^2 \\right) \\right] dx dy$$
* Solved iteratively using Gauss-Seidel relaxation to produce a dense flow field.

---

### 4. Sensitivity Analysis

| Environmental Perturbation | Impact on Differential Methods | Mitigation Technique |
| :--- | :--- | :--- |
| **High Sensor Noise** | Derivative operators ($I_x, I_y, I_t$) amplify high-frequency noise, ruining gradient estimates. | Pre-filter frames with a 2D Gaussian smoothing filter ($G_\\sigma$). |
| **Illumination Changes** | Directly violates the core assumption $I(t+dt) = I(t)$, generating massive false motion vectors. | Normalize contrast via gradient constancy ($|\\nabla I|$) or census transform. |
| **Large Displacements ($>2$ px)** | Taylor series truncation error explodes; gradient descent fails to converge. | Multi-scale coarse-to-fine Gaussian pyramids. |"""
    },
    {
        "id": "MID2-Q09",
        "mid": "Mid-II",
        "qno": 9,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Analyze matching-based motion estimation methods and evaluate their computational complexity and accuracy trade-offs.",
        "punchline": "Matching-based methods divide frames into macroblocks and search for optimal displacements using matching criteria (SAD/MAD/MSE); Full Search is optimal but heavy O((2p+1)^2); Fast algorithms (TSS, 2D-Log, Diamond) achieve 90% speedup with minimal loss.",
        "mnemonic": "F-T-D-C: Full Search, Three-Step Search, Diamond Search, Criteria (SAD/MAD)",
        "analogy": "Searching for a missing puzzle piece: Full Search tests every single piece on the table one by one; Three-Step Search tests 8 widely spaced pieces, picks the closest zone, and zooms in iteratively.",
        "diagram": """BLOCK MATCHING ALGORITHMS (Search Strategies):

1. FULL SEARCH (Exhaustive Search over [-p, +p]):
   Tests ALL (2p+1)² candidate locations in search window.
   For p = 7 ──► 225 candidate locations per block! (High compute, 100% optimal)

2. THREE-STEP SEARCH (TSS):
   Step 1: Check 8 points at step s = 4 around center (0,0)
   Step 2: Center around minimum, halve step s = 2, check 8 points
   Step 3: Center around minimum, halve step s = 1, check 8 points
   Total Points Checked: 1 + 8 + 8 + 8 = 25 Points! (9x Faster than Full Search!)

   Step 1 (s=4)        Step 2 (s=2)        Step 3 (s=1)
   ●     ●     ●
                       ●   ●   ●
   ●    (0)    ●           ●           ● ● ●
                       ●   ●   ●       ● ★ ● ◄── Final Best Match
   ●     ●     ●                       ● ● ●""",
        "content": """### 1. Principle of Matching-Based Motion Estimation
Block Matching Algorithms (BMA) are the universal standard for video compression (MPEG-1/2/4, H.261/263/264, HEVC).
* The current target frame $t$ is partitioned into non-overlapping blocks of size $N \\times N$ (typically $16 \\times 16$ macroblocks or $8 \\times 8$ blocks).
* For each block centered at $(x, y)$, the algorithm searches within a predefined search area $[-p, +p]$ in reference frame $t - 1$ to find the candidate block that minimizes a matching error criterion.

---

### 2. Matching Error Criteria

#### 1. Mean Absolute Difference (MAD) / Sum of Absolute Differences (SAD)
$$SAD(d_x, d_y) = \\sum_{i=0}^{N-1} \\sum_{j=0}^{N-1} |I_t(x + i, y + j) - I_{t-1}(x + i + d_x, y + j + d_y)|$$
* **Evaluation:** Computationally most efficient. Requires only integer subtractions, absolute values, and additions (no multiplications). Universally implemented in hardware encoders.

#### 2. Mean Squared Error (MSE)
$$MSE(d_x, d_y) = \\frac{1}{N^2} \\sum_{i=0}^{N-1} \\sum_{j=0}^{N-1} \\left(I_t(x + i, y + j) - I_{t-1}(x + i + d_x, y + j + d_y)\\right)^2$$
* **Evaluation:** Matches the $L_2$ norm and theoretical Rate-Distortion Optimization (RDO), but requires $N^2$ multiplications per candidate, making it expensive for real-time video encoders.

---

### 3. Detailed Algorithmic Evaluation & Search Strategies

#### 1. Full Search (Exhaustive Search - FS)
* **Algorithm:** Evaluates SAD at **every single integer location** within the $(2p + 1) \\times (2p + 1)$ search window.
* **Complexity:**
  $$C_{\\text{FS}} = (2p + 1)^2 \\text{ candidate locations per block}$$
  For search parameter $p = 7$: $(2 \\times 7 + 1)^2 = 15^2 = \\mathbf{225\\text{ search points/block}}$.
  For a 1080p frame ($8160$ blocks of $16 \\times 16$): $\\\\approx 470\\text{ million operations per frame!}$
* **Accuracy:** Universally **optimal**. Finds the global minimum error and produces the smallest residual bitrate.

#### 2. Three-Step Search (TSS)
* **Algorithm:**
  1. Initialize step size $s = 2^{\\lfloor \\log_2 p \\rfloor - 1}$ (for $p = 7, s = 4$). Test the center point $(0, 0)$ and 8 surrounding points at distance $s$.
  2. Find the point with minimum SAD. Set it as the new center, halve the step size $s = s / 2 = 2$, and test 8 surrounding points.
  3. Halve step size again ($s = 1$), test 8 points. The minimum point is the final motion vector.
* **Complexity:**
  $$C_{\\text{TSS}} = 1 + 8 + 8 + 8 = \\mathbf{25\\text{ search points/block (a 9x speedup over FS!)}}$$
* **Trade-off:** Assumes the error surface is monotonically unimodal. If the surface is multimodal, it can get trapped in local minima, leading to slightly higher prediction residuals.

#### 3. 2D-Logarithmic Search
* **Algorithm:** Successively tracks along coordinate axes using a cross-shaped pattern ($5$ points), halving step size when the minimum is at the center or boundary.
* **Complexity:** Typically $13$ to $21$ points per block.

#### 4. Diamond Search (DS)
* **Algorithm:** Employs Large Diamond Search Pattern (LDSP - 9 points) until the minimum falls at the center, then switches to Small Diamond Search Pattern (SDSP - 5 points).
* **Evaluation:** The standard algorithm in modern encoders; delivers near-Full-Search accuracy with only $15-20$ search points per block.

---

### 4. Comprehensive Trade-off Matrix

| Algorithm | Search Points ($p=7$) | Computational Complexity | Speedup vs. FS | Risk of Local Minima | PSNR vs. Full Search |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Full Search (FS)** | 225 | $O((2p+1)^2)$ | $1\\times$ (Baseline) | **Zero (Global Optimum)** | **Highest (Baseline 0 dB)** |
| **Three-Step Search** | 25 | $O(9 \\log_2 p)$ | $\\\\approx 9\\times$ | Moderate (in complex scenes) | $-0.3$ to $-0.6\\text{ dB}$ |
| **2D-Logarithmic** | 13 - 21 | $O(5 \\log_2 p)$ | $\\\\approx 12\\times$ | Moderate | $-0.4$ to $-0.7\\text{ dB}$ |
| **Diamond Search** | 15 - 20 | Adaptive | $\\\\approx 14\\times$ | Low (compact pattern) | $-0.1$ to $-0.2\\text{ dB}$ |"""
    },
    {
        "id": "MID2-Q10",
        "mid": "Mid-II",
        "qno": 10,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Critically evaluate nonlinear optimization techniques used in motion estimation and justify their convergence behavior",
        "punchline": "Nonlinear motion estimation optimizes parametric models (affine/homography) by minimizing sum-of-squared errors; Levenberg-Marquardt adaptively bridges Gradient Descent and Gauss-Newton for robust convergence.",
        "mnemonic": "G-G-L-P: Gradient descent, Gauss-Newton, Levenberg-Marquardt, Pyramidal coarse-to-fine",
        "analogy": "Hiking down a foggy mountain to find the lowest valley: Gradient descent takes small careful downhill steps; Gauss-Newton calculates a direct parabolic jump; Levenberg-Marquardt blends both depending on terrain roughness.",
        "diagram": """NONLINEAR OPTIMIZATION CONVERGENCE COMPARISON:

  Error Surface E(p)
  ▲
  │    Gauss-Newton Jump (Fast quadratic convergence near minimum)
  │            ╭───────╮       ▲
  │           ╭         ╮     ╱
  │          ╭    Local  ╮   ╱  Divergence Risk if Hessian is ill-conditioned!
  │         ╭    Minimum  ╮ ╱
  │        ╭               v
  │       ╭─────────────────╮
  │      ╭   Global Minimum  ╮
  └─────┴─────────────────────┴──────────────────► Parameter Vector p

LEVENBERG-MARQUARDT DAMPING DYNAMICS:
  Update Equation: Δp = - (J^T J + λ · diag(J^T J))^-1 · J^T · r
  - If λ is LARGE : Behaves like GRADIENT DESCENT (Guaranteed descent, slow)
  - If λ is SMALL : Behaves like GAUSS-NEWTON     (Quadratic convergence near minimum)

MULTI-RESOLUTION COARSE-TO-FINE PYRAMID (Overcomes Local Minima):
  Level 2 (Coarse 1/4 Res) ──► Level 1 (Medium 1/2 Res) ──► Level 0 (Full Res)""",
        "content": """### 1. The Nonlinear Optimization Problem in Motion Estimation
When estimating multi-parameter motion models (Affine: 6 parameters, Homography: 8 parameters), block-matching exhaustive search becomes mathematically impossible due to exponential parameter dimensionality.
Instead, motion estimation is formulated as a continuous non-linear least-squares optimization problem:
$$\\min_{\\mathbf{p}} E(\\mathbf{p}) = \\frac{1}{2} \\sum_{i=1}^N r_i^2(\\mathbf{p}) = \\frac{1}{2} \\|\\mathbf{r}(\\mathbf{p})\\|^2$$
where the residual error vector $\\mathbf{r}(\\mathbf{p}) = [r_1, r_2, \\dots, r_N]^T$ represents brightness difference:
$$r_i(\\mathbf{p}) = I_{t+1}(f(\\mathbf{x}_i; \\mathbf{p})) - I_t(\\mathbf{x}_i)$$

---

### 2. Critical Evaluation of Optimization Algorithms

#### 1. Gradient Descent (Steepest Descent)
* **Update Step:**
  $$\\mathbf{p}^{(k+1)} = \\mathbf{p}^{(k)} - \\eta \\nabla E(\\mathbf{p}^{(k)}) = \\mathbf{p}^{(k)} - \\eta \\mathbf{J}^T \\mathbf{r}$$
  where $\\mathbf{J} = \\frac{\\partial \\mathbf{r}}{\\partial \\mathbf{p}}$ is the $N \\times P$ Jacobian matrix and $\\eta$ is the learning rate.
* **Convergence Behavior:**
  * **First-order convergence (Linear).**
  * Highly stable when far from the minimum.
  * **Severe Drawback:** Suffers from catastrophic slow convergence (zigzagging) in narrow error valleys where eigenvalues of the Hessian differ by orders of magnitude.

#### 2. Gauss-Newton Algorithm
* **Theoretical Basis:** Approximates the Hessian matrix $\\mathbf{H} = \\nabla^2 E(\\mathbf{p})$ by dropping second-order derivative terms:
  $$\\mathbf{H} \\approx \\mathbf{J}^T \\mathbf{J}$$
* **Update Step:**
  $$\\mathbf{p}^{(k+1)} = \\mathbf{p}^{(k)} - \\left( \\mathbf{J}^T \\mathbf{J} \\right)^{-1} \\mathbf{J}^T \\mathbf{r}$$
* **Convergence Behavior:**
  * **Second-order (Quadratic) convergence near the minimum.** Requires very few iterations (3 to 6).
  * **Severe Drawback:** If $\\mathbf{J}^T \\mathbf{J}$ is singular or ill-conditioned (e.g. in textureless image regions), the matrix inverse explodes, causing extreme oscillation and numerical **divergence**.

#### 3. The Levenberg-Marquardt (LM) Algorithm (Optimal Choice)
* **Formulation:** Introduces an adaptive damping factor $\\lambda \\ge 0$:
  $$\\Delta \\mathbf{p} = - \\left( \\mathbf{J}^T \\mathbf{J} + \\lambda \\, \\text{diag}(\\mathbf{J}^T \\mathbf{J}) \\right)^{-1} \\mathbf{J}^T \\mathbf{r}$$
* **Convergence Dynamics:**
  * If the update step reduces error $E(\\mathbf{p})$: The step is accepted, and $\\lambda$ is divided by 10 (shifting toward fast **Gauss-Newton quadratic convergence**).
  * If the update step increases error: The step is rejected, and $\\lambda$ is multiplied by 10 (shifting toward safe, guaranteed **Gradient Descent**).
* **Justification:** Combines the global robustness of Gradient Descent with the local quadratic convergence speed of Gauss-Newton.

---

### 3. Convergence Failure Modes & Robust Mitigations

#### 1. Trapping in Local Minima
* **Problem:** Image brightness surfaces are highly non-convex with numerous local ripples caused by image noise and repetitive textures.
* **Solution (Coarse-to-Fine Gaussian Pyramids):**
  1. Build a multi-level Gaussian pyramid of frames ($L_2 = 1/4$ size, $L_1 = 1/2$ size, $L_0 = \\text{Full size}$).
  2. Estimate coarse motion at Level 2 (where high-frequency ripples are smoothed away and displacements are small).
  3. Upsample and initialize Level 1 with Level 2 estimates, refining motion down to Level 0.

#### 2. Ill-Conditioned Image Gradients (Aperture Problem in Optimization)
* If an image block contains only horizontal edges, $I_x \\approx 0$. Then $\\mathbf{J}^T \\mathbf{J}$ has rank 1 and cannot be inverted.
* **Mitigation:** Levenberg-Marquardt's diagonal damping $\\lambda \\mathbf{I}$ guarantees that the matrix is strictly positive-definite and invertible under all conditions."""
    },
    {
        "id": "MID2-Q11",
        "mid": "Mid-II",
        "qno": 11,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K5",
        "marks": "10 Marks",
        "title": "Design transform-domain motion estimation algorithms and optimize their performance for video compression applications.",
        "punchline": "Transform-domain motion estimation utilizes Phase Correlation based on the Fourier Shift Theorem; cross-power spectrum inversion produces a sharp Dirac delta peak identifying global/block displacement with sub-pixel precision.",
        "mnemonic": "P-C-F-S: Phase Correlation, Cross-power spectrum, Fourier shift, Sub-pixel peak",
        "analogy": "Matching two transparent slides on an overhead projector: You slide them over each other until suddenly a bright beam of light flashes through the aligned pinholes, pinpointing exact displacement.",
        "diagram": """PHASE CORRELATION MOTION ESTIMATION PIPELINE:

Frame 1: f1(x, y) ────────► [ 2D-FFT ] ────────► F1(u, v)
                                                   │
                                                   ▼
Frame 2: f2(x, y) = f1(x-x0, y-y0) ──► [ 2D-FFT ] ──► F2(u, v)
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────┐
│ Normalized Cross-Power Spectrum R(u, v):               │
│               F1(u, v) · F2*(u, v)                     │
│    R(u, v) = ────────────────────── = e^-j2π(u·x0 + v·y0)
│              |F1(u, v) · F2*(u, v)|                    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
                  [ Inverse 2D-FFT ]
                           │
                           ▼
              Phase Correlation Surface r(x, y)
                           │
                           ▼
            δ(x - x0, y - y0) (Sharp Dirac Delta Peak at Displacement!)
                           │
                           ▼
       [ Sub-pixel Interpolation ──► (dx, dy) = (x0, y0) ]""",
        "content": """### 1. Conceptual Foundation: The Phase Correlation Method
Transform-domain motion estimation computes spatial displacements directly in the frequency domain without spatial block searching. It is mathematically rooted in the **Fourier Shift Property**:
* Let $f_1(x, y)$ be the reference frame and $f_2(x, y)$ be the translated frame shifted by displacement $(x_0, y_0)$:
  $$f_2(x, y) = f_1(x - x_0, y - y_0)$$
* Taking the 2D Continuous/Discrete Fourier Transform:
  $$F_2(u, v) = F_1(u, v) \\cdot e^{-j 2\\pi \\left( \\frac{u x_0}{M} + \\frac{v y_0}{N} \\right)}$$
* The translation is entirely encoded in the **phase difference**, while the magnitude spectrum remains identical ($|F_2(u, v)| = |F_1(u, v)|$).

---

### 2. Step-by-Step Transform-Domain Algorithm Design

#### Step 1: Compute 2D-FFT of Both Blocks / Frames
Compute $F_1(u, v) = \\text{FFT2}\\{f_1(x, y)\\}$ and $F_2(u, v) = \\text{FFT2}\\{f_2(x, y)\\}$.

#### Step 2: Compute the Normalized Cross-Power Spectrum ($R(u, v)$)
Multiply $F_1(u, v)$ by the complex conjugate of $F_2(u, v)$, and normalize by magnitude:
$$R(u, v) = \\frac{F_1(u, v) \\cdot F_2^*(u, v)}{|F_1(u, v) \\cdot F_2^*(u, v)|} = \\frac{|F_1(u, v)|^2 e^{j 2\\pi \\left( \\frac{u x_0}{M} + \\frac{v y_0}{N} \\right)}}{|F_1(u, v)|^2} = e^{j 2\\pi \\left( \\frac{u x_0}{M} + \\frac{v y_0}{N} \\right)}$$
* **Critical Advantage:** Normalizing by magnitude strips away all image content and illumination variations, leaving **pure phase information**.

#### Step 3: Compute Inverse 2D-FFT to Obtain the Correlation Surface
Taking the Inverse 2D-FFT of the phase exponential yields a spatial **Dirac Delta Function**:
$$r(x, y) = \\mathcal{F}^{-1}\\{R(u, v)\\} = \\delta(x + x_0, y + y_0)$$
* The correlation surface $r(x, y)$ is near zero everywhere, exhibiting a **sharp, prominent impulse spike** located precisely at $(-x_0, -y_0)$.

#### Step 4: Peak Detection and Sub-Pixel Refinement
Find the integer coordinates $(x^*, y^*)$ of the maximum peak:
$$(x_0, y_0) = \\arg\\max_{x, y} \\{ r(x, y) \\}$$
* **Sub-Pixel Optimization:** Fit a 2D paraboloid or sinc function across the $3 \\times 3$ neighborhood of the peak to achieve **quarter-pixel ($1/4$ px)** accuracy without requiring fractional spatial interpolation.

---

### 3. Optimizations for Video Compression Applications
1. **Global Motion Compensation (GMC):** In video sequences with panning/zooming cameras, Phase Correlation estimates global camera motion across entire frames in a single FFT pass, allowing the encoder to subtract camera motion globally.
2. **Robustness to Illumination Fluctuations:** Because the magnitude spectrum is completely discarded in the denominator normalization, Phase Correlation is **$100\\%$ immune to uniform lighting changes, contrast fading, and brightness flicker**.
3. **Hardware Acceleration via 2D-FFT ASICs:** Modern GPUs and video DSPs feature dedicated hardware FFT coprocessors, making transform-domain correlation faster than spatial full-search block matching."""
    },
    {
        "id": "MID2-Q12",
        "mid": "Mid-II",
        "qno": 12,
        "unit": "Unit-4",
        "co": "CO4",
        "bloom": "K6",
        "marks": "10 Marks",
        "title": "Develop a comprehensive framework for 3D motion and structure estimation integrating geometric and statistical models.",
        "punchline": "The 3D Structure from Motion (SfM) framework integrates epipolar geometry, Essential Matrix (E = [t]_x R), 8-Point SVD algorithm, RANSAC outlier rejection, and Bundle Adjustment to reconstruct 3D scene structure and camera trajectory.",
        "mnemonic": "E-F-8-R-B: Epipolar geometry, Fundamental/Essential matrix, 8-Point SVD, RANSAC, Bundle adjustment",
        "analogy": "Creating a 3D digital statue from smartphone photos: As you walk around the statue taking pictures, SfM tracks distinctive facial features, calculates where your camera was standing for each photo, and triangulates 3D points in space.",
        "diagram": """EPIPOLAR GEOMETRY & 3D STRUCTURE FROM MOTION (SfM) PIPELINE:

  Camera 1 (C1)                                           Camera 2 (C2)
  Center ── ── ── ── ── ── Baseline (t) ── ── ── ── ── ── Center
    │  \                                                /  │
    │    \  Ray 1                                  Ray 2   │
    │      \                                      /        │
    ▼        \                                  /          ▼
  [ Image 1 ]  \                              /        [ Image 2 ]
    Point p1 ───►\                          /◄─── Epipolar Line l2
                   \                      /
                     ▼                  ▼
                    [ 3D Scene Point P(X, Y, Z) ]

COMPLETE SfM PIPELINE:
  Multi-view Video ──► [ Feature Extraction (SIFT/ORB) ]
                             │
                             ▼
                       [ Feature Matching & RANSAC Outlier Removal ]
                             │
                             ▼
                       [ Essential Matrix E = [t]× R via 8-Point SVD ]
                             │
                             ▼
                       [ SVD Decomposition ──► Camera Pose (R, t) ]
                             │
                             ▼
                       [ Triangulation ──► Sparse 3D Point Cloud ]
                             │
                             ▼
                       [ Bundle Adjustment (Nonlinear Levenberg-Marquardt) ]
                             │
                             ▼
                [ Optimized 3D Structure & Camera Trajectory ]""",
        "content": """### 1. Architectural Overview of the 3D Estimation Framework
Recovering 3D scene structure (a 3D point cloud) and 3D camera trajectory (rotation $R$, translation $\\mathbf{t}$) from a 2D video sequence is known as **Structure from Motion (SfM)**. The framework synergistically unifies:
1. **Geometric Models:** Epipolar geometry, projection matrices, and multi-view projective constraints.
2. **Statistical Models:** RANSAC robust estimation and maximum likelihood Bundle Adjustment.

---

### 2. Geometric Foundation: Epipolar Geometry & The Essential Matrix

#### 1. Epipolar Geometry
Let a 3D point $\\mathbf{P} = [X, Y, Z]^T$ be observed by two calibrated camera poses with relative rotation $\\mathbf{R}$ and translation $\\mathbf{t}$.
* The 3D camera centers $\\mathbf{C}_1, \\mathbf{C}_2$ and point $\\mathbf{P}$ form the **Epipolar Plane**.
* The intersection of this plane with the image sensors defines the **Epipolar Lines**.
* The projection of camera center $\\mathbf{C}_1$ onto image 2 is the **Epipole** $\\mathbf{e}_2$.

#### 2. The Essential Matrix ($\\mathbf{E}$) and Fundamental Matrix ($\\mathbf{F}$)
* For calibrated normalized coordinates $\\mathbf{x}_1 = K_1^{-1} \\mathbf{p}_1$ and $\\mathbf{x}_2 = K_2^{-1} \\mathbf{p}_2$, the **Epipolar Coplanarity Constraint** is:
  $$\\mathbf{x}_2^T \\mathbf{E} \\mathbf{x}_1 = 0$$
  where $\\mathbf{E}$ is the **Essential Matrix** ($3 \\times 3$, Rank 2, 5 Degrees of Freedom):
  $$\\mathbf{E} = [\\mathbf{t}]_\\times \\mathbf{R} = \\begin{bmatrix} 0 & -t_z & t_y \\\\ t_z & 0 & -t_x \\\\ -t_y & t_x & 0 \\end{bmatrix} \\mathbf{R}$$
* For uncalibrated pixel coordinates, the **Fundamental Matrix** $\\mathbf{F} = K_2^{-T} \\mathbf{E} K_1^{-1}$ satisfies $\\mathbf{p}_2^T \\mathbf{F} \\mathbf{p}_1 = 0$.

---

### 3. Step-by-Step SfM Computational Framework

#### Stage 1: Feature Extraction & Correspondence
* Extract scale- and rotation-invariant feature keypoints (SIFT, ORB) across all video frames.
* Match feature descriptors between adjacent and wide-baseline frame pairs using $k$-d trees and Lowe's ratio test.

#### Stage 2: Statistical Outlier Rejection via RANSAC
* Real video correspondences contain $20-40\\%$ false matches (outliers from motion blur or repeating patterns) that destroy linear estimators.
* **RANSAC (Random Sample Consensus) Loop:**
  1. Randomly sample 8 minimal point correspondences.
  2. Compute candidate matrix $\\mathbf{E}$ via the 8-Point Algorithm.
  3. Count inliers satisfying epipolar distance $|\\mathbf{x}_2^T \\mathbf{E} \\mathbf{x}_1| < \\tau$.
  4. Repeat for $N$ iterations to find the matrix supported by the largest consensus inlier set.

#### Stage 3: Eight-Point Algorithm with SVD
Linear formulation of $\\mathbf{x}_2^T \\mathbf{E} \\mathbf{x}_1 = 0$:
$$\\mathbf{A} \\mathbf{e} = 0, \\quad \\mathbf{e} = [e_{11}, e_{12}, \\dots, e_{33}]^T$$
1. Compute Singular Value Decomposition (SVD): $\\mathbf{A} = \\mathbf{U} \\mathbf{D} \\mathbf{V}^T$. The solution $\\mathbf{e}$ is the singular vector corresponding to the smallest singular value (last column of $\\mathbf{V}$).
2. **Enforce Singularity Constraint:** A valid Essential Matrix must have two identical non-zero singular values and one zero singular value (Rank 2). Compute $\\mathbf{E} = \\mathbf{U} \\operatorname{diag}(\\sigma_1, \\sigma_2, \\sigma_3) \\mathbf{V}^T$, replace singular values with $(1, 1, 0)$, and reconstruct:
   $$\\mathbf{E}^* = \\mathbf{U} \\operatorname{diag}\\left(\\frac{\\sigma_1 + \\sigma_2}{2}, \\frac{\\sigma_1 + \\sigma_2}{2}, 0\\right) \\mathbf{V}^T$$

#### Stage 4: Pose Recovery (Decomposition of $\\mathbf{E}$)
* SVD decomposition of $\\mathbf{E}$ yields four possible $(R, \\mathbf{t})$ camera pose configurations.
* **Cheirality Check:** Triangulate a single test point; the unique correct pose is the one where the 3D point has positive depth ($Z > 0$) in front of both cameras.

#### Stage 5: 3D Triangulation
* For each inlier correspondence, find the 3D point $\\mathbf{P}$ that minimizes the distance between the two back-projected optical rays using linear least squares.

#### Stage 6: Global Bundle Adjustment (Nonlinear Refinement)
* Refine all 3D scene point coordinates $\\mathbf{P}_j$ and all camera poses $(R_i, \\mathbf{t}_i)$ simultaneously by minimizing the total 2D **re-projection error** using the Levenberg-Marquardt algorithm:
  $$\\min_{\\{R_i, \\mathbf{t}_i\\}, \\{\\mathbf{P}_j\\}} \\sum_{i=1}^M \\sum_{j=1}^N \\rho\\left( \\left\\| \\mathbf{p}_{ij} - \\pi(K_i, R_i, \\mathbf{t}_i, \\mathbf{P}_j) \\right\\|^2 \\right)$$
  where $\\pi(\\cdot)$ is the perspective camera projection function and $\\rho(\\cdot)$ is a robust Huber loss function that suppresses remaining outliers."""
    }
]
