"""
Animation: Scaling a circle fixed at the origin
"""

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Circle

# Shape and simulation parameters
dt = 0.01               # Simulation timestep (s)
radius = 1              # Current radius value
d_radius = 1            # Rate of change (units/s)
radius_log = [radius]   # Array to keep track of simulation data

# Scale the circle to its max and min size, logging the radius at each timestep
while radius < 5:
    radius += dt * d_radius
    radius_log.append(radius)
while radius > 1:
    radius -= dt * d_radius
    radius_log.append(radius)

# Initialize the plot
fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
ax.axis('scaled')
ax.axis([-6, 6, -6, 6])
ax.axis('off')

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
    frames=len(radius_log),
    interval=int(1000 * dt),
    blit=True,
    repeat=False)

plt.show()

ani.save('../media/circle_scaling.gif', writer=FFMpegWriter(fps=50))
