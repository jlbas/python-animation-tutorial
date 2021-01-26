"""
Template file for a Python animation
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
# from matplotlib.patches import ...

# Specify your simulation and animation parameters
dt = 0.01       # Simulation timestep (s)
data_log = []   # List to keep track of your simulation data

# Simulate your interesting dynamical system
# while not robot.at_goal():
#     robot.discrete_integration_step()
#     data_log.append(robot.new_state)

# Initialize the plot
fig, ax = plt.subplots()
ax.axis('scaled')
# ax.axis([x_min, x_max, y_min, y_max])

# Create and add some patches to the axis
patch_list = [...]
for patch in patch_list:
    ax.add_patch(patch)

# Animation function to update and return multiple patches
def animate(i):
    for patch in patch_list:
        patch.some_transformation(data_log[i])
    return patch_list

# Animation function to update and return a single patch
# Notice the ',' in the return value since FuncAnimation expects an iterable
# def animate(i):
#     patch.some_transformation(data_log[i])
#     return patch,

# Specify the animation parameters and call animate
ani = FuncAnimation(fig,
    animate,
    frames=len(data_log),       # Total number of frames in the animation
    interval=int(1000 * dt),    # Set the length of each frame (milliseconds)
    blit=True,                  # Only update patches that have changed (more efficient)
    repeat=False)               # Only play the animation once

# Play the animation
# plt.show()

# Uncomment to save the animation to a local file
# ani.save('/path/to/save/animation.mp4', writer=FFMpegWriter(fps=50))
