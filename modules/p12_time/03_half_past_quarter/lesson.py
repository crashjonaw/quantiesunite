"""Half Past, Quarter Past, Quarter To — Primary 1-2 lesson."""

TITLE = "Quarter Past, Half Past, Quarter To"

SECTIONS = [
    {
        "title": "Special Times: Quarter & Half ⏰",
        "body": """<p>Some times on the clock have special names because they're so common!</p>
<p>These are times that are 15, 30, and 45 minutes past the hour.</p>
<svg viewBox="0 0 400 280" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Three Special Times</text>

  <!-- :15 = Quarter past -->
  <rect x="20" y="50" width="110" height="110" fill='#e0f2fe' stroke='#0284c7' stroke-width="2" rx="6"/>
  <circle cx="75" cy="85" r="30" fill='#1f2937' stroke='#e5e7eb' stroke-width="1"/>
  <text x="75" y="72" text-anchor='middle' fill='currentColor' font-size='10'>12</text>
  <text x="95" y="90" text-anchor='middle' fill='currentColor' font-size='10'>3</text>
  <text x="75" y="105" text-anchor='middle' fill='currentColor' font-size='10'>6</text>
  <text x="55" y="90" text-anchor='middle' fill='currentColor' font-size='10'>9</text>
  <line x1="75" y1="85" x2="78" y2="65" stroke='#4f8ef7' stroke-width="2" stroke-linecap="round"/>
  <line x1="75" y1="85" x2="95" y2="90" stroke='#22c55e' stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="75" cy="85" r="2" fill='#e5e7eb'/>
  <text x="75" y="135" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>3:15</text>
  <text x="75" y="150" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>Quarter past</text>

  <!-- :30 = Half past -->
  <rect x="145" y="50" width="110" height="110" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="6"/>
  <circle cx="200" cy="85" r="30" fill='#1f2937' stroke='#e5e7eb' stroke-width="1"/>
  <text x="200" y="72" text-anchor='middle' fill='currentColor' font-size='10'>12</text>
  <text x="220" y="90" text-anchor='middle' fill='currentColor' font-size='10'>3</text>
  <text x="200" y="105" text-anchor='middle' fill='currentColor' font-size='10'>6</text>
  <text x="180" y="90" text-anchor='middle' fill='currentColor' font-size='10'>9</text>
  <line x1="200" y1="85" x2="205" y2="65" stroke='#4f8ef7' stroke-width="2" stroke-linecap="round"/>
  <line x1="200" y1="85" x2="200" y2="115" stroke='#22c55e' stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="200" cy="85" r="2" fill='#e5e7eb'/>
  <text x="200" y="135" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>3:30</text>
  <text x="200" y="150" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>Half past</text>

  <!-- :45 = Quarter to -->
  <rect x="270" y="50" width="110" height="110" fill='#f5d3e4' stroke='#ec4899' stroke-width="2" rx="6"/>
  <circle cx="325" cy="85" r="30" fill='#1f2937' stroke='#e5e7eb' stroke-width="1"/>
  <text x="325" y="72" text-anchor='middle' fill='currentColor' font-size='10'>12</text>
  <text x="345" y="90" text-anchor='middle' fill='currentColor' font-size='10'>3</text>
  <text x="325" y="105" text-anchor='middle' fill='currentColor' font-size='10'>6</text>
  <text x="305" y="90" text-anchor='middle' fill='currentColor' font-size='10'>9</text>
  <line x1="325" y1="85" x2="320" y2="65" stroke='#4f8ef7' stroke-width="2" stroke-linecap="round"/>
  <line x1="325" y1="85" x2="305" y2="90" stroke='#22c55e' stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="325" cy="85" r="2" fill='#e5e7eb'/>
  <text x="325" y="135" text-anchor='middle' font-size='12' font-weight='bold' fill='#161b22'>3:45</text>
  <text x="325" y="150" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>Quarter to 4</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px;">
<p style="margin: 0; font-weight: bold;">These times are so common they have special names!</p>
<p style="margin: 8px 0;">• :15 = Quarter past (15 minutes)</p>
<p style="margin: 8px 0;">• :30 = Half past (30 minutes, halfway!)</p>
<p style="margin: 0">• :45 = Quarter to the next hour (45 minutes)</p>
</div>"""
    },
    {
        "title": "Understanding Quarters: Breaking the Hour into 4 Pieces",
        "body": """<p>Think of an hour like a pizza cut into 4 equal pieces. Each piece is a "quarter"!</p>
<svg viewBox="0 0 460 300" style="width:100%;max-width:380px;display:block;margin:20px auto;">
  <text x="190" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Breaking an Hour into Quarters</text>

  <!-- Pizza visual -->
  <circle cx="150" cy="120" r="70" fill='#fff7ed' stroke='#ea580c' stroke-width="2"/>
  <!-- Lines -->
  <line x1="150" y1="50" x2="150" y2="190" stroke='#ea580c' stroke-width="1"/>
  <line x1="80" y1="120" x2="220" y2="120" stroke='#ea580c' stroke-width="1"/>
  <!-- Labels on slices -->
  <text x="150" y="80" text-anchor='middle' font-size='11' font-weight='bold' fill='#161b22'>0 min</text>
  <text x="95" y="130" text-anchor='middle' font-size='11' font-weight='bold' fill='#161b22'>15 min</text>
  <text x="150" y="155" text-anchor='middle' font-size='11' font-weight='bold' fill='#161b22'>30 min</text>
  <text x="205" y="130" text-anchor='middle' font-size='11' font-weight='bold' fill='#161b22'>45 min</text>

  <!-- Minute hand positions -->
  <text x="280" y="70" font-size='12' font-weight='bold' fill='#161b22'>Clock hand positions:</text>

  <!-- Top (0 min/12) -->
  <circle cx="280" cy="90" r="3" fill='#22c55e'/>
  <text x="300" y="95" font-size='11' fill='#161b22'>Pointing at 12 = 0 min (start)</text>

  <!-- Right (15 min/3) -->
  <circle cx="280" cy="120" r="3" fill='#22c55e'/>
  <text x="300" y="125" font-size='11' fill='#161b22'>Pointing at 3 = 15 min</text>

  <!-- Bottom (30 min/6) -->
  <circle cx="280" cy="150" r="3" fill='#22c55e'/>
  <text x="300" y="155" font-size='11' fill='#161b22'>Pointing at 6 = 30 min</text>

  <!-- Left (45 min/9) -->
  <circle cx="280" cy="180" r="3" fill='#22c55e'/>
  <text x="300" y="185" font-size='11' fill='#161b22'>Pointing at 9 = 45 min</text>

  <!-- Formula box -->
  <rect x="20" y="220" width="340" height="70" fill='#f0f8ff' stroke='#4f8ef7' stroke-width="2" rx="6"/>
  <text x="30" y="240" font-size='12' font-weight='bold' fill='#161b22'>Key pattern:</text>
  <text x="30" y="260" font-size='11' fill='#161b22'>Every number on the clock = 5 minutes</text>
  <text x="30" y="275" font-size='11' fill='#161b22;'>So 3 × 5 = 15,  6 × 5 = 30,  9 × 5 = 45</text>
</svg>"""
    },
    {
        "title": "Reading Half Past & Quarter Times",
        "body": """<p>Now let's practice reading these special times!</p>
<svg viewBox="0 0 400 400" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Practice: What Time Is It?</text>

  <!-- Example 1: 4:30 -->
  <circle cx="100" cy="100" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="100" y="65" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="140" y="105" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="100" y="140" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="60" y="105" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <!-- Hour hand between 4 and 5 -->
  <line x1="100" y1="100" x2="120" y2="85" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 6 (30 min) -->
  <line x1="100" y1="100" x2="100" y2="145" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="100" cy="100" r="2" fill='#e5e7eb'/>
  <text x="100" y="175" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>4:30</text>
  <text x="100" y="190" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Half past 4)</text>

  <!-- Example 2: 7:15 -->
  <circle cx="280" cy="100" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="280" y="65" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="320" y="105" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="280" y="140" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="240" y="105" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <!-- Hour hand just past 7 -->
  <line x1="280" y1="100" x2="265" y2="105" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 3 (15 min) -->
  <line x1="280" y1="100" x2="315" y2="105" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="280" cy="100" r="2" fill='#e5e7eb'/>
  <text x="280" y="175" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>7:15</text>
  <text x="280" y="190" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Quarter past 7)</text>

  <!-- Example 3: 10:45 -->
  <circle cx="100" cy="280" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="100" y="245" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="140" y="285" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="100" y="320" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="60" y="285" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <!-- Hour hand almost at 11 -->
  <line x1="100" y1="280" x2="90" y2="255" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 9 (45 min) -->
  <line x1="100" y1="280" x2="60" y2="285" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="100" cy="280" r="2" fill='#e5e7eb'/>
  <text x="100" y="355" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>10:45</text>
  <text x="100" y="370" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Quarter to 11)</text>

  <!-- Example 4: 2:15 -->
  <circle cx="280" cy="280" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="280" y="245" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="320" y="285" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="280" y="320" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="240" y="285" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <!-- Hour hand just past 2 -->
  <line x1="280" y1="280" x2="285" y2="255" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 3 (15 min) -->
  <line x1="280" y1="280" x2="315" y2="285" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="280" cy="280" r="2" fill='#e5e7eb'/>
  <text x="280" y="355" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>2:15</text>
  <text x="280" y="370" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>(Quarter past 2)</text>
</svg>"""
    },
    {
        "title": "Real-World Uses: When Do We Use These Times? ⏰",
        "body": """<p>These special times show up in your daily life all the time!</p>
<svg viewBox="0 0 400 320" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Common Times in Real Life</text>

  <!-- School starts at 8:30 -->
  <rect x="20" y="50" width="360" height="55" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <text x="40" y="75" font-size='12' font-weight='bold' fill='#161b22'>8:30 AM (Half past 8)</text>
  <text x="40" y="92" font-size='11' fill='currentColor' opacity='0.6'>School often starts at this time 🏫</text>

  <!-- Lunch at 12:15 -->
  <rect x="20" y="115" width="360" height="55" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <text x="40" y="140" font-size='12' font-weight='bold' fill='#161b22'>12:15 PM (Quarter past 12)</text>
  <text x="40" y="157" font-size='11' fill='currentColor' opacity='0.6'>Lunch time at many schools 🍽️</text>

  <!-- Play time at 2:30 -->
  <rect x="20" y="180" width="360" height="55" fill='#f5d3e4' stroke='#ec4899' stroke-width="1" rx="4"/>
  <text x="40" y="205" font-size='12' font-weight='bold' fill='#161b22'>2:30 PM (Half past 2)</text>
  <text x="40" y="222" font-size='11' fill='currentColor' opacity='0.6'>Afternoon play or activities 🎮</text>

  <!-- Bedtime at 8:45 -->
  <rect x="20" y="245" width="360" height="55" fill='#e0e7ff' stroke='#6366f1' stroke-width="1" rx="4"/>
  <text x="40" y="270" font-size='12' font-weight='bold' fill='#161b22'>8:45 PM (Quarter to 9)</text>
  <text x="40" y="287" font-size='11' fill='currentColor' opacity='0.6'>Getting ready for bed 😴</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px;">
<p style="margin: 0; font-weight: bold;">Remember the pattern:</p>
<p style="margin: 8px 0;">Minute hand → 3 = :15 (quarter past)</p>
<p style="margin: 8px 0;">Minute hand → 6 = :30 (half past)</p>
<p style="margin: 0">Minute hand → 9 = :45 (quarter to next hour)</p>
</div>"""
    }
]
