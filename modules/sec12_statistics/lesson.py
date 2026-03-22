SECTIONS = [
    {
        "title": "Measures of Central Tendency: Introduction",
        "body": """
<p><strong>What is "Central Tendency"?</strong></p>
<p>When we have a set of data, we often want to find a single number that represents the whole set - a "typical" or "average" value. This is called a measure of central tendency.</p>

<p>There are three main measures:</p>
<ul>
<li><strong>Mean:</strong> The arithmetic average</li>
<li><strong>Median:</strong> The middle value</li>
<li><strong>Mode:</strong> The most common value</li>
</ul>

<p><strong>Why Do We Need Three Measures?</strong></p>
<p>Different measures work better for different types of data. We'll see that sometimes one measure is more useful or representative than the others.</p>

<div class='example-box'>
<p><strong>Simple Example:</strong></p>
<pre class='code-block'>
Data set: 2, 3, 4, 5, 6

Mean: (2 + 3 + 4 + 5 + 6) ÷ 5 = 20 ÷ 5 = 4
Median: 4 (the middle value)
Mode: No mode (all values appear once)
</pre>
</div>

<p><strong>What Measure Should We Use?</strong></p>
<p>This depends on the data and what we want to know. Let's explore each measure in detail.</p>
"""
    },
    {
        "title": "The Mean (Average)",
        "body": """
<p><strong>The Mean</strong> is the sum of all values divided by how many values there are.</p>

<p><strong>Formula: Mean = Sum of all values / Number of values</strong></p>

<div class='example-box'>
<p><strong>Example 1: Simple mean</strong></p>
<pre class='code-block'>
Test scores: 75, 82, 88, 79, 91

Mean = (75 + 82 + 88 + 79 + 91) ÷ 5
     = 415 ÷ 5
     = 83

The average score is 83.
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Mean with a frequency table</strong></p>
<pre class='code-block'>
Number of cars in households:

Number | Frequency
--------|----------
   0    |    3     (3 households have 0 cars)
   1    |    7     (7 households have 1 car)
   2    |    5     (5 households have 2 cars)
   3    |    2     (2 households have 3 cars)

Total sum = (0×3) + (1×7) + (2×5) + (3×2)
          = 0 + 7 + 10 + 6
          = 23

Total frequency = 3 + 7 + 5 + 2 = 17

Mean = 23 ÷ 17 ≈ 1.35 cars per household
</pre>
</div>

<p><strong>Properties of the Mean:</strong></p>
<ul>
<li>It uses ALL the data values</li>
<li>It can be affected by extreme values (outliers)</li>
<li>It gives the "fair share" or "balance point"</li>
<li>It can be a decimal, even if all data are whole numbers</li>
</ul>

<div class='example-box'>
<p><strong>The Effect of Outliers:</strong></p>
<pre class='code-block'>
Situation 1: Pocket money (normal case)
Data: £5, £6, £7, £8, £9
Mean = £7

Situation 2: Pocket money (with one very large value)
Data: £5, £6, £7, £8, £100 (one lucky person got £100!)
Mean = (5 + 6 + 7 + 8 + 100) ÷ 5 = 126 ÷ 5 = £25.20

The single large value (£100) pulled the mean way up!
Only one person got more than £9, but the mean is £25.20!

In situations like this, the mean can be misleading.
</pre>
</div>

<p><strong>When to Use the Mean:</strong></p>
<ul>
<li>When data is roughly evenly distributed</li>
<li>When there are no extreme outliers</li>
<li>When you need a measure for further calculations</li>
</ul>
"""
    },
    {
        "title": "The Median (Middle Value)",
        "body": """
<p><strong>The Median</strong> is the middle value when data is arranged in order from smallest to largest.</p>

<p><strong>Finding the Median:</strong></p>
<ol>
<li>Arrange the data in order (smallest to largest)</li>
<li>If there's an odd number of values, the median is the middle value</li>
<li>If there's an even number of values, the median is the mean of the two middle values</li>
</ol>

<div class='example-box'>
<p><strong>Example 1: Odd number of values</strong></p>
<pre class='code-block'>
Test scores: 75, 82, 88, 79, 91

Arrange in order: 75, 79, 82, 88, 91
                        ↑
                      middle

Median = 82
</pre>
</div>

<div class='example-box'>
<p><strong>Example 2: Even number of values</strong></p>
<pre class='code-block'>
Test scores: 75, 82, 88, 79, 91, 85

Arrange in order: 75, 79, 82, 85, 88, 91
                        ↑    ↑
                    two middle values

Median = (82 + 85) ÷ 2 = 167 ÷ 2 = 83.5
</pre>
</div>

<p><strong>The Median is Resistant to Outliers:</strong></p>

<div class='example-box'>
<p><strong>Using our outlier example:</strong></p>
<pre class='code-block'>
Data: £5, £6, £7, £8, £9
Median = £7

Data with outlier: £5, £6, £7, £8, £100
Arrange: £5, £6, £7, £8, £100
              ↑
          median = £7

Notice: The median is still £7, even though one value is £100!
The median was not affected by the extreme value.
</pre>
</div>

<p><strong>Properties of the Median:</strong></p>
<ul>
<li>It's not affected by extreme values (outliers)</li>
<li>Exactly half the data is above it, half below</li>
<li>It must be one of the actual data values (for odd-sized sets)</li>
<li>It's easy to understand - "the middle value"</li>
</ul>

<p><strong>When to Use the Median:</strong></p>
<ul>
<li>When there are extreme outliers</li>
<li>When data is skewed (not evenly distributed)</li>
<li>When you want a "typical" value that isn't pulled by extremes</li>
<li>Examples: house prices, salaries (often better than the mean)</li>
</ul>
"""
    },
    {
        "title": "The Mode (Most Frequent Value)",
        "body": """
<p><strong>The Mode</strong> is the value that appears most frequently in a data set.</p>

<div class='example-box'>
<p><strong>Example 1: Finding the mode</strong></p>
<pre class='code-block'>
Shoe sizes in a class: 4, 5, 5, 5, 6, 6, 7, 8, 8, 9

Frequency count:
Size 4: 1 time
Size 5: 3 times ← highest frequency
Size 6: 2 times
Size 7: 1 time
Size 8: 2 times
Size 9: 1 time

Mode = size 5 (appears most often)
</pre>
</div>

<p><strong>Special Cases with Mode:</strong></p>

<div class='example-box'>
<p><strong>Case 1: No Mode</strong></p>
<pre class='code-block'>
Data: 2, 3, 4, 5, 6
All values appear exactly once.
There is no mode (or we say "no mode exists").
</pre>
</div>

<div class='example-box'>
<p><strong>Case 2: Bimodal (two modes)</strong></p>
<pre class='code-block'>
Data: 3, 3, 3, 5, 5, 5, 7, 8, 9
Value 3 appears 3 times
Value 5 appears 3 times
Both have the same highest frequency.
Modes = 3 and 5 (bimodal distribution)
</pre>
</div>

<div class='example-box'>
<p><strong>Case 3: Multimodal (several modes)</strong></p>
<pre class='code-block'>
If three or more values share the highest frequency,
we say the data is multimodal.
</pre>
</div>

<p><strong>Properties of the Mode:</strong></p>
<ul>
<li>It's the only measure that works for categorical data (non-numeric)</li>
<li>It's easy to find and understand</li>
<li>It can be unaffected by outliers</li>
<li>It must be an actual value from the data</li>
<li>It's not useful if no value appears more than once</li>
</ul>

<div class='example-box'>
<p><strong>Mode for Categorical Data (Non-numeric):</strong></p>
<pre class='code-block'>
Favorite colors in a class:
Red, Blue, Red, Green, Blue, Red, Yellow, Blue, Red

Frequency:
Red: 4 times ← most frequent
Blue: 3 times
Green: 1 time
Yellow: 1 time

Mode = Red

We couldn't calculate mean or median for colors,
but we can find the mode!
</pre>
</div>

<p><strong>When to Use the Mode:</strong></p>
<ul>
<li>When you need the most common value</li>
<li>For categorical (non-numeric) data</li>
<li>When looking at preferences or opinions</li>
<li>For discrete data like shoe sizes, clothing sizes</li>
</ul>
"""
    },
    {
        "title": "Grouped Data and Choosing the Right Measure",
        "body": """
<p><strong>Working with Grouped Data:</strong></p>
<p>Sometimes data is presented in groups (intervals) rather than individual values.</p>

<div class='example-box'>
<p><strong>Example: Heights of students in a class</strong></p>
<pre class='code-block'>
Height (cm) | Frequency
------------|----------
150-160     |    4
160-170     |    8
170-180     |    6
180-190     |    2

To estimate the mean, we use the midpoint of each group:
Midpoint for 150-160: (150 + 160) ÷ 2 = 155
Midpoint for 160-170: (160 + 170) ÷ 2 = 165
Midpoint for 170-180: (170 + 180) ÷ 2 = 175
Midpoint for 180-190: (180 + 190) ÷ 2 = 185

Mean ≈ (155×4 + 165×8 + 175×6 + 185×2) ÷ (4+8+6+2)
     = (620 + 1320 + 1050 + 370) ÷ 20
     = 3360 ÷ 20
     = 168 cm

For grouped data:
- The median is in the group with the middle frequency
- The mode is the midpoint of the group with highest frequency
</pre>
</div>

<p><strong>Choosing the Right Measure:</strong></p>

<div class='example-box'>
<p><strong>Comparison of the three measures:</strong></p>
<pre class='code-block'>
            MEAN          MEDIAN        MODE
Uses all    ✓ Yes         ✗ No          ✗ No
data?

Affected    ✗ Yes         ✓ No          ✓ No
by outliers?

Works for   ✗ No          ✗ No          ✓ Yes
categories?

Easy to     ✓ Yes         ✓ Yes         ✓ Yes
find?

Unique      Often         Often         May not exist
value?      (can be       (if even      or may have
            between       number)       multiple
            values)                     modes
</pre>
</div>

<p><strong>Decision Guide:</strong></p>

<div class='example-box'>
<p><strong>Situation 1: House prices in a city</strong></p>
<pre class='code-block'>
Most houses: £150,000-£250,000
A few luxury homes: £1,000,000+

Mean would be pulled up by luxury homes.
Use MEDIAN - better represents typical house price.
</pre>
</div>

<div class='example-box'>
<p><strong>Situation 2: Test scores that vary little</strong></p>
<pre class='code-block'>
Scores: 78, 79, 80, 81, 82

No extreme outliers, values are close together.
Use MEAN - good representation, uses all data.
</pre>
</div>

<div class='example-box'>
<p><strong>Situation 3: Most popular shoe size in a shop</strong></p>
<pre class='code-block'>
Need to know which size to stock most.

Use MODE - tells us the most common size.
(Mean and median of shoe sizes don't make practical sense)
</pre>
</div>

<p><strong>In Summary:</strong></p>
<ul>
<li><strong>Mean:</strong> Best when data is evenly distributed with no major outliers</li>
<li><strong>Median:</strong> Best when there are outliers or skewed data</li>
<li><strong>Mode:</strong> Best for categorical data or finding the most common value</li>
</ul>
"""
    }
]
