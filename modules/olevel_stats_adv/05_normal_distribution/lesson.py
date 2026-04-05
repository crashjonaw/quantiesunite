TITLE = "The Normal Distribution: The Bell Curve and Its Power"

SECTIONS = [
    {
        "title": "Why the Normal Distribution Matters",
        "body": """
        <h3>The Most Important Distribution in Statistics</h3>
        <p>The <strong>normal distribution</strong> (also called the Gaussian distribution or bell curve) is the foundation of much of statistics. Why is it so important?</p>

        <p>Many real-world phenomena are normally distributed:</p>
        <ul>
            <li>Human heights and weights</li>
            <li>Test scores</li>
            <li>Measurement errors</li>
            <li>IQ scores</li>
            <li>Biological characteristics</li>
            <li>Manufacturing tolerances</li>
        </ul>

        <p>Because so much data follows this pattern, understanding the normal distribution unlocks powerful insights and predictions.</p>

        <h4>What Makes Data "Normal"?</h4>
        <p>A normal distribution has these characteristic properties:</p>

        <div class="concept-box">
            <ol>
                <li><strong>Bell-shaped:</strong> Most values cluster near the center; fewer values at the extremes</li>
                <li><strong>Symmetric:</strong> The left and right halves are mirror images</li>
                <li><strong>Single peak:</strong> One mode (most common value) at the center</li>
                <li><strong>Mean = Median = Mode:</strong> All three measures of center coincide</li>
                <li><strong>Described by two parameters:</strong> The mean (μ) and standard deviation (σ) completely determine the shape</li>
            </ol>
        </div>

        <h4>Why Symmetric?</h4>
        <p>The symmetry of a normal distribution reflects a fundamental principle: random variations are equally likely to go above or below the mean. There's no built-in bias toward high or low values.</p>

        <h4>Visual Understanding</h4>
        <p>Picture a bell curve:</p>
        <ul>
            <li>The <strong>peak</strong> is at the mean (μ)</li>
            <li>The curve widens as you move away from the mean (showing more variability)</li>
            <li>The curve approaches (but never touches) the x-axis at the extremes</li>
            <li>The curve drops off faster if σ is small (tight cluster) or slower if σ is large (wide spread)</li>
        </ul>

        <div class="success-box">
            <p><strong>Key Insight:</strong> A normal distribution is completely determined by just two numbers: its mean and standard deviation. Once you know these, you can predict what proportion of data falls in any range.</p>
        </div>
        """
    },
    {
        "title": "The Empirical Rule: 68-95-99.7",
        "body": """
        <h3>The Most Useful Rule in Statistics</h3>
        <p>For any data that follows a normal distribution, there's a simple rule that lets us make powerful predictions without complex calculations.</p>

        <div class="concept-box">
            <p><strong>The Empirical Rule (68-95-99.7 Rule):</strong></p>
            <ul>
                <li>Approximately <strong>68%</strong> of data falls within <strong>1 standard deviation</strong> of the mean: [μ − σ, μ + σ]</li>
                <li>Approximately <strong>95%</strong> of data falls within <strong>2 standard deviations</strong> of the mean: [μ − 2σ, μ + 2σ]</li>
                <li>Approximately <strong>99.7%</strong> of data falls within <strong>3 standard deviations</strong> of the mean: [μ − 3σ, μ + 3σ]</li>
            </ul>
        </div>

        <p>This means:</p>
        <ul>
            <li>About 32% of data is outside 1σ (16% on each tail)</li>
            <li>About 5% of data is outside 2σ (2.5% on each tail)</li>
            <li>About 0.3% of data is outside 3σ (0.15% on each tail)</li>
        </ul>

        <h4>Why This Matters: Real-World Examples</h4>

        <div class="worked-example">
            <p><strong>Example 1: Human Heights</strong></p>
            <p>Heights are normally distributed with mean 170 cm and standard deviation 5 cm.</p>
            <ul>
                <li>1σ range: [165, 175] cm → 68% of people are between 165 and 175 cm</li>
                <li>2σ range: [160, 180] cm → 95% of people are between 160 and 180 cm</li>
                <li>3σ range: [155, 185] cm → 99.7% of people are between 155 and 185 cm</li>
            </ul>
            <p><strong>Practical insight:</strong> Only 0.3% of people are shorter than 155 cm or taller than 185 cm. These heights are exceptional.</p>
        </div>

        <div class="worked-example">
            <p><strong>Example 2: Test Scores</strong></p>
            <p>Test scores are normally distributed with mean 75 and standard deviation 10.</p>
            <p><strong>Question:</strong> What proportion of students score between 65 and 85?</p>
            <p><strong>Solution:</strong></p>
            <ul>
                <li>65 = 75 − 10 = μ − σ (one SD below mean)</li>
                <li>85 = 75 + 10 = μ + σ (one SD above mean)</li>
                <li>By the empirical rule, 68% score in this range</li>
            </ul>
        </div>

        <div class="worked-example">
            <p><strong>Example 3: Finding Extreme Values</strong></p>
            <p>Test scores: mean 75, SD 10. What percentage score above 95?</p>
            <p><strong>Solution:</strong></p>
            <ul>
                <li>95 = 75 + 20 = 75 + 2(10) = μ + 2σ (two SDs above mean)</li>
                <li>By the empirical rule, 95% of scores fall in [μ − 2σ, μ + 2σ] = [55, 95]</li>
                <li>So 5% fall outside this range</li>
                <li>By symmetry, 2.5% fall above 95</li>
            </ul>
        </div>

        <h4>Pictorial Understanding</h4>
        <p>Imagine the bell curve with vertical lines at μ ± σ, μ ± 2σ, and μ ± 3σ:</p>
        <pre style="padding: 15px; border-radius: 5px; font-size: 12px">
                            Area under curve:
         .68 (68%)         .95 (95%)        .997 (99.7%)
        ‾ ‾ ‾ ‾ ‾           ‾ ‾ ‾ ‾ ‾        ‾ ‾ ‾ ‾ ‾ ‾
          |‾‾‾|               |‾‾‾‾‾|        |‾‾‾‾‾‾‾‾|
    ···┬─────────┬···    ···┬─────────────┬···  ···┬───────────────┬···
   -3σ -2σ -1σ 0 1σ 2σ 3σ
         μ
        </pre>

        <h4>When to Use the Empirical Rule</h4>
        <p>Use this rule when:</p>
        <ul>
            <li>Data is normally distributed (or approximately so)</li>
            <li>You know the mean and standard deviation</li>
            <li>You want a quick estimate (you don't need extreme precision)</li>
        </ul>

        <div class="warning-box">
            <p><strong>Important Caveat:</strong> The empirical rule applies to normal distributions. If your data is skewed, multimodal, or has heavy outliers, this rule won't work as stated.</p>
        </div>

        <div class="success-box">
            <p><strong>Why 68-95-99.7?</strong> These aren't arbitrary numbers. They come from the mathematical properties of the normal distribution curve and are derived from calculus. They've been verified empirically for centuries across countless datasets.</p>
        </div>
        """
    },
    {
        "title": "Using the Empirical Rule: Problem-Solving",
        "body": """
        <h3>From Theory to Practice</h3>
        <p>Now let's solve various problems using the empirical rule. The key is to:</p>
        <ol>
            <li>Identify the mean (μ) and standard deviation (σ)</li>
            <li>Express the range in terms of σ (how many standard deviations from the mean?)</li>
            <li>Apply the empirical rule</li>
        </ol>

        <h4>Problem Type 1: Finding a Percentage Within a Range</h4>

        <div class="worked-example">
            <p><strong>Problem:</strong> Weights are normally distributed with mean 70 kg and SD 5 kg. What percentage of people weigh between 60 and 80 kg?</p>
            <p><strong>Solution:</strong></p>
            <ul>
                <li>60 kg = 70 − 10 = 70 − 2(5) = μ − 2σ</li>
                <li>80 kg = 70 + 10 = 70 + 2(5) = μ + 2σ</li>
                <li>This is the range [μ − 2σ, μ + 2σ]</li>
                <li>By the empirical rule, 95% fall in this range</li>
                <li><strong>Answer: 95%</strong></li>
            </ul>
        </div>

        <h4>Problem Type 2: Finding Percentages in Tails</h4>

        <div class="worked-example">
            <p><strong>Problem:</strong> IQ scores are normally distributed with mean 100 and SD 15. What percentage have IQ above 130?</p>
            <p><strong>Solution:</strong></p>
            <ul>
                <li>130 = 100 + 30 = 100 + 2(15) = μ + 2σ</li>
                <li>The empirical rule tells us 95% fall in [μ − 2σ, μ + 2σ] = [70, 130]</li>
                <li>So 5% fall outside this range</li>
                <li>By symmetry, half of that 5% is above 130</li>
                <li>5% ÷ 2 = 2.5%</li>
                <li><strong>Answer: 2.5%</strong></li>
            </ul>
        </div>

        <h4>Problem Type 3: Multi-Step Problems</h4>

        <div class="worked-example">
            <p><strong>Problem:</strong> Test scores are normally distributed with mean 80 and SD 8. What percentage score between 72 and 96?</p>
            <p><strong>Solution:</strong></p>
            <ul>
                <li>72 = 80 − 8 = μ − σ (one SD below mean)</li>
                <li>96 = 80 + 16 = 80 + 2(8) = μ + 2σ (two SDs above mean)</li>
                <li>This is NOT a symmetric range, so we can't use 68% or 95% directly</li>
                <li>We need to add portions:
                    <ul>
                        <li>From μ − σ to μ: This is half of the 68% (the lower half of the 1σ interval) = 34%</li>
                        <li>From μ to μ + 2σ: This includes the upper half of the 1σ interval (34%) plus the area from 1σ to 2σ</li>
                        <li>The area between 1σ and 2σ is (95% − 68%) ÷ 2 = 27% ÷ 2 = 13.5%</li>
                        <li>So from μ to μ + 2σ is 34% + 13.5% = 47.5%</li>
                    </ul>
                </li>
                <li>Total: 34% + 47.5% = 81.5%</li>
                <li><strong>Answer: 81.5%</strong></li>
            </ul>
        </div>

        <div class="worked-example">
            <p><strong>Problem:</strong> Battery lifetimes are normally distributed with mean 500 hours and SD 25 hours. What percentage fail within the first 450 hours?</p>
            <p><strong>Solution:</strong></p>
            <ul>
                <li>450 = 500 − 50 = 500 − 2(25) = μ − 2σ</li>
                <li>By the empirical rule, 95% of batteries last between 450 and 550 hours</li>
                <li>So 5% fail before 450 hours or after 550 hours</li>
                <li>By symmetry, 2.5% fail before 450 hours</li>
                <li><strong>Answer: 2.5%</strong></li>
            </ul>
        </div>

        <h4>Mental Model: The 68-95-99.7 Diagram</h4>
        <p>Memorize this breakdown:</p>
        <pre style="padding: 15px; border-radius: 5px; font-size: 11px">
        −3σ to −2σ: 2.35%
        −2σ to −1σ: 13.5%
        −1σ to 0:   34%     | Within 1σ (±): 68%
         0 to +1σ:  34%     |
        +1σ to +2σ: 13.5%   |
        +2σ to +3σ: 2.35%   | Within 2σ (±): 95%
        Beyond +3σ: 0.15%   |
        </pre>

        <h4>Practice Strategy</h4>
        <p>For any problem:</p>
        <ol>
            <li>Write out the mean and SD clearly</li>
            <li>Mark the boundary values on your mental bell curve</li>
            <li>Count how many SDs away from the mean</li>
            <li>Use the empirical rule percentages</li>
            <li>Add/subtract as needed</li>
        </ol>

        <div class="success-box">
            <p><strong>Mastery Tip:</strong> Draw a simple sketch of the bell curve for each problem, even if it's rough. Mark the mean and the σ boundaries. This visual reference prevents mistakes.</p>
        </div>
        """
    },
    {
        "title": "Normal Distribution in Context: When and Why It Applies",
        "body": """
        <h3>Is Your Data Actually Normal?</h3>
        <p>The empirical rule and normal distribution techniques are powerful, but they only work if your data actually follows a normal distribution. How do you know?</p>

        <h4>Signs That Data Might Be Normal</h4>
        <ul>
            <li>Histogram is roughly bell-shaped and symmetric</li>
            <li>Mean ≈ Median (difference is small relative to SD)</li>
            <li>Box plot is roughly symmetric (median line centered in box)</li>
            <li>Data comes from a process known to produce normal distributions (e.g., human heights, test scores)</li>
            <li>Large sample size (by the Central Limit Theorem, sample means tend to be normal)</li>
        </ul>

        <h4>Red Flags: Data Is NOT Normal</h4>
        <ul>
            <li>Histogram is clearly skewed or multi-peaked</li>
            <li>Mean is substantially different from median</li>
            <li>Extreme outliers (beyond 3σ but numerous)</li>
            <li>Data is bounded (e.g., percentages 0–100%, grades on a curved scale)</li>
        </ul>

        <div class="worked-example">
            <p><strong>Example: Income Distribution</strong></p>
            <p>Income in a country is NOT normally distributed. It's right-skewed: a few very high earners and many more low earners create a tail to the right. The median income is much less than the mean. The empirical rule would give wrong predictions here.</p>
        </div>

        <h4>When to Use Normal Distribution Methods</h4>

        <p><strong>✓ Appropriate:</strong></p>
        <ul>
            <li>Heights, weights of populations</li>
            <li>Test scores (when well-designed)</li>
            <li>Manufacturing measurements (when process is stable)</li>
            <li>Errors and deviations</li>
            <li>Biological measurements</li>
        </ul>

        <p><strong>✗ Inappropriate:</strong></p>
        <ul>
            <li>Income or wealth (highly skewed)</li>
            <li>Counts of rare events</li>
            <li>Reaction times (bounded at zero)</li>
            <li>Test scores when many students max out or fail badly</li>
        </ul>

        <h4>The Central Limit Theorem: Why Normal is So Common</h4>
        <p>A remarkable mathematical principle explains why normal distributions are so prevalent:</p>

        <div class="concept-box">
            <p><strong>Central Limit Theorem (Simplified):</strong> If you take many samples from ANY distribution and calculate the mean of each sample, those sample means will be approximately normally distributed, even if the original data isn't normal.</p>
        </div>

        <p>This is profound! It means:</p>
        <ul>
            <li>Sample averages tend to follow a normal distribution</li>
            <li>This explains why test scores (averages of many small skills) are often normal</li>
            <li>It's why normal distributions appear in so many real situations</li>
        </ul>

        <h4>Best Practices</h4>
        <ol>
            <li>Always look at a histogram or sketch before assuming normality</li>
            <li>Compare mean and median; if they differ significantly, question normality</li>
            <li>Use box plots to check symmetry</li>
            <li>If unsure, use IQR and the five-number summary (these don't assume normality) instead of relying on the empirical rule</li>
            <li>Remember: The empirical rule is a tool, not a law. It works when the assumption of normality is reasonable.</li>
        </ol>

        <div class="success-box">
            <p><strong>Final Insight:</strong> Statistics is about making sound inferences from data. The normal distribution is a powerful model, but like all models, it's an approximation. Use it wisely, check your assumptions, and don't blindly apply it where it doesn't fit.</p>
        </div>
        """
    }
]
