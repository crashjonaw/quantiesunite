MINDMAP = {
    "concepts": [
        {"title": "Integration by Substitution", "points": [
            "Replace a complicated expression with \\(u\\), find \\(du\\)",
            "Change limits if doing definite integrals",
            "Reverse chain rule: \\(\\int f(g(x))g'(x)\\,dx = F(g(x)) + C\\)",
        ]},
        {"title": "Integration by Parts", "points": [
            "\\(\\int u\\,dv = uv - \\int v\\,du\\)",
            "LIATE rule for choosing \\(u\\): Logs, Inverse trig, Algebra, Trig, Exponentials",
            "Sometimes apply twice, or use the tabular method",
        ]},
        {"title": "Partial Fractions", "points": [
            "Decompose rational functions before integrating",
            "Linear factors: \\(\\frac{A}{x-a} + \\frac{B}{x-b}\\)",
            "Repeated factors: include \\(\\frac{A}{(x-a)} + \\frac{B}{(x-a)^2}\\)",
        ]},
        {"title": "Applications of Integration", "points": [
            "Area between curves: \\(\\int_a^b [f(x) - g(x)]\\,dx\\)",
            "Volume of revolution: \\(V = \\pi\\int_a^b y^2\\,dx\\)",
            "Arc length, surface area of revolution",
        ]},
    ],
    "formulas": [
        {"label": "By Parts", "expr": "\\(\\int u\\,dv = uv - \\int v\\,du\\)"},
        {"label": "Volume (x-axis)", "expr": "\\(V = \\pi\\int_a^b y^2\\,dx\\)"},
        {"label": "Volume (y-axis)", "expr": "\\(V = \\pi\\int_c^d x^2\\,dy\\)"},
        {"label": "Useful Result", "expr": "\\(\\int \\frac{f'(x)}{f(x)}\\,dx = \\ln|f(x)| + C\\)"},
    ],
    "tips": [
        "For by parts, if the integral cycles back to itself, collect it on one side and solve",
        "Always check: can you simplify or use partial fractions before attempting substitution?",
        "For volume of revolution, sketch the region first to identify correct limits and axis",
    ],
}
