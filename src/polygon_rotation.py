"""
Animation: Rotating a polygon
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Polygon

# --------------------------------------------------------------------------------------------------
# Initialize the parameters
# --------------------------------------------------------------------------------------------------

dt = 0.01                                           # Simulation timestep (s)
coords = np.array([[-1,0], [0,1], [1,0], [0,-1]])   # Shape coordinates
th = 0                                              # Current heading
th_log = [th]                                       # Array to keep track of simulation data
w = 1                                               # Angular velocity of the shape (rad/s)

# --------------------------------------------------------------------------------------------------
# Simulation
#
# Here, we rotate the shape 2*pi rads. At every timestep, we only have to keep track of the heading 
# by appending it to our th_log list.
# --------------------------------------------------------------------------------------------------

while th < 2 * np.pi:
    th += dt * w
    th_log.append(th)

# --------------------------------------------------------------------------------------------------
# Animation
#
# Using the simulation data, we now make the animation. Using a rotation matrix on the polygon's 
# orignal coordinates, we set the coordinates as specified by the corresponding heading value.
# --------------------------------------------------------------------------------------------------

fig, ax = plt.subplots()
ax.axis('scaled')
ax.axis([-2, 2, -2, 2])

# Create and add a polygon patch to the axis
patch = Polygon(coords)
ax.add_patch(patch)

# Return the coordinates after a rotation of 'th' radians
def rotate(coords, th):
    rot_matrix = np.array([[np.cos(th), np.sin(th)],
                        [-np.sin(th), np.cos(th)]])
    return coords @ rot_matrix

# Animation function to update and return the patch at each frame
def animate(i):
    patch.set_xy(rotate(coords, th_log[i]))
    return patch,

# Specify the animation parameters and call animate
ani = FuncAnimation(fig,
    animate,
    frames=len(th_log),        # Total number of frames in the animation
    interval=int(1000 * dt),    # Set the length of each frame (milliseconds)
    blit=True,                  # Only update patches that have changed (more efficient)
    repeat=False)               # Only play the animation once

# Play the animation
plt.show()

# Uncomment to save the animation to a local file
# ani.save('/path/to/save/animation.mp4', writer=FFMpegWriter(fps=int(1/dt)))
