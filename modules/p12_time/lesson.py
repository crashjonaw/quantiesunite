"""Telling Time — Lesson sections."""

SECTIONS = [
    {
        "title": "Understanding Time: What are Hours & Minutes? ⏰",
        "body": """<p><strong>Time</strong> measures how long something takes or when something happens. We measure time in hours and minutes.</p>
<p>Think of time as a continuous cycle: the day goes around and around, like a clock!</p>
<svg width="360" height="240" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Basic time units:</text>

  <rect x="20" y="45" width="150" height="80" fill="lightyellow" stroke="orange" stroke-width="2" rx="5"/>
  <text x="30" y="70" font-size="12" font-weight="bold">1 HOUR (h)</text>
  <text x="30" y="90" font-size="11">= 60 minutes</text>
  <text x="30" y="110" font-size="11">It takes about 1 hour</text>
  <text x="30" y="125" font-size="11">to watch a movie</text>

  <rect x="200" y="45" width="150" height="80" fill="lightgreen" stroke="green" stroke-width="2" rx="5"/>
  <text x="210" y="70" font-size="12" font-weight="bold">1 MINUTE (min)</text>
  <text x="210" y="90" font-size="11">= 60 seconds</text>
  <text x="210" y="110" font-size="11">It takes about 1 minute</text>
  <text x="210" y="125" font-size="11">to tie your shoes</text>

  <text x="10" y="160" font-size="13" font-weight="bold">The bigger picture:</text>
  <text x="20" y="185" font-size="12">📅 1 day = 24 hours</text>
  <text x="20" y="205" font-size="12">📆 1 week = 7 days</text>
  <text x="20" y="225" font-size="12">📕 1 year = 12 months (about 365 days)</text>
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
<svg width="360" height="280" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Reading an analog clock:</text>

  <circle cx="120" cy="120" r="90" fill="white" stroke="black" stroke-width="2"/>

  <!-- Clock numbers -->
  <text x="110" y="45" font-size="16" font-weight="bold">12</text>
  <text x="180" y="130" font-size="16" font-weight="bold">3</text>
  <text x="110" y="210" font-size="16" font-weight="bold">6</text>
  <text x="45" y="130" font-size="16" font-weight="bold">9</text>

  <text x="115" y="75" font-size="12">1</text>
  <text x="145" y="55" font-size="12">2</text>
  <text x="160" y="85" font-size="12">4</text>
  <text x="160" y="155" font-size="12">5</text>
  <text x="145" y="185" font-size="12">7</text>
  <text x="115" y="205" font-size="12">8</text>
  <text x="75" y="185" font-size="12">10</text>
  <text x="75" y="85" font-size="12">11</text>

  <!-- Hour markers -->
  <circle cx="120" cy="35" r="2" fill="black"/>
  <circle cx="185" cy="120" r="2" fill="black"/>
  <circle cx="120" cy="205" r="2" fill="black"/>
  <circle cx="55" cy="120" r="2" fill="black"/>

  <!-- Hands showing 3:00 -->
  <line x1="120" y1="120" x2="120" y2="50" stroke="black" stroke-width="4" stroke-linecap="round"/>
  <line x1="120" y1="120" x2="175" y2="120" stroke="black" stroke-width="3" stroke-linecap="round"/>

  <!-- Center dot -->
  <circle cx="120" cy="120" r="5" fill="black"/>

  <text x="150" y="170" font-size="12" font-weight="bold">Short hand</text>
  <text x="150" y="185" font-size="11">(hour hand)</text>

  <text x="150" y="205" font-size="12" font-weight="bold">Long hand</text>
  <text x="150" y="220" font-size="11">(minute hand)</text>

  <text x="10" y="260" font-size="12">This clock shows: 3:00 (3 o'clock)</text>
</svg>
<div class='example-box'>
<strong>The two important hands:</strong><br>
<br>
⏱️ <strong>Hour hand (short):</strong> Points to the hour (1-12)<br>
⏱️ <strong>Minute hand (long):</strong> Points to the minutes<br>
<br>
The minute hand is ALWAYS longer!
</div>
<p><strong>Remember:</strong> The hour hand points to the hour number. The minute hand is longer and points to the minutes!</p>"""
    },
    {
        "title": "Reading the Hour: Telling Whole Hours ⏰",
        "body": """<p>Let's start by reading <strong>whole hours</strong> — times like 1:00, 2:00, 3:00, etc.</p>
<p>This is the easiest because the minute hand points straight up at 12!</p>
<svg width="360" height="300" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Examples of whole hours:</text>

  <!-- Clock 1: 2:00 -->
  <circle cx="70" cy="100" r="50" fill="white" stroke="black" stroke-width="1"/>
  <text x="55" y="55" font-size="12">12</text>
  <text x="105" y="75" font-size="12">3</text>
  <text x="55" y="150" font-size="12">6</text>
  <text x="25" y="75" font-size="12">9</text>
  <line x1="70" y1="100" x2="70" y2="60" stroke="black" stroke-width="2"/>
  <line x1="70" y1="100" x2="85" y2="100" stroke="black" stroke-width="1.5"/>
  <circle cx="70" cy="100" r="3" fill="black"/>
  <text x="45" y="170" font-size="12" font-weight="bold">2:00</text>

  <!-- Clock 2: 5:00 -->
  <circle cx="190" cy="100" r="50" fill="white" stroke="black" stroke-width="1"/>
  <text x="175" y="55" font-size="12">12</text>
  <text x="225" y="75" font-size="12">3</text>
  <text x="175" y="150" font-size="12">6</text>
  <text x="145" y="75" font-size="12">9</text>
  <line x1="190" y1="100" x2="190" y2="60" stroke="black" stroke-width="2"/>
  <line x1="190" y1="100" x2="190" y2="145" stroke="black" stroke-width="1.5"/>
  <circle cx="190" cy="100" r="3" fill="black"/>
  <text x="165" y="170" font-size="12" font-weight="bold">5:00</text>

  <!-- Clock 3: 9:00 -->
  <circle cx="310" cy="100" r="50" fill="white" stroke="black" stroke-width="1"/>
  <text x="295" y="55" font-size="12">12</text>
  <text x="345" y="75" font-size="12">3</text>
  <text x="295" y="150" font-size="12">6</text>
  <text x="265" y="75" font-size="12">9</text>
  <line x1="310" y1="100" x2="310" y2="60" stroke="black" stroke-width="2"/>
  <line x1="310" y1="100" x2="270" y2="100" stroke="black" stroke-width="1.5"/>
  <circle cx="310" cy="100" r="3" fill="black"/>
  <text x="285" y="170" font-size="12" font-weight="bold">9:00</text>

  <text x="10" y="210" font-size="13" font-weight="bold">How to read whole hours:</text>
  <text x="20" y="235" font-size="12">1. Find where the short hand (hour hand) points</text>
  <text x="20" y="255" font-size="12">2. That number is the hour</text>
  <text x="20" y="275" font-size="12">3. The long hand points to 12 (0 minutes)</text>
  <text x="20" y="295" font-size="12">4. Write it as: [hour]:00</text>
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
<svg width="360" height="320" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Special times on the clock:</text>

  <!-- Clock showing 3:15 -->
  <circle cx="70" cy="110" r="45" fill="white" stroke="black" stroke-width="1"/>
  <text x="55" y="70" font-size="11">12</text>
  <text x="105" y="85" font-size="11">3</text>
  <text x="55" y="160" font-size="11">6</text>
  <text x="25" y="85" font-size="11">9</text>
  <line x1="70" y1="110" x2="75" y2="70" stroke="black" stroke-width="2"/>
  <line x1="70" y1="110" x2="105" y2="85" stroke="black" stroke-width="1.5"/>
  <circle cx="70" cy="110" r="2" fill="black"/>
  <text x="50" y="175" font-size="11" font-weight="bold">3:15</text>
  <text x="35" y="190" font-size="10">Quarter past</text>

  <!-- Clock showing 3:30 -->
  <circle cx="190" cy="110" r="45" fill="white" stroke="black" stroke-width="1"/>
  <text x="175" y="70" font-size="11">12</text>
  <text x="225" y="85" font-size="11">3</text>
  <text x="175" y="160" font-size="11">6</text>
  <text x="145" y="85" font-size="11">9</text>
  <line x1="190" y1="110" x2="190" y2="70" stroke="black" stroke-width="2"/>
  <line x1="190" y1="110" x2="190" y2="145" stroke="black" stroke-width="1.5"/>
  <circle cx="190" cy="110" r="2" fill="black"/>
  <text x="170" y="175" font-size="11" font-weight="bold">3:30</text>
  <text x="160" y="190" font-size="10">Half past</text>

  <!-- Clock showing 3:45 -->
  <circle cx="310" cy="110" r="45" fill="white" stroke="black" stroke-width="1"/>
  <text x="295" y="70" font-size="11">12</text>
  <text x="345" y="85" font-size="11">3</text>
  <text x="295" y="160" font-size="11">6</text>
  <text x="265" y="85" font-size="11">9</text>
  <line x1="310" y1="110" x2="305" y2="70" stroke="black" stroke-width="2"/>
  <line x1="310" y1="110" x2="275" y2="85" stroke="black" stroke-width="1.5"/>
  <circle cx="310" cy="110" r="2" fill="black"/>
  <text x="290" y="175" font-size="11" font-weight="bold">3:45</text>
  <text x="280" y="190" font-size="10">Quarter to 4</text>

  <text x="10" y="230" font-size="13" font-weight="bold">Key times to remember:</text>
  <rect x="10" y="240" width="340" height="75" fill="lightyellow" stroke="orange" stroke-width="1" rx="3"/>
  <text x="20" y="260" font-size="12">⏰ :15 = Quarter past (15 minutes, long hand at 3)</text>
  <text x="20" y="280" font-size="12">⏰ :30 = Half past (30 minutes, long hand at 6)</text>
  <text x="20" y="300" font-size="12">⏰ :45 = Quarter to the next hour (45 minutes, long hand at 9)</text>
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
        "title": "AM/PM, Calendars & Time Management 📅",
        "body": """<p><strong>AM</strong> (ante meridiem) means morning, and <strong>PM</strong> (post meridiem) means afternoon/evening.</p>
<p>This helps us distinguish between morning and evening times.</p>
<svg width="360" height="280" style="border: 1px solid #ccc; margin: 10px;">
  <text x="10" y="25" font-size="14" font-weight="bold">Understanding AM and PM:</text>

  <rect x="10" y="40" width="165" height="80" fill="lightyellow" stroke="orange" stroke-width="2" rx="5"/>
  <text x="20" y="65" font-size="12" font-weight="bold">🌅 AM (morning)</text>
  <text x="20" y="85" font-size="11">6:00 AM = 6 o'clock</text>
  <text x="20" y="100" font-size="11">in the morning</text>
  <text x="20" y="115" font-size="11">Sunrise is 6-7 AM</text>

  <rect x="185" y="40" width="165" height="80" fill="lightblue" stroke="blue" stroke-width="2" rx="5"/>
  <text x="195" y="65" font-size="12" font-weight="bold">🌆 PM (afternoon/evening)</text>
  <text x="195" y="85" font-size="11">6:00 PM = 6 o'clock</text>
  <text x="195" y="100" font-size="11">in the evening</text>
  <text x="195" y="115" font-size="11">Sunset is 6-7 PM</text>

  <text x="10" y="155" font-size="13" font-weight="bold">Daily schedule example:</text>

  <rect x="10" y="170" width="340" height="100" fill="lightgreen" stroke="green" stroke-width="1" rx="3"/>
  <text x="20" y="190" font-size="12">🛏️  Wake up: 7:00 AM</text>
  <text x="20" y="210" font-size="12">🏫 School starts: 8:30 AM</text>
  <text x="20" y="230" font-size="12">🍽️  Lunch: 12:30 PM</text>
  <text x="20" y="250" font-size="12">🚗 Leave school: 3:00 PM</text>
  <text x="20" y="270" font-size="12">😴 Bedtime: 9:00 PM</text>
</svg>
<div class='example-box'>
<strong>Important calendar facts:</strong><br>
<br>
📅 1 week = 7 days (Mon-Sun)<br>
📅 1 month = 28-31 days<br>
📅 1 year = 12 months = 365 days<br>
<br>
The days of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
</div>
<p><strong>Real-world application:</strong> Knowing time helps you be on time for school, appointments, and activities with friends!</p>"""
    }
]
