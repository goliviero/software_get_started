"""
==============
Bar color demo
==============

This is an example showing how to control bar color and legend entries
using the *color* and *label* parameters of `~matplotlib.pyplot.bar`.
Note that labels with a preceding underscore won't show up in the legend.

This Example have been taken from:
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py
"""

# Import the lybrary
import matplotlib.pyplot as plt

# Create the Figure and Axes objects
fig, ax = plt.subplots()

# The data set
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]

# Graph labels and colors options
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# Create the Graph
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

# Draw and display your Figure
plt.show()
