TITLE = "Equivalent Ratios and Scaling"

SECTIONS = [
    {
        "title": "What Are Equivalent Ratios?",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Equivalent Ratios Are Equal Relationships</h3>
    <p>Two ratios are <strong>equivalent</strong> if they represent the same relationship.</p>
    <p>Just like equivalent fractions ($$\\frac{1}{2} = \\frac{2}{4} = \\frac{3}{6}$$), equivalent ratios show the same comparison in different forms.</p>
    <p><strong>Example:</strong> The ratios \\(2:3\\), \\(4:6\\), \\(6:9\\), and \\(8:12\\) are all equivalent. They all mean "for every 2 of the first, there are 3 of the second."</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 550 300" xmlns="http://www.w3.org/2000/svg">
      <text x="275" y="30" font-size='14' font-weight='bold' text-anchor='middle' fill='currentColor'>Recipe: Same Relationship, Different Amounts</text>

      <text x="50" y="70" font-size='12' fill='currentColor'>Normal recipe (2:3)</text>
      <rect x="50" y="80" width="80" height="40" fill='#f59e0b' opacity='0.6' stroke='#30363d' stroke-width="2"/>
      <rect x="140" y="80" width="120" height="40" fill='#22c55e' opacity='0.6' stroke='#30363d' stroke-width="2"/>
      <text x="90" y="105" font-size='11' text-anchor='middle' fill='#161b22' font-weight='bold'>2 flour</text>
      <text x="200" y="105" font-size='11' text-anchor='middle' fill='#161b22' font-weight='bold'>3 sugar</text>

      <text x="50" y="160" font-size='12' fill='currentColor'>Double recipe (4:6)</text>
      <rect x="50" y="170" width="160" height="40" fill='#f59e0b' opacity='0.6' stroke='#30363d' stroke-width="2"/>
      <rect x="220" y="170" width="240" height="40" fill='#22c55e' opacity='0.6' stroke='#30363d' stroke-width="2"/>
      <text x="130" y="195" font-size='11' text-anchor='middle' fill='#161b22' font-weight='bold'>4 flour</text>
      <text x="340" y="195" font-size='11' text-anchor='middle' fill='#161b22' font-weight='bold'>6 sugar</text>

      <text x="50" y="250" font-size='11' fill='currentColor'>2:3 = 4:6 = 6:9 = 8:12...</text>
      <text x="50" y="270" font-size='11' fill='currentColor'>All equivalent! Same relationship, different scale.</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>Key Insight:</h4>
    <p>If you multiply (or divide) BOTH parts of a ratio by the same number, you get an equivalent ratio.</p>
    <p>$$a : b = (a \\times k) : (b \\times k)$$ for any number $$k$$</p>
  </div>
</div>"""
    },
    {
        "title": "Scaling Ratios Up (Multiplying)",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Scaling Up: Making a Ratio Bigger</h3>
    <p>To scale a ratio UP, multiply both parts by the same number.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Scale Up a Ratio</h3>
    <div class="step">
      <h4>Example 1: Multiply 3:5 by 2</h4>
      <p>3:5 × 2 = (3 × 2) : (5 × 2) = 6:10</p>
      <p><strong>Check:</strong> Both ratios mean the same thing!</p>
    </div>
    <div class="step">
      <h4>Example 2: Multiply 2:7 by 3</h4>
      <p>2:7 × 3 = (2 × 3) : (7 × 3) = 6:21</p>
    </div>
    <div class="step">
      <h4>Example 3: Multiply 1:4 by 5</h4>
      <p>1:4 × 5 = (1 × 5) : (4 × 5) = 5:20</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg">
      <text x="250" y="30" font-size='13' font-weight='bold' text-anchor='middle' fill='currentColor'>Scaling Up Ratio 2:3</text>

      <text x="50" y="70" font-size='11' fill='currentColor'>Start: 2:3</text>
      <circle cx="70" cy="90" r="10" fill='#4169E1'/>
      <circle cx="95" cy="90" r="10" fill='#4169E1'/>
      <circle cx="130" cy="90" r="10" fill='#22c55e'/>
      <circle cx="155" cy="90" r="10" fill='#22c55e'/>
      <circle cx="180" cy="90" r="10" fill='#22c55e'/>

      <text x="50" y="140" font-size='11' fill='currentColor'>×2: 4:6</text>
      <circle cx="70" cy="160" r="8" fill='#4169E1'/>
      <circle cx="90" cy="160" r="8" fill='#4169E1'/>
      <circle cx="110" cy="160" r="8" fill='#4169E1'/>
      <circle cx="130" cy="160" r="8" fill='#4169E1'/>
      <circle cx="155" cy="160" r="8" fill='#22c55e'/>
      <circle cx="175" cy="160" r="8" fill='#22c55e'/>
      <circle cx="195" cy="160" r="8" fill='#22c55e'/>
      <circle cx="215" cy="160" r="8" fill='#22c55e'/>
      <circle cx="235" cy="160" r="8" fill='#22c55e'/>
      <circle cx="255" cy="160" r="8" fill='#22c55e'/>

      <text x="50" y="210" font-size='11' fill='currentColor'>×3: 6:9</text>

      <text x="300" y="70" font-size='11' fill='currentColor'>Original ratio 2:3:</text>
      <text x="300" y="90" font-size='11' fill='currentColor'>For every 2 blue,</text>
      <text x="300" y="110" font-size='11' fill='currentColor'>there are 3 green</text>
      <text x="300" y="140" font-size='11' fill='currentColor'>Double it (×2): 4:6</text>
      <text x="300" y="160" font-size='11' fill='currentColor'>Still "2 blue for every 3 green"</text>
      <text x="300" y="180" font-size='11' fill='currentColor'>just with bigger numbers</text>
    </svg>
  </div>

  <div class="worked-example">
    <h4>Real Example: Scaling a Recipe</h4>
    <p><strong>Recipe ratio:</strong> Flour to sugar is \\(2:1\\)</p>
    <p><strong>Normal (×1):</strong> 2 cups flour, 1 cup sugar</p>
    <p><strong>Double (×2):</strong> 4 cups flour, 2 cups sugar</p>
    <p><strong>Triple (×3):</strong> 6 cups flour, 3 cups sugar</p>
    <p>All maintain the 2:1 ratio! More cake, same taste.</p>
  </div>
</div>"""
    },
    {
        "title": "Scaling Ratios Down (Dividing)",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Scaling Down: Making a Ratio Smaller</h3>
    <p>To scale a ratio DOWN, divide both parts by the same number (this is actually simplifying!).</p>
  </div>

  <div class="steps-container">
    <h3>Method: Scale Down a Ratio</h3>
    <div class="step">
      <h4>Example 1: Divide 12:8 by 4</h4>
      <p>12:8 ÷ 4 = (12 ÷ 4) : (8 ÷ 4) = 3:2</p>
      <p><strong>This is simplifying!</strong></p>
    </div>
    <div class="step">
      <h4>Example 2: Divide 20:15 by 5</h4>
      <p>20:15 ÷ 5 = (20 ÷ 5) : (15 ÷ 5) = 4:3</p>
    </div>
    <div class="step">
      <h4>Example 3: Divide 6:10 by 2</h4>
      <p>6:10 ÷ 2 = (6 ÷ 2) : (10 ÷ 2) = 3:5</p>
    </div>
  </div>

  <div class="warning-box">
    <h4>Important: You Can Only Divide If Both Are Divisible</h4>
    <p>You can only divide by a number if it divides evenly into BOTH parts of the ratio.</p>
    <ul>
      <li><strong>✓ Can do:</strong> 12:8 ÷ 4 (both divisible by 4)</li>
      <li><strong>❌ Cannot do:</strong> 12:8 ÷ 3 (8 is not divisible by 3)</li>
      <li><strong>✓ Can do:</strong> 12:8 ÷ 2 (both divisible by 2)</li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Real Example: Scaling Down a Map</h4>
    <p><strong>Map scale:</strong> 100:200 (meaning 100 map units : 200 real units)</p>
    <p><strong>Divide by 100:</strong> 1:2</p>
    <p>The simplified ratio 1:2 is much easier to understand! For every 1 unit on the map, there are 2 units in reality.</p>
  </div>
</div>"""
    },
    {
        "title": "Ratio Tables: Showing All Equivalent Ratios",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Ratio Tables Organize Equivalent Ratios</h3>
    <p>A <strong>ratio table</strong> shows equivalent ratios in an organized way. Each column represents a ratio equivalent to the others.</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 550 300" xmlns="http://www.w3.org/2000/svg">
      <text x="275" y="30" font-size='13' font-weight='bold' text-anchor='middle' fill='currentColor'>Ratio Table: Flour to Sugar (ratio 2:1)</text>

      <rect x="50" y="50" width="150" height="40" fill='#4169E1' opacity='0.3' stroke='#30363d' stroke-width="2"/>
      <rect x="200" y="50" width="150" height="40" fill='#22c55e' opacity='0.3' stroke='#30363d' stroke-width="2"/>

      <text x="125" y="75" font-size='12' font-weight='bold' text-anchor='middle' fill='currentColor'>Flour (cups)</text>
      <text x="275" y="75" font-size='12' font-weight='bold' text-anchor='middle' fill='currentColor'>Sugar (cups)</text>

      <rect x="50" y="90" width="150" height="35" fill='#4169E1' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <rect x="200" y="90" width="150" height="35" fill='#22c55e' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <text x="125" y="115" font-size='11' text-anchor='middle' fill='currentColor'>2</text>
      <text x="275" y="115" font-size='11' text-anchor='middle' fill='currentColor'>1</text>

      <rect x="50" y="125" width="150" height="35" fill='#4169E1' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <rect x="200" y="125" width="150" height="35" fill='#22c55e' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <text x="125" y="150" font-size='11' text-anchor='middle' fill='currentColor'>4</text>
      <text x="275" y="150" font-size='11' text-anchor='middle' fill='currentColor'>2</text>

      <rect x="50" y="160" width="150" height="35" fill='#4169E1' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <rect x="200" y="160" width="150" height="35" fill='#22c55e' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <text x="125" y="185" font-size='11' text-anchor='middle' fill='currentColor'>6</text>
      <text x="275" y="185" font-size='11' text-anchor='middle' fill='currentColor'>3</text>

      <rect x="50" y="195" width="150" height="35" fill='#4169E1' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <rect x="200" y="195" width="150" height="35" fill='#22c55e' opacity='0.2' stroke='#30363d' stroke-width="1"/>
      <text x="125" y="220" font-size='11' text-anchor='middle' fill='currentColor'>8</text>
      <text x="275" y="220" font-size='11' text-anchor='middle' fill='currentColor'>4</text>

      <text x="50" y="270" font-size='11' fill='currentColor'>×1 ×2 ×3 ×4</text>
      <text x="350" y="115" font-size='11' fill='currentColor'>2:1 (×1)</text>
      <text x="350" y="150" font-size='11' fill='currentColor'>4:2 (×2)</text>
      <text x="350" y="185" font-size='11' fill='currentColor'>6:3 (×3)</text>
      <text x="350" y="220" font-size='11' fill='currentColor'>8:4 (×4)</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>How to Read a Ratio Table:</h4>
    <ul>
      <li>Each column shows ONE equivalent ratio</li>
      <li>Multiply BOTH columns by the same number to move across</li>
      <li>The relationship stays constant: 2:1, 4:2, 6:3, 8:4 all have the same meaning</li>
      <li>You can go backward (divide) too!</li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Fill in the Missing Values</h4>
    <p><strong>Ratio table for 3:5:</strong></p>
    <table style="border-collapse: collapse; margin: 10px 0;">
      <tr >
        <td style="padding: 8px;">3</td>
        <td style="padding: 8px;">?</td>
        <td style="padding: 8px;">9</td>
        <td style="padding: 8px;">?</td>
      </tr>
      <tr >
        <td style="padding: 8px;">5</td>
        <td style="padding: 8px;">10</td>
        <td style="padding: 8px;">?</td>
        <td style="padding: 8px;">20</td>
      </tr>
    </table>
    <p><strong>Solutions:</strong> 3:5 | 6:10 (×2) | 9:15 (×3) | 12:20 (×4)</p>
  </div>
</div>"""
    }
]
