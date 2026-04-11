TITLE = "Dividing Fractions"

SECTIONS = [
    {
        "title": "Understanding Fraction Division from First Principles",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Division Asks a Different Question</h3>
    <p>You already know fractions represent parts of a whole. And dividing by a fraction? That's asking <strong>"How many halves fit in 3?"</strong>—which gives something <strong>BIGGER</strong> than what you started with!</p>
    <p>This is the opposite of multiplication. Division asks: "How many of these pieces do I need?"</p>
    <p><strong>Example:</strong> \\(\\frac{3}{4} \\div \\frac{1}{2}\\) means "How many halves fit into 3 fourths?"</p>
  </div>

  <p style="text-align:center; font-weight:bold; margin:10px 0;">We have \\(\\frac{3}{4}\\). How many halves fit in it?</p>
  <div class="diagram-container">
    <svg viewBox="0 0 400 140" xmlns="http://www.w3.org/2000/svg" style="width:100%; max-width:400px; display:block; margin:0 auto;">
      <!-- 3/4 bar -->
      <rect x="40" y="10" width="200" height="40" fill='none' stroke='#8b949e' stroke-width="2"/>
      <line x1="90" y1="10" x2="90" y2="50" stroke='#8b949e' stroke-width="1"/>
      <line x1="140" y1="10" x2="140" y2="50" stroke='#8b949e' stroke-width="1"/>
      <line x1="190" y1="10" x2="190" y2="50" stroke='#8b949e' stroke-width="1"/>
      <rect x="40" y="10" width="150" height="40" fill='#4169E1' opacity='0.5'/>
      <text x="260" y="35" font-size='13' fill='currentColor'>← 3/4 shaded</text>

      <!-- Show halves fitting in -->
      <rect x="40" y="65" width="100" height="35" fill='#4169E1' opacity='0.5' stroke='#8b949e' stroke-width="2"/>
      <text x="90" y="88" font-size='11' text-anchor='middle' fill='currentColor'>1st half</text>

      <rect x="140" y="65" width="50" height="35" fill='#22c55e' opacity='0.5' stroke='#8b949e' stroke-width="2"/>
      <text x="165" y="88" font-size='11' text-anchor='middle' fill='currentColor'>1/2 of a half</text>

      <text x="200" y="125" font-size='14' text-anchor='middle' fill='currentColor' font-weight='bold'>Answer: 1 and 1/2 halves fit → 3/4 ÷ 1/2 = 3/2</text>
    </svg>
  </div>

  <div class="success-box">
    <h4>The Main Idea:</h4>
    <p>When you divide by a fraction, the answer is <strong>larger</strong> than the dividend (the number you started with). Division by a small number makes things bigger!</p>
  </div>
</div>"""
    },
    {
        "title": "The Keep-Change-Flip Method (Invert and Multiply)",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Dividing Is Really Just Multiplying in Disguise</h3>
    <p>To divide by a fraction, you don't actually divide. Instead, multiply by the <strong>reciprocal</strong> (the flipped version) of the fraction you're dividing by.</p>
    <p>$$\\frac{a}{b} \\div \\frac{c}{d} = \\frac{a}{b} \\times \\frac{d}{c}$$</p>
    <p><strong>The reciprocal:</strong> Flip the numerator and denominator. \\(\\frac{2}{3}\\) becomes \\(\\frac{3}{2}\\)</p>
  </div>

  <div class="steps-container">
    <h3>Method: Keep-Change-Flip</h3>
    <div class="step">
      <h4>Step 1: Keep the first fraction</h4>
      <p>\\(\\frac{3}{4} \\div \\frac{1}{2}\\) → Keep \\(\\frac{3}{4}\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Change ÷ to ×</h4>
      <p>\\(\\frac{3}{4} \\times \\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Flip the second fraction</h4>
      <p>\\(\\frac{1}{2}\\) becomes \\(\\frac{2}{1}\\)</p>
    </div>
    <div class="step">
      <h4>Step 4: Multiply as normal</h4>
      <p>$$\\frac{3}{4} \\times \\frac{2}{1} = \\frac{6}{4} = \\frac{3}{2} = 1\\frac{1}{2}$$</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>More Examples:</h4>
    <p><strong>Example 1:</strong> \\(\\frac{2}{3} \\div \\frac{5}{7}\\)</p>
    <p>Keep: \\(\\frac{2}{3}\\)</p>
    <p>Change: ÷ to ×</p>
    <p>Flip: \\(\\frac{5}{7}\\) to \\(\\frac{7}{5}\\)</p>
    <p>$$\\frac{2}{3} \\times \\frac{7}{5} = \\frac{14}{15}$$</p>

    <p><strong>Example 2:</strong> \\(\\frac{5}{8} \\div \\frac{3}{4}\\)</p>
    <p>$$\\frac{5}{8} \\times \\frac{4}{3} = \\frac{20}{24} = \\frac{5}{6}$$</p>
  </div>

  <div class="warning-box">
    <h4>Why Does This Work?</h4>
    <p>Division is the opposite of multiplication. The reciprocal is the "opposite" of a fraction—when you multiply a number by its reciprocal, you get 1. So \\(\\frac{2}{3} \\times \\frac{3}{2} = 1\\)</p>
  </div>
</div>"""
    },
    {
        "title": "Dividing Fractions by Whole Numbers and Vice Versa",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Whole Numbers Can Be Fractions Too</h3>
    <p>Any whole number can be written as a fraction: \\(3 = \\frac{3}{1}\\), \\(7 = \\frac{7}{1}\\)</p>
    <p>So you can divide fractions by whole numbers (or vice versa) using the same Keep-Change-Flip method!</p>
  </div>

  <div class="steps-container">
    <h3>Method: Fraction ÷ Whole Number</h3>
    <div class="step">
      <h4>Step 1: Write whole number as a fraction</h4>
      <p>\\(\\frac{4}{5} \\div 2 = \\frac{4}{5} \\div \\frac{2}{1}\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Apply Keep-Change-Flip</h4>
      <p>$$\\frac{4}{5} \\times \\frac{1}{2} = \\frac{4}{10} = \\frac{2}{5}$$</p>
    </div>
  </div>

  <div class="steps-container">
    <h3>Method: Whole Number ÷ Fraction</h3>
    <div class="step">
      <h4>Step 1: Write whole number as a fraction</h4>
      <p>\\(3 \\div \\frac{1}{4} = \\frac{3}{1} \\div \\frac{1}{4}\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Apply Keep-Change-Flip</h4>
      <p>$$\\frac{3}{1} \\times \\frac{4}{1} = \\frac{12}{1} = 12$$</p>
    </div>
  </div>

  <div class="worked-example">
    <h4>Examples:</h4>
    <p><strong>Example 1:</strong> \\(\\frac{3}{8} \\div 2\\)</p>
    <p>$$\\frac{3}{8} \\div \\frac{2}{1} = \\frac{3}{8} \\times \\frac{1}{2} = \\frac{3}{16}$$</p>

    <p><strong>Example 2:</strong> \\(5 \\div \\frac{1}{3}\\)</p>
    <p>$$\\frac{5}{1} \\div \\frac{1}{3} = \\frac{5}{1} \\times \\frac{3}{1} = \\frac{15}{1} = 15$$</p>
    <p>This makes sense: How many thirds fit in 5? Fifteen thirds!</p>
  </div>

  <div class="success-box">
    <h4>Pattern Recognition:</h4>
    <p>Dividing by a fraction always makes the answer <strong>bigger</strong>. Dividing by a whole number makes it <strong>smaller</strong>.</p>
  </div>
</div>"""
    },
    {
        "title": "Real-World Division: Splitting and Portioning",
        "body": """<div class="lesson-container">
  <div class="concept-box">
    <h3>Division Solves Portioning Problems</h3>
    <p>Division is useful when you want to split something into equal pieces or find how many portions you can make.</p>
    <p><strong>Example Problem:</strong> I have \\(\\frac{3}{4}\\) of a pizza. I want to split it equally among \\(\\frac{1}{2}\\) pizza portions. How many people can get a portion?</p>
  </div>

  <div class="worked-example">
    <h4>Ribbon Problem</h4>
    <p><strong>Problem:</strong> I have \\(\\frac{3}{4}\\) metre of ribbon. I need \\(\\frac{1}{8}\\) metre for each bookmark. How many bookmarks can I make?</p>
    <p><strong>Solution:</strong></p>
    <p>$$\\frac{3}{4} \\div \\frac{1}{8} = \\frac{3}{4} \\times \\frac{8}{1} = \\frac{24}{4} = 6$$</p>
    <p><strong>Answer: 6 bookmarks!</strong></p>
  </div>

  <div class="worked-example">
    <h4>More Real-World Examples:</h4>
    <p><strong>Example 1:</strong> A bottle holds \\(\\frac{2}{3}\\) litre. How many bottles can I fill from 4 litres of juice?</p>
    <p>$$4 \\div \\frac{2}{3} = \\frac{4}{1} \\times \\frac{3}{2} = \\frac{12}{2} = 6$$ bottles</p>

    <p><strong>Example 2:</strong> I have \\(\\frac{5}{6}\\) metre of fabric. Each dress needs \\(\\frac{1}{4}\\) metre. How many dresses can I make?</p>
    <p>$$\\frac{5}{6} \\div \\frac{1}{4} = \\frac{5}{6} \\times \\frac{4}{1} = \\frac{20}{6} = \\frac{10}{3} = 3\\frac{1}{3}$$ dresses (or 3 complete dresses)</p>
  </div>

  <div class="success-box">
    <h4>Key Insight:</h4>
    <p>When dividing fractions in real-world problems, the answer often tells you "how many groups" or "how many portions" you can make.</p>
  </div>
</div>"""
    }
]
