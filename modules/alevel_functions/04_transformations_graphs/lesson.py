TITLE = "Transformations of Graphs"

SECTIONS = [
    {
        "title": "Graphical Transformations: Theory and Systematic Analysis",
        "body": """
<h3>Fundamental Transformation Classes</h3>
<p>Given the graph of \\( y = f(x) \\), we can systematically generate new functions via transformations. Each transformation affects the graph in a precise, predictable way.</p>

<h3>Vertical Transformations (Affect \\( y \\)-coordinates)</h3>

<div class="formula-box">
<h4>Vertical Shift</h4>
<p>\\( y = f(x) + k \\) shifts the graph vertically:</p>
<ul>
<li>\\( k > 0 \\): shift UP by \\( k \\) units</li>
<li>\\( k < 0 \\): shift DOWN by \\( |k| \\) units</li>
</ul>
<p><strong>Effect on range:</strong> \\( R_{f+k} = R_f + k = \\{ y + k : y \\in R_f \\} \\)</p>
</div>

<div class="formula-box">
<h4>Vertical Scaling and Reflection</h4>
<p>\\( y = a \\cdot f(x) \\) stretches or compresses vertically:</p>
<ul>
<li>\\( |a| > 1 \\): stretch vertically by factor \\( |a| \\)</li>
<li>\\( 0 < |a| < 1 \\): compress vertically by factor \\( 1/|a| \\)</li>
<li>\\( a < 0 \\): also reflects across \\( x \\)-axis</li>
</ul>
</div>

<h3>Horizontal Transformations (Affect \\( x \\)-coordinates)</h3>

<div class="formula-box">
<h4>Horizontal Shift</h4>
<p>\\( y = f(x - h) \\) shifts the graph horizontally:</p>
<ul>
<li>\\( h > 0 \\): shift RIGHT by \\( h \\) units</li>
<li>\\( h < 0 \\): shift LEFT by \\( |h| \\) units</li>
</ul>
<p><strong>Key insight:</strong> \\( f(x - h) \\) means "the value at \\( x \\) is what \\( f \\) had at \\( x - h \\)", so the graph shifts right.</p>
</div>

<div class="formula-box">
<h4>Horizontal Scaling and Reflection</h4>
<p>\\( y = f(bx) \\) compresses or stretches horizontally:</p>
<ul>
<li>\\( |b| > 1 \\): compress horizontally by factor \\( 1/|b| \\)</li>
<li>\\( 0 < |b| < 1 \\): stretch horizontally by factor \\( 1/|b| \\)</li>
<li>\\( b < 0 \\): also reflects across \\( y \\)-axis</li>
</ul>
</div>

<h3>General Transformation Composition</h3>

<div class="formula-box">
<h4>Standard Form</h4>
$$y = a \\cdot f\\left(b(x - h)\\right) + k$$
<p><strong>Order of operations:</strong></p>
<ol>
<li>Apply \\( f \\) to \\( bx \\) (horizontal scaling \\( b \\))</li>
<li>Apply \\( f(b(\\cdot)) \\) to \\( (x - h) \\) (horizontal shift \\( h \\))</li>
<li>Multiply by \\( a \\) (vertical scaling \\( a \\))</li>
<li>Add \\( k \\) (vertical shift \\( k \\))</li>
</ol>
</div>

<div class="example-box">
<h4>Example 1: Complex Transformation Sequence</h4>
<p><strong>Describe transformations from \\( y = \\sqrt{x} \\) to \\( y = -2\\sqrt{3(x-1)} + 4 \\)</strong></p>
<p><strong>Rewrite in standard form:</strong> \\( y = -2\\sqrt{3}\\sqrt{x-1} + 4 \\)</p>
<p><strong>Transformations (reading inside-out):</strong></p>
<ol>
<li>Shift RIGHT by 1: \\( \\sqrt{x-1} \\)</li>
<li>Compress horizontally by \\( 1/\\sqrt{3} \\approx 0.577 \\): \\( \\sqrt{3(x-1)} \\)</li>
<li>Stretch vertically by 2: \\( 2\\sqrt{3(x-1)} \\)</li>
<li>Reflect across \\( x \\)-axis: \\( -2\\sqrt{3(x-1)} \\)</li>
<li>Shift UP by 4: \\( -2\\sqrt{3(x-1)} + 4 \\)</li>
</ol>
</div>

<h3>Reflections</h3>

<div class="formula-box">
<h4>Three Types of Reflection</h4>
<ul>
<li><strong>Across \\( x \\)-axis:</strong> \\( y = -f(x) \\)</li>
<li><strong>Across \\( y \\)-axis:</strong> \\( y = f(-x) \\)</li>
<li><strong>Across \\( y = x \\):</strong> \\( y = f^{-1}(x) \\)</li>
</ul>
</div>

<div class="example-box">
<h4>Example 2: Reflection Mechanics</h4>
<p><strong>Graph of \\( f(x) = |x| \\):</strong></p>
<ul>
<li>Reflect across \\( x \\)-axis: \\( y = -|x| \\)</li>
<li>Reflect across \\( y \\)-axis: \\( y = |-x| = |x| \\) (even function, unchanged)</li>
<li>Reflect across \\( y = x \\): \\( y = |x|^{-1} \\) is not a function (fails horizontal line test)</li>
</ul>
</div>

<h3>Effect of Transformations on Key Features</h3>

<table style="margin: 15px auto; border-collapse: collapse; width: 95%;">
<tr style="border-bottom: 2px solid #333">
<td style="padding: 10px;"><strong>Transformation</strong></td>
<td style="padding: 10px;"><strong>Domain</strong></td>
<td style="padding: 10px;"><strong>Range</strong></td>
<td style="padding: 10px;"><strong>Asymptotes</strong></td>
</tr>
<tr >
<td style="padding: 10px;">\\( f(x) + k \\)</td>
<td style="padding: 10px;">Unchanged</td>
<td style="padding: 10px;">Shift by \\( k \\)</td>
<td style="padding: 10px;">Horiz. unch.; vert. shift \\( k \\)</td>
</tr>
<tr >
<td style="padding: 10px;">\\( a \\cdot f(x) \\)</td>
<td style="padding: 10px;">Unchanged</td>
<td style="padding: 10px;">Scale by \\( |a| \\)</td>
<td style="padding: 10px;">Vert. unch.; vert. asymptotes scale \\( |a| \\)</td>
</tr>
<tr >
<td style="padding: 10px;">\\( f(x-h) \\)</td>
<td style="padding: 10px;">Shift by \\( h \\)</td>
<td style="padding: 10px;">Unchanged</td>
<td style="padding: 10px;">Shift by \\( h \\)</td>
</tr>
<tr >
<td style="padding: 10px;">\\( f(bx) \\)</td>
<td style="padding: 10px;">Scale by \\( 1/|b| \\)</td>
<td style="padding: 10px;">Unchanged</td>
<td style="padding: 10px;">Vert. unch.; scale \\( x \\) by \\( 1/|b| \\)</td>
</tr>
</table>
"""
    }
]
