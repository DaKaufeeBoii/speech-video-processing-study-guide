# -*- coding: utf-8 -*-
"""
Unit 5: Video Segmentation, Change Detection, Object Tracking & Performance Evaluation
Questions: Mid-II Q13 to Q20
Regulation: KGR23 | Academic Year: 2026-27 | Course Code: KG23ACM408 | Dr. Sandeep Kumar M
Written in student-friendly, zero-jargon peer-tutor style with complete mathematical rigor.
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
        "punchline": "Region methods group pixels that look alike (filling areas inside lines); Boundary methods trace sharp color changes (drawing outlines); practical video systems combine both so Canny outlines keep region growing from spilling over.",
        "mnemonic": "Region = Grouping Homogeneity; Boundary = Detecting Discontinuity.",
        "analogy": "Coloring a coloring book: region-based segmentation fills entire shapes with crayon wax based on color similarity; boundary-based segmentation takes a black sharpie and traces only the sharp ink outlines.",
        "diagram": """1. REGION-BASED (Homogeneity):          2. BOUNDARY-BASED (Discontinuity):
   Groups similar neighboring pixels        Detects sharp gradient edges: ∇I
   ┌──────────────────────┐                 ┌──────────────────────┐
   │  Region R₁ (Green)   │                 │   /────────────────\\ │
   │  • Seed  ──► Grows   │                 │  /  Canny / Sobel   \\│
   │                      │                 │ │   Edge Contours    ││
   │  Region R₂ (Blue)    │                 │  \\                  /│
   └──────────────────────┘                 └──────────────────────┘
   Techniques: Growing, Split & Merge       Techniques: Sobel, Canny, Laplacian

VIDEO TRACKING SUITABILITY:
• Region-based provides solid foreground object masks (great for tracking car area).
• Boundary-based detects moving silhouettes quickly, but edges can break under noise.
• Modern video AI fuses both: Canny edges form the boundary walls for Region growing!""",
        "content": """### 1. The Big Picture (What is Image Segmentation?)
**Image segmentation** means slicing a digital photo into meaningful objects (like separating a car, a pedestrian, and the road from each other) instead of looking at raw unorganized pixels.
In computer vision, there are two fundamentally opposing ways to do this:
1. **Region-Based (Similarity):** Look for pixels that share the same color or texture and group them together.
2. **Boundary-Based (Discontinuity):** Look for sharp brightness jumps (edges) and draw an outline around the object.

---

### 2. Breakdown of the Two Approaches (Unit 5 Notes)

#### A. Region-Based Segmentation (Grouping Homogeneous Pixels)
* **How it works:** Starts with a similarity rule (e.g., all pixels within $\\pm 10$ intensity belong to the same region).
* **Core Techniques:**
  1. **Region Growing:** Starts with a "seed pixel" (e.g., a green pixel on a leaf) and expands outward to swallow adjacent pixels if their color matches.
  2. **Split & Merge (Quadtree):** Chops an image into 4 quadrants. If a quadrant has mixed colors, it splits again into 4 sub-blocks. Adjacent uniform blocks are then merged back together.
* **Pros & Cons:** Guarantees solid, closed regions (great for measuring object surface area), but can accidentally "bleed" into the background if colors are similar.

#### B. Boundary-Based Segmentation (Detecting Sharp Edges)
* **How it works:** Calculates spatial derivatives (gradients $\\nabla I$) to find where light changes suddenly.
* **Core Techniques:**
  1. **Sobel Operator:** Uses $3 \\times 3$ derivative masks ($G_x, G_y$) to detect horizontal and vertical edges.
  2. **Canny Edge Detector:** The gold standard! Runs Gaussian smoothing $\\rightarrow$ gradient calculation $\\rightarrow$ Non-Maximum Suppression (thins edges to 1 pixel) $\\rightarrow$ Hysteresis thresholding (bridges broken edges).
  3. **Laplacian Operator:** Finds zero-crossings of the second derivative $\\nabla^2 I$.
* **Pros & Cons:** Blazing fast on GPUs, but noise creates fake edge fragments, and edges often have gaps that fail to form a closed object.

---

### 3. Cheat Sheet Comparison Table (Unit 5 Notes)
| Comparison Factor | Region-Based Segmentation | Boundary-Based Segmentation |
| :--- | :--- | :--- |
| **Fundamental Idea** | Groups pixels based on **similarity / homogeneity** | Locates objects based on **gradient discontinuity / edges** |
| **Input Clues** | Color, intensity, and texture statistics | First and second spatial derivatives ($\\nabla I, \\nabla^2 I$) |
| **Output Shape** | Solid, connected 2D pixel masks | Thin edge contours and boundary lines |
| **Noise Tolerance** | Robust (averaging smooths noise) | **Fragile** (derivative operators amplify camera grain) |
| **Standard Algorithms** | Region Growing, Split-and-Merge, Watershed | Sobel, Prewitt, Canny Edge Detector, Laplacian |

