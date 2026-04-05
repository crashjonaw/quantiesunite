TITLE = "Advanced Topics and Practical Workflow"

SECTIONS = [
    {
        "title": "Multiple Linear Regression",
        "body": """
<h3>Multiple Linear Regression (Conceptual Introduction)</h3>
<p>When predicting y from multiple predictors $x_1, x_2, \\ldots, x_p$:</p>
<p style="text-align: center; font-weight: bold;">$$\\hat{y} = a + b_1 x_1 + b_2 x_2 + \\ldots + b_p x_p$$</p>

<p><strong>Interpretation:</strong> $b_i$ = change in $\\hat{y}$ for a 1-unit increase in $x_i$, holding all other variables constant.</p>

<h3>Advantages of Multiple Regression</h3>
<ul>
<li>Accounts for multiple factors simultaneously</li>
<li>Can improve predictions by including relevant variables</li>
<li>Helps control for confounding variables</li>
</ul>

<h3>Challenges in Multiple Regression</h3>

<p><strong>1. Multicollinearity:</strong> Predictors are correlated with each other</p>
<ul>
<li>Makes coefficients unstable and hard to interpret</li>
<li>Solution: Remove redundant variables or use dimensionality reduction</li>
</ul>

<p><strong>2. Overfitting:</strong> Using too many predictors</p>
<ul>
<li>Model fits noise instead of the true relationship</li>
<li>Predictions on new data are poor</li>
<li>Solution: Use fewer variables, cross-validation, or regularization</li>
</ul>

<p><strong>3. Model Selection:</strong> Which variables to include?</p>
<ul>
<li>More predictors don't always improve predictions</li>
<li>Use domain knowledge, forward/backward selection, or information criteria (AIC, BIC)</li>
</ul>

<div class="concept-box">
<h4>Multiple Regression Example</h4>
<p>Predicting house price from: size (sq ft), number of bedrooms, age (years)</p>
<p>$$\\hat{\\text{Price}} = 50000 + 150 \\cdot \\text{Size} + 30000 \\cdot \\text{Bedrooms} - 1000 \\cdot \\text{Age}$$</p>
<p><strong>Interpretation:</strong> Each additional square foot adds $150 to predicted price (holding bedrooms and age constant).</p>
</div>
"""
    },
    {
        "title": "Non-Linear Transformations and Curved Relationships",
        "body": """
<h3>When the Relationship Is Not Linear</h3>
<p>If a scatter plot shows a curved pattern, try transforming variables to linearize the relationship.</p>

<h3>Common Transformations</h3>

<p><strong>1. Logarithmic Transformation (Power Law)</strong></p>
<p>If $y = a \\cdot x^b$ (power law), apply log to both sides:</p>
<p style="text-align: center;">$$\\log(y) = \\log(a) + b \\cdot \\log(x)$$</p>
<p>Then fit linear regression: $\\log(y)$ vs. $\\log(x)$</p>

<p><strong>2. Exponential Transformation</strong></p>
<p>If $y = a \\cdot e^{bx}$ (exponential growth), take natural log of y:</p>
<p style="text-align: center;">$$\\ln(y) = \\ln(a) + bx$$</p>
<p>Then fit linear regression: $\\ln(y)$ vs. $x$</p>

<div class="worked-example">
<h4>Worked Example: Log Transformation</h4>
<p>Growth data suggests exponential: $y = a \\cdot e^{bx}$</p>
<p><strong>Step 1:</strong> Transform: $\\ln(y) = \\ln(a) + bx$</p>
<p><strong>Step 2:</strong> Fit linear regression of $\\ln(y)$ vs. $x$. Suppose we get: $\\ln(y) = 0.5 + 0.1x$</p>
<p><strong>Step 3:</strong> Back-transform to original scale: $y = e^{0.5} \\cdot e^{0.1x} \\approx 1.649 \\cdot e^{0.1x}$</p>
</div>

<p><strong>3. Polynomial Transformations</strong></p>
<p>For parabolic or polynomial patterns, include powers of x:</p>
<p style="text-align: center;">$$\\hat{y} = a + bx + cx^2$$ (quadratic)</p>

<h3>Important Caveat</h3>

<div class="warning-box">
<strong>Always check residual plots after transformation.</strong> The transformed variables must still satisfy linearity, homoscedasticity, normality, and independence assumptions. Transformations don't always solve all problems.
</div>

<h3>Correlation Matrix for Multiple Variables</h3>
<p>A <strong>correlation matrix</strong> shows pairwise correlations for multiple variables.</p>

<p><strong>Usage:</strong></p>
<ul>
<li>Identify which variables are most correlated with the response</li>
<li>Detect multicollinearity among predictors</li>
<li>Guide variable selection for multiple regression</li>
</ul>
"""
    },
    {
        "title": "Practical Regression Workflow and Best Practices",
        "body": """
<h3>A Complete Regression Analysis Workflow</h3>

<ol>
<li><strong>Exploratory Data Analysis (EDA):</strong> Create scatter plot to assess direction, strength, and linearity of the relationship</li>
<li><strong>Compute correlation coefficient:</strong> Calculate r and r² to quantify association strength</li>
<li><strong>Fit regression line:</strong> Calculate slope (b) and intercept (a) using least squares</li>
<li><strong>Examine residuals:</strong> Plot residuals vs. fitted values or vs. x to check assumptions</li>
<li><strong>Validate assumptions:</strong>
   <ul>
   <li>Linearity: Residuals show no pattern</li>
   <li>Homoscedasticity: Constant variance</li>
   <li>Normality: Residuals approximately normal (Q-Q plot or histogram)</li>
   <li>Independence: By design (not testable from residuals)</li>
   </ul>
</li>
<li><strong>Report results:</strong> Regression equation, r², standard error, and interpretation</li>
<li><strong>Make predictions:</strong> Use for interpolation (within data range). Avoid extrapolation or report with caution</li>
<li><strong>Discuss limitations:</strong> Potential confounders, causal interpretation pitfalls, assumption violations</li>
</ol>

<h3>Documentation and Reporting</h3>

<div class="success-box">
<strong>A Complete Regression Report Should Include:</strong>
<ul>
<li>Scatter plot with regression line</li>
<li>Regression equation: $\\hat{y} = a + bx$</li>
<li>Correlation coefficient (r) and coefficient of determination (r²)</li>
<li>Interpretation: "For each 1-unit increase in x, y increases by b units (on average)."</li>
<li>Residual plots to check assumptions</li>
<li>Outlier analysis and influential point discussion</li>
<li>Caution about causation and extrapolation</li>
</ul>
</div>

<h3>Summary: When to Use Each Tool</h3>

<p><strong>Scatter plot:</strong> First step; assess linearity and identify outliers</p>
<p><strong>Correlation coefficient (r):</strong> Quantify strength and direction; quick summary</p>
<p><strong>Regression line:</strong> Make predictions within the data range (interpolation)</p>
<p><strong>Residual plots:</strong> Validate that regression assumptions hold</p>
<p><strong>Coefficient of determination (r²):</strong> Communicate explained variance to stakeholders</p>
<p><strong>Transformations or multiple regression:</strong> When simple linear regression isn't adequate</p>
"""
    }
]
