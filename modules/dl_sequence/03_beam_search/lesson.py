TITLE = "Beam Search Decoding"

SECTIONS = [
    {
        "id": "beam_search_motivation",
        "title": "Why Beam Search? Beyond Greedy Decoding",
        "body": "<p>Greedy decoding picks the highest-probability token at each step, but this is often suboptimal for the full sequence. A low-probability token early on might enable much better tokens later.</p><p>Beam search explores multiple partial hypotheses simultaneously, keeping the top-K (beam width) candidates at each step. This trades computation for quality.</p><p>For vocabulary size \\(V\\) and beam width \\(K\\), complexity is \\(O(M \\cdot K \\cdot V)\\) versus \\(O(M \\cdot V)\\) for greedy.</p>"
    },
    {
        "id": "beam_search_algorithm",
        "title": "Beam Search Algorithm",
        "body": "<p>Initialize with beam width \\(K\\). At each step:</p><p>1. For each of the \\(K\\) active hypotheses, compute log-probabilities for all next tokens.</p><p>2. Keep the top-\\(K\\) candidates by cumulative log-probability.</p><p>3. Continue until all hypotheses end (generate EOS token) or reach maximum length.</p><p>Log-probabilities prevent numerical underflow. Length normalization prevents bias toward short sequences.</p>"
    },
    {
        "id": "length_normalization",
        "title": "Length Normalization and Tuning",
        "body": "<p>Raw log-probabilities favor shorter sequences (more negative cumulative sum). Length normalization divides cumulative score by sequence length \\(M\\):</p><p>\\(\\text{score} = \\frac{1}{M} \\sum_{t=1}^{M} \\log P(y_t | y_1, \\ldots, y_{t-1}, c)\\)</p><p>Alternatively, add a length penalty: \\(\\text{score} = \\sum_{t=1}^{M} \\log P(y_t | \\ldots) - \\alpha \\cdot M\\)</p>"
    },
    {
        "id": "sampling_alternatives",
        "title": "Sampling-Based Decoding",
        "body": "<p>Instead of selecting top-K tokens deterministically, sample from the distribution at each step. This introduces diversity and avoids mode collapse.</p><p>Temperature scaling controls randomness: \\(P(y_t) \\propto \\exp(\\log\\text{its}_t / T)\\)</p><p>Top-K sampling keeps only the \\(K\\) most likely tokens before sampling. Top-P (nucleus) sampling keeps tokens with cumulative probability up to \\(P\\).</p><p>Sampling is essential for creative tasks (poetry, music) but less suitable for deterministic ones (translation).</p>"
    }
]
