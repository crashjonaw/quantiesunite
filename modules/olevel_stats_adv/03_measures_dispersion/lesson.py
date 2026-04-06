TITLE = "Measures of Dispersion: Quantifying Data Spread"

SECTIONS = [
    {
        "title": "Why Spread Matters: Beyond the Average",
        "body": """
        <h3>The Problem with Averages Alone</h3>
        <p>Two datasets can have the same mean but look very different. Consider:</p>
        <ul>
            <li><strong>Class A test scores:</strong> 75, 76, 77, 78, 79 (mean = 77)</li>
            <li><strong>Class B test scores:</strong> 50, 60, 77, 90, 98 (mean = 75)</li>
        </ul>

        <p>Class A has a mean of 77 and very consistent scores. Class B has a similar mean but wildly inconsistent scores. A teacher would draw very different conclusions about these two classes!</p>

        <div class="concept-box">
            <p><strong>Dispersion</strong> measures how spread out data is from the center. It answers: "Are all values clustered tightly near the mean, or are they scattered widely?"</p>
        </div>

        <h4>Why Study Dispersion?</h4>
        <ul>
            <li><strong>Consistency:</strong> Lower dispersion = more predictable, stable data</li>
            <li><strong>Reliability:</strong> Manufacturing wants low dispersion (consistent products)</li>
            <li><strong>Risk:</strong> Investment portfolios with high dispersion are riskier</li>
            <li><strong>Comparison:</strong> Compare which of two groups is more homogeneous</li>
        </ul>

        <p>Now let's learn four key measures of dispersion, from simplest to most sophisticated.</p>
        """
    },
    {
        "title": "Range and Interquartile Range (IQR)",
        "body": """
        <h3>Simple Measures: Range and IQR</h3>

        <h4>Range: The Simplest Measure</h4>
        <p><strong>Range = Maximum Value − Minimum Value</strong></p>

        <p>The range is intuitive and easy to calculate, but it has a critical flaw: it depends only on the two extreme values.</p>

        <div class="worked-example">
            <p><strong>Example:</strong> Data: 2, 5, 7, 9, 11, 13, 15, 17, 19</p>
            <p>Range = 19 − 2 = 17</p>
            <p>But if there's an outlier at 100, the range becomes 100 − 2 = 98, even though most data is still tightly clustered.</p>
        </div>

        <div class="warning-box">
            <p><strong>Limitation of Range:</strong> A single extreme outlier can drastically inflate the range, making it a poor indicator of typical spread.</p>
        </div>

        <h4>Interquartile Range (IQR): A More Robust Measure</h4>
        <p><strong>IQR = Q₃ − Q₁</strong></p>

        <p>The IQR measures the spread of the <strong>middle 50%</strong> of data. It ignores the bottom 25% and top 25%, making it much less sensitive to outliers.</p>

        <div class="concept-box">
            <p><strong>Why IQR is Better:</strong> IQR focuses on the central bulk of the data. Extreme outliers don't affect it because they're already outside Q₁ and Q₃.</p>
        </div>

        <div class="worked-example">
            <p><strong>Example:</strong> Using our five-number summary (2, 6, 11, 16, 19)</p>
            <p>IQR = 16 − 6 = 10</p>
            <p>This tells us that the middle 50% of students' heights span 10 cm. Even if we had a very tall outlier at 250 cm, the IQR would stay at 10 because Q₁ and Q₃ are unaffected.</p>
        </div>

        <h4>Range vs IQR: When to Use Each</h4>
        <ul>
            <li><strong>Use Range when:</strong> You need a quick, simple measure; data has no outliers</li>
            <li><strong>Use IQR when:</strong> You want a robust measure; data may contain outliers; you care about the central distribution</li>
        </ul>

        <div class="success-box">
            <p><strong>In Practice:</strong> Professional statisticians nearly always prefer IQR over range because it's more reliable and interpretable.</p>
        </div>
        """
    },
    {
        "title": "Variance and Standard Deviation",
        "body": """
        <h3>Understanding How Far Values Deviate from the Mean</h3>
        <p>Range and IQR tell us the span of data, but they don't use all the information available. <strong>Variance</strong> and <strong>standard deviation</strong> consider every single value's distance from the mean.</p>

        <h4>The Concept: Deviations from the Mean</h4>
        <p>First, let's understand "deviation":</p>
        <ul>
            <li><strong>Deviation</strong> = (value − mean)</li>
            <li>If a student scores 82 and the class mean is 75, their deviation is 82 − 75 = 7</li>
            <li>If a student scores 65, their deviation is 65 − 75 = −10</li>
        </ul>

        <p>We want to measure the "average deviation," but deviations above the mean are positive and below are negative, so they cancel out. The solution: <strong>square the deviations.</strong></p>

        <h4>Variance: Average Squared Deviation</h4>

        <div class="concept-box">
            <p><strong>Population Variance:</strong> \\(\\sigma^2 = \\frac{\\sum(x - \\mu)^2}{n}\\)</p>
            <p><strong>Sample Variance:</strong> \\(s^2 = \\frac{\\sum(x - \\bar{x})^2}{n - 1}\\)</p>
            <p>where \\(\\mu\\) is the population mean, \\(\\bar{x}\\) is the sample mean, and \\(n\\) is the sample size</p>
        </div>

        <p>Units of variance are squared (e.g., cm² for height). This is hard to interpret intuitively, so we take the square root to get standard deviation.</p>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Data: 2, 4, 6, 8, 10</p>
            <p><strong>Step 1:</strong> Find the mean: (2+4+6+8+10)/5 = 30/5 = 6</p>
            <p><strong>Step 2:</strong> Calculate deviations and square them:</p>
            <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
                <tr >
                    <td style="padding: 10px;">x</td>
                    <td style="padding: 10px;">x − 6</td>
                    <td style="padding: 10px;">(x − 6)²</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">2</td>
                    <td style="padding: 10px;">−4</td>
                    <td style="padding: 10px;">16</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">4</td>
                    <td style="padding: 10px;">−2</td>
                    <td style="padding: 10px;">4</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">6</td>
                    <td style="padding: 10px;">0</td>
                    <td style="padding: 10px;">0</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">8</td>
                    <td style="padding: 10px;">2</td>
                    <td style="padding: 10px;">4</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">10</td>
                    <td style="padding: 10px;">4</td>
                    <td style="padding: 10px;">16</td>
                </tr>
            </table>
            <p><strong>Step 3:</strong> Sum the squared deviations: 16 + 4 + 0 + 4 + 16 = 40</p>
            <p><strong>Step 4:</strong> Divide by n (population) or n−1 (sample): 40/5 = 8</p>
            <p><strong>Variance σ² = 8</strong></p>
        </div>

        <h4>Standard Deviation: Taking the Square Root</h4>

        <div class="concept-box">
            <p><strong>Standard Deviation:</strong> \\(\\sigma = \\sqrt{\\sigma^2}\\)</p>
        </div>

        <p>Standard deviation brings units back to the original scale. If variance is in cm², standard deviation is in cm.</p>

        <div class="worked-example">
            <p><strong>Continuing our example:</strong></p>
            <p>\\(\\sigma = \\sqrt{8} \\approx 2.83\\)</p>
            <p>This means, on average, values deviate from the mean (6) by about 2.83 units.</p>
        </div>

        <h4>Interpreting Standard Deviation</h4>
        <ul>
            <li><strong>Small σ:</strong> Data clustered tightly around the mean (consistent, predictable)</li>
            <li><strong>Large σ:</strong> Data scattered widely (variable, unpredictable)</li>
            <li><strong>σ = 0:</strong> All values are identical</li>
        </ul>

        <div class="success-box">
            <p><strong>Standard Deviation in Context:</strong> For normally distributed data, approximately 68% of values fall within one standard deviation of the mean (covered in the Normal Distribution section).</p>
        </div>

        <h4>Population vs Sample Variance: Why n−1?</h4>
        <p>We divide by (n−1) for sample variance, not n. Why? Samples tend to underestimate variation in the population, so (n−1) is a correction factor that gives us a more accurate (unbiased) estimate. This is called <strong>Bessel's correction.</strong></p>

        <div class="warning-box">
            <p><strong>Important:</strong> Use n−1 when calculating standard deviation from sample data. Use n only when you have the entire population.</p>
        </div>
        """
    },
    {
        "title": "Coefficient of Variation and Comparing Spreads",
        "body": """
        <h3>Comparing Variability Across Different Scales</h3>
        <p>Standard deviation has units (e.g., cm, kg, pounds). This makes it hard to compare spread across variables with different units or vastly different magnitudes.</p>

        <div class="worked-example">
            <p><strong>Problem:</strong></p>
            <p>Heights: mean = 170 cm, SD = 10 cm</p>
            <p>Weights: mean = 70 kg, SD = 5 kg</p>
            <p>Question: Which is more variable, height or weight?</p>
            <p>If we compare raw SD (10 vs 5), weight looks less variable. But the first is in cm and the second in kg — we're comparing apples to oranges!</p>
        </div>

        <h4>Coefficient of Variation: A Unitless Measure</h4>

        <div class="concept-box">
            <p><strong>Coefficient of Variation (CV):</strong></p>
            <p style="text-align: center;">\\(CV = \\frac{\\text{Standard Deviation}}{\\text{Mean}} \\times 100\\%\\)</p>
        </div>

        <p>CV expresses standard deviation as a percentage of the mean, making it unitless and comparable across different scales.</p>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> From our 2, 4, 6, 8, 10 dataset</p>
            <p>Mean \\(= 6\\), SD \\(\\approx 2.83\\)</p>
            <p>\\(CV = \\frac{2.83}{6} \\times 100\\% \\approx 47.2\\%\\)</p>
            <p>This means the standard deviation is about 47% of the mean.</p>
        </div>

        <div class="worked-example">
            <p><strong>Worked Example Continued:</strong> Height vs Weight</p>
            <p>Heights: \\(CV = \\frac{10}{170} \\times 100\\% \\approx 5.9\\%\\)</p>
            <p>Weights: \\(CV = \\frac{5}{70} \\times 100\\% \\approx 7.1\\%\\)</p>
            <p>Now we can fairly compare: weight is slightly more variable (7.1%) than height (5.9%).</p>
        </div>

        <h4>When to Use CV</h4>
        <ul>
            <li>Comparing variability across variables with different units (price in dollars vs. quantity in units)</li>
            <li>Comparing variability across datasets with different means (small dataset: mean 10 vs. large dataset: mean 1000)</li>
            <li>Assessing the quality of measurements (lower CV = more precise measuring technique)</li>
        </ul>

        <h4>Summary Table: When to Use Which Measure</h4>
        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
            <tr >
                <td style="padding: 10px;"><strong>Measure</strong></td>
                <td style="padding: 10px;"><strong>Formula</strong></td>
                <td style="padding: 10px;"><strong>When to Use</strong></td>
            </tr>
            <tr >
                <td style="padding: 10px;">Range</td>
                <td style="padding: 10px;">Max − Min</td>
                <td style="padding: 10px;">Quick overview, no outliers</td>
            </tr>
            <tr >
                <td style="padding: 10px;">IQR</td>
                <td style="padding: 10px;">Q₃ − Q₁</td>
                <td style="padding: 10px;">Robust measure, handles outliers</td>
            </tr>
            <tr >
                <td style="padding: 10px;">Variance</td>
                <td style="padding: 10px;">\\(\\sigma^2 = \\frac{\\sum(x-\\mu)^2}{n}\\)</td>
                <td style="padding: 10px;">Mathematical/theoretical work</td>
            </tr>
            <tr >
                <td style="padding: 10px;">Std Dev</td>
                <td style="padding: 10px;">\\(\\sigma = \\sqrt{\\sigma^2}\\)</td>
                <td style="padding: 10px;">Same units as data; most interpretable</td>
            </tr>
            <tr >
                <td style="padding: 10px;">CV</td>
                <td style="padding: 10px;">\\((\\sigma/\\mu) \\times 100\\%\\)</td>
                <td style="padding: 10px;">Comparing spreads across different scales</td>
            </tr>
        </table>

        <div class="success-box">
            <p><strong>Best Practice:</strong> Report both the mean/median AND a measure of spread (usually standard deviation or IQR). Never report an average without its variability — it tells an incomplete story.</p>
        </div>
        """
    }
]
