SECTIONS = [
    {
        "title": "Understanding AND vs OR in Inequalities",
        "body": "<h3>Two Types of Logical Connections</h3><p>When we have multiple inequality conditions, they are connected by AND or OR. The meaning is very different:</p><ul><li><strong>AND</strong> (∩ intersection): Both conditions MUST be true simultaneously. The solution is the OVERLAP.</li><li><strong>OR</strong> (∪ union): At least ONE condition must be true. The solution is BOTH regions combined.</li></ul><div class='example-box'><h4>Section 1 Example: AND vs OR</h4><p><strong>AND:</strong> \\(x > 2\\) AND \\(x < 5\\) means 2 < x < 5 (the overlap)</p><p><strong>OR:</strong> \\(x < 2\\) OR \\(x > 5\\) means all x outside [2,5] (two separate regions)</p><p>Notice: AND typically gives a bounded region (from a to b), while OR typically gives unbounded regions (to ∞ on one or both sides)</p></div>"
    },
    {
        "title": "Solving AND Inequalities: Compound Form",
        "body": "<h3>Chained Inequalities (AND in the Middle)</h3><p>A chained inequality like \\(-3 < 2x + 1 \\leq 7\\) is shorthand for two ANDed inequalities:</p><p>\\(-3 < 2x + 1\\) AND \\(2x + 1 \\leq 7\\)</p><p><strong>Solution Strategy:</strong> Perform the same operation on all three parts to isolate x.</p><div class='example-box'><h4>Section 2 Example: Solving a Chained Inequality</h4><p>Solve \\(-3 \\leq 2x + 1 < 5\\)</p><p>Subtract 1 from all parts: \\(-4 \\leq 2x < 4\\)</p><p>Divide all parts by 2: \\(-2 \\leq x < 2\\)</p><p>Solution: \\(x \\in [-2, 2)\\) or all x from -2 to 2 (including -2, excluding 2)</p></div><p><strong>Key insight:</strong> Treat the compound inequality as a single unit. Whatever you do to one part, do to all parts. If multiplying/dividing by negative, reverse ALL inequality signs.</p>"
    },
    {
        "title": "Solving OR Inequalities: Union of Regions",
        "body": "<h3>When Conditions Cannot Both Be True</h3><p>Some inequalities have OR because both conditions cannot be true at the same time. For example, you cannot have x < 2 AND x > 5 simultaneously.</p><p>\\(x < 2\\) OR \\(x > 5\\) describes two separate, disconnected regions.</p><div class='example-box'><h4>Section 3 Example: Solving with Absolute Value Leading to OR</h4><p>Solve \\(|x - 3| > 2\\)</p><p>This means: \\(x - 3 > 2\\) OR \\(x - 3 < -2\\)</p><p>Simplify: \\(x > 5\\) OR \\(x < 1\\)</p><p>Solution: \\((-\\infty, 1) \\cup (5, \\infty)\\) (two separate rays)</p></div><p>When writing OR solutions in interval notation, use the union symbol \\(\\cup\\) to show you're combining two separate regions.</p>"
    },
    {
        "title": "Integer Solutions and Applications",
        "body": "<h3>Finding Which Whole Numbers Satisfy an Inequality</h3><p>Often we need the solution as a list of integers rather than a continuous interval.</p><p><strong>Method:</strong> Solve the inequality to get an interval, then list all integers within that interval.</p><div class='example-box'><h4>Section 4 Example: Finding Integer Solutions</h4><p>Solve \\(2x - 1 < 9\\) and find all integer solutions</p><p>\\(2x < 10\\) (add 1)</p><p>\\(x < 5\\) (divide by 2)</p><p>Interval: \\((-\\infty, 5)\\)</p><p>Integer solutions: \\(\\{..., -2, -1, 0, 1, 2, 3, 4\\}\\) (all integers less than 5)</p><p>For a bounded example: If \\(1 \\leq x < 4\\), the integer solutions are {1, 2, 3}</p></div><p><strong>Real-world context:</strong> A recipe needs at least 2 cups of flour but less than 5 cups. If we measure in whole cups, the integer solutions are {2, 3, 4}.</p>"
    }
]
