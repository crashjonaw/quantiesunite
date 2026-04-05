"""Numerical Integration - Quadrature Methods for 1D and Multi-dimensional Integrals"""

TITLE = "Numerical Integration: Quadrature and ODE Solvers"

SECTIONS = [
    {
        "id": "py_scipy_int_01",
        "title": "Foundations of Numerical Integration",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Why Numerical Integration?</h3>
        <p>Many integrals cannot be solved analytically. Numerical integration (quadrature) approximates the definite integral by sampling the function at strategic points and summing weighted contributions.</p>

        <h4>Core Idea: From Sums to Integrals</h4>
        <p>The fundamental theorem of calculus states:</p>
        <p style="text-align: center; font-family: monospace; margin: 12px 0;">∫ₐᵇ f(x)dx ≈ Σ wᵢ f(xᵢ)</p>
        <p>where xᵢ are sample points and wᵢ are weights. Different quadrature methods choose points and weights differently:</p>

        <h4>Common Quadrature Rules</h4>
        <ul>
            <li><strong>Trapezoidal:</strong> Linear approximation between points. Simple but requires many samples.</li>
            <li><strong>Simpson's Rule:</strong> Parabolic approximation. Better accuracy with fewer samples.</li>
            <li><strong>Gaussian Quadrature:</strong> Optimal point selection for polynomials. Very accurate for smooth functions.</li>
            <li><strong>Adaptive Quadrature:</strong> Refines sampling in regions where function varies rapidly.</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Single Integral with scipy.integrate.quad</h4>
        <pre class="code-block">
import numpy as np
from scipy.integrate import quad

# Compute the integral of sin(x) from 0 to π
# Analytical result: [-cos(x)] from 0 to π = 2
def integrand(x):
    return np.sin(x)

result, error = quad(integrand, 0, np.pi)
print(f"∫₀^π sin(x)dx = {result:.10f}")
print(f"Estimated error: {error:.2e}")
print(f"Analytical: 2.0")

# quad uses adaptive quadrature, automatically refining sampling
# Returns both the integral and estimated error bound
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: Error Estimation</h4>
        <p>quad returns TWO values: the integral estimate and an error bound. The error represents SciPy's confidence in accuracy. Smaller error indicates more reliable results.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_int_02",
        "title": "Multi-dimensional Integration",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Double and Triple Integrals</h3>
        <p>For multi-dimensional integrals, numerical quadrature extends naturally. SciPy provides dblquad for 2D and tplquad for 3D integrals with variable limits.</p>

        <h4>Handling Variable Integration Limits</h4>
        <p>In multi-dimensional integration, outer integral limits may be fixed, but inner limits often depend on outer variables:</p>
        <p style="text-align: center; font-family: monospace; margin: 12px 0;">∫∫ f(x,y) dy dx  where y ∈ [a(x), b(x)]</p>

        <h4>SciPy's Multi-dimensional Functions</h4>
        <ul>
            <li><strong>dblquad:</strong> Double integration over rectangular regions (with variable y limits)</li>
            <li><strong>tplquad:</strong> Triple integration (with variable inner limits)</li>
            <li><strong>nquad:</strong> General N-dimensional quadrature</li>
        </ul>

        <h4>Function Signature Pattern</h4>
        <p>Integrand must have arguments in specific order: innermost variable first. Integration limits reverse that order.</p>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Double Integral with dblquad</h4>
        <pre class="code-block">
import numpy as np
from scipy.integrate import dblquad

# Compute volume under z = x*y over region:
# 0 ≤ x ≤ 2, 0 ≤ y ≤ 3
# Analytical: [∫(y²/2 dy)] from 0 to 3 = 9

def integrand(y, x):  # Note: y first (innermost)
    return x * y

# y limits can be constants or functions of x
y_lower = lambda x: 0
y_upper = lambda x: 3

result, error = dblquad(integrand, 0, 2, y_lower, y_upper)
print(f"∫₀² ∫₀³ xy dy dx = {result:.10f}")
print(f"Estimated error: {error:.2e}")
print(f"Analytical: 9.0")

# Example with variable y limits (triangular region)
def y_limit_lower(x):
    return 0

def y_limit_upper(x):
    return 2 - x  # y ≤ 2 - x

result2, _ = dblquad(integrand, 0, 2, y_limit_lower, y_limit_upper)
print(f"\nWith variable limits: {result2:.6f}")
        </pre>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Argument Order Matters!</h4>
        <p>In dblquad, the integrand has y first, then x. Integration limits go: x first (outer), then y functions (inner). This reversal confuses many users.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_int_03",
        "title": "Ordinary Differential Equations",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Solving ODEs Numerically</h3>
        <p>Ordinary differential equations dy/dt = f(t, y) describe how systems evolve over time. Numerical solvers integrate these step-by-step.</p>

        <h4>The IVP (Initial Value Problem)</h4>
        <p>Given an ODE and initial condition y(t₀) = y₀, find y(t) for t > t₀. Solvers like odeint use Runge-Kutta methods to advance the solution iteratively.</p>

        <h4>Key Properties of ODE Solvers</h4>
        <ul>
            <li><strong>Adaptive Timesteping:</strong> Step size increases in smooth regions, decreases near rapid changes</li>
            <li><strong>Error Control:</strong> Monitors local truncation error and refines solution</li>
            <li><strong>Method Selection:</strong> RK45 (4th/5th order), RK23, DOP853 available in solve_ivp</li>
        </ul>

        <h4>When to Use Each Solver</h4>
        <ul>
            <li><strong>odeint:</strong> Simple interface, good for standard problems</li>
            <li><strong>solve_ivp:</strong> More flexible, modern, supports event detection</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Solving the Pendulum Equation</h4>
        <pre class="code-block">
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Pendulum: d²θ/dt² = -(g/L)sin(θ)
# Convert to system: dθ/dt = ω, dω/dt = -(g/L)sin(θ)
g, L = 9.81, 1.0

def pendulum(t, state):
    theta, omega = state
    dtheta_dt = omega
    domega_dt = -(g/L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Initial conditions: θ(0) = π/4, ω(0) = 0
y0 = [np.pi/4, 0]
t_span = (0, 10)
t_eval = np.linspace(0, 10, 1000)

# Solve using RK45 (5th order Runge-Kutta)
sol = solve_ivp(pendulum, t_span, y0, method='RK45', t_eval=t_eval)

print(f"Solution computed at {len(sol.t)} points")
print(f"Integration successful: {sol.status == 0}")

# Extract and visualize
theta = sol.y[0]
# Plot theta vs time
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight: Order Matters</h4>
        <p>Higher-order Runge-Kutta methods (RK45, RK78) give better accuracy but cost more per step. Choose based on accuracy requirements and computation budget.</p>
    </div>
</div>
        """
    }
]
