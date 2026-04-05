"""Lists: Ordered, mutable collections for managing sequences of data."""

TITLE = "Lists"

SECTIONS = [
    {
        "id": "lists_01_fundamentals",
        "title": "Fundamentals of Lists",
        "body": """<div class="concept-box">
<h3>What is a List?</h3>
<p>A list is Python's fundamental ordered collection that can hold multiple items of any type. Lists are <strong>mutable</strong>, meaning their contents can be changed after creation. They are indexed starting from 0.</p>
</div>

<h4>Creating Lists</h4>
<div class="worked-example">
<p><strong>Example: Basic list creation</strong></p>
<pre><code># Empty list
empty_list = []

# List with integers
numbers = [1, 2, 3, 4, 5]

# List with mixed types
mixed = [42, "hello", 3.14, True, None]

# List constructor
another_list = list()
</code></pre>
</div>

<h4>Accessing Elements</h4>
<div class="worked-example">
<p><strong>Example: Indexing and slicing</strong></p>
<pre><code>colors = ["red", "green", "blue", "yellow"]

# Forward indexing (0-based)
first = colors[0]      # "red"
third = colors[2]      # "blue"

# Negative indexing (from end)
last = colors[-1]      # "yellow"
second_last = colors[-2]  # "blue"

# Slicing
subset = colors[1:3]   # ["green", "blue"]
from_start = colors[:2]  # ["red", "green"]
to_end = colors[2:]    # ["blue", "yellow"]
</code></pre>
</div>

<div class="success-box">
<strong>Key Insight:</strong> Lists use 0-based indexing. The first element is at index 0, the second at index 1, and so on. Negative indices count from the end: -1 is the last element, -2 is second-to-last.
</div>

<h4>Modifying Lists</h4>
<div class="worked-example">
<p><strong>Example: Mutating list contents</strong></p>
<pre><code>items = ["apple", "banana", "cherry"]

# Change an element
items[1] = "blueberry"  # ["apple", "blueberry", "cherry"]

# Add elements
items.append("date")     # ["apple", "blueberry", "cherry", "date"]
items.insert(0, "aaa")   # ["aaa", "apple", "blueberry", "cherry", "date"]

# Remove elements
items.remove("blueberry")  # ["aaa", "apple", "cherry", "date"]
popped = items.pop()       # ["aaa", "apple", "cherry"], popped = "date"
popped_first = items.pop(0)  # ["apple", "cherry"], popped_first = "aaa"

# Clear all
items.clear()  # []
</code></pre>
</div>

<div class="warning-box">
<strong>⚠️ Warning:</strong> The <code>remove()</code> method removes only the <strong>first occurrence</strong>. Use <code>pop()</code> to remove by index or <code>clear()</code> to remove all elements.
</div>
"""
    },
    {
        "id": "lists_02_operations",
        "title": "List Operations and Methods",
        "body": """<h4>Common List Methods</h4>
<div class="worked-example">
<p><strong>Example: Searching and counting</strong></p>
<pre><code>numbers = [1, 2, 3, 2, 4, 2, 5]

# Find index of first occurrence
idx = numbers.index(2)   # 1
idx = numbers.index(5)   # 6

# Count occurrences
count = numbers.count(2)   # 3
count = numbers.count(10)  # 0

# Check membership
is_present = 3 in numbers    # True
is_present = 10 in numbers   # False
</code></pre>
</div>

<h4>Sorting and Reversing</h4>
<div class="worked-example">
<p><strong>Example: Organizing lists</strong></p>
<pre><code>nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort in place (ascending)
nums.sort()  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort descending
nums.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Create sorted copy (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)  # [1, 1, 3, 4, 5]

# Reverse order
nums.reverse()  # Reverses in place
reversed_copy = original[::-1]  # Create reversed copy
</code></pre>
</div>

<h4>Combining and Extending</h4>
<div class="worked-example">
<p><strong>Example: Merging lists</strong></p>
<pre><code>list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation (creates new list)
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Extend in place
list1.extend(list2)  # list1 is now [1, 2, 3, 4, 5, 6]

# Append vs Extend
list3 = [1, 2, 3]
list3.append([4, 5])      # [1, 2, 3, [4, 5]]
list3_copy = [1, 2, 3]
list3_copy.extend([4, 5])  # [1, 2, 3, 4, 5]
</code></pre>
</div>

<div class="success-box">
<strong>Memory Impact:</strong> <code>extend()</code> is more efficient than repeated <code>append()</code> calls when adding multiple items, as it requires fewer memory reallocations.
</div>

<h4>Iteration and Comprehension</h4>
<div class="worked-example">
<p><strong>Example: Iterating through lists</strong></p>
<pre><code>items = [10, 20, 30, 40]

# Basic iteration
for item in items:
    print(item)  # 10, 20, 30, 40

# With index
for idx, item in enumerate(items):
    print(f"Index {idx}: {item}")

# List comprehension (create new list by transforming)
squared = [x**2 for x in items]  # [100, 400, 900, 1600]

# With filtering
evens = [x for x in items if x % 20 == 0]  # [20, 40]
</code></pre>
</div>
"""
    },
    {
        "id": "lists_03_performance",
        "title": "Memory and Performance Considerations",
        "body": """<h4>Time Complexity of List Operations</h4>
<div class="concept-box">
<table style="width: 100%; border-collapse: collapse">
<tr >
<th style="text-align: left; padding: 8px;">Operation</th>
<th style="text-align: left; padding: 8px;">Time Complexity</th>
<th style="text-align: left; padding: 8px;">Notes</th>
</tr>
<tr >
<td style="padding: 8px;"><code>indexing (list[i])</code></td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">Direct memory access, fastest operation</td>
</tr>
<tr >
<td style="padding: 8px;"><code>append()</code></td>
<td style="padding: 8px;">O(1) amortized</td>
<td style="padding: 8px;">Usually constant, occasionally requires resizing</td>
</tr>
<tr >
<td style="padding: 8px;"><code>insert(i, x)</code></td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Requires shifting elements after position i</td>
</tr>
<tr >
<td style="padding: 8px;"><code>remove(x)</code></td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Must search for element, then shift remainder</td>
</tr>
<tr >
<td style="padding: 8px;"><code>pop()</code></td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">Removing from end is constant</td>
</tr>
<tr >
<td style="padding: 8px;"><code>pop(i)</code></td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Removing from middle requires shifting</td>
</tr>
<tr >
<td style="padding: 8px;"><code>in (membership)</code></td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Linear search through list</td>
</tr>
<tr>
<td style="padding: 8px;"><code>sort()</code></td>
<td style="padding: 8px;">O(n log n)</td>
<td style="padding: 8px;">Timsort algorithm, optimized for partially sorted data</td>
</tr>
</table>
</div>

<h4>Dynamic Memory Growth</h4>
<div class="worked-example">
<p><strong>Why append is usually O(1):</strong></p>
<p>Python lists allocate more capacity than needed. When the capacity is exceeded, the list is resized to a larger capacity (typically 1.25x the current size), allowing subsequent appends to run in constant time.</p>
<pre><code># This happens automatically:
# Start: capacity=0, size=0
# After 1st append: allocate for 4 items
# After 5th append: reallocate for 8 items
# After 9th append: reallocate for 13 items (8 * 1.25)

lst = []
for i in range(1000):
    lst.append(i)  # Usually O(1), occasionally O(n) during reallocation
</code></pre>
</div>

<div class="warning-box">
<strong>⚠️ Important:</strong> Avoid inserting at the beginning or middle of large lists frequently. This requires shifting all subsequent elements, leading to O(n) operations. Consider using <code>collections.deque</code> for efficient insertion at both ends.
</div>

<h4>Memory Layout</h4>
<div class="worked-example">
<p><strong>Example: List vs item storage</strong></p>
<pre><code># Lists store REFERENCES, not the objects themselves
list1 = [1, "hello", 3.14]
# Memory layout:
# [pointer_to_1, pointer_to_"hello", pointer_to_3.14]

# This means:
list2 = list1       # Both reference same objects
list1[0] = 999
print(list2[0])     # Still 1 (integers are immutable)

# But with mutable objects:
list3 = [[1, 2], [3, 4]]
list4 = list3
list3[0].append(999)
print(list4[0])     # [1, 2, 999] - same list object!

# Use copy to avoid this:
list5 = list3.copy()  # Shallow copy
list5[0].append(888)
print(list3[0])     # [1, 2, 999, 888] - still affected!

# For deep copy:
import copy
list6 = copy.deepcopy(list3)
list6[0].append(777)
print(list3[0])     # [1, 2, 999, 888] - not affected
</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use <code>copy.deepcopy()</code> when you need completely independent copies of nested lists. For simple lists of immutable objects, <code>.copy()</code> or slicing <code>[:]</code> is sufficient.
</div>
"""
    }
]
