"""
==================
 Simple Plot demo
==================

This is an example showing how to create a simple plot with some options.

Author: Pierre Charpentier
"""

# Import the lybrary
import matplotlib.pyplot as plt

# Create the Figure and Axes objects
fig, ax = plt.subplots()

# The data set
X = [0, 1, 2, 3, 4, 5] # X coordinate of each points.
Y = [1, -1, 1, -1, 1, -1] # Y coordinate of each points.

# Graph labels and colors options

# Create the Graph
ax.plot(X, Y)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (m)')
ax.set_title('Position tracking over time')

# Draw and display your Figure
plt.show()
