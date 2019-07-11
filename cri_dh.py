from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def func1(x, y):
    critical_ratio = (200.0 * (x - 380.0) / 3300.0 + 50.0) / 1000.0
    critical_damage_scale = (200.0 * (x - 380.0) / 3300.0 + 1400.) / 1000.0
    critical_up = critical_ratio * critical_damage_scale + (1.0 - critical_ratio) * 1.0
    directhit_ratio = (550.0 * (y - 380.0) / 3300.0) / 1000.0
    directhit_damage_scale = 1.25
    directhit_up = directhit_ratio * directhit_damage_scale + (1.0 - directhit_ratio) * 1.0
    return (critical_up * directhit_up - 1.0) * 100.0


x = np.arange(0, 5000, 10)
y = np.arange(0, 5000, 10)

X, Y = np.meshgrid(x, y)
Z = func1(X, Y)

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("cri")
ax.set_ylabel("dh")
ax.set_zlabel("%")

ax.plot_wireframe(X, Y, Z)

surf = ax.plot_surface(X, Y, Z, cmap='bwr', linewidth=0)
fig.colorbar(surf)

plt.show()

