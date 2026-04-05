TITLE = "Classification of States"

SECTIONS = [
    {
        "title": "Transient and Recurrent States",
        "body": """
        <div class="concept-box">
        <p><strong>Transient State:</strong> A state $i$ is transient if there's a positive probability of leaving and never returning.</p>
        <p><strong>Recurrent State:</strong> A state $i$ is recurrent if, starting from $i$, the chain will return to $i$ with probability 1.</p>
        </div>

        <p><strong>Formal Definitions:</strong> Let $f_i = P(X_n = i \\text{ for some } n \\geq 1 \\mid X_0 = i)$ be the probability of ever returning to state $i$.</p>
        <ul>
        <li>State $i$ is <strong>recurrent</strong> if $f_i = 1$</li>
        <li>State $i$ is <strong>transient</strong> if $f_i < 1$</li>
        </ul>

        <p><strong>Key Criterion:</strong> State $i$ is recurrent iff $\\sum_{n=1}^{\\infty} P^n_{ii} = \\infty$ (infinite expected visits).</p>

        <p>State $i$ is transient iff $\\sum_{n=1}^{\\infty} P^n_{ii} < \\infty$ (finite expected visits).</p>

        <div class="worked-example">
        <p><strong>Example: Simple Transient Chain</strong></p>
        <pre class='code-block'>$$P = \\begin{bmatrix} 1 & 0 \\\\ 0.5 & 0.5 \\end{bmatrix}$$

State 0: $P_{00} = 1$, so once in state 0, never leave. Recurrent.
State 1: $P^1_{11} = 0.5$, $P^2_{11} = 0.5 \\cdot 0.5 = 0.25$, $P^3_{11} = 0.125$, ...
         Sum $= 0.5 + 0.25 + 0.125 + \\cdots = 1$ (finite)
         State 1 is transient.</pre>
        </div>

        <div class="warning-box">
        <p><strong>Intuition:</strong> If you leave a transient state, you won't come back (eventually). Transient states represent "temporary" behaviors; recurrent states represent "permanent" ones.</p>
        </div>
        """
    },
    {
        "title": "Absorbing States and the Fundamental Matrix",
        "body": """
        <div class="concept-box">
        <p><strong>Absorbing State:</strong> A state $i$ where $P_{ii} = 1$ (once entered, never leaves). A special case of recurrent states.</p>
        </div>

        <p><strong>Absorbing Chain:</strong> A Markov chain with at least one absorbing state, and from every state, absorption eventually occurs with probability 1.</p>

        <p><strong>Canonical Form:</strong> Rearrange states so absorbing states come first. The transition matrix becomes:</p>
        <p>$$P = \\begin{bmatrix} I & 0 \\\\ R & Q \\end{bmatrix}$$</p>
        <p>where: $I$ = identity matrix (absorbing states), $0$ = zero matrix, $R$ = transitions from transient to absorbing states, $Q$ = transitions among transient states.</p>

        <p><strong>Fundamental Matrix:</strong> $N = (I - Q)^{-1}$</p>

        <p>$N_{ij}$ = expected number of visits to transient state $j$ before absorption, starting from transient state $i$.</p>

        <div class="worked-example">
        <p><strong>Example: Gambler's Ruin (Simple)</strong></p>
        <pre class='code-block'>States: $0$ (ruin), $1, 2, \\ldots, N$ (wealth), $N+1$ (rich)
Absorbing: $0$ and $N+1$
Transient: $1, 2, \\ldots, N$

From state $i$ ($1 \\leq i \\leq N$): move to $i+1$ with prob $p$, to $i-1$ with prob $1-p$

Absorption probabilities:
- If $p = 0.5$ (fair): $P(\\text{reach } N+1 \\mid \\text{start at } i) = i/(N+1)$
- If $p < 0.5$ (unfavorable): lower probability of wealth
- If $p > 0.5$ (favorable): higher probability of wealth</pre>
        </div>

        <p><strong>Absorption Probabilities:</strong> The matrix $B = NR$ gives the probability of being absorbed into each absorbing state, starting from each transient state.</p>

        <p><strong>Mean Time to Absorption:</strong> $\\mathbf{t} = N \\cdot \\mathbf{1}$, where $\\mathbf{1}$ is the vector of ones. $t_i$ = expected steps until absorption starting from transient state $i$.</p>
        """
    },
    {
        "title": "Communication and Irreducibility",
        "body": """
        <p><strong>State $i$ communicates with state $j$</strong> (written $i \\leftrightarrow j$) if:</p>
        <ul>
        <li>You can go from $i$ to $j$ in some number of steps ($j$ is accessible from $i$), AND</li>
        <li>You can go from $j$ to $i$ in some number of steps ($i$ is accessible from $j$)</li>
        </ul>

        <p>$$i \\leftrightarrow j \\iff \\exists\\, m, n : P^m_{ij} > 0 \\text{ and } P^n_{ji} > 0$$</p>

        <p><strong>Communicating Class:</strong> A maximal set of states that all communicate with each other.</p>

        <p><strong>Irreducible Chain:</strong> A chain where all states form a single communicating class (all states communicate with each other).</p>

        <div class="worked-example">
        <p><strong>Example: Chain with Multiple Classes</strong></p>
        <pre class='code-block'>Transition matrix:
$$\\begin{array}{c|cccc} & 1 & 2 & 3 & 4 \\\\ \\hline 1 & 0.5 & 0.5 & 0 & 0 \\\\ 2 & 0.5 & 0.5 & 0 & 0 \\\\ 3 & 0 & 0 & 0.7 & 0.3 \\\\ 4 & 0 & 0 & 0.3 & 0.7 \\end{array}$$

States $\\{1, 2\\}$ form one class (they communicate).
States $\\{3, 4\\}$ form another class.
Class $\\{1,2\\}$ and Class $\\{3,4\\}$ do not communicate.
Chain is reducible; NOT irreducible.</pre>
        </div>

        <p><strong>Periodicity:</strong> State $i$ has period $d$ if the only returns to $i$ occur at multiples of $d$ steps:</p>
        <p>$$d = \\gcd\\{n \\geq 1 : P^n_{ii} > 0\\}$$</p>

        <p>A state with period 1 is <strong>aperiodic</strong>. If the chain is irreducible and any state is aperiodic, all states are aperiodic.</p>

        <div class="success-box">
        <p><strong>Key Result:</strong> An irreducible, aperiodic, finite-state Markov chain is <strong>ergodic</strong>. It has a unique steady-state, and the chain converges to it regardless of initial state.</p>
        </div>
        """
    }
]
