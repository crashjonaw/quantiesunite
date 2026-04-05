# Loop Control: break, continue, pass

TITLE = "Loop Control: break, continue, pass"

SECTIONS = [
    {
        'id': 'loop_control_01',
        'title': 'The break Statement',
        'body': '''
<div class="worked-example">
<h3>The break Statement</h3>
<p>The break statement immediately exits a loop, skipping any remaining iterations.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> When break executes, the loop terminates and execution continues after the loop.
</div>

<h4>When to Use break</h4>
<ul>
<li>Search for a target value and stop when found</li>
<li>Exit on error or exception</li>
<li>Implement early termination</li>
</ul>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Search for a number in a list
<pre><code class="code-block">numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
found = False

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        found = True
        break  # Exit the loop immediately
    print(f"Checking {num}...")

print("Search complete.")</code></pre>
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Break on user command
<pre><code class="code-block">while True:
    user_input = input("Enter a command (or 'quit' to exit): ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

print("Goodbye!")</code></pre>
</div>
</div>
'''
    },
    {
        'id': 'loop_control_02',
        'title': 'The continue Statement',
        'body': '''
<div class="worked-example">
<h3>The continue Statement</h3>
<p>The continue statement skips the rest of the current iteration and jumps to the next one.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> When continue executes, any code after it in the loop is skipped, and the next iteration begins.
</div>

<h4>When to Use continue</h4>
<ul>
<li>Skip invalid data</li>
<li>Avoid processing specific items</li>
<li>Simplify conditional logic</li>
</ul>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Process only even numbers
<pre><code class="code-block">numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 != 0:  # Skip odd numbers
        continue
    print(f"{num} is even")</code></pre>
Output: 2 is even, 4 is even, 6 is even, 8 is even, 10 is even
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Skip empty lines
<pre><code class="code-block">lines = ["hello", "", "world", "", "python"]

for line in lines:
    if line == "":  # Skip empty strings
        continue
    print(line)</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> continue is often cleaner than wrapping code in if statements. It simplifies logic flow.
</div>
</div>
'''
    },
    {
        'id': 'loop_control_03',
        'title': 'The pass Statement',
        'body': '''
<div class="worked-example">
<h3>The pass Statement</h3>
<p>The pass statement is a placeholder that does nothing. It's useful when syntax requires a statement but you have nothing to execute.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> pass is a null operation. When executed, nothing happens and execution continues to the next statement.
</div>

<h4>Common Uses</h4>
<ul>
<li>Placeholder in incomplete code</li>
<li>Empty except blocks</li>
<li>Definition stubs for functions or classes</li>
</ul>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Placeholder loop
<pre><code class="code-block">for i in range(5):
    if i == 2:
        pass  # TODO: Add logic here later
    else:
        print(f"Number: {i}")</code></pre>
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Empty except block
<pre><code class="code-block">try:
    result = 10 / int(user_input)
except ValueError:
    pass  # Silently ignore invalid input</code></pre>
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Important:</strong> Don't overuse pass. Use it only as a temporary placeholder or for very specific cases like empty exception handlers.
</div>
</div>
'''
    },
    {
        'id': 'loop_control_04',
        'title': 'Combining break and continue',
        'body': '''
<div class="worked-example">
<h3>Combining break and continue</h3>
<p>You can use break and continue together to create complex control flow.</p>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Search with filtering
<pre><code class="code-block">data = [1, -5, 3, -2, 7, 0, 4, -1]

for num in data:
    if num == 0:  # Skip zeros
        continue
    if num < 0:   # Stop at first negative
        break
    print(f"Processing: {num}")</code></pre>
Output: Processing: 1, Processing: 3
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Input validation with break and continue
<pre><code class="code-block">valid_count = 0

while True:
    user_input = input("Enter a positive number (or 'done'): ")

    if user_input == "done":
        break  # Exit loop

    if not user_input.isdigit():
        print("Invalid! Enter digits only.")
        continue  # Skip to next iteration

    valid_count += 1

print(f"You entered {valid_count} valid numbers.")</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use break and continue to make loops clearer and reduce nesting. Code is often more readable with these statements.
</div>
</div>
'''
    }
]
