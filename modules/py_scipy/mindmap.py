MINDMAP = {
    "concepts": [
        {"title": "Numerical Integration", "points": [
            "scipy.integrate.quad for definite integrals of one variable",
            "scipy.integrate.dblquad / tplquad for double and triple integrals",
            "scipy.integrate.solve_ivp for initial value ODE problems (replaces odeint)",
            "Returns (result, error_estimate) — always check the error",
        ]},
        {"title": "Optimisation", "points": [
            "scipy.optimize.minimize for unconstrained and constrained minimisation",
            "Methods: Nelder-Mead (derivative-free), BFGS (gradient), L-BFGS-B (bounded)",
            "scipy.optimize.minimize_scalar for single-variable problems",
            "scipy.optimize.root and fsolve for finding roots of equations",
        ]},
        {"title": "Linear Algebra (scipy.linalg)", "points": [
            "solve(A, b) solves \\(Ax = b\\) — faster and more stable than inv(A) @ b",
            "eig(A) returns eigenvalues and eigenvectors",
            "lu, qr, svd, cholesky decompositions available",
            "det(A) for determinant, norm(A) for matrix norms",
        ]},
        {"title": "Interpolation & Curve Fitting", "points": [
            "scipy.interpolate.interp1d for 1-D interpolation (linear, cubic, etc.)",
            "scipy.optimize.curve_fit for non-linear least-squares fitting",
            "UnivariateSpline for smoothing spline fits",
        ]},
        {"title": "Signal & Special Functions", "points": [
            "scipy.signal for filtering, convolution, FFT-based spectral analysis",
            "scipy.special for Bessel, gamma, beta, error functions and more",
            "scipy.stats for probability distributions, hypothesis tests, descriptive stats",
        ]},
    ],
    "formulas": [
        {"label": "Numerical Integral", "expr": "\\(\\int_a^b f(x)\\,dx \\approx \\texttt{quad}(f, a, b)\\)"},
        {"label": "Minimise", "expr": "\\(\\min_{x} f(x) \\text{ subject to } g(x) \\le 0\\)"},
        {"label": "Linear Solve", "expr": "\\(Ax = b \\Rightarrow x = A^{-1}b\\)"},
        {"label": "Least-Squares Fit", "expr": "\\(\\min_{\\theta} \\sum_i (y_i - f(x_i; \\theta))^2\\)"},
    ],
    "tips": [
        "Prefer scipy.linalg.solve over numpy.linalg.inv — it is faster and numerically stabler.",
        "Always supply an initial guess (x0) to optimisers; bad guesses lead to local minima.",
        "Use scipy.integrate.solve_ivp instead of the older odeint for new code.",
        "Check convergence flags: res.success for optimise, error bounds for integrate.",
    ],
}
