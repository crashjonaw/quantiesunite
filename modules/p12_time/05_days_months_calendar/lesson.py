"""Days, Weeks, Months, and Calendars — Primary 1-2 lesson."""

TITLE = "Days, Months, and Calendars"

SECTIONS = [
    {
        "title": "The Days of the Week 📅",
        "body": """<p>A <strong>week</strong> has 7 days. Learning the days of the week helps us plan what we do each day!</p>
<svg viewBox="0 0 400 340" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>The 7 Days of the Week</text>

  <!-- Day boxes - one per day in a vertical list -->
  <rect x="30" y="42" width="155" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="6"/>
  <text x="107" y="63" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Monday</text>

  <rect x="215" y="42" width="155" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="6"/>
  <text x="292" y="63" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Tuesday</text>

  <rect x="30" y="82" width="155" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="6"/>
  <text x="107" y="103" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Wednesday</text>

  <rect x="215" y="82" width="155" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="6"/>
  <text x="292" y="103" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Thursday</text>

  <rect x="30" y="122" width="155" height="32" fill='#e0f2fe' stroke='#0284c7' stroke-width="1.5" rx="6"/>
  <text x="107" y="143" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Friday</text>

  <rect x="215" y="122" width="155" height="32" fill='#fef3c7' stroke='#d97706' stroke-width="1.5" rx="6"/>
  <text x="292" y="143" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Saturday</text>

  <rect x="30" y="162" width="155" height="32" fill='#fef3c7' stroke='#d97706' stroke-width="1.5" rx="6"/>
  <text x="107" y="183" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Sunday</text>

  <!-- Arrows showing the cycle -->
  <text x="195" y="63" text-anchor='middle' font-size='14' fill='currentColor'>→</text>
  <text x="195" y="103" text-anchor='middle' font-size='14' fill='currentColor'>→</text>
  <text x="195" y="143" text-anchor='middle' font-size='14' fill='currentColor'>→</text>

  <!-- Divider -->
  <line x1="30" y1="210" x2="370" y2="210" stroke='currentColor' stroke-width="0.5" opacity="0.3"/>

  <!-- School days vs weekend -->
  <text x="200" y="235" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>School Days vs Weekend</text>

  <rect x="30" y="248" width="210" height="36" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="6"/>
  <text x="135" y="271" text-anchor='middle' font-size='11' fill='currentColor'>Mon, Tue, Wed, Thu, Fri 🏫</text>

  <rect x="260" y="248" width="110" height="36" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="6"/>
  <text x="315" y="271" text-anchor='middle' font-size='11' fill='currentColor'>Sat, Sun 🎮</text>

  <text x="135" y="300" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.7'>5 school days</text>
  <text x="315" y="300" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.7'>2 weekend days</text>

  <text x="200" y="330" text-anchor='middle' font-size='12' fill='currentColor'>5 + 2 = 7 days in a week!</text>
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
<svg viewBox="0 0 440 420" style="width:100%;max-width:440px;display:block;margin:20px auto;">
  <text x="220" y="28" text-anchor='middle' font-size='18' font-weight='bold' fill='currentColor'>The 12 Months of the Year</text>

  <!-- Row 1: Winter/Spring — Jan, Feb, Mar, Apr -->
  <rect x="10" y="44" width="100" height="52" fill='#bfdbfe' stroke='#3b82f6' stroke-width="1.5" rx="8"/>
  <text x="60" y="67" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>1</text>
  <text x="60" y="84" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>January</text>

  <rect x="118" y="44" width="100" height="52" fill='#c7d2fe' stroke='#6366f1' stroke-width="1.5" rx="8"/>
  <text x="168" y="67" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>2</text>
  <text x="168" y="84" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>February</text>

  <rect x="226" y="44" width="100" height="52" fill='#bbf7d0' stroke='#22c55e' stroke-width="1.5" rx="8"/>
  <text x="276" y="67" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>3</text>
  <text x="276" y="84" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>March</text>

  <rect x="334" y="44" width="100" height="52" fill='#d9f99d' stroke='#84cc16' stroke-width="1.5" rx="8"/>
  <text x="384" y="67" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>4</text>
  <text x="384" y="84" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>April</text>

  <!-- Row 2: Spring/Summer — May, Jun, Jul, Aug -->
  <rect x="10" y="106" width="100" height="52" fill='#a7f3d0' stroke='#10b981' stroke-width="1.5" rx="8"/>
  <text x="60" y="129" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>5</text>
  <text x="60" y="146" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>May</text>

  <rect x="118" y="106" width="100" height="52" fill='#fef08a' stroke='#eab308' stroke-width="1.5" rx="8"/>
  <text x="168" y="129" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>6</text>
  <text x="168" y="146" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>June</text>

  <rect x="226" y="106" width="100" height="52" fill='#fed7aa' stroke='#f97316' stroke-width="1.5" rx="8"/>
  <text x="276" y="129" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>7</text>
  <text x="276" y="146" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>July</text>

  <rect x="334" y="106" width="100" height="52" fill='#fecaca' stroke='#ef4444' stroke-width="1.5" rx="8"/>
  <text x="384" y="129" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>8</text>
  <text x="384" y="146" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>August</text>

  <!-- Row 3: Autumn/Winter — Sep, Oct, Nov, Dec -->
  <rect x="10" y="168" width="100" height="52" fill='#fde68a' stroke='#d97706' stroke-width="1.5" rx="8"/>
  <text x="60" y="191" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>9</text>
  <text x="60" y="208" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>September</text>

  <rect x="118" y="168" width="100" height="52" fill='#fdba74' stroke='#ea580c' stroke-width="1.5" rx="8"/>
  <text x="168" y="191" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>10</text>
  <text x="168" y="208" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>October</text>

  <rect x="226" y="168" width="100" height="52" fill='#e9d5ff' stroke='#a855f7' stroke-width="1.5" rx="8"/>
  <text x="276" y="191" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>11</text>
  <text x="276" y="208" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>November</text>

  <rect x="334" y="168" width="100" height="52" fill='#dbeafe' stroke='#2563eb' stroke-width="1.5" rx="8"/>
  <text x="384" y="191" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>12</text>
  <text x="384" y="208" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>December</text>

  <!-- Season legend -->
  <line x1="10" y1="240" x2="434" y2="240" stroke='currentColor' stroke-width="0.5" opacity="0.2"/>
  <text x="220" y="265" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>Seasons at a Glance</text>

  <rect x="10" y="280" width="16" height="16" fill='#bfdbfe' rx="3"/>
  <text x="32" y="293" font-size='12' fill='currentColor'>Winter (Dec-Feb)</text>

  <rect x="170" y="280" width="16" height="16" fill='#bbf7d0' rx="3"/>
  <text x="192" y="293" font-size='12' fill='currentColor'>Spring (Mar-May)</text>

  <rect x="10" y="306" width="16" height="16" fill='#fed7aa' rx="3"/>
  <text x="32" y="319" font-size='12' fill='currentColor'>Summer (Jun-Aug)</text>

  <rect x="170" y="306" width="16" height="16" fill='#fde68a' rx="3"/>
  <text x="192" y="319" font-size='12' fill='currentColor'>Autumn (Sep-Nov)</text>

  <!-- Fun facts -->
  <line x1="10" y1="336" x2="434" y2="336" stroke='currentColor' stroke-width="0.5" opacity="0.2"/>
  <text x="220" y="360" text-anchor='middle' font-size='13' font-weight='bold' fill='currentColor'>Fun Facts</text>
  <text x="220" y="382" text-anchor='middle' font-size='12' fill='currentColor'>🎄 December = Christmas time</text>
  <text x="220" y="400" text-anchor='middle' font-size='12' fill='currentColor'>🎂 Your birthday month is special!</text>
</svg>"""
    },
    {
        "title": "Reading and Using a Calendar 📆",
        "body": """<p>A <strong>calendar</strong> shows all the days of a month so you can plan what you're doing!</p>
<svg viewBox="0 0 520 420" style="width:100%;max-width:540px;display:block;margin:20px auto;">
  <text x="260" y="30" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>A Month Calendar</text>

  <!-- Calendar frame -->
  <rect x="20" y="50" width="480" height="350" fill='#f0f4f8' stroke='currentColor' stroke-width="2" rx="8"/>

  <!-- Month/year header -->
  <rect x="20" y="50" width="480" height="42" fill='#e0eaff' stroke='none' rx="8"/>
  <rect x="20" y="80" width="480" height="12" fill='#e0eaff' stroke='none' rx='4'/>
  <text x="260" y="80" text-anchor='middle' font-size='18' font-weight='bold' fill='currentColor'>March 2026</text>

  <!-- Day headers -->
  <g fill='currentColor' opacity='0.7' font-size='14' font-weight='bold'>
    <text x="55" y="115" text-anchor='middle' fill='currentColor'>Sun</text>
    <text x="125" y="115" text-anchor='middle' fill='currentColor'>Mon</text>
    <text x="195" y="115" text-anchor='middle' fill='currentColor'>Tue</text>
    <text x="265" y="115" text-anchor='middle' fill='currentColor'>Wed</text>
    <text x="335" y="115" text-anchor='middle' fill='currentColor'>Thu</text>
    <text x="405" y="115" text-anchor='middle' fill='currentColor'>Fri</text>
    <text x="465" y="115" text-anchor='middle' fill='currentColor'>Sat</text>
  </g>

  <line x1="30" y1="125" x2="490" y2="125" stroke='currentColor' stroke-width="1" opacity="0.3"/>

  <!-- Dates grid -->
  <!-- Row 1: 1-7 -->
  <text x="55" y="155" text-anchor='middle' fill='currentColor' font-size='16'>1</text>
  <text x="125" y="155" text-anchor='middle' fill='currentColor' font-size='16'>2</text>
  <text x="195" y="155" text-anchor='middle' fill='currentColor' font-size='16'>3</text>
  <text x="265" y="155" text-anchor='middle' fill='currentColor' font-size='16'>4</text>
  <text x="335" y="155" text-anchor='middle' fill='currentColor' font-size='16'>5</text>
  <text x="405" y="155" text-anchor='middle' fill='currentColor' font-size='16'>6</text>
  <text x="465" y="155" text-anchor='middle' fill='currentColor' font-size='16'>7</text>

  <!-- Row 2: 8-14 -->
  <text x="55" y="200" text-anchor='middle' fill='currentColor' font-size='16'>8</text>
  <text x="125" y="200" text-anchor='middle' fill='currentColor' font-size='16'>9</text>
  <text x="195" y="200" text-anchor='middle' fill='currentColor' font-size='16'>10</text>
  <text x="265" y="200" text-anchor='middle' fill='currentColor' font-size='16'>11</text>
  <text x="335" y="200" text-anchor='middle' fill='currentColor' font-size='16'>12</text>
  <rect x="381" y="184" width="48" height="28" fill='#3b82f6' rx="4"/>
  <text x="405" y="204" text-anchor='middle' fill='white' font-size='16' font-weight='bold'>13</text>
  <text x="465" y="200" text-anchor='middle' fill='currentColor' font-size='16'>14</text>

  <!-- Row 3: 15-21 -->
  <text x="55" y="245" text-anchor='middle' fill='currentColor' font-size='16'>15</text>
  <text x="125" y="245" text-anchor='middle' fill='currentColor' font-size='16'>16</text>
  <text x="195" y="245" text-anchor='middle' fill='currentColor' font-size='16'>17</text>
  <text x="265" y="245" text-anchor='middle' fill='currentColor' font-size='16'>18</text>
  <text x="335" y="245" text-anchor='middle' fill='currentColor' font-size='16'>19</text>
  <text x="405" y="245" text-anchor='middle' fill='currentColor' font-size='16'>20</text>
  <text x="465" y="245" text-anchor='middle' fill='currentColor' font-size='16'>21</text>

  <!-- Row 4: 22-28 -->
  <text x="55" y="290" text-anchor='middle' fill='currentColor' font-size='16'>22</text>
  <text x="125" y="290" text-anchor='middle' fill='currentColor' font-size='16'>23</text>
  <text x="195" y="290" text-anchor='middle' fill='currentColor' font-size='16'>24</text>
  <text x="265" y="290" text-anchor='middle' fill='currentColor' font-size='16'>25</text>
  <text x="335" y="290" text-anchor='middle' fill='currentColor' font-size='16'>26</text>
  <text x="405" y="290" text-anchor='middle' fill='currentColor' font-size='16'>27</text>
  <text x="465" y="290" text-anchor='middle' fill='currentColor' font-size='16'>28</text>

  <!-- Row 5: 29-31 -->
  <text x="55" y="335" text-anchor='middle' fill='currentColor' font-size='16'>29</text>
  <text x="125" y="335" text-anchor='middle' fill='currentColor' font-size='16'>30</text>
  <text x="195" y="335" text-anchor='middle' fill='currentColor' font-size='16'>31</text>

  <!-- Today indicator label -->
  <text x="260" y="385" text-anchor='middle' font-size='13' fill='currentColor' opacity='0.6'>The highlighted date (13) shows today</text>
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
<svg viewBox="0 0 500 440" style="width:100%;max-width:520px;display:block;margin:20px auto;">
  <text x="250" y="32" text-anchor='middle' font-size='20' font-weight='bold' fill='currentColor'>Duration: From Start to End</text>

  <!-- Example 1: Brushing teeth -->
  <rect x="20" y="52" width="460" height="80" fill='#e0f2fe' stroke='#0284c7' stroke-width="2" rx="8"/>
  <text x="35" y="78" font-size='15' font-weight='bold' fill='currentColor'>Brushing teeth</text>
  <text x="35" y="100" font-size='13' fill='currentColor' opacity='0.7'>Start: 8:00 AM</text>
  <text x="220" y="100" font-size='13' fill='currentColor' opacity='0.7'>End: 8:02 AM</text>
  <rect x="350" y="82" width="120" height="28" fill='#0284c7' rx="14"/>
  <text x="410" y="101" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>2 minutes</text>
  <text x="35" y="122" font-size='12' font-weight='bold' fill='currentColor'>Duration: 2 minutes</text>

  <!-- Example 2: Playing at recess -->
  <rect x="20" y="148" width="460" height="80" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="8"/>
  <text x="35" y="174" font-size='15' font-weight='bold' fill='currentColor'>Playing at recess</text>
  <text x="35" y="196" font-size='13' fill='currentColor' opacity='0.7'>Start: 10:00 AM</text>
  <text x="220" y="196" font-size='13' fill='currentColor' opacity='0.7'>End: 10:15 AM</text>
  <rect x="350" y="178" width="120" height="28" fill='#d97706' rx="14"/>
  <text x="410" y="197" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>15 minutes</text>
  <text x="35" y="218" font-size='12' font-weight='bold' fill='currentColor'>Duration: 15 minutes</text>

  <!-- Example 3: Watching a movie -->
  <rect x="20" y="244" width="460" height="80" fill='#fce7f3' stroke='#ec4899' stroke-width="2" rx="8"/>
  <text x="35" y="270" font-size='15' font-weight='bold' fill='currentColor'>Watching a movie</text>
  <text x="35" y="292" font-size='13' fill='currentColor' opacity='0.7'>Start: 2:00 PM</text>
  <text x="220" y="292" font-size='13' fill='currentColor' opacity='0.7'>End: 3:30 PM</text>
  <rect x="330" y="274" width="140" height="28" fill='#ec4899' rx="14"/>
  <text x="400" y="293" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>1 hr 30 min</text>
  <text x="35" y="314" font-size='12' font-weight='bold' fill='currentColor'>Duration: 1 hour 30 minutes</text>

  <!-- Example 4: School day -->
  <rect x="20" y="340" width="460" height="80" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="8"/>
  <text x="35" y="366" font-size='15' font-weight='bold' fill='currentColor'>School day</text>
  <text x="35" y="388" font-size='13' fill='currentColor' opacity='0.7'>Start: 8:30 AM</text>
  <text x="220" y="388" font-size='13' fill='currentColor' opacity='0.7'>End: 3:00 PM</text>
  <rect x="330" y="370" width="140" height="28" fill='#16a34a' rx="14"/>
  <text x="400" y="389" text-anchor='middle' font-size='13' font-weight='bold' fill='white'>6 hr 30 min</text>
  <text x="35" y="410" font-size='12' font-weight='bold' fill='currentColor'>Duration: 6 hours 30 minutes</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">How to find duration:</p>
<p style="margin: 8px 0;">1. Note the start time</p>
<p style="margin: 8px 0;">2. Note the end time</p>
<p style="margin: 0">3. Count how much time passed</p>
</div>"""
    }
]
