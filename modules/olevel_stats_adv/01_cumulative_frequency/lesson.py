TITLE = "Cumulative Frequency and Cumulative Frequency Graphs"

SECTIONS = [
    {
        "title": "Understanding Cumulative Frequency",
        "body": """
        <h3>What is Cumulative Frequency and Why Does it Matter?</h3>
        <p>In statistics, we often ask "How many observations are there UP TO a certain value?" This running total is called <strong>cumulative frequency</strong>. It helps us understand the distribution of data in a way that raw frequencies cannot.</p>

        <div class="concept-box">
            <p><strong>Definition:</strong> Cumulative frequency for a class is the sum of all frequencies from the first class up to and including that class.</p>
        </div>

        <h4>Why Learn Cumulative Frequency?</h4>
        <p>Cumulative frequency allows us to:</p>
        <ul>
            <li>Find the median and quartiles (key percentiles) directly from a graph</li>
            <li>Answer questions like "How many students scored up to 70 marks?"</li>
            <li>Identify the distribution of data visually</li>
        </ul>

        <h4>Building a Cumulative Frequency Table from First Principles</h4>
        <p>Think of this as a staircase. Each step adds to the previous total:</p>
        <ol>
            <li>List the classes (intervals) in order from smallest to largest</li>
            <li>Write the frequency for each class</li>
            <li>For the first class: cumulative frequency = frequency</li>
            <li>For each subsequent class: cumulative frequency = previous cumulative frequency + current frequency</li>
        </ol>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Heights of 30 students (in cm)</p>
            <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
                <tr >
                    <td style="padding: 10px;"><strong>Height (cm)</strong></td>
                    <td style="padding: 10px;"><strong>Frequency</strong></td>
                    <td style="padding: 10px;"><strong>Cumulative Frequency</strong></td>
                    <td style="padding: 10px;"><strong>Explanation</strong></td>
                </tr>
                <tr >
                    <td style="padding: 10px;">150−160</td>
                    <td style="padding: 10px;">5</td>
                    <td style="padding: 10px;">5</td>
                    <td style="padding: 10px;">5 students are ≤160 cm</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">160−170</td>
                    <td style="padding: 10px;">12</td>
                    <td style="padding: 10px;">17</td>
                    <td style="padding: 10px;">5 + 12 = 17 students are ≤170 cm</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">170−180</td>
                    <td style="padding: 10px;">8</td>
                    <td style="padding: 10px;">25</td>
                    <td style="padding: 10px;">17 + 8 = 25 students are ≤180 cm</td>
                </tr>
                <tr >
                    <td style="padding: 10px;">180−190</td>
                    <td style="padding: 10px;">5</td>
                    <td style="padding: 10px;">30</td>
                    <td style="padding: 10px;">25 + 5 = 30 students (total)</td>
                </tr>
            </table>
        </div>

        <h4>Key Insight</h4>
        <p>The final cumulative frequency should equal the total number of observations. If it doesn't, you've made an error!</p>
        """
    },
    {
        "title": "Cumulative Frequency Graphs (Ogives)",
        "body": """
        <h3>From Table to Graph: Visualizing Cumulative Frequency</h3>
        <p>A <strong>cumulative frequency graph</strong> (also called an <strong>ogive</strong>) is a curve that shows how cumulative frequency increases as we move across the data range. It's the key tool for finding medians and quartiles graphically.</p>

        <h4>How to Plot a Cumulative Frequency Graph</h4>
        <p>The crucial rule: <strong>Plot each point at the upper boundary of its class.</strong></p>
        <ol>
            <li>On the x-axis: mark the upper class boundary</li>
            <li>On the y-axis: mark the cumulative frequency for that class</li>
            <li>Plot a point at (upper boundary, cumulative frequency)</li>
            <li>Start with a point at (lower boundary of first class, 0)</li>
            <li>Connect all points with a smooth curve (not straight lines)</li>
        </ol>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Plotting from the height data above</p>
            <p>Points to plot (using upper boundaries):</p>
            <ul>
                <li>(150, 0) — before any students</li>
                <li>(160, 5) — 5 students at or below 160</li>
                <li>(170, 17) — 17 students at or below 170</li>
                <li>(180, 25) — 25 students at or below 180</li>
                <li>(190, 30) — 30 students at or below 190</li>
            </ul>
            <p>Connect these with a smooth curve. The curve should be smooth and gentle, rising steeply where frequency is high, and more gradually elsewhere.</p>
        </div>

        <h4>Why Start at Zero?</h4>
        <p>The point (lower boundary, 0) represents "no data before the first class." This anchors the curve and reminds us that at the start, the cumulative frequency is zero.</p>

        <h4>Why Use Upper Boundaries?</h4>
        <p>The upper boundary represents the maximum value in that class. By plotting at the upper boundary, we show "everything up to this value is included in the cumulative total." This is the standard convention and makes reading the graph consistent.</p>

        <div class="success-box">
            <p><strong>Key Tip:</strong> Always label your axes clearly with units. The y-axis should say "Cumulative Frequency" and the x-axis should show the variable name (e.g., "Height (cm)").</p>
        </div>
        """
    },
    {
        "title": "Reading from Cumulative Frequency Graphs",
        "body": """
        <h3>Using Cumulative Frequency Graphs to Find Key Statistics</h3>
        <p>The main power of cumulative frequency graphs is finding the median, quartiles, and other percentiles without complex calculations. We simply draw horizontal and vertical lines on the graph.</p>

        <h4>Finding the Median</h4>
        <p>The median is the value where exactly 50% of the data lies below it.</p>
        <ol>
            <li>Find n/2 (half the total frequency) on the y-axis</li>
            <li>Draw a horizontal line from this value to the curve</li>
            <li>From the intersection point, draw a vertical line down to the x-axis</li>
            <li>Read the x-value — this is the median</li>
        </ol>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Using our height data (n = 30)</p>
            <p>Median position: 30/2 = 15</p>
            <p>Step 1: On the y-axis, find 15</p>
            <p>Step 2: Draw a horizontal line to where it meets the curve (somewhere between 160 and 170)</p>
            <p>Step 3: Draw a vertical line down</p>
            <p>Step 4: Read the height — let's say it's approximately 165 cm</p>
            <p>So the median height is approximately 165 cm</p>
        </div>

        <h4>Finding Quartiles</h4>
        <p><strong>Q₁ (Lower Quartile)</strong> is at 25% of the data:</p>
        <ul>
            <li>Find n/4 on the y-axis</li>
            <li>For our data: 30/4 = 7.5</li>
            <li>Follow the same line-drawing procedure to find Q₁</li>
        </ul>

        <p><strong>Q₃ (Upper Quartile)</strong> is at 75% of the data:</p>
        <ul>
            <li>Find 3n/4 on the y-axis</li>
            <li>For our data: 3(30)/4 = 22.5</li>
            <li>Follow the same line-drawing procedure to find Q₃</li>
        </ul>

        <div class="worked-example">
            <p><strong>Worked Example:</strong> Finding quartiles from the graph</p>
            <ul>
                <li>Q₁ position: 7.5 → horizontal line to curve → vertical down → ≈ 162 cm</li>
                <li>Q₂ (median) position: 15 → horizontal line to curve → vertical down → ≈ 165 cm</li>
                <li>Q₃ position: 22.5 → horizontal line to curve → vertical down → ≈ 173 cm</li>
            </ul>
        </div>

        <h4>Finding Percentiles</h4>
        <p>Any percentile can be found using the same method:</p>
        <p style="text-align: center;"><strong>Position = (k/100) × n</strong> where k is the percentile (e.g., k = 90 for 90th percentile)</p>

        <div class="success-box">
            <p><strong>Reading Accuracy Tip:</strong> Use a ruler or straight edge when drawing lines on the graph. Be precise with your horizontal and vertical lines to get accurate readings.</p>
        </div>

        <div class="warning-box">
            <p><strong>Remember:</strong> Cumulative frequency graphs give approximate values by visual inspection. The exact values depend on careful drawing and reading. For precision, calculate from the raw data instead.</p>
        </div>
        """
    }
]
