# For Loops: Iterating Over Sequences

TITLE = "For Loops: Iterating Over Sequences"

SECTIONS = [
    {
        'id': 'for_loops_01',
        'title': 'Iteration Over Collections',
        'body': '''
<div class="worked-example">
<h3>Iteration Over Collections</h3>
<p>A for loop iterates over each item in a sequence without needing a counter variable.</p>

<div class="concept-box formula-box">
<strong>Core Concept:</strong> For loops handle the iteration mechanism automatically. Each iteration, the loop variable holds the next item from the sequence.
</div>

<h4>Syntax</h4>
<pre><code class="formula-box">for item in sequence:
    # Code executes once per item
    statement1
    statement2</code></pre>

<h4>Iterables in Python</h4>
<p>You can iterate over:</p>
<ul>
<li><strong>Lists:</strong> <code class="formula-box" style="padding: 2px 6px;">["apple", "banana", "cherry"]</code></li>
<li><strong>Tuples:</strong> <code class="formula-box" style="padding: 2px 6px;">(1, 2, 3)</code></li>
<li><strong>Strings:</strong> <code class="formula-box" style="padding: 2px 6px;">"hello"</code> (iterates character by character)</li>
<li><strong>Ranges:</strong> <code class="formula-box" style="padding: 2px 6px;">range(5)</code></li>
<li><strong>Dictionaries:</strong> <code class="formula-box" style="padding: 2px 6px;">{"a": 1, "b": 2}</code></li>
</ul>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Print each color in a list
<pre><code class="code-block">colors = ["red", "green", "blue"]

for color in colors:
    print(color)</code></pre>
Output: red, green, blue
</div>
</div>
'''
    },
    {
        'id': 'for_loops_02',
        'title': 'The range() Function',
        'body': '''
<div class="worked-example">
<h3>The range() Function</h3>
<p>range() generates sequences of numbers, commonly used to repeat code a specific number of times.</p>

<div class="concept-box formula-box">
<strong>Syntax:</strong> <code class="formula-box" style="padding: 2px 6px;">range(stop)</code> or <code class="formula-box" style="padding: 2px 6px;">range(start, stop, step)</code>
</div>

<h4>Three Forms</h4>
<pre><code class="formula-box">range(5)           # 0, 1, 2, 3, 4 (stop is exclusive)
range(2, 5)        # 2, 3, 4 (start at 2, stop before 5)
range(0, 10, 2)    # 0, 2, 4, 6, 8 (every 2nd number)</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Print 1 through 5
<pre><code class="code-block">for i in range(1, 6):
    print(i)</code></pre>
Output: 1, 2, 3, 4, 5
</div>

<div class="warning-box" style="border-left: 4px solid #dc3545; padding: 15px; margin: 15px 0">
<strong>Key Point:</strong> The stop value is exclusive. <code style="padding: 2px 6px; border-radius: 4px">range(5)</code> goes to 4, not 5.
</div>
</div>
'''
    },
    {
        'id': 'for_loops_03',
        'title': 'Iterating Strings and Index Access',
        'body': '''
<div class="worked-example">
<h3>Iterating Strings and Index Access</h3>
<p>Strings are sequences of characters. You can iterate over them or access characters by position.</p>

<h4>Direct Iteration</h4>
<pre><code class="formula-box">word = "Python"

for letter in word:
    print(letter)</code></pre>

<h4>Index-Based Access</h4>
<p>Access characters by their position (0-indexed):</p>
<pre><code class="formula-box">word = "Python"
print(word[0])    # "P"
print(word[1])    # "y"
print(word[2])    # "t"</code></pre>

<div class="worked-example success-box">
<strong>Worked Example:</strong> Reverse a string
<pre><code class="code-block">word = "hello"
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)  # Output: olleh</code></pre>
</div>

<div class="success-box">
<strong>Tip:</strong> <code class="formula-box" style="padding: 2px 6px;">len()</code> returns the length of a string, allowing you to iterate using indices.
</div>
</div>
'''
    },
    {
        'id': 'for_loops_04',
        'title': 'Looping Over Lists and enumerate()',
        'body': '''
<div class="worked-example">
<h3>Looping Over Lists and enumerate()</h3>
<p>Lists are collections of items. You can iterate directly or use enumerate() to get both index and value.</p>

<h4>Direct Iteration</h4>
<pre><code class="formula-box">fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)</code></pre>

<h4>Using enumerate()</h4>
<p>When you need both the index and the item:</p>
<pre><code class="formula-box">fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")</code></pre>
Output: 0: apple, 1: banana, 2: orange

<div class="worked-example success-box">
<strong>Worked Example:</strong> Score list with positions
<pre><code class="code-block">scores = [95, 87, 92, 88]

for position, score in enumerate(scores, 1):  # Start counting at 1
    print(f"Student {position}: {score}")</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use enumerate() instead of manually managing indices. It's cleaner and less error-prone.
</div>
</div>
'''
    }
]
