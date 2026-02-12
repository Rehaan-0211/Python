import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8, 5))

ax.set_title("Live Data Animation", fontsize=14)
ax.set_xlabel("Time")
ax.set_ylabel("Value")
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.grid(alpha=0.3)

x_data = []
y_data = []

line, = ax.plot([], [], color="cyan", linewidth=2)

ax.set_facecolor("#111111")
fig.patch.set_facecolor("#111111")
ax.tick_params(colors='white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.title.set_color('white')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                    init_func=init, blit=True, interval=50)

plt.show()
