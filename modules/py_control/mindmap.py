MINDMAP = {
    "concepts": [
        {"title": "if / elif / else", "points": [
            "if condition: ... elif condition: ... else: ...",
            "Indentation defines code blocks (no braces)",
            "Conditions can use and, or, not, in",
        ]},
        {"title": "for Loops", "points": [
            "for item in iterable: — iterate over list, range, string",
            "range(start, stop, step) — generates integer sequences",
            "Useful: enumerate() for index + value, zip() for parallel iteration",
        ]},
        {"title": "while Loops", "points": [
            "while condition: — repeats as long as condition is True",
            "break exits the loop, continue skips to next iteration",
            "Beware infinite loops — ensure condition eventually becomes False",
        ]},
        {"title": "Comprehensions", "points": [
            "List: [x**2 for x in range(10) if x % 2 == 0]",
            "Dict: {k: v for k, v in items}",
            "Concise alternative to for loops for building collections",
        ]},
    ],
    "formulas": [],
    "tips": [
        "Use for when you know how many iterations; while when you don't",
        "Avoid modifying a list while iterating over it — use a copy or comprehension",
        "range(n) gives 0 to n-1, not 1 to n",
    ],
}
