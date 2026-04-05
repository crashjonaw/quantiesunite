TITLE = "Chain Rule Review"

SECTIONS = [
    {
        "id": "chain_rule_basics",
        "title": "Fundamental Chain Rule",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">The Chain Rule</h3>
    <p>For composite functions $f(g(x))$, the derivative is:</p>
    <p>$$\\frac{df}{dx} = \\frac{df}{dg} \\cdot \\frac{dg}{dx}$$</p>
    <p style="font-size: 0.95em; margin-top: 12px;">This is the foundation of backpropagation. We break down complex derivatives into simpler parts and multiply them together.</p>
</div>
"""
    },
    {
        "id": "chain_rule_example",
        "title": "Worked Example",
        "body": """
<div class="worked-example formula-box">
    <h3 class="accent-heading">Example: Computing $\\frac{d}{dx} \\sin(x^2)$</h3>
    <p><strong>Given:</strong> $y = \\sin(x^2)$</p>
    <p><strong>Step 1:</strong> Identify composition: $f(u) = \\sin(u)$, $g(x) = x^2$</p>
    <p><strong>Step 2:</strong> Compute individual derivatives:</p>
    <ul>
        <li>$\\frac{df}{du} = \\cos(u)$</li>
        <li>$\\frac{dg}{dx} = 2x$</li>
    </ul>
    <p><strong>Step 3:</strong> Apply chain rule:</p>
    <p>$$\\frac{dy}{dx} = \\cos(x^2) \\cdot 2x$$</p>
</div>
"""
    },
    {
        "id": "multivariate_chain_rule",
        "title": "Multivariate Chain Rule",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">Multiple Variables</h3>
    <p>When $f$ depends on multiple variables that each depend on $x$:</p>
    <p>$$\\frac{df}{dx} = \\frac{\\partial f}{\\partial u} \\frac{du}{dx} + \\frac{\\partial f}{\\partial v} \\frac{dv}{dx} + \\cdots$$</p>
    <p style="font-size: 0.95em; margin-top: 12px;">This generalizes to multiple paths in a computation graph, which we'll explore in backpropagation.</p>
</div>
"""
    },
    {
        "id": "chain_rule_intuition",
        "title": "Intuition",
        "body": """
<div class="success-box formula-box">
    <h3 class="accent-heading">Why the Chain Rule?</h3>
    <p>Imagine a chain of transformations: $x \\to g(x) \\to f(g(x))$. The chain rule tells us how a tiny change in $x$ ripples through each transformation. We compute the "rate of change" at each step, then multiply them together to get the total effect.</p>
    <p style="margin-top: 12px;">This is exactly what happens during backpropagation: errors propagate backward through the network, with derivatives multiplying at each layer.</p>
</div>
"""
    }
]
