TITLE = "RNN Applications: Text, Time Series, and Beyond"

SECTIONS = [
    {
        "id": "app_language_modeling",
        "title": "Language Modeling and Generation",
        "body": """
        <p ><strong>Task:</strong> Predict next word given previous words.</p>
        <div class="worked-example">
            <p style="font-weight: bold">Example: Character-level language model</p>
            <p >Input: "Ther" → Output: "e" (predict next character)</p>
            <p >Train on large text corpus, then sample to generate new text.</p>
        </div>
        <p ><strong>Loss:</strong> Cross-entropy between predicted \\(y_t\\) and true next token.</p>
        <div class="concept-box">
            <p class="concept-box">
            RNNs allow leveraging arbitrarily long context to predict tokens.
            </p>
        </div>
        """
    },
    {
        "id": "app_machine_translation",
        "title": "Machine Translation (Sequence-to-Sequence)",
        "body": """
        <p ><strong>Architecture:</strong> Encoder-Decoder</p>
        <ul >
            <li><strong>Encoder RNN:</strong> Read input sentence, compress to final hidden state</li>
            <li><strong>Decoder RNN:</strong> Use encoder's final state as seed, generate output sentence word-by-word</li>
        </ul>
        <p >Modern variant: Transformer attention replaces bottleneck final state.</p>
        <div class="success-box">
            <p class="concept-box">
            Handles variable-length input/output naturally with RNNs.
            </p>
        </div>
        """
    },
    {
        "id": "app_sentiment_classification",
        "title": "Sentiment Classification and NLP Tasks",
        "body": """
        <p ><strong>Task:</strong> Classify entire sequence (e.g., review → positive/negative).</p>
        <div class="worked-example">
            <p style="font-weight: bold">Process:</p>
            <ol >
                <li>Feed all tokens through RNN, accumulating hidden state</li>
                <li>Take final \\(h_T\\) (captures full context)</li>
                <li>Pass \\(h_T\\) to classifier: \\(\\text{logits} = W h_T + b\\)</li>
                <li>Output: softmax over class labels</li>
            </ol>
        </div>
        <p >Variants: attend to specific tokens, use bidirectional RNNs for full context at each position.</p>
        """
    },
    {
        "id": "app_time_series",
        "title": "Time Series Forecasting",
        "body": """
        <p ><strong>Task:</strong> Predict next value(s) in temporal sequence (stocks, weather, etc.).</p>
        <div class="worked-example">
            <p style="font-weight: bold">Example: Stock price forecast</p>
            <p >Input: prices \\([p_1, p_2, \\ldots, p_T]\\) → Output: \\(p_{T+1}\\) (or \\(p_{T+k}\\))</p>
            <p >RNN hidden state captures trend, seasonality, momentum.</p>
        </div>
        <p >Multi-step forecasting: teacher forcing during training, autoregressive during inference.</p>
        <div class="concept-box">
            <p class="concept-box">
            RNNs excel at capturing temporal patterns and dependencies in real-world data.
            </p>
        </div>
        """
    }
]