---

### 4. Which is Better for Video Processing? (The Verdict)
- **Region-based** is ideal for **background subtraction**: it produces solid, filled-in silhouettes of moving vehicles needed for tracking size and centroid.
- **Boundary-based** is ideal for **rigid object contour tracking**: fast and lightweight for detecting road signs and car silhouettes.
- **The Modern Hybrid Winner:** Real-time surveillance cameras fuse both! They use Canny edge detectors to outline objects, and use those edges as impenetrable walls to stop region growing from leaking into the background."""
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
        "punchline": "Change detection spots moving objects by subtracting consecutive frames (D = |I_t - I_{t-1}|) or subtracting a background model (D = |I_t - B|); it's the 24/7 motion sensor that tells security cameras when to record.",
        "mnemonic": "F-B-T-O: Frame Differencing, Background Subtraction, Thresholding, Optical Flow.",
        "analogy": "Like a security guard watching an empty bank lobby at 3:00 AM: instead of burning his eyes staring at stationary marble pillars all night, the guard's motion alarm triggers only when someone actually walks through the front door (pixel intensity change).",
        "diagram": """1. FRAME DIFFERENCING:
   Frame t ──► [ - ] ◄── Frame t-1 ──► D(x, y) = |I_t - I_{t-1}| (Fast, but creates hollow interior holes!)
                  │
2. BACKGROUND SUBTRACTION:
   Frame t ──► [ - ] ◄── Background B(x, y) ──► D(x, y) = |I_t - B| (Solid moving silhouettes!)
                  │
                  ▼
3. THRESHOLDING (Binarization):
   Binary Motion Mask: M(x, y) = 1 if D(x, y) > T else 0 (T = noise threshold)
                  │
                  ▼
4. SURVEILLANCE ACTION:
   • Parking Lot: Logs arrival timestamp when car enters empty stall
   • Perimeter Security: Sounds alarm when intruder crosses fence line""",
        "content": """### 1. The Big Picture (What is Change Detection?)
In video surveillance, cameras record for thousands of hours. Storing empty hallways or parking lots wastes petabytes of hard drives. 
**Change detection** is the computer vision technique that compares incoming video frames to spot whenever an object moves, enters, or alters the scene.

---

### 2. The 4 Core Principles of Change Detection (Unit 5 Notes)

#### A. Frame Differencing (Adjacent Frame Comparison)
* **The Math:** Subtracts the previous frame from the current frame:
  $$D(x, y) = |I_t(x, y) - I_{t-1}(x, y)|$$
* **Pros & Cons:** Blazing fast and instantly adapts to gradual daytime sunlight changes. But it suffers from the **aperture hole problem**: uniformly colored moving objects (like a white truck) only show changes along their front and back bumpers, leaving a hollow ghost hole in the middle!

#### B. Background Subtraction (Reference Model Comparison)
* **The Math:** Compares the current frame against a running background model $B(x, y)$:
  $$D(x, y) = |I_t(x, y) - B(x, y)|$$
  where the background is updated over time: $B_t = (1 - \\alpha) B_{t-1} + \\alpha I_t$.
* **Pros & Cons:** Captures the complete, solid silhouette of the moving person or car! But it can get confused if clouds cast large sudden shadows.

#### C. Thresholding (Binarizing Motion)
* **The Math:** Turns the difference map into a clean black-and-white binary mask:
  $$M(x, y) = \\begin{cases} 1 & \\text{if } D(x, y) > T \\quad (\\text{Motion Detected!}) \\\\ 0 & \\text{if } D(x, y) \\le T \\quad (\\text{Static Background}) \\end{cases}$$
  where $T$ is an experimentally tuned noise threshold.

#### D. Optical Flow
* **The Math:** Solves $I_x u + I_y v + I_t = 0$ to get directional velocity vectors $(u, v)$ for every pixel.
* **Pros:** Tells you not just *that* something moved, but *how fast* and in *which direction* it is running.

---

### 3. Why It's Crucial in Video Surveillance (Exam Points)
1. **Intrusion Alarms:** Immediately sounds an alert if a pedestrian crosses a boundary after business hours.
2. **Parking Lot Monitoring (Classic Lecture Example):**
   - *Frame 1:* Parking stall is empty (stored in background model $B$).
   - *Frame 2:* A car drives into the stall.
   - *Frame 3:* Background subtraction flags a huge difference ($D > T$). The system logs the car's arrival and marks the spot as occupied.
