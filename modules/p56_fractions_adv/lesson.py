SECTIONS = [
    {
        "id": "1_fraction_parts",
        "title": "Understanding Fractions from First Principles",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>What is a Fraction?</h3>
    <p>A fraction represents <strong>equal parts of a whole</strong>. When we write \\\\( \\\frac{3}{4} \\\\), we are saying:</p>
    <ul>
      <li><strong>3</strong> = how many parts we have (numerator)</li>
      <li><strong>4</strong> = how many equal parts the whole is divided into (denominator)</li>
    </ul>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 430 160" xmlns="http://www.w3.org/2000/svg">
      <rect x="65" y="25" width="300" height="80" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="140" y1="25" x2="140" y2="105" stroke="#30363d" stroke-width="1"/>
      <line x1="215" y1="25" x2="215" y2="105" stroke="#30363d" stroke-width="1"/>
      <line x1="290" y1="25" x2="290" y2="105" stroke="#30363d" stroke-width="1"/>
      <rect x="65" y="25" width="75" height="80" fill="#4169E1" opacity="0.6" rx="4"/>
      <rect x="140" y="25" width="75" height="80" fill="#4169E1" opacity="0.6"/>
      <rect x="215" y="25" width="75" height="80" fill="#4169E1" opacity="0.6"/>
      <text x="215" y="145" font-size="22" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">3/4</text>
      <text x="102" y="70" font-size="16" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">1</text>
      <text x="177" y="70" font-size="16" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">2</text>
      <text x="252" y="70" font-size="16" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">3</text>
      <text x="327" y="70" font-size="16" text-anchor="middle" fill="currentColor" font-weight="bold" font-family="sans-serif">4</text>
    </svg>
  </div>

  <p><strong>Why this matters:</strong> Fractions describe parts of things—recipes, time, money, sharing fairly. Understanding what the top and bottom numbers mean is the foundation for all fraction work.</p>
</div>'''
    },
    {
        "id": "2_equivalent_fractions",
        "title": "Equivalent Fractions: The Same Amount, Different Names",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>What Are Equivalent Fractions?</h3>
    <p>Equivalent fractions represent the same amount but use different numerators and denominators.</p>
    <p><strong>The Golden Rule:</strong> If we multiply (or divide) BOTH the numerator and denominator by the same number, we get an equivalent fraction.</p>
    <p>$$ \\\frac{a}{b} = \\\frac{a \\\times k}{b \\\times k} $$</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 530 180" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="#30363d"/>
        </marker>
      </defs>

      <rect x="25" y="25" width="200" height="60" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="125" y1="25" x2="125" y2="85" stroke="#30363d" stroke-width="1"/>
      <rect x="25" y="25" width="100" height="60" fill="#4169E1" opacity="0.6" rx="4"/>
      <text x="125" y="115" font-size="18" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">1/2</text>

      <path d="M 240 55 L 280 55" fill="none" stroke="#30363d" stroke-width="2" marker-end="url(#arrowhead)"/>
      <text x="260" y="45" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">x 2</text>

      <rect x="300" y="25" width="200" height="60" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="350" y1="25" x2="350" y2="85" stroke="#30363d" stroke-width="1"/>
      <line x1="400" y1="25" x2="400" y2="85" stroke="#30363d" stroke-width="1"/>
      <line x1="450" y1="25" x2="450" y2="85" stroke="#30363d" stroke-width="1"/>
      <rect x="300" y="25" width="100" height="60" fill="#4169E1" opacity="0.6" rx="4"/>
      <text x="400" y="115" font-size="18" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">2/4</text>

      <text x="265" y="155" font-size="16" font-weight="bold" text-anchor="middle" fill="currentColor" font-family="sans-serif">Same amount, different names</text>
    </svg>
  </div>

  <div class="formula-box">
    <h4>Key Concept: Multiplying the numerator and denominator by the same number doesn't change the value.</h4>
    <p>This is because we are multiplying by \\\\( \\\frac{k}{k} \\\\), which equals 1!</p>
  </div>
</div>'''
    },
    {
        "id": "3_simplifying_fractions",
        "title": "Simplifying Fractions to Lowest Terms",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>What Does Simplifying Mean?</h3>
    <p>A fraction is in <strong>simplest form</strong> (or lowest terms) when the numerator and denominator have no common factors except 1.</p>
    <p>We simplify by dividing both by their <strong>Greatest Common Factor (GCF)</strong>.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Finding the GCF</h3>
    <div class="step">
      <h4>Step 1: List the factors</h4>
      <p>For \\\\( \\\frac{12}{18} \\\\):</p>
      <p>Factors of 12: 1, 2, 3, 4, 6, 12</p>
      <p>Factors of 18: 1, 2, 3, 6, 9, 18</p>
    </div>
    <div class="step">
      <h4>Step 2: Find common factors</h4>
      <p>Common factors: 1, 2, 3, 6</p>
      <p>Greatest Common Factor: <strong>6</strong></p>
    </div>
    <div class="step">
      <h4>Step 3: Divide both by the GCF</h4>
      <p>$$ \\\frac{12}{18} = \\\frac{12 \\\\div 6}{18 \\\\div 6} = \\\frac{2}{3} $$</p>
    </div>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 430 150" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowhead2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="#30363d"/>
        </marker>
      </defs>

      <rect x="15" y="20" width="162" height="80" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="33" y1="20" x2="33" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="51" y1="20" x2="51" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="69" y1="20" x2="69" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="87" y1="20" x2="87" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="105" y1="20" x2="105" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="123" y1="20" x2="123" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="141" y1="20" x2="141" y2="100" stroke="#999" stroke-width="1"/>
      <line x1="159" y1="20" x2="159" y2="100" stroke="#999" stroke-width="1"/>

      <rect x="15" y="20" width="120" height="80" fill="#ef4444" opacity="0.5" rx="4"/>
      <text x="96" y="130" font-size="18" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">12/18</text>

      <path d="M 195 60 L 230 60" stroke="#30363d" stroke-width="2" marker-end="url(#arrowhead2)"/>
      <text x="212" y="48" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">÷ 6</text>

      <rect x="250" y="20" width="162" height="80" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="304" y1="20" x2="304" y2="100" stroke="#30363d" stroke-width="1"/>
      <line x1="358" y1="20" x2="358" y2="100" stroke="#30363d" stroke-width="1"/>

      <rect x="250" y="20" width="108" height="80" fill="#22c55e" opacity="0.5" rx="4"/>
      <text x="331" y="130" font-size="18" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">2/3</text>
    </svg>
  </div>

  <div class="example-box">
    <h4>Example:</h4>
    <p>Simplify \\\\( \\\frac{15}{25} \\\\)</p>
    <p>Factors of 15: 1, 3, 5, 15</p>
    <p>Factors of 25: 1, 5, 25</p>
    <p>GCF = 5</p>
    <p>$$ \\\frac{15}{25} = \\\frac{15 \\\\div 5}{25 \\\\div 5} = \\\frac{3}{5} $$</p>
  </div>
</div>'''
    },
    {
        "id": "4_adding_subtracting_fractions",
        "title": "Adding and Subtracting Fractions",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Why We Need Common Denominators</h3>
    <p>You can only add or subtract fractions if they represent the <strong>same size pieces</strong>.</p>
    <p>Imagine trying to add \\\\( \\\frac{1}{2} \\\\) pizza slice to \\\\( \\\frac{1}{4} \\\\) pizza slice directly—the pieces are different sizes!</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 530 200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowhead3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <polygon points="0 0, 10 3, 0 6" fill="#30363d"/>
        </marker>
      </defs>

      <text x="15" y="25" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">Different denominators:</text>

      <rect x="15" y="40" width="120" height="50" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="75" y1="40" x2="75" y2="90" stroke="#30363d" stroke-width="1"/>
      <rect x="15" y="40" width="60" height="50" fill="#4169E1" opacity="0.6" rx="4"/>
      <text x="75" y="115" font-size="16" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">1/2</text>

      <text x="155" y="72" font-size="24" font-weight="bold" fill="currentColor" font-family="sans-serif">+</text>

      <rect x="180" y="40" width="120" height="50" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="210" y1="40" x2="210" y2="90" stroke="#30363d" stroke-width="1"/>
      <line x1="240" y1="40" x2="240" y2="90" stroke="#30363d" stroke-width="1"/>
      <line x1="270" y1="40" x2="270" y2="90" stroke="#30363d" stroke-width="1"/>
      <rect x="180" y="40" width="30" height="50" fill="#22c55e" opacity="0.6" rx="4"/>
      <text x="240" y="115" font-size="16" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">1/4</text>

      <path d="M 320 70 L 355 70" fill="none" stroke="#30363d" stroke-width="2" marker-end="url(#arrowhead3)"/>
      <text x="337" y="58" font-size="12" text-anchor="middle" fill="currentColor" font-family="sans-serif">Convert</text>

      <text x="375" y="25" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">Same denominator:</text>

      <rect x="375" y="40" width="140" height="50" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="410" y1="40" x2="410" y2="90" stroke="#30363d" stroke-width="1"/>
      <line x1="445" y1="40" x2="445" y2="90" stroke="#30363d" stroke-width="1"/>
      <line x1="480" y1="40" x2="480" y2="90" stroke="#30363d" stroke-width="1"/>
      <rect x="375" y="40" width="70" height="50" fill="#4169E1" opacity="0.6" rx="4"/>
      <rect x="445" y="40" width="35" height="50" fill="#22c55e" opacity="0.6"/>
      <text x="445" y="115" font-size="16" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="serif">2/4 + 1/4 = 3/4</text>

      <text x="265" y="170" font-size="16" font-weight="bold" text-anchor="middle" fill="currentColor" font-family="sans-serif">Convert to the same denominator, then add numerators</text>
    </svg>
  </div>

  <div class="steps-container">
    <h3>Method: Adding Fractions</h3>
    <div class="step">
      <h4>Step 1: Find a Common Denominator</h4>
      <p>For \\\\( \\\frac{1}{2} + \\\frac{1}{4} \\\\), the LCD (Least Common Denominator) is 4.</p>
    </div>
    <div class="step">
      <h4>Step 2: Convert to Equivalent Fractions</h4>
      <p>\\\\( \\\frac{1}{2} = \\\frac{2}{4} \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Add the Numerators</h4>
      <p>$$ \\\frac{2}{4} + \\\frac{1}{4} = \\\frac{2+1}{4} = \\\frac{3}{4} $$</p>
    </div>
    <div class="step">
      <h4>Step 4: Simplify if Needed</h4>
      <p>\\\\( \\\frac{3}{4} \\\\) is already in lowest terms.</p>
    </div>
  </div>

  <div class="example-box">
    <h4>More Examples:</h4>
    <p>$$ \\\frac{2}{5} + \\\frac{3}{10} = \\\frac{4}{10} + \\\frac{3}{10} = \\\frac{7}{10} $$</p>
    <p>$$ \\\frac{3}{4} - \\\frac{1}{6} = \\\frac{9}{12} - \\\frac{2}{12} = \\\frac{7}{12} $$</p>
  </div>
</div>'''
    },
    {
        "id": "5_multiplying_fractions",
        "title": "Multiplying Fractions: Whole and Partial",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Understanding Fraction Multiplication</h3>
    <p>When we multiply fractions, we are finding "a fraction OF another fraction."</p>
    <p><strong>Key insight:</strong> \\\\( \\\frac{1}{2} \\\times \\\frac{3}{4} \\\\) means "1 half of 3 fourths."</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 460 280" xmlns="http://www.w3.org/2000/svg">
      <text x="25" y="25" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">Start with 3/4:</text>
      <rect x="25" y="45" width="240" height="60" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="85" y1="45" x2="85" y2="105" stroke="#30363d" stroke-width="1"/>
      <line x1="145" y1="45" x2="145" y2="105" stroke="#30363d" stroke-width="1"/>
      <line x1="205" y1="45" x2="205" y2="105" stroke="#30363d" stroke-width="1"/>
      <rect x="25" y="45" width="180" height="60" fill="#4169E1" opacity="0.6" rx="4"/>

      <text x="25" y="145" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">Take 1/2 of that:</text>
      <rect x="25" y="160" width="240" height="60" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="85" y1="160" x2="85" y2="220" stroke="#30363d" stroke-width="1"/>
      <line x1="145" y1="160" x2="145" y2="220" stroke="#30363d" stroke-width="1"/>
      <line x1="205" y1="160" x2="205" y2="220" stroke="#30363d" stroke-width="1"/>
      <line x1="115" y1="160" x2="115" y2="220" stroke="#22c55e" stroke-width="2" stroke-dasharray="4,2"/>
      <rect x="25" y="160" width="90" height="60" fill="#f59e0b" opacity="0.8" rx="4"/>

      <text x="300" y="140" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">1/2 x 3/4</text>
      <text x="300" y="168" font-size="16" fill="currentColor" font-family="sans-serif">= (1x3) / (2x4)</text>
      <text x="300" y="196" font-size="20" font-weight="bold" fill="currentColor" font-family="serif">= 3/8</text>

      <text x="230" y="260" font-size="16" font-weight="bold" text-anchor="middle" fill="currentColor" font-family="sans-serif">Multiply numerators, multiply denominators</text>
    </svg>
  </div>

  <div class="formula-box">
    <h4>Multiplication Rule:</h4>
    <p>$$ \\\frac{a}{b} \\\times \\\frac{c}{d} = \\\frac{a \\\times c}{b \\\times d} $$</p>
    <p><strong>In words:</strong> Multiply the numerators together, multiply the denominators together.</p>
  </div>

  <div class="steps-container">
    <h3>Method: Multiplying Fractions</h3>
    <div class="step">
      <h4>Step 1: Multiply numerators</h4>
      <p>\\\\( \\\frac{2}{3} \\\times \\\frac{5}{7} \\\\) → numerators: \\\\( 2 \\\times 5 = 10 \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Multiply denominators</h4>
      <p>Denominators: \\\\( 3 \\\times 7 = 21 \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Write the result</h4>
      <p>$$ \\\frac{2}{3} \\\times \\\frac{5}{7} = \\\frac{10}{21} $$</p>
    </div>
    <div class="step">
      <h4>Step 4: Simplify if possible</h4>
      <p>\\\\( \\\frac{10}{21} \\\\) has no common factors, so it is done.</p>
    </div>
  </div>

  <div class="example-box">
    <h4>Multiplying by Whole Numbers:</h4>
    <p>A whole number can be written as a fraction: \\\\( 3 = \\\frac{3}{1} \\\\)</p>
    <p>$$ 3 \\\times \\\frac{2}{5} = \\\frac{3}{1} \\\times \\\frac{2}{5} = \\\frac{6}{5} = 1\\\frac{1}{5} $$</p>
  </div>
</div>'''
    },
    {
        "id": "6_dividing_fractions",
        "title": "Dividing Fractions: The Invert and Multiply Method",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>What Does Dividing by a Fraction Mean?</h3>
    <p>\\\\( \\\frac{3}{4} \\\\div \\\frac{1}{2} \\\\) asks: <strong>"How many halves fit into 3 fourths?"</strong></p>
    <p>Or: <strong>"How many \\\\( \\\frac{1}{2} \\\\)s are in \\\\( \\\frac{3}{4} \\\\)?"</strong></p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 500 210" xmlns="http://www.w3.org/2000/svg">
      <text x="15" y="25" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">We have 3/4:</text>
      <rect x="15" y="40" width="200" height="50" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="65" y1="40" x2="65" y2="90" stroke="#30363d" stroke-width="1"/>
      <line x1="115" y1="40" x2="115" y2="90" stroke="#30363d" stroke-width="1"/>
      <line x1="165" y1="40" x2="165" y2="90" stroke="#30363d" stroke-width="1"/>
      <rect x="15" y="40" width="150" height="50" fill="#4169E1" opacity="0.6" rx="4"/>
      <text x="90" y="72" font-size="14" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">3/4</text>

      <text x="260" y="25" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">Each half looks like:</text>
      <rect x="260" y="40" width="200" height="50" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="360" y1="40" x2="360" y2="90" stroke="#30363d" stroke-width="1"/>
      <rect x="260" y="40" width="100" height="50" fill="#22c55e" opacity="0.6" rx="4"/>
      <text x="310" y="72" font-size="14" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">1/2</text>

      <text x="250" y="130" font-size="16" font-weight="bold" text-anchor="middle" fill="currentColor" font-family="sans-serif">How many halves fit into 3/4?</text>

      <rect x="75" y="150" width="200" height="40" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="175" y1="150" x2="175" y2="190" stroke="#30363d" stroke-width="1"/>
      <rect x="75" y="150" width="100" height="40" fill="#22c55e" opacity="0.5" rx="4"/>
      <rect x="175" y="150" width="50" height="40" fill="#22c55e" opacity="0.3"/>
      <text x="175" y="140" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">1 full half + half a half</text>

      <text x="350" y="175" font-size="20" font-weight="bold" fill="currentColor" font-family="serif">= 3/2 = 1 1/2</text>
    </svg>
  </div>

  <div class="formula-box">
    <h4>The Invert and Multiply Rule:</h4>
    <p>$$ \\\frac{a}{b} \\\\div \\\frac{c}{d} = \\\frac{a}{b} \\\times \\\frac{d}{c} $$</p>
    <p><strong>Steps:</strong></p>
    <ol>
      <li>Keep the first fraction as is</li>
      <li>Change ÷ to ×</li>
      <li>Flip the second fraction (invert it)</li>
      <li>Multiply as normal</li>
    </ol>
  </div>

  <div class="steps-container">
    <h3>Method: Dividing Fractions</h3>
    <div class="step">
      <h4>Example: \\\\( \\\frac{2}{3} \\\\div \\\frac{5}{7} \\\\)</h4>
    </div>
    <div class="step">
      <h4>Step 1: Keep the first fraction</h4>
      <p>\\\\( \\\frac{2}{3} \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Invert the second fraction</h4>
      <p>\\\\( \\\frac{5}{7} \\\\) becomes \\\\( \\\frac{7}{5} \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Multiply</h4>
      <p>$$ \\\frac{2}{3} \\\times \\\frac{7}{5} = \\\frac{14}{15} $$</p>
    </div>
  </div>

  <div class="warning-box">
    <h4>Why Does Invert and Multiply Work?</h4>
    <p>Division is the opposite of multiplication. When we invert (flip) the fraction, we are finding the reciprocal—the number that, when multiplied by the original, gives 1.</p>
    <p>\\\\( \\\frac{2}{3} \\\times \\\frac{3}{2} = 1 \\\\)</p>
  </div>

  <div class="example-box">
    <h4>Dividing by a Whole Number:</h4>
    <p>$$ \\\frac{4}{5} \\\\div 2 = \\\frac{4}{5} \\\\div \\\frac{2}{1} = \\\frac{4}{5} \\\times \\\frac{1}{2} = \\\frac{4}{10} = \\\frac{2}{5} $$</p>
  </div>
</div>'''
    },
    {
        "id": "7_mixed_numbers",
        "title": "Mixed Numbers and Improper Fractions",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>Two Ways to Write the Same Amount</h3>
    <p><strong>Improper Fraction:</strong> The numerator is greater than or equal to the denominator.</p>
    <p><strong>Mixed Number:</strong> A whole number and a fraction together.</p>
    <p>Example: \\\\( \\\frac{7}{3} = 2\\\frac{1}{3} \\\\) (they represent the same amount!)</p>
  </div>

  <div class="diagram-container">
    <svg viewBox="0 0 460 200" xmlns="http://www.w3.org/2000/svg">
      <text x="15" y="25" font-size="16" font-weight="bold" fill="currentColor" font-family="sans-serif">7/3 shown as wholes and parts:</text>

      <rect x="15" y="50" width="90" height="60" fill="#4169E1" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="45" y1="50" x2="45" y2="110" stroke="#30363d" stroke-width="1"/>
      <line x1="75" y1="50" x2="75" y2="110" stroke="#30363d" stroke-width="1"/>
      <text x="60" y="85" font-size="14" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">3/3</text>
      <text x="60" y="135" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">1 whole</text>

      <text x="120" y="85" font-size="20" font-weight="bold" fill="currentColor" font-family="sans-serif">+</text>

      <rect x="145" y="50" width="90" height="60" fill="#4169E1" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="175" y1="50" x2="175" y2="110" stroke="#30363d" stroke-width="1"/>
      <line x1="205" y1="50" x2="205" y2="110" stroke="#30363d" stroke-width="1"/>
      <text x="190" y="85" font-size="14" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">3/3</text>
      <text x="190" y="135" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">1 whole</text>

      <text x="250" y="85" font-size="20" font-weight="bold" fill="currentColor" font-family="sans-serif">+</text>

      <rect x="275" y="50" width="90" height="60" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
      <line x1="305" y1="50" x2="305" y2="110" stroke="#30363d" stroke-width="1"/>
      <line x1="335" y1="50" x2="335" y2="110" stroke="#30363d" stroke-width="1"/>
      <rect x="275" y="50" width="30" height="60" fill="#22c55e" opacity="0.6" rx="4"/>
      <text x="320" y="85" font-size="14" text-anchor="middle" fill="currentColor" font-weight="bold" font-family="sans-serif">1/3</text>
      <text x="320" y="135" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">part</text>

      <text x="230" y="175" font-size="20" font-weight="bold" text-anchor="middle" fill="currentColor" font-family="serif">7/3 = 2 1/3</text>
    </svg>
  </div>

  <div class="steps-container">
    <h3>Method: Convert Improper Fraction to Mixed Number</h3>
    <div class="step">
      <h4>Step 1: Divide numerator by denominator</h4>
      <p>\\\\( \\\frac{11}{4} \\\\): Divide \\\\( 11 \\\\div 4 = 2 \\\\) remainder \\\\( 3 \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Write as mixed number</h4>
      <p>Whole part = 2, numerator = remainder = 3, denominator = 4</p>
      <p>Result: \\\\( 2\\\frac{3}{4} \\\\)</p>
    </div>
  </div>

  <div class="steps-container">
    <h3>Method: Convert Mixed Number to Improper Fraction</h3>
    <div class="step">
      <h4>Step 1: Multiply whole by denominator</h4>
      <p>\\\\( 3\\\frac{2}{5} \\\\): \\\\( 3 \\\times 5 = 15 \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 2: Add the numerator</h4>
      <p>\\\\( 15 + 2 = 17 \\\\)</p>
    </div>
    <div class="step">
      <h4>Step 3: Use same denominator</h4>
      <p>Result: \\\\( \\\frac{17}{5} \\\\)</p>
    </div>
  </div>

  <div class="success-box">
    <h4>Why This Matters:</h4>
    <p>Mixed numbers are easier to read (\\\\( 2\\\frac{1}{3} \\\\) "two and one third"). But improper fractions are easier for calculations.</p>
    <p>Many problems ask you to convert between them!</p>
  </div>
</div>'''
    },
    {
        "id": "8_fraction_word_problems",
        "title": "Solving Real-World Fraction Problems",
        "content": '''<div class="lesson-container">
  <div class="concept-box">
    <h3>The Bar Model Strategy</h3>
    <p>The <strong>bar model</strong> is a visual tool used in Singapore Math to break down word problems.</p>
    <p>It helps you:</p>
    <ul>
      <li>See what you know and what you need to find</li>
      <li>Choose the right operation</li>
      <li>Check if your answer makes sense</li>
    </ul>
  </div>

  <div class="example-box">
    <h4>Problem 1: Finding a Fraction of a Whole</h4>
    <p><strong>Question:</strong> Sarah has 20 apples. She gives away \\\\( \\\frac{3}{5} \\\\) of them. How many apples does she give away?</p>

    <div class="diagram-container">
      <svg viewBox="0 0 500 160" xmlns="http://www.w3.org/2000/svg">
        <text x="30" y="25" font-size="14" font-weight="bold" fill="currentColor" font-family="sans-serif">Total apples (20):</text>
        <rect x="30" y="35" width="400" height="40" fill="none" stroke="#30363d" stroke-width="2" rx="4"/>
        <line x1="110" y1="35" x2="110" y2="75" stroke="#30363d" stroke-width="1"/>
        <line x1="190" y1="35" x2="190" y2="75" stroke="#30363d" stroke-width="1"/>
        <line x1="270" y1="35" x2="270" y2="75" stroke="#30363d" stroke-width="1"/>
        <line x1="350" y1="35" x2="350" y2="75" stroke="#30363d" stroke-width="1"/>

        <rect x="30" y="35" width="240" height="40" fill="#4169E1" opacity="0.5" rx="4"/>

        <text x="70" y="60" font-size="11" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">4</text>
        <text x="150" y="60" font-size="11" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">4</text>
        <text x="230" y="60" font-size="11" text-anchor="middle" fill="white" font-weight="bold" font-family="sans-serif">4</text>
        <text x="310" y="60" font-size="11" text-anchor="middle" fill="currentColor" font-weight="bold" font-family="sans-serif">4</text>
        <text x="390" y="60" font-size="11" text-anchor="middle" fill="currentColor" font-weight="bold" font-family="sans-serif">4</text>

        <text x="150" y="100" font-size="14" text-anchor="middle" font-weight="bold" fill="currentColor" font-family="sans-serif">3/5 of 20 = ?</text>

        <text x="250" y="140" font-size="14" text-anchor="middle" fill="currentColor" font-family="sans-serif">Solution: 3/5 x 20 = (3 x 20) / 5 = 60 / 5 = 12 apples</text>
      </svg>
    </div>
  </div>

  <div class="example-box">
    <h4>Problem 2: Combining Fractions</h4>
    <p><strong>Question:</strong> A recipe uses \\\\( \\\frac{2}{3} \\\\) cup of sugar and \\\\( \\\frac{1}{4} \\\\) cup of honey. How much sweetener total?</p>

    <div class="diagram-container">
      <svg viewBox="0 0 500 160" xmlns="http://www.w3.org/2000/svg">
        <text x="30" y="25" font-size="14" font-weight="bold" fill="currentColor" font-family="sans-serif">Sugar: 2/3 cup</text>
        <rect x="30" y="35" width="180" height="30" fill="#f59e0b" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>

        <text x="30" y="90" font-size="14" font-weight="bold" fill="currentColor" font-family="sans-serif">Honey: 1/4 cup</text>
        <rect x="30" y="100" width="135" height="30" fill="#22c55e" opacity="0.6" stroke="#30363d" stroke-width="2" rx="4"/>

        <text x="350" y="60" font-size="14" fill="currentColor" font-family="sans-serif">2/3 + 1/4</text>
        <text x="350" y="85" font-size="14" fill="currentColor" font-family="sans-serif">= 8/12 + 3/12</text>
        <text x="350" y="110" font-size="16" font-weight="bold" fill="currentColor" font-family="serif">= 11/12 cup total</text>
      </svg>
    </div>
  </div>

  <div class="steps-container">
    <h3>Strategy: Solving Fraction Word Problems</h3>
    <div class="step">
      <h4>Step 1: Read carefully</h4>
      <p>Identify what you know and what you need to find.</p>
    </div>
    <div class="step">
      <h4>Step 2: Draw a bar model</h4>
      <p>Represent the total as a bar divided into equal parts.</p>
    </div>
    <div class="step">
      <h4>Step 3: Write the operation</h4>
      <p>Decide whether you need to add, subtract, multiply, or divide.</p>
    </div>
    <div class="step">
      <h4>Step 4: Solve</h4>
      <p>Perform the calculation.</p>
    </div>
    <div class="step">
      <h4>Step 5: Check your answer</h4>
      <p>Does it make sense? Is the answer reasonable?</p>
    </div>
  </div>

  <div class="warning-box">
    <h4>Key Phrases and Operations:</h4>
    <ul>
      <li><strong>"of"</strong> usually means multiply: "\\\\( \\\frac{1}{2} \\\\) of 10" → \\\\( \\\frac{1}{2} \\\times 10 \\\\)</li>
      <li><strong>"How many... left"</strong> means subtract: "Start with 20, give away \\\\( \\\frac{3}{4} \\\\)" → \\\\( 20 - \\\frac{3}{4} \\\times 20 \\\\)</li>
      <li><strong>"How many times"</strong> means divide: "\\\\( 5 \\\\) divided into \\\\( \\\frac{1}{4} \\\\) portions" → \\\\( 5 \\\\div \\\frac{1}{4} \\\\)</li>
    </ul>
  </div>
</div>'''
    }
]
