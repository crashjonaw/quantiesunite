TITLE = "Bar Charts and Pictographs"

SECTIONS = [
    {
        "title": "What is a Bar Chart?",
        "body": """<h3>What is a Bar Chart?</h3>

<p>A <strong>bar chart</strong> (or bar graph) uses rectangular bars to compare quantities across categories. The length (or height) of each bar represents the value for that category. Longer bars = larger values.</p>

<div class='concept-box'>
<p><strong>Key parts of a bar chart:</strong></p>
<ul>
<li><strong>X-axis (horizontal):</strong> Shows categories (fruits, regions, sports, etc.)</li>
<li><strong>Y-axis (vertical):</strong> Shows the scale of values (0, 5, 10, 15, 20, ...)</li>
<li><strong>Bars:</strong> One bar per category, height = frequency/value</li>
<li><strong>Title:</strong> Tells us what the chart shows</li>
</ul>
</div>

<h3>Example: Favorite Fruits Bar Chart</h3>

<p>Using data from our survey (Apple: 11, Banana: 10, Mango: 6, Orange: 3), here's the bar chart:</p>

<div class='worked-example'>
<canvas id="data_bar_fruits" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Apple", "Banana", "Mango", "Orange"],
    "datasets": [{
      "label": "Number of Votes",
      "data": [11, 10, 6, 3],
      "backgroundColor": ["#ef4444", "#fbbf24", "#22c55e", "#f97316"]
    }]
  },
  "options": {
    "plugins": {"title": {"display": true, "text": "Favorite Fruits (30 Students)"}}
  }
}' height="300"></canvas>
</div>

<p><strong>Reading the chart:</strong> The bar for Apple reaches 11 on the y-axis. Banana reaches 10. Mango reaches 6. Orange reaches 3. We instantly see Apple is most popular!</p>"""
    },
    {
        "title": "Vertical vs. Horizontal Bar Charts",
        "body": """<h3>Vertical Bar Charts (Column Charts)</h3>

<p>Bars go up and down. Categories are on the x-axis (bottom), values on the y-axis (left side).</p>

<div class='worked-example'>
<p><strong>Example: Monthly Sales</strong></p>
<canvas id="data_bar_sales_vertical" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Jan", "Feb", "Mar", "Apr", "May"],
    "datasets": [{
      "label": "Sales ($)",
      "data": [500, 650, 700, 600, 800],
      "backgroundColor": ["#3b82f6", "#3b82f6", "#3b82f6", "#3b82f6", "#3b82f6"]
    }]
  },
  "options": {
    "plugins": {"title": {"display": true, "text": "Monthly Sales"}}
  }
}' height="300"></canvas>
</div>

<h3>Horizontal Bar Charts</h3>

<p>Bars go left and right. Categories are on the y-axis (left), values on the x-axis (bottom). Useful when category names are long!</p>

<div class='worked-example'>
<p><strong>Example: Student Test Scores in Different Subjects</strong></p>
<canvas id="data_bar_scores_horizontal" data-chart='{
  "type": "bar",
  "indexAxis": "y",
  "data": {
    "labels": ["Mathematics", "English", "Science", "History", "Geography"],
    "datasets": [{
      "label": "Average Score",
      "data": [85, 78, 92, 80, 75],
      "backgroundColor": ["#8b5cf6", "#8b5cf6", "#8b5cf6", "#8b5cf6", "#8b5cf6"]
    }]
  },
  "options": {
    "plugins": {"title": {"display": true, "text": "Class Average Scores by Subject"}}
  }
}' height="300"></canvas>
</div>

<p><strong>Why use horizontal?</strong> When you have many categories or long names, horizontal bars prevent labels from overlapping or becoming hard to read.</p>"""
    },
    {
        "title": "Reading and Interpreting Bar Charts",
        "body": """<h3>Questions You Can Answer with a Bar Chart</h3>

<p><strong>Using the Favorite Fruits chart:</strong></p>

<div class='success-box'>
<p><strong>1. Which category has the highest value?</strong> Apple (tallest bar = 11)</p>
<p><strong>2. Which category has the lowest value?</strong> Orange (shortest bar = 3)</p>
<p><strong>3. What is the value for each category?</strong> Read from the y-axis where each bar reaches</p>
<p><strong>4. How much more than...?</strong> Apple (11) vs Mango (6): difference \(= 11 - 6 = 5\) more</p>
<p><strong>5. Total of all values?</strong> \(11 + 10 + 6 + 3 = 30\) votes</p>
</div>

<h3>Worked Example: Ice Cream Sales</h3>

<p><strong>A shop sold ice cream over 5 days:</strong></p>

<canvas id="data_bar_icecream" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "datasets": [{
      "label": "Cones Sold",
      "data": [24, 32, 28, 35, 30],
      "backgroundColor": ["#f472b6", "#f472b6", "#f472b6", "#f472b6", "#f472b6"]
    }]
  },
  "options": {
    "plugins": {"title": {"display": true, "text": "Ice Cream Sales (Mon-Fri)"}}
  }
}' height="300"></canvas>

<div class='worked-example'>
<p><strong>Q1: On which day were the most cones sold?</strong></p>
<p>A: Thursday (35 cones—tallest bar)</p>
<p><strong>Q2: How many more cones on Thursday than Monday?</strong></p>
<p>A: \(35 - 24 = 11\) more cones</p>
<p><strong>Q3: Total cones sold Mon-Fri?</strong></p>
<p>A: \(24 + 32 + 28 + 35 + 30 = 149\) cones</p>
<p><strong>Q4: Average (mean) cones per day?</strong></p>
<p>A: \(149 \div 5 = 29.8 \approx 30\) cones per day</p>
</div>"""
    },
    {
        "title": "Pictographs (Picture Graphs)",
        "body": """<h3>What is a Pictograph?</h3>

<p>A <strong>pictograph</strong> (or picture graph) uses small pictures or symbols to represent quantities. Instead of bars, we draw multiple identical images where each image = a fixed value.</p>

<h3>Example: Apples Harvested by 5 Friends</h3>

<div class='worked-example'>
<table border="1" cellpadding="8">
<tr><th>Person</th><th>Pictograph (🍎 = 5 apples)</th><th>Total</th></tr>
<tr><td>Ali</td><td>🍎 🍎 🍎</td><td>15 apples</td></tr>
<tr><td>Bella</td><td>🍎 🍎 🍎 🍎</td><td>20 apples</td></tr>
<tr><td>Chen</td><td>🍎 🍎</td><td>10 apples</td></tr>
<tr><td>Diego</td><td>🍎 🍎 🍎 🍎 🍎</td><td>25 apples</td></tr>
<tr><td>Emma</td><td>🍎 🍎 🍎 🍎</td><td>20 apples</td></tr>
</table>

<p><strong>Key:</strong> 🍎 = 5 apples</p>
<p><strong>Why use pictographs?</strong> Young children find pictures easier to understand than numbers or bars. The visual is intuitive!</p>
</div>

<h3>Symbols with Fractions</h3>

<p>Sometimes we need to show values that don't divide evenly into our key.</p>

<div class='worked-example'>
<p><strong>If 🍎 = 10 apples, but someone harvested 25 apples:</strong></p>
<p>We show: 🍎 🍎 🍎 ½🍎 (2.5 symbols)</p>
<p>Check: \((2 \times 10) + (0.5 \times 10) = 20 + 5 = 25\) ✓</p>
</div>

<h3>Advantage and Limitation</h3>

<div class='concept-box'>
<p><strong>Advantage:</strong> Pictographs are colorful, engaging, and fun for younger students.</p>
<p><strong>Limitation:</strong> For large numbers, you need many symbols, making the pictograph long and hard to read.</p>
</div>"""
    },
    {
        "title": "Comparing with Bar Charts and Pictographs",
        "body": """<h3>Same Data, Two Ways to Show It</h3>

<p><strong>Data: Pets owned by 20 students</strong></p>

<table border="1" cellpadding="8">
<tr><th>Pet</th><th>Frequency</th></tr>
<tr><td>Dogs</td><td>8</td></tr>
<tr><td>Cats</td><td>6</td></tr>
<tr><td>Fish</td><td>4</td></tr>
<tr><td>Birds</td><td>2</td></tr>
</table>

<h3>As a Bar Chart:</h3>

<canvas id="data_bar_pets" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Dogs", "Cats", "Fish", "Birds"],
    "datasets": [{
      "label": "Number of Students",
      "data": [8, 6, 4, 2],
      "backgroundColor": ["#8b4513", "#ff69b4", "#4169e1", "#32cd32"]
    }]
  },
  "options": {
    "plugins": {"title": {"display": true, "text": "Pets Owned by Students"}}
  }
}' height="300"></canvas>

<h3>As a Pictograph:</h3>

<div class='worked-example'>
<table border="1" cellpadding="8">
<tr><th>Pet</th><th>Pictograph (🐾 = 2 students)</th></tr>
<tr><td>Dogs</td><td>🐾 🐾 🐾 🐾</td></tr>
<tr><td>Cats</td><td>🐾 🐾 🐾</td></tr>
<tr><td>Fish</td><td>🐾 🐾</td></tr>
<tr><td>Birds</td><td>🐾</td></tr>
</table>

<p><strong>Key:</strong> 🐾 = 2 students</p>
</div>

<h3>When to Use Each</h3>

<div class='success-box'>
<p><strong>Use Bar Charts when:</strong> Comparing many categories, dealing with large numbers, or needing exact values.</p>
<p><strong>Use Pictographs when:</strong> Teaching young students, making a visually engaging display, or working with smaller numbers.</p>
</div>"""
    }
]