3. **Smart Video Storage:** CCTV cameras record at low 1 fps when nothing is moving, and instantly jump to full 60 fps recording when change detection triggers."""
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
        "punchline": "Checking SAD against 100: Regions A (120 > 100) and C (200 > 100) have motion; Region B (45 < 100) is static; Region C has the most dominant motion (max SAD = 200).",
        "mnemonic": "Compare SAD to Threshold 100: A (Yes), B (No), C (Yes). Dominant = max(120, 45, 200) = C.",
        "analogy": "Like three sound sensors in a library set to trigger alarms at 100 decibels: Room A is 120 dB (alarm!), Room B is 45 dB (quiet studying), and Room C is 200 dB (a rock concert!). Rooms A and C triggered the alarm, and Room C is by far the loudest source.",
        "diagram": """SAD Frame Difference ▲
                 200 │                                          █ Region C = 200
                     │                                          █ (DOMINANT MOTION!)
                 150 │                                          █
                 120 │             █ Region A = 120             █
                     │             █ (Motion Detected!)         █
     ════════════100 ╞═════════════╪════════════════════════════╪════════════════════►
                     │  Threshold  │                            │   THRESHOLD = 100
                  50 │             │        █ Region B = 45     │
                     │             │        █ (NO MOTION)       │
                   0 └─────────────┴────────┴───────────────────┴────────────────►
                                Region A  Region B            Region C

FINAL VERDICT:
• Regions WITH Motion   : Region A (120 > 100) and Region C (200 > 100)
• Regions WITHOUT Motion: Region B (45 < 100)
• Dominant Motion Region: Region C (Highest SAD = 200)""",
        "content": """### 1. The Given Problem Data (Unit 5 Notes)
In a video sequence, frame differences are calculated using the **Sum of Absolute Differences (SAD)**:
* **Region A:** $\\text{SAD}_A = 120$
* **Region B:** $\\text{SAD}_B = 45$
* **Region C:** $\\text{SAD}_C = 200$
* **Motion Threshold:** $T = 100$

---

### 2. The Decision Rule
For any region:
$$\\text{If } \\text{SAD} > 100 \\implies \\mathbf{Motion\\ Detected}$$
$$\\text{If } \\text{SAD} \\le 100 \\implies \\mathbf{No\\ Significant\\ Motion\\ (Static\\ Background)}$$

---

### 3. Step-by-Step Numerical Evaluation

#### 1. Identify Regions Containing Motion:
* **Region A:** $\\text{SAD}_A = 120 > 100 \\implies$ **Motion Detected!**
* **Region B:** $\\text{SAD}_B = 45 < 100 \\implies$ No Motion.
* **Region C:** $\\text{SAD}_C = 200 > 100 \\implies$ **Motion Detected!**
* **Answer to Part 1:** **Regions A and C** contain significant motion.

#### 2. Identify Regions Without Motion:
* **Region B:** $\\text{SAD}_B = 45 < 100 \\implies$ **No Motion Detected.**
* **Answer to Part 2:** **Region B** is the region without motion.

#### 3. Determine the Dominant Motion Region:
The dominant motion region is the one with the maximum frame difference:
$$\\text{Dominant Motion} = \\max(\\text{SAD}_A, \\text{SAD}_B, \\text{SAD}_C) = \\max(120, 45, 200) = \\mathbf{200}$$
* **Answer to Part 3:** **Region C** has the most dominant motion because it has the highest SAD value ($200$).

---

### 4. Summary Table for Full Exam Marks (Unit 5 Notes)
| Region | Measured SAD | Comparison | Status | Dominance Rank |
| :---: | :---: | :---: | :---: | :---: |
| **Region A** | $120$ | $120 > 100$ | **Motion Detected** | 2nd Place |
| **Region B** | $45$ | $45 < 100$ | **No Motion (Static)** | 3rd Place |
| **Region C** | $200$ | $200 > 100$ | **Motion Detected** | **1st Place (Dominant Winner!)** |"""
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
        "punchline": "Motion tracking follows objects across frames using Optical Flow, Kalman, or Particle filters; trajectory calculation records the ordered sequence of centroid coordinates T = {P1, P2, P3, P4} to map the object's path.",
        "mnemonic": "Detect -> Track -> Calculate MV -> Plot Trajectory T = {(x_t, y_t)}.",
        "analogy": "Like looking at footprints in snow: tracking identifies which boots made each footprint; trajectory calculation connects the footprints with a GPS line to prove where the hiker walked, how fast they ran, and what direction they headed.",
        "diagram": """SPATIAL TRAJECTORY PLOT ACROSS 4 FRAMES:
Y-axis ▲
    35 │                                              • F₄ (25, 35)
       │                                            /
    30 │                               • F₃ (20, 30)
       │                             /   MV = (5, 5)
    25 │                  • F₂ (15, 25)
       │                /   MV = (5, 5)
    20 │   • F₁ (10, 20)
       │     MV = (5, 5)
       └───┴──────────────┴──────────────┴──────────────┴──────────────► X-axis
           10             15             20             25

