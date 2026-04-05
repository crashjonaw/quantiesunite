TITLE = "Training RNNs: Backpropagation Through Time (BPTT)"

SECTIONS = [
    {
        "id": "bptt_motivation",
        "title": "Why Standard Backprop Fails for RNNs",
        "body": """
        <p >Standard backprop assumes feedforward flow. RNNs have <strong>cycles</strong> (hidden state recursion).</p>
        <p >Solution: "Unroll" the RNN in time, treat as deep feedforward network, then apply backprop.</p>
        <div class="concept-box">
            <p class="concept-box">
            BPTT "unfolds" the recurrence to compute gradients across all T time steps.
            </p>
        </div>
        """
    },
    {
        "id": "bptt_chain_rule",
        "title": "The Chain Rule Across Time",
        "body": """
        <p >Gradient for hidden state at step \\(t\\) depends on loss at \\(t\\) and loss at \\(t+1\\):</p>
        <div class="worked-example">
            <p class="concept-box">
            $$\\frac{\\partial L}{\\partial h_t} = \\frac{\\partial L}{\\partial y_t} \\frac{\\partial y_t}{\\partial h_t} + \\frac{\\partial L}{\\partial h_{t+1}} \\frac{\\partial h_{t+1}}{\\partial h_t}$$
            </p>
            <p >Error from output + error propagated backwards from next step.</p>
        </div>
        """
    },
    {
        "id": "bptt_weight_gradients",
        "title": "Weight Updates via Truncated BPTT",
        "body": """
        <p >Computing \\(\\frac{\\partial L}{\\partial W_{hh}}\\) requires summing over all steps where \\(W_{hh}\\) is used:</p>
        <div class="concept-box">
            <p class="concept-box">
            $$\\frac{\\partial L}{\\partial W_{hh}} = \\sum_{t=1}^{T} \\frac{\\partial L}{\\partial h_t} \\frac{\\partial h_t}{\\partial W_{hh}}$$
            </p>
            <p ><strong>In practice:</strong> Truncate at sequence chunks (e.g., 35 steps) to reduce memory and computation.</p>
        </div>
        """
    },
    {
        "id": "bptt_practical",
        "title": "Practical BPTT Implementation",
        "body": """
        <ol >
            <li><strong>Forward Pass:</strong> Process sequence, store all \\(h_t\\) and \\(x_t\\)</li>
            <li><strong>Loss Computation:</strong> Compare \\(y_t\\) with targets, aggregate loss</li>
            <li><strong>Backward Pass:</strong> Propagate \\(\\frac{\\partial L}{\\partial h_t}\\) backwards through time</li>
            <li><strong>Gradient Clipping:</strong> Prevent exploding gradients (more on this later)</li>
            <li><strong>Weight Update:</strong> Apply SGD, Adam, RMSprop</li>
        </ol>
        <div class="success-box">
            <p class="concept-box">
            Modern frameworks (PyTorch, TensorFlow) handle BPTT automatically.
            </p>
        </div>
        """
    }
]
