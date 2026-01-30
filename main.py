import numpy as np
import matplotlib.pyplot as plt

# Physical constants and variables (YOU CAN EDIT THIS!)
dt = 0.01       # Time step (s)
total_time = 50.0 # Total duration (s)
steps = int(total_time / dt)

# initializing arrays
t = np.linspace(0, total_time, steps)
x = np.zeros(steps)
v = np.zeros(steps)

# initializing motion, values given in problem
x[0] = 0.0      # Starting height (m)
v[0] = 0.0      # Initial velocity (m/s)

# VARIABLES TO FIND FROM THE PROBLEM
zero_velocity_index = -1
final_position = None

# Euler method simulation/loop
for i in range(1, steps):
    # Velocity update:
    v[i] = np.exp(-t[i]**2/100) * (t[i]+10*np.sin(np.pi*t[i]))
    x[i] = x[i-1] + v[i] * dt

    if zero_velocity_index == -1 and i > 1: # we want to know when the velocity
                                            # is zero AFTER the first point in
                                            # time
      if v[i-1] >= 0 and v[i] <= 0: # slope looks like \
        zero_velocity_index = i # rounding to the top of the time interval

      if v[i-1] <= 0 and v[i] >= 0: # slope looks like /
        zero_velocity_index = i

# finishing the solve
zero_velocity_time = zero_velocity_index * dt

# plotting with matplotlib (plt)
fig, axs = plt.subplots(2, 2)
plt.subplots_adjust(hspace=0.7, wspace=0.4)

axs[0][0].plot([0, min(x.size+1, zero_velocity_index*2) * dt],
            [x[zero_velocity_index], x[zero_velocity_index]],
            color='red',
            linestyle='--',
            linewidth=1
)
axs[0][0].plot(
    t[:min(x.size+1, zero_velocity_index*2)],
    x[:min(x.size+1, zero_velocity_index*2)]
) # use reasonable window size

axs[0][0].set_title("Finding part (a)")
axs[0][0].set_xlabel("Time (s)")
axs[0][0].set_ylabel("X-position (m)")
axs[0][0].grid(True)

print(f"""The first time that the object has a velocity of 0 after 0 sec is at
t = {zero_velocity_time}s, at position {x[zero_velocity_index]:.3g}m.
      """)

# plot full graph of position vs time
axs[1][0].plot(
    t[:x.size+1],
    x[:x.size+1]
)

axs[1][0].set_title("X-position vs time")
axs[1][0].set_xlabel("Time (s)")
axs[1][0].set_ylabel("X-position (m)")
axs[1][0].grid(True)

# column 2 (velocity vs time graphs)

axs[0][1].plot([0, min(x.size+1, zero_velocity_index*2) * dt],
            [v[zero_velocity_index], v[zero_velocity_index]],
            color='red',
            linestyle='--',
            linewidth=1
)
axs[0][1].plot(
    t[:min(x.size+1, zero_velocity_index*2)],
    v[:min(x.size+1, zero_velocity_index*2)]
) # use reasonable window size

axs[0][1].set_title("Finding part (a)")
axs[0][1].set_xlabel("Time (s)")
axs[0][1].set_ylabel("X-velocity (m/s)")
axs[0][1].grid(True)

# plot full graph of velocity vs time
axs[1][1].plot(
    t[:x.size+1],
    v[:x.size+1]
)

axs[1][1].set_title("X-velocity vs time")
axs[1][1].set_xlabel("Time (s)")
axs[1][1].set_ylabel("X-velocity (m)")
axs[1][1].grid(True)
