# Line and Scatter Plots

TITLE = "Line and Scatter Plots"

SECTIONS = [
    {
        'id': 'scatter_01_line_plots',
        'title': 'Creating and Styling Line Plots',
        'body': '''
<div class="concept-box">
<h3>Line Plots: Visualizing Relationships</h3>
<p>Line plots connect data points with lines, ideal for showing trends over time or continuous relationships.</p>
<p><strong>Core Principle:</strong> Each point (x, y) is plotted, then consecutive points are connected.</p>
</div>

<div class="worked-example">
<h4>Basic Line Plot</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

ax.plot(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Line Style Customization</h3>
<p>Control how lines appear with style parameters:</p>
<ul>
<li><code>linestyle</code>: '-' (solid), '--' (dashed), ':' (dotted), '-.' (dash-dot)</li>
<li><code>linewidth</code>: thickness in points</li>
<li><code>color</code>: by name, hex code, or RGB tuple</li>
<li><code>marker</code>: 'o', 's', '^', etc. for point markers</li>
</ul>
</div>

<div class="worked-example">
<h4>Styled Line Plot</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

ax.plot(x, y,
        linestyle='--',
        linewidth=2,
        color='#4f8ef7',
        marker='o',
        markersize=8)

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Pro Tip</h4>
<p>You can plot multiple lines on the same axes by calling <code>ax.plot()</code> multiple times. Each call adds a new line.</p>
</div>
'''
    },
    {
        'id': 'scatter_02_scatter_plots',
        'title': 'Scatter Plots for Relationships',
        'body': '''
<div class="concept-box">
<h3>Scatter Plots: Showing Individual Points</h3>
<p>Scatter plots display individual data points without connecting them, revealing patterns and relationships.</p>
<p><strong>Key Use Case:</strong> Identifying correlations, clusters, and outliers.</p>
</div>

<div class="worked-example">
<h4>Basic Scatter Plot</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x = [1, 2, 3, 4, 5, 1, 2, 3]
y = [2, 4, 1, 3, 5, 3, 3, 2]

ax.scatter(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Scatter Plot Parameters</h3>
<ul>
<li><code>s</code>: marker size (in points²)</li>
<li><code>c</code>: color(s) - can be a single color or array for color mapping</li>
<li><code>alpha</code>: transparency (0 to 1)</li>
<li><code>edgecolors</code>: color of marker borders</li>
<li><code>cmap</code>: colormap for mapping values to colors</li>
</ul>
</div>

<div class="worked-example">
<h4>Advanced Scatter Plot with Color Mapping</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.random.rand(50)
y = np.random.rand(50)
values = np.random.rand(50)

scatter = ax.scatter(x, y,
                     s=100,
                     c=values,
                     cmap='viridis',
                     alpha=0.7,
                     edgecolors='black')

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Value')

fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>When to Use Each</h4>
<p><strong>Line plots:</strong> Time series, continuous processes</p>
<p><strong>Scatter plots:</strong> Relationships between two variables, finding patterns</p>
</div>
'''
    },
    {
        'id': 'scatter_03_multiple_series',
        'title': 'Plotting Multiple Series',
        'body': '''
<div class="concept-box">
<h3>Comparing Multiple Datasets</h3>
<p>Plot multiple series on the same axes to compare trends, relationships, or distributions.</p>
</div>

<div class="worked-example">
<h4>Multiple Line Series</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 1, 3, 2]
y2 = [2, 3, 2, 4, 3]
y3 = [3, 1, 4, 2, 5]

ax.plot(x, y1, label='Series 1')
ax.plot(x, y2, label='Series 2')
ax.plot(x, y3, label='Series 3')

ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

fig.show()
</code></pre>
</div>

<div class="worked-example">
<h4>Multiple Scatter Series</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Group 1
x1, y1 = np.random.normal(0, 1, (2, 30))
ax.scatter(x1, y1, label='Group A', alpha=0.6)

# Group 2
x2, y2 = np.random.normal(2, 1, (2, 30))
ax.scatter(x2, y2, label='Group B', alpha=0.6)

ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Always Label Your Series</h4>
<p>When plotting multiple series, always add labels with the <code>label</code> parameter and call <code>ax.legend()</code>. This makes your plot readable and professional.</p>
</div>
'''
    }
]
