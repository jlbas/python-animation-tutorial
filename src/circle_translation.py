"""
Animation: Translating a circle along the x axis
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Circle

# Shape and simulation parameters
dt = 0.01                   # Simulation timestep (s)
radius = 1                  # Circle radius
pos = np.array([0.0, 0.0])  # Current position (x, y)
pos_log = [pos]             # Array to keep track of simulation data
v = np.array([3.0, 0.0])    # Speed of the circle (v_x, v_y)

# Translate the circle along the x axis, logging the position at each timestep
while pos[0] < 5:
    pos += dt * v
    pos_log.append(list(pos))
# Change direction
v = -v
while pos[0] > 0:
    pos += dt * v
    pos_log.append(list(pos))

# Initialize the plot
fig, ax = plt.subplots()
ax.axis('scaled')
ax.axis([-2, 7, -2, 2])

# Create and add a circle patch to the axis
patch = Circle((0, 0), radius=radius)
ax.add_patch(patch)

# Animation function to update and return the patch at each frame
def animate(i):
    patch.center = pos_log[i]
    return patch,

# Specify the animation parameters and call animate
ani = FuncAnimation(fig,
    animate,
    frames=len(pos_log),        # Total number of frames in the animation
    interval=int(1000 * dt),    # Set the length of each frame (milliseconds)
    blit=True,                  # Only update patches that have changed (more efficient)
    repeat=False)               # Only play the animation once

# Play the animation
plt.show()

# Uncomment to save the animation to a local file
# ani.save('/path/to/save/animation.mp4', writer=FFMpegWriter(fps=int(1/dt)))
