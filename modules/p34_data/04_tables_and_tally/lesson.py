TITLE = "Tables and Tally Marks"
SECTIONS = [
    {
        "title": "Organizing Data in Tables",
        "body": """<h3>What is a Data Table?</h3>

<p>A <strong>table</strong> is a way to organize data using <strong>rows and columns</strong>. Tables make it easy to see all your data clearly and neatly.</p>

<h3>Parts of a Table</h3>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Student Name</td>
    <td style="text-align: center; font-weight: bold;">Height (cm)</td>
    <td style="text-align: center; font-weight: bold;">Age (years)</td>
  </tr>
  <tr>
    <td>Ali</td>
    <td>135</td>
    <td>9</td>
  </tr>
  <tr>
    <td>Bella</td>
    <td>142</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Chen</td>
    <td>138</td>
    <td>9</td>
  </tr>
  <tr>
    <td>Diana</td>
    <td>145</td>
    <td>10</td>
  </tr>
</table>

<p><strong>Parts of this table:</strong></p>
<ul>
  <li><strong>Header row (top):</strong> Column titles that tell us what the data shows</li>
  <li><strong>Columns (vertical):</strong> Data organized by category (Student Name, Height, Age)</li>
  <li><strong>Rows (horizontal):</strong> Each row shows data for one person</li>
  <li><strong>Cells:</strong> Individual boxes where data goes</li>
</ul>

<h3>Advantages of Tables</h3>

<div class="concept-box">
<p>Tables are great for:</p>
<ul>
  <li>Organizing lots of data neatly</li>
  <li>Showing multiple pieces of information about each item</li>
  <li>Quick lookup of specific information</li>
  <li>Raw data before making charts</li>
</ul>
</div>

<h3>Reading a Table</h3>

<div class="worked-example">
<p><strong>Example: Weather Data Table</strong></p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Day</td>
    <td style="text-align: center; font-weight: bold;">Weather</td>
    <td style="text-align: center; font-weight: bold;">Temperature</td>
    <td style="text-align: center; font-weight: bold;">Rainfall (mm)</td>
  </tr>
  <tr>
    <td>Monday</td>
    <td>Sunny</td>
    <td>22°C</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td>Rainy</td>
    <td>18°C</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Wednesday</td>
    <td>Cloudy</td>
    <td>20°C</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Thursday</td>
    <td>Sunny</td>
    <td>24°C</td>
    <td>0</td>
  </tr>
</table>

<p><strong>Questions we can ask:</strong></p>
<ul>
  <li>What was the temperature on Tuesday? Answer: 18°C (find "Tuesday" row, read "Temperature" column)</li>
  <li>How much rainfall was there on Wednesday? Answer: 2mm</li>
  <li>Which day was the warmest? Answer: Thursday (24°C)</li>
</ul>
</div>

<h3>Creating a Table</h3>

<div class="worked-example">
<p><strong>Steps to create a table:</strong></p>
<ol>
  <li>Decide what information you need (columns)</li>
  <li>List your items or categories (rows)</li>
  <li>Write clear headers at the top</li>
  <li>Fill in data neatly and accurately</li>
</ol>

<p><strong>Example: Favourite Pet Survey</strong></p>
<p>Data collected: Ali likes cats, Bella likes dogs, Chen likes rabbits, Diana likes cats</p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Student</td>
    <td style="text-align: center; font-weight: bold;">Favourite Pet</td>
  </tr>
  <tr>
    <td>Ali</td>
    <td>Cat</td>
  </tr>
  <tr>
    <td>Bella</td>
    <td>Dog</td>
  </tr>
  <tr>
    <td>Chen</td>
    <td>Rabbit</td>
  </tr>
  <tr>
    <td>Diana</td>
    <td>Cat</td>
  </tr>
</table>

<p>Now the data is organized so we can easily see that 2 students like cats!</p>
</div>
"""
    },
    {
        "title": "Tally Marks and Tally Charts",
        "body": """<h3>Using Tally Marks</h3>

<p><strong>Tally marks</strong> (or tick marks) are a quick way to count as you collect data. They look like small lines.</p>

<h3>How to Make Tally Marks</h3>

<svg width="400" height="200" viewBox="0 0 400 200">
  <!-- Title -->
  <text x="200" y="25" font-size='16' font-weight='bold' text-anchor='middle'>How to Write Tally Marks</text>

  <!-- Single tally -->
  <text x="50" y="55" font-size='12' font-weight='bold'>One:</text>
  <line x1="40" y1="75" x2="40" y2="110" stroke='#8b949e' stroke-width="3"/>
  <text x="40" y="135" font-size='14' text-anchor='middle'>|</text>

  <!-- Two tallies -->
  <text x="150" y="55" font-size='12' font-weight='bold'>Two:</text>
  <line x1="130" y1="75" x2="130" y2="110" stroke='#8b949e' stroke-width="3"/>
  <line x1="145" y1="75" x2="145" y2="110" stroke='#8b949e' stroke-width="3"/>
  <text x="137" y="135" font-size='14' text-anchor='middle'>||</text>

  <!-- Five tallies (with diagonal) -->
  <text x="290" y="55" font-size='12' font-weight='bold'>Five:</text>
  <line x1="260" y1="75" x2="260" y2="110" stroke='#8b949e' stroke-width="3"/>
  <line x1="275" y1="75" x2="275" y2="110" stroke='#8b949e' stroke-width="3"/>
  <line x1="290" y1="75" x2="290" y2="110" stroke='#8b949e' stroke-width="3"/>
  <line x1="305" y1="75" x2="305" y2="110" stroke='#8b949e' stroke-width="3"/>
  <line x1="265" y1="80" x2="305" y2="105" stroke='#8b949e' stroke-width="3"/>
  <text x="285" y="135" font-size='14' text-anchor='middle'>||||/</text>
</svg>

<h3>Rules for Tally Marks</h3>

<div class="concept-box">
<ul>
  <li><strong>First 4:</strong> Draw 4 vertical lines: | | | |</li>
  <li><strong>Fifth mark:</strong> Draw diagonally across the 4: ||||/</li>
  <li><strong>Grouping:</strong> This creates groups of 5, which are easy to count</li>
  <li><strong>Continue:</strong> ||||/ ||||/ || means 5 + 5 + 2 = 12</li>
</ul>
</div>

<h3>Counting Tally Marks</h3>

<div class="worked-example">
<p><strong>How many items?</strong></p>

<p>||||/ ||||/ ||||/ ||</p>

<p><strong>To count:</strong></p>
<ol>
  <li>Count complete groups of 5: Three groups = \\(3 \\times 5 = 15\\)</li>
  <li>Count remaining marks: 2 marks</li>
  <li>Total: \\(15 + 2 = 17\\)</li>
</ol>

<p><strong>Answer: 17 items</strong></p>
</div>

<h3>Tally Charts</h3>

<p>A <strong>tally chart</strong> combines a table with tally marks to organize and count data as you collect it.</p>

<div class="worked-example">
<p><strong>Example: Recording Favourite Colours</strong></p>

<p>As students answer "What's your favourite colour?" we mark a tally for each answer.</p>

<table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Colour</td>
    <td style="text-align: center; font-weight: bold;">Tally Marks</td>
    <td style="text-align: center; font-weight: bold;">Total</td>
  </tr>
  <tr>
    <td>Red</td>
    <td>||||/ ||</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Blue</td>
    <td>||||/ ||||/</td>
    <td>10</td>
  </tr>
  <tr>
    <td>Green</td>
    <td>||||/ |||</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Yellow</td>
    <td>||||/</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Purple</td>
    <td>||||/ |</td>
    <td>6</td>
  </tr>
</table>

<p><strong>Reading the tally chart:</strong></p>
<ul>
  <li>Red: 7 students (5 + 2)</li>
  <li>Blue: 10 students (5 + 5)</li>
  <li>Green: 8 students (5 + 3)</li>
  <li>Yellow: 5 students (5)</li>
  <li>Purple: 6 students (5 + 1)</li>
  <li><strong>Total students:</strong> \\(7 + 10 + 8 + 5 + 6 = 36\\) students</li>
</ul>

<p><strong>Most popular colour?</strong> Blue (10 students)</p>
</div>
"""
    },
    {
        "title": "Converting Data Between Formats",
        "body": """<h3>Data Can Be Shown Different Ways</h3>

<p>The same data can be shown as a <strong>tally chart, data table, pictogram, or bar chart</strong>. All show the same information, just in different formats!</p>

<h3>Example: Converting a Tally Chart to a Table</h3>

<div class="worked-example">
<p><strong>Step 1: Start with a tally chart</strong></p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; margin-bottom: 20px;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Pet Type</td>
    <td style="text-align: center; font-weight: bold;">Tally Marks</td>
    <td style="text-align: center; font-weight: bold;">Total</td>
  </tr>
  <tr>
    <td>Cat</td>
    <td>||||/ |||</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Dog</td>
    <td>||||/ ||||/ |</td>
    <td>11</td>
  </tr>
  <tr>
    <td>Hamster</td>
    <td>||||/</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Fish</td>
    <td>||||/ ||</td>
    <td>7</td>
  </tr>
</table>

<p><strong>Step 2: Organize the totals in a simple table</strong></p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; margin-bottom: 20px;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Pet Type</td>
    <td style="text-align: center; font-weight: bold;">Number of Families</td>
  </tr>
  <tr>
    <td>Cat</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Dog</td>
    <td>11</td>
  </tr>
  <tr>
    <td>Hamster</td>
    <td>5</td>
  </tr>
  <tr>
    <td>Fish</td>
    <td>7</td>
  </tr>
</table>

<p><strong>Step 3: Create a bar chart from the numbers</strong></p>

<canvas id="data_pets1" data-chart='{"type":"bar","data":{"labels":["Cat","Dog","Hamster","Fish"],"datasets":[{"label":"Number of Families","data":[8,11,5,7],"backgroundColor":["#f97316","#a855f7","#f59e0b","#3b82f6"]}]},"options":{"plugins":{"title":{"display":true,"text":"Class Pet Ownership"}},"scales":{"y":{"beginAtZero":true,"title":{"display":true,"text":"Number of Families"}}}}}' height="300"></canvas>

<p><strong>All three show the same data!</strong> Choose the format that's easiest to work with.</p>
</div>

<h3>When to Use Each Format</h3>

<div class="concept-box">
<ul>
  <li><strong>Tally Chart:</strong> When collecting data in person (quick and easy)</li>
  <li><strong>Table:</strong> When storing and looking up specific data</li>
  <li><strong>Pictogram:</strong> When you want a visual representation that's fun and easy</li>
  <li><strong>Bar Chart:</strong> When you want to clearly compare values and see patterns</li>
</ul>
</div>
"""
    },
    {
        "title": "Organizing Complex Data",
        "body": """<h3>Two-Way Tables</h3>

<p>Sometimes we need to organize data by <strong>two different categories at once</strong>. We use a <strong>two-way table</strong> (or frequency table).</p>

<div class="worked-example">
<p><strong>Example: Favourite Fruit by Year Group</strong></p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Fruit</td>
    <td style="text-align: center; font-weight: bold;">Year 3</td>
    <td style="text-align: center; font-weight: bold;">Year 4</td>
    <td style="text-align: center; font-weight: bold;">Total</td>
  </tr>
  <tr>
    <td>Apple</td>
    <td>6</td>
    <td>8</td>
    <td>14</td>
  </tr>
  <tr>
    <td>Banana</td>
    <td>7</td>
    <td>9</td>
    <td>16</td>
  </tr>
  <tr>
    <td>Orange</td>
    <td>5</td>
    <td>4</td>
    <td>9</td>
  </tr>
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Total</td>
    <td style="text-align: center;">18</td>
    <td style="text-align: center;">21</td>
    <td style="text-align: center;">39</td>
  </tr>
</table>

<p><strong>What questions can we ask?</strong></p>
<ul>
  <li>How many Year 3 students like apples? 6</li>
  <li>How many Year 4 students like bananas? 9</li>
  <li>Which fruit is most popular overall? Banana (16 total)</li>
  <li>How many students were surveyed? 39</li>
</ul>
</div>

<h3>Organizing Data by Ranges</h3>

<p>When data is spread across many values, we can group them into <strong>ranges</strong> to make patterns clearer.</p>

<div class="worked-example">
<p><strong>Example: Test Scores</strong></p>

<p>Individual scores: 45, 52, 67, 78, 81, 88, 92, 55, 73, 86, 91, 58, 64, 75, 89</p>

<p><strong>Grouped into ranges:</strong></p>

<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
  <tr class="formula-box">
    <td style="text-align: center; font-weight: bold;">Score Range</td>
    <td style="text-align: center; font-weight: bold;">Tally</td>
    <td style="text-align: center; font-weight: bold;">Frequency</td>
  </tr>
  <tr>
    <td>40-49</td>
    <td>|</td>
    <td>1</td>
  </tr>
  <tr>
    <td>50-59</td>
    <td>||||/</td>
    <td>5</td>
  </tr>
  <tr>
    <td>60-69</td>
    <td>||</td>
    <td>2</td>
  </tr>
  <tr>
    <td>70-79</td>
    <td>||||/</td>
    <td>5</td>
  </tr>
  <tr>
    <td>80-89</td>
    <td>||</td>
    <td>2</td>
  </tr>
  <tr>
    <td>90-99</td>
    <td>|||</td>
    <td>3</td>
  </tr>
</table>

<p><strong>Pattern:</strong> Most scores are in the 50-59 and 70-79 ranges. Few scores are very low or very high.</p>
</div>

<h3>Data Organization Tips</h3>

<div class="success-box">
<ul>
  <li><strong>Use clear headers:</strong> Anyone should understand what each column means</li>
  <li><strong>Use consistent units:</strong> If measuring temperature, always use °C</li>
  <li><strong>Keep it organized:</strong> Align data neatly in columns and rows</li>
  <li><strong>Include totals:</strong> Add a total row if it makes sense</li>
  <li><strong>Check accuracy:</strong> Double-check all numbers are correct</li>
</ul>
</div>
"""
    }
]
