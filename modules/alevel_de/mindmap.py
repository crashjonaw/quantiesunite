MINDMAP = {
    "concepts": [
        {"title": "First-Order Separable DEs", "points": [
            "Form: \\(\\frac{dy}{dx} = f(x)g(y)\\)",
            "Separate: \\(\\frac{1}{g(y)}dy = f(x)dx\\), then integrate both sides",
            "Don't forget the constant of integration \\(+C\\)",
        ]},
        {"title": "First-Order Linear DEs", "points": [
            "Form: \\(\\frac{dy}{dx} + P(x)y = Q(x)\\)",
            "Integrating factor: \\(\\mu = e^{\\int P(x)\\,dx}\\)",
            "Multiply through by \\(\\mu\\), then \\(\\frac{d}{dx}(\\mu y) = \\mu Q(x)\\)",
        ]},
        {"title": "Modelling with DEs", "points": [
            "Growth/decay: \\(\\frac{dN}{dt} = kN \\Rightarrow N = N_0 e^{kt}\\)",
            "Newton's cooling: \\(\\frac{dT}{dt} = -k(T - T_s)\\)",
            "Logistic growth: \\(\\frac{dP}{dt} = kP(1 - P/K)\\)",
        ]},
        {"title": "Second-Order DEs", "points": [
            "Homogeneous: solve auxiliary equation \\(am^2 + bm + c = 0\\)",
            "Distinct roots: \\(y = Ae^{m_1x} + Be^{m_2x}\\)",
            "Repeated roots: \\(y = (A + Bx)e^{mx}\\)",
            "Complex roots \\(p \\pm qi\\): \\(y = e^{px}(A\\cos qx + B\\sin qx)\\)",
        ]},
    ],
    "formulas": [
        {"label": "Integrating Factor", "expr": "\\(\\mu = e^{\\int P(x)\\,dx}\\)"},
        {"label": "Exponential Growth", "expr": "\\(N = N_0 e^{kt}\\)"},
        {"label": "Auxiliary Equation", "expr": "\\(am^2 + bm + c = 0\\)"},
        {"label": "General + Particular", "expr": "\\(y = y_{CF} + y_{PI}\\)"},
    ],
    "tips": [
        "Always apply initial/boundary conditions AFTER finding the general solution",
        "For particular integrals, if your trial solution is part of the CF, multiply by \\(x\\)",
        "Check your solution by substituting back into the original DE",
    ],
}
