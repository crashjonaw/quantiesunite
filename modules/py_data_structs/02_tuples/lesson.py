"""Tuples: Immutable, ordered sequences for fixed data collections."""

TITLE = "Tuples"

SECTIONS = [
    {
        "id": "tuples_01_fundamentals",
        "title": "Fundamentals of Tuples",
        "body": """<div class="concept-box">
<h3>What is a Tuple?</h3>
<p>A tuple is an <strong>immutable</strong> ordered collection. Once created, its contents cannot be changed. Tuples are created using parentheses <code>()</code> and are hashable, making them suitable as dictionary keys or set members—something lists cannot do.</p>
</div>

<h4>Creating Tuples</h4>
<div class="worked-example">
<p><strong>Example: Various tuple creation methods</strong></p>
<pre><code># Empty tuple (note: single parenthesis is not enough)
empty = ()
also_empty = tuple()

# Single element tuple (comma is REQUIRED!)
single = (42,)
not_a_tuple = (42)      # This is just 42, an integer!

# Multiple elements
coords = (10, 20)
mixed = (1, "hello", 3.14, True, None)
nested = ((1, 2), (3, 4), (5, 6))

# Tuple unpacking
x, y = (10, 20)  # x=10, y=20
a, b, c = (1, 2, 3)

# Parentheses are optional
no_parens = 1, 2, 3  # Still a tuple: (1, 2, 3)

# Convert from other types
from_list = tuple([1, 2, 3])      # (1, 2, 3)
from_string = tuple("abc")        # ('a', 'b', 'c')
</code></pre>
</div>

<div class="warning-box">
<strong>⚠️ Critical:</strong> A single-element tuple MUST have a trailing comma: <code>(42,)</code>. Without it, <code>(42)</code> is interpreted as an integer with extra parentheses, not a tuple!
</div>

<h4>Accessing Tuple Elements</h4>
<div class="worked-example">
<p><strong>Example: Indexing and slicing</strong></p>
<pre><code>rgb = ("red", "green", "blue")

# Indexing (same as lists)
first = rgb[0]       # "red"
last = rgb[-1]       # "blue"

# Slicing
subset = rgb[1:]     # ("green", "blue")
middle = rgb[0:2]    # ("red", "green")

# Iteration
for color in rgb:
    print(color)

# Enumeration
for idx, color in enumerate(rgb):
    print(f"{idx}: {color}")
</code></pre>
</div>

<h4>Why Immutability Matters</h4>
<div class="worked-example">
<p><strong>Example: Tuples cannot be modified</strong></p>
<pre><code>point = (10, 20)

# These will raise TypeError:
point[0] = 15          # TypeError: 'tuple' object does not support item assignment
point.append(30)       # TypeError: 'tuple' object has no attribute 'append'

# BUT: mutable objects inside tuples can be modified
data = ([1, 2], [3, 4])
data[0].append(999)    # OK! ([1, 2, 999], [3, 4])
data[0] = [5, 6]       # ERROR! Cannot reassign tuple elements
</code></pre>
</div>

<div class="success-box">
<strong>Key Insight:</strong> Tuples are immutable at the reference level. You cannot change which objects a tuple references, but the objects themselves (if mutable like lists) can be modified.
</div>
"""
    },
    {
        "id": "tuples_02_operations",
        "title": "Tuple Operations and Use Cases",
        "body": """<h4>Basic Operations</h4>
<div class="worked-example">
<p><strong>Example: Searching and counting in tuples</strong></p>
<pre><code>nums = (1, 2, 3, 2, 4, 2, 5)

# Count occurrences
count = nums.count(2)      # 3

# Find first index
idx = nums.index(4)        # 4
idx = nums.index(2)        # 1 (first occurrence)

# Membership test
is_present = 3 in nums     # True
is_present = 10 in nums    # False

# Concatenation (creates new tuple)
t1 = (1, 2)
t2 = (3, 4)
combined = t1 + t2         # (1, 2, 3, 4)

# Repetition
repeated = (1, 2) * 3      # (1, 2, 1, 2, 1, 2)

# Length
length = len(nums)         # 7
</code></pre>
</div>

<h4>Unpacking and Multiple Return Values</h4>
<div class="worked-example">
<p><strong>Example: Powerful tuple unpacking patterns</strong></p>
<pre><code># Basic unpacking
point = (10, 20, 30)
x, y, z = point

# Unpacking with _ (ignore value)
name, _, age = ("Alice", "secret", 25)  # name="Alice", age=25

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2, 3, 4], last=5

# Swapping variables (no temporary needed!)
a, b = 5, 10
a, b = b, a  # a=10, b=5

# Multiple return values from functions
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# Dictionary from pairs
pairs = (('a', 1), ('b', 2), ('c', 3))
d = dict(pairs)  # {'a': 1, 'b': 2, 'c': 3}
</code></pre>
</div>

<h4>Tuples as Dictionary Keys</h4>
<div class="worked-example">
<p><strong>Example: Using tuples as keys (lists cannot be used)</strong></p>
<pre><code># Tuples are hashable - can be dictionary keys
locations = {
    (10, 20): "Home",
    (5, 15): "Office",
    (0, 0): "Origin"
}

# Access by coordinate
home = locations[(10, 20)]  # "Home"

# Tuples in sets
visited = {(1, 1), (2, 2), (3, 3)}
if (1, 1) in visited:
    print("Been there!")

# This would NOT work with lists:
# bad = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
</code></pre>
</div>

<h4>Named Tuples</h4>
<div class="worked-example">
<p><strong>Example: Structured tuples with named fields</strong></p>
<pre><code>from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y', 'z'])
Color = namedtuple('Color', 'r g b')  # Alternative syntax

# Create instances
p = Point(10, 20, 30)
c = Color(255, 128, 0)

# Access by name (clearer than indexing)
print(p.x, p.y, p.z)      # 10 20 30
print(c.r, c.g, c.b)      # 255 128 0

# Still indexable
print(p[0])                # 10

# Immutable like regular tuples
# p.x = 15  # AttributeError
</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use <code>namedtuple</code> for small, fixed-size data records. It provides readability and structure while maintaining tuple efficiency and immutability.
</div>
"""
    },
    {
        "id": "tuples_03_performance",
        "title": "Performance and Memory Efficiency",
        "body": """<h4>Time Complexity Comparison</h4>
<div class="concept-box">
<table style="width: 100%; border-collapse: collapse">
<tr >
<th style="text-align: left; padding: 8px;">Operation</th>
<th style="text-align: left; padding: 8px;">Tuple</th>
<th style="text-align: left; padding: 8px;">List</th>
<th style="text-align: left; padding: 8px;">Notes</th>
</tr>
<tr >
<td style="padding: 8px;">Indexing</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">Same speed</td>
</tr>
<tr >
<td style="padding: 8px;">Iteration</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Tuples slightly faster</td>
</tr>
<tr >
<td style="padding: 8px;">Membership (in)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Same complexity</td>
</tr>
<tr >
<td style="padding: 8px;">Length</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">Same speed</td>
</tr>
<tr >
<td style="padding: 8px;">Hashing</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">N/A</td>
<td style="padding: 8px;">Only tuples can be hashed</td>
</tr>
<tr>
<td style="padding: 8px;">Concatenation</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Creates new object</td>
</tr>
</table>
</div>

<h4>Memory Efficiency</h4>
<div class="worked-example">
<p><strong>Example: Tuples use less memory than lists</strong></p>
<pre><code>import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # ~104 bytes (includes capacity)
print(sys.getsizeof(my_tuple))  # ~80 bytes (exact size, no overhead)

# Tuples are cached for small integers
t1 = (1,)
t2 = (1,)
print(t1 is t2)  # May be True (tuple interning)

# Lists are never interned
l1 = [1]
l2 = [1]
print(l1 is l2)  # False (different objects)
</code></pre>
</div>

<h4>When to Use Tuples vs Lists</h4>
<div class="worked-example">
<p><strong>Example: Choosing the right structure</strong></p>
<pre><code># Use TUPLES when:
# 1. Data should not change
coordinates = (10, 20)  # Fixed point

# 2. Using as dictionary key
cache = {(1, 1): "value"}  # Tuple key

# 3. Returning multiple values
def get_user():
    return ("Alice", 25, "alice@example.com")

# 4. Function arguments (varargs use tuples)
def print_args(*args):
    # args is a tuple
    for arg in args:
        print(arg)

# Use LISTS when:
# 1. Data may change
tasks = ["Write code", "Test code", "Deploy"]
tasks.append("Monitor")

# 2. Need efficient insertion/deletion
# (Not at beginning/middle, but Python lists handle this)

# 3. Need list-specific methods
scores = [85, 90, 78, 92]
scores.sort()
</code></pre>
</div>

<div class="success-box">
<strong>Performance Insight:</strong> Tuples have lower memory overhead and can be slightly faster to iterate. More importantly, their immutability enables optimizations (like caching small tuples) and makes them safe for use as dict keys or in sets.
</div>
"""
    }
]