TRAJECTORY SET:
T = { (10, 20), (15, 25), (20, 30), (25, 35) }
Uniform Motion Vector: MV = (5, 5) pixels/frame
Heading: 45° diagonal motion in positive X and Y directions!""",
        "content": """### 1. The Big Picture (What is Motion Tracking?)
**Motion tracking** means locating a moving object (like a car or person) and keeping continuous lock on it across every video frame.
**Trajectory estimation** connects the object's recorded $(x, y)$ center points over time to map its exact path, speed, and heading.

---

### 2. Major Motion Tracking Algorithms (Unit 5 Notes)
* **Optical Flow Tracking:** Tracks sharp corner features frame-to-frame based on pixel gradients.
* **Kalman Filter Tracking:** Predicts where the object will move next based on its speed, smoothing out noisy camera jitter.
* **Particle Filter Tracking:** Uses hundreds of random virtual hypotheses (particles) to track objects undergoing erratic turns or temporary occlusions.

---

### 3. Step-by-Step Trajectory Calculation (Worked Lecture Problem)
Consider a moving vehicle tracked across **4 consecutive video frames**:
* Frame $F_1$: Centroid at $(x_1, y_1) = (10, 20)$
* Frame $F_2$: Centroid at $(x_2, y_2) = (15, 25)$
* Frame $F_3$: Centroid at $(x_3, y_3) = (20, 30)$
* Frame $F_4$: Centroid at $(x_4, y_4) = (25, 35)$

#### Step 1: Calculate Inter-Frame Motion Vectors (Displacement)
The motion vector between frame $k$ and $k+1$ is $\\mathbf{MV}_k = (x_{k+1} - x_k, \\ y_{k+1} - y_k)$:
* **Displacement from $F_1$ to $F_2$:**
  $$\\mathbf{MV}_1 = (15 - 10, \\ 25 - 20) = \\mathbf{(5, \\ 5)}$$
* **Displacement from $F_2$ to $F_3$:**
  $$\\mathbf{MV}_2 = (20 - 15, \\ 30 - 25) = \\mathbf{(5, \\ 5)}$$
* **Displacement from $F_3$ to $F_4$:**
  $$\\mathbf{MV}_3 = (25 - 20, \\ 35 - 30) = \\mathbf{(5, \\ 5)}$$

#### Step 2: Formulate the Trajectory Set $\\mathcal{T}$
The complete trajectory $\\mathcal{T}$ is the ordered chronological sequence of positions:
$$\\mathcal{T} = \\left\\{ (10, 20), \\ (15, 25), \\ (20, 30), \\ (25, 35) \\right\\}$$

#### Step 3: Interpret Speed and Direction
* **Velocity:** Because $\\mathbf{MV} = (5, 5)$ is constant, the vehicle travels with a uniform velocity of $5\\text{ pixels/frame}$ horizontally and $5\\text{ pixels/frame}$ vertically.
* **Speed (Distance per frame):**
  $$v = \\sqrt{5^2 + 5^2} = \\sqrt{50} \\approx \\mathbf{7.07\\text{ pixels/frame}}$$
