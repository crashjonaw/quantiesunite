"""
Data Representation - Lesson Content

Topics covered:
- Bar graphs
- Line graphs
- Picture graphs
- Reading and interpreting data
- Scales and axes
"""

SECTIONS = [
    {
        "title": "Understanding Data and Graphs",
        "body": """
        <h3>What is Data?</h3>
        <p>Data is <strong>information or facts</strong> that we collect. For example: heights of students, temperatures each day, favourite colours, test scores.</p>

        <h3>Why Do We Use Graphs?</h3>
        <p>Graphs help us <strong>visualize data</strong> so we can:</p>
        <ul>
            <li>See patterns and trends</li>
            <li>Compare different values easily</li>
            <li>Communicate information clearly</li>
            <li>Make predictions</li>
        </ul>

        <div class='example-box'>
            <p><strong>Example:</strong> Instead of saying "Monday: 5 customers, Tuesday: 8 customers, Wednesday: 6 customers," we can show this in a bar graph where we instantly see Tuesday had the most customers.</p>
        </div>

        <h3>Parts of a Graph</h3>
        <p>Every graph should have:</p>
        <ul>
            <li><strong>Title:</strong> Tells us what the graph shows</li>
            <li><strong>Axes:</strong> Lines with labels and numbers</li>
            <li><strong>Scale:</strong> The spacing and numbering on axes</li>
            <li><strong>Legend:</strong> Explanation of colours or symbols (if needed)</li>
            <li><strong>Data:</strong> The actual information shown</li>
        </ul>
        """
    },
    {
        "title": "Bar Graphs (Bar Charts)",
        "body": """
        <h3>What is a Bar Graph?</h3>
        <p>A bar graph uses <strong>rectangular bars</strong> to show and compare amounts. The height or length of each bar represents the value.</p>

        <div class='example-box'>
            <p><strong>Example: Favourite Fruits (Vertical Bar Graph)</strong></p>
            <p>Apple: 8 students<br>
            Banana: 6 students<br>
            Orange: 5 students<br>
            Grape: 7 students</p>
            <p>Each bar's height shows how many students chose that fruit.</p>
        </div>

        <h3>Reading a Bar Graph</h3>
        <p><strong>Step 1: Read the title</strong> to understand what the graph shows</p>
        <p><strong>Step 2: Check the scale</strong> on the axes. Count the numbers to understand spacing.</p>
        <p><strong>Step 3: Find the bar</strong> you're interested in</p>
        <p><strong>Step 4: Read the value</strong> by seeing where the top of the bar aligns with the scale</p>

        <div class='example-box'>
            <p><strong>Question: How many students chose apples?</strong><br>
            Find the Apple bar, trace to the top, see it aligns with 8 on the vertical axis.<br>
            <strong>Answer: 8 students</strong></p>
        </div>

        <h3>Horizontal vs Vertical Bar Graphs</h3>
        <div class='example-box'>
            <p><strong>Vertical bars:</strong> Categories on horizontal axis, numbers on vertical axis</p>
            <p><strong>Horizontal bars:</strong> Categories on vertical axis, numbers on horizontal axis</p>
            <p>Both show the same information, just rotated!</p>
        </div>

        <h3>Comparing Data with Bar Graphs</h3>
        <p>Bar graphs make comparison easy:</p>
        <div class='example-box'>
            <p><strong>Question: Which fruit is most popular? Least popular?</strong><br>
            <strong>Answer:</strong> Apple (tallest bar) is most popular. Orange (shortest bar) is least popular.</p>
        </div>
        """
    },
    {
        "title": "Line Graphs",
        "body": """
        <h3>What is a Line Graph?</h3>
        <p>A line graph uses <strong>points connected by lines</strong> to show how something <strong>changes over time</strong>. It's perfect for showing trends.</p>

        <div class='example-box'>
            <p><strong>Example: Temperature Over a Week</strong></p>
            <p>Monday: 20°C, Tuesday: 22°C, Wednesday: 25°C, Thursday: 23°C, Friday: 21°C</p>
            <p>A line graph shows this trend clearly—temperature went up, then down.</p>
        </div>

        <h3>Reading a Line Graph</h3>
        <p><strong>Step 1: Identify the axes</strong> - Horizontal (usually time) and Vertical (the measured value)</p>
        <p><strong>Step 2: Find a point</strong> by locating its position on both axes</p>
        <p><strong>Step 3: Read the value</strong> where the point sits on the graph</p>

        <div class='example-box'>
            <p><strong>Question: What was the temperature on Wednesday?</strong><br>
            Find Wednesday on the horizontal axis, go up to the point, read across to the vertical axis: 25°C</p>
        </div>

        <h3>Interpreting Trends</h3>
        <p>Line graphs help us see patterns:</p>
        <ul>
            <li><strong>Line going up:</strong> The value is increasing</li>
            <li><strong>Line going down:</strong> The value is decreasing</li>
            <li><strong>Flat line:</strong> The value stays the same</li>
            <li><strong>Steep slope:</strong> Large change</li>
            <li><strong>Gentle slope:</strong> Small change</li>
        </ul>

        <div class='example-box'>
            <p><strong>Question: When did temperature increase the most?</strong><br>
            Look for the steepest upward slope: Monday to Wednesday (increase of 5°C)</p>
        </div>
        """
    },
    {
        "title": "Picture Graphs (Pictographs)",
        "body": """
        <h3>What is a Picture Graph?</h3>
        <p>A picture graph uses <strong>symbols or pictures</strong> to represent data. Each symbol or picture represents a certain amount.</p>

        <div class='example-box'>
            <p><strong>Example: Books Read by Students</strong></p>
            <p>Ali: 📚📚📚 = 3 books<br>
            Bena: 📚📚📚📚 = 4 books<br>
            Chen: 📚📚 = 2 books<br>
            Diana: 📚📚📚📚📚 = 5 books</p>
            <p>Each 📚 (book symbol) represents 1 book read.</p>
        </div>

        <h3>Understanding Symbols with Different Values</h3>
        <p>Sometimes one symbol = more than 1:</p>
        <div class='example-box'>
            <p><strong>Legend: 🎾 = 10 tennis balls</strong></p>
            <p>Store A has: 🎾🎾 = 20 balls<br>
            Store B has: 🎾🎾🎾 = 30 balls<br>
            Store C has: 🎾 (half) = 5 balls</p>
            <p>You need to read the legend to understand the value!</p>
        </div>

        <h3>Reading a Picture Graph</h3>
        <p><strong>Step 1: Read the legend</strong> to see what each symbol means</p>
        <p><strong>Step 2: Count the symbols</strong> in each row or column</p>
        <p><strong>Step 3: Multiply</strong> the number of symbols by the value each symbol represents</p>

        <div class='example-box'>
            <p><strong>Question: How many books did Bena read?</strong><br>
            Count Bena's symbols: 4<br>
            Value per symbol (from legend): 1 book<br>
            Total: 4 × 1 = 4 books</p>
        </div>

        <h3>Picture Graphs Are Great For:</h3>
        <ul>
            <li>Young learners (pictures are easy to understand)</li>
            <li>Data that uses whole numbers</li>
            <li>Making comparisons visually</li>
        </ul>
        """
    },
    {
        "title": "Scales and Interpreting Complex Data",
        "body": """
        <h3>Understanding Scales</h3>
        <p>A scale is the sequence of numbers on a graph's axis. Choosing the right scale is important.</p>

        <div class='example-box'>
            <p><strong>Bad scale example:</strong> If your data goes from 0 to 100, a scale going 0, 1, 2, 3... would be tiny and hard to read.</p>
            <p><strong>Good scale:</strong> Using 0, 10, 20, 30... 100 makes the graph clear and easy to read.</p>
        </div>

        <h3>Why Scale Matters</h3>
        <p>The same data can look very different with different scales!</p>
        <div class='example-box'>
            <p><strong>Sales data:</strong> Jan: 100, Feb: 110, Mar: 120</p>
            <p>With scale 0-200: The differences look small<br>
            With scale 95-125: The differences look huge!</p>
            <p>The data is the same, but the visual impression is different!</p>
        </div>

        <h3>Extracting Information from Graphs</h3>
        <p><strong>Reading specific values:</strong> Find the point or bar, read the value</p>
        <p><strong>Comparing values:</strong> Look at which bar is taller or which point is higher</p>
        <p><strong>Finding totals:</strong> Add up all the values</p>
        <p><strong>Finding averages:</strong> Divide the total by the number of values</p>

        <div class='example-box'>
            <p><strong>Question: From a bar graph showing ice cream sales (vanilla: 40, chocolate: 35, strawberry: 25), what's the total?</strong><br>
            <strong>Answer:</strong> 40 + 35 + 25 = 100 ice cream scoops</p>
            <p><strong>Question: What's the average sales per flavour?</strong><br>
            <strong>Answer:</strong> 100 ÷ 3 = 33.3 scoops per flavour (approximately)</p>
        </div>

        <h3>Making and Interpreting Graphs</h3>
        <ul>
            <li><strong>Choose the right type:</strong> Bar graphs for comparison, line graphs for trends, picture graphs for simple data</li>
            <li><strong>Choose appropriate scale:</strong> Not too crowded, not too spread out</li>
            <li><strong>Label clearly:</strong> Title, axes, legend (if needed)</li>
            <li><strong>Read carefully:</strong> Check the scale before reading values</li>
        </ul>
        """
    }
]
