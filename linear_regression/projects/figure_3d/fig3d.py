import numpy as np
import pylab as pl
import math as mt

from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()
ax = Axes3D(fig)

X = np.arange(-2*mt.pi, 2*mt.pi, 0.25)
Y = np.arange(-2*mt.pi, 2*mt.pi, 0.25)

X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = - np.exp(-0.25 * R) * np.cos(2 * R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=pl.cm.hot)
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=pl.cm.hot)
ax.set_zlim(-2, 2)

pl.show()
