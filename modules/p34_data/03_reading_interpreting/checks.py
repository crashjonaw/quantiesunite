CHECKS = [
    {
        "q": 'From a bar chart showing: Red: 10, Blue: 15, Green: 8. Which colour is most popular and which is least popular?',
        "hint": 'Look for the tallest bar and the shortest bar.',
        "options": [
            {"text": 'Most: Blue (15). Least: Green (8).', "correct": True},
            {"text": 'Most: Red (10). Least: Blue (15).', "correct": False},
            {"text": 'Most: Green (8). Least: Red (10).', "correct": False},
            {"text": 'All colors are equally popular.', "correct": False},
        ]
    },
    {
        "q": 'A bar chart shows: Soccer: 20, Tennis: 15, Basketball: 25, Running: 10. What is the total number of students surveyed?',
        "hint": 'Add all the values together to find the total.',
        "options": [
            {"text": '70 students (20 + 15 + 25 + 10 = 70)', "correct": True},
            {"text": '60 students', "correct": False},
            {"text": '50 students', "correct": False},
            {"text": '25 students (just the highest number)', "correct": False},
        ]
    },
    {
        "q": 'From the same chart, how many more students chose basketball than running?',
        "hint": 'Subtract the smaller value from the larger value.',
        "options": [
            {"text": '15 more students (25 - 10 = 15)', "correct": True},
            {"text": '5 more students (25 - 20 = 5)', "correct": False},
            {"text": '35 more students (25 + 10 = 35)', "correct": False},
            {"text": '10 more students', "correct": False},
        ]
    },
    {
        "q": 'A line graph shows temperature rising from 15°C to 28°C from morning to afternoon. What does this trend tell us?',
        "hint": 'When a line goes up, it means the value is increasing.',
        "options": [
            {"text": 'The temperature is increasing (getting warmer) during the day.', "correct": True},
            {"text": 'The temperature is decreasing (getting colder) during the day.', "correct": False},
            {"text": 'The temperature stays the same all day.', "correct": False},
            {"text": 'It is nighttime when the temperature gets warmer.', "correct": False},
        ]
    },
    {
        "q": 'If 40 out of 100 students prefer chocolate ice cream, what fraction prefer chocolate?',
        "hint": 'The number who prefer chocolate goes on top, the total goes on the bottom.',
        "options": [
            {"text": '40/100 or 2/5 (simplifying)', "correct": True},
            {"text": '100/40 (upside down)', "correct": False},
            {"text": '60/100 (the ones who do not prefer chocolate)', "correct": False},
            {"text": '40/60 (wrong total)', "correct": False},
        ]
    },
]
