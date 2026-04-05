# Conditional Statements: if, elif, else

TITLE = "Conditional Statements: if, elif, else"

SECTIONS = [
    {
        'id': 'conditionals_01',
        'title': 'Boolean Conditions and Decision Points',
        'body': '''
<div class="worked-example">
<h3>Boolean Conditions and Decision Points</h3>
<p>At the heart of control flow are boolean conditions: expressions that evaluate to either <code class="formula-box" style="padding: 2px 6px;">True</code> or <code class="formula-box" style="padding: 2px 6px;">False</code>.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> A boolean condition determines which code block executes. Python evaluates the condition and takes one path or another.
</div>

<h4>Comparison Operators</h4>
<p>Comparisons create boolean values:</p>
<pre><code class="formula-box">x = 10
y = 5

x > y    # True (greater than)
x < y    # False (less than)
x == y   # False (equal)
x != y   # True (not equal)
x >= 10  # True (greater than or equal)
y <= 10  # True (less than or equal)</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Checking user eligibility for a discount
<pre><code class="code-block">age = 65
has_membership = True

age >= 60           # True (senior discount available)
has_membership      # True (membership discount available)</code></pre>
</div>
</div>
'''
    },
    {
        'id': 'conditionals_02',
        'title': 'The if Statement',
        'body': '''
<div class="worked-example">
<h3>The if Statement</h3>
<p>The simplest conditional: execute code only if a condition is True.</p>

<div class="concept-box formula-box">
<strong>Syntax:</strong>
<pre><code class="code-block">if condition:
    # Code executes only if condition is True
    statement1
    statement2</code></pre>
</div>

<h4>Indentation is Critical</h4>
<p>Python uses indentation to define code blocks. Code inside the if must be indented (typically 4 spaces).</p>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Check if user is old enough to vote
<pre><code class="code-block">age = 18

if age >= 18:
    print("You can vote!")
    print("Voting is a civic responsibility.")</code></pre>
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Common Mistake:</strong> Forgetting the colon after the condition. The colon <code style="padding: 2px 6px; border-radius: 4px">:</code> is required.
</div>
</div>
'''
    },
    {
        'id': 'conditionals_03',
        'title': 'if-else: Two Paths',
        'body': '''
<div class="worked-example">
<h3>if-else: Two Paths</h3>
<p>When you need to execute different code for True and False conditions, use else.</p>

<div class="concept-box formula-box">
<strong>Syntax:</strong>
<pre><code class="code-block">if condition:
    # Executes if True
    statement1
else:
    # Executes if False
    statement2</code></pre>
</div>

<h4>Mutually Exclusive Paths</h4>
<p>Exactly one branch executes. This creates a fork in program flow.</p>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Check test score and assign grade category
<pre><code class="code-block">score = 75

if score >= 70:
    print("You passed!")
else:
    print("You did not pass. Try again.")</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use if-else when there are exactly two possible outcomes you need to handle.
</div>
</div>
'''
    },
    {
        'id': 'conditionals_04',
        'title': 'if-elif-else: Multiple Conditions',
        'body': '''
<div class="worked-example">
<h3>if-elif-else: Multiple Conditions</h3>
<p>When you need to check multiple conditions in sequence, use elif (else if).</p>

<div class="concept-box formula-box">
<strong>Syntax:</strong>
<pre><code class="code-block">if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4</code></pre>
</div>

<h4>Execution Order</h4>
<p>Conditions are checked from top to bottom. Once a condition is True, its block executes and the rest are skipped.</p>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Classify student performance
<pre><code class="code-block">score = 82

if score >= 90:
    grade = "A"
    print("Excellent work!")
elif score >= 80:
    grade = "B"
    print("Good job!")
elif score >= 70:
    grade = "C"
    print("Satisfactory.")
else:
    grade = "F"
    print("You need to study harder.")</code></pre>
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Important:</strong> You can have multiple elif blocks, but else is optional and must come last.
</div>
</div>
'''
    }
]
