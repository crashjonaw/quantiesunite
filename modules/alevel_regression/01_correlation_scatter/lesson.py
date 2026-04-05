TITLE = "Correlation and Scatter Diagrams"

SECTIONS = [
    {
        "title": "Scatter Plots and Visual Correlation Analysis",
        "body": """
<h3>Reading and Creating Scatter Plots</h3>
<p>A <strong>scatter plot</strong> displays the relationship between two quantitative variables:</p>
<ul>
<li>x-axis: independent variable (predictor)</li>
<li>y-axis: dependent variable (response)</li>
<li>Each point: one observation</li>
</ul>

<h3>Patterns to Identify</h3>

<p><strong>1. Direction:</strong></p>
<ul>
<li><strong>Positive association:</strong> As x increases, y tends to increase</li>
<li><strong>Negative association:</strong> As x increases, y tends to decrease</li>
<li><strong>No association:</strong> No clear pattern</li>
</ul>

<p><strong>2. Strength:</strong></p>
<ul>
<li><strong>Strong:</strong> Points cluster tightly around a line or curve</li>
<li><strong>Moderate:</strong> Clear trend but with substantial scatter</li>
<li><strong>Weak:</strong> Little apparent relationship</li>
</ul>

<p><strong>3. Form:</strong></p>
<ul>
<li><strong>Linear:</strong> Points roughly form a straight line</li>
<li><strong>Curved:</strong> Points follow a non-linear pattern</li>
<li><strong>Outliers:</strong> Points far from the overall pattern</li>
</ul>

<div class="concept-box">
<h4>Example 1: Interpreting Scatter Plots</h4>
<p>Heights and weights of students: scatter plot shows positive linear association (taller → heavier), with some scatter around a trend line.</p>
<p>This suggests using linear regression is appropriate.</p>
</div>

<h3>Conditions for Regression</h3>
<p><strong>Quantitative data:</strong> Both variables must be numeric</p>
<p><strong>Independence:</strong> Observations should be independent</p>
<p><strong>Linearity:</strong> The scatter plot should show a linear trend (not curved)</p>
<p><strong>No extreme outliers:</strong> Outliers can heavily influence results</p>
"""
    },
    {
        "title": "Correlation Coefficient: Measuring Association Strength",
        "body": """
<h3>Pearson Correlation Coefficient (r)</h3>
<p>The <strong>sample correlation coefficient</strong> r measures the strength and direction of linear association:</p>

<p style="text-align: center; font-weight: bold;">$$r = \\frac{\\sum_{i=1}^{n}(x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum_{i=1}^{n}(x_i - \\bar{x})^2 \\cdot \\sum_{i=1}^{n}(y_i - \\bar{y})^2}}$$</p>

<p><strong>Alternative formula (computational):</strong></p>
<p style="text-align: center;">$$r = \\frac{n \\cdot \\sum xy - \\sum x \\cdot \\sum y}{\\sqrt{[n \\cdot \\sum x^2 - (\\sum x)^2] \\times [n \\cdot \\sum y^2 - (\\sum y)^2]}}$$</p>

<h3>Properties of r</h3>
<ul>
<li>-1 ≤ r ≤ 1</li>
<li>r = 1: Perfect positive linear relationship</li>
<li>r = -1: Perfect negative linear relationship</li>
<li>r = 0: No linear relationship</li>
<li>|r| close to 1: Strong linear association</li>
<li>|r| close to 0: Weak linear association</li>
</ul>

<p><strong>Interpretation guideline:</strong></p>
<ul>
<li>|r| > 0.8: Very strong</li>
<li>0.6 < |r| ≤ 0.8: Strong</li>
<li>0.4 < |r| ≤ 0.6: Moderate</li>
<li>0.2 < |r| ≤ 0.4: Weak</li>
<li>|r| ≤ 0.2: Very weak or none</li>
</ul>

<div class="worked-example">
<h4>Worked Example: Computing Correlation</h4>
<p>Data: (1,2), (2,4), (3,5), (4,4), (5,5)</p>
<p>$\\bar{x} = 3$, $\\bar{y} = 4$</p>
<p>Numerator: $(1-3)(2-4) + (2-3)(4-4) + (3-3)(5-4) + (4-3)(4-4) + (5-3)(5-4)$</p>
<p>$= 4 + 0 + 0 + 0 + 2 = 6$</p>
<p>$\\sum(x_i - \\bar{x})^2 = 4 + 1 + 0 + 1 + 4 = 10$</p>
<p>$\\sum(y_i - \\bar{y})^2 = 4 + 0 + 1 + 0 + 1 = 6$</p>
<p>$r = \\frac{6}{\\sqrt{10 \\times 6}} = \\frac{6}{\\sqrt{60}} \\approx 0.775$ (strong positive)</p>
</div>

<h3>Coefficient of Determination (r²)</h3>
<p>r² represents the proportion of variance in y explained by x:</p>
<p style="text-align: center; font-weight: bold;">$$r^2 = \\frac{\\sum_{i=1}^{n}(\\hat{y}_i - \\bar{y})^2}{\\sum_{i=1}^{n}(y_i - \\bar{y})^2}$$</p>

<p>For r = 0.8: r² = 0.64, meaning 64% of variance in y is explained by x.</p>

<h3>Important: Correlation ≠ Causation</h3>
<p>A strong correlation doesn't imply x causes y. Consider:</p>
<ul>
<li><strong>Reverse causation:</strong> y might cause x</li>
<li><strong>Confounding:</strong> A third variable Z might cause both x and y</li>
<li><strong>Coincidence:</strong> The association might be by chance</li>
</ul>

<div class="success-box">
<strong>Key Insight:</strong> Correlation describes the strength and direction of a linear relationship, but finding correlation alone cannot establish causation. Always consider alternative explanations.
</div>
"""
    }
]
