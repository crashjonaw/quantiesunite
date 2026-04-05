TITLE = "Multiplying Fractions"

SECTIONS = [
    {
        "title": "Understanding Fraction Multiplication from First Principles",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>A Fraction OF a Fraction</h3>
    <p>You already know fractions represent parts of a whole. But what happens when you multiply \\(\\frac{1}{2} \\times \\frac{3}{4}\\)? You're taking a <strong>part of a part</strong>—which makes something even smaller!</p>
    <p>This is the key insight: multiplication shrinks, and fractions are about shrinking!</p>
    <p><strong>Example:</strong> \\(\\frac{1}{2} \\times \\frac{3}{4}\\) means "take 1 half of 3 fourths."</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 350" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='16' font-weight='bold'>Start with \\(\\frac{3}{4}\\):</text>
      <rect x="50" y="50" width="200" height="60" fill='none' stroke='#8b949e' stroke-width="2"/>
      <line x1="100" y1="50" x2="100" y2="110" stroke='#8b949e' stroke-width="1"/>
      <line x1="150" y1="50" x2="150" y2="110" stroke='#8b949e' stroke-width="1"/>
      <line x1="200" y1="50" x2="200" y2="110" stroke='#8b949e' stroke-width="1"/>
      <rect x="50" y="50" width="150" height="60" fill='#4169E1' opacity='0.6'/>

      <text x="50" y="150" font-size='16' font-weight='bold'>Take \\(\\frac{1}{2}\\) of that (cut in half horizontally):</text>
      <rect x="50" y="170" width="200" height="60" fill='none' stroke='#8b949e' stroke-width="2"/>
      <line x1="100" y1="170" x2="100" y2="230" stroke='#8b949e' stroke-width="1"/>
      <line x1="150" y1="170" x2="150" y2="230" stroke='#8b949e' stroke-width="1"/>
      <line x1="200" y1="170" x2="200" y2="230" stroke='#8b949e' stroke-width="1"/>
      <line x1="125" y1="170" x2="125" y2="230" stroke='#22c55e' stroke-width="2"/>
      <rect x="50" y="170" width="75" height="60" fill='#f59e0b' opacity='0.8'/>
      <text x="150" y="270" font-size='16' text-anchor='middle' font-weight='bold'>Result: \\(\\frac{3}{8}\\)</text>

      <text x="50" y="310" font-size='16' font-weight='bold'>$$\\frac{1}{2} \\times \\frac{3}{4} = \\frac{1 \\times 3}{2 \\times 4} = \\frac{3}{8}$$</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>The Main Idea:</h4>
    <p>When you multiply fractions, you're asking: "What fraction of a fraction?" The answer is always <strong>smaller</strong> than what you started with (unless one fraction is 1 or more).</p>
  </div>
</div>"""
    },
    {
        "title": "The Multiplication Rule: Numerators and Denominators",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Multiply Across (Numerators × Numerators, Denominators × Denominators)</h3>
    <p>To multiply two fractions, multiply the numerators together to get the new numerator, and multiply the denominators together to get the new denominator.</p>
    <p>$$\\frac{a}{b} \\times \\frac{c}{d} = \\frac{a \\times c}{b \\times d}$$</p>
  </div>

  <div class="steps-container">
    <h3>Method: Multiplying Two Fractions</h3>
    <div class="step">
      <h4>Step 1: Multiply the numerators</h4>
      <p>For \\(\\frac{2}{3} \\times \\frac{5}{7}\\): \\(2 \\times 5 = 10\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Multiply the denominators</h4>
      <p>\\(3 \\times 7 = 21\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Write the result</h4>
      <p>$$\\frac{2}{3} \\times \\frac{5}{7} = \\frac{10}{21}$$</p>
    </div>
    <div class="step">
      <h4>Step 4: Simplify if possible</h4>
      <p>\\(\\frac{10}{21}\\) has no common factors, so it is already in lowest terms.</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>More Examples:</h4>
    <p><strong>Example 1:</strong> \\(\\frac{3}{4} \\times \\frac{2}{5}\\)</p>
    <p>Numerators: \\(3 \\times 2 = 6\\)</p>
    <p>Denominators: \\(4 \\times 5 = 20\\)</p>
    <p>Result: \\(\\frac{6}{20} = \\frac{3}{10}\\) (simplified)</p>

    <p><strong>Example 2:</strong> \\(\\frac{5}{6} \\times \\frac{3}{4}\\)</p>
    <p>\\(\\frac{5 \\times 3}{6 \\times 4} = \\frac{15}{24} = \\frac{5}{8}\\)</p>
  </div>

  <div class="formula-box">
    <h4>Remember:</h4>
    <p>Always simplify at the end by finding the GCF of numerator and denominator!</p>
  </div>
</div>"""
    },
    {
        "title": "Multiplying Fractions by Whole Numbers",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Whole Numbers Are Fractions Too!</h3>
    <p>Any whole number can be written as a fraction with denominator 1. So \\(3 = \\frac{3}{1}\\), and \\(7 = \\frac{7}{1}\\).</p>
    <p>This means we can multiply fractions by whole numbers using the exact same rule!</p>
  </div>

  <div class="steps-container">
    <h3>Method: Fraction × Whole Number</h3>
    <div class="step">
      <h4>Step 1: Rewrite the whole number as a fraction</h4>
      <p>\\(3 \\times \\frac{2}{5} = \\frac{3}{1} \\times \\frac{2}{5}\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Multiply numerators and denominators</h4>
      <p>$$\\frac{3 \\times 2}{1 \\times 5} = \\frac{6}{5}$$</p>
    </div>
    <div class="step">
      <h4>Step 3: Convert to mixed number if needed</h4>
      <p>\\(\\frac{6}{5} = 1\\frac{1}{5}\\)</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg">
      <text x="50" y="30" font-size='16' font-weight='bold'>Visual: \\(3 \\times \\frac{2}{5}\\)</text>

      <rect x="50" y="50" width="40" height="40" fill='#4169E1' opacity='0.6' stroke='#8b949e' stroke-width="1"/>
      <line x1="70" y1="50" x2="70" y2="90" stroke='#8b949e' stroke-width="1"/>
      <text x="60" y="75" font-size='12' text-anchor='middle'>2 fifths</text>

      <rect x="100" y="50" width="40" height="40" fill='#4169E1' opacity='0.6' stroke='#8b949e' stroke-width="1"/>
      <line x1="120" y1="50" x2="120" y2="90" stroke='#8b949e' stroke-width="1"/>

      <rect x="150" y="50" width="40" height="40" fill='#4169E1' opacity='0.6' stroke='#8b949e' stroke-width="1"/>
      <line x1="170" y1="50" x2="170" y2="90" stroke='#8b949e' stroke-width="1"/>

      <text x="120" y="130" font-size='14' font-weight='bold'>= 6 fifths = \\(\\frac{6}{5} = 1\\frac{1}{5}\\)</text>

      <text x="50" y="170" font-size='13'>Three times two-fifths = six-fifths</text>
    </svg>
  </div>

  <div class="worked-example">
    <h4>Examples:</h4>
    <p><strong>Example 1:</strong> \\(2 \\times \\frac{3}{4}\\)</p>
    <p>$$\\frac{2}{1} \\times \\frac{3}{4} = \\frac{6}{4} = \\frac{3}{2} = 1\\frac{1}{2}\\)</p>

    <p><strong>Example 2:</strong> \\(5 \\times \\frac{1}{3}\\)</p>
    <p>$$\\frac{5}{1} \\times \\frac{1}{3} = \\frac{5}{3} = 1\\frac{2}{3}\\)</p>
  </div>
</div>"""
    },
    {
        "title": "Simplifying Before You Multiply (Cross-Cancelling)",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Make Your Work Easier First!</h3>
    <p>Before multiplying, look for common factors between any numerator and any denominator. You can cancel (divide out) these common factors <strong>before</strong> multiplying. This makes the numbers smaller and the work easier!</p>
    <p>This is called <strong>cross-cancelling</strong> or <strong>simplifying before multiplying</strong>.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Cross-Cancelling</h3>
    <div class="step">
      <h4>Step 1: Look for common factors</h4>
      <p>\\(\\frac{2}{5} \\times \\frac{5}{8}\\) has a 5 in both a numerator and denominator!</p>
    </div>
    <div class="step">
      <h4>Step 2: Cancel (divide) the common factors</h4>
      <p>$$\\frac{2}{\\cancel{5}} \\times \\frac{\\cancel{5}}{8} = \\frac{2}{8}$$</p>
    </div>
    <div class="step">
      <h4>Step 3: Multiply what's left</h4>
      <p>$$\\frac{2}{8} = \\frac{1}{4}$$</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>Example with Bigger Numbers:</h4>
    <p><strong>Problem:</strong> \\(\\frac{6}{7} \\times \\frac{14}{9}\\)</p>
    <p>Look for common factors:</p>
    <p>• 6 and 9 share a factor of 3: \\(\\frac{6}{9}\\) simplifies to \\(\\frac{2}{3}\\)</p>
    <p>• 7 and 14 share a factor of 7: \\(\\frac{7}{14}\\) simplifies to \\(\\frac{1}{2}\\)</p>
    <p>$$\\frac{6}{7} \\times \\frac{14}{9} = \\frac{\\cancel{6}2}{\\cancel{7}1} \\times \\frac{\\cancel{14}2}{\\cancel{9}3} = \\frac{2 \\times 2}{1 \\times 3} = \\frac{4}{3} = 1\\frac{1}{3}\\)</p>
  </div>

  <div class="success-box">
    <h4>Pro Tip:</h4>
    <p>Always simplify before multiplying! It saves time and reduces errors. Smaller numbers are easier to work with.</p>
  </div>
</div>"""
    }
]
