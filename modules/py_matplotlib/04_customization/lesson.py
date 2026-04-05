# Customization: Labels, Legends, and Styles

TITLE = "Customization: Labels, Legends, and Styles"

SECTIONS = [
    {
        'id': 'custom_01_labels_titles',
        'title': 'Adding Labels and Titles',
        'body': '''
<div class="concept-box">
<h3>Labels: Making Your Plot Readable</h3>
<p>Clear labels are essential for effective communication. Every axis should have a descriptive label including units.</p>
</div>

<div class="worked-example">
<h4>Adding Basic Labels</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4, 5], [2, 4, 1, 3, 5])

# Add labels
ax.set_xlabel('Time (seconds)', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_title('Temperature Over Time', fontsize=14, fontweight='bold')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Label Formatting</h3>
<ul>
<li><code>fontsize</code>: size in points</li>
<li><code>fontweight</code>: 'normal', 'bold', 'heavy'</li>
<li><code>color</code>: text color</li>
<li><code>rotation</code>: angle in degrees</li>
<li><code>ha</code> (horizontal alignment): 'left', 'center', 'right'</li>
<li><code>va</code> (vertical alignment): 'top', 'center', 'bottom'</li>
</ul>
</div>

<div class="worked-example">
<h4>Formatted Labels</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4, 5], [2, 4, 1, 3, 5], marker='o')

ax.set_xlabel('Time (seconds)',
              fontsize=14,
              fontweight='bold',
              color='#e6edf3')

ax.set_ylabel('Temperature (°C)',
              fontsize=14,
              fontweight='bold',
              color='#e6edf3')

ax.set_title('Temperature Over Time',
             fontsize=16,
             fontweight='bold',
             pad=20)

fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Best Practice</h4>
<p>Always include units in axis labels. This prevents misinterpretation and makes your plot immediately understandable.</p>
</div>
'''
    },
    {
        'id': 'custom_02_legends',
        'title': 'Legends: Identifying Multiple Series',
        'body': '''
<div class="concept-box">
<h3>Legends: Essential for Multiple Series</h3>
<p>A legend maps visual elements (colors, markers, lines) to data series. Always use legends when plotting multiple datasets.</p>
</div>

<div class="worked-example">
<h4>Basic Legend</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4], [1, 2, 1, 3], label='Series A')
ax.plot([1, 2, 3, 4], [2, 1, 3, 2], label='Series B')
ax.plot([1, 2, 3, 4], [3, 3, 2, 1], label='Series C')

# Create legend
ax.legend()

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Legend Positioning and Styling</h3>
<ul>
<li><code>loc</code>: position ('best', 'upper left', 'lower right', etc.)</li>
<li><code>fontsize</code>: text size</li>
<li><code>ncol</code>: number of columns</li>
<li><code>frameon</code>: show/hide frame border</li>
<li><code>fancybox</code>: rounded vs sharp corners</li>
<li><code>shadow</code>: add drop shadow</li>
</ul>
</div>

<div class="worked-example">
<h4>Customized Legend</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4], [1, 2, 1, 3], label='Series A', linewidth=2)
ax.plot([1, 2, 3, 4], [2, 1, 3, 2], label='Series B', linewidth=2)
ax.plot([1, 2, 3, 4], [3, 3, 2, 1], label='Series C', linewidth=2)

# Customized legend
ax.legend(loc='upper left',
          fontsize=11,
          frameon=True,
          fancybox=True,
          shadow=True,
          title='Data Series')

fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>Avoid Legend Overlap</h4>
<p>Place legends where they don't obscure data. Use <code>loc='best'</code> to let matplotlib choose automatically.</p>
</div>
'''
    },
    {
        'id': 'custom_03_colors_and_styles',
        'title': 'Colors, Line Styles, and Markers',
        'body': '''
<div class="concept-box">
<h3>Working with Colors</h3>
<p>Matplotlib supports multiple color specification methods:</p>
<ul>
<li><strong>Named colors:</strong> 'red', 'blue', 'green'</li>
<li><strong>Hex codes:</strong> '#FF0000', '#4f8ef7'</li>
<li><strong>RGB tuples:</strong> (1.0, 0, 0) or (255, 0, 0)</li>
<li><strong>Single letters:</strong> 'r', 'b', 'g', 'k' (red, blue, green, black)</li>
</ul>
</div>

<div class="worked-example">
<h4>Color Examples</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Different color specifications
ax.plot([1, 2, 3], [1, 2, 1], color='red', label='Named color')
ax.plot([1, 2, 3], [2, 3, 2], color='#4f8ef7', label='Hex code')
ax.plot([1, 2, 3], [3, 4, 3], color=(0.2, 0.8, 0.3), label='RGB tuple')

ax.legend()
fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Line Styles and Markers</h3>
<p>Combine line styles and markers for clear visual differentiation:</p>
<ul>
<li><strong>Line styles:</strong> '-' (solid), '--' (dashed), ':' (dotted), '-.' (dash-dot)</li>
<li><strong>Markers:</strong> 'o' (circle), 's' (square), '^' (triangle), 'D' (diamond), '+' (plus)</li>
</ul>
</div>

<div class="worked-example">
<h4>Style Combinations</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4], [1, 2, 1, 3],
        linestyle='-', marker='o', color='#4f8ef7', label='Solid + circle')

ax.plot([1, 2, 3, 4], [2, 1, 3, 2],
        linestyle='--', marker='s', color='#58a6ff', label='Dashed + square')

ax.plot([1, 2, 3, 4], [3, 3, 2, 1],
        linestyle=':', marker='^', color='#3fb950', label='Dotted + triangle')

ax.legend()
fig.show()
</code></pre>
</div>

<div class="success-box">
<h4>Dark Theme Considerations</h4>
<p>On dark backgrounds, use bright colors. The palette (#4f8ef7, #58a6ff, #3fb950, #f85149) works well on #0d1117 backgrounds.</p>
</div>
'''
    },
    {
        'id': 'custom_04_tick_formatting',
        'title': 'Customizing Ticks and Tick Labels',
        'body': '''
<div class="concept-box">
<h3>Ticks: The Small Details Matter</h3>
<p>Ticks are the marks on axes. Control their position, labels, and formatting for professional-looking plots.</p>
</div>

<div class="worked-example">
<h4>Custom Tick Positions and Labels</h4>
<pre><code>import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

ax.plot(x, y, marker='o')

# Set custom x-tick positions and labels
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May'])

# Set custom y-ticks
ax.set_yticks([0, 10, 20, 30])

fig.show()
</code></pre>
</div>

<div class="concept-box">
<h3>Tick Formatting</h3>
<ul>
<li><code>set_major_locator()</code>: control major tick positions</li>
<li><code>set_minor_locator()</code>: control minor tick positions</li>
<li><code>tick_params()</code>: format tick label size, rotation, colors</li>
<li><code>xticks(rotation=45)</code>: rotate labels to avoid overlap</li>
</ul>
</div>

<div class="worked-example">
<h4>Formatted Ticks</h4>
<pre><code>import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5]
y = [1000, 2000, 1500, 3000, 2500]

ax.plot(x, y, marker='o')

# Format y-axis labels as thousands
def thousands(x, pos):
    return f'{int(x/1000)}K'

formatter = FuncFormatter(thousands)
ax.yaxis.set_major_formatter(formatter)

# Rotate x-labels
plt.xticks(rotation=45)

fig.show()
</code></pre>
</div>

<div class="warning-box">
<h4>Avoid Overlapping Labels</h4>
<p>When x-axis labels overlap, rotate them (45° or 90°) or use smaller font. Unreadable ticks defeat the purpose of a plot.</p>
</div>
'''
    }
]
