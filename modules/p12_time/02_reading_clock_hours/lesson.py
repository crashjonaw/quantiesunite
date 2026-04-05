"""Reading Clock Hours — Primary 1-2 lesson."""

TITLE = "Reading the Clock: Hours"

SECTIONS = [
    {
        "title": "Anatomy of an Analog Clock 🕐",
        "body": """<p>An analog clock is a circle with <strong>numbers 1-12</strong> and <strong>hands that point</strong> to show the time.</p>
<svg viewBox="0 0 300 320" style="width:100%;max-width:300px;display:block;margin:20px auto;">
  <text x="150" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Parts of a Clock</text>

  <!-- Main clock -->
  <circle cx="150" cy="150" r="100" fill='#1f2937' stroke='#e5e7eb' stroke-width="3"/>

  <!-- Numbers -->
  <text x="150" y="65" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>12</text>
  <text x="225" y="160" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>3</text>
  <text x="150" y="245" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>6</text>
  <text x="75" y="160" text-anchor='middle' fill='currentColor' font-size='18' font-weight='bold'>9</text>

  <!-- Hour markers (small dots) -->
  <circle cx="150" cy="52" r="3" fill='#e5e7eb'/>
  <circle cx="228" cy="150" r="3" fill='#e5e7eb'/>
  <circle cx="150" cy="248" r="3" fill='#e5e7eb'/>
  <circle cx="72" cy="150" r="3" fill='#e5e7eb'/>

  <!-- Hour hand (short, blue) pointing at 10 -->
  <line x1="150" y1="150" x2="120" y2="85" stroke='#4f8ef7' stroke-width="5" stroke-linecap="round"/>

  <!-- Minute hand (long, green) pointing at 12 -->
  <line x1="150" y1="150" x2="150" y2="55" stroke='#22c55e' stroke-width="3" stroke-linecap="round"/>

  <!-- Center dot -->
  <circle cx="150" cy="150" r="5" fill='#e5e7eb'/>

  <!-- Labels with arrows -->
  <text x="20" y="240" font-size='12' font-weight='bold' fill='#161b22'>⏳ Minute hand</text>
  <text x="20" y="255" font-size='11' fill='currentColor' opacity='0.6'>(long, green)</text>

  <text x="20" y="280" font-size='12' font-weight='bold' fill='#161b22'>⏱️ Hour hand</text>
  <text x="20" y="295" font-size='11' fill='currentColor' opacity='0.6'>(short, blue)</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">The two hands you need to know:</p>
<p style="margin: 8px 0;"><strong>Hour hand (short):</strong> Points to the hour number (1-12)</p>
<p style="margin: 8px 0;"><strong>Minute hand (long):</strong> Points to the minutes</p>
<p style="margin: 0; font-size: 11px">The minute hand is ALWAYS longer!</p>
</div>"""
    },
    {
        "title": "Reading Whole Hours (O'Clock Times)",
        "body": """<p>Let's start with the easiest times to read: <strong>whole hours</strong> like 1:00, 2:00, 3:00, etc.</p>
<p>When it's a whole hour, the <strong>minute hand always points straight up at 12</strong>.</p>
<svg viewBox="0 0 380 295" style="width:100%;max-width:380px;display:block;margin:20px auto;">
  <text x="190" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Three Examples</text>

  <!-- Clock 1: 2:00 -->
  <circle cx="70" cy="130" r="50" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="70" y="92" text-anchor='middle' fill='currentColor' font-size='14'>12</text>
  <text x="108" y="138" text-anchor='middle' fill='currentColor' font-size='14'>3</text>
  <text x="70" y="175" text-anchor='middle' fill='currentColor' font-size='14'>6</text>
  <text x="32" y="138" text-anchor='middle' fill='currentColor' font-size='14'>9</text>
  <!-- Hour hand to 2 -->
  <line x1="70" y1="130" x2="85" y2="105" stroke='#4f8ef7' stroke-width="4" stroke-linecap="round"/>
  <!-- Minute hand to 12 -->
  <line x1="70" y1="130" x2="70" y2="85" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="70" cy="130" r="3" fill='#e5e7eb'/>
  <text x="70" y="210" text-anchor='middle' font-size='14' font-weight='bold' fill='#161b22'>2:00</text>

  <!-- Clock 2: 5:00 -->
  <circle cx="190" cy="130" r="50" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="190" y="92" text-anchor='middle' fill='currentColor' font-size='14'>12</text>
  <text x="228" y="138" text-anchor='middle' fill='currentColor' font-size='14'>3</text>
  <text x="190" y="175" text-anchor='middle' fill='currentColor' font-size='14'>6</text>
  <text x="152" y="138" text-anchor='middle' fill='currentColor' font-size='14'>9</text>
  <!-- Hour hand to 5 -->
  <line x1="190" y1="130" x2="210" y2="160" stroke='#4f8ef7' stroke-width="4" stroke-linecap="round"/>
  <!-- Minute hand to 12 -->
  <line x1="190" y1="130" x2="190" y2="85" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="190" cy="130" r="3" fill='#e5e7eb'/>
  <text x="190" y="210" text-anchor='middle' font-size='14' font-weight='bold' fill='#161b22'>5:00</text>

  <!-- Clock 3: 9:00 -->
  <circle cx="310" cy="130" r="50" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="310" y="92" text-anchor='middle' fill='currentColor' font-size='14'>12</text>
  <text x="348" y="138" text-anchor='middle' fill='currentColor' font-size='14'>3</text>
  <text x="310" y="175" text-anchor='middle' fill='currentColor' font-size='14'>6</text>
  <text x="272" y="138" text-anchor='middle' fill='currentColor' font-size='14'>9</text>
  <!-- Hour hand to 9 -->
  <line x1="310" y1="130" x2="270" y2="130" stroke='#4f8ef7' stroke-width="4" stroke-linecap="round"/>
  <!-- Minute hand to 12 -->
  <line x1="310" y1="130" x2="310" y2="85" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="310" cy="130" r="3" fill='#e5e7eb'/>
  <text x="310" y="210" text-anchor='middle' font-size='14' font-weight='bold' fill='#161b22'>9:00</text>

  <!-- Step-by-step -->
  <text x="20" y="250" font-size='12' font-weight='bold' fill='#161b22'>How to read whole hours:</text>
  <text x="20" y="268" font-size='11' fill='currentColor' opacity='0.6'>1. Check if the minute hand points to 12 ✓</text>
  <text x="20" y="283" font-size='11' fill='currentColor' opacity='0.6'>2. Look at where the hour hand points</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px;">
<p style="margin: 0; font-weight: bold;">Remember: Whole hour = Minute hand at 12</p>
<p style="margin: 8px 0;">The time is [hour]:00</p>
</div>"""
    },
    {
        "title": "Practice: What Hour Is It?",
        "body": """<p>Let's practice reading times from clocks!</p>
<svg viewBox="0 0 380 420" style="width:100%;max-width:380px;display:block;margin:20px auto;">
  <text x="190" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Practice Clocks</text>

  <!-- Practice 1: 3:00 -->
  <circle cx="90" cy="100" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="90" y="65" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="125" y="105" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="90" y="140" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="55" y="105" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <line x1="90" y1="100" x2="105" y2="90" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <line x1="90" y1="100" x2="90" y2="60" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="90" cy="100" r="2" fill='#e5e7eb'/>

  <!-- Practice 2: 7:00 -->
  <circle cx="270" cy="100" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="270" y="65" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="305" y="105" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="270" y="140" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="235" y="105" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <line x1="270" y1="100" x2="245" y2="100" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <line x1="270" y1="100" x2="270" y2="60" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="270" cy="100" r="2" fill='#e5e7eb'/>

  <text x="20" y="170" font-size='13' font-weight='bold' fill='#161b22'>Answer these:</text>
  <text x="20" y="190" font-size='12' fill='#161b22'>← What time is shown?</text>
  <text x="200" y="190" font-size='12' fill='#161b22'>What time is shown? →</text>

  <!-- Practice 3: 1:00 -->
  <circle cx="90" cy="270" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="90" y="235" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="125" y="275" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="90" y="310" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="55" y="275" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <line x1="90" y1="270" x2="95" y2="245" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <line x1="90" y1="270" x2="90" y2="230" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="90" cy="270" r="2" fill='#e5e7eb'/>

  <!-- Practice 4: 11:00 -->
  <circle cx="270" cy="270" r="45" fill='#1f2937' stroke='#e5e7eb' stroke-width="2"/>
  <text x="270" y="235" text-anchor='middle' fill='currentColor' font-size='12'>12</text>
  <text x="305" y="275" text-anchor='middle' fill='currentColor' font-size='12'>3</text>
  <text x="270" y="310" text-anchor='middle' fill='currentColor' font-size='12'>6</text>
  <text x="235" y="275" text-anchor='middle' fill='currentColor' font-size='12'>9</text>
  <line x1="270" y1="270" x2="260" y2="245" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <line x1="270" y1="270" x2="270" y2="230" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="270" cy="270" r="2" fill='#e5e7eb'/>

  <text x="20" y="360" font-size='13' font-weight='bold' fill='#161b22'>Answer these:</text>
  <text x="20" y="380" font-size='12' fill='#161b22'>← What time is shown?</text>
  <text x="200" y="380" font-size='12' fill='#161b22'>What time is shown? →</text>

  <text x="190" y="410" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6' font-style="italic">Hint: Look at the short hand!</text>
</svg>"""
    },
    {
        "title": "Real-World Times: When Do Things Happen? 🕐",
        "body": """<p>Now let's connect clock reading to your real day!</p>
<svg viewBox="0 0 400 360" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>Times in Your Day</text>

  <!-- Wake up at 7:00 -->
  <rect x="20" y="50" width="360" height="60" fill='#fff7ed' stroke='#ea580c' stroke-width="1" rx="4"/>
  <circle cx="50" cy="80" r="20" fill='#161b22'/>
  <text x="50" y="87" text-anchor='middle' font-size='10' fill='white'>7</text>
  <text x="95" y="80" font-size='12' font-weight='bold' fill='#161b22'>Wake up: 7:00 AM</text>
  <text x="95" y="98" font-size='11' fill='currentColor' opacity='0.6'>In the morning 🌅</text>

  <!-- School starts at 8:00 -->
  <rect x="20" y="125" width="360" height="60" fill='#f0fdf4' stroke='#16a34a' stroke-width="1" rx="4"/>
  <circle cx="50" cy="155" r="20" fill='#161b22'/>
  <text x="50" y="162" text-anchor='middle' font-size='10' fill='white'>8</text>
  <text x="95" y="155" font-size='12' font-weight='bold' fill='#161b22'>School starts: 8:00 AM</text>
  <text x="95" y="173" font-size='11' fill='currentColor' opacity='0.6'>Time to learn! 🏫</text>

  <!-- Lunch at 12:00 -->
  <rect x="20" y="200" width="360" height="60" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <circle cx="50" cy="230" r="20" fill='#161b22'/>
  <text x="50" y="237" text-anchor='middle' font-size='10' fill='white'>12</text>
  <text x="95" y="230" font-size='12' font-weight='bold' fill='#161b22'>Lunch: 12:00 PM</text>
  <text x="95" y="248" font-size='11' fill='currentColor' opacity='0.6'>Noon—middle of day 🍽️</text>

  <!-- School ends at 3:00 -->
  <rect x="20" y="275" width="360" height="60" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <circle cx="50" cy="305" r="20" fill='#161b22'/>
  <text x="50" y="312" text-anchor='middle' font-size='10' fill='white'>3</text>
  <text x="95" y="305" font-size='12' font-weight='bold' fill='#161b22'>School ends: 3:00 PM</text>
  <text x="95" y="323" font-size='11' fill='currentColor' opacity='0.6'>Afternoon—time to play! 🎮</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">Key times you might see:</p>
<p style="margin: 8px 0;">• 7:00 or 8:00 AM = Morning time to wake up</p>
<p style="margin: 8px 0;">• 12:00 PM = Lunch time (noon)</p>
<p style="margin: 8px 0;">• 3:00 PM = School ends</p>
<p style="margin: 0">• 9:00 PM = Bedtime</p>
</div>"""
    }
]
