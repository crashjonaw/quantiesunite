"""What is Time? — Primary 1-2 lesson."""

TITLE = "What is Time?"

SECTIONS = [
    {
        "title": "How Do We Know When Things Happen? ⏰",
        "body": """<p>How do you know when to wake up, eat lunch, or go to bed? <strong>Time tells us WHERE we are in the day.</strong></p>
<p>Time is like an invisible clock that keeps going and going. Every second, every minute, every hour moves us forward through our day.</p>
<svg viewBox="0 0 415 265" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <rect x="15" y="15" width="385" height="235" fill='#f0f8ff' stroke='#4f8ef7' stroke-width="2" rx="4"/>
  <text x="207" y="45" text-anchor='middle' font-size='18' font-weight='bold' fill='#1a1a2e'>Timeline of a Day</text>

  <line x1="50" y1="90" x2="365" y2="90" stroke='#4f8ef7' stroke-width="2"/>

  <circle cx="50" cy="90" r="5" fill='#22c55e'/>
  <text x="50" y="120" text-anchor='middle' font-size='12' fill='#1a1a2e'>Wake up</text>
  <text x="50" y="135" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>7 AM</text>

  <circle cx="155" cy="90" r="5" fill='#fbbf24'/>
  <text x="155" y="120" text-anchor='middle' font-size='12' fill='#1a1a2e'>Lunch</text>
  <text x="155" y="135" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>12 PM</text>

  <circle cx="260" cy="90" r="5" fill='#f97316'/>
  <text x="260" y="120" text-anchor='middle' font-size='12' fill='#1a1a2e'>School ends</text>
  <text x="260" y="135" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>3 PM</text>

  <circle cx="365" cy="90" r="5" fill='#8b5cf6'/>
  <text x="365" y="120" text-anchor='middle' font-size='12' fill='#1a1a2e'>Bedtime</text>
  <text x="365" y="135" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>9 PM</text>

  <text x="207" y="190" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>Time moves forward all day long</text>
</svg>
<p><strong>Why learn time?</strong> Time helps us plan our day, meet with friends, and know when to do important things!</p>"""
    },
    {
        "title": "Time Units: Seconds, Minutes, Hours",
        "body": """<p>We measure time using small units that build up into bigger units.</p>
<div style="background: #f0f8ff; padding: 16px; margin: 16px 0; border-radius: 4px; color: #1a1a2e;">
<p style="margin: 0; font-weight: bold;">Time conversions to remember:</p>
<p style="margin: 8px 0;">60 seconds = 1 minute</p>
<p style="margin: 8px 0;">60 minutes = 1 hour</p>
<p style="margin: 8px 0;">24 hours = 1 day</p>
</div>
<svg viewBox="0 0 415 290" style="width:100%;max-width:415px;height:auto;display:block;margin:20px auto;">
  <text x="207" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>What does each unit measure?</text>

  <!-- Seconds box -->
  <rect x="15" y="50" width="120" height="105" fill='#e0f2fe' stroke='#0284c7' stroke-width="2" rx="4"/>
  <text x="75" y="75" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Seconds</text>
  <text x="75" y="95" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>Very short</text>
  <text x="75" y="110" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>time</text>
  <text x="75" y="130" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>Snap your</text>
  <text x="75" y="145" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>fingers</text>

  <!-- Minutes box -->
  <rect x="148" y="50" width="120" height="105" fill='#fef3c7' stroke='#d97706' stroke-width="2" rx="4"/>
  <text x="208" y="75" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Minutes</text>
  <text x="208" y="95" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>Medium</text>
  <text x="208" y="110" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>time</text>
  <text x="208" y="130" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>Sing a</text>
  <text x="208" y="145" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>song</text>

  <!-- Hours box -->
  <rect x="281" y="50" width="120" height="105" fill='#dcfce7' stroke='#16a34a' stroke-width="2" rx="4"/>
  <text x="341" y="75" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Hours</text>
  <text x="341" y="95" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>Long</text>
  <text x="341" y="110" text-anchor='middle' font-size='11' fill='#1a1a2e' opacity='0.6'>time</text>
  <text x="341" y="130" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>Watch a</text>
  <text x="341" y="145" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>movie</text>

  <!-- Real examples -->
  <text x="15" y="190" font-size='12' fill='currentColor'>Real examples:</text>
  <text x="15" y="212" font-size='11' fill='currentColor' opacity='0.6'>Brushing teeth = 2 minutes</text>
  <text x="15" y="232" font-size='11' fill='currentColor' opacity='0.6'>Playing at recess = 15 minutes</text>
  <text x="15" y="252" font-size='11' fill='currentColor' opacity='0.6'>Math lesson = 1 hour</text>
  <text x="15" y="272" font-size='11' fill='currentColor' opacity='0.6'>Whole school day = 6 hours</text>
</svg>"""
    },
    {
        "title": "Clocks Are Tools We Invented 🕐",
        "body": """<p>Clocks are special tools that show us what <strong>time it is right now.</strong> People invented clocks to measure and display time.</p>
<p>There are two main types of clocks:</p>
<svg viewBox="0 0 415 215" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <!-- Analog clock -->
  <rect x="15" y="15" width="180" height="185" fill='#f3f4f6' stroke='#6b7280' stroke-width="2" rx="4"/>
  <text x="105" y="40" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Analog Clock</text>

  <circle cx="105" cy="115" r="55" fill='#fff' stroke='#8B0000' stroke-width="3"/>
  <text x="105" y="75" text-anchor='middle' font-size='12' fill='#000'>12</text>
  <text x="150" y="120" text-anchor='middle' font-size='12' fill='#000'>3</text>
  <text x="105" y="162" text-anchor='middle' font-size='12' fill='#000'>6</text>
  <text x="60" y="120" text-anchor='middle' font-size='12' fill='#000'>9</text>
  <!-- Minute hand to 12 -->
  <line x1="105" y1="115" x2="105" y2="70" stroke='#1a1a2e' stroke-width="2" stroke-linecap="round"/>
  <!-- Hour hand to 3 -->
  <line x1="105" y1="115" x2="145" y2="115" stroke='#1a1a2e' stroke-width="3" stroke-linecap="round"/>
  <circle cx="105" cy="115" r="4" fill='#1a1a2e'/>

  <!-- Digital clock -->
  <rect x="220" y="15" width="180" height="185" fill='#f3f4f6' stroke='#6b7280' stroke-width="2" rx="4"/>
  <text x="310" y="40" text-anchor='middle' font-size='13' font-weight='bold' fill='#1a1a2e'>Digital Clock</text>

  <rect x="245" y="75" width="130" height="55" fill='#1a1a2e' stroke='#374151' stroke-width="2" rx="4"/>
  <text x="310" y="115" text-anchor='middle' font-size='36' fill='#22c55e' font-family='monospace' font-weight='bold'>3:00</text>

  <text x="310" y="160" text-anchor='middle' font-size='10' fill='#1a1a2e' opacity='0.6'>Shows numbers</text>
</svg>
<p>An <strong>analog clock</strong> has hands that point to numbers. A <strong>digital clock</strong> shows numbers on a screen.</p>
<p>In this lesson, we focus on <strong>analog clocks</strong> because understanding how the hands move teaches us how time works!</p>"""
    },
    {
        "title": "The Big Picture: Days, Weeks, Months, Years",
        "body": """<p>Time doesn't just go in hours -- it builds up into bigger and bigger units!</p>
<svg viewBox="0 0 415 360" style="width:100%;max-width:415px;display:block;margin:20px auto;">
  <text x="207" y="30" text-anchor='middle' font-size='16' font-weight='bold' fill='currentColor'>How Time Builds Up</text>

  <!-- 60 seconds = 1 minute -->
  <rect x="15" y="50" width="385" height="50" fill='#dbeafe' stroke='#3b82f6' stroke-width="1" rx="4"/>
  <text x="35" y="80" font-size='13' fill='#1e3a5f'>60 seconds = 1 minute</text>
  <text x="355" y="80" text-anchor='middle' font-size='12' fill='#1e3a5f' opacity='0.7'>Tick tock</text>

  <!-- 60 minutes = 1 hour -->
  <rect x="15" y="112" width="385" height="50" fill='#fef3c7' stroke='#f59e0b' stroke-width="1" rx="4"/>
  <text x="35" y="142" font-size='13' fill='#5c3d00'>60 minutes = 1 hour</text>
  <text x="355" y="142" text-anchor='middle' font-size='12' fill='#5c3d00' opacity='0.7'>Clock hands</text>

  <!-- 24 hours = 1 day -->
  <rect x="15" y="174" width="385" height="50" fill='#dbeafe' stroke='#3b82f6' stroke-width="1" rx="4"/>
  <text x="35" y="204" font-size='13' fill='#1e3a5f'>24 hours = 1 day</text>
  <text x="355" y="204" text-anchor='middle' font-size='12' fill='#1e3a5f' opacity='0.7'>Morning to night</text>

  <!-- 7 days = 1 week -->
  <rect x="15" y="236" width="385" height="50" fill='#d1fae5' stroke='#10b981' stroke-width="1" rx="4"/>
  <text x="35" y="266" font-size='13' fill='#064e3b'>7 days = 1 week</text>
  <text x="355" y="266" text-anchor='middle' font-size='12' fill='#064e3b' opacity='0.7'>School week</text>

  <!-- 12 months = 1 year -->
  <rect x="15" y="298" width="385" height="50" fill='#f5d3e4' stroke='#ec4899' stroke-width="1" rx="4"/>
  <text x="35" y="328" font-size='13' fill='#831843'>12 months = 1 year</text>
  <text x="355" y="328" text-anchor='middle' font-size='12' fill='#831843' opacity='0.7'>Birthday!</text>
</svg>
<p style="text-align: center; margin-top: 20px; font-size: 12">All of these build up -- seconds become minutes, minutes become hours, hours become days, and so on!</p>"""
    }
]
