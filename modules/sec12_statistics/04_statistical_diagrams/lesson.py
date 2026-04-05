TITLE = "Statistical Diagrams"

SECTIONS = [
    {
        "title": "Why Visualize? A Picture Worth a Thousand Numbers",
        "body": """<div class="concept-box"><p>A graph or diagram lets you see patterns instantly that would take forever to spot in raw data. A good diagram answers:</p><ul><li>What is typical?</li><li>How spread out is the data?</li><li>Are there clusters or gaps?</li><li>Are there outliers?</li></ul></div><h3>Four Key Statistical Diagrams</h3><ol><li><strong>Dot Plot:</strong> Shows individual data points</li><li><strong>Stem-and-Leaf Diagram:</strong> Organizes data by place value</li><li><strong>Histogram:</strong> Shows frequency distribution for grouped continuous data</li><li><strong>Box-and-Whisker Plot:</strong> Shows five-number summary</li></ol><p><strong>Each diagram tells a different story. Each is best for certain data types.</strong></p>"""
    },
    {
        "title": "Dot Plots and Stem-and-Leaf Diagrams",
        "body": """<h3>Dot Plot</h3>
<p>Each data point is shown as a dot on a number line.</p>
<h3>Example: Heights of 10 Students (cm)</h3>
<svg viewBox="0 0 350 100" style="width:100%;max-width:400px;height:auto;display:block;margin:20px auto;">
  <line x1="40" y1="50" x2="330" y2="50" stroke='#e6edf3' stroke-width="2"/>
  <text x="40" y="70" font-size='11' fill='#8b949e'>160</text>
  <text x="110" y="70" font-size='11' fill='#8b949e'>165</text>
  <text x="185" y="70" font-size='11' fill='#8b949e'>170</text>
  <text x="255" y="70" font-size='11' fill='#8b949e'>175</text>
  <text x="320" y="70" font-size='11' fill='#8b949e'>180</text>
  <circle cx="50" cy="35" r="4" fill='#79c0ff'/>
  <circle cx="60" cy="35" r="4" fill='#79c0ff'/>
  <circle cx="65" cy="25" r="4" fill='#79c0ff'/>
  <circle cx="130" cy="35" r="4" fill='#79c0ff'/>
  <circle cx="135" cy="25" r="4" fill='#79c0ff'/>
  <circle cx="195" cy="35" r="4" fill='#79c0ff'/>
  <circle cx="200" cy="25" r="4" fill='#79c0ff'/>
  <circle cx="265" cy="35" r="4" fill='#79c0ff'/>
  <circle cx="310" cy="35" r="4" fill='#79c0ff'/>
  <circle cx="320" cy="25" r="4" fill='#79c0ff'/>
</svg>
<p><strong>What you see instantly:</strong> Most students cluster around 165-175 cm.</p>

<h3>Stem-and-Leaf Diagram</h3>
<p>Organizes data by the leading digit (stem) and trailing digit (leaf).</p>
<div class="worked-example">
<p><strong>Test scores: 42, 45, 48, 51, 54, 57, 61, 68, 72, 78</strong></p>
<table style="border-collapse:collapse;margin:12px 0;">
<tr ><th style="padding: 6px 16px">Stem</th><th style="padding: 6px 16px">Leaf</th></tr>
<tr><td style="padding: 4px 16px; font-weight: bold">4</td><td style="padding: 4px 16px">2 &nbsp; 5 &nbsp; 8</td></tr>
<tr><td style="padding: 4px 16px; font-weight: bold">5</td><td style="padding: 4px 16px">1 &nbsp; 4 &nbsp; 7</td></tr>
<tr><td style="padding: 4px 16px; font-weight: bold">6</td><td style="padding: 4px 16px">1 &nbsp; 8</td></tr>
<tr><td style="padding: 4px 16px; font-weight: bold">7</td><td style="padding: 4px 16px">2 &nbsp; 8</td></tr>
</table>
<p>Stem 4, leaf 2 means 42. Stem 7, leaf 8 means 78.</p>
</div>
<div class="success-box"><p><strong>Advantages:</strong> Shows individual data points (not lost like in a histogram), easy to spot clusters and gaps, preserves actual values.</p></div>"""
    },
    {
        "title": "Histograms: Grouped Frequency Data",
        "body": """<h3>What Is a Histogram?</h3>
<p>A <strong>histogram</strong> shows the frequency of data grouped into intervals (bins).</p>
<ul>
<li><strong>X-axis:</strong> Intervals (e.g., 50-60, 60-70, 70-80)</li>
<li><strong>Y-axis:</strong> Frequency (how many values fall in each interval)</li>
<li><strong>Bars:</strong> Touch each other (showing continuous data)</li>
</ul>

<h3>Example: Test Scores (50 Students)</h3>
<div class="worked-example">
<table style="border-collapse:collapse;margin:12px 0;width:100%;">
<tr ><th style="padding: 6px 16px">Score Range</th><th style="padding: 6px 16px">Frequency</th></tr>
<tr><td style="padding: 4px 16px">50 &ndash; 60</td><td style="padding: 4px 16px; font-weight: bold">5</td></tr>
<tr><td style="padding: 4px 16px">60 &ndash; 70</td><td style="padding: 4px 16px; font-weight: bold">12</td></tr>
<tr><td style="padding: 4px 16px">70 &ndash; 80</td><td style="padding: 4px 16px; font-weight: bold">18</td></tr>
<tr><td style="padding: 4px 16px">80 &ndash; 90</td><td style="padding: 4px 16px; font-weight: bold">10</td></tr>
<tr><td style="padding: 4px 16px">90 &ndash; 100</td><td style="padding: 4px 16px; font-weight: bold">5</td></tr>
</table>
</div>

<svg viewBox="0 0 400 250" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <text x="200" y="20" font-size='13' font-weight='bold' fill='#e6edf3' text-anchor='middle'>Test Score Distribution</text>
  <line x1="60" y1="200" x2="370" y2="200" stroke='#8b949e' stroke-width="2"/>
  <line x1="60" y1="200" x2="60" y2="30" stroke='#8b949e' stroke-width="2"/>
  <text x="215" y="230" font-size='11' fill='#8b949e' text-anchor='middle'>Test Score</text>
  <rect x="70" y="172" width="50" height="28" fill='#4f8ef780' stroke='#4f8ef7' stroke-width="1.5"/>
  <rect x="125" y="132" width="50" height="68" fill='#4f8ef780' stroke='#4f8ef7' stroke-width="1.5"/>
  <rect x="180" y="60" width="50" height="140" fill='#4f8ef780' stroke='#4f8ef7' stroke-width="1.5"/>
  <rect x="235" y="120" width="50" height="80" fill='#4f8ef780' stroke='#4f8ef7' stroke-width="1.5"/>
  <rect x="290" y="172" width="50" height="28" fill='#4f8ef780' stroke='#4f8ef7' stroke-width="1.5"/>
  <text x="95" y="215" font-size='10' fill='#8b949e' text-anchor='middle'>50-60</text>
  <text x="150" y="215" font-size='10' fill='#8b949e' text-anchor='middle'>60-70</text>
  <text x="205" y="215" font-size='10' fill='#8b949e' text-anchor='middle'>70-80</text>
  <text x="260" y="215" font-size='10' fill='#8b949e' text-anchor='middle'>80-90</text>
  <text x="315" y="215" font-size='10' fill='#8b949e' text-anchor='middle'>90-100</text>
  <text x="50" y="176" font-size='10' fill='#8b949e' text-anchor='end'>5</text>
  <text x="50" y="136" font-size='10' fill='#8b949e' text-anchor='end'>12</text>
  <text x="50" y="64" font-size='10' fill='#8b949e' text-anchor='end'>18</text>
  <text x="50" y="124" font-size='10' fill='#8b949e' text-anchor='end'>10</text>
</svg>

<h3>Histogram vs. Bar Chart</h3>
<div class="concept-box">
<p><strong>Histogram:</strong> Bars touch. For continuous data grouped into intervals.</p>
<p><strong>Bar Chart:</strong> Bars have gaps. For categorical data (colors, brands, etc.).</p>
</div>"""
    },
    {
        "title": "Misleading Graphs and How to Spot Them",
        "body": """<h3>Common Ways Graphs Can Mislead</h3>

<div class="warning-box">
<h4>1. Wrong Axis Scale</h4>
<p>Y-axis starts at 95 instead of 0. A small change from 95 to 98 looks like a huge jump!</p>
<p><strong>Fix:</strong> Y-axis should start at 0, or clearly note if it does not.</p>
</div>

<div class="warning-box">
<h4>2. Broken Axis</h4>
<p>Y-axis goes 0, 10, 20, then jumps to 100. The jump hides the true scale.</p>
<p><strong>Fix:</strong> Use a continuous scale or clearly mark breaks with a // symbol.</p>
</div>

<div class="warning-box">
<h4>3. Wrong Graph Type</h4>
<p>Using a pie chart for data over time (pie charts show parts of a whole, not change). Using a histogram for categorical data (should use a bar chart).</p>
<p><strong>Fix:</strong> Match graph type to data type.</p>
</div>

<div class="warning-box">
<h4>4. Cherry-Picked Data</h4>
<p>Showing only 5 years of a 20-year trend to make sales look better (or worse).</p>
<p><strong>Fix:</strong> Show all relevant data, not selected portions.</p>
</div>

<h3>Red Flags When Reading Graphs</h3>
<ul>
<li>Does the axis start at 0? If not, why?</li>
<li>Are both axes labeled clearly?</li>
<li>Is the data source shown?</li>
<li>Has data been cherry-picked or truncated?</li>
<li>Is the graph type appropriate for the data?</li>
</ul>

<div class="success-box"><p><strong>Key Lesson:</strong> Always check the axes, scale, and source. A true number presented with a deceptive graph is still deceptive.</p></div>"""
    }
]
