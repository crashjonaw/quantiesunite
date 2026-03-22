CHECKS = [
    {"section": "seq_language_modeling", "type": "fill_blank", "question": "Language model predicts next ____", "answer": "token"},
    {"section": "seq_machine_translation", "type": "true_false", "question": "Encoder-decoder uses shared weights between encoder and decoder", "correct": False},
    {"section": "seq_attention_context", "type": "fill_blank", "question": "Context vector is weighted sum of ____", "answer": "encoder states"},
    {"section": "seq_beam_search", "type": "true_false", "question": "Beam search with width 1 is greedy search", "correct": True},
    {"section": "seq_speech_recognition", "type": "fill_blank", "question": "Common loss for speech: ____ (Connectionist Temporal Classification)", "answer": "CTC"},
    {"section": "seq_music_generation", "type": "true_false", "question": "Temperature=0 makes generation deterministic", "correct": True}
]