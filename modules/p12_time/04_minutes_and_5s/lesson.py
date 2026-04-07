"""Reading Minutes in 5-Minute Intervals — Primary 1-2 lesson."""

TITLE = "Reading Minutes: Counting by 5s"

SECTIONS = [
    {
        "title": "The Magic Pattern: Every Number = 5 Minutes",
        "body": """<p>Here's a super useful pattern to remember: <strong>Each number on the clock represents 5 minutes.</strong></p>
<p>This makes it easy to read any time!</p>
<svg viewBox="0 0 420 420" style="width:100%;max-width:420px;display:block;margin:20px auto;">
  <text x="210" y="24" text-anchor='middle' font-size='15' font-weight='bold' fill='currentColor'>The 5-Minute Pattern</text>

  <!-- Clock face -->
  <circle cx="210" cy="210" r="160" fill='#fff' stroke='#8B0000' stroke-width="3"/>
  <!-- Inner ring for minute labels -->
  <circle cx="210" cy="210" r="130" fill='none' stroke='#e5e7eb' stroke-width="1" stroke-dasharray="4,4"/>

  <!-- All 12 numbers (outer) with minute equivalents (inner, green) -->
  <!-- 12 = 0 min -->
  <text x="210" y="72" text-anchor='middle' fill='#000' font-size='18' font-weight='bold'>12</text>
  <text x="210" y="100" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:00</text>
  <!-- 1 = 5 min -->
  <text x="289" y="88" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>1</text>
  <text x="272" y="112" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:05</text>
  <!-- 2 = 10 min -->
  <text x="340" y="140" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>2</text>
  <text x="316" y="148" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:10</text>
  <!-- 3 = 15 min -->
  <text x="355" y="216" text-anchor='middle' fill='#000' font-size='18' font-weight='bold'>3</text>
  <text x="326" y="216" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:15</text>
  <!-- 4 = 20 min -->
  <text x="340" y="290" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>4</text>
  <text x="316" y="280" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:20</text>
  <!-- 5 = 25 min -->
  <text x="289" y="342" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>5</text>
  <text x="272" y="322" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:25</text>
  <!-- 6 = 30 min -->
  <text x="210" y="358" text-anchor='middle' fill='#000' font-size='18' font-weight='bold'>6</text>
  <text x="210" y="334" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:30</text>
  <!-- 7 = 35 min -->
  <text x="131" y="342" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>7</text>
  <text x="148" y="322" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:35</text>
  <!-- 8 = 40 min -->
  <text x="80" y="290" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>8</text>
  <text x="104" y="280" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:40</text>
  <!-- 9 = 45 min -->
  <text x="65" y="216" text-anchor='middle' fill='#000' font-size='18' font-weight='bold'>9</text>
  <text x="94" y="216" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:45</text>
  <!-- 10 = 50 min -->
  <text x="80" y="140" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>10</text>
  <text x="104" y="148" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:50</text>
  <!-- 11 = 55 min -->
  <text x="131" y="88" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>11</text>
  <text x="148" y="112" text-anchor='middle' fill='#16a34a' font-size='12' font-weight='bold'>:55</text>

  <!-- Center dot -->
  <circle cx="210" cy="210" r="4" fill='#1a1a2e'/>

  <!-- Bottom rule box -->
  <rect x="55" y="385" width="310" height="28" fill='#f0fdf4' stroke='#16a34a' stroke-width="1" rx="4"/>
  <text x="210" y="404" text-anchor='middle' font-size='11' fill='#000' font-weight='bold'>Number on clock × 5 = minutes past the hour</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">The core rule:</p>
<p style="margin: 8px 0;">Number on clock x 5 = minutes past the hour</p>
<p style="margin: 0">Example: The 7 = 7 x 5 = 35 minutes</p>
</div>"""
    },
    {
        "title": "Counting Minutes: How to Read Any Time",
        "body": """<p>Using the 5-minute pattern, you can read ANY time on the clock in 5-minute intervals!</p>
<p>Start at 12 and count by 5s until you reach where the minute hand is pointing.</p>
<svg viewBox="0 0 415 390" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <text x="207" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>Counting by 5s Around the Clock</text>

  <!-- Clock with numbers -->
  <circle cx="207" cy="165" r="85" fill='#fff' stroke='#8B0000' stroke-width="3"/>

  <!-- All 12 numbers -->
  <text x="207" y="92" text-anchor='middle' fill='#000' font-size='14'>12</text>
  <text x="242" y="103" text-anchor='middle' fill='#000' font-size='14'>1</text>
  <text x="270" y="125" text-anchor='middle' fill='#000' font-size='14'>2</text>
  <text x="280" y="172" text-anchor='middle' fill='#000' font-size='14'>3</text>
  <text x="270" y="210" text-anchor='middle' fill='#000' font-size='14'>4</text>
  <text x="242" y="232" text-anchor='middle' fill='#000' font-size='14'>5</text>
  <text x="207" y="242" text-anchor='middle' fill='#000' font-size='14'>6</text>
  <text x="172" y="232" text-anchor='middle' fill='#000' font-size='14'>7</text>
  <text x="144" y="210" text-anchor='middle' fill='#000' font-size='14'>8</text>
  <text x="134" y="172" text-anchor='middle' fill='#000' font-size='14'>9</text>
  <text x="144" y="125" text-anchor='middle' fill='#000' font-size='14'>10</text>
  <text x="172" y="103" text-anchor='middle' fill='#000' font-size='14'>11</text>

  <!-- Minutes outside the clock -->
  <text x="207" y="75" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>0</text>
  <text x="248" y="86" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>5</text>
  <text x="280" y="110" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>10</text>
  <text x="298" y="172" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>15</text>
  <text x="280" y="225" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>20</text>
  <text x="248" y="248" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>25</text>
  <text x="207" y="260" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>30</text>
  <text x="166" y="248" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>35</text>
  <text x="134" y="225" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>40</text>
  <text x="116" y="172" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>45</text>
  <text x="134" y="110" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>50</text>
  <text x="166" y="86" text-anchor='middle' fill='#22c55e' font-size='10' font-weight='bold'>55</text>

  <!-- Center dot -->
  <circle cx="207" cy="165" r="4" fill='#1a1a2e'/>

  <!-- Examples below -->
  <text x="15" y="288" font-size='12' font-weight='bold' fill='currentColor'>Practice Examples:</text>

  <!-- Example 1 -->
  <rect x="15" y="302" width="385" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <text x="25" y="323" font-size='11' fill='currentColor'>Minute hand points at 4: Count 5, 10, 15, 20 = 20 minutes (like 3:20)</text>

  <!-- Example 2 -->
  <rect x="15" y="346" width="385" height="32" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <text x="25" y="367" font-size='11' fill='currentColor'>Minute hand points at 8: Count 5, 10, 15, 20, 25, 30, 35, 40 = 40 minutes</text>
</svg>"""
    },
    {
        "title": "Reading Times: Putting It All Together",
        "body": """<p>Now you can read ANY time! Use the hour hand + the minute hand together.</p>
<svg viewBox="0 0 395 410" style="width:100%;max-width:395px;display:block;margin:20px auto;">
  <text x="197" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>Practice Reading Times</text>

  <!-- Time 1: 2:15 -->
  <g>
    <circle cx="95" cy="95" r="45" fill='#fff' stroke='#8B0000' stroke-width="2"/>
    <text x="95" y="62" text-anchor='middle' fill='#000' font-size='11'>12</text>
    <text x="130" y="100" text-anchor='middle' fill='#000' font-size='11'>3</text>
    <text x="95" y="135" text-anchor='middle' fill='#000' font-size='11'>6</text>
    <text x="60" y="100" text-anchor='middle' fill='#000' font-size='11'>9</text>
    <!-- Hour hand to 2 -->
    <line x1="95" y1="95" x2="103" y2="68" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand to 3 (15 min) -->
    <line x1="95" y1="95" x2="128" y2="100" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="95" cy="95" r="2" fill='#1a1a2e'/>
    <text x="95" y="160" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>2:15</text>
    <text x="95" y="175" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(Quarter past 2)</text>
  </g>

  <!-- Time 2: 5:35 -->
  <g>
    <circle cx="290" cy="95" r="45" fill='#fff' stroke='#8B0000' stroke-width="2"/>
    <text x="290" y="62" text-anchor='middle' fill='#000' font-size='11'>12</text>
    <text x="325" y="100" text-anchor='middle' fill='#000' font-size='11'>3</text>
    <text x="290" y="135" text-anchor='middle' fill='#000' font-size='11'>6</text>
    <text x="255" y="100" text-anchor='middle' fill='#000' font-size='11'>9</text>
    <!-- Hour hand to 5 -->
    <line x1="290" y1="95" x2="308" y2="115" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand to 7 (35 min) -->
    <line x1="290" y1="95" x2="272" y2="130" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="290" cy="95" r="2" fill='#1a1a2e'/>
    <text x="290" y="160" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>5:35</text>
    <text x="290" y="175" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(between 35 and 40)</text>
  </g>

  <!-- Time 3: 8:50 -->
  <g>
    <circle cx="95" cy="260" r="45" fill='#fff' stroke='#8B0000' stroke-width="2"/>
    <text x="95" y="227" text-anchor='middle' fill='#000' font-size='11'>12</text>
    <text x="130" y="265" text-anchor='middle' fill='#000' font-size='11'>3</text>
    <text x="95" y="300" text-anchor='middle' fill='#000' font-size='11'>6</text>
    <text x="60" y="265" text-anchor='middle' fill='#000' font-size='11'>9</text>
    <!-- Hour hand to 8 -->
    <line x1="95" y1="260" x2="73" y2="280" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand to 10 (50 min) -->
    <line x1="95" y1="260" x2="68" y2="245" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="95" cy="260" r="2" fill='#1a1a2e'/>
    <text x="95" y="325" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>8:50</text>
    <text x="95" y="340" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(at 50 minutes)</text>
  </g>

  <!-- Time 4: 11:25 -->
  <g>
    <circle cx="290" cy="260" r="45" fill='#fff' stroke='#8B0000' stroke-width="2"/>
    <text x="290" y="227" text-anchor='middle' fill='#000' font-size='11'>12</text>
    <text x="325" y="265" text-anchor='middle' fill='#000' font-size='11'>3</text>
    <text x="290" y="300" text-anchor='middle' fill='#000' font-size='11'>6</text>
    <text x="255" y="265" text-anchor='middle' fill='#000' font-size='11'>9</text>
    <!-- Hour hand to 11 -->
    <line x1="290" y1="260" x2="282" y2="228" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
    <!-- Minute hand to 5 (25 min) -->
    <line x1="290" y1="260" x2="315" y2="290" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
    <circle cx="290" cy="260" r="2" fill='#1a1a2e'/>
    <text x="290" y="325" text-anchor='middle' font-size='12' font-weight='bold' fill='currentColor'>11:25</text>
    <text x="290" y="340" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>(at 25 minutes)</text>
  </g>

  <!-- Explanation -->
  <rect x="15" y="375" width="365" height="28" fill='#f0f8ff' stroke='#4f8ef7' stroke-width="1" rx="4"/>
  <text x="197" y="394" text-anchor='middle' font-size='10' fill='currentColor'>Start at 12 and count by 5s where the minute hand points!</text>
</svg>"""
    },
    {
        "title": "AM and PM: Morning vs Afternoon/Evening ⏰",
        "body": """<p>The same times happen twice in a day! We use <strong>AM</strong> (morning) and <strong>PM</strong> (afternoon/evening) to tell the difference.</p>
<svg viewBox="0 0 415 290" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <text x="207" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>AM vs PM</text>

  <!-- AM side -->
  <rect x="15" y="48" width="185" height="225" fill='#fff7ed' stroke='#ea580c' stroke-width="2" rx="4"/>
  <text x="107" y="78" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>AM</text>
  <text x="107" y="98" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Ante Meridiem)</text>
  <text x="107" y="118" text-anchor='middle' font-size='11' font-weight='bold' fill='currentColor'>Morning Time</text>

  <text x="30" y="145" font-size='11' fill='currentColor'>6:00 AM = sunrise</text>
  <text x="30" y="165" font-size='11' fill='currentColor'>7:00 AM = wake up</text>
  <text x="30" y="185" font-size='11' fill='currentColor'>8:00 AM = school</text>
  <text x="30" y="205" font-size='11' fill='currentColor'>12:00 PM = noon</text>

  <text x="107" y="240" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>Before noon</text>

  <!-- PM side -->
  <rect x="215" y="48" width="185" height="225" fill='#e0e7ff' stroke='#6366f1' stroke-width="2" rx="4"/>
  <text x="307" y="78" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>PM</text>
  <text x="307" y="98" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Post Meridiem)</text>
  <text x="307" y="118" text-anchor='middle' font-size='11' font-weight='bold' fill='currentColor'>Afternoon/Evening</text>

  <text x="230" y="145" font-size='11' fill='currentColor'>1:00 PM = afternoon</text>
  <text x="230" y="165" font-size='11' fill='currentColor'>3:00 PM = leave school</text>
  <text x="230" y="185" font-size='11' fill='currentColor'>6:00 PM = dinner</text>
  <text x="230" y="205" font-size='11' fill='currentColor'>9:00 PM = bedtime</text>

  <text x="307" y="240" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>After noon</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">Remember:</p>
<p style="margin: 8px 0;">AM = morning (dawn to noon)</p>
<p style="margin: 8px 0;">PM = afternoon and evening (noon to midnight)</p>
<p style="margin: 0">12:00 PM = noon (middle of day)</p>
</div>"""
    }
]
