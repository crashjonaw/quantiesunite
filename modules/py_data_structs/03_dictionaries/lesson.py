"""Dictionaries: Unordered, mutable key-value mappings for efficient lookups."""

TITLE = "Dictionaries"

SECTIONS = [
    {
        "id": "dicts_01_fundamentals",
        "title": "Dictionary Fundamentals",
        "body": """<div class="concept-box">
<h3>What is a Dictionary?</h3>
<p>A dictionary is a mutable, unordered collection of key-value pairs. Keys must be hashable (immutable types like strings, numbers, tuples), while values can be any type. Dictionaries provide O(1) average access time, making them ideal for fast lookups.</p>
</div>

<h4>Creating Dictionaries</h4>
<div class="worked-example">
<p><strong>Example: Various dictionary creation methods</strong></p>
<pre><code># Empty dictionary
empty = {}
also_empty = dict()

# Dictionary literal with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

# Mixed key types (all hashable)
mixed = {
    1: "integer key",
    "name": "string key",
    (1, 2): "tuple key",
    3.14: "float key"
}

# Dictionary constructor
d = dict(name="Bob", age=25)  # {'name': 'Bob', 'age': 25}

# From list of pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = dict(pairs)  # {'a': 1, 'b': 2, 'c': 3}

# From list of keys (all get default value)
keys = ["x", "y", "z"]
defaults = dict.fromkeys(keys, 0)  # {'x': 0, 'y': 0, 'z': 0}
</code></pre>
</div>

<h4>Accessing and Modifying</h4>
<div class="worked-example">
<p><strong>Example: Getting, setting, and deleting items</strong></p>
<pre><code>student = {"name": "Charlie", "grade": "A"}

# Access by key
name = student["name"]  # "Charlie"

# Safe access with get()
email = student.get("email")  # None (no KeyError)
email = student.get("email", "unknown@example.com")  # Default value

# Check membership
has_grade = "grade" in student  # True
has_email = "email" in student  # False

# Add or modify
student["email"] = "charlie@example.com"
student["grade"] = "A+"  # Overwrite existing

# Delete items
del student["email"]  # Remove specific key
grade = student.pop("grade")  # Remove and return value

# Remove all
student.clear()  # {}
</code></pre>
</div>

<div class="warning-box">
<strong>⚠️ Common Mistake:</strong> Using <code>dict[key]</code> raises <code>KeyError</code> if the key doesn't exist. Use <code>dict.get(key, default)</code> for safe access.
</div>

<h4>Dictionary Structure and Ordering</h4>
<div class="worked-example">
<p><strong>Example: Dictionary ordering (Python 3.7+)</strong></p>
<pre><code># Python 3.7+ maintains insertion order
ordered = {}
ordered["z"] = 1
ordered["a"] = 2
ordered["m"] = 3

# Iteration preserves insertion order
for key in ordered:
    print(key)  # z, a, m (in insertion order)

# Get all keys, values, items
keys = ordered.keys()      # dict_keys(['z', 'a', 'm'])
values = ordered.values()  # dict_values([1, 2, 3])
items = ordered.items()    # dict_items([('z', 1), ('a', 2), ('m', 3)])

# Unpack key-value pairs
for key, value in ordered.items():
    print(f"{key}: {value}")
</code></pre>
</div>

<div class="success-box">
<strong>Note:</strong> While dictionaries maintain insertion order, they should not be relied upon for ordering in all contexts. Use <code>collections.OrderedDict</code> if explicit ordering semantics are required for older Python versions.
</div>
"""
    },
    {
        "id": "dicts_02_operations",
        "title": "Dictionary Operations and Methods",
        "body": """<h4>Common Dictionary Methods</h4>
<div class="worked-example">
<p><strong>Example: Essential operations</strong></p>
<pre><code>config = {"host": "localhost", "port": 8080, "debug": True}

# Add with default if missing
config.setdefault("timeout", 30)  # Adds if not present
# config = {"host": "localhost", "port": 8080, "debug": True, "timeout": 30}

# Update with another dict
new_config = {"port": 9000, "username": "admin"}
config.update(new_config)

# Get and set with defaults
timeout = config.pop("timeout", 60)  # Remove and return with default

# Copy
shallow = config.copy()
import copy
deep = copy.deepcopy(config)

# Length
size = len(config)  # Number of key-value pairs
</code></pre>
</div>

<h4>Iteration Patterns</h4>
<div class="worked-example">
<p><strong>Example: Different ways to iterate</strong></p>
<pre><code>scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Iterate over keys (default)
for name in scores:
    print(name)

# Explicitly iterate over keys
for name in scores.keys():
    print(name)

# Iterate over values
for score in scores.values():
    print(score)

# Iterate over key-value pairs
for name, score in scores.items():
    print(f"{name}: {score}")

# Build new dict from existing (dict comprehension)
doubled = {name: score * 2 for name, score in scores.items()}
# {'Alice': 190, 'Bob': 174, 'Charlie': 184}

# Filter while building
high_scores = {n: s for n, s in scores.items() if s >= 90}
# {'Alice': 95, 'Charlie': 92}
</code></pre>
</div>

<h4>Advanced Dictionary Patterns</h4>
<div class="worked-example">
<p><strong>Example: Merging and nested dictionaries</strong></p>
<pre><code># Merge multiple dicts (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = d1 | d2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Update syntax (Python 3.9+)
d1 |= d2  # Updates d1 in place

# Nested dictionaries (common in JSON)
person = {
    "name": "Alice",
    "address": {
        "street": "123 Main St",
        "city": "NYC",
        "zip": "10001"
    },
    "contacts": {
        "email": "alice@example.com",
        "phone": "555-1234"
    }
}

# Access nested values
city = person["address"]["city"]  # "NYC"

# Safe nested access
email = person.get("contacts", {}).get("email")  # "alice@example.com"
</code></pre>
</div>

<h4>Default Values and Counters</h4>
<div class="worked-example">
<p><strong>Example: Using defaultdict and Counter</strong></p>
<pre><code>from collections import defaultdict, Counter

# defaultdict with default value
word_counts = defaultdict(int)  # Default value is 0
words = ["apple", "banana", "apple", "cherry", "apple"]
for word in words:
    word_counts[word] += 1
# defaultdict(int, {'apple': 3, 'banana': 1, 'cherry': 1})

# Counter - optimized for counting
counts = Counter(words)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
counts.most_common(2)   # [('apple', 3), ('banana', 1)]

# Without defaultdict, you need defensive code:
regular = {}
for word in words:
    if word in regular:
        regular[word] += 1
    else:
        regular[word] = 1
</code></pre>
</div>

<div class="success-box">
<strong>Best Practice:</strong> Use <code>defaultdict</code> to eliminate "if key exists" checks, and <code>Counter</code> for counting hashable objects.
</div>
"""
    },
    {
        "id": "dicts_03_performance",
        "title": "Hash Tables and Performance",
        "body": """<h4>Hash Table Mechanics</h4>
<div class="concept-box">
<p><strong>How Python dictionaries work:</strong></p>
<ol >
<li>Key is passed to a hash function: <code>hash_value = hash(key)</code></li>
<li>Hash value mapped to table index: <code>index = hash_value % table_size</code></li>
<li>Value stored at that index</li>
<li>Hash collisions resolved using linear probing or open addressing</li>
</ol>
</div>

<h4>Time Complexity Analysis</h4>
<div class="concept-box">
<table style="width: 100%; border-collapse: collapse">
<tr >
<th style="text-align: left; padding: 8px;">Operation</th>
<th style="text-align: left; padding: 8px;">Average Case</th>
<th style="text-align: left; padding: 8px;">Worst Case</th>
<th style="text-align: left; padding: 8px;">Notes</th>
</tr>
<tr >
<td style="padding: 8px;">Access/Lookup</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Rare; happens with bad hash collisions</td>
</tr>
<tr >
<td style="padding: 8px;">Insertion</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">May trigger resizing: O(n)</td>
</tr>
<tr >
<td style="padding: 8px;">Deletion</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Same as insertion</td>
</tr>
<tr >
<td style="padding: 8px;">Iteration</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Must visit all entries</td>
</tr>
<tr>
<td style="padding: 8px;">Contains (in)</td>
<td style="padding: 8px;">O(1)</td>
<td style="padding: 8px;">O(n)</td>
<td style="padding: 8px;">Same as lookup</td>
</tr>
</table>
</div>

<h4>Hash Function Requirements</h4>
<div class="worked-example">
<p><strong>Example: What makes a good key</strong></p>
<pre><code># GOOD keys - hashable and immutable
d = {}
d["string_key"] = 1         # Strings are immutable
d[42] = 2                   # Numbers are immutable
d[(1, 2, 3)] = 3            # Tuples (of immutables) are immutable
d[frozenset([1, 2])] = 4    # frozenset is immutable

# BAD keys - mutable types
# d[[1, 2, 3]] = "bad"      # TypeError: lists are unhashable
# d[{1, 2}] = "bad"         # TypeError: sets are unhashable
# d[{"a": 1}] = "bad"       # TypeError: dicts are unhashable

# Custom objects as keys
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
d[p1] = "data"  # Works - objects are hashable by default (identity)

# However, if you modify mutable objects, be careful
my_list = [1, 2, 3]
my_list.append(4)  # List content changed
# All previous lookups still work because hash is based on identity
</code></pre>
</div>

<h4>Dictionary Size and Load Factor</h4>
<div class="worked-example">
<p><strong>Example: How Python manages dictionary growth</strong></p>
<pre><code>import sys

# Initial empty dictionary
d = {}
print(sys.getsizeof(d))  # ~240 bytes (includes hash table)

# Adding items - dictionary grows as load factor increases
d = {i: i for i in range(1000)}
print(sys.getsizeof(d))  # Much larger

# Python maintains load factor around 2/3
# When exceeded, dictionary is rehashed with larger table
# This is O(n) but amortized to O(1) per insertion

# Worst case: all keys hash to same value
# (extremely rare with Python's good hash functions)
class BadHash:
    def __hash__(self):
        return 0  # All instances hash to same value

d = {}
for i in range(100):
    d[BadHash()] = i  # O(n) insertion for each item!
</code></pre>
</div>

<div class="success-box">
<strong>Memory Insight:</strong> Dictionaries use more memory than lists of the same size (hash table overhead), but this overhead enables O(1) lookups instead of O(n). For applications requiring many lookups, dictionaries are worth the extra memory.
</div>
"""
    }
]
