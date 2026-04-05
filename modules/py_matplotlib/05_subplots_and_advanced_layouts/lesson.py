# Subplots and Advanced Layouts

TITLE = "Subplots and Advanced Layouts"

SECTIONS = [
    {
        'id': 'subplot_01_basic_subplots',
        'title': 'Creating Basic Subplots',
        'body': '''
<div class="concept-box">
<h3>Subplots: Multiple Plots in One Figure</h3>
<p>Create a grid of plots using <code>subplots()</code> with <code>nrows</code> and <code>ncols</code> parameters.</p>
<p><strong>Key Concept:</strong> One figure contains multiple axes arranged in a grid.</p>
</div>

<div class="worked-example">
<h4>2x2 Subplot Grid</h4>
<pre><code>import matplotlib.pyplot as plt

# Create 2x2 grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# axes is a 2D array
x = [1, 2, 3, 4, 5]

# Top-left
axes[0, 0].plot(x, [1, 2, 1, 3, 2])
axes[0, 0].set_title('Plot 1')

# Top-right
axes[0, 1].plot(x, [2, 1, 3, 2, 1])
axes[0, 1].set_title('Plot 2')

# Bottom-left
axes[1, 0].scatter(x, [3, 1, 2, 4, 3])
axes[1, 0].set_title('Plot 3')

# Bottom-right
axes[1, 1].bar(x, [1, 3, 2, 4, 2])
axes[1, 1].set_title('Plot 4')

plt.tight_layout()
fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Subplot Layouts</h3>
<ul>
<li><code>nrows, ncols</code>: grid dimensions</li>
<li><code>figsize</code>: (width, height) in inches</li>
<li><code>tight_layout()</code>: auto-adjust spacing</li>
<li><code>subplots_adjust()</code>: manual spacing control</li>
</ul>
</div>

<div class="worked-example">
<h4>1D Subplot Grid</h4>
<pre><code>import matplotlib.pyplot as plt

# Three plots in a row
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

x = [1, 2, 3, 4, 5]

axes[0].plot(x, [1, 2, 1, 3, 2])
axes[0].set_title('Time Series')

axes[1].scatter(x, [2, 1, 3, 2, 1])
axes[1].set_title('Scatter')

axes[2].bar(x, [1, 3, 2, 4, 2])
axes[2].set_title('Bar Chart')

plt.tight_layout()
fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Always Use Tight Layout</h4>
<p>Call <code>plt.tight_layout()</code> after creating subplots to prevent overlapping labels and titles.</p>
</div>
'''
    },
    {
        'id': 'subplot_02_shared_axes',
        'title': 'Shared Axes for Comparison',
        'body': '''
<div class="concept-box">
<h3>Shared Axes: Common Reference</h3>
<p>Share x or y axes across subplots to facilitate direct comparison of datasets.</p>
</div>

<div class="worked-example">
<h4>Shared X-Axis</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

x = np.linspace(0, 10, 100)

# All three plots use the same x-axis
axes[0].plot(x, np.sin(x))
axes[0].set_ylabel('sin(x)')

axes[1].plot(x, np.cos(x))
axes[1].set_ylabel('cos(x)')

axes[2].plot(x, np.tan(x))
axes[2].set_ylabel('tan(x)')

axes[2].set_xlabel('x')

plt.tight_layout()
fig.show()
</code></pre>
</div>

<div class="worked-example">
<h4>Shared Y-Axis</h4>
<pre><code>import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

categories = ['A', 'B', 'C']
data1 = [10, 20, 15]
data2 = [12, 18, 16]
data3 = [15, 22, 18]

axes[0].bar(categories, data1)
axes[0].set_title('Dataset 1')

axes[1].bar(categories, data2)
axes[1].set_title('Dataset 2')

axes[2].bar(categories, data3)
axes[2].set_title('Dataset 3')

axes[0].set_ylabel('Value')

plt.tight_layout()
fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>When to Share Axes</h4>
<p><strong>Share x-axis:</strong> When comparing time series or continuous data</p>
<p><strong>Share y-axis:</strong> When comparing magnitudes across categories</p>
<p><strong>Don't overuse:</strong> Shared axes can mislead if data ranges differ significantly</p>
</div>
'''
    },
    {
        'id': 'subplot_03_gridspec_advanced',
        'title': 'Advanced Layouts with GridSpec',
        'body': '''
<div class="concept-box">
<h3>GridSpec: Fine-Grained Control</h3>
<p>For non-uniform layouts (plots of different sizes), use <code>GridSpec</code>.</p>
</div>

<div class="worked-example">
<h4>Mixed Subplot Sizes</h4>
<pre><code>import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(3, 3, figure=fig)

# Large plot on left
ax1 = fig.add_subplot(gs[:, 0:2])
ax1.plot([1, 2, 3, 4], [1, 2, 1, 3])
ax1.set_title('Main Plot')

# Three smaller plots on right
ax2 = fig.add_subplot(gs[0, 2])
ax2.plot([1, 2], [1, 2])
ax2.set_title('Top')

ax3 = fig.add_subplot(gs[1, 2])
ax3.scatter([1, 2], [1, 2])
ax3.set_title('Middle')

ax4 = fig.add_subplot(gs[2, 2])
ax4.bar([1, 2], [1, 2])
ax4.set_title('Bottom')

plt.tight_layout()
fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>GridSpec Parameters</h3>
<ul>
<li><code>nrows, ncols</code>: grid dimensions</li>
<li><code>hspace, wspace</code>: height/width spacing between subplots</li>
<li><code>height_ratios, width_ratios</code>: relative sizes of rows/columns</li>
</ul>
</div>

<div class="worked-example">
<h4>Different Sized Rows</h4>
<pre><code>import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 8))

# Create 3 rows with different heights
gs = GridSpec(3, 1, figure=fig,
              height_ratios=[3, 1, 1],
              hspace=0.4)

ax1 = fig.add_subplot(gs[0])
ax1.plot([1, 2, 3, 4], [1, 3, 2, 4])
ax1.set_title('Main Plot (3x height)')

ax2 = fig.add_subplot(gs[1])
ax2.bar([1, 2, 3], [1, 2, 1])
ax2.set_title('Small Plot')

ax3 = fig.add_subplot(gs[2])
ax3.scatter([1, 2, 3], [1, 2, 1])
ax3.set_title('Small Plot')

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>When to Use GridSpec</h4>
<p>GridSpec is powerful but complex. Use it when <code>subplots()</code> can't achieve your desired layout. For most cases, simple subplots work fine.</p>
</div>
'''
    },
    {
        'id': 'subplot_04_colorbars_and_multiple_yaxis',
        'title': 'Colorbars and Multiple Y-Axes',
        'body': '''
<div class="concept-box">
<h3>Colorbars: Displaying Color Mappings</h3>
<p>Colorbars show the scale for color-mapped data (heatmaps, scatter plots with color mapping).</p>
</div>

<div class="worked-example">
<h4>Colorbar with Scatter Plot</h4>
<pre><code>import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))

x = np.random.rand(100)
y = np.random.rand(100)
values = np.random.rand(100)

scatter = ax.scatter(x, y, c=values, cmap='viridis', s=100)

# Add colorbar
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Value', rotation=270, labelpad=20)

ax.set_xlabel('X')
ax.set_ylabel('Y')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Multiple Y-Axes: Comparing Different Scales</h3>
<p>Plot data with different scales on separate y-axes using <code>twinx()</code>.</p>
</div>

<div class="worked-example">
<h4>Dual Y-Axes</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

# First y-axis
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 1, 3, 2]

line1 = ax1.plot(x, y1, color='#4f8ef7', label='Temperature')
ax1.set_ylabel('Temperature (°C)', color='#4f8ef7')
ax1.tick_params(axis='y', labelcolor='#4f8ef7')
ax1.set_xlabel('Time')

# Second y-axis (different scale)
ax2 = ax1.twinx()
y2 = [100, 150, 120, 200, 180]

line2 = ax2.plot(x, y2, color='#3fb950', label='Pressure')
ax2.set_ylabel('Pressure (kPa)', color='#3fb950')
ax2.tick_params(axis='y', labelcolor='#3fb950')

# Combined legend
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>Careful with Multiple Axes</h4>
<p>Dual y-axes can be misleading if not used carefully. Make axis relationships clear with labels and legends.</p>
</div>
'''
    }
]
