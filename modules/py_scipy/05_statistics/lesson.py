"""Statistics - Probability Distributions, Inference, and Hypothesis Testing"""

TITLE = "Statistics: Distributions, Inference, and Hypothesis Tests"

SECTIONS = [
    {
        "id": "py_scipy_stats_01",
        "title": "Probability Distributions",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Understanding Probability Distributions</h3>
        <p>A probability distribution describes the likelihood of different outcomes. scipy.stats provides 100+ distributions with methods for sampling, computing probabilities, and estimating parameters.</p>

        <h4>Universal Distribution Interface</h4>
        <p>All distributions in scipy.stats follow a consistent API:</p>
        <ul>
            <li><strong>pdf(x):</strong> Probability density function at x (for continuous distributions)</li>
            <li><strong>pmf(k):</strong> Probability mass function at k (for discrete distributions)</li>
            <li><strong>cdf(x):</strong> Cumulative distribution function P(X ≤ x)</li>
            <li><strong>sf(x):</strong> Survival function P(X > x) = 1 - cdf(x)</li>
            <li><strong>ppf(q):</strong> Percent point function (inverse CDF, quantiles)</li>
            <li><strong>rvs():</strong> Random variable samples</li>
            <li><strong>fit(data):</strong> Estimate parameters from data (MLE)</li>
        </ul>

        <h4>Common Distributions</h4>
        <ul>
            <li><strong>norm:</strong> Normal/Gaussian distribution (location, scale)</li>
            <li><strong>uniform:</strong> Uniform distribution (a, b)</li>
            <li><strong>expon:</strong> Exponential distribution (scale parameter)</li>
            <li><strong>binom:</strong> Binomial distribution (n trials, p success)</li>
            <li><strong>poisson:</strong> Poisson distribution (mean count)</li>
            <li><strong>chi2:</strong> Chi-squared (k degrees of freedom)</li>
            <li><strong>t:</strong> Student's t-distribution</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Working with the Normal Distribution</h4>
        <pre class="code-block">
import numpy as np
from scipy.stats import norm

# Define a normal distribution: μ=100, σ=15 (like IQ scores)
dist = norm(loc=100, scale=15)

# Probability density at x=100
pdf_at_mean = dist.pdf(100)
print(f"PDF at mean (100): {pdf_at_mean:.6f}")

# Cumulative probability: P(X ≤ 115)
prob_le_115 = dist.cdf(115)
print(f"P(X ≤ 115) = {prob_le_115:.6f}")

# Quantiles: find x such that P(X ≤ x) = 0.95
x_95th = dist.ppf(0.95)
print(f"95th percentile: {x_95th:.2f}")

# Generate random samples
samples = dist.rvs(size=1000)
print(f"Sample mean: {samples.mean():.2f}, Sample std: {samples.std():.2f}")

# Fit parameters to data
data = np.random.normal(105, 12, 100)
params = norm.fit(data)
print(f"Estimated μ={params[0]:.2f}, σ={params[1]:.2f}")
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: Vectorized Operations</h4>
        <p>All distribution methods accept arrays, not just scalars. This allows computing PDFs/CDFs for many values simultaneously.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_stats_02",
        "title": "Statistical Tests and Hypothesis Testing",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Hypothesis Testing Framework</h3>
        <p>Hypothesis testing uses data to evaluate claims. A test produces a p-value: the probability of observing the data if the null hypothesis were true. Small p-values suggest the null hypothesis is unlikely.</p>

        <h4>Key Concepts</h4>
        <ul>
            <li><strong>Null Hypothesis (H₀):</strong> Default assumption (usually no effect)</li>
            <li><strong>Alternative Hypothesis (H₁):</strong> What we're testing for</li>
            <li><strong>p-value:</strong> Probability of data under H₀. Small (< 0.05) means reject H₀.</li>
            <li><strong>Type I Error:</strong> Rejecting true null hypothesis (false positive)</li>
            <li><strong>Type II Error:</strong> Failing to reject false null hypothesis (false negative)</li>
        </ul>

        <h4>Common Tests in scipy.stats</h4>
        <ul>
            <li><strong>ttest_ind:</strong> Compare means of two independent samples</li>
            <li><strong>ttest_rel:</strong> Compare means of paired samples</li>
            <li><strong>mannwhitneyu:</strong> Non-parametric alternative to t-test</li>
            <li><strong>chi2_contingency:</strong> Test independence in categorical data</li>
            <li><strong>shapiro:</strong> Test for normality</li>
            <li><strong>levene:</strong> Test equality of variances</li>
            <li><strong>f_oneway:</strong> ANOVA for multiple groups</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Two-Sample t-Test</h4>
        <pre class="code-block">
import numpy as np
from scipy.stats import ttest_ind, shapiro

# Test if two treatment groups differ in mean response
control = np.array([2.1, 2.4, 2.6, 1.9, 2.2])
treatment = np.array([3.1, 2.9, 3.4, 3.2, 3.3])

# Check assumptions: are data normally distributed?
_, p_control = shapiro(control)
_, p_treatment = shapiro(treatment)
print(f"Normality test p-values: control={p_control:.3f}, treatment={p_treatment:.3f}")

# Two-sample t-test
# H₀: μ_control = μ_treatment
# H₁: μ_control ≠ μ_treatment
t_stat, p_value = ttest_ind(control, treatment)

print(f"\nTwo-sample t-test:")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Significant at α=0.05: {p_value < 0.05}")

# Effect size (Cohen's d)
pooled_std = np.sqrt((np.var(control, ddof=1) + np.var(treatment, ddof=1)) / 2)
cohens_d = (treatment.mean() - control.mean()) / pooled_std
print(f"Cohen's d (effect size): {cohens_d:.4f}")
        </pre>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Common Misinterpretation</h4>
        <p>p-value is NOT the probability that H₀ is true. It's P(data | H₀). A low p-value doesn't prove H₁; it just says the data would be unlikely under H₀.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_stats_03",
        "title": "Descriptive Statistics and Correlation",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Summarizing Data: Descriptive Statistics</h3>
        <p>Descriptive statistics summarize datasets using central tendency (mean, median), spread (std, IQR), and relationships (correlation, covariance).</p>

        <h4>Location and Spread Measures</h4>
        <ul>
            <li><strong>Mean/Median:</strong> Center of data. Mean affected by outliers; median robust.</li>
            <li><strong>Variance/Std Dev:</strong> Spread around center. Sensitive to outliers.</li>
            <li><strong>IQR (Interquartile Range):</strong> Distance between 25th and 75th percentiles. Robust.</li>
            <li><strong>Skewness:</strong> Asymmetry of distribution</li>
            <li><strong>Kurtosis:</strong> Tail heaviness (propensity for outliers)</li>
        </ul>

        <h4>Correlation Measures</h4>
        <ul>
            <li><strong>Pearson r:</strong> Linear correlation (-1 to 1). Assumes bivariate normality.</li>
            <li><strong>Spearman ρ:</strong> Rank correlation. Non-parametric, robust to outliers.</li>
            <li><strong>Kendall τ:</strong> Rank correlation based on concordance. Good for small samples.</li>
        </ul>

        <h4>Key Functions</h4>
        <ul>
            <li><strong>describe:</strong> Returns count, mean, std, min, max, skewness, kurtosis</li>
            <li><strong>pearsonr:</strong> Pearson correlation and p-value</li>
            <li><strong>spearmanr:</strong> Spearman correlation and p-value</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Summary Statistics and Correlation</h4>
        <pre class="code-block">
import numpy as np
from scipy.stats import describe, pearsonr, spearmanr

# Sample data: height and weight
height = np.array([165, 170, 175, 180, 185, 190, 172, 178])  # cm
weight = np.array([60, 65, 75, 80, 90, 95, 68, 82])  # kg

# Descriptive statistics
summary = describe(height)
print("Height statistics:")
print(f"  n={summary.nobs}, mean={summary.mean:.1f}, std={summary.variance**0.5:.1f}")
print(f"  min={summary.minmax[0]}, max={summary.minmax[1]}")
print(f"  skewness={summary.skewness:.3f}, kurtosis={summary.kurtosis:.3f}")

# Pearson correlation (linear relationship)
r_pearson, p_pearson = pearsonr(height, weight)
print(f"\nPearson correlation: r={r_pearson:.4f}, p={p_pearson:.4f}")

# Spearman correlation (rank relationship, robust)
r_spearman, p_spearman = spearmanr(height, weight)
print(f"Spearman correlation: ρ={r_spearman:.4f}, p={p_spearman:.4f}")

# Interpretation
print(f"\nStrong linear relationship: {abs(r_pearson) > 0.7}")
print(f"Significant at α=0.05: {p_pearson < 0.05}")
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: Robust Statistics</h4>
        <p>Use median and IQR instead of mean/std for skewed data or data with outliers. Use Spearman instead of Pearson for non-linear relationships.</p>
    </div>
</div>
        """
    }
]
