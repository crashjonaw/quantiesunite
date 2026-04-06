"""Sets: Unordered, mutable collections of unique elements with fast membership testing."""

TITLE = "Sets"

SECTIONS = [
    {
        "id": "sets_01_fundamentals",
        "title": "Set Fundamentals",
        "body": """<div class="concept-box">
<h3>What is a Set?</h3>
<p>A set is an unordered, mutable collection that contains only unique elements. Sets are ideal for:</p>
<ul>
<li>Removing duplicates from sequences</li>
<li>Fast membership testing (O(1))</li>
<li>Mathematical set operations (union, intersection, difference)</li>
<li>Tracking unique items</li>
</ul>
</div>

<h4>Creating Sets</h4>
<div class="worked-example">
<p><strong>Example: Various set creation methods</strong></p>
<pre><code># Set literal (must have elements)
colors = {"red", "green", "blue"}

# Set constructor
from_list = set([1, 2, 3, 2, 1])  # {1, 2, 3} - duplicates removed

# Empty set (must use set(), NOT {})
empty = set()  # Correct: empty set
not_empty = {}  # Wrong: this is an empty dict!

# From string (each character becomes element)
letters = set("hello")  # {'h', 'e', 'l', 'o'}

# Set comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# From iterable
words = set(["apple", "banana", "apple"])  # {'apple', 'banana'}
</code></pre>
</div>

<div class="warning-box">
<strong>⚠️ Critical:</strong> <code>{}</code> creates an empty <strong>dictionary</strong>, not a set! Use <code>set()</code> for an empty set.
</div>

<h4>Adding and Removing Elements</h4>
<div class="worked-example">
<p><strong>Example: Modifying sets</strong></p>
<pre><code>colors = {"red", "green"}

# Add single element
colors.add("blue")  # {"red", "green", "blue"}

# Add is idempotent (duplicate has no effect)
colors.add("red")  # No change: {"red", "green", "blue"}

# Add multiple elements
colors.update(["yellow", "purple"])  # {"red", "green", "blue", "yellow", "purple"}

# Remove (raises KeyError if missing)
colors.remove("red")  # {"green", "blue", "yellow", "purple"}

# Discard (silent if missing)
colors.discard("orange")  # No error
colors.discard("green")   # {"blue", "yellow", "purple"}

# Pop arbitrary element
random = colors.pop()  # Removes and returns an element

# Clear all
colors.clear()  # set()
</code></pre>
</div>

<h4>Membership and Iteration</h4>
<div class="worked-example">
<p><strong>Example: Testing and looping</strong></p>
<pre><code>fruits = {"apple", "banana", "cherry"}

# Membership test (O(1) average)
has_apple = "apple" in fruits     # True
has_grape = "grape" in fruits     # False

# Not in
not_mango = "mango" not in fruits  # True

# Length
count = len(fruits)  # 3

# Iteration (order not guaranteed)
for fruit in fruits:
    print(fruit)

# Check if subset/superset
s1 = {1, 2, 3}
s2 = {1, 2}
s2.issubset(s1)     # True
s1.issuperset(s2)   # True

# Equality
s3 = {3, 2, 1}
s1 == s3  # True (same elements, order irrelevant)
</code></pre>
</div>

<div class="success-box">
<strong>Performance Win:</strong> Membership testing in a set is O(1) average, compared to O(n) for lists. For large collections where you frequently check membership, sets are much faster.
</div>
"""
    },
    {
        "id": "sets_02_operations",
        "title": "Set Operations and Mathematical Sets",
        "body": """<h4>Set Union</h4>
<div class="worked-example">
<p><strong>Example: Combining sets</strong></p>
<pre><code>a = {1, 2, 3}
b = {3, 4, 5}

# Union: all elements from both sets
result = a | b  # {1, 2, 3, 4, 5}
result = a.union(b)  # Same

# Union in place
a |= b  # a becomes {1, 2, 3, 4, 5}

# Union of multiple sets
c = {5, 6, 7}
result = a | b | c  # {1, 2, 3, 4, 5, 6, 7}
result = a.union(b, c)  # Same
</code></pre>
</div>

<h4>Set Intersection</h4>
<div class="worked-example">
<p><strong>Example: Common elements</strong></p>
<pre><code>languages1 = {"Python", "Java", "C++", "Go"}
languages2 = {"Python", "JavaScript", "Go", "Rust"}

# Intersection: elements in both
common = languages1 & languages2  # {"Python", "Go"}
common = languages1.intersection(languages2)  # Same

# Intersection in place
languages1 &= languages2  # languages1 becomes {"Python", "Go"}

# Find common to all sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5}
set3 = {3, 4, 5, 6}
all_common = set1 & set2 & set3  # {3, 4}
</code></pre>
</div>

<h4>Set Difference</h4>
<div class="worked-example">
<p><strong>Example: Elements unique to each set</strong></p>
<pre><code>team_a = {"Alice", "Bob", "Charlie", "Diana"}
team_b = {"Bob", "Diana", "Eve", "Frank"}

# Difference: in first but not second
only_in_a = team_a - team_b  # {"Alice", "Charlie"}
only_in_a = team_a.difference(team_b)  # Same

# Symmetric difference: in either but not both
different = team_a ^ team_b  # {"Alice", "Charlie", "Eve", "Frank"}
different = team_a.symmetric_difference(team_b)  # Same

# Difference in place
team_a -= team_b  # team_a becomes {"Alice", "Charlie"}
</code></pre>
</div>

<h4>Practical Applications</h4>
<div class="worked-example">
<p><strong>Example: Real-world set operations</strong></p>
<pre><code># Remove duplicates
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]\\nunique = list(set(data))  # [1, 2, 3, 4] (order not guaranteed)

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)  # {3, 4, 5}

# Find elements in one list but not the other
only_in_list1 = set(list1) - set(list2)  # {1, 2}

# Data validation: ensure all required fields present
required = {"name", "email", "age"}
provided = {"name", "email", "phone"}
missing = required - provided  # {"age"}
if missing:
    print(f"Missing fields: {missing}")

# Deduplicate while preserving order
def unique_preserving_order(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

data = [1, 2, 2, 3, 1, 4]\\nunique = unique_preserving_order(data)  # [1, 2, 3, 4]
</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use set operations instead of nested loops to find common/different elements. Set operations are faster and more readable.
</div>
"""
    },
    {
        "id": "sets_03_performance",
        "title": "Frozensets and Performance",
        "body": """<h4>Frozensets: Immutable Sets</h4>
<div class="worked-example">
<p><strong>Example: When you need immutable sets</strong></p>
<pre><code># Frozensets are immutable
immutable = frozenset([1, 2, 3])

# Cannot modify
# immutable.add(4)  # AttributeError
# immutable.remove(1)  # AttributeError

# But can be used as dict keys or set members
d = {}
d[frozenset([1, 2])] = "value"  # Works!

# Or in a set of sets
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}

# Read operations work
3 in immutable  # False
1 in immutable  # True

# Set operations still work (return frozensets)
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])\\nunion = fs1 | fs2  # frozenset({1, 2, 3, 4, 5})
</code></pre>
</div>

<h4>Time Complexity Summary</h4>
<div class="concept-box">
<table style="width: 100%; border-collapse: collapse">
<tr >
<th style="text-align: left; padding: 8px;">Operation</th>
<th style="text-align: left; padding: 8px;">Set</th>
<th style="text-align: left; padding: 8px;">List</th>
<th style="text-align: left; padding: 8px;">Use Set When</th>
</tr>
<tr >
<td style="padding: 8px;">Membership (in)</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Frequent lookups</td>
</tr>
<tr >
<td style="padding: 8px;">Add element</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(1) append</td>
<td style="padding: 8px;">Need uniqueness</td>
</tr>
<tr >
<td style="padding: 8px;">Remove element</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Many removals</td>
</tr>
<tr >
<td style="padding: 8px;">Intersection</td>
<td style="padding: 8px;">O(min(n,m))</td>
<td style="padding: 8px;">O(n*m)</td>
<td style="padding: 8px;">Finding common items</td>
</tr>
<tr >
<td style="padding: 8px;">Union</td>
<td style="padding: 8px;">O(n+m)</td>
<td style="padding: 8px;">O(n+m)</td>
<td style="padding: 8px;">Combining sequences</td>
</tr>
<tr>
<td style="padding: 8px;">Iteration</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Same</td>
</tr>
</table>
</div>

<h4>Memory and Hash Table Performance</h4>
<div class="worked-example">
<p><strong>Example: Sets use hash tables like dicts</strong></p>
<pre><code>import sys

# Sets have hash table overhead like dicts
s = {1, 2, 3, 4, 5}
l = [1, 2, 3, 4, 5]

print(sys.getsizeof(s))  # ~232 bytes (hash table)
print(sys.getsizeof(l))  # ~56 bytes (compact)

# But for membership testing at scale, sets win:
import time

# Create large list and set
n = 1000000
data = list(range(n))
data_set = set(data)

# Test membership 10,000 times
start = time.time()
count = 0
for _ in range(10000):
    if 999999 in data:  # O(n) scan to end
        count += 1
list_time = time.time() - start

start = time.time()
count = 0
for _ in range(10000):
    if 999999 in data_set:  # O(1) hash lookup
        count += 1
set_time = time.time() - start

# Set is orders of magnitude faster!
print(f"List: {list_time:.3f}s, Set: {set_time:.3f}s")
</code></pre>
</div>

<h4>When to Use Each Structure</h4>
<div class="worked-example">
<p><strong>Example: Choosing the right data structure</strong></p>
<pre><code># Use LIST when:
# - Order matters
tasks = ["write", "test", "deploy"]
tasks[0]  # Get first

# - Need duplicates
grades = [95, 90, 95, 88]

# - Need indexing
items = ["a", "b", "c"]
items[1]  # Get by position

# Use SET when:
# - Need fast membership testing\\nusers = set(user_data)
if user_id in users:  # O(1)
    pass

# - Need uniqueness
visited = set()
for location in locations:
    if location not in visited:
        visited.add(location)

# - Need set operations
common = users_group1 & users_group2
</code></pre>
</div>

<div class="success-box">
<strong>Memory Trade-off:</strong> Sets use more memory than lists (hash table overhead) but provide O(1) lookups instead of O(n). For applications with frequent membership testing, the performance gain justifies the extra memory.
</div>
"""
    }
]
