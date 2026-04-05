MINDMAP = {
    "concepts": [
        {"title": "Basic Plotting", "points": [
            "plt.plot(x, y) for line charts",
            "plt.scatter(x, y) for scatter plots",
            "plt.bar(x, heights), plt.hist(data, bins=N)",
            "plt.show() to display, plt.savefig('file.png') to save",
        ]},
        {"title": "Customisation", "points": [
            "Labels: plt.xlabel(), plt.ylabel(), plt.title()",
            "Legend: plt.legend(), use label= in plot calls",
            "Colours, markers, linestyles: 'r--o', color='blue', marker='x'",
            "Grid: plt.grid(True)",
        ]},
        {"title": "Subplots", "points": [
            "fig, axes = plt.subplots(nrows, ncols)",
            "Access each: axes[0].plot(...) or axes[0,1].plot(...)",
            "fig.tight_layout() to prevent overlap",
        ]},
        {"title": "Advanced Plots", "points": [
            "plt.contourf() for heatmaps, plt.imshow() for images",
            "3D: from mpl_toolkits.mplot3d import Axes3D",
            "Seaborn integration for statistical plots",
        ]},
    ],
    "formulas": [],
    "tips": [
        "Use fig, ax = plt.subplots() pattern for better control than plt.plot()",
        "Always label axes and add a title — plots should be self-explanatory",
        "Use plt.style.use('seaborn') or other styles for better-looking defaults",
    ],
}
