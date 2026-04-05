# Introduction to Matplotlib

TITLE = "Introduction to Matplotlib"

SECTIONS = [
    {
        'id': 'intro_01_understanding_figure_axes',
        'title': 'Understanding Figure and Axes',
        'body': '''
<div class="concept-box">
<h3>Core Concept: The Figure-Axes Hierarchy</h3>
<p>At the heart of matplotlib lies a hierarchical structure:</p>
<ul>
<li><strong>Figure:</strong> The top-level container for all visual elements. Think of it as the canvas.</li>
<li><strong>Axes:</strong> The area where data is plotted. Each figure can contain multiple axes.</li>
</ul>
<p>This hierarchy allows you to create complex multi-plot layouts with precise control over each element.</p>
</div>

<div class="worked-example">
<h4>First Principles Example</h4>
<p>Let's create a simple figure with one axis:</p>
<pre><code>import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Plot some data
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Display
plt.show()
</code></pre>
<p>Here, <code>fig</code> is the Figure object, and <code>ax</code> is the Axes object. All plotting happens on the axes.</p>
</div>

<div class="success-box">
<h4>Key Insight</h4>
<p>Understanding the Figure-Axes distinction is fundamental. Most visualization problems can be solved once you grasp this hierarchy.</p>
</div>
'''
    },
    {
        'id': 'intro_02_pyplot_interface',
        'title': 'The PyPlot Interface vs Object-Oriented API',
        'body': '''
<div class="concept-box">
<h3>Two Approaches to Matplotlib</h3>
<p>Matplotlib provides two interfaces:</p>
<ul>
<li><strong>PyPlot Interface (Simple):</strong> MATLAB-like, good for quick plots</li>
<li><strong>Object-Oriented API (Powerful):</strong> Direct control via Figure and Axes objects</li>
</ul>
</div>

<div class="worked-example">
<h4>PyPlot Interface (Quick)</h4>
<pre><code>import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 2, 3])
plt.show()
</code></pre>

<h4>Object-Oriented API (Recommended)</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>Best Practice</h4>
<p>For anything beyond the simplest plots, use the Object-Oriented API. It's more explicit, flexible, and scalable.</p>
</div>
'''
    },
    {
        'id': 'intro_03_coordinate_systems',
        'title': 'Data vs Display Coordinates',
        'body': '''
<div class="concept-box">
<h3>Understanding Coordinate Systems</h3>
<p>Matplotlib operates with two coordinate systems:</p>
<ul>
<li><strong>Data Coordinates:</strong> The space defined by your data (x-axis, y-axis limits)</li>
<li><strong>Display Coordinates:</strong> Pixels on your screen or output file</li>
</ul>
<p>Transformations between these coordinate systems happen automatically.</p>
</div>

<div class="worked-example">
<h4>Example: Working with Data Coordinates</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

# Plot in data coordinates
ax.plot([0, 10], [0, 100])

# Set axis limits (data coordinates)
ax.set_xlim(-1, 11)
ax.set_ylim(-10, 110)

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Why This Matters</h4>
<p>Understanding coordinate systems is crucial for annotations, adding elements, and transforming data for display.</p>
</div>
'''
    },
    {
        'id': 'intro_04_rendering_and_backends',
        'title': 'Rendering and Backends',
        'body': '''
<div class="concept-box">
<h3>How Matplotlib Renders</h3>
<p>Matplotlib uses <strong>backends</strong> to render plots to different outputs:</p>
<ul>
<li><strong>Interactive Backends:</strong> display() for Jupyter, TkAgg for GUI windows</li>
<li><strong>Static Backends:</strong> Agg for PNG/PDF files</li>
</ul>
</div>

<div class="worked-example">
<h4>Selecting a Backend</h4>
<pre><code>import matplotlib
matplotlib.use('Agg')  # Set before importing pyplot

import matplotlib.pyplot as plt

# Now all plots will render to PNG/PDF files
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3])
fig.savefig('plot.png')
</code></pre>
</div>

<div class="warning-box">
<h4>Important</h4>
<p>Backend selection must happen before importing pyplot. Most of the time, the default backend is fine.</p>
</div>
'''
    }
]
