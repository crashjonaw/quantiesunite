TITLE = "Applications of Integration"

SECTIONS = [
    {
        "title": "Finding Area and Volume",
        "body": """
        <h3>Finding Area</h3>

        <div class="worked-example">
            <p><strong>Example 10:</strong> Find the area enclosed by $y = x^2 - 2x$ and the $x$-axis</p>
            <p>First, find $x$-intercepts: $x^2 - 2x = x(x - 2) = 0$, so $x = 0, 2$</p>
            <p>The parabola is below the $x$-axis between 0 and 2</p>
            <p>Area $= \\left|\\int_0^2 (x^2 - 2x)\\,dx\\right| = \\left|\\left[\\frac{x^3}{3} - x^2\\right]_0^2\\right|$</p>
            <p>$= \\left|\\frac{8}{3} - 4\\right| = \\left|-\\frac{4}{3}\\right| = \\frac{4}{3}$</p>
        </div>

        <h3>Volume of Solids of Revolution</h3>
        <p>When rotating $y = f(x)$ about the $x$-axis from $a$ to $b$:</p>

        <p>$$V = \\pi \\int_a^b [f(x)]^2\\,dx$$</p>

        <div class="worked-example">
            <p><strong>Example 11:</strong> Find the volume when $y = \\sqrt{x}$ is rotated about the $x$-axis from $x = 0$ to $x = 4$</p>
            <p>$V = \\pi \\int_0^4 (\\sqrt{x})^2\\,dx = \\pi \\int_0^4 x\\,dx$</p>
            <p>$= \\pi \\left[\\frac{x^2}{2}\\right]_0^4 = \\pi \\cdot 8 = 8\\pi$</p>
        </div>
        """
    },
    {
        "title": "Accumulated Change and Work",
        "body": """
        <h3>Accumulated Change</h3>
        <p>If we know the rate of change $f'(t)$, the total change from $t = a$ to $t = b$ is:</p>

        <p>$$\\text{Total Change} = \\int_a^b f'(t)\\,dt = f(b) - f(a)$$</p>

        <div class="worked-example">
            <p><strong>Example 12:</strong> A car's velocity is $v(t) = 3t^2$ m/s. How far does it travel from $t = 1$ to $t = 4$ seconds?</p>
            <p>Distance $= \\int_1^4 3t^2\\,dt = \\left[t^3\\right]_1^4 = 64 - 1 = 63$ m</p>
        </div>

        <h3>Work Done by a Force</h3>
        <p>Work $= \\int_a^b F(x)\\,dx$, where $F(x)$ is force at position $x$</p>

        <div class="worked-example">
            <p><strong>Example 13:</strong> A spring force is $F(x) = 5x$ N. How much work is done compressing the spring 0.2 m?</p>
            <p>Work $= \\int_0^{0.2} 5x\\,dx = \\left[\\frac{5x^2}{2}\\right]_0^{0.2} = \\frac{5(0.04)}{2} = 0.1$ J</p>
        </div>

        <div class="concept-box">
            <p><strong>Key Applications:</strong> Integration measures accumulated quantities: area, volume, distance, work, and any quantity that can be expressed as a sum of infinitesimal elements.</p>
        </div>
        """
    }
]
