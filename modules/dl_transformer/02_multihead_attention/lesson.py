TITLE = "Multi-Head Self-Attention"

SECTIONS = [
    {
        "id": "tf_scaling",
        "title": "Scaled Dot-Product Attention",
        "body": '<p>The foundation of all Transformer attention is scaled dot-product attention:</p><p>$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$$</p><p>Breaking this down: compute similarity between queries and keys, apply softmax to get weights, aggregate values.</p><p><strong>Scaling factor:</strong> dividing by $$\\sqrt{d_k}$$ prevents the dot products from growing too large, which would compress gradients through the softmax.</p>'
    },
    {
        "id": "tf_multihead",
        "title": "Multiple Representation Subspaces",
        "body": '<p>Instead of one attention head, Transformers use multiple heads in parallel. Each head learns to attend to different aspects of the sequence:</p><p>$$\\text{MultiHead}(Q, K, V) = \\text{Concat}(\\text{head}_1, ..., \\text{head}_h)W^O$$</p><p>Where each head is: $$\\text{head}_i = \\text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$</p><p>Typical configurations use 8 or 12 heads with $$d_{model} = 512$$ or $$d_{model} = 768$$, giving $$d_k = 64$$ or $$d_k = 64$$ per head.</p>'
    },
    {
        "id": "tf_attention_patterns",
        "title": "What Attention Learns",
        "body": '<p>Different heads capture different linguistic and structural relationships:</p><ul><li><strong>Local attention:</strong> some heads focus on neighboring tokens</li><li><strong>Long-range dependencies:</strong> other heads connect distant parts of the sequence</li><li><strong>Structural roles:</strong> heads may identify grammatical relationships or semantic roles</li></ul><p>The model learns to distribute these responsibilities across heads without explicit instruction.</p>'
    },
    {
        "id": "tf_self_vs_cross",
        "title": "Self-Attention vs Cross-Attention",
        "body": '<p><strong>Self-attention:</strong> Q, K, V all come from the same sequence. Each token attends to all tokens in that sequence. Used in both encoder and decoder.</p><p><strong>Cross-attention:</strong> Q comes from the decoder, K and V come from encoder outputs. Allows decoder to attend to relevant encoder positions while generating output.</p>'
    }
]
