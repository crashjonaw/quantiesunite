CHECKS = [
    {"section": "attn_motivation", "type": "fill_blank", "question": "Attention solves the ____ bottleneck", "answer": "context"},
    {"section": "attn_query_key_value", "type": "multiple_choice", "question": "Query represents:", "options": ["Encoder state", "Decoder state/query", "Values to attend", "Alignment"], "correct": 1},
    {"section": "attn_alignment", "type": "true_false", "question": "Dot-product attention more complex than additive", "correct": False},
    {"section": "attn_soft_vs_hard", "type": "fill_blank", "question": "Soft attention is ____ (differentiable/not)", "answer": "differentiable"},
    {"section": "attn_visualization", "type": "true_false", "question": "Attention heatmap shows learned alignments", "correct": True},
    {"section": "attn_variants", "type": "fill_blank", "question": "Multi-headed attention uses ____ subspaces", "answer": "multiple"}
]