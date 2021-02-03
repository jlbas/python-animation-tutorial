"""
Animation: Scaling a circle fixed at the origin
"""

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Circle

# --------------------------------------------------------------------------------------------------
# Initialize the parameters
# --------------------------------------------------------------------------------------------------

dt = 0.01               # Simulation timestep (s)
radius = 1              # Current radius value
d_radius = 1            # Rate of change (units/s)
radius_log = [radius]   # Array to keep track of simulation data

# --------------------------------------------------------------------------------------------------
# Simulation
#
# Here, we scale the circle to its max and min size. At every timestep, we keep track of the radius
# by appending it to our radius_log list.
# --------------------------------------------------------------------------------------------------

while radius < 5:
    radius += dt * d_radius
    radius_log.append(radius)

d_radius = -d_radius

while radius > 1:
    radius += dt * d_radius
    radius_log.append(radius)

# --------------------------------------------------------------------------------------------------
# Animation
#
# Using the simulation data, we now make the animation
# --------------------------------------------------------------------------------------------------

# Initialize the plot
fig, ax = plt.subplots()
ax.axis('scaled')
ax.axis([-6, 6, -6, 6])

# Create and add a circle patch to the axis
patch = Circle((0, 0), radius=radius_log[0])
ax.add_patch(patch)

# Animation function to update and return the patch at each frame
def animate(i):
    patch.radius = radius_log[i]
    return patch,

# Specify the animation parameters and call animate
ani = FuncAnimation(fig,
    animate,
    frames=len(radius_log),     # Total number of frames in the animation
    interval=int(1000 * dt),    # Set the length of each frame (milliseconds)
    blit=True,                  # Only update patches that have changed (more efficient)
    repeat=False)               # Only play the animation once

# Play the animation
plt.show()

# Uncomment to save the animation to a local file
# ani.save('/path/to/save/animation.mp4', writer=FFMpegWriter(fps=int(1/dt)))
