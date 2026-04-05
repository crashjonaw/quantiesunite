TITLE = "Collecting and Organizing Data"

SECTIONS = [
    {
        "title": "What is Data?",
        "body": """<h3>What is Data?</h3>

<p>Data is a collection of information or facts. It can be numbers, measurements, observations, or descriptions.</p>

<div class='concept-box'>
<p><strong>Examples of data:</strong></p>
<ul>
<li>Test scores (92, 87, 95, ...)</li>
<li>Heights of students (150 cm, 155 cm, 160 cm, ...)</li>
<li>Temperatures throughout the week (20°C, 22°C, 25°C, ...)</li>
<li>Favorite fruits (Apple, Banana, Mango, Orange, ...)</li>
<li>Number of books read per month (5, 7, 3, 8, ...)</li>
</ul>
</div>

<h3>Two Types of Data</h3>

<div class='worked-example'>
<p><strong>Quantitative Data:</strong> Numbers that can be measured or counted</p>
<ul>
<li>Ages: 11, 12, 10, 11, 13 years old</li>
<li>Test scores: 85, 92, 78, 88 marks</li>
<li>Heights: 145, 152, 148, 155 cm</li>
</ul>
</div>

<div class='worked-example'>
<p><strong>Qualitative Data:</strong> Categories or descriptions</p>
<ul>
<li>Favorite colors: Red, Blue, Green, Yellow</li>
<li>Pet types: Dog, Cat, Bird, Fish</li>
<li>Favorite sports: Football, Cricket, Tennis, Swimming</li>
</ul>
</div>

<p><strong>Key idea:</strong> Quantitative data answers "how many?" or "how much?" Qualitative data answers "what kind?"</p>"""
    },
    {
        "title": "Collecting Data: Surveys and Tallies",
        "body": """<h3>How to Collect Data</h3>

<p>Before we can organize data, we must collect it. The most common method is a <strong>survey</strong>—asking people questions and recording their responses.</p>

<div class='concept-box'>
<p><strong>Example: Favorite Fruits Survey</strong></p>
<p>Question: "What is your favorite fruit?"</p>
<p>We ask 30 classmates and get these answers (in order):</p>
<p style="font-size: 0.9em; word-wrap: break-word;">Apple, Banana, Mango, Apple, Banana, Apple, Orange, Banana, Mango, Apple, Banana, Apple, Mango, Apple, Banana, Orange, Apple, Banana, Mango, Apple, Banana, Apple, Orange, Apple, Banana, Mango, Apple, Banana, Orange, Apple</p>
<p><strong>30 answers. Staring at this list is confusing!</strong> We need to organize it.</p>
</div>

<h3>Tally Marks: The First Step to Organization</h3>

<p>A <strong>tally mark</strong> (|) represents one count. We group tally marks in fives: |||| (4 marks) and then cross with a diagonal line: ⁄ (5th mark). This makes counting easier.</p>

<div class='worked-example'>
<p><strong>Tally chart for the fruit survey:</strong></p>
<table border="1" cellpadding="8">
<tr><th>Fruit</th><th>Tally Marks</th><th>Count</th></tr>
<tr><td>Apple</td><td>|||| |||| |||| | </td><td>11</td></tr>
<tr><td>Banana</td><td>|||| |||| |</td><td>10</td></tr>
<tr><td>Mango</td><td>|||| |||</td><td>6</td></tr>
<tr><td>Orange</td><td>|||</td><td>3</td></tr>
</table>
<p><strong>Total: 11 + 10 + 6 + 3 = 30 ✓</strong></p>
</div>

<p><strong>Why tally marks?</strong> They help us count quickly without mistakes. When we see 5 tally marks bundled together, we instantly know it's 5.</p>"""
    },
    {
        "title": "Frequency Tables: Organizing Data Clearly",
        "body": """<h3>What is a Frequency Table?</h3>

<p>A <strong>frequency table</strong> (or frequency chart) organizes data in rows and columns. It shows each category and how many times (frequency) it appears.</p>

<div class='worked-example'>
<p><strong>Frequency table for the fruit survey:</strong></p>
<table border="1" cellpadding="8">
<tr><th>Fruit</th><th>Frequency</th><th>Percentage</th></tr>
<tr><td>Apple</td><td>11</td><td>\\(\\frac{11}{30} \\times 100 = 36.67\\%\\)</td></tr>
<tr><td>Banana</td><td>10</td><td>\\(\\frac{10}{30} \\times 100 = 33.33\\%\\)</td></tr>
<tr><td>Mango</td><td>6</td><td>\\(\\frac{6}{30} \\times 100 = 20\\%\\)</td></tr>
<tr><td>Orange</td><td>3</td><td>\\(\\frac{3}{30} \\times 100 = 10\\%\\)</td></tr>
<tr><td><strong>Total</strong></td><td><strong>30</strong></td><td><strong>100%</strong></td></tr>
</table>
</div>

<h3>Reading Frequency Tables</h3>

<p>From the table above, we can instantly answer questions:</p>

<div class='success-box'>
<ul>
<li><strong>What is the most popular fruit?</strong> Apple (11 votes)</li>
<li><strong>What is the least popular?</strong> Orange (3 votes)</li>
<li><strong>How many prefer Mango?</strong> 6 students = 20%</li>
<li><strong>Did most students prefer Apple or Banana?</strong> Apple (11 > 10)</li>
</ul>
</div>

<h3>Why Use Frequency Tables?</h3>

<p><strong>Before a table:</strong> "30 fruit names in a messy list—hard to see patterns."</p>

<p><strong>After a table:</strong> "Instant summary! Apple wins, Orange is least popular, exactly what fraction likes each."</p>

<p><strong>Key principle:</strong> <em>Messy data becomes clear stories through organization.</em></p>"""
    },
    {
        "title": "Calculating with Frequency Data",
        "body": """<h3>Finding Percentages from Frequency</h3>

<p>Once we have a frequency table, we can calculate what percentage each category represents.</p>

<div class='worked-example'>
<p><strong>Formula: Percentage = \\(\\frac{\\text{Frequency}}{\\text{Total}} \\times 100\\)%</strong></p>
<p>For Apple in our survey:</p>
<p>Percentage = \\(\\frac{11}{30} \\times 100 = \\frac{1100}{30} = 36.67\\%\\)</p>
</div>

<h3>Real-World Example: Class Attendance</h3>

<p>A teacher records attendance for 20 school days:</p>

<table border="1" cellpadding="8">
<tr><th>Status</th><th>Frequency</th><th>Calculation</th><th>Percentage</th></tr>
<tr><td>Present</td><td>18</td><td>\\(\\frac{18}{20} \\times 100\\)</td><td>90%</td></tr>
<tr><td>Absent</td><td>2</td><td>\\(\\frac{2}{20} \\times 100\\)</td><td>10%</td></tr>
<tr><td>Total</td><td>20</td><td></td><td>100%</td></tr>
</table>

<h3>The Power of Percentages</h3>

<div class='success-box'>
<p>Percentages let us compare groups of different sizes:</p>
<ul>
<li>In a school of 200 students: 90% = 180 students present</li>
<li>In a school of 500 students: 90% = 450 students present</li>
<li>Both have the same attendance rate, but different numbers!</li>
</ul>
</div>"""
    },
    {
        "title": "From Data to Visual: Why We Need Graphs",
        "body": """<h3>The Problem with Tables</h3>

<p>Tables are organized and show exact numbers. But can we <em>see</em> the pattern at a glance?</p>

<table border="1" cellpadding="8">
<tr><th>Fruit</th><th>Frequency</th></tr>
<tr><td>Apple</td><td>11</td></tr>
<tr><td>Banana</td><td>10</td></tr>
<tr><td>Mango</td><td>6</td></tr>
<tr><td>Orange</td><td>3</td></tr>
</table>

<p>We see "Apple has 11" but to compare all four, we must look at each number. The relationships aren't <em>visual</em>.</p>

<h3>The Power of Graphs</h3>

<p>A <strong>graph</strong> (bar chart, pie chart, line graph) shows the same data <em>visually</em> so patterns jump out instantly.</p>

<div class='concept-box'>
<canvas id="data_viz_intro" data-chart='{
  "type": "bar",
  "data": {
    "labels": ["Apple", "Banana", "Mango", "Orange"],
    "datasets": [{
      "label": "Votes",
      "data": [11, 10, 6, 3],
      "backgroundColor": ["#ef4444", "#fbbf24", "#22c55e", "#f97316"]
    }]
  },
  "options": {
    "indexAxis": "y",
    "plugins": {"title": {"display": true, "text": "Favorite Fruits (Horizontal Bar Chart)"}}
  }
}' height="200"></canvas>
</div>

<p><strong>Now it's obvious:</strong> Apple is the clear winner. Orange is far behind. This bar chart tells the story in seconds!</p>

<h3>Next Steps</h3>

<p>Now that you know how to collect and organize data with tables, the next concepts will teach you how to visualize this data with different types of graphs:</p>
<ul>
<li><strong>Bar Charts & Pictographs:</strong> Compare categories side by side</li>
<li><strong>Line Graphs:</strong> Show trends over time</li>
<li><strong>Pie Charts:</strong> Show parts of a whole (percentages)</li>
</ul>"""
    }
]
