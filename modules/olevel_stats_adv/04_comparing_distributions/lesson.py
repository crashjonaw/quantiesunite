TITLE = "Comparing Distributions and Standardization"

SECTIONS = [
    {
        "title": "Comparing Multiple Datasets: A Strategic Approach",
        "body": """
        <h3>When Do We Compare Distributions?</h3>
        <p>In real life, we rarely analyze a single dataset in isolation. We compare:</p>
        <ul>
            <li>Two products (Which is more consistent?)</li>
            <li>Two treatments (Which performs better?)</li>
            <li>Two time periods (Has performance improved?)</li>
            <li>Multiple groups (Are there meaningful differences?)</li>
        </ul>

        <h4>What to Compare: The Key Aspects</h4>
        <p>When comparing two or more distributions, always examine three things:</p>

        <div class="concept-box">
            <ol>
                <li><strong>Location (Central Tendency):</strong> Where is the "center" of each distribution? (mean, median)</li>
                <li><strong>Spread (Dispersion):</strong> How scattered is each distribution? (range, IQR, SD)</li>
                <li><strong>Shape (Skewness/Symmetry):</strong> Is each distribution symmetric or skewed?</li>
            </ol>
        </div>

        <h4>Tools for Comparison</h4>

        <p><strong>1. Summary Statistics</strong></p>
        <p>Calculate and compare:</p>
        <ul>
            <li>Mean and median (location)</li>
            <li>Standard deviation and IQR (spread)</li>
            <li>Range (overall span)</li>
            <li>Five-number summary (shape indicator)</li>
        </ul>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Comparing two classes' test scores</p>
            <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
                <tr >
                    <td style="padding: 10px;"><strong>Statistic</strong></td>
                    <td style="padding: 10px;"><strong>Class A</strong></td>
                    <td style="padding: 10px;"><strong>Class B</strong></td>
                </tr>
                <tr >
                    <td style="padding: 10px;">Mean</td>
                    <td style="padding: 10px;">78</td>
                    <td style="padding: 10px;">74</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">Median</td>
                    <td style="padding: 10px;">79</td>
                    <td style="padding: 10px;">72</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">SD</td>
                    <td style="padding: 10px;">8</td>
                    <td style="padding: 10px;">15</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">IQR</td>
                    <td style="padding: 10px;">10</td>
                    <td style="padding: 10px;">20</td>
                </tr>
            </table>
            <p><strong>Interpretation:</strong></p>
            <ul>
                <li>Class A has a higher mean (78 vs 74) and higher median (79 vs 72) → Class A students perform better on average</li>
                <li>Class A has lower SD (8 vs 15) and lower IQR (10 vs 20) → Class A is more consistent</li>
                <li>Median > mean in Class A (79 > 78) and median < mean in Class B (72 < 74) → Class B is more right-skewed (some low scores)</li>
                <li><strong>Conclusion:</strong> Class A outperforms Class B both in average score and consistency.</li>
            </ul>
        </div>

        <p><strong>2. Visual Comparison: Side-by-Side Box Plots</strong></p>
        <p>Box plots allow instant visual comparison of location, spread, and skewness. (See the Box Plots section for details.)</p>

        <p><strong>3. Back-to-Back Stem and Leaf Plots</strong></p>
        <p>Show both distributions on one plot, making patterns immediately visible.</p>

        <h4>Writing a Comparison Statement</h4>
        <p>When comparing distributions, follow this structure:</p>
        <ol>
            <li>State which dataset has higher/lower location (mean/median)</li>
            <li>Quantify the difference with numbers</li>
            <li>Comment on spread and consistency</li>
            <li>Note any outliers or unusual patterns</li>
            <li>Draw a clear conclusion linked to context</li>
        </ol>

        <div class="worked-example">
            <p><strong>Example comparison statement:</strong></p>
            <p>"Class A students have a higher median score (79 vs 72) and are more consistent in their performance (SD = 8 vs 15). While Class B has some high scorers, it also has more variability, suggesting inconsistent performance. Class A demonstrates superior and more stable achievement."</p>
        </div>
        """
    },
    {
        "title": "Standardization and Z-Scores",
        "body": """
        <h3>The Problem: Comparing Across Different Scales</h3>
        <p>Sometimes we want to compare individual values across different datasets or variables. But the datasets may have different units or different means.</p>

        <div class="worked-example">
            <p><strong>Problem Example:</strong></p>
            <p>Two students take different tests:</p>
            <ul>
                <li>Alice scores 82 on a Math test (class mean = 75, SD = 8)</li>
                <li>Bob scores 88 on a Science test (class mean = 80, SD = 10)</li>
            </ul>
            <p>Who did better relative to their class? We can't just compare 82 vs 88 because the class distributions are different!</p>
        </div>

        <h4>The Solution: Z-Scores (Standardization)</h4>

        <div class="concept-box">
            <p><strong>Z-Score Formula:</strong></p>
            <p style="text-align: center;">z = (x − μ) / σ</p>
            <p>where x is the individual value, μ is the mean, and σ is the standard deviation</p>
        </div>

        <p>A z-score tells you <strong>how many standard deviations a value is from the mean.</strong> It's unitless, making it perfect for comparisons.</p>

        <h4>Interpretation of Z-Scores</h4>
        <ul>
            <li><strong>z = 0:</strong> The value equals the mean</li>
            <li><strong>z = 1:</strong> The value is 1 SD above the mean (good performance)</li>
            <li><strong>z = 2:</strong> The value is 2 SDs above the mean (excellent performance)</li>
            <li><strong>z = −1:</strong> The value is 1 SD below the mean (below average)</li>
            <li><strong>z = −2:</strong> The value is 2 SDs below the mean (poor performance)</li>
        </ul>

        <p>The further z is from 0, the more unusual or extreme the value is within its distribution.</p>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Resolving our comparison problem</p>
            <p><strong>Alice:</strong> z = (82 − 75) / 8 = 7/8 = 0.875</p>
            <p><strong>Bob:</strong> z = (88 − 80) / 10 = 8/10 = 0.8</p>
            <p><strong>Interpretation:</strong> Alice's score is 0.875 standard deviations above her class mean. Bob's score is 0.8 standard deviations above his class mean. Alice performed slightly better relative to her class average.</p>
        </div>

        <div class="worked-example">
            <p><strong>Another Example:</strong> Identifying unusual performances</p>
            <p>Heights are normally distributed with mean 170 cm and SD 5 cm.</p>
            <p>Person A: 185 cm → z = (185 − 170) / 5 = 3 (3 SDs above mean, very tall!)</p>
            <p>Person B: 150 cm → z = (150 − 170) / 5 = −4 (4 SDs below mean, exceptionally short!)</p>
            <p>Person B is more unusual than Person A because |−4| > |3|.</p>
        </div>

        <h4>Why Z-Scores Matter</h4>
        <ul>
            <li>Compare individual performances across different tests/scales</li>
            <li>Identify outliers (z > 3 or z < −3 is typically considered unusual)</li>
            <li>Standardize data for further statistical analysis</li>
            <li>Convert different measurement scales to a common basis</li>
        </ul>

        <div class="success-box">
            <p><strong>Standard Normal Distribution:</strong> When you convert any normally distributed data to z-scores, you get what's called the "standard normal distribution." This has mean 0 and standard deviation 1, making it a universal reference for all normal distributions.</p>
        </div>

        <h4>From Z-Score Back to Raw Score</h4>
        <p>If you know the z-score and want to find the original value:</p>
        <p style="text-align: center;">x = μ + z × σ</p>

        <div class="worked-example">
            <p><strong>Example:</strong> If a student's z-score is 1.5 on a test with mean 70 and SD 10, what was their raw score?</p>
            <p>x = 70 + 1.5 × 10 = 70 + 15 = 85</p>
        </div>
        """
    },
    {
        "title": "Making Evidence-Based Conclusions",
        "body": """
        <h3>From Statistics to Insight</h3>
        <p>Calculating statistics is only half the job. The other half is interpreting those numbers and drawing sound conclusions in context.</p>

        <h4>The Framework for Comparison</h4>
        <p>When you compare two or more distributions, follow this structure:</p>

        <div class="concept-box">
            <ol>
                <li><strong>State the location:</strong> "The median of Group A is 78, while Group B's median is 74..."</li>
                <li><strong>Quantify the difference:</strong> "This is a difference of 4 points..."</li>
                <li><strong>Discuss spread:</strong> "Group A is more consistent (SD = 8 vs 15)..."</li>
                <li><strong>Note shape/outliers:</strong> "Group B shows one unusual low score of 30..."</li>
                <li><strong>Draw a conclusion:</strong> "This suggests Group A has both higher and more stable performance."</li>
            </ol>
        </div>

        <h4>Common Pitfalls to Avoid</h4>

        <p><strong>1. Ignoring Context</strong></p>
        <p>A difference of 4 points might be huge in one context (standardized test scores 0–100) but trivial in another (temperature readings). Always relate your findings to the real-world situation.</p>

        <p><strong>2. Confusing "Average" with "Typical"</strong></p>
        <p>When data is skewed, the mean and median differ. The median is often more representative of a "typical" value because it's not pulled by outliers.</p>

        <p><strong>3. Overlooking Variability</strong></p>
        <p>Two groups might have similar means but very different spreads. The spread often matters more than the center for decision-making.</p>

        <div class="worked-example">
            <p><strong>Real-World Example:</strong> Comparing Two Manufacturing Processes</p>
            <p><strong>Process A:</strong> Mean output = 100 units, SD = 5</p>
            <p><strong>Process B:</strong> Mean output = 102 units, SD = 15</p>
            <p><strong>Wrong conclusion:</strong> "Process B is better because its mean is higher."</p>
            <p><strong>Correct conclusion:</strong> "Process A is better for production planning. Although Process B has a slightly higher average output, it's much less reliable (SD = 15 vs 5). This inconsistency creates scheduling problems and waste. Process A is the safer choice."</p>
        </div>

        <h4>Statistical vs. Practical Significance</h4>
        <p>A difference can be:</p>
        <ul>
            <li><strong>Statistically significant:</strong> Real and unlikely to be due to chance</li>
            <li><strong>Practically significant:</strong> Large enough to matter in real-world decisions</li>
        </ul>

        <p>Both matter! A tiny difference might be statistically significant (with large enough data) but practically irrelevant. Conversely, a large difference might not be statistically significant if data is highly variable.</p>

        <h4>Writing Strong Comparison Conclusions</h4>

        <p><strong>Weak conclusion:</strong> "Class A has a higher mean than Class B."</p>
        <p><strong>Strong conclusion:</strong> "Class A outperforms Class B with a higher median (79 vs 72) and greater consistency (IQR = 10 vs 20). Class A students are both more successful and more uniformly skilled, suggesting more effective teaching methods or student motivation in Class A."</p>

        <div class="success-box">
            <p><strong>Best Practice:</strong> Always pair measures of location WITH measures of spread. A complete comparison discusses both the "center" and the "scatter" of the data.</p>
        </div>

        <h4>Steps for Writing a Comparison</h4>
        <ol>
            <li>Calculate summary statistics (mean, median, SD, IQR, range) for each group</li>
            <li>Create box plots side-by-side for visual comparison</li>
            <li>Identify the most important differences</li>
            <li>Write 3–4 sentences explaining what the numbers mean</li>
            <li>Conclude with a practical implication or insight</li>
        </ol>

        <div class="worked-example">
            <p><strong>Full Comparison Example:</strong></p>
            <p>"The two suppliers deliver widgets with different quality profiles. Supplier A produces an average of 95 conforming units per batch (SD = 3), while Supplier B averages 94 units (SD = 8). Although Supplier A has slightly higher output, the key difference is reliability: Supplier A's lower standard deviation (3 vs 8) means more predictable quality. For a manufacturing operation requiring consistency, Supplier A is the better choice despite slightly lower volume, because we can rely on steady, predictable performance."</p>
        </div>
        """
    }
]
