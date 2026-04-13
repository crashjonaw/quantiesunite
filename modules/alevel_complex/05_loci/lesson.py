TITLE = "Loci and Regions in the Complex Plane"

SECTIONS = [
    {
        "title": "Loci Defined by Modulus Conditions",
        "body": """
<h3>Circles in the Complex Plane</h3>
<p>Equations involving the modulus |z| define curves in the Argand diagram:</p>
<div class="concept-box">
<p><strong>|z - a| = r:</strong> Circle centered at a with radius r</p>
<p><strong>|z - a| &lt; r:</strong> Interior of the circle (open disk)</p>
<p><strong>|z - a| ≤ r:</strong> Closed disk (interior plus boundary)</p>
<p><strong>|z - a| &gt; r:</strong> Exterior of the circle</p>
</div>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 1:</strong> Identifying a circle</p>
<p>The equation |z - 2| = 3 represents all complex numbers at distance 3 from the point 2 (on the real axis).</p>
<p>This is a circle with center at (2, 0) and radius 3.</p>
<p>In parametric form: \(z = 2 + 3 \\cdot \\text{cis}(\\theta) = 2 + 3(\cos\\theta + i \\cdot \sin\\theta)\) for \(\\theta \in [0, 2\\pi)\)</p>
</div>

<div class="worked-example">
<p><strong>Example 2:</strong> Finding a circle equation</p>
<p>Express |z - (1 + i)| = 2 in rectangular form \(z = x + yi\):</p>
<p>|(x + yi) - (1 + i)| = 2</p>
<p>|(x - 1) + (y - 1)i| = 2</p>
<p>\\(\\sqrt{(x-1)^2 + (y-1)^2} = 2\\)</p>
<p>\((x - 1)^2 + (y - 1)^2 = 4\)</p>
<p>This is a circle centered at (1, 1) with radius 2.</p>
</div>

<h3>Perpendicular Bisectors</h3>
<div class="concept-box">
<p><strong>|z - a| = |z - b|:</strong> Perpendicular bisector of the segment joining a and b</p>
</div>

<div class="worked-example">
<p><strong>Example 3:</strong> Perpendicular bisector equation</p>
<p>Describe the locus of points satisfying |z - 1| = |z - i|</p>
<p>These are points equidistant from 1 and i. Let \(z = x + yi\):</p>
<p>|(x - 1) + yi| = |x + (y - 1)i|</p>
<p>\\(\\sqrt{(x-1)^2 + y^2} = \\sqrt{x^2 + (y-1)^2}\\)</p>
<p>\((x - 1)^2 + y^2 = x^2 + (y - 1)^2\)</p>
<p>\(x^2 - 2x + 1 + y^2 = x^2 + y^2 - 2y + 1\)</p>
<p>\(-2x = -2y \Rightarrow x = y\)</p>
<p>The locus is the line \(y = x\) (passing through the origin at 45°).</p>
</div>
"""
    },
    {
        "title": "Loci Defined by Argument Conditions",
        "body": """
<h3>Rays and Sectors</h3>
<p>Equations involving the argument arg(z) define rays and angular regions:</p>
<div class="concept-box">
<p><strong>arg(z) = \(\\theta\):</strong> Ray from the origin at angle \(\\theta\) (half-line)</p>
<p><strong>arg(z - a) = \(\\theta\):</strong> Ray from point a at angle \(\\theta\)</p>
<p><strong>\(\\alpha\) &lt; arg(z) &lt; \(\\beta\):</strong> Angular sector (wedge) between angles \(\\alpha\) and \(\\beta\)</p>
</div>

<p><strong>Note:</strong> The argument is typically taken in the principal range \((-\\pi, \\pi]\) or \([0, 2\\pi)\).</p>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 4:</strong> Identifying a ray</p>
<p>The equation \(\arg(z) = \\pi/4\) represents all non-zero complex numbers at angle \(\\pi/4\) from the positive real axis.</p>
<p>This is the ray \(z = r \\cdot e^{i\\pi/4} = r(\cos(\\pi/4) + i \\cdot \sin(\\pi/4)) = r(1/\\sqrt{2} + i/\\sqrt{2})\) for r &gt; 0.</p>
<p>In rectangular form: \(z = x + yi\) where \(y = x\) and \(x > 0\) (the line \(y = x\) in the first quadrant).</p>
</div>

<div class="worked-example">
<p><strong>Example 5:</strong> Angular sector</p>
<p>Describe the region satisfying \(\\pi/6 < \arg(z) < \\pi/3\)</p>
<p>This is an open angular sector (wedge) between 30° and 60° from the positive real axis, extending infinitely from the origin.</p>
<p>Geometrically, it's a "pizza slice" shape with its vertex at the origin.</p>
</div>

<div class="worked-example">
<p><strong>Example 6:</strong> Ray from a shifted point</p>
<p>The equation \(\arg(z - (1 + i)) = \\pi/2\) represents all complex numbers whose direction from the point \((1 + i)\) is straight up (positive imaginary direction).</p>
<p>This is a vertical ray: \(z = (1 + i) + ti\) for \(t > 0\), or \(z = 1 + i(1 + t)\) with \(t > 0\).</p>
<p>In rectangular form: \(x = 1, y > 1\)</p>
</div>
"""
    },
    {
        "title": "Regions and Inequalities",
        "body": """
<h3>Combining Conditions</h3>
<p>Real-world problems often involve regions defined by multiple constraints. We combine modulus, argument, and other conditions:</p>

<div class="concept-box">
<p><strong>Common regions:</strong></p>
<ul>
<li><strong>Disk:</strong> |z - a| ≤ r (interior of circle plus boundary)</li>
<li><strong>Annulus (ring):</strong> \(r_1 < |z - a| < r_2\) (between two circles)</li>
<li><strong>Sector:</strong> \(\\alpha < \arg(z - a) < \\beta\) and |z - a| &lt; r (wedge inside a circle)</li>
<li><strong>Half-plane:</strong> Re(z) &gt; c (right of vertical line) or Im(z) &lt; d (below horizontal line)</li>
</ul>
</div>

<h3>Examples</h3>
<div class="worked-example">
<p><strong>Example 7:</strong> Annulus region</p>
<p>Describe the region: \(1 < |z| < 3\)</p>
<p>This is the set of points whose distance from the origin is between 1 and 3 (exclusive).</p>
<p>Geometrically, it's a ring (annulus) centered at the origin with inner radius 1 and outer radius 3.</p>
</div>

<div class="worked-example">
<p><strong>Example 8:</strong> Combined conditions</p>
<p>Describe the region: |z - i| ≤ 2 and Im(z) ≥ 0</p>
<p>First: |z - i| ≤ 2 is a closed disk centered at i with radius 2</p>
<p>Second: Im(z) ≥ 0 is the upper half-plane (including the real axis)</p>
<p>Combined: The upper half of the disk (a semicircular region)</p>
</div>

<div class="worked-example">
<p><strong>Example 9:</strong> Sector region</p>
<p>Describe the region: \(\\pi/4 < \arg(z) < \\pi/2\) and |z| &lt; 2</p>
<p>This is a circular sector ("pizza slice") with:</p>
<ul>
<li>Vertex at the origin</li>
<li>Radius less than 2</li>
<li>Angular span from 45° to 90° from the positive real axis</li>
</ul>
</div>

<h3>Applications</h3>
<p>Loci and regions are fundamental to:</p>
<ul>
<li><strong>Complex analysis:</strong> Defining domains of analytic functions</li>
<li><strong>Contour integration:</strong> Specifying paths in the complex plane</li>
<li><strong>Engineering:</strong> Representing Nyquist plots, poles, and zeros</li>
<li><strong>Signal processing:</strong> Characterizing stability regions</li>
</ul>
"""
    }
]
