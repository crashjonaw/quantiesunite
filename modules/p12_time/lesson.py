"""Telling Time — Lesson sections."""

SECTIONS = [
    {
        "title": "Understanding Time: What are Hours & Minutes? ⏰",
        "body": """<p><strong>Time</strong> measures how long something takes or when something happens. We measure time in hours and minutes.</p>
<p>Think of time as a continuous cycle: the day goes around and around, like a clock!</p>
<svg viewBox="0 0 390 255" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="30" font-size="14" font-weight="bold" fill='currentColor'>Basic time units:</text>

  <rect x="15" y="50" width="170" height="85" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>
  <text x="25" y="75" font-size="12" font-weight="bold" fill='#1a1a2e'>1 HOUR (h)</text>
  <text x="25" y="95" font-size="11" fill='#1a1a2e'>= 60 minutes</text>
  <text x="25" y="113" font-size="11" fill='#1a1a2e'>It takes about 1 hour</text>
  <text x="25" y="128" font-size="11" fill='#1a1a2e'>to watch a movie</text>

  <rect x="205" y="50" width="170" height="85" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="4"/>
  <text x="215" y="75" font-size="12" font-weight="bold" fill='#1a1a2e'>1 MINUTE (min)</text>
  <text x="215" y="95" font-size="11" fill='#1a1a2e'>= 60 seconds</text>
  <text x="215" y="113" font-size="11" fill='#1a1a2e'>It takes about 1 minute</text>
  <text x="215" y="128" font-size="11" fill='#1a1a2e'>to tie your shoes</text>

  <text x="15" y="165" font-size="13" font-weight="bold" fill='currentColor'>The bigger picture:</text>
  <text x="25" y="190" font-size="12" fill='currentColor'>1 day = 24 hours</text>
  <text x="25" y="210" font-size="12" fill='currentColor'>1 week = 7 days</text>
  <text x="25" y="230" font-size="12" fill='currentColor'>1 year = 12 months (about 365 days)</text>
</svg>
<div class='example-box'>
<strong>Remembering the conversions:</strong><br>
<br>
60 seconds = 1 minute<br>
60 minutes = 1 hour<br>
24 hours = 1 day
</div>
<p><strong>Why learn to tell time?</strong> Time helps us plan our day, meet with others, and understand schedules!</p>"""
    },
    {
        "title": "The Clock: Hands & Numbers 🕐",
        "body": """<p>A clock shows time using <strong>hands</strong> (pointer) and <strong>numbers</strong>. Understanding both is key to reading time!</p>
<p>An analog clock has 12 numbers and two (or three) moving hands.</p>
<svg viewBox="0 0 360 290" style="width:100%;max-width:360px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill='currentColor'>Reading an analog clock:</text>

  <circle cx="130" cy="140" r="100" fill="#fff" stroke="#8B0000" stroke-width="3"/>

  <!-- Clock numbers -->
  <text x="130" y="58" text-anchor="middle" font-size="16" font-weight="bold" fill='#000'>12</text>
  <text x="212" y="148" text-anchor="middle" font-size="16" font-weight="bold" fill='#000'>3</text>
  <text x="130" y="232" text-anchor="middle" font-size="16" font-weight="bold" fill='#000'>6</text>
  <text x="48" y="148" text-anchor="middle" font-size="16" font-weight="bold" fill='#000'>9</text>

  <text x="162" y="72" text-anchor="middle" font-size="13" fill='#000'>1</text>
  <text x="188" y="98" text-anchor="middle" font-size="13" fill='#000'>2</text>
  <text x="188" y="198" text-anchor="middle" font-size="13" fill='#000'>4</text>
  <text x="162" y="224" text-anchor="middle" font-size="13" fill='#000'>5</text>
  <text x="98" y="224" text-anchor="middle" font-size="13" fill='#000'>7</text>
  <text x="72" y="198" text-anchor="middle" font-size="13" fill='#000'>8</text>
  <text x="72" y="98" text-anchor="middle" font-size="13" fill='#000'>10</text>
  <text x="98" y="72" text-anchor="middle" font-size="13" fill='#000'>11</text>

  <!-- Hands showing 3:00 -->
  <line x1="130" y1="140" x2="130" y2="60" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <line x1="130" y1="140" x2="200" y2="140" stroke="#1a1a2e" stroke-width="4" stroke-linecap="round"/>

  <!-- Center dot -->
  <circle cx="130" cy="140" r="5" fill="#1a1a2e"/>

  <text x="245" y="170" font-size="12" font-weight="bold" fill='currentColor'>Short hand</text>
  <text x="245" y="185" font-size="11" fill='currentColor'>(hour hand)</text>

  <text x="245" y="210" font-size="12" font-weight="bold" fill='currentColor'>Long hand</text>
  <text x="245" y="225" font-size="11" fill='currentColor'>(minute hand)</text>

  <text x="15" y="275" font-size="12" fill='currentColor'>This clock shows: 3:00 (3 o'clock)</text>
</svg>
<div class='example-box'>
<strong>The two important hands:</strong><br>
<br>
<strong>Hour hand (short):</strong> Points to the hour (1-12)<br>
<strong>Minute hand (long):</strong> Points to the minutes<br>
<br>
The minute hand is ALWAYS longer!
</div>
<p><strong>Remember:</strong> The hour hand points to the hour number. The minute hand is longer and points to the minutes!</p>"""
    },
    {
        "title": "Reading the Hour: Telling Whole Hours ⏰",
        "body": """<p>Let's start by reading <strong>whole hours</strong> -- times like 1:00, 2:00, 3:00, etc.</p>
<p>This is the easiest because the minute hand points straight up at 12!</p>
<svg viewBox="0 0 390 310" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill='currentColor'>Examples of whole hours:</text>

  <!-- Clock 1: 2:00 -->
  <circle cx="75" cy="105" r="55" fill="#fff" stroke="#8B0000" stroke-width="2"/>
  <text x="75" y="65" text-anchor="middle" font-size="12" fill='#000'>12</text>
  <text x="118" y="112" text-anchor="middle" font-size="12" fill='#000'>3</text>
  <text x="75" y="155" text-anchor="middle" font-size="12" fill='#000'>6</text>
  <text x="32" y="112" text-anchor="middle" font-size="12" fill='#000'>9</text>
  <!-- Minute hand to 12 -->
  <line x1="75" y1="105" x2="75" y2="60" stroke="#1a1a2e" stroke-width="2" stroke-linecap="round"/>
  <!-- Hour hand to 2 -->
  <line x1="75" y1="105" x2="95" y2="80" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <circle cx="75" cy="105" r="3" fill="#1a1a2e"/>
  <text x="75" y="180" text-anchor="middle" font-size="12" font-weight="bold" fill='currentColor'>2:00</text>

  <!-- Clock 2: 5:00 -->
  <circle cx="195" cy="105" r="55" fill="#fff" stroke="#8B0000" stroke-width="2"/>
  <text x="195" y="65" text-anchor="middle" font-size="12" fill='#000'>12</text>
  <text x="238" y="112" text-anchor="middle" font-size="12" fill='#000'>3</text>
  <text x="195" y="155" text-anchor="middle" font-size="12" fill='#000'>6</text>
  <text x="152" y="112" text-anchor="middle" font-size="12" fill='#000'>9</text>
  <!-- Minute hand to 12 -->
  <line x1="195" y1="105" x2="195" y2="60" stroke="#1a1a2e" stroke-width="2" stroke-linecap="round"/>
  <!-- Hour hand to 5 -->
  <line x1="195" y1="105" x2="215" y2="135" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <circle cx="195" cy="105" r="3" fill="#1a1a2e"/>
  <text x="195" y="180" text-anchor="middle" font-size="12" font-weight="bold" fill='currentColor'>5:00</text>

  <!-- Clock 3: 9:00 -->
  <circle cx="315" cy="105" r="55" fill="#fff" stroke="#8B0000" stroke-width="2"/>
  <text x="315" y="65" text-anchor="middle" font-size="12" fill='#000'>12</text>
  <text x="358" y="112" text-anchor="middle" font-size="12" fill='#000'>3</text>
  <text x="315" y="155" text-anchor="middle" font-size="12" fill='#000'>6</text>
  <text x="272" y="112" text-anchor="middle" font-size="12" fill='#000'>9</text>
  <!-- Minute hand to 12 -->
  <line x1="315" y1="105" x2="315" y2="60" stroke="#1a1a2e" stroke-width="2" stroke-linecap="round"/>
  <!-- Hour hand to 9 -->
  <line x1="315" y1="105" x2="270" y2="105" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <circle cx="315" cy="105" r="3" fill="#1a1a2e"/>
  <text x="315" y="180" text-anchor="middle" font-size="12" font-weight="bold" fill='currentColor'>9:00</text>

  <text x="15" y="215" font-size="13" font-weight="bold" fill='currentColor'>How to read whole hours:</text>
  <text x="25" y="240" font-size="12" fill='currentColor'>1. Find where the short hand (hour hand) points</text>
  <text x="25" y="260" font-size="12" fill='currentColor'>2. That number is the hour</text>
  <text x="25" y="280" font-size="12" fill='currentColor'>3. The long hand points to 12 (0 minutes)</text>
  <text x="25" y="300" font-size="12" fill='currentColor'>4. Write it as: [hour]:00</text>
</svg>
<div class='example-box'>
<strong>Quick rule for whole hours:</strong><br>
<br>
The minute hand ALWAYS points to 12<br>
Look at where the hour hand points = the hour<br>
Answer = [hour number]:00
</div>
<p><strong>Practice:</strong> Look at a clock in your home. When the long hand points straight up at 12, that's a whole hour!</p>"""
    },
    {
        "title": "Reading Minutes: Half Hours & Quarter Hours 🕐",
        "body": """<p>Now let's learn about <strong>half hours</strong> (like 3:30) and <strong>quarter hours</strong> (like 3:15 and 3:45).</p>
<p>These are important times we use often!</p>
<svg viewBox="0 0 390 330" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill='currentColor'>Special times on the clock:</text>

  <!-- Clock showing 3:15 -->
  <circle cx="75" cy="110" r="50" fill="#fff" stroke="#8B0000" stroke-width="2"/>
  <text x="75" y="72" text-anchor="middle" font-size="11" fill='#000'>12</text>
  <text x="115" y="115" text-anchor="middle" font-size="11" fill='#000'>3</text>
  <text x="75" y="155" text-anchor="middle" font-size="11" fill='#000'>6</text>
  <text x="35" y="115" text-anchor="middle" font-size="11" fill='#000'>9</text>
  <!-- Hour hand just past 3 -->
  <line x1="75" y1="110" x2="80" y2="72" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 3 (15 min) -->
  <line x1="75" y1="110" x2="115" y2="115" stroke="#1a1a2e" stroke-width="2" stroke-linecap="round"/>
  <circle cx="75" cy="110" r="2" fill="#1a1a2e"/>
  <text x="75" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill='currentColor'>3:15</text>
  <text x="75" y="195" text-anchor="middle" font-size="10" fill='currentColor'>Quarter past</text>

  <!-- Clock showing 3:30 -->
  <circle cx="195" cy="110" r="50" fill="#fff" stroke="#8B0000" stroke-width="2"/>
  <text x="195" y="72" text-anchor="middle" font-size="11" fill='#000'>12</text>
  <text x="235" y="115" text-anchor="middle" font-size="11" fill='#000'>3</text>
  <text x="195" y="155" text-anchor="middle" font-size="11" fill='#000'>6</text>
  <text x="155" y="115" text-anchor="middle" font-size="11" fill='#000'>9</text>
  <!-- Hour hand between 3 and 4 -->
  <line x1="195" y1="110" x2="200" y2="72" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 6 (30 min) -->
  <line x1="195" y1="110" x2="195" y2="155" stroke="#1a1a2e" stroke-width="2" stroke-linecap="round"/>
  <circle cx="195" cy="110" r="2" fill="#1a1a2e"/>
  <text x="195" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill='currentColor'>3:30</text>
  <text x="195" y="195" text-anchor="middle" font-size="10" fill='currentColor'>Half past</text>

  <!-- Clock showing 3:45 -->
  <circle cx="315" cy="110" r="50" fill="#fff" stroke="#8B0000" stroke-width="2"/>
  <text x="315" y="72" text-anchor="middle" font-size="11" fill='#000'>12</text>
  <text x="355" y="115" text-anchor="middle" font-size="11" fill='#000'>3</text>
  <text x="315" y="155" text-anchor="middle" font-size="11" fill='#000'>6</text>
  <text x="275" y="115" text-anchor="middle" font-size="11" fill='#000'>9</text>
  <!-- Hour hand almost at 4 -->
  <line x1="315" y1="110" x2="310" y2="72" stroke="#1a1a2e" stroke-width="3" stroke-linecap="round"/>
  <!-- Minute hand at 9 (45 min) -->
  <line x1="315" y1="110" x2="275" y2="115" stroke="#1a1a2e" stroke-width="2" stroke-linecap="round"/>
  <circle cx="315" cy="110" r="2" fill="#1a1a2e"/>
  <text x="315" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill='currentColor'>3:45</text>
  <text x="315" y="195" text-anchor="middle" font-size="10" fill='currentColor'>Quarter to 4</text>

  <text x="15" y="230" font-size="13" font-weight="bold" fill='currentColor'>Key times to remember:</text>
  <rect x="15" y="245" width="360" height="75" fill="#fef3c7" stroke="#d97706" stroke-width="1" rx="4"/>
  <text x="25" y="268" font-size="12" fill='#1a1a2e'>:15 = Quarter past (15 minutes, long hand at 3)</text>
  <text x="25" y="290" font-size="12" fill='#1a1a2e'>:30 = Half past (30 minutes, long hand at 6)</text>
  <text x="25" y="312" font-size="12" fill='#1a1a2e'>:45 = Quarter to next hour (45 min, long hand at 9)</text>
</svg>
<div class='example-box'>
<strong>Remembering the minute hand positions:</strong><br>
<br>
Pointing at 12 = :00 (0 minutes)<br>
Pointing at 3 = :15 (15 minutes)<br>
Pointing at 6 = :30 (30 minutes)<br>
Pointing at 9 = :45 (45 minutes)
</div>
<p><strong>Quick tip:</strong> Every time the minute hand moves to a new number, that's 5 more minutes! (12=0, 1=5, 2=10, 3=15, etc.)</p>"""
    },
    {
        "title": "AM/PM, Calendars & Time Management",
        "body": """<p><strong>AM</strong> (ante meridiem) means morning, and <strong>PM</strong> (post meridiem) means afternoon/evening.</p>
<p>This helps us distinguish between morning and evening times.</p>
<svg viewBox="0 0 390 290" style="width:100%;max-width:390px;height:auto;display:block;margin:16px auto;">
  <text x="15" y="25" font-size="14" font-weight="bold" fill='currentColor'>Understanding AM and PM:</text>

  <rect x="15" y="45" width="175" height="85" fill="#fff7ed" stroke="#ea580c" stroke-width="2" rx="4"/>
  <text x="25" y="68" font-size="12" font-weight="bold" fill='#1a1a2e'>AM (morning)</text>
  <text x="25" y="88" font-size="11" fill='#1a1a2e'>6:00 AM = 6 o'clock</text>
  <text x="25" y="103" font-size="11" fill='#1a1a2e'>in the morning</text>
  <text x="25" y="120" font-size="11" fill='#1a1a2e'>Sunrise is 6-7 AM</text>

  <rect x="200" y="45" width="175" height="85" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" rx="4"/>
  <text x="210" y="68" font-size="12" font-weight="bold" fill='#1a1a2e'>PM (afternoon/evening)</text>
  <text x="210" y="88" font-size="11" fill='#1a1a2e'>6:00 PM = 6 o'clock</text>
  <text x="210" y="103" font-size="11" fill='#1a1a2e'>in the evening</text>
  <text x="210" y="120" font-size="11" fill='#1a1a2e'>Sunset is 6-7 PM</text>

  <text x="15" y="160" font-size="13" font-weight="bold" fill='currentColor'>Daily schedule example:</text>

  <rect x="15" y="175" width="360" height="105" fill="#dcfce7" stroke="#16a34a" stroke-width="1" rx="4"/>
  <text x="25" y="198" font-size="12" fill='#1a1a2e'>Wake up: 7:00 AM</text>
  <text x="25" y="218" font-size="12" fill='#1a1a2e'>School starts: 8:30 AM</text>
  <text x="25" y="238" font-size="12" fill='#1a1a2e'>Lunch: 12:30 PM</text>
  <text x="25" y="258" font-size="12" fill='#1a1a2e'>Leave school: 3:00 PM</text>
  <text x="25" y="278" font-size="12" fill='#1a1a2e'>Bedtime: 9:00 PM</text>
</svg>
<div class='example-box'>
<strong>Important calendar facts:</strong><br>
<br>
1 week = 7 days (Mon-Sun)<br>
1 month = 28-31 days<br>
1 year = 12 months = 365 days<br>
<br>
The days of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
</div>
<p><strong>Real-world application:</strong> Knowing time helps you be on time for school, appointments, and activities with friends!</p>"""
    }
]
