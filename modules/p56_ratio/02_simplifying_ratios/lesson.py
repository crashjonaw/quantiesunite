TITLE = "Simplifying Ratios to Lowest Terms"

SECTIONS = [
    {
        "title": "What Does Simplifying a Ratio Mean?",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Ratio in Simplest Form</h3>
    <p>A ratio is in <strong>simplest form</strong> (or <strong>lowest terms</strong>) when the two numbers have no common factors except 1.</p>
    <p>Just like we simplify fractions, we simplify ratios by dividing both parts by their greatest common factor (GCF).</p>
    <p><strong>Example:</strong> The ratio \\(12:8\\) can be simplified to \\(3:2\\)</p>
  </div>

  <div class="success-box">
    <h4>Why Simplify?</h4>
    <ul>
      <li>Simplified ratios are easier to understand and work with</li>
      <li>They show the relationship in its clearest form</li>
      <li>It's easier to see that \\(3:2\\) than \\(30:20\\) or \\(300:200\\)</li>
      <li>In mathematics, we always present answers in simplest form</li>
    </ul>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
      <text x="250" y="30" font-size='14' font-weight='bold' text-anchor='middle' fill='currentColor'>These ratios are equivalent but only 3:2 is simplified</text>

      <text x="50" y="70" font-size='12' fill='currentColor'>12:8</text>
      <rect x="50" y="80" width="80" height="40" fill='#4169E1' opacity='0.6' stroke='#30363d' stroke-width="2"/>
      <rect x="140" y="80" width="60" height="40" fill='#22c55e' opacity='0.6' stroke='#30363d' stroke-width="2"/>

      <path d="M 220 100 L 260 100" stroke='currentColor' stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="240" y="90" font-size='11' fill='currentColor' text-anchor='middle'>÷4</text>

      <text x="280" y="70" font-size='12' fill='currentColor'>3:2 (simplified)</text>
      <rect x="280" y="80" width="30" height="40" fill='#4169E1' opacity='0.6' stroke='#30363d' stroke-width="2"/>
      <rect x="320" y="80" width="20" height="40" fill='#22c55e' opacity='0.6' stroke='#30363d' stroke-width="2"/>

      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill='currentColor'/>
        </marker>
      </defs>

      <text x="50" y="160" font-size='11' fill='currentColor'>12:8 has a GCF of 4</text>
      <text x="50" y="180" font-size='11' fill='currentColor'>12÷4 = 3, and 8÷4 = 2, so 12:8 = 3:2</text>
    </svg>
  </div>
</div>"""
    },
    {
        "title": "Finding the GCF (Greatest Common Factor)",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Step 1: Find the GCF</h3>
    <p>The <strong>Greatest Common Factor (GCF)</strong> is the largest number that divides evenly into both numbers in the ratio.</p>
  </div>

  <div class="steps-container">
    <h3>Method to Find GCF</h3>
    <div class="step">
      <h4>Example: Find GCF of 18 and 24</h4>
      <p><strong>Step A: List all factors</strong></p>
      <p>Factors of 18: 1, 2, 3, 6, 9, 18</p>
      <p>Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24</p>
    </div>
    <div class="step">
      <h4>Step B: Find common factors</h4>
      <p>Numbers that appear in BOTH lists:</p>
      <p>Common factors: 1, 2, 3, 6</p>
    </div>
    <div class="step">
      <h4>Step C: Pick the greatest</h4>
      <p>The greatest (largest) common factor = <strong>6</strong></p>
    </div>
  </div>

  <div class="worked-example">
    <h4>Finding GCF: More Examples</h4>
    <p><strong>Example 1: GCF of 15 and 25</strong></p>
    <ul>
      <li>Factors of 15: 1, 3, 5, 15</li>
      <li>Factors of 25: 1, 5, 25</li>
      <li>Common factors: 1, 5</li>
      <li><strong>GCF = 5</strong></li>
    </ul>

    <p><strong>Example 2: GCF of 20 and 30</strong></p>
    <ul>
      <li>Factors of 20: 1, 2, 4, 5, 10, 20</li>
      <li>Factors of 30: 1, 2, 3, 5, 6, 10, 15, 30</li>
      <li>Common factors: 1, 2, 5, 10</li>
      <li><strong>GCF = 10</strong></li>
    </ul>
  </div>

  <div class="success-box">
    <h4>Quick Tip: Division Method</h4>
    <p>You can also find GCF by testing prime numbers (2, 3, 5, 7, 11...):</p>
    <p>For 24:36: both divisible by 2? Yes (12:18) → both divisible by 2? Yes (6:9) → both divisible by 3? Yes (2:3) → GCF = 2×2×3 = 12</p>
  </div>
</div>"""
    },
    {
        "title": "Simplifying Ratios Step by Step",
        "body": """<div class="lesson-container">
  <div class="steps-container">
    <h3>Complete Method: Simplify a Ratio</h3>
    <div class="step">
      <h4>Step 1: Find the GCF</h4>
      <p>For ratio 18:24</p>
      <p>Factors of 18: 1, 2, 3, 6, 9, 18</p>
      <p>Factors of 24: 1, 2, 3, 4, 6, 8, 12, 24</p>
      <p>GCF = 6</p>
    </div>
    <div class="step">
      <h4>Step 2: Divide both parts by the GCF</h4>
      <p>18 ÷ 6 = 3</p>
      <p>24 ÷ 6 = 4</p>
      <p>So 18:24 = 3:4</p>
    </div>
    <div class="step">
      <h4>Step 3: Verify it's simplified</h4>
      <p>Are 3 and 4 coprime? (No common factors except 1?)</p>
      <p>Yes! 3 and 4 share no common factors.</p>
      <p>Therefore 3:4 is in simplest form.</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 550 350" xmlns="http://www.w3.org/2000/svg">
      <text x="275" y="30" font-size='14' font-weight='bold' text-anchor='middle' fill='currentColor'>Simplifying 20:30</text>

      <text x="50" y="70" font-size='12' fill='currentColor'>Start: 20:30</text>

      <text x="50" y="100" font-size='11' fill='currentColor'>Find GCF</text>
      <text x="50" y="120" font-size='11' fill='currentColor'>20 = 2 × 10 = 2 × 2 × 5</text>
      <text x="50" y="140" font-size='11' fill='currentColor'>30 = 2 × 15 = 2 × 3 × 5</text>
      <text x="50" y="160" font-size='11' fill='currentColor'>Common: 2 × 5 = 10, so GCF = 10</text>

      <text x="50" y="190" font-size='11' fill='currentColor'>Divide both by 10</text>
      <text x="50" y="210" font-size='11' fill='currentColor'>20 ÷ 10 = 2</text>
      <text x="50" y="230" font-size='11' fill='currentColor'>30 ÷ 10 = 3</text>

      <text x="50" y="270" font-size='12' font-weight='bold' fill='#22c55e'>Result: 2:3 (simplified)</text>

      <text x="50" y="310" font-size='11' fill='currentColor'>Check: 2 and 3 share no common factors → simplified ✓</text>
    </svg>
  </div>

  <div class="worked-example">
    <h4>Practice Example: Simplify 15:25</h4>
    <p><strong>Step 1: Find GCF</strong></p>
    <p>GCF of 15 and 25 is 5</p>
    <p><strong>Step 2: Divide by GCF</strong></p>
    <p>15 ÷ 5 = 3</p>
    <p>25 ÷ 5 = 5</p>
    <p><strong>Step 3: Answer</strong></p>
    <p>15:25 simplifies to <strong>3:5</strong></p>
  </div>
</div>"""
    },
    {
        "title": "Checking Your Work",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>How to Know If a Ratio is Fully Simplified</h3>
    <p>A ratio is in simplest form when:</p>
    <ul>
      <li>The two numbers have NO common factors except 1</li>
      <li>You cannot divide both by the same number anymore</li>
      <li>The numbers are as small as they can be while keeping the same relationship</li>
    </ul>
  </div>

  <div class="warning-box">
    <h4>Common Mistakes to Avoid</h4>
    <ul>
      <li><strong>❌ Wrong:</strong> Simplify 12:8 to 6:4 (only divided by 2, not fully simplified)</li>
      <li><strong>✓ Correct:</strong> Simplify 12:8 to 3:2 (divided by GCF of 4)</li>
      <li><strong>❌ Wrong:</strong> Simplify 15:25 by subtracting: 15 - 10 = 5 to get 5:25</li>
      <li><strong>✓ Correct:</strong> Simplify 15:25 by dividing: 15÷5 and 25÷5 to get 3:5</li>
      <li><strong>❌ Wrong:</strong> Divide only one number: 12:8 becomes 3:8</li>
      <li><strong>✓ Correct:</strong> Divide BOTH: 12:8 becomes 3:2</li>
    </ul>
  </div>

  <div class="worked-example">
    <h4>Verification: Is 5:8 simplified?</h4>
    <p><strong>Check factors:</strong></p>
    <ul>
      <li>Factors of 5: 1, 5</li>
      <li>Factors of 8: 1, 2, 4, 8</li>
      <li>Only common factor: 1</li>
    </ul>
    <p><strong>Answer: YES, 5:8 is fully simplified</strong></p>
  </div>

  <div class="worked-example">
    <h4>Verification: Is 10:15 simplified?</h4>
    <p><strong>Check factors:</strong></p>
    <ul>
      <li>Factors of 10: 1, 2, 5, 10</li>
      <li>Factors of 15: 1, 3, 5, 15</li>
      <li>Common factors: 1, 5</li>
    </ul>
    <p><strong>Answer: NO, it's not simplified. GCF is 5, so 10:15 = 2:3</strong></p>
  </div>

  <div class="success-box">
    <h4>The Test:</h4>
    <p><strong>Ask yourself: Can I divide both numbers by the same whole number (other than 1)?</strong></p>
    <ul>
      <li>If YES → not simplified yet, divide both</li>
      <li>If NO → you're done! It's simplified</li>
    </ul>
  </div>
</div>"""
    }
]
