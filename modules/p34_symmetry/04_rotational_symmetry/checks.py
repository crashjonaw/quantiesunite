CHECKS = [
    {
        "q": "If a shape has rotational symmetry of order 4, how many times does it look the same when rotating 360\u00b0?",
        "hint": "Order 4 means it looks identical 4 times during a full rotation. Examples: square, regular 4-pointed star.",
        "options": [
            {"text": "5", "correct": False},
            {"text": "4 times (at 90\u00b0, 180\u00b0, 270\u00b0, and 360\u00b0)", "correct": True},
            {"text": "3", "correct": False},
            {"text": "8", "correct": False},
        ]
    },
    {
        "q": "Does a rectangle have rotational symmetry? If so, what is its order?",
        "hint": "A rectangle only looks the same after rotating 180\u00b0 (half turn). A square would look the same at 90\u00b0, but rectangles are longer on one side.",
        "options": [
            {"text": "Yes, order 4, because a rectangle has 4 sides", "correct": False},
            {"text": "Yes, order 2 (it looks the same at 180\u00b0 and 360\u00b0, but not at 90\u00b0)", "correct": True},
            {"text": "No, only squares have rotational symmetry", "correct": False},
            {"text": "Yes, order 1, because it only looks the same after a full turn", "correct": False},
        ]
    },
    {
        "q": "An equilateral triangle has rotational symmetry of order 3. What angle must you rotate it to see an identical shape?",
        "hint": "To find the rotation angle, divide 360\u00b0 by the order. Order 3 means 360\u00b0 \u00f7 3 = 120\u00b0.",
        "options": [
            {"text": "120\u00b0 (360\u00b0 \u00f7 3 = 120\u00b0)", "correct": True},
            {"text": "90\u00b0 (360\u00b0 \u00f7 4 = 90\u00b0)", "correct": False},
            {"text": "180\u00b0 (360\u00b0 \u00f7 2 = 180\u00b0)", "correct": False},
            {"text": "60\u00b0 (360\u00b0 \u00f7 6 = 60\u00b0)", "correct": False},
        ]
    },
]
