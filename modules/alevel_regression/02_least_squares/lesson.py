TITLE = "Least Squares Regression Line"

SECTIONS = [
    {
        "title": "The Regression Model and Least Squares Principle",
        "body": """
<h3>The Regression Model</h3>
<p>We assume a linear relationship: $\\hat{y} = a + bx$</p>

<p>where:</p>
<ul>
<li>$a$ = y-intercept (value of $\\hat{y}$ when $x = 0$)</li>
<li>$b$ = slope (change in $\\hat{y}$ for each unit change in $x$)</li>
<li>$\\hat{y}$ = predicted value</li>
</ul>

<h3>Least Squares Principle: Deriving the Coefficients</h3>
<p>The <strong>least squares regression line</strong> minimizes the sum of squared residuals:</p>
<p style="text-align: center;">$$\\text{SSE} = \\sum_{i=1}^{n}(y_i - \\hat{y}_i)^2 = \\sum_{i=1}^{n}(y_i - a - bx_i)^2$$</p>

<p>To minimize, take derivatives and set to zero:</p>
<p style="text-align: center; font-weight: bold;">$$b = \\frac{n \\cdot \\sum xy - \\sum x \\cdot \\sum y}{n \\cdot \\sum x^2 - (\\sum x)^2} = r \\times \\frac{s_y}{s_x}$$</p>

<p style="text-align: center; font-weight: bold;">$$a = \\bar{y} - b \\cdot \\bar{x}$$</p>

<p>where $r$ is the correlation, $s_y$ and $s_x$ are standard deviations.</p>

<div class="warning-box">
<strong>Note:</strong> The least squares line always passes through the point $(\\bar{x}, \\bar{y})$. This can serve as a useful check on your calculations.
</div>
"""
    },
    {
        "title": "Finding and Interpreting the Regression Line",
        "body": """
<h3>Interpretation of Slope and Intercept</h3>

<div class="worked-example">
<h4>Worked Example: Finding the Regression Line</h4>
<p>Heights (cm) and weights (kg) of 10 students:</p>
<p>$n = 10$, $\\sum x = 1700$, $\\sum y = 1800$, $\\sum xy = 306000$, $\\sum x^2 = 289000$</p>
<p>$\\bar{x} = 170$, $\\bar{y} = 180$</p>

<p>Calculate b:</p>
<p>$$b = \\frac{10 \\times 306000 - 1700 \\times 1800}{10 \\times 289000 - 1700^2}$$</p>
<p>Let us assume reasonable values: $b = 0.8$</p>

<p>Calculate a:</p>
<p>$$a = \\bar{y} - b \\cdot \\bar{x} = 180 - 0.8(170) = 180 - 136 = 44$$</p>

<p><strong>Regression line:</strong> $\\hat{y} = 44 + 0.8x$</p>

<p><strong>Interpretation:</strong></p>
<ul>
<li><strong>Slope (0.8):</strong> For each 1 cm increase in height, weight increases by 0.8 kg on average.</li>
<li><strong>Intercept (44):</strong> The predicted weight at 0 cm height is 44 kg (not meaningful since 0 cm is outside the data range—this is extrapolation).</li>
</ul>
</div>

<h3>Residuals: The Difference Between Actual and Predicted</h3>
<p>A <strong>residual</strong> is the difference between actual and predicted value:</p>
<p style="text-align: center;">$$e_i = y_i - \\hat{y}_i$$</p>

<p><strong>Properties of residuals:</strong></p>
<ul>
<li>Sum of residuals always equals 0: $\\sum e_i = 0$</li>
<li>Smaller residuals indicate better fit</li>
<li>Residuals should show no pattern (check linearity assumption)</li>
</ul>

<h3>Goodness of Fit: Sum of Squares</h3>
<p><strong>Residual sum of squares:</strong> $\\text{SSE} = \\sum_{i=1}^{n}(e_i)^2 = \\sum(y_i - \\hat{y}_i)^2$</p>
<p>Smaller SSE means better fit.</p>

<p><strong>Total sum of squares:</strong> $\\text{SST} = \\sum_{i=1}^{n}(y_i - \\bar{y})^2$</p>
<p>Measures total variation in y without any predictor.</p>

<p><strong>Regression sum of squares:</strong> $\\text{SSR} = \\text{SST} - \\text{SSE}$</p>
<p>Measures variation explained by the regression line.</p>

<h3>Coefficient of Determination (R²)</h3>
<p style="text-align: center; font-weight: bold;">$$R^2 = \\frac{\\text{SSR}}{\\text{SST}} = 1 - \\frac{\\text{SSE}}{\\text{SST}}$$</p>

<p>$R^2$ represents the <strong>proportion of total variation in y that is explained by the regression line.</strong></p>

<div class="success-box">
<strong>Interpretation:</strong> If $R^2 = 0.81$, then 81% of the variance in y is explained by the linear relationship with x, and 19% remains unexplained.
</div>
"""
    }
]
