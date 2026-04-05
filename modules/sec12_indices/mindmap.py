MINDMAP = {
    "concepts": [
        {
            "title": "Index Notation",
            "points": [
                "\\(a^n\\) means \\(a\\) multiplied by itself \\(n\\) times",
                "\\(a\\) is the base, \\(n\\) is the index (or exponent or power)",
                "Example: \\(2^5 = 2 \\times 2 \\times 2 \\times 2 \\times 2 = 32\\)",
            ],
        },
        {
            "title": "Laws of Indices",
            "points": [
                "Multiplication: \\(a^m \\times a^n = a^{m+n}\\)",
                "Division: \\(a^m \\div a^n = a^{m-n}\\)",
                "Power of a power: \\((a^m)^n = a^{mn}\\)",
                "Power of a product: \\((ab)^n = a^n b^n\\)",
            ],
        },
        {
            "title": "Special Indices",
            "points": [
                "Zero index: \\(a^0 = 1\\) (for \\(a \\neq 0\\))",
                "Negative index: \\(a^{-n} = \\frac{1}{a^n}\\)",
                "These follow from the division law",
            ],
        },
        {
            "title": "Standard Form (Scientific Notation)",
            "points": [
                "Written as \\(A \\times 10^n\\) where \\(1 \\leq A < 10\\)",
                "Large numbers: positive \\(n\\), e.g. \\(45000 = 4.5 \\times 10^4\\)",
                "Small numbers: negative \\(n\\), e.g. \\(0.003 = 3 \\times 10^{-3}\\)",
            ],
        },
        {
            "title": "Calculations in Standard Form",
            "points": [
                "Multiply/divide the \\(A\\) parts and add/subtract the powers of 10",
                "Adjust if \\(A\\) is no longer between 1 and 10",
            ],
        },
    ],
    "formulas": [
        {"label": "Multiply", "expr": "\\(a^m \\times a^n = a^{m+n}\\)"},
        {"label": "Divide", "expr": "\\(a^m \\div a^n = a^{m-n}\\)"},
        {"label": "Power of power", "expr": "\\((a^m)^n = a^{mn}\\)"},
        {"label": "Zero index", "expr": "\\(a^0 = 1\\)"},
        {"label": "Negative index", "expr": "\\(a^{-n} = \\frac{1}{a^n}\\)"},
        {"label": "Standard form", "expr": "\\(A \\times 10^n, \\quad 1 \\leq A < 10\\)"},
    ],
    "tips": [
        "Index laws only apply when the BASES are the same (for multiply/divide rules).",
        "A negative index does NOT make the answer negative — it makes a reciprocal.",
        "In standard form, count decimal places moved to find \\(n\\).",
    ],
}
