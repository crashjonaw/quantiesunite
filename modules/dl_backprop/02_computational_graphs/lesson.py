TITLE = "Computational Graphs"

SECTIONS = [
    {
        "id": "graph_definition",
        "title": "What is a Computational Graph?",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">Graph Structure</h3>
    <p>A computational graph is a directed acyclic graph (DAG) where:</p>
    <ul>
        <li><strong>Nodes:</strong> Represent operations or variables (inputs, weights, intermediate values)</li>
        <li><strong>Edges:</strong> Represent data flow between operations</li>
        <li><strong>Direction:</strong> Flows from inputs toward outputs (forward pass direction)</li>
    </ul>
    <p style="font-size: 0.95em; margin-top: 12px;">Every neural network computation can be represented as a computational graph. Backpropagation traverses this graph backward to compute gradients.</p>
</div>
"""
    },
    {
        "id": "graph_example",
        "title": "Concrete Example",
        "body": """
<div class="worked-example formula-box">
    <h3 class="accent-heading">Simple Linear Layer</h3>
    <p>Consider: y = wx + b</p>
    <p><strong>Graph structure:</strong></p>
    <pre style="padding: 12px; border-radius: 4px; overflow-x: auto">
x (input)
    ↓
  [× w]  → temp1
    ↓
  [+ b]  → y (output)
</pre>
    <p style="margin-top: 12px;"><strong>Forward pass:</strong> Compute temp1 = x·w, then y = temp1 + b</p>
    <p><strong>Backward pass:</strong> Compute gradients flowing back through each operation</p>
</div>
"""
    },
    {
        "id": "multiple_paths",
        "title": "Multiple Paths and Accumulation",
        "body": """
<div class="concept-box formula-box">
    <h3 class="accent-heading">Path Convergence</h3>
    <p>When multiple computation paths converge at a node, gradients must be accumulated:</p>
    <p>$$\\frac{\\partial L}{\\partial x} = \\sum_{\\text{all paths}} \\frac{\\partial L}{\\partial y_i} \\frac{\\partial y_i}{\\partial x}$$</p>
    <p style="font-size: 0.95em; margin-top: 12px;">This is crucial for networks where variables are used in multiple places (e.g., skip connections, shared weights).</p>
</div>
"""
    },
    {
        "id": "graph_traversal",
        "title": "Graph Traversal Strategy",
        "body": """
<div class="success-box formula-box">
    <h3 class="accent-heading">Forward and Backward Traversal</h3>
    <p><strong>Forward pass:</strong> Traverse graph from inputs to outputs, computing intermediate values.</p>
    <p><strong>Backward pass:</strong> Traverse graph from output (loss) to inputs, computing gradients using chain rule.</p>
    <p style="margin-top: 12px;">The computational graph makes explicit the dependencies between variables, enabling systematic gradient computation via the chain rule.</p>
</div>
"""
    }
]
