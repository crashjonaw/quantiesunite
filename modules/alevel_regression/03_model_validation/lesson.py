TITLE = "Residuals and Model Validation"

SECTIONS = [
    {
        "title": "Making Predictions and Understanding Interpolation vs. Extrapolation",
        "body": """
<h3>Making Predictions with the Regression Line</h3>
<p>Once we have $\\hat{y} = a + bx$, we can predict y for any x value by substituting into the equation.</p>

<div class="worked-example">
<h4>Worked Example: Using the Regression Line for Prediction</h4>
<p>Using $\\hat{y} = 44 + 0.8x$, predict weight for someone 180 cm tall:</p>
<p>$$\\hat{y} = 44 + 0.8(180) = 44 + 144 = 188 \\text{ kg}$$</p>
</div>

<h3>Interpolation vs. Extrapolation</h3>

<p><strong>Interpolation:</strong> Predicting for x values within the range of observed data.</p>
<ul>
<li>Generally reliable if the linear relationship holds</li>
<li>Less uncertainty in predictions</li>
<li>Recommended approach for making predictions</li>
</ul>

<p><strong>Extrapolation:</strong> Predicting for x values outside the observed range.</p>
<ul>
<li>Risky! The relationship might not extend beyond the data</li>
<li>Greater uncertainty and unreliability</li>
<li>Example: Using a height-weight regression model built on data from 160–180 cm to predict weight at 250 cm (implausibly tall)</li>
</ul>

<div class="concept-box">
<h4>Distinguishing Interpolation from Extrapolation</h4>
<p>Suppose data range: 160–180 cm.</p>
<ul>
<li><strong>Predict at 170 cm:</strong> Interpolation (within range, reliable)</li>
<li><strong>Predict at 200 cm:</strong> Extrapolation (outside range, risky)</li>
<li><strong>Predict at 50 cm:</strong> Extrapolation (clearly unrealistic; model breaks down)</li>
</ul>
</div>

<div class="warning-box">
<strong>Caution:</strong> Linear regression assumes the relationship continues as observed. Outside the data range, this assumption may not hold. Always report the data range and caution users about extrapolation.
</div>
"""
    },
    {
        "title": "Residual Diagnostics and Model Assumptions",
        "body": """
<h3>Residual Diagnostics: Checking Regression Assumptions</h3>
<p>Plot residuals versus fitted values (or versus x) to check whether the regression model is appropriate.</p>

<p><strong>1. Linearity:</strong> Residual plot shows no pattern (random scatter)</p>
<ul>
<li>If residuals show a curved pattern, the relationship may not be linear.</li>
<li>Consider transformation or non-linear models.</li>
</ul>

<p><strong>2. Homoscedasticity (Constant Variance):</strong> Residuals have constant variance</p>
<ul>
<li>Residuals should not "fan out" (heteroscedasticity) as fitted values increase.</li>
<li>If variance increases with fitted values, predictions are less reliable for larger x.</li>
</ul>

<p><strong>3. Normality:</strong> Residuals are approximately normally distributed</p>
<ul>
<li>Check with a Q-Q plot or histogram of residuals.</li>
<li>Minor deviations are usually acceptable with large samples.</li>
</ul>

<p><strong>4. Independence:</strong> Observations are independent</p>
<ul>
<li>Depends on study design, not on data analysis.</li>
<li>Ensure data collection method ensures independence.</li>
</ul>

<div class="warning-box">
<strong>If Assumptions Are Violated:</strong> The regression line may not be appropriate, and predictions may be unreliable. Consider:
<ul>
<li>Transforming variables (log, square root)</li>
<li>Using a non-linear model (polynomial, exponential)</li>
<li>Using robust regression methods</li>
<li>Examining the data for data entry errors or measurement issues</li>
</ul>
</div>

<h3>Influential Points and Outliers</h3>

<p><strong>Outlier:</strong> An observation with a y value far from the regression line (large residual)</p>
<ul>
<li>May indicate a data entry error, special case, or genuine observation</li>
<li>Has a large residual but may not affect the regression line if x is typical</li>
</ul>

<p><strong>Influential point:</strong> An observation that significantly changes the regression line if removed</p>
<ul>
<li>Often has an unusual x value (far from $\\bar{x}$)</li>
<li>Can have a small residual but large impact on the fitted line</li>
</ul>

<div class="worked-example">
<h4>Worked Example: Detecting Outliers and Influential Points</h4>
<p>Height-weight data includes a student with height 165 cm but weight 120 kg (very heavy for height).</p>
<ul>
<li><strong>Is it an outlier?</strong> Yes, the residual is large (actual weight far above predicted).</li>
<li><strong>Is it influential?</strong> Probably not, because x = 165 is near $\\bar{x}$. Other points with similar heights would balance its effect.</li>
<li><strong>Action:</strong> Report results with and without this observation to assess sensitivity.</li>
</ul>

<p>Compare to another observation with height 200 cm (unusual) and weight 140 kg. Even if the residual is small, it could be influential because x = 200 is far from $\\bar{x}$.</p>
</div>

<h3>Strategies for Handling Outliers</h3>
<ul>
<li><strong>Investigate:</strong> Is it a data entry error, measurement error, or genuine special case?</li>
<li><strong>Report both:</strong> Provide regression results with and without the outlier.</li>
<li><strong>Document:</strong> Explain why the outlier was included or excluded.</li>
<li><strong>Robust methods:</strong> Use robust regression or other methods less sensitive to outliers.</li>
</ul>
"""
    },
    {
        "title": "Limitations of Linear Regression",
        "body": """
<h3>When Linear Regression May Not Be Appropriate</h3>

<ul>
<li><strong>Non-linear relationship:</strong> Assumes linear relationship. Scatter plot and residual plots will reveal if data is curved.</li>
<li><strong>Outliers and influential points:</strong> Sensitive to extreme values and unusual observations.</li>
<li><strong>Predictions outside data range:</strong> Extrapolation is unreliable; relationship may not extend beyond observed x values.</li>
<li><strong>Correlation ≠ causation:</strong> Regression describes association, not causation. Don't infer cause from regression alone.</li>
<li><strong>Confounding variables:</strong> A third variable may be the true driver of the relationship.</li>
</ul>

<h3>Key Limitations to Remember</h3>

<div class="success-box">
<strong>Summary of Limitations:</strong>
<ul>
<li>Check scatter plot for linearity before fitting.</li>
<li>Always examine residual plots to validate assumptions.</li>
<li>Use regression for interpolation; extrapolation is risky.</li>
<li>Report r² and standard error of estimate to convey uncertainty.</li>
<li>Consider alternative explanations and confounders.</li>
</ul>
</div>
"""
    }
]
