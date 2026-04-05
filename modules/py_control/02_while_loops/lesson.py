# While Loops: Condition-Based Iteration

TITLE = "While Loops: Condition-Based Iteration"

SECTIONS = [
    {
        'id': 'while_loops_01',
        'title': 'Repetition with while',
        'body': '''
<div class="worked-example">
<h3>Repetition with while</h3>
<p>A while loop repeats a block of code as long as a condition remains True.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> The condition is checked before each iteration. If it's True, the loop body executes. If it becomes False, the loop stops.
</div>

<h4>Syntax</h4>
<pre><code class="formula-box">while condition:
    # This code repeats while condition is True
    statement1
    statement2
# Code continues here when condition becomes False</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Countdown from 5 to 1
<pre><code class="code-block">count = 5

while count > 0:
    print(count)
    count = count - 1  # Decrement: must change condition!

print("Blastoff!")</code></pre>
Output: 5, 4, 3, 2, 1, Blastoff!
</div>
</div>
'''
    },
    {
        'id': 'while_loops_02',
        'title': 'Loop Control: The Increment Pattern',
        'body': '''
<div class="worked-example">
<h3>Loop Control: The Increment Pattern</h3>
<p>To avoid infinite loops, you must change the variable in the condition.</p>

<div class="concept-box formula-box">
<strong>Key Rule:</strong> Always modify the variable being tested in the while condition. Otherwise, the condition never changes and the loop runs forever.
</div>

<h4>Common Pattern: Increment</h4>
<pre><code class="formula-box">i = 1

while i <= 5:
    print(f"Iteration {i}")
    i = i + 1  # Must increment i to reach the end condition</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Print numbers 1 through 10
<pre><code class="code-block">num = 1

while num <= 10:
    print(num)
    num += 1  # Shorthand for num = num + 1</code></pre>
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Infinite Loop Danger:</strong> If you forget to update the condition variable, the loop never ends.
<pre><code class="code-block">count = 5
while count > 0:
    print(count)
    # MISSING: count = count - 1
    # This loop never stops!</code></pre>
</div>
</div>
'''
    },
    {
        'id': 'while_loops_03',
        'title': 'User Input Loops',
        'body': '''
<div class="worked-example">
<h3>User Input Loops</h3>
<p>While loops are useful for repeating until the user provides valid input.</p>

<div class="concept-box formula-box">
<strong>Pattern:</strong> Loop while input doesn't meet requirements, asking again each time.
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Get a valid age from user
<pre><code class="code-block">age = -1

while age < 0 or age > 150:
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 150:
            print("Please enter a valid age.")
    except ValueError:
        print("Please enter a number.")

print(f"You are {age} years old.")</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Initialize the variable to a value that will make the condition True on the first iteration.
</div>
</div>
'''
    },
    {
        'id': 'while_loops_04',
        'title': 'Sentinel Values',
        'body': '''
<div class="worked-example">
<h3>Sentinel Values</h3>
<p>A sentinel is a special value that signals the end of a loop.</p>

<div class="concept-box formula-box">
<strong>Concept:</strong> Continue looping until a specific "stop" value is entered.
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Sum numbers until user enters -1
<pre><code class="code-block">total = 0
num = 0

while num != -1:
    num = int(input("Enter a number (-1 to stop): "))
    if num != -1:
        total += num

print(f"Sum: {total}")</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Choose a sentinel value that users won't enter as normal input (e.g., -1 for positive numbers).
</div>
</div>
'''
    }
]
