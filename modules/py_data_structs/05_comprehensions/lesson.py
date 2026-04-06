"""Comprehensions: Elegant, concise syntax for creating collections from iterables."""

TITLE = "Comprehensions"

SECTIONS = [
    {
        "id": "comp_01_list",
        "title": "List Comprehensions",
        "body": """<div class="concept-box">
<h3>What is a Comprehension?</h3>
<p>A comprehension is a concise, readable way to create a new collection by transforming or filtering an existing iterable. The basic syntax is:</p>
<pre style="padding: 10px; border-radius: 4px"><code>[expression for item in iterable if condition]</code></pre>
</div>

<h4>Basic List Comprehensions</h4>
<div class="worked-example">
<p><strong>Example: Simple transformation</strong></p>
<pre><code># Equivalent forms:

# Traditional loop
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension (cleaner)
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Other examples
doubled = [x * 2 for x in [1, 2, 3, 4, 5]]  # [2, 4, 6, 8, 10]\\nuppercase = [s.upper() for s in ["a", "b", "c"]]  # ["A", "B", "C"]
</code></pre>
</div>

<h4>Filtering with Conditions</h4>
<div class="worked-example">
<p><strong>Example: Creating filtered collections</strong></p>
<pre><code># Filter: keep only items matching a condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional loop with condition
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# List comprehension with condition
evens = [n for n in numbers if n % 2 == 0]
# [2, 4, 6, 8, 10]

# Complex filtering
data = [10, 20, 30, 40, 50]
filtered = [x for x in data if x > 15 and x < 45]
# [20, 30, 40]

# String filtering
words = ["apple", "ant", "banana", "apricot", "cherry"]
a_words = [w for w in words if w.startswith("a")]
# ["apple", "ant", "apricot"]
</code></pre>
</div>

<h4>Nested List Comprehensions</h4>
<div class="worked-example">
<p><strong>Example: Multiple loops and transformations</strong></p>
<pre><code># Flatten nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Traditional nested loop
flat = []
for row in matrix:
    for item in row:
        flat.append(item)

# List comprehension
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create Cartesian product
colors = ["red", "green"]
sizes = ["S", "M", "L"]
products = [(c, s) for c in colors for s in sizes]
# [("red", "S"), ("red", "M"), ("red", "L"), ("green", "S"), ("green", "M"), ("green", "L")]

# Conditional nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_values = [x for row in matrix for x in row if x % 2 == 0]
# [2, 4, 6, 8]
</code></pre>
</div>

<div class="warning-box">
<strong>⚠️ Readability Warning:</strong> Avoid deeply nested comprehensions (3+ loops). They become hard to read. Use traditional loops instead for clarity.
</div>

<h4>Conditional Expression in Comprehension</h4>
<div class="worked-example">
<p><strong>Example: Transform and filter with conditional expression</strong></p>
<pre><code># Transform based on condition
numbers = [1, 2, 3, 4, 5]

# If/else in comprehension (transform)
doubled_or_original = [x * 2 if x % 2 == 0 else x for x in numbers]
# [1, 4, 3, 8, 5]

# Label items
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
# ["odd", "even", "odd", "even", "odd"]

# vs if-only condition (filters)
evens = [x for x in numbers if x % 2 == 0]
# [2, 4] - filter only

# Transform and filter combined
transformed = [x * 10 if x > 2 else x for x in numbers if x % 2 == 1]
# Filter to odd: [1, 3, 5]
# Transform by rule: [1, 30, 50]
</code></pre>
</div>

<div class="success-box">
<strong>Pattern:</strong>
<ul>
<li><code>[expr for x in iterable]</code> - Transform</li>
<li><code>[x for x in iterable if condition]</code> - Filter</li>
<li><code>[transform if condition else default for x in iterable]</code> - Transform with condition</li>
</ul>
</div>
"""
    },
    {
        "id": "comp_02_dict_set",
        "title": "Dictionary and Set Comprehensions",
        "body": """<h4>Dictionary Comprehensions</h4>
<div class="worked-example">
<p><strong>Example: Creating dictionaries elegantly</strong></p>
<pre><code># Basic dict comprehension: {key: value for item in iterable}
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = {k: v for k, v in pairs}
# {"a": 1, "b": 2, "c": 3}

# Swap keys and values
original = {"name": "Alice", "age": 30}
swapped = {v: k for k, v in original.items()}
# {30: "age", "Alice": "name"}

# Filter while creating
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
# {2: 4, 4: 16, 6: 36}

# Transform values
words = ["apple", "banana", "cherry"]
word_lengths = {w: len(w) for w in words}
# {"apple": 5, "banana": 6, "cherry": 6}
</code></pre>
</div>

<h4>Set Comprehensions</h4>
<div class="worked-example">
<p><strong>Example: Creating sets with comprehension syntax</strong></p>
<pre><code># Basic set comprehension: {expression for item in iterable}
squares = {x**2 for x in range(5)}
# {0, 1, 4, 9, 16}

# Remove duplicates while transforming
numbers = [1, 2, 2, 3, 3, 3, 4]\\nunique_doubled = {x * 2 for x in numbers}
# {2, 4, 6, 8}

# Filter values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = {2, 3, 5, 7}
only_primes = {n for n in numbers if n in primes}
# {2, 3, 5, 7}

# Extract from strings
words = ["apple", "apricot", "banana"]
first_letters = {w[0] for w in words}
# {"a", "b"}

# Unique elements from nested structure
data = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
all_unique = {x for row in data for x in row}
# {1, 2, 3, 4, 5}
</code></pre>
</div>

<h4>Practical Applications</h4>
<div class="worked-example">
<p><strong>Example: Real-world use cases</strong></p>
<pre><code># Create lookup table\\nusers = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]\\nuser_dict = {u["id"]: u["name"] for u in users}
# {1: "Alice", 2: "Bob", 3: "Charlie"}

# Group by property
students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("Diana", "B")
]
# Manual grouping (before defaultdict)
grades = {}
for name, grade in students:
    if grade not in grades:
        grades[grade] = []
    grades[grade].append(name)

# Better: use defaultdict
from collections import defaultdict
grades = defaultdict(list)
for name, grade in students:
    grades[grade].append(name)
# {"A": ["Alice", "Charlie"], "B": ["Bob", "Diana"]}

# Quick unique values
emails = ["alice@example.com", "bob@example.com", "alice@example.com"]\\nunique_emails = {e for e in emails}
# {"alice@example.com", "bob@example.com"}
</code></pre>
</div>

<div class="success-box">
<strong>Pattern Summary:</strong>
<ul>
<li><code>{x**2 for x in iterable}</code> - Set comprehension</li>
<li><code>{key: value for item in iterable}</code> - Dict comprehension</li>
<li><code>{k: v for k, v in iterable if condition}</code> - Filtered dict</li>
</ul>
</div>
"""
    },
    {
        "id": "comp_03_generator",
        "title": "Generator Expressions",
        "body": """<div class="concept-box">
<h3>Generator Expressions</h3>
<p>Generator expressions are like list comprehensions but use parentheses <code>()</code> instead of brackets. They produce values lazily (on-demand) rather than creating the entire list in memory upfront. This is memory-efficient for large datasets.</p>
</div>

<h4>Syntax and Basic Usage</h4>
<div class="worked-example">
<p><strong>Example: List vs Generator comparison</strong></p>
<pre><code># List comprehension - creates entire list
list_comp = [x**2 for x in range(1000000)]
# All 1 million squared values stored in memory

# Generator expression - produces on-demand
gen_exp = (x**2 for x in range(1000000))
# Nothing computed yet!

# Iterate through generator
for value in gen_exp:
    print(value)  # Computed one at a time

# Memory usage: generator uses constant memory
import sys
list_comp = [x**2 for x in range(10000)]
gen_exp = (x**2 for x in range(10000))

print(sys.getsizeof(list_comp))  # ~80,000+ bytes
print(sys.getsizeof(gen_exp))    # ~128 bytes (minimal!)
</code></pre>
</div>

<h4>Generator Functions and yield</h4>
<div class="worked-example">
<p><strong>Example: Creating generators with functions</strong></p>
<pre><code># Generator function uses yield instead of return
def count_up(max):
    current = 0
    while current < max:
        yield current  # Pause here, return value to caller
        current += 1

# Usage
for num in count_up(5):
    print(num)  # 0, 1, 2, 3, 4
# No list created - only one value in memory at a time

# Generator with filtering
def even_numbers(max):
    for i in range(max):
        if i % 2 == 0:
            yield i

# Usage
evens = even_numbers(10)  # Generator object
print(list(evens))  # [0, 2, 4, 6, 8] (convert to list only when needed)

# Multiple yields
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Generate first 5 Fibonacci numbers
fib = fibonacci(100)
print([next(fib) for _ in range(5)])  # [0, 1, 1, 2, 3]
</code></pre>
</div>

<h4>Generator Expressions in Functions</h4>
<div class="worked-example">
<p><strong>Example: Using generators with Python built-ins</strong></p>
<pre><code># sum() with generator - memory efficient
data = range(1000000)

# This creates a huge list, wastes memory
total = sum([x for x in data])

# This computes on-demand, minimal memory
total = sum(x for x in data)

# Note: parentheses optional when generator is sole argument
total = sum((x for x in data))  # Same as above

# Other functions that accept generators
numbers = [1, 2, 3, 4, 5]

# any() - returns True if any element matches
has_even = any(n % 2 == 0 for n in numbers)  # True

# all() - returns True if all elements match
all_positive = all(n > 0 for n in numbers)  # True

# max() / min()
max_even = max((n for n in numbers if n % 2 == 0))  # 4

# Chaining generators
def file_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def long_lines(filename, min_length):
    for line in file_lines(filename):
        if len(line) >= min_length:
            yield line

# Use without loading entire file
for line in long_lines("data.txt", 100):
    print(line)
</code></pre>
</div>

<h4>When to Use Each Form</h4>
<div class="worked-example">
<p><strong>Example: Choosing the right form</strong></p>
<pre><code># Use LIST COMPREHENSION when:
# 1. You need to use the list multiple times
squares = [x**2 for x in range(100)]
print(len(squares))  # Get length
print(squares[50])   # Access by index
print(max(squares))  # Do multiple operations

# 2. The dataset is small
config_values = [int(x) for x in "1,2,3,4,5".split(",")]

# Use GENERATOR EXPRESSION when:
# 1. Processing large datasets
total = sum(x**2 for x in range(1000000))  # O(1) memory

# 2. Data might not be fully consumed
def process_until_found(items):
    for item in (transform(x) for x in items):
        if check(item):
            return item  # Stop early, didn't process all

# 3. Chaining with other generators
def pipeline(items):
    # Multiple transformation stages
    step1 = (clean(x) for x in items)
    step2 = (validate(x) for x in step1)
    for result in step2:
        yield result

# Use GENERATOR FUNCTION when:
# 1. Complex state or logic needed
def parse_json_stream(stream):
    for line in stream:
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            yield None  # or log error
</code></pre>
</div>

<div class="success-box">
<strong>Key Insight:</strong> Generators enable processing of data larger than available memory. For large files, datasets, or infinite streams, generators are essential for memory-efficient Python programs.
</div>
"""
    }
]
