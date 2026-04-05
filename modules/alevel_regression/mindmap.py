MINDMAP = {
    "concepts": [
        {"title": "Correlation", "points": [
            "Product moment correlation coefficient \\(r\\): measures linear association",
            "\\(-1 \\leq r \\leq 1\\): strong negative to strong positive",
            "\\(r = 0\\) means no linear correlation (not necessarily no relationship)",
        ]},
        {"title": "Least Squares Regression", "points": [
            "Line of best fit: \\(y = a + bx\\) minimises sum of squared residuals",
            "\\(b = \\frac{S_{xy}}{S_{xx}}\\), \\(a = \\bar{y} - b\\bar{x}\\)",
            "Line always passes through \\((\\bar{x}, \\bar{y})\\)",
        ]},
        {"title": "Interpretation & Prediction", "points": [
            "Interpolation (within data range) is reliable; extrapolation is not",
            "\\(r^2\\): proportion of variation in \\(y\\) explained by \\(x\\)",
            "Residual = observed \\(y\\) - predicted \\(y\\)",
        ]},
        {"title": "Transformations", "points": [
            "If data is non-linear, transform variables (e.g. \\(\\ln y\\) vs \\(x\\))",
            "Choose transformation that gives \\(r\\) closest to \\(\\pm 1\\)",
        ]},
    ],
    "formulas": [
        {"label": "Gradient", "expr": "\\(b = \\frac{S_{xy}}{S_{xx}} = \\frac{\\sum xy - n\\bar{x}\\bar{y}}{\\sum x^2 - n\\bar{x}^2}\\)"},
        {"label": "Intercept", "expr": "\\(a = \\bar{y} - b\\bar{x}\\)"},
        {"label": "PMCC", "expr": "\\(r = \\frac{S_{xy}}{\\sqrt{S_{xx} \\cdot S_{yy}}}\\)"},
    ],
    "tips": [
        "Correlation does not imply causation",
        "Use y-on-x regression line for predicting y; x-on-y for predicting x",
        "Never extrapolate beyond the range of your data",
    ],
}
