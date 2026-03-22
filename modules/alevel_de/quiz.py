QUIZ = [
    {
        "question": "Solve the separable ODE dy/dx = (1+y²)/x with y(1) = 0",
        "answer": "arctan(y) = ln(x), or y = tan(ln(x))",
        "explanation": "Rearrange: dy/(1+y²) = dx/x. Integrate: arctan(y) = ln|x| + C. Apply y(1) = 0: arctan(0) = ln(1) + C ⟹ C = 0. So arctan(y) = ln(x), thus y = tan(ln(x))."
    },
    {
        "question": "Show that y = e^(-t) + 1 is a solution to dy/dt + y = 1 and satisfies y(0) = 2",
        "answer": "dy/dt = -e^(-t). dy/dt + y = -e^(-t) + e^(-t) + 1 = 1. ✓ y(0) = e^0 + 1 = 2. ✓",
        "explanation": "If y = e^(-t) + 1, then dy/dt = -e^(-t). Substituting into dy/dt + y = 1: -e^(-t) + (e^(-t) + 1) = 1 ✓. Initial condition: y(0) = e^0 + 1 = 2 ✓."
    },
    {
        "question": "A population grows according to dP/dt = 0.1P. If P(0) = 1000, find P(t)",
        "answer": "P(t) = 1000e^(0.1t)",
        "explanation": "This is a separable equation: dP/P = 0.1 dt. Integrate: ln|P| = 0.1t + C. P(t) = Ae^(0.1t). Apply P(0) = 1000: 1000 = A. So P(t) = 1000e^(0.1t)."
    },
    {
        "question": "Solve the linear ODE dy/dx + y = e^x and find the general solution",
        "answer": "y = (e^x + C)e^(-x) or y = (1/2)e^x + Ce^(-x)",
        "explanation": "Integrating factor: μ(x) = e^(∫1 dx) = e^x. Multiply: e^x·dy/dx + e^x·y = e^(2x). This becomes d/dx[e^x·y] = e^(2x). Integrate: e^x·y = (1/2)e^(2x) + C. So y = (1/2)e^x + Ce^(-x)."
    },
    {
        "question": "Determine the stability of the equilibrium y = 0 for dy/dx = -2y",
        "answer": "y = 0 is stable (sink) because solutions decay toward it",
        "explanation": "For dy/dx = -2y, if y > 0, then dy/dx < 0 (decreasing toward 0). If y < 0, then dy/dx > 0 (increasing toward 0). All nearby solutions converge to y = 0, making it a stable equilibrium (sink)."
    }
]