* **Heading Direction:**
  $$\\theta = \\arctan\\left(\\frac{5}{5}\\right) = \\arctan(1) = \\mathbf{45^\\circ}\\text{ diagonally in positive X and Y}$$"""
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
        "punchline": "Matting calculates soft transparency alpha values (I = αF + (1-α)B, α ∈ [0,1]) to extract hair strands and glass reflections without jagged borders; deep learning and optical flow video matting maintain flicker-free temporal consistency.",
        "mnemonic": "Matting Equation: I = αF + (1-α)B. Types: Chroma, Bayesian, Closed-Form, Deep Learning.",
        "analogy": "Image segmentation is like cutting out an actor from a magazine with scissors (hard jagged paper edge, chops off hair strands); image matting is like creating a photographic transparency slide where individual hairs and see-through sunglasses blend seamlessly onto any background.",
        "diagram": """COMPOSITING EQUATION:
  I(x, y) = α(x, y) · F(x, y) + [ 1 - α(x, y) ] · B(x, y)
  • α = 1.0  ──► 100% Solid Foreground (Actor's body)
  • α = 0.0  ──► 100% Background (Studio wall)
  • 0 < α < 1──► Semi-transparent transition (Flyaway hair, fur, glass, water)

MATTING TECHNIQUES COMPARED:
┌──────────────────────────────────┬──────────────────────────────────────────┐
│ Image Matting                    │ Video Matting (Temporal Extension)       │
├──────────────────────────────────┼──────────────────────────────────────────┤
│ • Chroma Keying (Green Screen)   │ • Background Subtraction Matting         │
│ • Bayesian Matting (Probabilistic)│ • Optical Flow Matting (Alpha warped)   │
│ • Closed-Form Matting (Laplacian)│ • Deep Learning Video Matting (Attention)│
└──────────────────────────────────┴──────────────────────────────────────────┘

EVALUATION METRICS:
SAD = Σ |α - α*|  │  MSE = (1/N) Σ (α - α*)²  │  Gradient Error  │  Temporal Consistency""",
        "content": """### 1. The Big Picture (Segmentation vs Matting)
Standard image segmentation is binary: every pixel is either 1 (foreground) or 0 (background). This looks terrible on fuzzy edges (hair, animal fur, transparent water, motion blur).
**Matting** is soft-segmentation: it calculates a fractional transparency value **$\\alpha \\in [0, 1]$** for every single pixel.

---

### 2. The Fundamental Matting Equation (Unit 5 Notes)
An observed pixel color $\\mathbf{I}(x, y)$ is modeled as a blend of true foreground $\\mathbf{F}$ and background $\\mathbf{B}$:
$$\\mathbf{I}(x, y) = \\alpha(x, y) \\mathbf{F}(x, y) + [1 - \\alpha(x, y)] \\mathbf{B}(x, y)$$
where:
* $\\alpha = 1.0$: Pure solid foreground (actor's jacket).
* $\\alpha = 0.0$: Pure background (studio wall).
* $0 < \\alpha < 1.0$: Semi-transparent transition (flying hair strands, smoke, glass).

#### The 3 vs 7 Dilemma (Why Matting is Hard):
At each pixel, we have **3 known values** $(R, G, B)$ but **7 unknown variables** (3 foreground colors, 3 background colors, and $\\alpha$). It is mathematically impossible to solve without extra clues!
We give algorithms extra clues using a **Trimap** (dividing the image into Known Foreground, Known Background, and an Unknown fuzzy boundary band).

---

### 3. Comparing Image Matting Techniques (Unit 5 Notes)
* **Chroma Keying (Green Screen):** Uses a solid green/blue backdrop. Fast and real-time for live TV, but fails if the actor wears green clothes or green light reflects onto their skin (color spill).
* **Bayesian Matting:** Uses Gaussian probability distributions to guess foreground and background colors in local windows. High accuracy for hair, but slow.
* **Closed-Form Matting (Levin Laplacian):** Assumes local color linearity and derives the **Matting Laplacian Matrix $\\mathbf{L}$** to solve for alpha in a clean quadratic equation. Beautiful for fine structures.
* **Deep Learning Matting (MODNet / Deep Image Matting):** Uses CNN encoder-decoders to predict alpha mattes automatically **without needing any trimaps**!

---

### 4. Video Matting & Temporal Consistency
In video matting, extracting each frame independently causes ugly flickering.
To keep alpha mattes smooth across time:
1. **Optical Flow Video Matting:** Warps alpha mattes along motion vectors $(u, v)$ from frame to frame.
2. **Deep Learning with Temporal Attention:** Uses ConvLSTM and temporal attention layers to ensure hair doesn't flash or jitter between frames.

---

### 5. Cheat Sheet Comparison Table (Unit 5 Notes)
| Technique | Accuracy on Hair | Computational Speed | Needs User Input? | Major Limitation |
| :--- | :--- | :--- | :--- | :--- |
| **Chroma Key** | Good | **Real-time (Fastest)** | Needs green screen | Screen spill & color reflection |
| **Bayesian Matting** | High | Slow | Needs 3-zone Trimap | Computationally heavy |
| **Closed-Form** | High | Medium | Needs Trimap/Scribble | Struggles on textured backgrounds |
| **Deep Learning** | **Highest** | Fast on GPU | **Trimap-Free!** | Requires large training datasets |

---

### 6. Quantitative Evaluation Metrics
* **Sum of Absolute Differences (SAD):** $\\text{SAD} = \\sum |\\alpha - \\alpha^*|$ (Lower is better).
* **Mean Squared Error (MSE):** $\\text{MSE} = \\frac{1}{N} \\sum (\\alpha - \\alpha^*)^2$.
* **Gradient Error:** Measures differences in edge sharpness (keeps hair crisp)."""
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
        "punchline": "Part A: Sum = 0.2 + 0.3 + 0.1 + 0.4 = 1.0 (already normalized!); Particle 4 is most likely at 40% (0.4), giving multi-hypothesis safety against occlusion. Part B: Updated position is x̂ = 50 + 0.6(60 - 50) = 56; gain of 0.6 balances 60% measurement trust against 40% predicted model trust.",
        "mnemonic": "Part A: Sum=1.0 (Norm), Max=P4 (40%). Part B: x̂ = x⁻ + K(z - x⁻) = 50 + 0.6(10) = 56.",
        "analogy": "Part A: Four search dogs hunting a fugitive; Dog 4 smells the strongest scent (40% confidence), but keeping all 4 dogs active prevents getting tricked if the fugitive doubles back. Part B: You predict a train is at mile 50, GPS says mile 60; with 60% GPS trust (K=0.6), you conclude the train is at mile 56.",
        "diagram": """PART A: PARTICLE FILTER WEIGHTS
  Particles:    P₁       P₂       P₃       P₄
  Weights  :   [0.2,    0.3,     0.1,     0.4]
  Sum Check:   0.2 + 0.3 + 0.1 + 0.4 = 1.00  ==► PERFECTLY NORMALIZED!
  Most Likely: Particle 4 (Highest probability: 0.4 or 40%)

PART B: KALMAN FILTER STATE UPDATE
  State Line:
  0                 x̂⁻ = 50        x̂ = 56              z = 60
  |────────────────────•──────────────•───────────────────•──────────────────► Position
                    Predicted      UPDATED             Measurement
                    Position       STATE               (GPS sensor)
                       │              ▲                   │
                       └──────────────┴───────────────────┘
                          Innovation / Error = (60 - 50) = 10
                          Correction = K · Error = 0.6 · 10 = +6
                          Updated State x̂ = 50 + 6 = 56""",
        "content": """### PART A: Particle Filter Weight Normalization & Robustness (Unit 5 Notes)

#### 1. Given Data:
Particle weights: $\\mathbf{W} = [0.2, \\ 0.3, \\ 0.1, \\ 0.4]$

#### 2. Task 1: Check and Normalize the Weights
To be valid probabilities, the sum of all particle weights must equal $1.0$:
$$\\sum_{i=1}^4 W_i = 0.2 + 0.3 + 0.1 + 0.4 = \\mathbf{1.00}$$

Compute normalized weights ($W'_i = \\frac{W_i}{\\sum W_i}$):
* $W'_1 = \\frac{0.2}{1.0} = \\mathbf{0.2}$
* $W'_2 = \\frac{0.3}{1.0} = \\mathbf{0.3}$
* $W'_3 = \\frac{0.1}{1.0} = \\mathbf{0.1}$
* $W'_4 = \\frac{0.4}{1.0} = \\mathbf{0.4}$
* **Verdict:** The weights are **already perfectly normalized**!

#### 3. Task 2: Identify the Most Likely Particle
The most likely particle is the one with the maximum weight:
$$i^* = \\arg\\max(0.2, 0.3, 0.1, 0.4) = \\mathbf{0.4} \\implies \\mathbf{Particle\\ 4}$$
* **Result:** **Particle 4** is the most likely state, holding **$40\\%$ ($0.4$) probability**.

#### 4. Task 3: Why This Choice Improves Robustness
Particle filtering is robust against uncertainty because:
1. **Multi-Hypothesis Tracking:** It doesn't put all its eggs in one basket. It tracks multiple candidate positions at once.
2. **Resilience to Occlusion:** If an object walks behind a pillar and the top particle loses tracking, surviving particles in nearby spots keep lock on the target.
3. **Non-Gaussian Dynamics:** Handles wild direction changes that crash standard Kalman filters.

---

### PART B: State Update Using Kalman Filter (Unit 5 Notes)

#### 1. Given Parameters:
* Predicted state estimate ($\\hat{x}^-$): $50$
* New measurement observation ($z$): $60$
* Kalman Gain ($K$): $0.6$

#### 2. Task 1: Compute the Updated State ($\\hat{x}$)
The Kalman filter state update equation is:
$$\\hat{x} = \\hat{x}^- + K \\left( z - \\hat{x}^- \\right)$$

* **Step 1: Calculate measurement error (Innovation):**
  $$\\text{Innovation} = z - \\hat{x}^- = 60 - 50 = 10$$
* **Step 2: Scale by Kalman Gain:**
  $$\\text{Correction} = K \\times \\text{Innovation} = 0.6 \\times 10 = 6$$
* **Step 3: Calculate updated state:**
  $$\\hat{x} = 50 + 6 = \\mathbf{56}$$

#### 3. Task 2: Technical Interpretation of Kalman Gain Influence
The formula can be rewritten as a weighted average:
$$\\hat{x} = (1 - K) \\hat{x}^- + K z = (1 - 0.6)(50) + 0.6(60) = 0.4(50) + 0.6(60) = 20 + 36 = \\mathbf{56}$$
* **Trust Allocation:** Because $K = 0.6$, the filter places **$60\\%$ trust in the new sensor measurement $z$** and **$40\\%$ trust in its internal physics prediction $\\hat{x}^-$**.
* **Motion Correction:** The filter corrects the initial prediction of $50$ by moving $6$ units towards the measured $60$, striking a perfect balance between model inertia and sensor responsiveness!"""
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
        "punchline": "A real-time tracking framework combines Change Detection, Background Subtraction, Morphology, Optical Flow, and Kalman Filtering across 9 stages; motion analysis predicts trajectories through blind spots and stops ID-swaps when objects cross paths.",
        "mnemonic": "A-D-B-T-M-O-K-T-T: Acquisition, Differencing, Background subtraction, Thresholding, Morphology, Optical flow, Kalman, Tracking, Trajectory.",
        "analogy": "Like an automated airport radar system: it detects incoming echoes (change detection), filters out ground clutter (morphological background subtraction), measures airplane heading and velocity (optical flow), and predicts future flight paths even when a plane flies through thick storm clouds (Kalman filter tracking).",
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
 [ 8. Trajectory Output ]──► Continuous vehicle path & speed analytics displayed!""",
        "content": """### 1. The Big Picture (Building a Real-Time Tracking Pipeline)
Tracking moving cars and pedestrians in real time requires combining low-level pixel math with high-level kinematic prediction so the camera doesn't lose track when objects walk behind trees or pass each other.

---

### 2. The 9 Integrated Stages of the Framework (Unit 5 Notes)

| Stage | Module Name | Algorithm / Technique | Practical Role in Pipeline |
| :---: | :--- | :--- | :--- |
| **1** | **Frame Ingestion** | Video capture (30 fps) | Ingests video stream and buffers adjacent frames |
| **2** | **Change Detection** | 2-Frame Differencing | Rapidly flags candidate moving areas ($|F_t - F_{t-1}|$) |
| **3** | **Background Subtraction**| Adaptive GMM / Running Average | Extracts complete foreground silhouettes from background |
| **4** | **Binarization** | Adaptive Thresholding | Converts difference maps into binary masks $M(x, y)$ |
| **5** | **Morphological Filtering**| Opening and Closing | Removes salt-and-pepper noise and seals interior holes |
| **6** | **Motion Estimation** | Dense Optical Flow | Calculates velocity vectors $(u, v)$ for each detected blob |
| **7** | **State Prediction** | Kalman Filter | Predicts next centroid position $\\hat{\\mathbf{x}}_k^- = \\mathbf{A} \\hat{\\mathbf{x}}_{k-1}$ |
| **8** | **Data Association** | Hungarian Algorithm | Matches newly detected blobs with existing active tracks |
| **9** | **Trajectory Output** | Coordinate Logging | Displays smooth paths $\\mathcal{T} = \\{(x_t, y_t)\\}$ and speeds |

---

### 3. How Motion Analysis Drastically Improves Tracking Accuracy
If you track objects using only visual appearance (color, bounding box), the tracker fails constantly. Adding **kinematic motion analysis (Optical Flow + Kalman Filtering)** transforms performance:
1. **Surviving Blind Spots & Occlusions:**
   When a car drives under an overhead highway bridge, it disappears from camera vision ($M(x, y) = 0$). The Kalman filter uses stored velocity vectors to **blindly coast the trajectory through the blind spot**, instantly re-locking onto the car the moment it emerges!
2. **Preventing ID Swaps When Objects Cross:**
   When two pedestrians walking in opposite directions pass each other, appearance trackers get confused and swap IDs. Motion analysis knows Pedestrian A has velocity $+u$ and Pedestrian B has $-u$, preventing ID swaps with $100\\%$ certainty!
3. **Filtering Out Sudden Sun/Headlight Glare:**
   Headlight flashes create large brightness changes ($D > T$), but optical flow checks if the pixels have coherent physical movement. Static flashes are instantly rejected as false alarms.
4. **Smoothing Jitter:**
   Raw bounding boxes bounce around due to pixel quantization; the Kalman filter smooths the path into a clean, professional trajectory line.

---

### 4. Real-World Traffic Surveillance Example (Unit 5 Notes)
In highway CCTV monitoring:
* Step 1: Capture traffic video.
* Step 2: Background subtraction isolates each vehicle.
* Step 3: Morphological closing forms a solid car outline.
* Step 4: Optical flow computes speed in km/h.
* Step 5: Kalman filtering predicts future position to detect lane weavers.
* Result: Automated red-light violation tickets and traffic congestion warnings in real time!"""
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
        "punchline": "The evaluation model compares AI predictions against ground truth using a Confusion Matrix; IoU measures spatial overlap, Precision measures purity (no false alarms), Recall measures completeness (no misses), and F1 balances both.",
        "mnemonic": "I-P-R-F: IoU = Overlap/Union, Precision = TP/(TP+FP), Recall = TP/(TP+FN), F1 = 2PR/(P+R).",
        "analogy": "Grading a student's exam: Precision is how many of your written answers were actually correct (did you write wrong guesses?); Recall is how many of all possible questions you answered (did you skip questions?); F1 is your overall balanced GPA; IoU is how closely your drawing overlapped with the teacher's grading stencil.",
        "diagram": """1. INTERSECTION OVER UNION (IoU):
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

WORKED NUMERICAL SCORES:
• Precision = 80 / (80 + 20) = 80.0%  │  Recall = 80 / (80 + 20) = 80.0%
• F1-Score  = 2(0.8)(0.8)/(0.8 + 0.8) = 80.0%
• IoU       = 80 / (80 + 20 + 20) = 80 / 120 = 66.7% (Exceeds 50% threshold!)""",
        "content": """### 1. The Big Picture (How We Grade Video AI)
Before deploying a self-driving car or video surveillance AI, we must prove mathematically how accurate it is.
A **performance evaluation model** tests the AI's predicted bounding boxes and masks against human-verified **ground-truth references**.

---

### 2. The 4 Fundamental Evaluation Metrics (Unit 5 Notes)

#### A. The Confusion Matrix
* **True Positive ($TP$):** AI correctly detected foreground pixels.
* **False Positive ($FP$):** AI hallucinated foreground where there was only background (False Alarm).
* **False Negative ($FN$):** Real foreground object that the AI missed completely (Missed Detection).
* **True Negative ($TN$):** Background pixels correctly left alone.

#### B. Intersection over Union (IoU / Jaccard Index)
Measures the percentage of spatial overlap between predicted region $A$ and ground truth $B$:
$$\\text{IoU} = \\frac{|A \\cap B|}{|A \\cup B|} = \\frac{TP}{TP + FP + FN}$$
*(In computer vision benchmarks, $\\text{IoU} \\ge 0.50$ ($50\\%$) is considered a successful detection).*

#### C. Precision (Purity / Correctness)
What fraction of the AI's detections were actually real?
$$\\text{Precision} = \\frac{TP}{TP + FP}$$

#### D. Recall (Completeness / Sensitivity)
What fraction of all real objects in the scene did the AI successfully catch?
$$\\text{Recall} = \\frac{TP}{TP + FN}$$

#### E. F1-Score (The Balanced Grade)
The harmonic mean of Precision and Recall:
$$F_1 = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\frac{2 TP}{2 TP + FP + FN}$$

---

### 3. Step-by-Step Worked Numerical Problem (Unit 5 Notes)
Consider a video segmentation system tested on a benchmark frame with the following results:
* $TP = 80\\text{ pixels}$
* $FP = 20\\text{ pixels}$
* $FN = 20\\text{ pixels}$
* $TN = 80\\text{ pixels}$

#### 1. Precision:
$$\\text{Precision} = \\frac{TP}{TP + FP} = \\frac{80}{80 + 20} = \\frac{80}{100} = \\mathbf{0.80 = 80.0\\%}$$

#### 2. Recall:
$$\\text{Recall} = \\frac{TP}{TP + FN} = \\frac{80}{80 + 20} = \\frac{80}{100} = \\mathbf{0.80 = 80.0\\%}$$

#### 3. F1-Score:
$$F_1 = 2 \\times \\frac{0.80 \\times 0.80}{0.80 + 0.80} = 2 \\times \\frac{0.64}{1.60} = 2 \\times 0.40 = \\mathbf{0.80 = 80.0\\%}$$

#### 4. Intersection over Union (IoU):
$$\\text{IoU} = \\frac{TP}{TP + FP + FN} = \\frac{80}{80 + 20 + 20} = \\frac{80}{120} = \\frac{2}{3} \\approx \\mathbf{0.6667 = 66.7\\%}$$

---

### 4. Summary Scorecard (Unit 5 Notes)
| Metric | Formula | Calculated Result | Benchmark Verdict |
| :--- | :---: | :---: | :--- |
| **Precision** | $\\frac{TP}{TP + FP}$ | **$80.0\\%$** | High purity (low false alarm rate) |
| **Recall** | $\\frac{TP}{TP + FN}$ | **$80.0\\%$** | High completeness (low missed detection rate) |
| **F1-Score** | $2 \\frac{P \\cdot R}{P + R}$ | **$80.0\\%$** | Perfect balance between precision and recall |
| **IoU** | $\\frac{TP}{TP + FP + FN}$ | **$66.7\\%$** | **Passed!** (Exceeds standard $50\\%$ benchmark) |

---

### 5. Optimization Strategies to Boost Scores (Unit 5 Notes)
1. **Adaptive Thresholding:** Eliminates $FP$ false alarms caused by changing shadows.
2. **Morphological Filtering:** Opening removes isolated noise speckles ($FP$), and closing seals interior holes ($FN$), directly boosting IoU.
3. **GPU Acceleration:** Delivers $>30\\text{ fps}$ real-time processing speed required for live autonomous vehicles."""
    }
]
