"""
Symmetry - Lesson Content

Topics covered:
- Lines of symmetry
- Reflective symmetry
- Rotational symmetry
- Identifying symmetry in shapes
- Completing symmetric figures
"""

SECTIONS = [
    {
        "title": "Understanding Symmetry",
        "body": """
        <h3>What is Symmetry?</h3>
        <p>Symmetry means a shape or object is <strong>balanced and identical on both sides of a line or point</strong>. If you fold the shape along the line of symmetry, the two sides match perfectly.</p>

        <div class='example-box'>
            <p><strong>Example:</strong> The letter "A" has symmetry. If you draw a vertical line down the middle, the left side is a mirror image of the right side.</p>
        </div>

        <div class="diagram-container">
          <svg width="400" height="200" viewBox="-15 -15 430 230">
            <rect x="0" y="0" width="400" height="200" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="200" y="30" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">The Letter A Has Symmetry</text>
            <line x1="200" y1="50" x2="200" y2="180" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4"/>
            <text x="200" y="198" text-anchor="middle" font-size="11" fill="#f59e0b">line of symmetry</text>
            <polygon points="200,60 145,170 160,170" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
            <polygon points="200,60 255,170 240,170" fill="#4169E180" stroke="#4169E1" stroke-width="2"/>
            <line x1="160" y1="135" x2="200" y2="135" stroke="#4169E1" stroke-width="2"/>
            <line x1="200" y1="135" x2="240" y2="135" stroke="#4169E1" stroke-width="2"/>
            <text x="120" y="140" text-anchor="middle" font-size="12" fill="currentColor">Left half</text>
            <text x="280" y="140" text-anchor="middle" font-size="12" fill="currentColor">Right half</text>
          </svg>
          <div class="diagram-caption">The dashed line divides the letter A into two matching halves</div>
        </div>

        <h3>Why Is Symmetry Important?</h3>
        <ul>
            <li><strong>Nature:</strong> Many animals and plants are symmetrical (butterflies, leaves, flowers)</li>
            <li><strong>Art and design:</strong> Symmetry creates balance and beauty</li>
            <li><strong>Mathematics:</strong> Symmetry helps us understand shapes and geometry</li>
            <li><strong>Science:</strong> Symmetry appears in molecules, crystals, and physical laws</li>
        </ul>

        <h3>Types of Symmetry</h3>
        <p>There are different kinds of symmetry:</p>
        <ul>
            <li><strong>Reflective symmetry:</strong> One half mirrors the other half</li>
            <li><strong>Rotational symmetry:</strong> A shape looks the same after turning it</li>
        </ul>
        """
    },
    {
        "title": "Reflective Symmetry (Mirror Symmetry)",
        "body": """
        <h3>What is a Line of Symmetry?</h3>
        <p>A line of symmetry is an <strong>imaginary line</strong> that divides a shape into two parts that are <strong>exact mirror images</strong> of each other.</p>

        <div class="diagram-container">
          <svg width="560" height="220" viewBox="-15 -15 590 250">
            <rect x="0" y="0" width="560" height="220" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="280" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">Lines of Symmetry in Common Shapes</text>

            <rect x="30" y="70" width="80" height="80" fill="#4169E180" stroke="#4169E1" stroke-width="2" rx="4"/>
            <line x1="70" y1="55" x2="70" y2="165" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
            <line x1="15" y1="110" x2="125" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
            <line x1="20" y1="60" x2="120" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>
            <line x1="120" y1="60" x2="20" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>
            <text x="70" y="185" text-anchor="middle" font-size="12" fill="currentColor">Square</text>
            <text x="70" y="200" text-anchor="middle" font-size="11" fill="#22c55e">4 lines</text>

            <rect x="170" y="80" width="110" height="60" fill="#22c55e80" stroke="#22c55e" stroke-width="2" rx="4"/>
            <line x1="225" y1="65" x2="225" y2="155" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
            <line x1="155" y1="110" x2="295" y2="110" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
            <text x="225" y="185" text-anchor="middle" font-size="12" fill="currentColor">Rectangle</text>
            <text x="225" y="200" text-anchor="middle" font-size="11" fill="#22c55e">2 lines</text>

            <polygon points="390,65 340,160 440,160" fill="#8b5cf680" stroke="#8b5cf6" stroke-width="2"/>
            <line x1="390" y1="50" x2="390" y2="175" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
            <line x1="365" y1="112" x2="440" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>
            <line x1="415" y1="112" x2="340" y2="160" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>
            <text x="390" y="185" text-anchor="middle" font-size="12" fill="currentColor">Equilateral Triangle</text>
            <text x="390" y="200" text-anchor="middle" font-size="11" fill="#22c55e">3 lines</text>

            <circle cx="510" cy="110" r="45" fill="#f59e0b40" stroke="#f59e0b" stroke-width="2"/>
            <line x1="510" y1="50" x2="510" y2="170" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5,3"/>
            <line x1="450" y1="110" x2="570" y2="110" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="5,3"/>
            <text x="510" y="185" text-anchor="middle" font-size="12" fill="currentColor">Circle</text>
            <text x="510" y="200" text-anchor="middle" font-size="11" fill="#22c55e">Infinite lines</text>
          </svg>
          <div class="diagram-caption">Dashed yellow lines show lines of symmetry for each shape</div>
        </div>

        <h3>How to Find Lines of Symmetry</h3>
        <p><strong>The Fold Test:</strong> Imagine folding the shape along a line. If the two halves match perfectly, that's a line of symmetry!</p>

        <div class='example-box'>
            <p><strong>Square:</strong> 4 lines of symmetry (vertical, horizontal, and two diagonals)</p>
            <p><strong>Rectangle:</strong> 2 lines of symmetry (vertical and horizontal only)</p>
            <p><strong>Equilateral triangle:</strong> 3 lines of symmetry (one through each vertex to the opposite side)</p>
            <p><strong>Isosceles triangle:</strong> 1 line of symmetry (from the top vertex straight down)</p>
            <p><strong>Circle:</strong> Infinite lines of symmetry (any line through the center!)</p>
        </div>

        <h3>Distinguishing Symmetrical from Asymmetrical</h3>

        <div class="diagram-container">
          <svg width="500" height="200" viewBox="-15 -15 530 230">
            <rect x="0" y="0" width="500" height="200" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="250" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">Symmetrical vs Asymmetrical</text>

            <text x="130" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#22c55e">Symmetrical</text>
            <rect x="40" y="70" width="60" height="60" fill="#22c55e30" stroke="#22c55e" stroke-width="2" rx="4"/>
            <text x="70" y="150" text-anchor="middle" font-size="11" fill="currentColor">Square</text>
            <polygon points="190,70 155,130 225,130" fill="#22c55e30" stroke="#22c55e" stroke-width="2"/>
            <text x="190" y="150" text-anchor="middle" font-size="11" fill="currentColor">Equil. Triangle</text>

            <line x1="260" y1="50" x2="260" y2="180" stroke="#555" stroke-width="1" stroke-dasharray="4,3"/>

            <text x="380" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#ef4444">Asymmetrical</text>
            <polygon points="310,70 300,130 370,130 360,80" fill="#ef444430" stroke="#ef4444" stroke-width="2"/>
            <text x="335" y="150" text-anchor="middle" font-size="11" fill="currentColor">Irregular Quad</text>
            <polygon points="420,75 400,110 415,130 455,125 460,90" fill="#ef444430" stroke="#ef4444" stroke-width="2"/>
            <text x="435" y="150" text-anchor="middle" font-size="11" fill="currentColor">Irregular Pentagon</text>
          </svg>
          <div class="diagram-caption">Symmetrical shapes can be folded evenly; asymmetrical shapes cannot</div>
        </div>

        <h3>Recognizing Reflective Symmetry</h3>
        <p>To check if something has reflective symmetry:</p>
        <ul>
            <li>Look for a line that divides the shape into two parts</li>
            <li>One part should be the mirror image of the other</li>
            <li>If you fold along that line, both sides match</li>
        </ul>
        """
    },
    {
        "title": "Rotational Symmetry",
        "body": """
        <h3>What is Rotational Symmetry?</h3>
        <p>Rotational symmetry means a shape looks <strong>the same after rotating it</strong> (turning it) around a central point, without flipping it.</p>

        <div class="diagram-container">
          <svg width="520" height="220" viewBox="-15 -15 550 250">
            <rect x="0" y="0" width="520" height="220" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="260" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">Rotating a Square by 90 Degrees</text>

            <rect x="30" y="65" width="80" height="80" fill="#4169E180" stroke="#4169E1" stroke-width="2" rx="4"/>
            <circle cx="45" cy="80" r="5" fill="#f59e0b"/>
            <text x="70" y="170" text-anchor="middle" font-size="11" fill="currentColor">Original (0 deg)</text>

            <text x="140" y="110" text-anchor="middle" font-size="18" fill="#8b949e">&#8594;</text>

            <rect x="165" y="65" width="80" height="80" fill="#4169E180" stroke="#4169E1" stroke-width="2" rx="4"/>
            <circle cx="230" cy="80" r="5" fill="#f59e0b"/>
            <text x="205" y="170" text-anchor="middle" font-size="11" fill="currentColor">90 deg turn</text>

            <text x="275" y="110" text-anchor="middle" font-size="18" fill="#8b949e">&#8594;</text>

            <rect x="300" y="65" width="80" height="80" fill="#4169E180" stroke="#4169E1" stroke-width="2" rx="4"/>
            <circle cx="365" cy="130" r="5" fill="#f59e0b"/>
            <text x="340" y="170" text-anchor="middle" font-size="11" fill="currentColor">180 deg turn</text>

            <text x="410" y="110" text-anchor="middle" font-size="18" fill="#8b949e">&#8594;</text>

            <rect x="430" y="65" width="80" height="80" fill="#4169E180" stroke="#4169E1" stroke-width="2" rx="4"/>
            <circle cx="445" cy="130" r="5" fill="#f59e0b"/>
            <text x="470" y="170" text-anchor="middle" font-size="11" fill="currentColor">270 deg turn</text>

            <text x="260" y="205" text-anchor="middle" font-size="12" fill="#22c55e">The square looks the same each time! Order 4 rotational symmetry.</text>
          </svg>
          <div class="diagram-caption">The yellow dot tracks the corner position as the square rotates</div>
        </div>

        <h3>Order of Rotational Symmetry</h3>
        <p>The <strong>order of rotational symmetry</strong> is the number of times a shape looks identical when rotated 360 degrees.</p>

        <div class="diagram-container">
          <svg width="500" height="200" viewBox="-15 -15 530 230">
            <rect x="0" y="0" width="500" height="200" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="250" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">Order of Rotational Symmetry</text>

            <polygon points="80,55 40,125 120,125" fill="#8b5cf680" stroke="#8b5cf6" stroke-width="2"/>
            <circle cx="80" cy="100" r="3" fill="#f59e0b"/>
            <text x="80" y="150" text-anchor="middle" font-size="12" fill="currentColor">Equil. Triangle</text>
            <text x="80" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#22c55e">Order 3</text>

            <rect x="170" y="60" width="70" height="70" fill="#4169E180" stroke="#4169E1" stroke-width="2" rx="4"/>
            <circle cx="205" cy="95" r="3" fill="#f59e0b"/>
            <text x="205" y="150" text-anchor="middle" font-size="12" fill="currentColor">Square</text>
            <text x="205" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#22c55e">Order 4</text>

            <polygon points="330,55 300,75 300,110 330,130 360,110 360,75" fill="#22c55e60" stroke="#22c55e" stroke-width="2"/>
            <circle cx="330" cy="92" r="3" fill="#f59e0b"/>
            <text x="330" y="150" text-anchor="middle" font-size="12" fill="currentColor">Hexagon</text>
            <text x="330" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#22c55e">Order 6</text>

            <rect x="405" y="70" width="90" height="50" fill="#f59e0b60" stroke="#f59e0b" stroke-width="2" rx="4"/>
            <circle cx="450" cy="95" r="3" fill="#ef4444"/>
            <text x="450" y="150" text-anchor="middle" font-size="12" fill="currentColor">Rectangle</text>
            <text x="450" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#22c55e">Order 2</text>
          </svg>
          <div class="diagram-caption">Higher order means more positions where the shape looks the same</div>
        </div>

        <h3>Difference Between Reflective and Rotational Symmetry</h3>
        <div class='example-box'>
            <p><strong>Reflective symmetry:</strong> You need to flip or mirror the shape (imagine reflecting in a mirror)</p>
            <p><strong>Rotational symmetry:</strong> You rotate or turn the shape (no flipping involved)</p>
            <p><strong>Note:</strong> A shape can have both! A square has both reflective AND rotational symmetry.</p>
        </div>
        """
    },
    {
        "title": "Completing Symmetric Figures",
        "body": """
        <h3>Drawing the Other Half</h3>
        <p>If you're given half of a symmetric figure and a line of symmetry, you can <strong>complete the figure by drawing the mirror image</strong>.</p>

        <div class="diagram-container">
          <svg width="400" height="280" viewBox="-15 -15 430 310">
            <rect x="0" y="0" width="400" height="280" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="200" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">Completing a Symmetric Figure</text>

            <line x1="200" y1="45" x2="200" y2="260" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6,4"/>
            <text x="200" y="275" text-anchor="middle" font-size="11" fill="#f59e0b">line of symmetry</text>

            <line x1="40" y1="80" x2="40" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="80" y1="80" x2="80" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="120" y1="80" x2="120" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="160" y1="80" x2="160" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="240" y1="80" x2="240" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="280" y1="80" x2="280" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="320" y1="80" x2="320" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="360" y1="80" x2="360" y2="240" stroke="#444" stroke-width="0.5"/>
            <line x1="40" y1="80" x2="360" y2="80" stroke="#444" stroke-width="0.5"/>
            <line x1="40" y1="120" x2="360" y2="120" stroke="#444" stroke-width="0.5"/>
            <line x1="40" y1="160" x2="360" y2="160" stroke="#444" stroke-width="0.5"/>
            <line x1="40" y1="200" x2="360" y2="200" stroke="#444" stroke-width="0.5"/>
            <line x1="40" y1="240" x2="360" y2="240" stroke="#444" stroke-width="0.5"/>

            <polygon points="200,80 120,120 80,200 120,240 200,240" fill="#4169E140" stroke="#4169E1" stroke-width="2.5"/>
            <text x="140" y="170" text-anchor="middle" font-size="11" fill="#4169E1">Given half</text>

            <polygon points="200,80 280,120 320,200 280,240 200,240" fill="#22c55e30" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="6,3"/>
            <text x="260" y="170" text-anchor="middle" font-size="11" fill="#22c55e">Mirror half</text>

            <circle cx="120" cy="120" r="4" fill="#4169E1"/>
            <circle cx="280" cy="120" r="4" fill="#22c55e"/>
            <line x1="120" y1="120" x2="280" y2="120" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>

            <circle cx="80" cy="200" r="4" fill="#4169E1"/>
            <circle cx="320" cy="200" r="4" fill="#22c55e"/>
            <line x1="80" y1="200" x2="320" y2="200" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>
          </svg>
          <div class="diagram-caption">Each point on the left is reflected the same distance on the right</div>
        </div>

        <h3>Step-by-Step Method</h3>
        <p><strong>Step 1: Identify the line of symmetry</strong> (usually marked with a dotted or dashed line)</p>
        <p><strong>Step 2: Look at each point on the given half</strong> and find its distance from the line of symmetry</p>
        <p><strong>Step 3: Mark the same distance on the other side</strong> of the line</p>
        <p><strong>Step 4: Connect the points</strong> to form the mirror image</p>

        <div class='example-box'>
            <p><strong>Example: Complete this triangle with a vertical line of symmetry</strong></p>
            <p>You're given the right half. The line is in the middle.</p>
            <p>Take the top point: it's 2cm from the line. On the left side, mark a point 2cm from the line.</p>
            <p>Take the bottom-right point: it's 3cm to the right, 5cm down from top. On the left, mark a point 3cm to the left, 5cm down.</p>
            <p>Connect these points to complete the triangle!</p>
        </div>

        <h3>Using a Grid to Help</h3>
        <p>Grids make completing symmetric figures easier:</p>
        <div class='example-box'>
            <p>If a point is on square (3,4) and the line of symmetry is vertical down the middle at x=5,
            the mirror point is at (7,4) -- same height, but reflected across the line.</p>
        </div>

        <h3>Types of Problems</h3>
        <ul>
            <li><strong>Mirror along vertical line:</strong> Swap left and right positions</li>
            <li><strong>Mirror along horizontal line:</strong> Swap top and bottom positions</li>
            <li><strong>Mirror along diagonal line:</strong> More complex; swap both coordinates</li>
        </ul>

        <h3>Checking Your Work</h3>
        <p>After completing a symmetric figure, fold your paper along the line of symmetry. Both halves should match perfectly!</p>
        """
    },
    {
        "title": "Symmetry in Nature and Design",
        "body": """
        <h3>Symmetry in Living Things</h3>
        <p>Nature is full of symmetry!</p>

        <div class="diagram-container">
          <svg width="500" height="220" viewBox="-15 -15 530 250">
            <rect x="0" y="0" width="500" height="220" rx="4" fill="#1e293b" stroke="#334155" stroke-width="1"/>
            <text x="250" y="28" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">Symmetry in Nature</text>

            <text x="80" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Butterfly</text>
            <text x="80" y="72" text-anchor="middle" font-size="10" fill="#22c55e">Bilateral</text>
            <line x1="80" y1="82" x2="80" y2="180" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>
            <ellipse cx="60" cy="115" rx="25" ry="15" fill="#8b5cf640" stroke="#8b5cf6" stroke-width="1.5" transform="rotate(-15,60,115)"/>
            <ellipse cx="100" cy="115" rx="25" ry="15" fill="#8b5cf640" stroke="#8b5cf6" stroke-width="1.5" transform="rotate(15,100,115)"/>
            <ellipse cx="62" cy="148" rx="20" ry="12" fill="#4169E140" stroke="#4169E1" stroke-width="1.5" transform="rotate(-10,62,148)"/>
            <ellipse cx="98" cy="148" rx="20" ry="12" fill="#4169E140" stroke="#4169E1" stroke-width="1.5" transform="rotate(10,98,148)"/>
            <ellipse cx="80" cy="130" rx="5" ry="25" fill="#333" stroke="#666" stroke-width="1"/>

            <text x="250" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Starfish</text>
            <text x="250" y="72" text-anchor="middle" font-size="10" fill="#22c55e">5-fold Rotational</text>
            <polygon points="250,85 258,115 290,120 265,140 272,172 250,155 228,172 235,140 210,120 242,115" fill="#f59e0b40" stroke="#f59e0b" stroke-width="1.5"/>
            <circle cx="250" cy="130" r="3" fill="#f59e0b"/>

            <text x="420" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">Snowflake</text>
            <text x="420" y="72" text-anchor="middle" font-size="10" fill="#22c55e">6-fold Rotational</text>
            <line x1="420" y1="88" x2="420" y2="178" stroke="#4169E1" stroke-width="2"/>
            <line x1="381" y1="111" x2="459" y2="155" stroke="#4169E1" stroke-width="2"/>
            <line x1="381" y1="155" x2="459" y2="111" stroke="#4169E1" stroke-width="2"/>
            <line x1="420" y1="88" x2="410" y2="100" stroke="#4169E1" stroke-width="1.5"/>
            <line x1="420" y1="88" x2="430" y2="100" stroke="#4169E1" stroke-width="1.5"/>
            <line x1="420" y1="178" x2="410" y2="166" stroke="#4169E1" stroke-width="1.5"/>
            <line x1="420" y1="178" x2="430" y2="166" stroke="#4169E1" stroke-width="1.5"/>
            <circle cx="420" cy="133" r="3" fill="#4169E1"/>

            <text x="250" y="210" text-anchor="middle" font-size="12" fill="currentColor">Many living things use symmetry for balance, movement, and beauty</text>
          </svg>
          <div class="diagram-caption">Different types of symmetry found in nature</div>
        </div>

        <div class='example-box'>
            <p><strong>Human body:</strong> Nearly bilateral symmetry (left-right symmetry)</p>
            <p><strong>Butterflies:</strong> Perfect bilateral symmetry</p>
            <p><strong>Starfish:</strong> Radial symmetry (5-fold rotational symmetry)</p>
            <p><strong>Flowers:</strong> Many have rotational symmetry (3-fold, 4-fold, 5-fold, etc.)</p>
            <p><strong>Snowflakes:</strong> 6-fold rotational symmetry!</p>
        </div>

        <h3>Symmetry in Architecture and Design</h3>
        <ul>
            <li>Buildings often have reflective symmetry (facade mirrors left and right)</li>
            <li>Logos and symbols use symmetry for balance and recognition</li>
            <li>Tiles and patterns use symmetry to create beautiful designs</li>
            <li>Letters and numbers: some have symmetry (A, H, I, M, O, U, V, W, X, Y, Z), others don't</li>
        </ul>

        <h3>Why Symmetry Is Used</h3>
        <ul>
            <li><strong>Efficiency:</strong> In nature, bilateral symmetry helps with movement and navigation</li>
            <li><strong>Beauty:</strong> Symmetrical designs are often more pleasing to the eye</li>
            <li><strong>Recognition:</strong> Symmetrical shapes are easier for our brain to recognize</li>
            <li><strong>Stability:</strong> Symmetrical structures are often more stable</li>
        </ul>

        <h3>Finding Symmetry Around You</h3>
        <p>Challenge yourself to find lines of symmetry:</p>
        <ul>
            <li>In road signs (triangle, square, circle)</li>
            <li>In letters and words (which ones are symmetrical?)</li>
            <li>In nature (leaves, flowers, insects)</li>
            <li>In architecture (buildings, bridges, doors)</li>
        </ul>

        <h3>Key Insight</h3>
        <p>Symmetry is everywhere, and recognizing it helps us understand and appreciate the world's design and structure!</p>
        """
    }
]
