"""Reading Clock Hours — Primary 1-2 lesson."""

TITLE = "Reading the Clock: Hours"

SECTIONS = [
    {
        "title": "Anatomy of an Analog Clock 🕐",
        "body": """<p>An analog clock is a circle with <strong>numbers 1-12</strong> and <strong>hands that point</strong> to show the time.</p>
<svg viewBox="0 0 315 335" style="width:100%;max-width:315px;display:block;margin:20px auto;">
  <text x="157" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>Parts of a Clock</text>

  <!-- Main clock -->
  <circle cx="157" cy="155" r="100" fill='#fff' stroke='#8B0000' stroke-width="3"/>

  <!-- Numbers 1-12 -->
  <text x="157" y="75" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>12</text>
  <text x="200" y="83" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>1</text>
  <text x="231" y="109" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>2</text>
  <text x="243" y="161" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>3</text>
  <text x="231" y="209" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>4</text>
  <text x="200" y="235" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>5</text>
  <text x="157" y="247" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>6</text>
  <text x="114" y="235" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>7</text>
  <text x="83" y="209" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>8</text>
  <text x="71" y="161" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>9</text>
  <text x="83" y="109" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>10</text>
  <text x="114" y="83" text-anchor='middle' fill='#000' font-size='16' font-weight='bold'>11</text>

  <!-- Hour hand (short, thick) pointing at 10 -->
  <line x1="157" y1="155" x2="127" y2="90" stroke='#1a1a2e' stroke-width="5" stroke-linecap="round"/>

  <!-- Minute hand (long, thin) pointing at 12 -->
  <line x1="157" y1="155" x2="157" y2="62" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>

  <!-- Center dot -->
  <circle cx="157" cy="155" r="5" fill='#1a1a2e'/>

  <!-- Labels -->
  <text x="15" y="290" font-size='12' font-weight='bold' fill='currentColor'>Minute hand (long, thin)</text>
  <text x="15" y="310" font-size='12' font-weight='bold' fill='currentColor'>Hour hand (short, thick)</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px; color: #1a1a2e;">
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
<svg viewBox="0 0 395 305" style="width:100%;max-width:395px;display:block;margin:20px auto;">
  <text x="197" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>Three Examples</text>

  <!-- Clock 1: 2:00 -->
  <circle cx="75" cy="130" r="55" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="75" y="88" text-anchor='middle' fill='#000' font-size='14'>12</text>
  <text x="118" y="138" text-anchor='middle' fill='#000' font-size='14'>3</text>
  <text x="75" y="180" text-anchor='middle' fill='#000' font-size='14'>6</text>
  <text x="32" y="138" text-anchor='middle' fill='#000' font-size='14'>9</text>
  <!-- Hour hand to 2 -->
  <line x1="75" y1="130" x2="90" y2="102" stroke='#1a1a2e' stroke-width="4" stroke-linecap="round"/>
  <!-- Minute hand to 12 -->
  <line x1="75" y1="130" x2="75" y2="82" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="75" cy="130" r="3" fill='#1a1a2e'/>
  <text x="75" y="210" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>2:00</text>

  <!-- Clock 2: 5:00 -->
  <circle cx="197" cy="130" r="55" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="197" y="88" text-anchor='middle' fill='#000' font-size='14'>12</text>
  <text x="240" y="138" text-anchor='middle' fill='#000' font-size='14'>3</text>
  <text x="197" y="180" text-anchor='middle' fill='#000' font-size='14'>6</text>
  <text x="154" y="138" text-anchor='middle' fill='#000' font-size='14'>9</text>
  <!-- Hour hand to 5 -->
  <line x1="197" y1="130" x2="217" y2="162" stroke='#1a1a2e' stroke-width="4" stroke-linecap="round"/>
  <!-- Minute hand to 12 -->
  <line x1="197" y1="130" x2="197" y2="82" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="197" cy="130" r="3" fill='#1a1a2e'/>
  <text x="197" y="210" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>5:00</text>

  <!-- Clock 3: 9:00 -->
  <circle cx="320" cy="130" r="55" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="320" y="88" text-anchor='middle' fill='#000' font-size='14'>12</text>
  <text x="363" y="138" text-anchor='middle' fill='#000' font-size='14'>3</text>
  <text x="320" y="180" text-anchor='middle' fill='#000' font-size='14'>6</text>
  <text x="277" y="138" text-anchor='middle' fill='#000' font-size='14'>9</text>
  <!-- Hour hand to 9 -->
  <line x1="320" y1="130" x2="275" y2="130" stroke='#1a1a2e' stroke-width="4" stroke-linecap="round"/>
  <!-- Minute hand to 12 -->
  <line x1="320" y1="130" x2="320" y2="82" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="320" cy="130" r="3" fill='#1a1a2e'/>
  <text x="320" y="210" text-anchor='middle' font-size='14' font-weight='bold' fill='currentColor'>9:00</text>

  <!-- Step-by-step -->
  <text x="15" y="250" font-size='12' font-weight='bold' fill='currentColor'>How to read whole hours:</text>
  <text x="15" y="270" font-size='11' fill='currentColor' opacity='0.6'>1. Check if the minute hand points to 12</text>
  <text x="15" y="288" font-size='11' fill='currentColor' opacity='0.6'>2. Look at where the hour hand points</text>
</svg>
<div style="background:#dcfce7;border-left:4px solid #16a34a;padding:12px;margin:16px 0;border-radius:4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">Remember: Whole hour = Minute hand at 12</p>
<p style="margin: 8px 0;">The time is [hour]:00</p>
</div>"""
    },
    {
        "title": "Practice: What Hour Is It?",
        "body": """<p>Let's practice reading times from clocks!</p>
<svg viewBox="0 0 395 430" style="width:100%;max-width:395px;display:block;margin:20px auto;">
  <text x="197" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>Practice Clocks</text>

  <!-- Practice 1: 3:00 -->
  <circle cx="95" cy="100" r="50" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="95" y="62" text-anchor='middle' fill='#000' font-size='12'>12</text>
  <text x="135" y="105" text-anchor='middle' fill='#000' font-size='12'>3</text>
  <text x="95" y="145" text-anchor='middle' fill='#000' font-size='12'>6</text>
  <text x="55" y="105" text-anchor='middle' fill='#000' font-size='12'>9</text>
  <line x1="95" y1="100" x2="120" y2="90" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
  <line x1="95" y1="100" x2="95" y2="58" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="95" cy="100" r="2" fill='#1a1a2e'/>

  <!-- Practice 2: 7:00 -->
  <circle cx="280" cy="100" r="50" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="280" y="62" text-anchor='middle' fill='#000' font-size='12'>12</text>
  <text x="320" y="105" text-anchor='middle' fill='#000' font-size='12'>3</text>
  <text x="280" y="145" text-anchor='middle' fill='#000' font-size='12'>6</text>
  <text x="240" y="105" text-anchor='middle' fill='#000' font-size='12'>9</text>
  <line x1="280" y1="100" x2="255" y2="118" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
  <line x1="280" y1="100" x2="280" y2="58" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="280" cy="100" r="2" fill='#1a1a2e'/>

  <text x="15" y="175" font-size='13' font-weight='bold' fill='currentColor'>Answer these:</text>
  <text x="15" y="195" font-size='12' fill='currentColor'>What time does the left clock show?</text>
  <text x="200" y="195" font-size='12' fill='currentColor'>What time does the right clock show?</text>

  <!-- Practice 3: 1:00 -->
  <circle cx="95" cy="270" r="50" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="95" y="232" text-anchor='middle' fill='#000' font-size='12'>12</text>
  <text x="135" y="275" text-anchor='middle' fill='#000' font-size='12'>3</text>
  <text x="95" y="315" text-anchor='middle' fill='#000' font-size='12'>6</text>
  <text x="55" y="275" text-anchor='middle' fill='#000' font-size='12'>9</text>
  <line x1="95" y1="270" x2="100" y2="240" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
  <line x1="95" y1="270" x2="95" y2="228" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="95" cy="270" r="2" fill='#1a1a2e'/>

  <!-- Practice 4: 11:00 -->
  <circle cx="280" cy="270" r="50" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="280" y="232" text-anchor='middle' fill='#000' font-size='12'>12</text>
  <text x="320" y="275" text-anchor='middle' fill='#000' font-size='12'>3</text>
  <text x="280" y="315" text-anchor='middle' fill='#000' font-size='12'>6</text>
  <text x="240" y="275" text-anchor='middle' fill='#000' font-size='12'>9</text>
  <line x1="280" y1="270" x2="268" y2="242" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
  <line x1="280" y1="270" x2="280" y2="228" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="280" cy="270" r="2" fill='#1a1a2e'/>

  <text x="15" y="360" font-size='13' font-weight='bold' fill='currentColor'>Answer these:</text>
  <text x="15" y="380" font-size='12' fill='currentColor'>What time does the left clock show?</text>
  <text x="200" y="380" font-size='12' fill='currentColor'>What time does the right clock show?</text>

  <text x="197" y="415" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6' font-style="italic">Hint: Look at the short hand!</text>
</svg>"""
    },
    {
        "title": "Real-World Times: When Do Things Happen? 🕐",
        "body": """<p>Now let's connect clock reading to your real day!</p>
<svg viewBox="0 0 415 370" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <text x="207" y="28" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>Times in Your Day</text>

  <!-- Wake up at 7:00 -->
  <rect x="15" y="48" width="385" height="65" fill='#fff7ed' stroke='#ea580c' stroke-width="1" rx="4"/>
  <circle cx="50" cy="80" r="22" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="50" y="87" text-anchor='middle' font-size='10' fill='#000' font-weight='bold'>7</text>
  <text x="95" y="78" font-size='12' font-weight='bold' fill='#1a1a2e'>Wake up: 7:00 AM</text>
  <text x="95" y="98" font-size='11' fill='#1a1a2e' opacity='0.6'>In the morning</text>

  <!-- School starts at 8:00 -->
  <rect x="15" y="125" width="385" height="65" fill='#f0fdf4' stroke='#16a34a' stroke-width="1" rx="4"/>
  <circle cx="50" cy="157" r="22" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="50" y="164" text-anchor='middle' font-size='10' fill='#000' font-weight='bold'>8</text>
  <text x="95" y="155" font-size='12' font-weight='bold' fill='#1a1a2e'>School starts: 8:00 AM</text>
  <text x="95" y="175" font-size='11' fill='#1a1a2e' opacity='0.6'>Time to learn!</text>

  <!-- Lunch at 12:00 -->
  <rect x="15" y="202" width="385" height="65" fill='#fef3c7' stroke='#d97706' stroke-width="1" rx="4"/>
  <circle cx="50" cy="234" r="22" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="50" y="241" text-anchor='middle' font-size='10' fill='#000' font-weight='bold'>12</text>
  <text x="95" y="232" font-size='12' font-weight='bold' fill='#1a1a2e'>Lunch: 12:00 PM</text>
  <text x="95" y="252" font-size='11' fill='#1a1a2e' opacity='0.6'>Noon -- middle of day</text>

  <!-- School ends at 3:00 -->
  <rect x="15" y="279" width="385" height="65" fill='#e0f2fe' stroke='#0284c7' stroke-width="1" rx="4"/>
  <circle cx="50" cy="311" r="22" fill='#fff' stroke='#8B0000' stroke-width="2"/>
  <text x="50" y="318" text-anchor='middle' font-size='10' fill='#000' font-weight='bold'>3</text>
  <text x="95" y="309" font-size='12' font-weight='bold' fill='#1a1a2e'>School ends: 3:00 PM</text>
  <text x="95" y="329" font-size='11' fill='#1a1a2e' opacity='0.6'>Afternoon -- time to play!</text>
</svg>
<div style="background: #f0f8ff; padding: 12px; margin: 16px 0; border-radius: 4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">Key times you might see:</p>
<p style="margin: 8px 0;">7:00 or 8:00 AM = Morning time to wake up</p>
<p style="margin: 8px 0;">12:00 PM = Lunch time (noon)</p>
<p style="margin: 8px 0;">3:00 PM = School ends</p>
<p style="margin: 0">9:00 PM = Bedtime</p>
</div>"""
    }
]
