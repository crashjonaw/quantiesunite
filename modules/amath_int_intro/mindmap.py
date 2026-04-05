MINDMAP = {
    "concepts": [
        {
            "title": "Indefinite Integration",
            "points": [
                "Reverse of differentiation: \\(\\int x^n \\, dx = \\frac{x^{n+1}}{n+1} + C, \\; n \\neq -1\\)",
                "Always include the constant of integration \\(C\\)",
                "\\(\\int \\frac{1}{x} \\, dx = \\ln|x| + C\\)",
                "\\(\\int e^x \\, dx = e^x + C\\)",
            ],
        },
        {
            "title": "Standard Integrals",
            "points": [
                "\\(\\int \\sin x \\, dx = -\\cos x + C\\)",
                "\\(\\int \\cos x \\, dx = \\sin x + C\\)",
                "\\(\\int \\sec^2 x \\, dx = \\tan x + C\\)",
                "\\(\\int (ax+b)^n \\, dx = \\frac{(ax+b)^{n+1}}{a(n+1)} + C\\)",
            ],
        },
        {
            "title": "Definite Integration",
            "points": [
                "\\(\\int_a^b f(x) \\, dx = F(b) - F(a)\\)",
                "Represents the signed area under the curve from \\(x=a\\) to \\(x=b\\)",
                "Area below x-axis is negative — take absolute value for actual area",
            ],
        },
        {
            "title": "Area & Volume",
            "points": [
                "Area between curve and x-axis: \\(\\int_a^b |f(x)| \\, dx\\)",
                "Area between two curves: \\(\\int_a^b |f(x) - g(x)| \\, dx\\)",
                "Volume of revolution about x-axis: \\(V = \\pi \\int_a^b y^2 \\, dx\\)",
                "Volume about y-axis: \\(V = \\pi \\int_c^d x^2 \\, dy\\)",
            ],
        },
    ],
    "formulas": [
        {"label": "Power rule", "expr": "\\(\\int x^n \\, dx = \\frac{x^{n+1}}{n+1} + C\\)"},
        {"label": "Linear composite", "expr": "\\(\\int (ax+b)^n \\, dx = \\frac{(ax+b)^{n+1}}{a(n+1)} + C\\)"},
        {"label": "Definite integral", "expr": "\\(\\int_a^b f(x)\\,dx = F(b) - F(a)\\)"},
        {"label": "Volume of revolution", "expr": "\\(V = \\pi\\int_a^b y^2 \\, dx\\)"},
    ],
    "tips": [
        "Never forget the \\(+C\\) in indefinite integrals.",
        "When the region crosses the x-axis, split the integral at the roots and take absolute values of each part.",
        "For linear composite functions \\(f(ax+b)\\), divide by the coefficient \\(a\\) after integrating.",
    ],
}
