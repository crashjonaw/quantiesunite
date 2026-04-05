"""What is Time? — Primary 1-2 lesson."""

TITLE = "What is Time?"

SECTIONS = [
    {
        "title": "How Do We Know When Things Happen? ⏰",
        "body": """<p>How do you know when to wake up, eat lunch, or go to bed? <strong>Time tells us WHERE we are in the day.</strong></p>
<p>Time is like an invisible clock that keeps going and going. Every second, every minute, every hour moves us forward through our day.</p>
<svg viewBox="0 0 400 250" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <rect x="20" y="20" width="360" height="210" fill='#f0f8ff' stroke='#4f8ef7' stroke-width="2" rx="8"/>
  <text x="200" y="50" text-anchor='middle' font-size='18' font-weight='bold' fill='#161b22'>Timeline of a Day</text>

  <line x1="50" y1="90" x2="350" y2="90" stroke='#4f8ef7' stroke-width="2"/>

  <circle cx="50" cy="90" r="5" fill='#22c55e'/>
  <text x="50" y="120" text-anchor='middle' font-size='12' fill='#161b22'>Wake up</text>
  <text x="50" y="135" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>7 AM</text>

  <circle cx="150" cy="90" r="5" fill='#fbbf24'/>
  <text x="150" y="120" text-anchor='middle' font-size='12' fill='#161b22'>Lunch</text>
  <text x="150" y="135" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>12 PM</text>

  <circle cx="250" cy="90" r="5" fill='#f97316'/>
  <text x="250" y="120" text-anchor='middle' font-size='12' fill='#161b22'>School ends</text>
  <text x="250" y="135" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>3 PM</text>

  <circle cx="350" cy="90" r="5" fill='#8b5cf6'/>
  <text x="350" y="120" text-anchor='middle' font-size='12' fill='#161b22'>Bedtime</text>
  <text x="350" y="135" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>9 PM</text>

  <text x="200" y="190" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>↑ Time moves forward all day long</text>
</svg>
<p><strong>Why learn time?</strong> Time helps us plan our day, meet with friends, and know when to do important things!</p>"""
    },
    {
        "title": "Time Units: Seconds, Minutes, Hours",
        "body": """<p>We measure time using small units that build up into bigger units.</p>
<div style="background: #f0f8ff; padding: 16px; margin: 16px 0; border-radius: 4px">
<p style="margin: 0; font-weight: bold;">Time conversions to remember:</p>
<p style="margin: 8px 0;">60 seconds = 1 minute</p>
<p style="margin: 8px 0;">60 minutes = 1 hour</p>
<p style="margin: 8px 0;">24 hours = 1 day</p>
</div>
<svg viewBox="0 0 400 280" style="width:100%;max-width:400px;height:auto;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>What does each unit measure?</text>

  <!-- Seconds box -->
  <rect x="20" y="50" width="110" height="100" fill='#e0f2fe' stroke='#0284c7' stroke-width="2" rx="6"/>
  <text x="75" y="75" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>⏱️ Seconds</text>
  <text x="75" y="95" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>Very short</text>
  <text x="75" y="110" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>time</text>
  <text x="75" y="130" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>⏱️ Snap your</text>
  <text x="75" y="145" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>fingers</text>

  <!-- Minutes box -->
  <rect x="145" y="50" width="110" height="100" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="6"/>
  <text x="200" y="75" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>⏲️ Minutes</text>
  <text x="200" y="95" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>Medium</text>
  <text x="200" y="110" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>time</text>
  <text x="200" y="130" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>🎵 Sing a</text>
  <text x="200" y="145" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>song</text>

  <!-- Hours box -->
  <rect x="270" y="50" width="110" height="100" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="6"/>
  <text x="325" y="75" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>⏰ Hours</text>
  <text x="325" y="95" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>Long</text>
  <text x="325" y="110" text-anchor='middle' font-size='11' fill='currentColor' opacity='0.6'>time</text>
  <text x="325" y="130" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>🎬 Watch a</text>
  <text x="325" y="145" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>movie</text>

  <!-- Real examples -->
  <text x="20" y="190" font-size='12' fill='#161b22'>Real examples:</text>
  <text x="20" y="210" font-size='11' fill='currentColor' opacity='0.6'>• Brushing teeth = 2 minutes</text>
  <text x="20" y="230" font-size='11' fill='currentColor' opacity='0.6'>• Playing at recess = 15 minutes</text>
  <text x="20" y="250" font-size='11' fill='currentColor' opacity='0.6'>• Math lesson = 1 hour</text>
  <text x="20" y="270" font-size='11' fill='currentColor' opacity='0.6'>• Whole school day = 6 hours</text>
</svg>"""
    },
    {
        "title": "Clocks Are Tools We Invented 🕐",
        "body": """<p>Clocks are special tools that show us what <strong>time it is right now.</strong> People invented clocks to measure and display time.</p>
<p>There are two main types of clocks:</p>
<svg viewBox="0 0 400 200" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <!-- Analog clock -->
  <rect x="20" y="20" width="160" height="160" fill='#f3f4f6' stroke='#6b7280' stroke-width="2" rx="6"/>
  <text x="100" y="45" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>Analog Clock</text>

  <circle cx="100" cy="110" r="50" fill='white' stroke='#374151' stroke-width="2"/>
  <text x="100" y="75" text-anchor='middle' font-size='12' fill='#161b22'>12</text>
  <text x="140" y="115" text-anchor='middle' font-size='12' fill='#161b22'>3</text>
  <text x="100" y="150" text-anchor='middle' font-size='12' fill='#161b22'>6</text>
  <text x="60" y="115" text-anchor='middle' font-size='12' fill='#161b22'>9</text>
  <line x1="100" y1="110" x2="100" y2="75" stroke='#4f8ef7' stroke-width="3" stroke-linecap="round"/>
  <line x1="100" y1="110" x2="130" y2="110" stroke='#22c55e' stroke-width="2" stroke-linecap="round"/>
  <circle cx="100" cy="110" r="4" fill='#161b22'/>

  <!-- Digital clock -->
  <rect x="220" y="20" width="160" height="160" fill='#f3f4f6' stroke='#6b7280' stroke-width="2" rx="6"/>
  <text x="300" y="45" text-anchor='middle' font-size='13' font-weight='bold' fill='#161b22'>Digital Clock</text>

  <rect x="240" y="70" width="120" height="60" fill='currentColor' stroke='#374151' stroke-width="2" rx="4"/>
  <text x="300" y="115" text-anchor='middle' font-size='36' fill='#22c55e' font-family='monospace' font-weight='bold'>3:00</text>

  <text x="300" y="155" text-anchor='middle' font-size='10' fill='currentColor' opacity='0.6'>Shows numbers</text>
</svg>
<p>An <strong>analog clock</strong> has hands that point to numbers. A <strong>digital clock</strong> shows numbers on a screen.</p>
<p>In this lesson, we focus on <strong>analog clocks</strong> because understanding how the hands move teaches us how time works!</p>"""
    },
    {
        "title": "The Big Picture: Days, Weeks, Months, Years 📅",
        "body": """<p>Time doesn't just go in hours—it builds up into bigger and bigger units!</p>
<svg viewBox="0 0 400 350" style="width:100%;max-width:400px;display:block;margin:20px auto;">
  <text x="200" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='#161b22'>How Time Builds Up</text>

  <!-- 60 seconds = 1 minute -->
  <rect x="20" y="50" width="360" height="50" fill='#dbeafe' stroke='#3b82f6' stroke-width="1" rx="4"/>
  <text x="40" y="75" font-size='12' fill='#161b22'>60 seconds = <strong>1 minute</strong></text>
  <text x="290" y="75" font-size='11' fill='currentColor' opacity='0.6'>⏱️ Tick tock</text>

  <!-- 60 minutes = 1 hour -->
  <rect x="20" y="110" width="360" height="50" fill='#fef3c7' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <text x="40" y="135" font-size='12' fill='#161b22'>60 minutes = <strong>1 hour</strong></text>
  <text x="290" y="135" font-size='11' fill='currentColor' opacity='0.6'>🕐 Clock hands</text>

  <!-- 24 hours = 1 day -->
  <rect x="20" y="170" width="360" height="50" fill='#dbeafe' stroke='#3b82f6' stroke-width="1" rx="4"/>
  <text x="40" y="195" font-size='12' fill='#161b22'>24 hours = <strong>1 day</strong></text>
  <text x="290" y="195" font-size='11' fill='currentColor' opacity='0.6'>🌅→🌆→🌙</text>

  <!-- 7 days = 1 week -->
  <rect x="20" y="230" width="360" height="50" fill='#d1fae5' stroke='#10b981' stroke-width="1" rx="4"/>
  <text x="40" y="255" font-size='12' fill='#161b22'>7 days = <strong>1 week</strong></text>
  <text x="290" y="255" font-size='11' fill='currentColor' opacity='0.6'>📅 School week</text>

  <!-- 12 months = 1 year -->
  <rect x="20" y="290" width="360" height="50" fill='#f5d3e4' stroke='#ec4899' stroke-width="1" rx="4"/>
  <text x="40" y="315" font-size='12' fill='#161b22'>12 months = <strong>1 year</strong></text>
  <text x="290" y="315" font-size='11' fill='currentColor' opacity='0.6'>🎂 Birthday!</text>
</svg>
<p style="text-align: center; margin-top: 20px; font-size: 12">All of these build up—seconds become minutes, minutes become hours, hours become days, and so on!</p>"""
    }
]
