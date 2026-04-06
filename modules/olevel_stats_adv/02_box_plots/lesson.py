TITLE = "Box Plots and the Five-Number Summary"

SECTIONS = [
    {
        "title": "The Five-Number Summary: Foundation of Box Plots",
        "body": """
        <h3>Five Numbers That Describe Your Data</h3>
        <p>A box plot is one of the most useful tools in statistics because it summarizes the entire distribution of data using just <strong>five numbers</strong>. These five numbers tell us the shape, spread, and center of the data.</p>

        <div class="concept-box">
            <p><strong>The Five-Number Summary:</strong></p>
            <ol>
                <li><strong>Minimum:</strong> The smallest value in the dataset</li>
                <li><strong>Q₁ (Lower Quartile):</strong> The value at 25% (one-quarter) of the data</li>
                <li><strong>Q₂ (Median):</strong> The value at 50% (middle) of the data</li>
                <li><strong>Q₃ (Upper Quartile):</strong> The value at 75% (three-quarters) of the data</li>
                <li><strong>Maximum:</strong> The largest value in the dataset</li>
            </ol>
        </div>

        <h4>Why Quartiles? Understanding Data in Quarters</h4>
        <p>Quartiles divide the data into four equal groups:</p>
        <ul>
            <li><strong>Below Q₁:</strong> 25% of the data (the bottom quarter)</li>
            <li><strong>Q₁ to Q₂:</strong> 25% of the data (the second quarter)</li>
            <li><strong>Q₂ to Q₃:</strong> 25% of the data (the third quarter)</li>
            <li><strong>Above Q₃:</strong> 25% of the data (the top quarter)</li>
        </ul>

        <p>This is more informative than just knowing the minimum, mean, and maximum because it shows us how the data is distributed across the range.</p>

        <h4>Finding Quartiles: The Method</h4>
        <p>For an ordered dataset with n values:</p>
        <ul>
            <li><strong>Q₁ position</strong> \\(= \\frac{n+1}{4}\\)</li>
            <li><strong>Q₂ position</strong> \\(= \\frac{n+1}{2}\\)</li>
            <li><strong>Q₃ position</strong> \\(= \\frac{3(n+1)}{4}\\)</li>
        </ul>

        <p>If the position is a decimal (e.g., 2.5), interpolate between the values at positions 2 and 3.</p>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Data: 2, 5, 7, 9, 11, 13, 15, 17, 19 (n=9)</p>
            <p>First, identify the positions:</p>
            <ul>
                <li>Q₁ position: \\(\\frac{9+1}{4} = 2.5\\)</li>
                <li>Q₂ position: \\(\\frac{9+1}{2} = 5\\)</li>
                <li>Q₃ position: \\(\\frac{3(9+1)}{4} = 7.5\\)</li>
            </ul>
            <p>Now find the values:</p>
            <ul>
                <li><strong>Minimum</strong> = 2 (1st value)</li>
                <li><strong>Q₁</strong> = (5 + 7)/2 = 6 (average of 2nd and 3rd values, since position is 2.5)</li>
                <li><strong>Q₂</strong> = 11 (5th value, the middle)</li>
                <li><strong>Q₃</strong> = (15 + 17)/2 = 16 (average of 7th and 8th values, since position is 7.5)</li>
                <li><strong>Maximum</strong> = 19 (9th value)</li>
            </ul>
            <p><strong>Five-Number Summary: (2, 6, 11, 16, 19)</strong></p>
        </div>

        <div class="success-box">
            <p><strong>Key Insight:</strong> The interquartile range (IQR) = Q₃ − Q₁. This tells us the spread of the middle 50% of the data, which is often more stable and useful than the range for comparing distributions.</p>
        </div>
        """
    },
    {
        "title": "Drawing and Interpreting Box Plots",
        "body": """
        <h3>Visualizing the Five-Number Summary</h3>
        <p>A box plot is a visual representation of the five-number summary. It consists of:</p>
        <ul>
            <li>A <strong>box</strong> from Q₁ to Q₃</li>
            <li>A <strong>line inside the box</strong> at the median (Q₂)</li>
            <li><strong>Whiskers</strong> (lines extending from the box) to the minimum and maximum</li>
        </ul>

        <h4>Step-by-Step: Drawing a Box Plot</h4>
        <ol>
            <li>Draw a horizontal number line that covers the range of your data</li>
            <li>Mark positions for minimum, Q₁, Q₂, Q₃, and maximum</li>
            <li>Draw a rectangular box from Q₁ to Q₃</li>
            <li>Draw a vertical line inside the box at Q₂ (median)</li>
            <li>Draw horizontal lines (whiskers) from the left side of the box to the minimum and from the right side to the maximum</li>
        </ol>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Using our data with five-number summary (2, 6, 11, 16, 19)</p>
            <pre style="padding: 15px; border-radius: 5px">
  Min Q₁  Q₂  Q₃  Max
   2   6  11  16  19
   •———|||||—————|————•
       └─ Box ─┘
    └────────────────┘ Whiskers
            </pre>
            <p>The box spans from 6 to 16 (IQR = 10). The median line is at 11. Whiskers extend to 2 and 19.</p>
        </div>

        <h4>Reading a Box Plot: What Does It Tell Us?</h4>

        <p><strong>Shape of Distribution:</strong></p>
        <ul>
            <li>If the median line is roughly in the center of the box → data is symmetric</li>
            <li>If the median line is closer to Q₁ → data is right-skewed (tails to the right)</li>
            <li>If the median line is closer to Q₃ → data is left-skewed (tails to the left)</li>
        </ul>

        <p><strong>Spread of Data:</strong></p>
        <ul>
            <li>A wide box (large IQR) indicates more variability in the middle 50% of data</li>
            <li>A narrow box (small IQR) indicates less variability</li>
            <li>Long whiskers suggest extreme values; short whiskers suggest data is clustered</li>
        </ul>

        <div class="worked-example">
            <p><strong>Interpretation Example:</strong> Two box plots side-by-side</p>
            <p>Dataset A: Box spans 10–20, median at 15 (symmetric) → consistent and balanced</p>
            <p>Dataset B: Box spans 10–22, median at 11 (closer to Q₁) → right-skewed, with some large values pulling the distribution</p>
        </div>

        <h4>Identifying and Marking Outliers</h4>
        <p>An <strong>outlier</strong> is a value that lies far from the rest of the data. We use a mathematical rule:</p>

        <div class="concept-box">
            <p><strong>Outlier Rule:</strong> A value is an outlier if:</p>
            <p style="text-align: center;">\\(\\text{value} < Q_1 - 1.5(IQR)\\) <strong>OR</strong> \\(\\text{value} > Q_3 + 1.5(IQR)\\)</p>
            <p>where \\(IQR = Q_3 - Q_1\\)</p>
        </div>

        <p>On a box plot, outliers are plotted as individual points beyond the whiskers, rather than extending the whiskers to extreme values. This makes the box plot more readable.</p>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Checking for outliers</p>
            <p>Using our five-number summary: (2, 6, 11, 16, 19)</p>
            <p>\\(IQR = 16 - 6 = 10\\)</p>
            <p>Lower outlier boundary: \\(6 - 1.5(10) = 6 - 15 = -9\\)</p>
            <p>Upper outlier boundary: \\(16 + 1.5(10) = 16 + 15 = 31\\)</p>
            <p>Outlier range: \\([-9, 31]\\)</p>
            <p>Since all values (2, 5, 7, 9, 11, 13, 15, 17, 19) fall within [−9, 31], there are <strong>no outliers</strong>.</p>
        </div>

        <div class="success-box">
            <p><strong>Why 1.5 × IQR?</strong> This threshold is based on statistical theory and works well for normally distributed data. It's a standard in data analysis and balances identifying genuine outliers while avoiding false positives.</p>
        </div>
        """
    },
    {
        "title": "Using Box Plots for Comparison",
        "body": """
        <h3>Comparing Multiple Datasets with Box Plots</h3>
        <p>One of the greatest strengths of box plots is the ability to compare distributions visually and quickly. By placing multiple box plots on the same axis, patterns emerge immediately.</p>

        <h4>Side-by-Side Box Plots: What to Look For</h4>
        <p>When comparing box plots, examine:</p>
        <ul>
            <li><strong>Medians (center lines in boxes):</strong> Which dataset has a higher/lower typical value?</li>
            <li><strong>Box widths (IQR):</strong> Which dataset has more/less variability?</li>
            <li><strong>Whisker lengths:</strong> Which dataset has a wider overall range?</li>
            <li><strong>Position of median within box:</strong> Which distribution is more skewed?</li>
            <li><strong>Outliers:</strong> Which dataset has extreme values?</li>
        </ul>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Comparing two test score distributions</p>
            <p><strong>Class A:</strong> Min=50, Q₁=65, Q₂=75, Q₃=80, Max=90</p>
            <p><strong>Class B:</strong> Min=45, Q₁=60, Q₂=70, Q₃=78, Max=95</p>
            <p><strong>Comparison:</strong></p>
            <ul>
                <li>Class A has a slightly higher median (75 vs 70) → slightly better average performance</li>
                <li>Class A has a smaller IQR (15 vs 18) → more consistent/uniform performance</li>
                <li>Class B has a wider range (50 vs 45) → more variability overall</li>
                <li><strong>Conclusion:</strong> Class A students are performing at a similar level on average, but more consistently. Class B has more spread.</li>
            </ul>
        </div>

        <h4>When Box Plots Excel</h4>
        <p>Box plots are particularly useful when:</p>
        <ul>
            <li>Comparing three or more groups (easier than comparing means and standard deviations)</li>
            <li>Assessing whether medians differ substantially</li>
            <li>Identifying outliers in large datasets</li>
            <li>Checking the symmetry of distributions</li>
            <li>Working with skewed data (medians are more robust than means)</li>
        </ul>

        <div class="success-box">
            <p><strong>Box Plot Advantage:</strong> Unlike histograms, box plots don't hide information about the actual distribution shape (they show quartiles, not just the overall range). They also handle outliers explicitly rather than distorting the visualization.</p>
        </div>

        <h4>Limitations of Box Plots</h4>
        <ul>
            <li>They don't show every value in the data (unlike scatter plots)</li>
            <li>They can hide bimodal distributions (two peaks)</li>
            <li>They don't reveal the sample size</li>
        </ul>

        <p>For these reasons, box plots are often used alongside histograms or other visualizations for a complete picture.</p>
        """
    }
]
