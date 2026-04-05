# Nested Control Flow: Combining Conditionals and Loops

TITLE = "Nested Control Flow: Combining Conditionals and Loops"

SECTIONS = [
    {
        'id': 'nested_01',
        'title': 'Nesting Conditionals',
        'body': '''
<div class="worked-example">
<h3>Nesting Conditionals</h3>
<p>Conditionals can be placed inside other conditionals to check multiple conditions in sequence.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> Nested conditionals allow you to make decisions based on the result of previous decisions.
</div>

<h4>Syntax Pattern</h4>
<pre><code class="formula-box">if condition1:
    if condition2:
        # Execute if BOTH condition1 AND condition2 are True
        statement
    else:
        # Execute if condition1 is True but condition2 is False
        statement
else:
    # Execute if condition1 is False
    statement</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Determine driver eligibility
<pre><code class="code-block">age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You must get a license first.")
else:
    print("You must be 18 to drive.")</code></pre>
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Readability Tip:</strong> Deeply nested conditionals (more than 3-4 levels) become hard to read. Consider using logical operators (&& and ||) or refactoring into functions.
</div>
</div>
'''
    },
    {
        'id': 'nested_02',
        'title': 'Loops Inside Loops',
        'body': '''
<div class="worked-example">
<h3>Loops Inside Loops</h3>
<p>A loop can contain another loop. The inner loop completes all iterations for each outer loop iteration.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> For each iteration of the outer loop, the inner loop runs completely.
</div>

<h4>Execution Pattern</h4>
<pre><code class="formula-box">for outer_var in outer_sequence:
    for inner_var in inner_sequence:
        # This executes many times!
        statement</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Create a multiplication table
<pre><code class="code-block">for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")</code></pre>
Output: 1 x 1 = 1, 1 x 2 = 2, 1 x 3 = 3, ---, 2 x 1 = 2, ...
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Print a square pattern
<pre><code class="code-block">size = 5

for row in range(size):
    for col in range(size):
        print("*", end=" ")
    print()  # Newline</code></pre>
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Performance Warning:</strong> Nested loops multiply execution time. A loop of 1000 items containing a loop of 1000 items = 1,000,000 operations!
</div>
</div>
'''
    },
    {
        'id': 'nested_03',
        'title': 'Conditionals Inside Loops',
        'body': '''
<div class="worked-example">
<h3>Conditionals Inside Loops</h3>
<p>A common pattern: loop through items and conditionally process them.</p>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Find even numbers in a list
<pre><code class="code-block">numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
        print(f"{num} is even")

print(f"Sum of evens: {even_sum}")</code></pre>
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Filter valid entries
<pre><code class="code-block">entries = ["apple", "", "banana", "", "cherry"]
valid_entries = []

for entry in entries:
    if entry != "":
        valid_entries.append(entry)

print(valid_entries)  # Output: ["apple", "banana", "cherry"]</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use continue to skip invalid items, making the code cleaner than deeply nested if statements.
</div>
</div>
'''
    },
    {
        'id': 'nested_04',
        'title': 'Loops Inside Conditionals',
        'body': '''
<div class="worked-example">
<h3>Loops Inside Conditionals</h3>
<p>A conditional can contain a loop, allowing you to conditionally repeat an action.</p>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Process only if list is not empty
<pre><code class="code-block">data = [10, 20, 30, 40]

if len(data) > 0:
    total = 0
    for value in data:
        total += value
    print(f"Average: {total / len(data)}")
else:
    print("No data to process.")</code></pre>
</div>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Conditional repetition
<pre><code class="code-block">is_learning = True
repeat_count = 3

if is_learning:
    for i in range(repeat_count):
        print(f"Practice attempt {i+1}")
else:
    print("Not practicing today.")</code></pre>
</div>

<div class="success-box">
<strong>Pattern:</strong> Check preconditions before looping. This prevents errors like iterating over empty collections.
</div>
</div>
'''
    }
]
