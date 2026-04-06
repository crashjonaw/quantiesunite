TITLE = "Multiplication and Addition Connection"
SECTIONS = [
    {
        "title": "Multiplication is Repeated Addition",
        "body": """<p>Remember: <strong>multiplication is just a shortcut for repeated addition.</strong></p>
<p>Instead of adding the same number over and over, we can multiply.</p>
<svg viewBox="0 0 500 200" style="width:100%; max-width:550px; height:auto; display:block; margin:16px auto; background: rgba(0,0,0,0.2); border-radius: 8px; padding: 16px;">
  <text x="250" y="30" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Multiplication = Fast Addition</text>

  <!-- Addition -->
  <text x="50" y="80" fill='currentColor' font-size='14'>The slow way:</text>
  <text x="50" y="105" fill='#4f8ef7' font-size='14' font-weight='bold'>5 + 5 + 5 + 5</text>
  <text x="50" y="130" fill='currentColor' font-size='12'>= 20</text>

  <!-- Arrow -->
  <text x="250" y="105" fill='currentColor' font-size='24'>→</text>

  <!-- Multiplication -->
  <text x="350" y="80" fill='currentColor' font-size='14'>The fast way:</text>
  <text x="350" y="105" fill='#22c55e' font-size='14' font-weight='bold'>4 × 5</text>
  <text x="350" y="130" fill='currentColor' font-size='12'>= 20</text>
</svg>
<p style="text-align: center; margin-top: 20px;"><strong>Same answer, much faster!</strong></p>"""
    },
    {
        "title": "Converting Between Multiplication and Addition",
        "body": """<p>You should be able to switch between multiplication and addition easily.</p>
<div class="worked-example" style="padding: 16px; border-radius: 6px; margin: 16px 0">
  <p style="margin: 0 0 12px 0; font-weight: bold;">Example 1: Convert multiplication to addition</p>
  <p style="margin: 0 0 8px 0;">\\(3 \\times 6\\) means:</p>
  <p style="margin: 0; color: #f59e0b; font-size: 15px;">\\(6 + 6 + 6 = 18\\)</p>
</div>
<div class="worked-example" style="background: rgba(34, 197, 94, 0.1); border-left: 4px solid #22c55e; padding: 16px; border-radius: 6px; margin: 16px 0;">
  <p style="margin: 0 0 12px 0; font-weight: bold;">Example 2: Convert addition to multiplication</p>
  <p style="margin: 0 0 8px 0;">\\(2 + 2 + 2 + 2 + 2\\) (5 groups of 2)</p>
  <p style="margin: 0; color: #f59e0b; font-size: 15px;">\\(5 \\times 2 = 10\\)</p>
</div>"""
    },
    {
        "title": "Why This Matters: Speed and Efficiency",
        "body": """<p>Imagine you're counting apples:</p>
<ul>
  <li><strong>Addition way:</strong> "I have 10 bags with 10 apples each. Let me count: 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10... That takes forever!"</li>
  <li><strong>Multiplication way:</strong> "I have 10 bags with 10 apples each. That's \(10 \times 10 = 100\) apples. Done!"</li>
</ul>
<p>Multiplication lets you answer faster and with fewer chances to make mistakes.</p>
<canvas id="efficiencyChart" data-chart='{"type":"bar","data":{"labels":["2×5","5×5","10×5"],"datasets":[{"label":"Number to Add","data":[5,5,5],"backgroundColor":"#4f8ef7"},{"label":"Total Items","data":[10,25,50],"backgroundColor":"#22c55e"}]},"options":{"plugins":{"title":{"display":true,"text":"Same Multiplication Problems, Growing Results"}}}}' height="250"></canvas>"""
    },
    {
        "title": "Connecting to Number Lines",
        "body": """<p>You can also see multiplication on a <strong>number line</strong> as repeated jumps!</p>
<svg viewBox="0 0 550 150" style="width:100%; max-width:600px; height:auto; display:block; margin:16px auto; background: rgba(0,0,0,0.2); border-radius: 8px; padding: 16px;">
  <text x="275" y="25" text-anchor='middle' fill='currentColor' font-size='15' font-weight='bold'>Number Line: 4 jumps of 3 = 4 × 3 = 12</text>

  <!-- Number line -->
  <line x1="50" y1="70" x2="500" y2="70" stroke='currentColor' stroke-width="2"/>

  <!-- Numbers -->
  <text x="50" y="95" text-anchor='middle' fill='currentColor' font-size='13'>0</text>
  <text x="112" y="95" text-anchor='middle' fill='currentColor' font-size='13'>3</text>
  <text x="174" y="95" text-anchor='middle' fill='currentColor' font-size='13'>6</text>
  <text x="236" y="95" text-anchor='middle' fill='currentColor' font-size='13'>9</text>
  <text x="298" y="95" text-anchor='middle' fill='currentColor' font-size='13'>12</text>
  <text x="360" y="95" text-anchor='middle' fill='#a0aec0' font-size='13'>15</text>
  <text x="422" y="95" text-anchor='middle' fill='#a0aec0' font-size='13'>18</text>
  <text x="484" y="95" text-anchor='middle' fill='#a0aec0' font-size='13'>21</text>

  <!-- Jumps -->
  <path d="M 50 55 Q 81 35 112 55" stroke='#f59e0b' stroke-width="2" fill='none' stroke-dasharray="4"/>
  <path d="M 112 55 Q 143 35 174 55" stroke='#f59e0b' stroke-width="2" fill='none' stroke-dasharray="4"/>
  <path d="M 174 55 Q 205 35 236 55" stroke='#f59e0b' stroke-width="2" fill='none' stroke-dasharray="4"/>
  <path d="M 236 55 Q 267 35 298 55" stroke='#f59e0b' stroke-width="2" fill='none' stroke-dasharray="4"/>

  <!-- Jump labels -->
  <text x="81" y="48" text-anchor='middle' fill='#f59e0b' font-size='11' font-weight='bold'>+3</text>
  <text x="143" y="48" text-anchor='middle' fill='#f59e0b' font-size='11' font-weight='bold'>+3</text>
  <text x="205" y="48" text-anchor='middle' fill='#f59e0b' font-size='11' font-weight='bold'>+3</text>
  <text x="267" y="48" text-anchor='middle' fill='#f59e0b' font-size='11' font-weight='bold'>+3</text>

  <!-- Start and end circles -->
  <circle cx="50" cy="70" r="6" fill='#22c55e'/>
  <circle cx="298" cy="70" r="6" fill='#ef4444'/>
</svg>
<p style="text-align: center; margin-top: 12px;">Starting at 0, we make 4 jumps of 3 steps each. We land on 12!</p>
<p style="text-align: center; font-size: 14px; ;">This is another way to understand why \\(4 \\times 3 = 12\\)</p>"""
    },
    {
        "title": "Practice: Switching Between Forms",
        "body": """<p>Try to convert between these forms:</p>
<div class="mcq-group" style="background: rgba(0,0,0,0.2); padding: 20px; border-radius: 6px; margin: 16px 0;">
  <p style="font-size: 16px; font-weight: bold;">Which addition is the same as \(5 \times 4\)?</p>
  <div class="mcq-options" style="display: flex; flex-direction: column; gap: 12px; margin-top: 12px;">
    <button class="mcq-option" data-correct="true" data-explanation="Yes! 5 × 4 means 5 groups of 4, which is 4 + 4 + 4 + 4 + 4 = 20" class="concept-box" style="cursor: pointer;">4 + 4 + 4 + 4 + 4</button>
    <button class="mcq-option" data-correct="false" class="concept-box" style="cursor: pointer;">5 + 5 + 5 + 5</button>
    <button class="mcq-option" data-correct="false" class="concept-box" style="cursor: pointer;">5 + 4</button>
  </div>
  <div class="mcq-feedback"></div>
</div>
<div class="success-box" style="background: rgba(34, 197, 94, 0.1); border-left: 4px solid #22c55e; padding: 16px; border-radius: 6px; margin: 20px 0;">
  <p style="margin: 0; font-weight: bold;">Remember:</p>
  <p style="margin: 8px 0 0 0;"><strong>\(5 \times 4\)</strong> = "5 groups of 4" = \(4 + 4 + 4 + 4 + 4 = 20\)</p>
</div>"""
    }
]
