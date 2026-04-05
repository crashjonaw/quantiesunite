TITLE = "What is an Angle?"

SECTIONS = [
    {
        "title": "Understanding Angles in Real Life",
        "body": """
<div class='concept-box'>
  <p><strong>Imagine opening a door.</strong> The door frame stays still. The door moves. The angle is the amount of turn between them. A slightly open door = a small angle. A door wide open = a large angle.</p>
  <p>An angle measures <strong>how much something has turned</strong> from one direction to another. Every angle has a starting point called a <strong>vertex</strong> (like the hinge of the door).</p>
</div>

<svg viewBox="0 0 300 250" style="width:100%;max-width:400px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Door frame (vertical line) -->
  <line x1="150" y1="50" x2="150" y2="200" stroke='#8b949e' stroke-width="3"/>
  <!-- Door (at 45 degree angle) -->
  <line x1="150" y1="125" x2="220" y2="55" stroke='#4f8ef7' stroke-width="4"/>
  <!-- Arc showing the angle -->
  <path d="M 150 125 Q 180 110 200 85" stroke='#22c55e' stroke-width="2" fill='none' stroke-dasharray="5,5"/>
  <!-- Vertex point -->
  <circle cx="150" cy="125" r="4" fill='#ff6b6b'/>
  <!-- Labels -->
  <text x="155" y="150" fill='#0969da' font-size='14' font-weight='bold'>Vertex (hinge)</text>
  <text x="160" y="80" fill='#22c55e' font-size='13'>The angle of rotation</text>
</svg>

<div class='worked-example'>
  <p><strong>Key idea:</strong> An angle is formed by two rays (half-lines) that start from the same point.</p>
  <ul>
    <li>The starting point = <strong>vertex</strong></li>
    <li>The two rays = the sides of the angle</li>
    <li>The opening between them = the <strong>measure</strong> of the angle</li>
  </ul>
</div>
        """
    },
    {
        "title": "Measuring Angles in Degrees",
        "body": """
<p>We measure angles in <strong>degrees</strong>, shown with the symbol <strong>°</strong>. Think of degrees like steps around a circle.</p>

<div class='concept-box'>
  <p>A complete circle = <strong>360°</strong> (one full turn, like spinning all the way around)</p>
  <p>Half a circle = <strong>180°</strong> (half turn)</p>
  <p>Quarter circle = <strong>90°</strong> (quarter turn, like a right angle)</p>
</div>

<svg viewBox="0 0 400 350" style="width:100%;max-width:450px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Circle showing 360 degrees -->
  <circle cx="200" cy="180" r="120" fill='none' stroke='#8b949e' stroke-width="2" opacity='0.5'/>
  <!-- 0 degrees line -->
  <line x1="200" y1="180" x2="320" y2="180" stroke='#0969da' stroke-width="2"/>
  <!-- 90 degree arc and line -->
  <path d="M 320 180 A 120 120 0 0 0 200 60" stroke='#22c55e' stroke-width="3" fill='none'/>
  <line x1="200" y1="180" x2="200" y2="60" stroke='#22c55e' stroke-width="2"/>
  <!-- 180 degree line -->
  <line x1="200" y1="180" x2="80" y2="180" stroke='#ff6b6b' stroke-width="2" stroke-dasharray="3,3"/>
  <!-- Labels -->
  <text x="320" y="200" fill='#0969da' font-size='12'>0°</text>
  <text x="180" y="50" fill='#22c55e' font-size='12'>90°</text>
  <text x="60" y="200" fill='#ff6b6b' font-size='12'>180°</text>
  <text x="200" y="320" fill='#24292f' font-size='14' font-weight='bold' text-anchor='middle'>360° = Full turn</text>
</svg>

<div class='worked-example'>
  <p><strong>Why 360?</strong> Mathematicians in ancient Babylon chose 360 because it divides evenly into many numbers (2, 3, 4, 5, 6, 8, 9, 10, 12...). This makes working with angles easier!</p>
</div>
        """
    },
    {
        "title": "Angles Everywhere Around You",
        "body": """
<p>Angles are not just in maths class. They are everywhere in the real world:</p>

<div class='concept-box'>
  <ul style='list-style-type: none; padding: 0;'>
    <li><strong>🕐 Clock hands:</strong> The angle between hour and minute hands changes every minute</li>
    <li><strong>✂️ Scissors:</strong> The blades form an angle that opens and closes</li>
    <li><strong>⛺ Tent:</strong> The fabric is held up by two poles that form an angle</li>
    <li><strong>📐 Roof:</strong> The slope of a roof is an angle (steep = large angle, flat = small angle)</li>
    <li><strong>🚀 Launch:</strong> Rockets launch at angles to reach space</li>
  </ul>
</div>

<svg viewBox="0 0 300 200" style="width:100%;max-width:350px;height:auto;display:block;margin:16px auto;background:#f6f8fa;border-radius:8px;">
  <!-- Scissors -->
  <circle cx="80" cy="100" r="3" fill='#ff6b6b'/>
  <!-- Left blade -->
  <line x1="80" y1="100" x2="40" y2="70" stroke='#4f8ef7' stroke-width="3"/>
  <!-- Right blade -->
  <line x1="80" y1="100" x2="40" y2="130" stroke='#4f8ef7' stroke-width="3"/>
  <!-- Arc showing angle -->
  <path d="M 65 85 A 20 20 0 0 0 65 115" stroke='#22c55e' stroke-width="2" fill='none'/>
  <text x="65" y="105" fill='#22c55e' font-size='12'>Angle</text>

  <!-- Clock -->
  <circle cx="230" cy="100" r="40" fill='none' stroke='#8b949e' stroke-width="2"/>
  <circle cx="230" cy="100" r="2" fill='#24292f'/>
  <!-- Hour hand (pointing to 10) -->
  <line x1="230" y1="100" x2="215" y2="75" stroke='#ff6b6b' stroke-width="3"/>
  <!-- Minute hand (pointing to 12) -->
  <line x1="230" y1="100" x2="230" y2="65" stroke='#0969da' stroke-width="2"/>
  <text x="230" y="160" fill='#24292f' font-size='12' text-anchor='middle'>Angle between hands</text>
</svg>

<div class='success-box'>
  <p><strong>Remember:</strong> Whenever two lines, rays, or objects meet at a point, they form an angle. Understanding angles helps us understand movement, rotation, and the shapes of objects around us!</p>
</div>
        """
    },
    {
        "title": "Three Key Angle Facts",
        "body": """
<div class='worked-example'>
  <p><strong>Fact 1: Angles are measured from a starting ray</strong></p>
  <p>We always measure an angle from one ray (the starting position) to another ray (the ending position). It's like measuring a turn from where you started.</p>
</div>

<div class='worked-example'>
  <p><strong>Fact 2: Angles can be any size from 0° to 360° (and beyond!)</strong></p>
  <p>A \\(0°\\) angle means no turn at all (the rays point the same way). A \\(360°\\) angle means one complete spin. You can even have angles bigger than \\(360°\\) if you spin more than once!</p>
</div>

<div class='worked-example'>
  <p><strong>Fact 3: The vertex is where the turn starts</strong></p>
  <p>The vertex is the most important part. It's the corner point where both rays meet. Without a vertex, there's no angle!</p>
</div>

<div class='success-box'>
  <p><strong>Quick Check:</strong> Can you identify the vertex and the two rays in these situations?</p>
  <ul>
    <li>A door opening (hinge = vertex)</li>
    <li>Scissors closing (the pivot = vertex)</li>
    <li>A clock hand moving (center of clock = vertex)</li>
  </ul>
</div>
        """
    }
]
