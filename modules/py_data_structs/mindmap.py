MINDMAP = {
    "concepts": [
        {"title": "Lists", "points": [
            "Ordered, mutable: [1, 2, 3]",
            "Methods: .append(), .extend(), .pop(), .sort(), .reverse()",
            "Slicing: lst[start:stop:step]",
        ]},
        {"title": "Tuples", "points": [
            "Ordered, immutable: (1, 2, 3)",
            "Use for fixed collections, dict keys, function returns",
            "Unpacking: a, b, c = (1, 2, 3)",
        ]},
        {"title": "Dictionaries", "points": [
            "Key-value pairs: {'name': 'Alice', 'age': 25}",
            "Access: d['key'] or d.get('key', default)",
            "Methods: .keys(), .values(), .items(), .update()",
        ]},
        {"title": "Sets", "points": [
            "Unordered, unique elements: {1, 2, 3}",
            "Operations: union |, intersection &, difference -, symmetric ^",
            "Fast membership testing: x in my_set is O(1)",
        ]},
    ],
    "formulas": [],
    "tips": [
        "Use lists for ordered collections, dicts for lookups, sets for uniqueness",
        "Lists are O(n) for 'in' checks; sets are O(1) — use sets for large membership tests",
        "Dictionary keys must be hashable (immutable) — strings, numbers, tuples work; lists don't",
    ],
}
