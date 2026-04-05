TITLE = "Attention Mechanisms in Seq2Seq"

SECTIONS = [
    {
        "id": "attention_motivation",
        "title": "Attention: Solving the Bottleneck",
        "body": "<p>The fixed context vector \\(c = h_T\\) loses information from early encoder states. Attention computes a weighted sum of all encoder hidden states, allowing the decoder to focus on relevant parts of the input.</p><p>At decoder step \\(t\\), compute: \\(c_t = \\sum_{i=1}^{T} \\alpha_{ti} h_i\\)</p><p>where \\(\\alpha_{ti}\\) are learned attention weights that sum to 1.</p>"
    },
    {
        "id": "attention_computation",
        "title": "Attention Mechanisms: Dot-Product and Additive",
        "body": "<p>Dot-product (multiplicative) attention: \\(\\alpha_{ti} = \\text{softmax}_i(s_t^T h_i / \\sqrt{d})\\) where \\(s_t\\) is the decoder state and \\(d\\) is the dimension. Scaling by \\(1/\\sqrt{d}\\) stabilizes gradients.</p><p>Additive (Bahdanau) attention: \\(\\alpha_{ti} = \\text{softmax}_i(v^T \\tanh(W_1 s_t + W_2 h_i))\\) where \\(v, W_1, W_2\\) are learned parameters.</p><p>Dot-product is more efficient; additive is more flexible but slower.</p>"
    },
    {
        "id": "multi_head_attention",
        "title": "Multi-Head Attention",
        "body": "<p>Instead of one attention mechanism, use multiple attention heads in parallel. Each head learns different weighted combinations of encoder states.</p><p>Head \\(i\\): \\(c_t^{(i)} = \\sum_{j} \\alpha_{tj}^{(i)} h_j\\)</p><p>Concatenate and project: \\(c_t = W(c_t^{(1)} \\oplus c_t^{(2)} \\oplus \\ldots \\oplus c_t^{(K)})\\)</p><p>This enables richer, multi-faceted representations of input relevance.</p>"
    },
    {
        "id": "attention_applications",
        "title": "Attention Across Architectures",
        "body": "<p>Attention has become fundamental in modern NLP. Transformer models use self-attention (queries, keys, values from the same sequence) and cross-attention (queries from decoder, keys/values from encoder).</p><p>Self-attention computes: \\(\\text{Attention}(Q, K, V) = \\text{softmax}(QK^T / \\sqrt{d_k})V\\)</p><p>Attention mechanisms are now applied in vision, speech, and multimodal models, far beyond the original seq2seq setting.</p>"
    }
]
