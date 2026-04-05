TITLE = "Sequential Data and Motivation for RNNs"

SECTIONS = [
    {
        "id": "seq_data_nature",
        "title": "Sequential Data: Why Order Matters",
        "body": """
        <div class="concept-box">
            <p class="concept-box">
            Sequences have temporal dependencies: \\(x_1, x_2, \\ldots, x_T\\). Each element depends on previous context.
            </p>
        </div>
        <p >Examples: text (words), audio (samples), time series (stock prices), DNA (bases).</p>
        <p >Feedforward networks treat inputs independently—losing temporal structure entirely.</p>
        """
    },
    {
        "id": "seq_memory_need",
        "title": "The Need for Memory",
        "body": """
        <div class="worked-example">
            <p style="font-weight: bold">Example: Language Understanding</p>
            <p >Sentence: "The bank can issue a loan."</p>
            <p >To understand "loan," you need context from "bank" and "issue." Neural networks need <em>memory</em> of prior tokens.</p>
        </div>
        """
    },
    {
        "id": "seq_rnn_intro",
        "title": "RNNs: Storing Hidden State",
        "body": """
        <p >RNNs maintain a <strong>hidden state</strong> \\(h_t\\) that captures information from all previous time steps.</p>
        <div class="success-box">
            <p class="concept-box">
            \\(h_t\\) acts as network's "memory," updated at each time step to incorporate new input and past context.
            </p>
        </div>
        """
    },
    {
        "id": "seq_key_insight",
        "title": "Key Insight: Weight Sharing Across Time",
        "body": """
        <p >RNNs use the <strong>same weights</strong> at every time step—drastically fewer parameters than deep feedforward nets.</p>
        <p >This allows processing variable-length sequences and capturing long-range dependencies.</p>
        """
    }
]
