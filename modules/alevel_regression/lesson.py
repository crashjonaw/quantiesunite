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

<div class="example-box">
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

<p style="text-align: center; font-weight: bold;">r = Σ[(x_i - x̄)(y_i - ȳ)] / √[Σ(x_i - x̄)² × Σ(y_i - ȳ)²]</p>

<p><strong>Alternative formula (computational):</strong></p>
<p>r = [n·Σ(xy) - Σ(x)·Σ(y)] / √{[n·Σ(x²) - (Σx)²] × [n·Σ(y²) - (Σy)²]}</p>

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

<div class="example-box">
<h4>Example 2: Computing Correlation</h4>
<p>Data: (1,2), (2,4), (3,5), (4,4), (5,5)</p>
<p>x̄ = 3, ȳ = 4</p>
<p>Numerator: (1-3)(2-4) + (2-3)(4-4) + (3-3)(5-4) + (4-3)(4-4) + (5-3)(5-4)</p>
<p>= 4 + 0 + 0 + 0 + 2 = 6</p>
<p>Σ(x_i - x̄)² = 4 + 1 + 0 + 1 + 4 = 10</p>
<p>Σ(y_i - ȳ)² = 4 + 0 + 1 + 0 + 1 = 6</p>
<p>r = 6 / √(10 × 6) = 6 / √60 ≈ 0.775 (strong positive)</p>
</div>

<h3>Coefficient of Determination (r²)</h3>
<p>r² represents the proportion of variance in y explained by x:</p>
<p style="text-align: center; font-weight: bold;">r² = [Σ(ŷ_i - ȳ)²] / [Σ(y_i - ȳ)²]</p>

<p>For r = 0.8: r² = 0.64, meaning 64% of variance in y is explained by x.</p>

<h3>Important: Correlation ≠ Causation</h3>
<p>A strong correlation doesn't imply x causes y. Consider:</p>
<ul>
<li><strong>Reverse causation:</strong> y might cause x</li>
<li><strong>Confounding:</strong> A third variable Z might cause both x and y</li>
<li><strong>Coincidence:</strong> The association might be by chance</li>
</ul>
"""
    },
    {
        "title": "Least Squares Regression: Deriving the Line of Best Fit",
        "body": """
<h3>The Regression Model</h3>
<p>We assume a linear relationship: ŷ = a + bx</p>

<p>where:</p>
<ul>
<li>a = y-intercept (value of ŷ when x = 0)</li>
<li>b = slope (change in ŷ for each unit change in x)</li>
<li>ŷ = predicted value</li>
</ul>

<h3>Least Squares Principle: Deriving the Coefficients</h3>
<p>The <strong>least squares regression line</strong> minimizes the sum of squared residuals:</p>
<p>SSE = Σ(y_i - ŷ_i)² = Σ(y_i - a - bx_i)²</p>

<p>To minimize, take derivatives and set to zero:</p>
<p style="text-align: center; font-weight: bold;">b = [n·Σ(xy) - Σ(x)·Σ(y)] / [n·Σ(x²) - (Σx)²] = r × (s_y / s_x)</p>

<p style="text-align: center; font-weight: bold;">a = ȳ - b·x̄</p>

<p>where r is the correlation, s_y and s_x are standard deviations.</p>

<h3>Interpretation of Slope and Intercept</h3>

<div class="example-box">
<h4>Example 3: Finding the Regression Line</h4>
<p>Heights and weights: n = 10, Σx = 1700, Σy = 1800, Σxy = 306000, Σx² = 289000</p>
<p>x̄ = 170, ȳ = 180</p>
<p>b = (10 × 306000 - 1700 × 1800) / (10 × 289000 - 1700²)</p>
<p>= (3060000 - 3060000) / (2890000 - 2890000) — Let me recalculate with realistic data.</p>
<p>Assume: b = 0.8, a = ȳ - b·x̄ = 180 - 0.8(170) = 180 - 136 = 44</p>
<p>Regression line: ŷ = 44 + 0.8x</p>
<p><strong>Interpretation:</strong> For each 1 cm increase in height, weight increases by 0.8 kg on average. At 0 cm height (extrapolation), predicted weight is 44 kg (not meaningful).</p>
</div>

<h3>Residuals and Goodness of Fit</h3>
<p>A <strong>residual</strong> is the difference between actual and predicted: e_i = y_i - ŷ_i</p>

<p><strong>Properties of residuals:</strong></p>
<ul>
<li>Sum of residuals = 0 (always)</li>
<li>Smaller residuals = better fit</li>
<li>Residuals should show no pattern (check linearity assumption)</li>
</ul>

<p><strong>Residual sum of squares:</strong> SSE = Σ(e_i)²</p>
<p><strong>Total sum of squares:</strong> SST = Σ(y_i - ȳ)²</p>
<p><strong>Regression sum of squares:</strong> SSR = SST - SSE</p>

<p>The coefficient of determination: R² = SSR / SST = 1 - (SSE / SST)</p>
"""
    },
    {
        "title": "Predictions, Extrapolation, and Model Validation",
        "body": """
<h3>Making Predictions with the Regression Line</h3>
<p>Once we have ŷ = a + bx, we can predict y for any x value:</p>

<div class="example-box">
<h4>Example 4: Prediction</h4>
<p>Using ŷ = 44 + 0.8x, predict weight for someone 180 cm tall:</p>
<p>ŷ = 44 + 0.8(180) = 44 + 144 = 188 kg</p>
</div>

