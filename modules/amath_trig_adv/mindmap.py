MINDMAP = {
    "concepts": [
        {
            "title": "Trigonometric Identities",
            "points": [
                "\\(\\sin^2\\theta + \\cos^2\\theta = 1\\)",
                "\\(\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}\\)",
                "\\(1 + \\tan^2\\theta = \\sec^2\\theta\\)",
                "\\(1 + \\cot^2\\theta = \\csc^2\\theta\\)",
            ],
        },
        {
            "title": "Addition & Double Angle Formulas",
            "points": [
                "\\(\\sin(A \\pm B) = \\sin A \\cos B \\pm \\cos A \\sin B\\)",
                "\\(\\cos(A \\pm B) = \\cos A \\cos B \\mp \\sin A \\sin B\\)",
                "\\(\\tan(A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1 \\mp \\tan A \\tan B}\\)",
                "\\(\\sin 2A = 2\\sin A \\cos A\\)",
                "\\(\\cos 2A = \\cos^2 A - \\sin^2 A = 2\\cos^2 A - 1 = 1 - 2\\sin^2 A\\)",
            ],
        },
        {
            "title": "R-Formula",
            "points": [
                "\\(a\\sin\\theta \\pm b\\cos\\theta = R\\sin(\\theta \\pm \\alpha)\\)",
                "\\(a\\cos\\theta \\pm b\\sin\\theta = R\\cos(\\theta \\mp \\alpha)\\)",
                "\\(R = \\sqrt{a^2 + b^2}\\), \\(\\tan\\alpha = \\frac{b}{a}\\)",
                "Useful for finding max/min values and solving equations",
            ],
        },
        {
            "title": "Solving Trig Equations",
            "points": [
                "Find the basic (reference) angle first",
                "Use ASTC rule to determine which quadrants give solutions",
                "Always list all solutions within the given range",
            ],
        },
        {
            "title": "Graphs of Trig Functions",
            "points": [
                "\\(y = a\\sin(bx + c) + d\\): amplitude \\(|a|\\), period \\(\\frac{2\\pi}{|b|}\\), phase shift \\(-\\frac{c}{b}\\), vertical shift \\(d\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Double angle (sin)", "expr": "\\(\\sin 2A = 2\\sin A \\cos A\\)"},
        {"label": "Double angle (cos)", "expr": "\\(\\cos 2A = 2\\cos^2 A - 1 = 1 - 2\\sin^2 A\\)"},
        {"label": "Double angle (tan)", "expr": "\\(\\tan 2A = \\frac{2\\tan A}{1 - \\tan^2 A}\\)"},
        {"label": "R-formula", "expr": "\\(a\\sin\\theta + b\\cos\\theta = \\sqrt{a^2+b^2}\\sin(\\theta+\\alpha)\\)"},
        {"label": "Pythagorean", "expr": "\\(\\sin^2\\theta + \\cos^2\\theta = 1\\)"},
    ],
    "tips": [
        "For proving identities, work on one side only — usually start with the more complex side.",
        "R-formula gives max value \\(R + d\\) and min value \\(-R + d\\) directly.",
        "When using double angle formulas, choose the version of \\(\\cos 2A\\) that simplifies best with the other terms.",
    ],
}
