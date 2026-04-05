TITLE = "Reading and Interpreting Data"
SECTIONS = [
    {
        "title": "Reading Specific Values from Charts",
        "body": """<h3>How to Find a Specific Value</h3>

<p>To find a specific value in a chart, follow these steps:</p>
<ol>
  <li><strong>Find the category</strong> you're looking for (e.g., "Monday" or "Apple")</li>
  <li><strong>Trace upward</strong> to the bar or point</li>
  <li><strong>Trace across</strong> to the scale on the side</li>
  <li><strong>Read the number</strong></li>
</ol>

<h3>Example: Reading a Line Graph</h3>

<div class="worked-example">
<p><strong>Temperature Over a Week</strong></p>

<canvas id="data_temp1" data-chart='{"type":"line","data":{"labels":["Monday","Tuesday","Wednesday","Thursday","Friday"],"datasets":[{"label":"Temperature (°C)","data":[20,22,25,23,21],"borderColor":"#ef4444","backgroundColor":"rgba(239, 68, 68, 0.1)","fill":true,"tension":0.4}]},"options":{"plugins":{"title":{"display":true,"text":"Daily Temperature"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Temperature (°C)"}}}}}' height="300"></canvas>

<p><strong>Question: What was the temperature on Wednesday?</strong></p>
<ol>
  <li>Find "Wednesday" on the horizontal axis (bottom)</li>
  <li>Look up to the point</li>
  <li>Read across to the left: 25°C</li>
</ol>

<p><strong>Answer: 25°C</strong></p>
</div>

<h3>Example: Reading a Bar Chart</h3>

<div class="worked-example">
<p><strong>Sports Equipment in the Gym</strong></p>

<canvas id="data_equipment1" data-chart='{"type":"bar","data":{"labels":["Basketballs","Footballs","Tennis Balls","Volleyballs"],"datasets":[{"label":"Number of Items","data":[15,20,30,12],"backgroundColor":["#f97316","#22c55e","#3b82f6","#8b5cf6"]}]},"options":{"plugins":{"title":{"display":true,"text":"Sports Equipment Inventory"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Items"}}}}}' height="300"></canvas>

<p><strong>Question: How many tennis balls are in the gym?</strong></p>
<ol>
  <li>Find the "Tennis Balls" bar</li>
  <li>Look up to the top of the bar</li>
  <li>Read across to the left scale: 30</li>
</ol>

<p><strong>Answer: 30 tennis balls</strong></p>
</div>

<h3>Quick Check Method</h3>

<div class="success-box">
<p><strong>Simple rule:</strong> Find the category, go to the top of its bar or point, read across to find the number.</p>
</div>
"""
    },
    {
        "title": "Comparing and Contrasting Data",
        "body": """<h3>Finding the Most and Least</h3>

<p>Charts make it easy to spot which value is highest and which is lowest.</p>

<div class="concept-box">
<ul>
  <li><strong>Highest/Most:</strong> Look for the tallest bar or highest point</li>
  <li><strong>Lowest/Least:</strong> Look for the shortest bar or lowest point</li>
</ul>
</div>

<div class="worked-example">
<p><strong>Example: Class Test Scores</strong></p>

<canvas id="data_scores1" data-chart='{"type":"bar","data":{"labels":["Ali","Bella","Chen","Diana","Evan"],"datasets":[{"label":"Test Score","data":[78,85,92,88,75],"backgroundColor":["#ef4444","#f59e0b","#22c55e","#3b82f6","#a855f7"]}]},"options":{"plugins":{"title":{"display":true,"text":"Test Scores"}},"scales":{"y":{"beginAtZero":false,"min":70,"max":100,"title":{"display":true,"text":"Score"}}}}}' height="300"></canvas>

<p><strong>Questions and Answers:</strong></p>
<ul>
  <li><strong>Who scored the highest?</strong> Chen (92) ← tallest bar</li>
  <li><strong>Who scored the lowest?</strong> Evan (75) ← shortest bar</li>
</ul>
</div>

<h3>Comparing Two Values</h3>

<p>You can use subtraction to find the <strong>difference</strong> between two values.</p>

<div class="worked-example">
<p><strong>From the test scores above:</strong></p>

<p><strong>How many more points did Chen score than Evan?</strong></p>
<p>Chen's score: 92<br>
Evan's score: 75<br>
Difference: \\(92 - 75 = 17\\) points</p>

<p><strong>Answer: Chen scored 17 more points than Evan.</strong></p>
</div>

<h3>Sorting from Highest to Lowest</h3>

<div class="worked-example">
<p><strong>Example: Books Read by Students (from a bar chart)</strong></p>
<p>Ali: 15, Bella: 22, Chen: 18, Diana: 20</p>

<p><strong>Sorted from most to least:</strong></p>
<ol>
  <li>Bella: 22</li>
  <li>Diana: 20</li>
  <li>Chen: 18</li>
  <li>Ali: 15</li>
</ol>

<p>This is useful for finding rankings!</p>
</div>
"""
    },
    {
        "title": "Finding Totals and Making Calculations",
        "body": """<h3>Calculating Totals</h3>

<p>To find the <strong>total</strong> of all values in a chart, <strong>add up all the individual values</strong>.</p>

<div class="concept-box">
<p><strong>Formula:</strong> \\(\\text{Total} = \\text{Value 1} + \\text{Value 2} + \\text{Value 3} + ...\\)</p>
</div>

<div class="worked-example">
<p><strong>Example: Ice Cream Sales</strong></p>

<canvas id="data_icecream1" data-chart='{"type":"bar","data":{"labels":["Vanilla","Chocolate","Strawberry","Mint"],"datasets":[{"label":"Number of Scoops Sold","data":[40,50,25,35],"backgroundColor":["#fbbf24","#8b4513","#fbbf24","#10b981"]}]},"options":{"plugins":{"title":{"display":true,"text":"Ice Cream Sales"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Scoops"}}}}}' height="300"></canvas>

<p><strong>Question: How many scoops of ice cream were sold in total?</strong></p>

<p>Vanilla: 40<br>
Chocolate: 50<br>
Strawberry: 25<br>
Mint: 35</p>

<p>Total: \\(40 + 50 + 25 + 35 = 150\\) scoops</p>

<p><strong>Answer: 150 scoops were sold.</strong></p>
</div>

<h3>Finding Average Values</h3>

<p>The <strong>average</strong> (or mean) is the middle value. To find the average:</p>
<ol>
  <li><strong>Add up all the values</strong> to find the total</li>
  <li><strong>Count how many values</strong> there are</li>
  <li><strong>Divide the total by the count</strong></li>
</ol>

<div class="concept-box">
<p><strong>Formula:</strong> \\(\\text{Average} = \\frac{\\text{Total}}{\\text{Number of values}}\\)</p>
</div>

<div class="worked-example">
<p><strong>From the ice cream example above:</strong></p>

<p><strong>Question: What is the average number of scoops per flavour?</strong></p>

<p>Total: 150 scoops<br>
Number of flavours: 4</p>

<p>Average: \\(\\frac{150}{4} = 37.5\\) scoops per flavour</p>

<p><strong>Answer: On average, 37.5 scoops of each flavour were sold.</strong></p>
</div>

<h3>Percent and Fractions (Introduction)</h3>

<div class="worked-example">
<p><strong>From the ice cream data:</strong></p>

<p><strong>What fraction of the total sales was chocolate?</strong></p>

<p>Chocolate: 50 scoops<br>
Total: 150 scoops</p>

<p>Fraction: \\(\\frac{50}{150} = \\frac{1}{3}\\)</p>

<p><strong>Answer: Chocolate was 1/3 of total sales.</strong></p>
</div>
"""
    },
    {
        "title": "Spotting Trends and Patterns",
        "body": """<h3>What Are Trends?</h3>

<p>A <strong>trend</strong> is how data changes over time. Line graphs are perfect for spotting trends!</p>

<h3>Types of Trends</h3>

<div class="worked-example">
<p><strong>Line going UP:</strong> The value is increasing<br>
<strong>Line going DOWN:</strong> The value is decreasing<br>
<strong>FLAT line:</strong> The value stays the same<br>
<strong>STEEP slope:</strong> Large change<br>
<strong>GENTLE slope:</strong> Small change</p>
</div>

<h3>Real-World Example: Temperature Trend</h3>

<div class="worked-example">
<p><strong>Temperature changes through the day</strong></p>

<canvas id="data_temptrend1" data-chart='{"type":"line","data":{"labels":["6am","9am","12pm","3pm","6pm","9pm"],"datasets":[{"label":"Temperature (°C)","data":[12,18,24,26,22,15],"borderColor":"#f97316","backgroundColor":"rgba(249, 115, 22, 0.1)","fill":true,"tension":0.4,"borderWidth":3}]},"options":{"plugins":{"title":{"display":true,"text":"Daily Temperature Changes"}},"scales":{"y":{"beginAtZero":false,"min":10,"max":28,"title":{"display":true,"text":"Temperature (°C)"}}}}}' height="300"></canvas>

<p><strong>What pattern do we see?</strong></p>
<ul>
  <li><strong>6am to 3pm:</strong> Temperature INCREASES (line goes up)</li>
  <li><strong>3pm to 9pm:</strong> Temperature DECREASES (line goes down)</li>
  <li><strong>Biggest change:</strong> Between 3pm and 6pm (steep downward slope)</li>
</ul>

<p><strong>Conclusion:</strong> The temperature rises in the morning/afternoon and falls in the evening.</p>
</div>

<h3>Spotting Important Changes</h3>

<div class="worked-example">
<p><strong>Example: Website Visits Over Time</strong></p>

<canvas id="data_visits1" data-chart='{"type":"line","data":{"labels":["Week 1","Week 2","Week 3","Week 4","Week 5","Week 6"],"datasets":[{"label":"Number of Visitors","data":[100,110,130,140,150,160],"borderColor":"#3b82f6","backgroundColor":"rgba(59, 130, 246, 0.1)","fill":true,"tension":0.3,"borderWidth":3}]},"options":{"plugins":{"title":{"display":true,"text":"Website Visitors Growth"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Visitors"}}}}}' height="300"></canvas>

<p><strong>Pattern:</strong> The line always goes UP. Visitors are increasing every week!</p>

<p><strong>Conclusion:</strong> The website is becoming more popular.</p>
</div>
"""
    },
    {
        "title": "Making Conclusions from Data",
        "body": """<h3>Using Data to Make Decisions</h3>

<p>Data helps us <strong>make decisions based on facts, not guesses</strong>.</p>

<div class="worked-example">
<p><strong>Example: Choosing a Class Pet</strong></p>

<canvas id="data_pet1" data-chart='{"type":"pie","data":{"labels":["Hamster","Guinea Pig","Rabbit","Fish"],"datasets":[{"data":[8,12,7,5],"backgroundColor":["#f59e0b","#ec4899","#a855f7","#3b82f6"]}]},"options":{"plugins":{"title":{"display":true,"text":"Class Pet Preference Vote"}}}}' height="300"></canvas>

<p><strong>Results:</strong> Guinea Pig: 12, Hamster: 8, Rabbit: 7, Fish: 5</p>

<p><strong>Conclusion:</strong> The class should choose a guinea pig because it got the most votes!</p>
</div>

<h3>Drawing Conclusions</h3>

<p>When making a conclusion, always:</p>
<ol>
  <li><strong>Look at the data</strong> carefully</li>
  <li><strong>Find patterns</strong> and important values</li>
  <li><strong>Use facts from the data</strong> to support your conclusion</li>
  <li><strong>Say what the data means</strong> in real life</li>
</ol>

<h3>Real-World Conclusions</h3>

<div class="worked-example">
<p><strong>Example: School Lunch Choices</strong></p>

<canvas id="data_lunch1" data-chart='{"type":"bar","data":{"labels":["Pizza","Sandwiches","Pasta","Salad","Burgers"],"datasets":[{"label":"Number of Students","data":[35,28,20,12,25],"backgroundColor":["#f97316","#22c55e","#a855f7","#06b6d4","#f59e0b"]}]},"options":{"plugins":{"title":{"display":true,"text":"Lunch Choice Survey"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Students"}}}}}' height="300"></canvas>

<p><strong>Data says:</strong> Pizza: 35, Sandwiches: 28, Pasta: 20, Salad: 12, Burgers: 25</p>

<p><strong>Conclusion:</strong> Pizza is the most popular lunch choice. The school should make pizza available more often.</p>

<p><strong>Why?</strong> The data shows 35 students chose pizza, which is more than any other choice.</p>
</div>

<h3>Avoiding Wrong Conclusions</h3>

<div class="warning-box">
<p><strong>⚠️ Incorrect:</strong> "Everyone loves pizza" (This is too strong! Not everyone chose it.)</p>

<p><strong>✓ Correct:</strong> "Most students prefer pizza to other lunch options." (This matches the data.)</p>

<p><strong>Remember:</strong> Let the data speak! Don't exaggerate or add personal opinions.</p>
</div>
"""
    }
]
