"""Days, Weeks, Months, and Calendars — Primary 1-2 lesson."""

TITLE = "Days, Months, and Calendars"

SECTIONS = [
    {
        "title": "The Days of the Week 📅",
        "body": """<p>A <strong>week</strong> has 7 days. Learning the days of the week helps us plan what we do each day!</p>
<svg viewBox="0 0 400 280" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>The 7 Days of the Week</text>

  <!-- Days -->
  <rect x="20" y="50" width="360" height="30" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <text x="50" y="72" font-size='11' fill='#161b22;'><strong>Monday</strong></text>
  <text x="150" y="72" font-size='11' fill='#161b22;'><strong>Tuesday</strong></text>
  <text x="280" y="72" font-size='11' fill='#161b22;'><strong>Wednesday</strong></text>

  <rect x="20" y="90" width="360" height="30" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <text x="50" y="112" font-size='11' fill='#161b22;'><strong>Thursday</strong></text>
  <text x="170" y="112" font-size='11' fill='#161b22;'><strong>Friday</strong></text>
  <text x="280" y="112" font-size='11' fill='#161b22;'><strong>Saturday</strong></text>

  <rect x="20" y="130" width="360" height="30" fill='#f5d3e4' stroke='#ec4899' stroke-width="1" rx="4"/>
  <text x="50" y="152" font-size='11' fill='#161b22;'><strong>Sunday</strong></text>

  <!-- School days highlighted -->
  <text x="20" y="185" font-size='12' font-weight='bold' fill='#161b22;'>School Days:</text>
  <rect x="20" y="195" width="360" height="50" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="4"/>
  <text x="30" y="215" font-size='11' fill='#161b22;'>Monday, Tuesday, Wednesday, Thursday, Friday 🏫</text>
  <text x="30" y="235" font-size='11' fill='#161b22;'>Weekend (time for play): Saturday, Sunday 🎮</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">Remember the order:</p>
<p style="margin: 8px 0;">Mon → Tue → Wed → Thu → Fri → Sat → Sun</p>
<p style="margin: 0">Then it starts again!</p>
</div>"""
    },
    {
        "title": "The 12 Months of the Year 🗓️",
        "body": """<p>A <strong>year</strong> has 12 months. Each month has a special name and a different number of days!</p>
<svg viewBox="0 0 400 320" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22;'>The 12 Months</text>

  <!-- Months in rows -->
  <rect x="20" y="50" width="360" height="30" fill='#dcfce7' stroke='#16a34a' stroke-width="1" rx="4"/>
  <text x="50" y="72" font-size='11' fill='#161b22;'>1. January</text>
  <text x="175" y="72" font-size='11' fill='#161b22;'>2. February</text>
  <text x="310" y="72" font-size='11' fill='#161b22;'>3. March</text>

  <rect x="20" y="90" width="360" height="30" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <text x="50" y="112" font-size='11' fill='#161b22;'>4. April</text>
  <text x="175" y="112" font-size='11' fill='#161b22;'>5. May</text>
  <text x="310" y="112" font-size='11' fill='#161b22;'>6. June</text>

  <rect x="20" y="130" width="360" height="30" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <text x="50" y="152" font-size='11' fill='#161b22;'>7. July</text>
  <text x="175" y="152" font-size='11' fill='#161b22;'>8. August</text>
  <text x="310" y="152" font-size='11' fill='#161b22;'>9. September</text>

  <rect x="20" y="170" width="360" height="30" fill='#f5d3e4' stroke='#ec4899' stroke-width="1" rx="4"/>
  <text x="50" y="192" font-size='11' fill='#161b22;'>10. October</text>
  <text x="190" y="192" font-size='11' fill='#161b22;'>11. November</text>
  <text x="305" y="192" font-size='11' fill='#161b22;'>12. December</text>

  <!-- Special months -->
  <text x="20" y="230" font-size='12' font-weight='bold' fill='#161b22;'>Special months you might know:</text>
  <text x="20" y="250" font-size='11' fill='#161b22;'>🎄 December = Christmas time</text>
  <text x="20" y="268" font-size='11' fill='#161b22;'>🎂 Your birthday month = special day!</text>
  <text x="20" y="286" font-size='11' fill='#161b22;'>❄️ January, February = winter (cold)</text>
  <text x="20" y="304" font-size='11' fill='#161b22;'>☀️ July, August = summer (hot)</text>
</svg>"""
    },
    {
        "title": "Reading and Using a Calendar 📆",
        "body": """<p>A <strong>calendar</strong> shows all the days of a month so you can plan what you're doing!</p>
<svg viewBox="0 0 400 320" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="25" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22;'>A Month Calendar</text>

  <!-- Calendar frame -->
  <rect x="20" y="40" width="360" height="270" fill='#1f2937' stroke='#8b949e' stroke-width="2" rx="6"/>

  <!-- Month/year header -->
  <rect x="20" y="40" width="360" height="35" fill='#374151' stroke='none' rx="6"/>
  <text x="200" y="65" text-anchor='middle' font-size='14' font-weight='bold' fill='#e6edf3'>March 2026</text>

  <!-- Day headers -->
  <g fill='#8b949e' font-size='10' font-weight='bold'>
    <text x="35" y="90">Sun</text>
    <text x="75" y="90">Mon</text>
    <text x="115" y="90">Tue</text>
    <text x="160" y="90">Wed</text>
    <text x="200" y="90">Thu</text>
    <text x="245" y="90">Fri</text>
    <text x="285" y="90">Sat</text>
  </g>

  <line x1="20" y1="100" x2="380" y2="100" stroke='#8b949e' stroke-width="1"/>

  <!-- Dates grid -->
  <!-- Row 1: 1-7 -->
  <text x="35" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>1</text>
  <text x="75" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>2</text>
  <text x="115" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>3</text>
  <text x="160" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>4</text>
  <text x="200" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>5</text>
  <text x="245" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>6</text>
  <text x="285" y="125" text-anchor='middle' fill='#e6edf3' font-size='13'>7</text>

  <!-- Row 2: 8-14 -->
  <text x="35" y="165" text-anchor='middle' fill='#e6edf3' font-size='13'>8</text>
  <text x="75" y="165" text-anchor='middle' fill='#e6edf3' font-size='13'>9</text>
  <text x="115" y="165" text-anchor='middle' fill='#e6edf3' font-size='13'>10</text>
  <text x="160" y="165" text-anchor='middle' fill='#e6edf3' font-size='13'>11</text>
  <text x="200" y="165" text-anchor='middle' fill='#e6edf3' font-size='13'>12</text>
  <rect x="225" y="152" width="40" height="25" fill='#4f8ef7' rx="2"/>
  <text x="245" y="165" text-anchor='middle' fill='white' font-size='13' font-weight='bold'>13</text>
  <text x="285" y="165" text-anchor='middle' fill='#e6edf3' font-size='13'>14</text>

  <!-- Row 3: 15-21 -->
  <text x="35" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>15</text>
  <text x="75" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>16</text>
  <text x="115" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>17</text>
  <text x="160" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>18</text>
  <text x="200" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>19</text>
  <text x="245" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>20</text>
  <text x="285" y="205" text-anchor='middle' fill='#e6edf3' font-size='13'>21</text>

  <!-- Row 4: 22-28 -->
  <text x="35" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>22</text>
  <text x="75" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>23</text>
  <text x="115" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>24</text>
  <text x="160" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>25</text>
  <text x="200" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>26</text>
  <text x="245" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>27</text>
  <text x="285" y="245" text-anchor='middle' fill='#e6edf3' font-size='13'>28</text>

  <!-- Row 5: 29-31 -->
  <text x="35" y="285" text-anchor='middle' fill='#e6edf3' font-size='13'>29</text>
  <text x="75" y="285" text-anchor='middle' fill='#e6edf3' font-size='13'>30</text>
  <text x="115" y="285" text-anchor='middle' fill='#e6edf3' font-size='13'>31</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">How to use a calendar:</p>
<p style="margin: 8px 0;">• Look at the month and year at the top</p>
<p style="margin: 8px 0;">• Find the date you're looking for</p>
<p style="margin: 0">• See what day of the week it falls on</p>
</div>"""
    },
    {
        "title": "Time Duration: How Long Does It Take? ⏱️",
        "body": """<p>Sometimes we need to know <strong>how long something takes</strong> — the time from the start to the end.</p>
<svg viewBox="0 0 400 340" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22;'>Duration: From Start to End</text>

  <!-- Example 1: Brushing teeth -->
  <rect x="20" y="50" width="360" height="60" fill='#e0f2fe' stroke='#0284c7' stroke-width="2" rx="6"/>
  <text x="30" y="75" font-size='12' font-weight='bold' fill='#161b22;'>🪥 Brushing teeth</text>
  <text x="30" y="93" font-size='11' fill='#666;'>Start: 8:00 AM</text>
  <text x="200" y="93" font-size='11' fill='#666;'>End: 8:02 AM</text>
  <text x="30" y="108" font-size='11' fill='#161b22;'>Duration: <strong>2 minutes</strong></text>

  <!-- Example 2: Playing at recess -->
  <rect x="20" y="120" width="360" height="60" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="6"/>
  <text x="30" y="145" font-size='12' font-weight='bold' fill='#161b22;'>🎮 Playing at recess</text>
  <text x="30" y="163" font-size='11' fill='#666;'>Start: 10:00 AM</text>
  <text x="200" y="163" font-size='11' fill='#666;'>End: 10:15 AM</text>
  <text x="30" y="178" font-size='11' fill='#161b22;'>Duration: <strong>15 minutes</strong></text>

  <!-- Example 3: Watching a movie -->
  <rect x="20" y="190" width="360" height="60" fill='#f5d3e4' stroke='#ec4899' stroke-width="2" rx="6"/>
  <text x="30" y="215" font-size='12' font-weight='bold' fill='#161b22;'>🎬 Watching a movie</text>
  <text x="30" y="233" font-size='11' fill='#666;'>Start: 2:00 PM</text>
  <text x="200" y="233" font-size='11' fill='#666;'>End: 3:30 PM</text>
  <text x="30" y="248" font-size='11' fill='#161b22;'>Duration: <strong>1 hour 30 minutes</strong></text>

  <!-- Example 4: School day -->
  <rect x="20" y="260" width="360" height="60" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="6"/>
  <text x="30" y="285" font-size='12' font-weight='bold' fill='#161b22;'>🏫 School day</text>
  <text x="30" y="303" font-size='11' fill='#666;'>Start: 8:30 AM</text>
  <text x="200" y="303" font-size='11' fill='#666;'>End: 3:00 PM</text>
  <text x="30" y="318" font-size='11' fill='#161b22;'>Duration: <strong>6 hours 30 minutes</strong></text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">How to find duration:</p>
<p style="margin: 8px 0;">1. Note the start time</p>
<p style="margin: 8px 0;">2. Note the end time</p>
<p style="margin: 0">3. Count how much time passed</p>
</div>"""
    }
]
