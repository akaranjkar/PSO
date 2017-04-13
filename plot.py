import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(111,projection='3d')

x1 = np.arange(-5,5,0.5)
x2 = np.arange(-5,5,0.5)
x1,x2 = np.meshgrid(x1,x2)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(0,50)
y = (x1**2) + (x2**2)

ax.plot_surface(x1,x2,y,rstride=1,cstride=1,cmap='gnuplot')
# ax.plot_wireframe(x1, x2, y, rstride=1, cstride=1)
plt.figtext(0.5,0.95,"Sphere function",size="xx-large",ha='center')
plt.show()

# test = [[2.0,2.0],
#         [3.5,1.5],
#         [0.0,0.0]]
#
# test = [[random.uniform(-5.0,5.0),random.uniform(-5.0,5.0)] for _ in range(20)]
#
# # ax.plot_surface(x1,x2,y,rstride=1,cstride=1,cmap='BuGn')
# for p in test:
#     ax.plot_surface(x1, x2, y, rstride=1, cstride=1, cmap='BuGn')
#     ax.scatter(p[0],p[1])
#     plt.pause(1)
#     plt.cla()