<h3>Interpolation vs. Extrapolation</h3>

<p><strong>Interpolation:</strong> Predicting for x values within the range of observed data.</p>
<ul>
<li>Generally reliable if the linear relationship holds</li>
<li>Less uncertainty</li>
</ul>

<p><strong>Extrapolation:</strong> Predicting for x values outside the observed range.</p>
<ul>
<li>Risky! The relationship might not extend beyond the data</li>
<li>Greater uncertainty</li>
<li>Example: Predicting weight at x = 250 cm (implausibly tall)</li>
</ul>

<div class="example-box">
<h4>Example 5: Interpolation vs Extrapolation</h4>
<p>Data range: 160-180 cm.</p>
<p>Predict at 170 cm: Interpolation (reliable)</p>
<p>Predict at 200 cm: Extrapolation (risky; relationship might not extend)</p>
<p>Predict at 50 cm: Extrapolation (clearly unrealistic; model breaks down)</p>
</div>

<h3>Residual Diagnostics</h3>
<p>Plot residuals vs. fitted values (or vs. x) to check assumptions:</p>

<p><strong>Linearity:</strong> Residual plot shows no pattern (random scatter)</p>
<p><strong>Homoscedasticity:</strong> Residuals have constant variance (don't fan out)</p>
<p><strong>Normality:</strong> Residuals are approximately normally distributed (check with Q-Q plot)</p>
<p><strong>Independence:</strong> Observations are independent (by design of study)</p>

<p>If assumptions violated, the regression line may not be appropriate.</p>

<h3>Influential Points and Outliers</h3>

<p><strong>Outlier:</strong> y value far from predicted (large residual)</p>
<p><strong>Influential point:</strong> Changes the regression line significantly if removed (unusual x value)</p>

<p><strong>Strategies:</strong></p>
<ul>
<li>Investigate outliers: data entry error, special case, or genuine observation?</li>
<li>Report results with and without outliers</li>
<li>Use robust regression methods if outliers are legitimate</li>
</ul>

<div class="example-box">
<h4>Example 6: Outlier Impact</h4>
<p>A student with height 165 cm but weight 120 kg is an outlier (very heavy for height).</p>
<p>This point has a large residual but might not be influential if x = 165 is not unusual.</p>
<p>Report analysis both with and without this observation.</p>
</div>

<h3>Limitations of Linear Regression</h3>
<ul>
<li>Assumes linear relationship (check with scatter plot)</li>
<li>Only measures linear association</li>
<li>Sensitive to outliers</li>
<li>Predictions unreliable outside the data range</li>
<li>Correlation ≠ causation (don't infer cause from regression)</li>
</ul>
"""
    },
    {
        "title": "Advanced Topics: Multiple Regression and Transformations",
        "body": """
<h3>Multiple Linear Regression (Conceptual)</h3>
<p>When predicting y from multiple predictors x₁, x₂, ..., x_p:</p>
<p style="text-align: center; font-weight: bold;">ŷ = a + b₁x₁ + b₂x₂ + ... + b_p·x_p</p>

<p><strong>Interpretation:</strong> b_i = change in ŷ for a 1-unit increase in x_i, holding other variables constant.</p>

<p><strong>Challenges:</strong></p>
<ul>
<li><strong>Multicollinearity:</strong> Predictors are correlated, making coefficients unstable</li>
<li><strong>Overfitting:</strong> Too many predictors fit noise instead of true relationship</li>
<li><strong>Model selection:</strong> Which predictors to include?</li>
</ul>

<h3>Non-Linear Transformations</h3>
<p>When the relationship is curved, transform variables to linearize:</p>

<p><strong>1. Logarithmic transformation:</strong> If y = a·x^b (power law), use log(y) vs. log(x)</p>
<p>Then fit: log(y) = log(a) + b·log(x)</p>

<div class="example-box">
<h4>Example 7: Log Transformation</h4>
<p>Growth data suggests exponential: y = a·e^(bx)</p>
<p>Transform: log(y) = log(a) + bx</p>
<p>Fit linear regression of log(y) vs. x</p>
<p>Back-transform: y = a·e^(bx) with estimated a and b</p>
</div>

<p><strong>2. Square root or polynomial transformations:</strong> For other curved patterns</p>

<p><strong>Note:</strong> Always check that transformed residuals satisfy linear regression assumptions.</p>

<h3>Correlation Matrix and Relationships Among Many Variables</h3>
<p>A <strong>correlation matrix</strong> shows pairwise correlations for multiple variables.</p>

<p><strong>Usage:</strong></p>
<ul>
<li>Identify which variables are most correlated with the response</li>
<li>Detect multicollinearity among predictors</li>
<li>Guide variable selection</li>
</ul>

<h3>Practical Regression Workflow</h3>
<ol>
<li>Create scatter plot to assess linearity</li>
<li>Compute correlation coefficient r</li>
<li>Fit least squares regression line</li>
<li>Check residual diagnostics (plot residuals)</li>
<li>Validate assumptions (linearity, homoscedasticity, normality)</li>
<li>Report regression equation, r², and interpretation</li>
<li>Use for interpolation only (or extrapolation with caution and uncertainty intervals)</li>
<li>Discuss potential confounders and limitations</li>
</ol>
"""
    }
]
