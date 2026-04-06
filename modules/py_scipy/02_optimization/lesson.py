"""Optimization Methods - Minimization, Root Finding, and Curve Fitting"""

TITLE = "Optimization: Function Minimization and Root Finding"

SECTIONS = [
    {
        "id": "py_scipy_opt_01",
        "title": "Function Minimization Fundamentals",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>What is Function Minimization?</h3>
        <p>Function minimization seeks to find the input value(s) that produce the smallest output. This is fundamental to machine learning (loss minimization), engineering (design optimization), and data science.</p>

        <h4>Core Principle: Gradient Descent</h4>
        <p>Most optimization algorithms work iteratively:</p>
        <ol>
            <li>Start at an initial guess x₀</li>
            <li>Compute the gradient (direction of steepest increase)</li>
            <li>Move in the opposite direction (steepest descent)</li>
            <li>Repeat until convergence (gradient ≈ 0)</li>
        </ol>

        <h4>Types of Optimization Problems</h4>
        <ul>
            <li><strong>Unconstrained:</strong> Minimize f(x) with no restrictions</li>
            <li><strong>Constrained:</strong> Minimize \(f(x)\) subject to \(g(x) \leq 0\)</li>
            <li><strong>Linear:</strong> Both objective and constraints are linear</li>
            <li><strong>Nonlinear:</strong> Objective or constraints are nonlinear</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Basic Minimization with scipy.optimize.minimize</h4>
        <pre class="code-block">
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Define objective function
def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# Minimize starting from (-1.2, 1.0)
result = minimize(rosenbrock, x0=[-1.2, 1.0], method='BFGS')

print(f"Optimization successful: {result.success}")
print(f"Minimum found at: x={result.x}")
print(f"Function value: f(x)={result.fun:.6f}")
print(f"Iterations: {result.nit}")

# The Rosenbrock function has global minimum at (1, 1)
# BFGS uses gradient information for efficient convergence
        </pre>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Common Pitfall: Local vs Global Minima</h4>
        <p>Most optimization algorithms find LOCAL minima (nearby lowest point), not global minima (the absolute lowest). Starting from different initial points may converge to different solutions.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_opt_02",
        "title": "Curve Fitting with scipy.optimize.curve_fit",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Understanding Curve Fitting</h3>
        <p>Curve fitting finds the best parameters of a model function that match observed data. It's a constrained least-squares problem: minimize the sum of squared residuals.</p>

        <h4>The Least Squares Principle</h4>
        <p>Given data points \((x_i, y_i)\) and a model \(y = f(x, \theta)\), find parameters \(\theta\) that minimize:</p>
        <p style="text-align: center; font-family: monospace; margin: 12px 0;">\(\chi^2 = \sum_i [y_i - f(x_i, \theta)]^2\)</p>

        <h4>Key Advantages of curve_fit</h4>
        <ul>
            <li>Automatically computes Jacobian (derivatives) numerically if analytical form not provided</li>
            <li>Returns covariance matrix (uncertainty estimates for fitted parameters)</li>
            <li>Handles both linear and nonlinear models</li>
            <li>More specialized than general minimize() for fitting applications</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Fitting an Exponential Decay Model</h4>
        <pre class="code-block">
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Generate synthetic data: exponential decay
t = np.linspace(0, 10, 50)
y_true = 5 * np.exp(-0.3 * t) + np.random.normal(0, 0.1, len(t))

# Define model: A * exp(-k * t)
def exponential_model(t, A, k):
    return A * np.exp(-k * t)

# Fit the model
params, cov = curve_fit(exponential_model, t, y_true, p0=[5, 0.5])
A_fit, k_fit = params
errors = np.sqrt(np.diag(cov))

print(f"Fitted parameters: A={A_fit:.3f}±{errors[0]:.3f}, k={k_fit:.3f}±{errors[1]:.3f}")
print(f"True values: A=5.0, k=0.3")

# Predict and visualize
y_fit = exponential_model(t, A_fit, k_fit)
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: Uncertainty Quantification</h4>
        <p>The covariance matrix from curve_fit tells you how confident you should be in each fitted parameter. Diagonal elements are variances; larger values indicate greater uncertainty.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_opt_03",
        "title": "Root Finding and Advanced Methods",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Finding Roots: Solving f(x) = 0</h3>
        <p>Root finding seeks values where a function equals zero. This is equivalent to minimization (find x where f(x) is minimized to zero) but uses specialized algorithms.</p>

        <h4>Root Finding Algorithms in SciPy</h4>
        <ul>
            <li><strong>fsolve:</strong> General-purpose solver using hybrid Powell method. Works for systems of equations.</li>
            <li><strong>brentq:</strong> Bracket-based method (similar to bisection). Requires function to change sign in interval.</li>
            <li><strong>root:</strong> Unified interface supporting multiple methods (HYBR, hybr, lm, broyden1, etc.)</li>
        </ul>

        <h4>Method Selection Guide</h4>
        <ul>
            <li><strong>If you can bracket the root:</strong> Use brentq or brenth (reliable, fast)</li>
            <li><strong>For systems of equations:</strong> Use fsolve or root with HYBR method</li>
            <li><strong>For smooth scalar functions:</strong> Use Newton or BFGS minimization</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Finding Roots of a Polynomial</h4>
        <pre class="code-block">
import numpy as np
from scipy.optimize import fsolve, brentq

# Solve: x³ - 6x² + 11x - 6 = 0 (roots at x=1, 2, 3)
def cubic(x):
    return x**3 - 6*x**2 + 11*x - 6

# Method 1: fsolve (general-purpose)
root1 = fsolve(cubic, x0=0)[0]  # Starting guess near 0
print(f"fsolve found root: x = {root1:.6f}")

# Method 2: brentq (bracket-based, if we know root is in [0.5, 1.5])
root2 = brentq(cubic, 0.5, 1.5)  # Must bracket the root
print(f"brentq found root: x = {root2:.6f}")

# Method 3: Vectorized search for all roots
roots = []
for guess in [-1, 1, 3]:
    root = fsolve(cubic, guess)[0]
    if abs(cubic(root)) < 1e-10:  # Verify solution
        roots.append(root)
print(f"All roots found: {sorted(set(np.round(roots, 6)))}")
        </pre>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Convergence Considerations</h4>
        <p>All iterative optimization methods may fail to converge. Always check the result object's success flag and verify the solution satisfies your problem constraints.</p>
    </div>
</div>
        """
    }
]
