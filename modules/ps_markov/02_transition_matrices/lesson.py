TITLE = "Transition Matrices"

SECTIONS = [
    {
        "title": "Definition and Properties of Transition Matrices",
        "body": """
        <div class="concept-box">
        <p><strong>Transition Matrix $P$:</strong> A matrix where entry $P_{ij}$ is the one-step transition probability from state $i$ to state $j$.</p>
        </div>

        <p><strong>Mathematical Notation:</strong> For a Markov chain with $n$ states:</p>
        <p>$$P = \\begin{bmatrix} P_{11} & P_{12} & \\cdots & P_{1n} \\\\ P_{21} & P_{22} & \\cdots & P_{2n} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ P_{n1} & P_{n2} & \\cdots & P_{nn} \\end{bmatrix}$$</p>

        <p><strong>Two Key Properties (Stochastic Matrix):</strong></p>
        <ol>
        <li>Each row sums to 1: $\\sum_j P_{ij} = 1$ (probabilities from each state sum to 1)</li>
        <li>All entries are non-negative: $P_{ij} \\geq 0$</li>
        </ol>

        <p>A matrix satisfying these properties is called <strong>stochastic</strong> or <strong>row-stochastic</strong>.</p>

        <div class="worked-example">
        <p><strong>Example: 3-State Weather Chain</strong></p>
        <pre class='code-block'>$$P = \\begin{array}{c|ccc} & S & R & C \\\\ \\hline S & 0.7 & 0.2 & 0.1 \\\\ R & 0.3 & 0.4 & 0.3 \\\\ C & 0.2 & 0.3 & 0.5 \\end{array}$$

Check: Row sums $= 0.7+0.2+0.1=1$ ✓, $0.3+0.4+0.3=1$ ✓, $0.2+0.3+0.5=1$ ✓
All entries $\\geq 0$ ✓
This is a valid transition matrix.</pre>
        </div>

        <p><strong>Interpretation:</strong></p>
        <ul>
        <li>Row $i$ represents the probabilities of transitioning FROM state $i$</li>
        <li>Column $j$ tells us what probability of transitioning TO state $j$</li>
        <li>$P_{21} = 0.3$ means: "Given it's rainy today, there's a 30% chance it's sunny tomorrow"</li>
        </ul>
        """
    },
    {
        "title": "Multi-Step Transitions and Matrix Powers",
        "body": """
        <p><strong>$n$-Step Transition Probability:</strong> What's the probability of going from state $i$ to state $j$ in exactly $n$ steps?</p>

        <p><strong>Key Result:</strong> The $n$-step transition matrix is $P^n$ ($P$ multiplied by itself $n$ times):</p>
        <p>$$P^{(n)} = P \\cdot P \\cdot \\ldots \\cdot P \\quad (n \\text{ times})$$</p>
        <p>$$P^{(n)}_{ij} = P(X_n = j \\mid X_0 = i)$$</p>

        <div class="worked-example">
        <p><strong>Computing $P^2$:</strong></p>
        <pre class='code-block'>$$P = \\begin{bmatrix} 0.7 & 0.2 & 0.1 \\\\ 0.3 & 0.4 & 0.3 \\\\ 0.2 & 0.3 & 0.5 \\end{bmatrix} \\quad P^2 = P \\cdot P$$

$(P^2)_{11} = 0.7 \\cdot 0.7 + 0.2 \\cdot 0.3 + 0.1 \\cdot 0.2 = 0.49 + 0.06 + 0.02 = 0.57$
$(P^2)_{12} = 0.7 \\cdot 0.2 + 0.2 \\cdot 0.4 + 0.1 \\cdot 0.3 = 0.14 + 0.08 + 0.03 = 0.25$
$(P^2)_{13} = 0.7 \\cdot 0.1 + 0.2 \\cdot 0.3 + 0.1 \\cdot 0.5 = 0.07 + 0.06 + 0.05 = 0.18$

$(P^2)_{11} = 0.57$ means: probability of being sunny two days from now, given sunny today.</pre>
        </div>

        <p><strong>State Distribution Evolution:</strong> If we start with a probability distribution $\\boldsymbol{\\pi}^{(0)}$ over states, the distribution after $n$ steps is:</p>
        <p>$$\\boldsymbol{\\pi}^{(n)} = \\boldsymbol{\\pi}^{(0)} P^n$$</p>

        <p><strong>Example:</strong> Start with certainty that it's sunny: $\\boldsymbol{\\pi}^{(0)} = [1, 0, 0]$</p>
        <pre class='code-block'>After 1 step: $\\boldsymbol{\\pi}^{(1)} = [1, 0, 0] \\cdot P = [0.7, 0.2, 0.1]$
After 2 steps: $\\boldsymbol{\\pi}^{(2)} = [1, 0, 0] \\cdot P^2 = [0.57, 0.25, 0.18]$</pre>
        """
    },
    {
        "title": "Computing and Interpreting Transition Matrices",
        "body": """
        <p><strong>From Data to Transition Matrix:</strong> If we observe a sequence of states, we can estimate transition probabilities using counts:</p>
        <p>$$\\hat{P}_{ij} = \\frac{\\text{\\# of transitions from } i \\text{ to } j}{\\text{total \\# of transitions from } i}$$</p>

        <div class="worked-example">
        <p><strong>Example: Estimating from Observations</strong></p>
        <pre class='code-block'>Observed sequence: $S \\to R \\to R \\to S \\to C \\to C \\to S \\to R \\to \\ldots$

Transitions from $S$: $S \\to R$ (1), $S \\to C$ (1), $S \\to R$ (1) = 3 total
  From $S$ to $R$: $2/3 \\approx 0.67$
  From $S$ to $C$: $1/3 \\approx 0.33$
  From $S$ to $S$: $0/3 = 0.00$

This gives the first row of $\\hat{P}$.</pre>
        </div>

        <div class="warning-box">
        <p><strong>Caution:</strong> Small sample sizes lead to unreliable estimates. Many transitions might be unobserved (zero probability), which may not reflect reality.</p>
        </div>

        <p><strong>Special Transition Matrices:</strong></p>
        <ul>
        <li><strong>Doubly stochastic:</strong> Columns also sum to 1. Rows and columns both sum to 1.</li>
        <li><strong>Sparse:</strong> Many entries are zero (common in applications).</li>
        <li><strong>Primitive:</strong> Some power $P^n$ has all strictly positive entries (ensures convergence to steady-state).</li>
        </ul>

        <p><strong>Key Insight:</strong> The structure of $P$ reveals the chain's behavior: where states communicate, where absorption occurs, and long-run dynamics.</p>
        """
    }
]
