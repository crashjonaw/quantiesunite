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
<svg viewBox="0 0 420 120" style="width:100%;max-width:480px;height:auto;display:block;margin:20px auto;">
  <!-- Title -->
  <text x="210" y="18" font-size="12" font-weight="bold" fill="currentColor" text-anchor="middle" font-family="sans-serif">Dot Plot: Heights of 10 Students (cm)</text>
  <!-- Axis line -->
  <line x1="40" y1="72" x2="400" y2="72" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
  <!-- Tick marks and labels at equal spacing: 40, 130, 220, 310, 400 -->
  <line x1="40" y1="72" x2="40" y2="78" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
  <text x="40" y="95" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">160</text>
  <line x1="130" y1="72" x2="130" y2="78" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
  <text x="130" y="95" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">165</text>
  <line x1="220" y1="72" x2="220" y2="78" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
  <text x="220" y="95" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">170</text>
  <line x1="310" y1="72" x2="310" y2="78" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
  <text x="310" y="95" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">175</text>
  <line x1="400" y1="72" x2="400" y2="78" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
  <text x="400" y="95" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">180</text>
  <!-- Dots: each cm = 18px. Stack upward with 12px gap between dots -->
  <!-- 161 cm = 40 + 1*18 = 58 -->
  <circle cx="58" cy="62" r="5" fill="#79c0ff"/>
  <!-- 162 cm = 40 + 2*18 = 76 -->
  <circle cx="76" cy="62" r="5" fill="#79c0ff"/>
  <!-- 163 cm = 40 + 3*18 = 94 (two dots stacked) -->
  <circle cx="94" cy="62" r="5" fill="#79c0ff"/>
  <circle cx="94" cy="48" r="5" fill="#79c0ff"/>
  <!-- 166 cm = 40 + 6*18 = 148 -->
  <circle cx="148" cy="62" r="5" fill="#79c0ff"/>
  <!-- 170 cm = 40 + 10*18 = 220 (two dots stacked) -->
  <circle cx="220" cy="62" r="5" fill="#79c0ff"/>
  <circle cx="220" cy="48" r="5" fill="#79c0ff"/>
  <!-- 175 cm = 40 + 15*18 = 310 -->
  <circle cx="310" cy="62" r="5" fill="#79c0ff"/>
  <!-- 179 cm = 40 + 19*18 = 382 -->
  <circle cx="382" cy="62" r="5" fill="#79c0ff"/>
  <!-- 180 cm = 40 + 20*18 = 400 -->
  <circle cx="400" cy="62" r="5" fill="#79c0ff"/>
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

<svg viewBox="0 0 430 270" style="width:100%;max-width:500px;height:auto;display:block;margin:20px auto;">
  <!-- Title -->
  <text x="235" y="22" font-size="13" font-weight="bold" fill="currentColor" text-anchor="middle" font-family="sans-serif">Test Score Distribution</text>
  <!-- Y-axis -->
  <line x1="80" y1="40" x2="80" y2="210" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
  <!-- X-axis -->
  <line x1="80" y1="210" x2="400" y2="210" stroke="currentColor" stroke-width="1.5" opacity="0.4"/>
  <!-- Y-axis label -->
  <text x="25" y="125" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7" transform="rotate(-90,25,125)">Frequency</text>
  <!-- X-axis label -->
  <text x="240" y="255" font-size="11" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">Test Score</text>
  <!-- Y-axis gridlines and labels: max freq=18, scale: 1 unit = 170/18 = 9.44px -->
  <!-- 0 at y=210, 5 at y=210-5*9.44=163, 10 at y=116, 15 at y=68, 18 at y=40 -->
  <line x1="75" y1="163" x2="400" y2="163" stroke="currentColor" stroke-width="0.5" opacity="0.15"/>
  <text x="70" y="167" font-size="10" fill="currentColor" text-anchor="end" font-family="sans-serif" opacity="0.7">5</text>
  <line x1="75" y1="116" x2="400" y2="116" stroke="currentColor" stroke-width="0.5" opacity="0.15"/>
  <text x="70" y="120" font-size="10" fill="currentColor" text-anchor="end" font-family="sans-serif" opacity="0.7">10</text>
  <line x1="75" y1="68" x2="400" y2="68" stroke="currentColor" stroke-width="0.5" opacity="0.15"/>
  <text x="70" y="72" font-size="10" fill="currentColor" text-anchor="end" font-family="sans-serif" opacity="0.7">15</text>
  <text x="70" y="214" font-size="10" fill="currentColor" text-anchor="end" font-family="sans-serif" opacity="0.7">0</text>
  <!-- Bars: 5 bars, each 60px wide, touching. Start at x=90 -->
  <!-- 50-60: freq=5, height=5*9.44=47, top=210-47=163 -->
  <rect x="90" y="163" width="60" height="47" rx="4" fill="#4f8ef780" stroke="#4f8ef7" stroke-width="1.5"/>
  <text x="120" y="156" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" font-weight="bold">5</text>
  <!-- 60-70: freq=12, height=12*9.44=113, top=210-113=97 -->
  <rect x="150" y="97" width="60" height="113" rx="4" fill="#4f8ef780" stroke="#4f8ef7" stroke-width="1.5"/>
  <text x="180" y="90" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" font-weight="bold">12</text>
  <!-- 70-80: freq=18, height=18*9.44=170, top=210-170=40 -->
  <rect x="210" y="40" width="60" height="170" rx="4" fill="#4f8ef780" stroke="#4f8ef7" stroke-width="1.5"/>
  <text x="240" y="35" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" font-weight="bold">18</text>
  <!-- 80-90: freq=10, height=10*9.44=94, top=210-94=116 -->
  <rect x="270" y="116" width="60" height="94" rx="4" fill="#4f8ef780" stroke="#4f8ef7" stroke-width="1.5"/>
  <text x="300" y="109" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" font-weight="bold">10</text>
  <!-- 90-100: freq=5, height=47, top=163 -->
  <rect x="330" y="163" width="60" height="47" rx="4" fill="#4f8ef780" stroke="#4f8ef7" stroke-width="1.5"/>
  <text x="360" y="156" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" font-weight="bold">5</text>
  <!-- X-axis tick labels -->
  <text x="90" y="228" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">50</text>
  <text x="150" y="228" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">60</text>
  <text x="210" y="228" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">70</text>
  <text x="270" y="228" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">80</text>
  <text x="330" y="228" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">90</text>
  <text x="390" y="228" font-size="10" fill="currentColor" text-anchor="middle" font-family="sans-serif" opacity="0.7">100</text>
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
