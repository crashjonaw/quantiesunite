SECTIONS = [
    {
        "title": "Cumulative Frequency and Cumulative Frequency Graphs",
        "body": """
        <h3>Understanding Cumulative Frequency</h3>
        <p><strong>Cumulative frequency</strong> is the running total of frequencies. For a class, it's the sum of all frequencies up to and including that class.</p>

        <h4>Building a Cumulative Frequency Table</h4>
        <ol>
            <li>List the classes (intervals)</li>
            <li>Write the frequency for each class</li>
            <li>Calculate cumulative frequency: add all previous frequencies</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 1:</strong> Heights of students (cm) with frequencies:</p>
            <table style="width: 100%; border-collapse: collapse;">
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;"><strong>Height (cm)</strong></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">150-160</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">160-170</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">170-180</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">180-190</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;"><strong>Frequency</strong></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">5</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">12</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">8</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">5</td>
                </tr>
                <tr style="border: 1px solid #ddd;">
                    <td style="border: 1px solid #ddd; padding: 8px;"><strong>Cumulative Freq</strong></td>
                    <td style="border: 1px solid #ddd; padding: 8px;">5</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">17</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">25</td>
                    <td style="border: 1px solid #ddd; padding: 8px;">30</td>
                </tr>
            </table>
        </div>

        <h4>Cumulative Frequency Graph</h4>
        <p>Plot points with the upper boundary of each class against cumulative frequency. Connect with a smooth curve.</p>
        <ul>
            <li>x-axis: Class upper boundaries</li>
            <li>y-axis: Cumulative frequencies</li>
            <li>Start at (lower boundary of first class, 0)</li>
            <li>Plot points at class upper boundaries</li>
        </ul>

        <h4>Reading from Cumulative Frequency Graphs</h4>
        <p>Use the graph to find:</p>
        <ul>
            <li><strong>Median:</strong> Draw horizontal line at height = n/2 (total frequency ÷ 2)</li>
            <li><strong>Quartiles:</strong> Q₁ at n/4, Q₃ at 3n/4</li>
            <li><strong>Percentiles:</strong> Pₖ at (k/100)×n</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 2:</strong> From the cumulative frequency graph in Example 1 (total = 30):</p>
            <ul>
                <li>Median position: 30/2 = 15</li>
                <li>Find where the horizontal line at 15 intersects the curve</li>
                <li>Read the corresponding height value</li>
            </ul>
        </div>
        """
    },
    {
        "title": "Box Plots (Box-and-Whisker Diagrams)",
        "body": """
        <h3>Five-Number Summary</h3>
        <p>A box plot displays five key values:</p>
        <ul>
            <li><strong>Minimum:</strong> Smallest value</li>
            <li><strong>Q₁ (Lower Quartile):</strong> 25th percentile; 1/4 of data below this</li>
            <li><strong>Q₂ (Median):</strong> 50th percentile; middle value</li>
            <li><strong>Q₃ (Upper Quartile):</strong> 75th percentile; 3/4 of data below this</li>
            <li><strong>Maximum:</strong> Largest value</li>
        </ul>

        <h4>Finding Quartiles</h4>
        <p>For ordered data with n values:</p>
        <ul>
            <li>Q₁ is at position (n+1)/4</li>
            <li>Q₂ (median) is at position (n+1)/2</li>
            <li>Q₃ is at position 3(n+1)/4</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 3:</strong> Data: 2, 5, 7, 9, 11, 13, 15, 17, 19 (n=9)</p>
            <ul>
                <li>Minimum = 2</li>
                <li>Q₁ position: 10/4 = 2.5 → average of 2nd and 3rd values → (5+7)/2 = 6</li>
                <li>Q₂ position: 10/2 = 5 → 5th value → 11</li>
                <li>Q₃ position: 30/4 = 7.5 → average of 7th and 8th values → (15+17)/2 = 16</li>
                <li>Maximum = 19</li>
            </ul>
        </div>

        <h4>Drawing a Box Plot</h4>
        <ol>
            <li>Draw a horizontal line (or vertical, depending on orientation)</li>
            <li>Mark minimum and maximum with whiskers (endpoints)</li>
            <li>Draw a box from Q₁ to Q₃</li>
            <li>Mark Q₂ (median) with a line inside the box</li>
        </ol>

        <h4>Interpreting Box Plots</h4>
        <ul>
            <li><strong>Symmetry:</strong> If median line is centered in box, distribution is roughly symmetric</li>
            <li><strong>Skewness:</strong> If median is off-center, distribution is skewed</li>
            <li><strong>Spread:</strong> Width of box (IQR) shows variability of middle 50%</li>
        </ul>

        <h4>Outliers</h4>
        <p>An outlier is a value outside the range [Q₁ − 1.5(IQR), Q₃ + 1.5(IQR)], where IQR = Q₃ − Q₁</p>

        <div class="example-box">
            <p><strong>Example 4:</strong> From Example 3: IQR = 16 − 6 = 10</p>
            <p>Outlier range: [6 − 15, 16 + 15] = [−9, 31]</p>
            <p>All values fall within this range, so no outliers.</p>
        </div>
        """
    },
    {
        "title": "Measures of Dispersion",
        "body": """
        <h3>Quantifying Data Spread</h3>
        <p>Measures of dispersion describe how scattered the data is from the average.</p>

        <h4>Range</h4>
        <p><strong>Range = Maximum − Minimum</strong></p>
        <p>Simple but affected by extreme values (outliers)</p>

        <div class="example-box">
            <p><strong>Example 5:</strong> Data: 2, 5, 7, 9, 11, 13, 15, 17, 19</p>
            <p>Range = 19 − 2 = 17</p>
        </div>

        <h4>Interquartile Range (IQR)</h4>
        <p><strong>IQR = Q₃ − Q₁</strong></p>
        <p>More robust than range; ignores extreme values. Shows spread of middle 50%.</p>

        <div class="example-box">
            <p><strong>Example 6:</strong> From Example 3: IQR = 16 − 6 = 10</p>
        </div>

        <h4>Variance</h4>
        <p><strong>Variance σ² = Σ(x − mean)² / n</strong> (population variance)</p>
        <p><strong>Sample variance s² = Σ(x − mean)² / (n − 1)</strong> (for samples)</p>

        <p>Measures average squared distance from the mean. Units are squared (e.g., cm² for height in cm).</p>

        <div class="example-box">
            <p><strong>Example 7:</strong> Data: 2, 4, 6, 8, 10</p>
            <p>Mean = 30/5 = 6</p>
            <p>Deviations: (2−6)² = 16, (4−6)² = 4, (6−6)² = 0, (8−6)² = 4, (10−6)² = 16</p>
            <p>Variance = (16+4+0+4+16)/5 = 40/5 = 8</p>
        </div>

        <h4>Standard Deviation</h4>
        <p><strong>Standard Deviation σ = √Variance</strong></p>
        <p>Most common measure of spread. Same units as the data.</p>

        <div class="example-box">
            <p><strong>Example 8:</strong> From Example 7: σ = √8 ≈ 2.83</p>
        </div>

        <h4>Coefficient of Variation</h4>
        <p><strong>CV = (Standard Deviation / Mean) × 100%</strong></p>
        <p>Allows comparison of variability between datasets with different scales.</p>

        <div class="example-box">
            <p><strong>Example 9:</strong> From Example 7: CV = (2.83/6) × 100% ≈ 47%</p>
        </div>
        """
    },
    {
        "title": "Comparing Distributions",
        "body": """
        <h3>Analyzing Two or More Data Sets</h3>

        <h4>Using Summary Statistics</h4>
        <p>Compare datasets using:</p>
        <ul>
            <li><strong>Central tendency:</strong> Mean, median, mode</li>
            <li><strong>Spread:</strong> Range, IQR, standard deviation</li>
            <li><strong>Shape:</strong> Skewness, symmetry</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 10:</strong> Two test scores (out of 100)</p>
            <p><strong>Class A:</strong> Mean = 75, SD = 8, IQR = 12</p>
            <p><strong>Class B:</strong> Mean = 75, SD = 15, IQR = 20</p>
            <p>Both have the same average, but Class A is more consistent (lower spread).</p>
        </div>

        <h4>Comparing with Box Plots</h4>
        <p>Place box plots side-by-side to visually compare:</p>
        <ul>
            <li>Medians (center of boxes) show typical values</li>
            <li>Box widths (IQR) show consistency</li>
            <li>Whisker lengths show overall range</li>
            <li>Outliers appear as individual points</li>
        </ul>

        <h4>Standardization (z-scores)</h4>
        <p>Convert to standard units to compare across different scales:</p>
        <p style="text-align: center;"><strong>z = (x − mean) / standard deviation</strong></p>

        <p>A z-score of 2 means the value is 2 standard deviations above the mean.</p>

        <div class="example-box">
            <p><strong>Example 11:</strong> Two students:</p>
            <ul>
                <li>Alice: scored 82 in Math (mean 75, SD 8) → z = (82−75)/8 = 0.875</li>
                <li>Bob: scored 88 in Science (mean 80, SD 10) → z = (88−80)/10 = 0.8</li>
            </ul>
            <p>Alice performed slightly better relative to her class average.</p>
        </div>

        <h4>Making Conclusions</h4>
        <p>When comparing distributions:</p>
        <ol>
            <li>State the mean/median values and explain what they show</li>
            <li>Compare spread using IQR or standard deviation</li>
            <li>Note any outliers or unusual patterns</li>
            <li>Draw conclusions based on context</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 12:</strong> Conclusion:</p>
            <p>"Class A has a higher median score (78 vs 74) and is more consistent (IQR 10 vs 15). This suggests Class A students performed better and more uniformly."</p>
        </div>
        """
    },
    {
        "title": "Normal Distribution (Introduction)",
        "body": """
        <h3>The Bell Curve</h3>
        <p>A <strong>normal distribution</strong> (or Gaussian distribution) is bell-shaped and symmetric about the mean.</p>

        <h4>Properties of Normal Distribution</h4>
        <ul>
            <li>Symmetric about the mean</li>
            <li>Mean = Median = Mode</li>
            <li>Most data cluster near the mean</li>
            <li>Described completely by mean (μ) and standard deviation (σ)</li>
        </ul>

        <h4>Empirical Rule (68-95-99.7 Rule)</h4>
        <p>For a normal distribution:</p>
        <ul>
            <li>≈68% of data fall within 1σ of the mean [μ − σ, μ + σ]</li>
            <li>≈95% of data fall within 2σ of the mean [μ − 2σ, μ + 2σ]</li>
            <li>≈99.7% of data fall within 3σ of the mean [μ − 3σ, μ + 3σ]</li>
        </ul>

        <div class="example-box">
            <p><strong>Example 13:</strong> Heights are normally distributed with mean 170 cm and SD 5 cm.</p>
            <ul>
                <li>68% of people have heights between 165 and 175 cm</li>
                <li>95% have heights between 160 and 180 cm</li>
                <li>Only 0.3% have heights above 185 cm</li>
            </ul>
        </div>

        <h4>Using the Empirical Rule</h4>
        <ol>
            <li>Find the mean and standard deviation</li>
            <li>Identify the range in terms of σ</li>
            <li>Apply the 68-95-99.7 rule</li>
        </ol>

        <div class="example-box">
            <p><strong>Example 14:</strong> Test scores with mean 80 and SD 10. What proportion of students score between 70 and 90?</p>
            <p>70 to 90 is μ − σ to μ + σ</p>
            <p>By the empirical rule, 68% of students score in this range.</p>
        </div>
        """
    }
]
