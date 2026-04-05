# Bar Charts and Histograms

TITLE = "Bar Charts and Histograms"

SECTIONS = [
    {
        'id': 'barchist_01_bar_charts',
        'title': 'Creating Bar Charts',
        'body': '''
<div class="concept-box">
<h3>Bar Charts: Comparing Categories</h3>
<p>Bar charts display categorical data as rectangular bars, with heights proportional to values.</p>
<p><strong>Core Principle:</strong> Each category gets one bar. Height represents the data value.</p>
</div>

<div class="worked-example">
<h4>Basic Bar Chart</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

ax.bar(categories, values)
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Simple Bar Chart')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Bar Chart Customization</h3>
<ul>
<li><code>color</code>: single color or list of colors per bar</li>
<li><code>width</code>: bar width (default 0.8)</li>
<li><code>edgecolor</code>: border color</li>
<li><code>linewidth</code>: border thickness</li>
<li><code>alpha</code>: transparency</li>
</ul>
</div>

<div class="worked-example">
<h4>Styled Bar Chart</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [100, 150, 120, 200]
colors = ['#4f8ef7', '#58a6ff', '#79c0ff', '#3fb950']

ax.bar(categories, values,
       color=colors,
       edgecolor='#e6edf3',
       linewidth=2,
       alpha=0.8)

ax.set_ylabel('Revenue ($1000s)')
ax.set_title('Quarterly Revenue')

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Adding Value Labels</h4>
<p>For clarity, add text labels showing exact values on each bar using a loop or <code>ax.bar_label()</code>.</p>
</div>
'''
    },
    {
        'id': 'barchist_02_grouped_stacked_bars',
        'title': 'Grouped and Stacked Bar Charts',
        'body': '''
<div class="concept-box">
<h3>Grouped Bar Charts</h3>
<p>Display multiple categories side-by-side to compare subcategories within groups.</p>
</div>

<div class="worked-example">
<h4>Grouped Bar Chart</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

categories = ['Product A', 'Product B', 'Product C']
year1 = [10, 15, 12]
year2 = [12, 18, 14]

x = np.arange(len(categories))
width = 0.35

ax.bar(x - width/2, year1, width, label='2023')
ax.bar(x + width/2, year2, width, label='2024')

ax.set_xlabel('Products')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Stacked Bar Charts</h3>
<p>Stack bars on top of each other to show composition of total values.</p>
</div>

<div class="worked-example">
<h4>Stacked Bar Chart</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

categories = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [10, 12, 15, 14]
product_b = [8, 10, 12, 11]
product_c = [5, 6, 7, 8]

ax.bar(categories, product_a, label='Product A')
ax.bar(categories, product_b, bottom=product_a, label='Product B')

bottom_sum = [a+b for a,b in zip(product_a, product_b)]
ax.bar(categories, product_c, bottom=bottom_sum, label='Product C')

ax.set_ylabel('Total Sales')
ax.legend()

fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>Choose Wisely</h4>
<p><strong>Grouped bars:</strong> Easy comparison across groups</p>
<p><strong>Stacked bars:</strong> Show composition and totals, but harder to compare individual segments</p>
</div>
'''
    },
    {
        'id': 'barchist_03_histograms',
        'title': 'Histograms: Distributional Analysis',
        'body': '''
<div class="concept-box">
<h3>Histograms: Understanding Data Distribution</h3>
<p>Histograms show frequency distributions by binning continuous data into ranges.</p>
<p><strong>Key Concept:</strong> Data is divided into bins, and bar height shows frequency in each bin.</p>
</div>

<div class="worked-example">
<h4>Basic Histogram</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

data = np.random.normal(loc=100, scale=15, size=1000)

ax.hist(data, bins=30, edgecolor='#e6edf3')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Data')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Histogram Parameters</h3>
<ul>
<li><code>bins</code>: number of bins or bin edges (default 10)</li>
<li><code>range</code>: (min, max) for data to include</li>
<li><code>density</code>: normalize to probability density</li>
<li><code>cumulative</code>: show cumulative distribution</li>
<li><code>color</code>, <code>edgecolor</code>, <code>alpha</code>: styling</li>
</ul>
</div>

<div class="worked-example">
<h4>Advanced Histogram: Multiple Distributions</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

data1 = np.random.normal(100, 15, 500)
data2 = np.random.normal(90, 20, 500)

ax.hist(data1, bins=25, alpha=0.6, label='Group A', color='#4f8ef7')
ax.hist(data2, bins=25, alpha=0.6, label='Group B', color='#58a6ff')

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Comparing Two Distributions')
ax.legend()

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Choosing Bin Size</h4>
<p>Bin size affects the histogram's appearance:</p>
<ul>
<li><strong>Too few bins:</strong> Loss of detail (over-smoothing)</li>
<li><strong>Too many bins:</strong> Noisy, hard to see pattern</li>
<li><strong>Rule of thumb:</strong> Start with 30-50 bins for 1000 data points</li>
</ul>
</div>
'''
    }
]
