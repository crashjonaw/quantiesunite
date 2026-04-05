"""SciPy Overview and Ecosystem - Core Concepts and Architecture"""

# Dark theme: text=#e6edf3, bg=#0d1117, surface=#161b22, accent=#4f8ef7
# CSS classes: concept-box, worked-example, warning-box, success-box

TITLE = "SciPy Overview and Ecosystem"

SECTIONS = [
    {
        "id": "py_scipy_overview_01",
        "title": "What is SciPy?",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Core Concept: SciPy as a Scientific Python Ecosystem</h3>
        <p>SciPy is a collection of mathematical algorithms and convenience functions built on NumPy. It extends NumPy functionality by providing domain-specific toolkits for optimization, integration, interpolation, linear algebra, statistics, and signal processing.</p>

        <h4>Key Architecture Principles</h4>
        <ul>
            <li><strong>Built on NumPy:</strong> All SciPy functions accept and return NumPy arrays for seamless integration</li>
            <li><strong>Module Organization:</strong> Functionality organized by domain (scipy.optimize, scipy.integrate, etc.)</li>
            <li><strong>C/Fortran Backend:</strong> Performance-critical operations delegated to compiled libraries (LAPACK, BLAS)</li>
            <li><strong>Interoperability:</strong> Works seamlessly with Matplotlib for visualization and Pandas for data handling</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Importing SciPy Modules</h4>
        <pre class="code-block">
import numpy as np
from scipy import optimize, integrate, linalg, stats

# Each module provides specialized functions
# scipy.optimize: minimization, root finding
# scipy.integrate: numerical integration
# scipy.linalg: linear algebra operations
# scipy.stats: statistical functions and distributions
        </pre>
        <p style="margin-top: 12px;">This modular structure allows selective importing of only needed functionality, reducing memory overhead.</p>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Common Pitfall</h4>
        <p>Many users confuse NumPy and SciPy functionality. Remember: NumPy provides basic array operations and linear algebra. SciPy provides advanced numerical methods built on top of NumPy.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_overview_02",
        "title": "SciPy Module Organization",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Understanding the SciPy Ecosystem</h3>
        <p>SciPy is organized into specialized submodules, each addressing a specific computational domain:</p>

        <table style="width: 100%; margin: 16px 0; border-collapse: collapse">
            <thead>
                <tr >
                    <th style="padding: 12px; text-align: left;">Module</th>
                    <th style="padding: 12px; text-align: left;">Purpose</th>
                </tr>
            </thead>
            <tbody>
                <tr >
                    <td style="padding: 12px;">scipy.optimize</td>
                    <td style="padding: 12px;">Function minimization, root finding, optimization algorithms</td>
                </tr>
                <tr >
                    <td style="padding: 12px;">scipy.integrate</td>
                    <td style="padding: 12px;">Numerical integration (ODE/PDE solvers)</td>
                </tr>
                <tr >
                    <td style="padding: 12px;">scipy.linalg</td>
                    <td style="padding: 12px;">Linear algebra (more comprehensive than numpy.linalg)</td>
                </tr>
                <tr >
                    <td style="padding: 12px;">scipy.stats</td>
                    <td style="padding: 12px;">Statistical distributions and tests</td>
                </tr>
                <tr >
                    <td style="padding: 12px;">scipy.signal</td>
                    <td style="padding: 12px;">Signal processing and filtering</td>
                </tr>
                <tr >
                    <td style="padding: 12px;">scipy.sparse</td>
                    <td style="padding: 12px;">Sparse matrix operations</td>
                </tr>
                <tr >
                    <td style="padding: 12px;">scipy.interpolate</td>
                    <td style="padding: 12px;">Interpolation and approximation</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Exploring Module Capabilities</h4>
        <pre class="code-block">
from scipy import optimize, stats
import numpy as np

# Using scipy.optimize to minimize a function
def quadratic(x):
    return (x - 3)**2 + 2

result = optimize.minimize(quadratic, x0=0)
print(f"Minimum at x={result.x[0]:.4f}, f(x)={result.fun:.4f}")

# Using scipy.stats for probability distributions
normal_dist = stats.norm(loc=0, scale=1)
probability = normal_dist.cdf(1.96)  # CDF at 1.96 standard deviations
print(f"P(X ≤ 1.96) = {probability:.4f}")
        </pre>
    </div>

    <div class="success-box">
        <h4>Key Insight</h4>
        <p>SciPy's modular design means you can import only what you need. This reduces initialization time and makes your code more explicit about dependencies.</p>
    </div>
</div>
        """
    },
    {
        "id": "py_scipy_overview_03",
        "title": "Performance and Dependencies",
        "body": """
<div class="worked-example">
    <div class="concept-box formula-box">
        <h3>Why SciPy is Fast: Under-the-Hood Architecture</h3>
        <p>SciPy achieves high performance through strategic use of compiled libraries and NumPy arrays:</p>

        <h4>Performance Strategy</h4>
        <ul>
            <li><strong>BLAS/LAPACK:</strong> Linear algebra operations use optimized Fortran libraries</li>
            <li><strong>NumPy Integration:</strong> Zero-copy operations when passing NumPy arrays</li>
            <li><strong>C/Cython Extensions:</strong> Performance-critical code written in compiled languages</li>
            <li><strong>Lazy Evaluation:</strong> Functions only compute what's requested</li>
        </ul>

        <h4>Memory Efficiency Principles</h4>
        <ul>
            <li>Use views instead of copies when possible</li>
            <li>Work with sparse matrices for large, mostly-empty arrays</li>
            <li>Use in-place operations for large arrays (e.g., <code>+=</code> modifies in-place)</li>
        </ul>
    </div>

    <div class="worked-example success-box">
        <h4>Worked Example: Performance Comparison</h4>
        <pre class="code-block">
import numpy as np
from scipy.linalg import solve
from scipy import stats

# Large linear system - SciPy uses optimized BLAS
n = 1000
A = np.random.rand(n, n)
b = np.random.rand(n)
x = solve(A, b)  # Much faster than numpy.linalg.solve for large systems

# Vectorized statistical operations
data = np.random.randn(10000)
p_value = stats.shapiro(data)[1]  # Shapiro-Wilk normality test
print(f"p-value: {p_value:.6f}")
        </pre>
        <p style="margin-top: 12px;">SciPy delegates to optimized libraries, so operations that look simple in Python are actually running compiled Fortran code underneath.</p>
    </div>

    <div class="warning-box" style="border-left: 4px solid #fd7e14; padding: 16px; margin: 16px 0; border-radius: 4px">
        <h4>Important: Version Compatibility</h4>
        <p>SciPy's API occasionally changes between versions. Always specify version requirements in production code. Some functions deprecated in 1.x may be removed in 2.x.</p>
    </div>
</div>
        """
    }
]
