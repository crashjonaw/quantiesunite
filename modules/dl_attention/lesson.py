SECTIONS = [
    {"id": "attn_motivation", "title": "The Bottleneck Problem in Encoder-Decoder", "content": '<p>Single context vector \\(c\\) cannot capture full source. Solution: attention computes dynamic context for each output step.</p>'},
    {"id": "attn_query_key_value", "title": "Query, Key, Value Framework", "content": '<p>Query \\(q_t\\) (what we want). Keys \\(k_i\\) (what exists). Values \\(v_i\\) (what to retrieve).</p><p>Attention: $$a_i = \\text{softmax}(q_t \\cdot k_i)$$</p><p>Output: $$c_t = \\sum_i a_i v_i$$</p>'},
    {"id": "attn_alignment", "title": "Alignment Scores and Scoring Functions", "content": '<p>Dot-product: \\(\\text{score}(q, k) = q \\cdot k\\)</p><p>Additive (Bahdanau): \\(\\text{score}(q, k) = v^T \\tanh(W[q; k])\\)</p>'},
    {"id": "attn_soft_vs_hard", "title": "Soft vs Hard Attention", "content": '<p>Soft: differentiable, all weights. Hard: sample discrete positions. Soft more common in practice.</p>'},
    {"id": "attn_visualization", "title": "Visualizing Attention Weights", "content": '<p>Attention heatmaps show which source positions attend to which target. Reveals learned alignments.</p>'},
    {"id": "attn_variants", "title": "Attention Variants: Local, Hierarchical", "content": '<p>Local attention: restrict to window. Multi-headed: multiple attention subspaces. Hierarchical: attend to coarse then fine.</p>'}
]