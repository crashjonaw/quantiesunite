"""Reading Minutes in 5-Minute Intervals — Primary 1-2 lesson."""

TITLE = "Reading Minutes: Counting by 5s"

SECTIONS = [
    {
        "title": "The Magic Pattern: Every Number = 5 Minutes ✨",
        "body": """<p>Here's a super useful pattern to remember: <strong>Each number on the clock represents 5 minutes.</strong></p>
<p>This makes it easy to read any time!</p>
<svg viewBox="0 0 400 300" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>The 5-Minute Pattern</text>

  <!-- Clock -->
  <circle cx="200" cy="140" r="90" fill='#1f2937' stroke='#e5e7eb' stroke-width="3"/>

  <!-- Numbers with their minute equivalents -->
  <text x="200" y="65" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>12</text>
  <text x="200" y="58" text-anchor='middle' fill='#22c55e' font-size='12'>0 min</text>

  <text x="268" y="150" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>3</text>
  <text x="278" y="150" text-anchor='middle' fill='#22c55e' font-size='12'>15 min</text>

  <text x="200" y="230" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>6</text>
  <text x="200" y="250" text-anchor='middle' fill='#22c55e' font-size='12'>30 min</text>

  <text x="132" y="150" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>9</text>
  <text x="110" y="150" text-anchor='middle' fill='#22c55e' font-size='12'>45 min</text>

  <!-- Center dot -->
  <circle cx="200" cy="140" r="5" fill='#e5e7eb'/>

  <!-- Center text -->
  <text x="200" y="230" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22' dy="-80">1 = 5 min</text>
  <text x="200" y="230" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22' dy="-65">2 = 10 min</text>
  <text x="200" y="230" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22' dy="-50">3 = 15 min</text>

  <!-- Bottom explanation -->
  <rect x="20" y="270" width="360" height="25" fill='#f0f8ff' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="200" y="290" text-anchor='middle' font-size='11' fill='#161b22'>Count: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px;">
<p style="margin: 0; font-weight: bold;">The core rule:</p>
<p style="margin: 8px 0;">Number on clock × 5 = minutes past the hour</p>
<p style="margin: 0">Example: The 7 = 7 × 5 = 35 minutes</p>
</div>"""
    },
    {
        "title": "Counting Minutes: How to Read Any Time",
        "body": """<p>Using the 5-minute pattern, you can read ANY time on the clock in 5-minute intervals!</p>
<p>Start at 12 and count by 5s until you reach where the minute hand is pointing.</p>
<svg viewBox="0 0 400 380" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Counting by 5s Around the Clock</text>

  <!-- Clock with numbers -->
  <circle cx="200" cy="160" r="80" fill='#1f2937' stroke='#e5e7eb' stroke-width="3"/>

  <!-- All 12 numbers -->
  <text x="200" y="88" text-anchor='middle' fill='currentColor' font-size='14'>12</text>
  <text x="234" y="98" text-anchor='middle' fill='currentColor' font-size='14'>1</text>
  <text x="263" y="120" text-anchor='middle' fill='currentColor' font-size='14'>2</text>
  <text x="280" y="150" text-anchor='middle' fill='currentColor' font-size='14'>3</text>
  <text x="263" y="200" text-anchor='middle' fill='currentColor' font-size='14'>5</text>
  <text x="234" y="222" text-anchor='middle' fill='currentColor' font-size='14'>7</text>
  <text x="200" y="232" text-anchor='middle' fill='currentColor' font-size='14'>6</text>
  <text x="166" y="222" text-anchor='middle' fill='currentColor' font-size='14'>8</text>
  <text x="137" y="200" text-anchor='middle' fill='currentColor' font-size='14'>9</text>
  <text x="120" y="150" text-anchor='middle' fill='currentColor' font-size='14'>10</text>
  <text x="137" y="120" text-anchor='middle' fill='currentColor' font-size='14'>11</text>

  <!-- Minutes outside the clock -->
  <text x="200" y="72" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>0</text>
  <text x="237" y="80" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>5</text>
  <text x="268" y="103" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>10</text>
  <text x="290" y="150" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>15</text>
  <text x="268" y="217" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>25</text>
  <text x="237" y="240" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>35</text>
  <text x="200" y="252" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>30</text>
  <text x="163" y="240" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>40</text>
  <text x="132" y="217" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>45</text>
  <text x="110" y="150" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>50</text>
  <text x="132" y="103" text-anchor='middle' fill='#22c55e' font-size='11' font-weight='bold'>55</text>

  <!-- Center dot -->
  <circle cx="200" cy="160" r="4" fill='#e5e7eb'/>

  <!-- Examples below -->
  <text x="20" y="280" font-size='12' font-weight='bold' fill='#161b22'>Practice Examples:</text>

  <!-- Example 1 -->
  <rect x="20" y="295" width="360" height="30" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <text x="30" y="317" font-size='11' fill='#161b22;'>Minute hand points at 4: Count 5, 10, 15, 20 = <strong>20 minutes</strong> (like 3:20)</text>

  <!-- Example 2 -->
  <rect x="20" y="335" width="360" height="30" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <text x="30" y="357" font-size='11' fill='#161b22;'>Minute hand points at 8: Count 5, 10, 15, 20, 25, 30, 35, 40 = <strong>40 minutes</strong> (like 2:40)</text>
</svg>"""
    },
    {
        "title": "Reading Times: Putting It All Together",
        "body": """<p>Now you can read ANY time! Use the hour hand + the minute hand together.</p>
<svg viewBox="0 0 380 400" style="width:100%;max-width:380px;display:block;margin:20px auto;">
  <text x="190" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Practice Reading Times</text>

  <!-- Time 1: 2:17 -->
  <g>
    <circle cx="90" cy="90" r="40" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
    <text x="90" y="58" text-anchor='middle' fill='currentColor' font-size='11'>12</text>
    <text x="120" y="95" text-anchor='middle' fill='currentColor' font-size='11'>3</text>
    <text x="90" y="125" text-anchor='middle' fill='currentColor' font-size='11'>6</text>
    <text x="60" y="95" text-anchor='middle' fill='currentColor' font-size='11'>9</text>
    <!-- Hour hand to 2 -->
    <line x1="90" y1="90" x2="98" y2="68" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand to 3.4 (between 3 and 4) -->
    <line x1="90" y1="90" x2="118" y2="88" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="90" cy="90" r="2" fill='#e5e7eb'/>
    <text x="90" y="150" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>2:17</text>
    <text x="90" y="163" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(counting by 5s)</text>
  </g>

  <!-- Time 2: 5:33 -->
  <g>
    <circle cx="280" cy="90" r="40" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
    <text x="280" y="58" text-anchor='middle' fill='currentColor' font-size='11'>12</text>
    <text x="310" y="95" text-anchor='middle' fill='currentColor' font-size='11'>3</text>
    <text x="280" y="125" text-anchor='middle' fill='currentColor' font-size='11'>6</text>
    <text x="250" y="95" text-anchor='middle' fill='currentColor' font-size='11'>9</text>
    <!-- Hour hand to 5 -->
    <line x1="280" y1="90" x2="298" y2="108" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand between 6 and 7 -->
    <line x1="280" y1="90" x2="283" y2="130" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="280" cy="90" r="2" fill='#e5e7eb'/>
    <text x="280" y="150" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>5:33</text>
    <text x="280" y="163" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(between 30 & 35)</text>
  </g>

  <!-- Time 3: 8:52 -->
  <g>
    <circle cx="90" cy="250" r="40" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
    <text x="90" y="218" text-anchor='middle' fill='currentColor' font-size='11'>12</text>
    <text x="120" y="255" text-anchor='middle' fill='currentColor' font-size='11'>3</text>
    <text x="90" y="285" text-anchor='middle' fill='currentColor' font-size='11'>6</text>
    <text x="60" y="255" text-anchor='middle' fill='currentColor' font-size='11'>9</text>
    <!-- Hour hand to 8 -->
    <line x1="90" y1="250" x2="78" y2="225" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand between 10 and 11 -->
    <line x1="90" y1="250" x2="72" y2="250" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="90" cy="250" r="2" fill='#e5e7eb'/>
    <text x="90" y="310" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>8:52</text>
    <text x="90" y="323" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(near 50, count to 52)</text>
  </g>

  <!-- Time 4: 11:26 -->
  <g>
    <circle cx="280" cy="250" r="40" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
    <text x="280" y="218" text-anchor='middle' fill='currentColor' font-size='11'>12</text>
    <text x="310" y="255" text-anchor='middle' fill='currentColor' font-size='11'>3</text>
    <text x="280" y="285" text-anchor='middle' fill='currentColor' font-size='11'>6</text>
    <text x="250" y="255" text-anchor='middle' fill='currentColor' font-size='11'>9</text>
    <!-- Hour hand to 11 -->
    <line x1="280" y1="250" x2="283" y2="218" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand between 5 and 6 -->
    <line x1="280" y1="250" x2="306" y2="253" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="280" cy="250" r="2" fill='#e5e7eb'/>
    <text x="280" y="310" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>11:26</text>
    <text x="280" y="323" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(between 25 & 30)</text>
  </g>

  <!-- Explanation -->
  <rect x="20" y="365" width="340" height="30" fill='#f0f8ff' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="190" y="385" text-anchor='middle' font-size='10' fill='#161b22'>Start at 12 and count by 5s where the minute hand points!</text>
</svg>"""
    },
    {
        "title": "AM and PM: Morning vs Afternoon/Evening ⏰",
        "body": """<p>The same times happen twice in a day! We use <strong>AM</strong> (morning) and <strong>PM</strong> (afternoon/evening) to tell the difference.</p>
<svg viewBox="0 0 400 280" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>AM vs PM</text>

  <!-- AM side -->
  <rect x="20" y="50" width="170" height="220" fill='#fff7ed' stroke='#ea580c' stroke-width="2" rx="6"/>
  <text x="105" y="80" text-anchor='middle' font-size='14' font-weight='bold' fill='#161b22'>🌅 AM</text>
  <text x="105" y="100" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Ante Meridiem)</text>
  <text x="105" y="120" text-anchor='middle' font-size='11' font-weight='bold' fill='#161b22'>Morning Time</text>

  <text x="30" y="145" font-size='11' fill='#161b22;'>6:00 AM = sunrise</text>
  <text x="30" y="163" font-size='11' fill='#161b22;'>7:00 AM = wake up</text>
  <text x="30" y="181" font-size='11' fill='#161b22;'>8:00 AM = school</text>
  <text x="30" y="199" font-size='11' fill='#161b22;'>12:00 PM = noon</text>

  <text x="105" y="235" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>Before noon</text>

  <!-- PM side -->
  <rect x="210" y="50" width="170" height="220" fill='#e0e7ff' stroke='#6366f1' stroke-width="2" rx="6"/>
  <text x="295" y="80" text-anchor='middle' font-size='14' font-weight='bold' fill='#161b22'>🌆 PM</text>
  <text x="295" y="100" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Post Meridiem)</text>
  <text x="295" y="120" text-anchor='middle' font-size='11' font-weight='bold' fill='#161b22'>Afternoon/Evening</text>

  <text x="220" y="145" font-size='11' fill='#161b22;'>1:00 PM = afternoon</text>
  <text x="220" y="163" font-size='11' fill='#161b22;'>3:00 PM = leave school</text>
  <text x="220" y="181" font-size='11' fill='#161b22;'>6:00 PM = dinner</text>
  <text x="220" y="199" font-size='11' fill='#161b22;'>9:00 PM = bedtime</text>

  <text x="295" y="235" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>After noon</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px;">
<p style="margin: 0; font-weight: bold;">Remember:</p>
<p style="margin: 8px 0;">• AM = morning (dawn to noon)</p>
<p style="margin: 8px 0;">• PM = afternoon and evening (noon to midnight)</p>
<p style="margin: 0">• 12:00 PM = noon (middle of day)</p>
</div>"""
    }
]
