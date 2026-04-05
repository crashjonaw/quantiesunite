TITLE = "Steady-State Distributions and Limiting Behavior"

SECTIONS = [
    {
        "title": "Steady-State Distribution Definition",
        "body": """
        <div class="concept-box">
        <p><strong>Steady-State Distribution $\\boldsymbol{\\pi}^*$:</strong> A probability distribution that doesn't change when multiplied by the transition matrix $P$.</p>
        </div>

        <p><strong>Mathematical Definition:</strong></p>
        <p>$$\\boldsymbol{\\pi}^* = \\boldsymbol{\\pi}^* P$$</p>

        <p>In other words, $\\boldsymbol{\\pi}^*$ is a left eigenvector of $P$ with eigenvalue 1, subject to $\\sum_i \\pi^*_i = 1$ (probabilities sum to 1).</p>

        <p><strong>Element-wise formulation:</strong> For each state $j$:</p>
        <p>$$\\pi^*_j = \\sum_i \\pi^*_i P_{ij}$$</p>

        <p>This is the <strong>balance equation</strong>: the long-run probability of being in state $j$ equals the sum of (probability of being in state $i$) $\\times$ (probability of transitioning $i \\to j$) for all $i$.</p>

        <div class="worked-example">
        <p><strong>Example: Simple 2-State Chain</strong></p>
        <pre class='code-block'>$$P = \\begin{bmatrix} 0.6 & 0.4 \\\\ 0.3 & 0.7 \\end{bmatrix}$$

Steady-state equation: $\\boldsymbol{\\pi}^* = \\boldsymbol{\\pi}^* P$
$\\pi^*_1 \\cdot 0.6 + \\pi^*_2 \\cdot 0.3 = \\pi^*_1$
$\\pi^*_1 \\cdot 0.4 + \\pi^*_2 \\cdot 0.7 = \\pi^*_2$
$\\pi^*_1 + \\pi^*_2 = 1$

From first equation: $\\pi^*_2 \\cdot 0.3 = 0.4\\pi^*_1$, so $\\pi^*_2 = \\frac{4}{3}\\pi^*_1$
Substituting into normalization: $\\pi^*_1 + \\frac{4}{3}\\pi^*_1 = 1$
$\\frac{7}{3}\\pi^*_1 = 1$, so $\\pi^*_1 = 3/7 \\approx 0.429$, $\\pi^*_2 = 4/7 \\approx 0.571$</pre>
        </div>
        """
    },
    {
        "title": "Existence, Uniqueness, and the Ergodic Theorem",
        "body": """
        <p><strong>When does steady-state exist?</strong> For finite-state chains, at least one steady-state always exists. However, uniqueness requires conditions:</p>

        <p><strong>Conditions for unique steady-state (Ergodic Theorem):</strong></p>
        <ol>
        <li><strong>Irreducible:</strong> All states communicate (can reach any state from any other state in finite time)</li>
        <li><strong>Aperiodic:</strong> No state has a period $> 1$ (not cycling in a fixed pattern)</li>
        </ol>

        <p>If both conditions hold, then:</p>
        <pre class='code-block'>1. A unique steady-state $\\boldsymbol{\\pi}^*$ exists
2. $\\lim_{n \\to \\infty} \\boldsymbol{\\pi}^{(n)} = \\boldsymbol{\\pi}^*$ (regardless of initial distribution $\\boldsymbol{\\pi}^{(0)}$)
3. $\\lim_{n \\to \\infty} P^n$ = matrix with all rows equal to $\\boldsymbol{\\pi}^*$</pre>

        <div class="worked-example">
        <p><strong>Example: Weather Chain</strong></p>
        <pre class='code-block'>$$P = \\begin{bmatrix} 0.7 & 0.2 & 0.1 \\\\ 0.3 & 0.4 & 0.3 \\\\ 0.2 & 0.3 & 0.5 \\end{bmatrix}$$

This chain is irreducible (all states communicate) and aperiodic.
Unique steady-state $\\boldsymbol{\\pi}^* \\approx [0.418, 0.285, 0.297]$

Starting from $[1, 0, 0]$ (sunny):
$\\boldsymbol{\\pi}^{(1)} \\approx [0.7, 0.2, 0.1]$
$\\boldsymbol{\\pi}^{(2)} \\approx [0.57, 0.25, 0.18]$
$\\boldsymbol{\\pi}^{(3)} \\approx [0.511, 0.272, 0.217]$
...
$\\lim_{n \\to \\infty} \\boldsymbol{\\pi}^{(n)} \\to [0.418, 0.285, 0.297]$

No matter the starting weather, the long-run distribution is the same!</pre>
        </div>

        <div class="success-box">
        <p><strong>Interpretation:</strong> In the long run, the chain "forgets" its initial state and settles into a steady state. The proportion of time spent in each state is given by $\\boldsymbol{\\pi}^*$.</p>
        </div>
        """
    },
    {
        "title": "Computation and Applications",
        "body": """
        <p><strong>How to Compute $\\boldsymbol{\\pi}^*$:</strong> Solve the system:</p>
        <p>$$\\boldsymbol{\\pi}^* P = \\boldsymbol{\\pi}^* \\quad \\text{(equivalently: } \\boldsymbol{\\pi}^* (P^T - I) = \\mathbf{0}\\text{)}$$</p>
        <p>$$\\sum_i \\pi^*_i = 1$$</p>

        <p>This is a system of linear equations. Computationally, it's often more stable to solve:</p>
        <p>$$(P^T - I)\\boldsymbol{\\pi}^* = \\mathbf{0} \\quad \\text{with normalization constraint}$$</p>

        <div class="worked-example">
        <p><strong>Example: Computing for 2-State Chain</strong></p>
        <pre class='code-block'>$$P = \\begin{bmatrix} 0.6 & 0.4 \\\\ 0.3 & 0.7 \\end{bmatrix}$$

$\\boldsymbol{\\pi}^* P = \\boldsymbol{\\pi}^*$ gives:
$\\pi^*_1 \\cdot 0.6 + \\pi^*_2 \\cdot 0.3 = \\pi^*_1$
$\\pi^*_1 \\cdot 0.4 + \\pi^*_2 \\cdot 0.7 = \\pi^*_2$

Rearranging:
$-0.4\\pi^*_1 + 0.3\\pi^*_2 = 0 \\to \\pi^*_2 = \\frac{4}{3}\\pi^*_1$
$0.4\\pi^*_1 - 0.3\\pi^*_2 = 0$ (redundant)

With $\\pi^*_1 + \\pi^*_2 = 1$:
$\\pi^*_1 + \\frac{4}{3}\\pi^*_1 = 1 \\to \\pi^*_1 = 3/7$, $\\pi^*_2 = 4/7$</pre>
        </div>

        <p><strong>Application: Expected Returns to a State</strong></p>
        <p>The expected time to return to state $i$ starting from state $i$ is:</p>
        <p>$$E[\\text{return time to } i] = \\frac{1}{\\pi^*_i}$$</p>

        <p>For the 2-state example: $E[\\text{return to state 1}] = 7/3 \\approx 2.33$ steps on average.</p>

        <p><strong>First Passage Time:</strong> Expected time to reach state $j$ starting from state $i$ ($i \\neq j$) is found by solving a system of linear equations:</p>
        <p>$$\\tau_{ij} = 1 + \\sum_k P_{ik} \\tau_{kj} \\quad \\text{(for } i \\neq j\\text{)}$$</p>
        <p>$$\\tau_{jj} = 0$$</p>

        <div class="warning-box">
        <p><strong>Note:</strong> These formulas assume an ergodic chain. Chains with absorbing states or reducibility have different behavior.</p>
        </div>
        """
    }
]
