"""Days, Weeks, Months, and Calendars — Primary 1-2 lesson."""

TITLE = "Days, Months, and Calendars"

SECTIONS = [
    {
        "title": "The Days of the Week",
        "body": """<p>A <strong>week</strong> has 7 days. Learning the days of the week helps us plan what we do each day!</p>
<svg viewBox="0 0 415 345" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <text x="207" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>The 7 Days of the Week</text>

  <!-- Day boxes - one per day in a grid -->
  <rect x="25" y="46" width="170" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="4"/>
  <text x="110" y="67" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Monday</text>

  <rect x="220" y="46" width="170" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="4"/>
  <text x="305" y="67" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Tuesday</text>

  <rect x="25" y="88" width="170" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="4"/>
  <text x="110" y="109" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Wednesday</text>

  <rect x="220" y="88" width="170" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="4"/>
  <text x="305" y="109" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Thursday</text>

  <rect x="25" y="130" width="170" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="4"/>
  <text x="110" y="151" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Friday</text>

  <rect x="220" y="130" width="170" height="32" fill='#fef3c7' stroke='#d97706' stroke-width="1.5" rx="4"/>
  <text x="305" y="151" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Saturday</text>

  <rect x="25" y="172" width="170" height="32" fill='#fef3c7' stroke='#d97706' stroke-width="1.5" rx="4"/>
  <text x="110" y="193" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Sunday</text>

  <!-- Arrows showing order -->
  <text x="200" y="67" text-anchor='middle' font-size='14' fill='#1a1a2e'>-></text>
  <text x="200" y="109" text-anchor='middle' font-size='14' fill='#1a1a2e'>-></text>
  <text x="200" y="151" text-anchor='middle' font-size='14' fill='#1a1a2e'>-></text>

  <!-- Divider -->
  <line x1="25" y1="220" x2="390" y2="220" stroke='currentColor' stroke-width="0.5" opacity="0.3"/>

  <!-- School days vs weekend -->
  <text x="207" y="245" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>School Days vs Weekend</text>

  <rect x="25" y="258" width="220" height="36" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="4"/>
  <text x="135" y="281" text-anchor='middle' font-size='11' fill='#1a1a2e'>Mon, Tue, Wed, Thu, Fri</text>

  <rect x="260" y="258" width="130" height="36" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="4"/>
  <text x="325" y="281" text-anchor='middle' font-size='11' fill='#1a1a2e'>Sat, Sun</text>

  <text x="135" y="310" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.7'>5 school days</text>
  <text x="325" y="310" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.7'>2 weekend days</text>

  <text x="207" y="338" text-anchor='middle' font-size='12' fill='currentColor'>5 + 2 = 7 days in a week!</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">Remember the order:</p>
<p style="margin: 8px 0;">Mon, Tue, Wed, Thu, Fri, Sat, Sun</p>
<p style="margin: 0">Then it starts again!</p>
</div>"""
    },
    {
        "title": "The 12 Months of the Year",
        "body": """<p>A <strong>year</strong> has 12 months. Each month has a special name and a different number of days!</p>
<svg viewBox="0 0 455 430" style="width:100%;max-width:455px;display:block;margin:20px auto;">
  <text x="227" y="28" text-anchor='middle' font-size='18' font-weight='bold' fill='currentColor'>The 12 Months of the Year</text>

  <!-- Row 1: Winter/Spring — Jan, Feb, Mar, Apr -->
  <rect x="15" y="46" width="102" height="52" fill='#bfdbfe' stroke='#3b82f6' stroke-width="1.5" rx="4"/>
  <text x="66" y="67" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>1</text>
  <text x="66" y="86" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>January</text>

  <rect x="125" y="46" width="102" height="52" fill='#c7d2fe' stroke='#6366f1' stroke-width="1.5" rx="4"/>
  <text x="176" y="67" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>2</text>
  <text x="176" y="86" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>February</text>

  <rect x="235" y="46" width="102" height="52" fill='#bbf7d0' stroke='#22c55e' stroke-width="1.5" rx="4"/>
  <text x="286" y="67" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>3</text>
  <text x="286" y="86" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>March</text>

  <rect x="345" y="46" width="96" height="52" fill='#d9f99d' stroke='#84cc16' stroke-width="1.5" rx="4"/>
  <text x="393" y="67" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>4</text>
  <text x="393" y="86" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>April</text>

  <!-- Row 2: Spring/Summer — May, Jun, Jul, Aug -->
  <rect x="15" y="110" width="102" height="52" fill='#a7f3d0' stroke='#10b981' stroke-width="1.5" rx="4"/>
  <text x="66" y="131" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>5</text>
  <text x="66" y="150" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>May</text>

  <rect x="125" y="110" width="102" height="52" fill='#fef08a' stroke='#eab308' stroke-width="1.5" rx="4"/>
  <text x="176" y="131" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>6</text>
  <text x="176" y="150" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>June</text>

  <rect x="235" y="110" width="102" height="52" fill='#fed7aa' stroke='#f97316' stroke-width="1.5" rx="4"/>
  <text x="286" y="131" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>7</text>
  <text x="286" y="150" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>July</text>

  <rect x="345" y="110" width="96" height="52" fill='#fecaca' stroke='#ef4444' stroke-width="1.5" rx="4"/>
  <text x="393" y="131" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>8</text>
  <text x="393" y="150" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>August</text>

  <!-- Row 3: Autumn/Winter — Sep, Oct, Nov, Dec -->
  <rect x="15" y="174" width="102" height="52" fill='#fde68a' stroke='#d97706' stroke-width="1.5" rx="4"/>
  <text x="66" y="195" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>9</text>
  <text x="66" y="214" text-anchor='middle' font-size='12' font-weight='bold' fill='#1a1a2e'>September</text>

  <rect x="125" y="174" width="102" height="52" fill='#fdba74' stroke='#ea580c' stroke-width="1.5" rx="4"/>
  <text x="176" y="195" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>10</text>
  <text x="176" y="214" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>October</text>

  <rect x="235" y="174" width="102" height="52" fill='#e9d5ff' stroke='#a855f7' stroke-width="1.5" rx="4"/>
  <text x="286" y="195" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>11</text>
  <text x="286" y="214" text-anchor='middle' font-size='12' font-weight='bold' fill='#1a1a2e'>November</text>

  <rect x="345" y="174" width="96" height="52" fill='#dbeafe' stroke='#2563eb' stroke-width="1.5" rx="4"/>
  <text x="393" y="195" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>12</text>
  <text x="393" y="214" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>December</text>

  <!-- Season legend -->
  <line x1="15" y1="245" x2="441" y2="245" stroke='currentColor' stroke-width="0.5" opacity="0.2"/>
  <text x="227" y="270" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Seasons at a Glance</text>

  <rect x="15" y="286" width="16" height="16" fill='#bfdbfe' rx="4"/>
  <text x="37" y="299" font-size='12' fill='currentColor'>Winter (Dec-Feb)</text>

  <rect x="175" y="286" width="16" height="16" fill='#bbf7d0' rx="4"/>
  <text x="197" y="299" font-size='12' fill='currentColor'>Spring (Mar-May)</text>

  <rect x="15" y="312" width="16" height="16" fill='#fed7aa' rx="4"/>
  <text x="37" y="325" font-size='12' fill='currentColor'>Summer (Jun-Aug)</text>

  <rect x="175" y="312" width="16" height="16" fill='#fde68a' rx="4"/>
  <text x="197" y="325" font-size='12' fill='currentColor'>Autumn (Sep-Nov)</text>

  <!-- Fun facts -->
  <line x1="15" y1="340" x2="441" y2="340" stroke='currentColor' stroke-width="0.5" opacity="0.2"/>
  <text x="227" y="365" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Fun Facts</text>
  <text x="227" y="390" text-anchor='middle' font-size='12' fill='currentColor'>December = Christmas time</text>
  <text x="227" y="410" text-anchor='middle' font-size='12' fill='currentColor'>Your birthday month is special!</text>
</svg>"""
    },
    {
        "title": "Reading and Using a Calendar",
        "body": """<p>A <strong>calendar</strong> shows all the days of a month so you can plan what you're doing!</p>
<svg viewBox="0 0 535 430" style="width:100%;max-width:535px;display:block;margin:20px auto;">
  <text x="267" y="28" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>A Month Calendar</text>

  <!-- Calendar frame -->
  <rect x="15" y="48" width="505" height="360" fill='#f0f4f8' stroke='currentColor' stroke-width="2" rx="4"/>

  <!-- Month/year header -->
  <rect x="15" y="48" width="505" height="42" fill='#e0eaff' stroke='none' rx="4"/>
  <rect x="15" y="78" width="505" height="12" fill='#e0eaff' stroke='none'/>
  <text x="267" y="78" text-anchor='middle' font-size='18' font-weight='bold' fill='#1a1a2e'>March 2026</text>

  <!-- Day headers -->
  <text x="52" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Sun</text>
  <text x="124" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Mon</text>
  <text x="196" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Tue</text>
  <text x="268" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Wed</text>
  <text x="340" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Thu</text>
  <text x="412" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Fri</text>
  <text x="484" y="115" text-anchor='middle' font-size='14' font-weight='bold' fill='#1a1a2e'>Sat</text>

  <line x1="25" y1="125" x2="510" y2="125" stroke='currentColor' stroke-width="1" opacity="0.3"/>

  <!-- Dates grid -->
  <!-- Row 1: 1-7 -->
  <text x="52" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>1</text>
  <text x="124" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>2</text>
  <text x="196" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>3</text>
  <text x="268" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>4</text>
  <text x="340" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>5</text>
  <text x="412" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>6</text>
  <text x="484" y="155" text-anchor='middle' fill='#1a1a2e' font-size='16'>7</text>

  <!-- Row 2: 8-14 -->
  <text x="52" y="200" text-anchor='middle' fill='#1a1a2e' font-size='16'>8</text>
  <text x="124" y="200" text-anchor='middle' fill='#1a1a2e' font-size='16'>9</text>
  <text x="196" y="200" text-anchor='middle' fill='#1a1a2e' font-size='16'>10</text>
  <text x="268" y="200" text-anchor='middle' fill='#1a1a2e' font-size='16'>11</text>
  <text x="340" y="200" text-anchor='middle' fill='#1a1a2e' font-size='16'>12</text>
  <rect x="388" y="184" width="48" height="28" fill='#3b82f6' rx="4"/>
  <text x="412" y="204" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>13</text>
  <text x="484" y="200" text-anchor='middle' fill='#1a1a2e' font-size='16'>14</text>

  <!-- Row 3: 15-21 -->
  <text x="52" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>15</text>
  <text x="124" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>16</text>
  <text x="196" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>17</text>
  <text x="268" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>18</text>
  <text x="340" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>19</text>
  <text x="412" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>20</text>
  <text x="484" y="245" text-anchor='middle' fill='#1a1a2e' font-size='16'>21</text>

  <!-- Row 4: 22-28 -->
  <text x="52" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>22</text>
  <text x="124" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>23</text>
  <text x="196" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>24</text>
  <text x="268" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>25</text>
  <text x="340" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>26</text>
  <text x="412" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>27</text>
  <text x="484" y="290" text-anchor='middle' fill='#1a1a2e' font-size='16'>28</text>

  <!-- Row 5: 29-31 -->
  <text x="52" y="335" text-anchor='middle' fill='#1a1a2e' font-size='16'>29</text>
  <text x="124" y="335" text-anchor='middle' fill='#1a1a2e' font-size='16'>30</text>
  <text x="196" y="335" text-anchor='middle' fill='#1a1a2e' font-size='16'>31</text>

  <!-- Today indicator label -->
  <text x="267" y="395" text-anchor='middle' font-size='13' fill='#1a1a2e' opacity='0.6'>The highlighted date (13) shows today</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">How to use a calendar:</p>
<p style="margin: 8px 0;">Look at the month and year at the top</p>
<p style="margin: 8px 0;">Find the date you are looking for</p>
<p style="margin: 0">See what day of the week it falls on</p>
</div>"""
    },
    {
        "title": "Time Duration: How Long Does It Take?",
        "body": """<p>Sometimes we need to know <strong>how long something takes</strong> -- the time from the start to the end.</p>
<svg viewBox="0 0 515 450" style="width:100%;max-width:515px;display:block;margin:20px auto;">
  <text x="257" y="28" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>Duration: From Start to End</text>

  <!-- Example 1: Brushing teeth -->
  <rect x="15" y="50" width="485" height="82" fill='#e0f2fe' stroke='#0284c7' stroke-width="2" rx="4"/>
  <text x="30" y="75" font-size='15' font-weight='bold' fill='#1a1a2e'>Brushing teeth</text>
  <text x="30" y="97" font-size='13' fill='#1a1a2e' opacity='0.7'>Start: 8:00 AM</text>
  <text x="220" y="97" font-size='13' fill='#1a1a2e' opacity='0.7'>End: 8:02 AM</text>
  <rect x="370" y="80" width="120" height="28" fill='#0284c7' rx="4"/>
  <text x="430" y="99" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>2 minutes</text>
  <text x="30" y="122" font-size='12' font-weight='bold' fill='#1a1a2e'>Duration: 2 minutes</text>

  <!-- Example 2: Playing at recess -->
  <rect x="15" y="148" width="485" height="82" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="4"/>
  <text x="30" y="173" font-size='15' font-weight='bold' fill='#1a1a2e'>Playing at recess</text>
  <text x="30" y="195" font-size='13' fill='#1a1a2e' opacity='0.7'>Start: 10:00 AM</text>
  <text x="220" y="195" font-size='13' fill='#1a1a2e' opacity='0.7'>End: 10:15 AM</text>
  <rect x="370" y="178" width="120" height="28" fill='#d97706' rx="4"/>
  <text x="430" y="197" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>15 minutes</text>
  <text x="30" y="220" font-size='12' font-weight='bold' fill='#1a1a2e'>Duration: 15 minutes</text>

  <!-- Example 3: Watching a movie -->
  <rect x="15" y="246" width="485" height="82" fill='#fce7f3' stroke='#ec4899' stroke-width="2" rx="4"/>
  <text x="30" y="271" font-size='15' font-weight='bold' fill='#1a1a2e'>Watching a movie</text>
  <text x="30" y="293" font-size='13' fill='#1a1a2e' opacity='0.7'>Start: 2:00 PM</text>
  <text x="220" y="293" font-size='13' fill='#1a1a2e' opacity='0.7'>End: 3:30 PM</text>
  <rect x="350" y="276" width="140" height="28" fill='#ec4899' rx="4"/>
  <text x="420" y="295" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>1 hr 30 min</text>
  <text x="30" y="318" font-size='12' font-weight='bold' fill='#1a1a2e'>Duration: 1 hour 30 minutes</text>

  <!-- Example 4: School day -->
  <rect x="15" y="344" width="485" height="82" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="4"/>
  <text x="30" y="369" font-size='15' font-weight='bold' fill='#1a1a2e'>School day</text>
  <text x="30" y="391" font-size='13' fill='#1a1a2e' opacity='0.7'>Start: 8:30 AM</text>
  <text x="220" y="391" font-size='13' fill='#1a1a2e' opacity='0.7'>End: 3:00 PM</text>
  <rect x="350" y="374" width="140" height="28" fill='#16a34a' rx="4"/>
  <text x="420" y="393" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>6 hr 30 min</text>
  <text x="30" y="416" font-size='12' font-weight='bold' fill='#1a1a2e'>Duration: 6 hours 30 minutes</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">How to find duration:</p>
<p style="margin: 8px 0;">1. Note the start time</p>
<p style="margin: 8px 0;">2. Note the end time</p>
<p style="margin: 0">3. Count how much time passed</p>
</div>"""
    }
]
