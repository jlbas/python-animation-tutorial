"""
Animation: 3-body simulation with partial trajectories

Initial conditions are taken from:
V. Szebehely and C. F. Peters (1967), "Complete solution of a general problem of three bodies", 
http://adsabs.harvard.edu/full/1967AJ.....72..876S
"""

import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Circle
from matplotlib.patches import Polygon

# --------------------------------------------------------------------------------------------------
# Initialize the parameters
# --------------------------------------------------------------------------------------------------

dt = 1E-5                                           # Simulation timestep (s)
tol = 1E-13                                         # ODE solver tolerance
sim_time = 70                                       # Length of simulation (s)
fps = 50                                            # Animation framerate
G = 1.0                                             # Gravitational constant
mass = [3, 4, 5]                                    # Mass of the bodies
init_pos = np.array([1, 3, -2, -1, 1, -1])          # (x1, y1, x2, y2, x3, y3)
init_vel = np.array([0, 0, 0, 0, 0, 0])             # (vx1, vy1, vx2, vy2, vx3, vy3)
init_state = np.concatenate((init_pos, init_vel))

# --------------------------------------------------------------------------------------------------
# Simulation
#
# Here we define the differential equations of our system and pass them along with the initial 
# conditions to the ODE solver. 
# --------------------------------------------------------------------------------------------------

def accel(m1, m2, r0, r1, r2):
    # Return the acceleration vector acting on a body resulting from the gravitational forces of the
    # other two
    r01 = r0 - r1
    r02 = r0 - r2
    r01_mag = np.linalg.norm(r01)
    r02_mag = np.linalg.norm(r02)
    return -G * (m1 * (r01 / r01_mag**3) + m2 * (r02 / r02_mag**3))

def body_eqs(t, state):
    # Return the system of 12 ODE's, where 'r' is the position vector and 'v' the velocity vector
    r0, r1, r2 = np.reshape(state[:6], (3, 2))
    r_dot = state[6:]
    v_dot = np.zeros(6)
    v_dot[0], v_dot[1] = accel(mass[1], mass[2], r0, r1, r2)
    v_dot[2], v_dot[3] = accel(mass[0], mass[2], r1, r0, r2)
    v_dot[4], v_dot[5] = accel(mass[0], mass[1], r2, r0, r1)
    return np.concatenate((r_dot, v_dot))

# Solve the system of differential equations
sol = solve_ivp(fun=body_eqs, 
        t_span=(0, sim_time),
        y0=init_state,
        t_eval=np.linspace(0, sim_time, int(sim_time/dt)),
        rtol=tol,
        atol=tol,
        method='DOP853')

# Downsample from the ODE solution to get our desired animation frame rate
step = int(1 / (fps * dt))
sol.y = sol.y[:,::step]

# Extract the positions from the solution
pos = np.dstack((sol.y[0:2], sol.y[2:4], sol.y[4:6])).T

# --------------------------------------------------------------------------------------------------
# Animation
#
# Using the simulation data, we now make the animation
# --------------------------------------------------------------------------------------------------

# Initialize the plot
fig, ax = plt.subplots()
ax.axis('scaled')
ax.axis([-5, 5, -5, 5])
fig.set_size_inches(6, 6)

colors = ["#D81B60", "#1E88E5", "#FFC107"]

# Create a bodies list containing a circle patch for each body and add to axis
bodies = []
for p, m, c in zip(pos, mass, colors):
    body = Circle(p[0], radius=m/30, color=c)
    ax.add_patch(body)
    bodies.append(body)

# Create a trajs list containing Polygon patches for the bodies' trajectories
trajs = []
for p, c in zip(pos, colors):
    traj = Polygon(p[0:2], 
                closed=False, 
                fill=False, 
                edgecolor=c, 
                capstyle='round', 
                linewidth=3, 
                zorder=0)
    ax.add_patch(traj)
    trajs.append(traj)

# Animation function to update and return the bodies and trajectories at each frame
def animate(i):
    for body, p in zip(bodies, pos):
        body.center = p[i]
    for traj, p in zip(trajs, pos):
        traj.set_xy(p[max(0, i-50):i])  
    # Concatenate the two lists before returning
    return bodies + trajs

# Specify the animation parameters and call animate
ani = FuncAnimation(fig,
    animate,
    frames=fps*sim_time,        # Total number of frames in the animation
    interval=1000/fps,          # Set the length of each frame (milliseconds)
    blit=True,                  # Only update patches that have changed (more efficient)
    repeat=False)               # Only play the animation once

# Play the animation
plt.show()

# Uncomment to save the animation to a local file
# ani.save('/path/to/save/animation.mp4', writer=FFMpegWriter(fps=fps))
