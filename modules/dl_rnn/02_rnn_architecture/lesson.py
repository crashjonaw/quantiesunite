TITLE = "RNN Architecture: Hidden State Mechanics"

SECTIONS = [
    {
        "id": "rnn_update_eq",
        "title": "The Recurrent Unit: Hidden State Update",
        "body": """
        <p >At each time step \\(t\\), the hidden state is computed from previous state and current input:</p>
        <div class="concept-box">
            <p class="concept-box">
            $$h_t = \\sigma(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$$
            </p>
        </div>
        <p ><strong>Components:</strong></p>
        <ul >
            <li>\\(W_{hh}\\): hidden-to-hidden weight matrix (recursion)</li>
            <li>\\(W_{xh}\\): input-to-hidden weight matrix</li>
            <li>\\(\\sigma\\): activation (tanh, ReLU)</li>
        </ul>
        """
    },
    {
        "id": "rnn_output",
        "title": "Output Computation",
        "body": """
        <p >After updating hidden state, compute output for current step:</p>
        <div class="concept-box">
            <p class="concept-box">
            $$y_t = W_{hy} h_t + b_y$$
            </p>
        </div>
        <p >Apply softmax for classification or other output layers for regression.</p>
        """
    },
    {
        "id": "rnn_unrolling",
        "title": "Unrolling Through Time",
        "body": """
        <div class="worked-example">
            <p style="font-weight: bold">Conceptual View</p>
            <p >Treat RNN as chain of copies of same cell. At step 1, 2, ..., T:</p>
            <p >\\(h_1 \\to h_2 \\to h_3 \\to \\cdots \\to h_T\\)</p>
            <p >This "unrolled" view reveals how information flows and where gradients must travel during learning.</p>
        </div>
        """
    },
    {
        "id": "rnn_init_state",
        "title": "Initial Hidden State",
        "body": """
        <p >Before the sequence begins, initialize \\(h_0\\) (usually zeros or learned):</p>
        <p >$$h_0 = \\mathbf{0}$$ or \\(h_0 \\sim \\mathcal{N}(0, \\sigma^2)\\)</p>
        <div class="success-box">
            <p class="concept-box">
            Clean slate: no prior information fed forward until first input arrives.
            </p>
        </div>
        """
    }
]
