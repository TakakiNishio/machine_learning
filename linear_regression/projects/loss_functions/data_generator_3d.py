import numpy as np
import math

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


#function for the figure
def generate_cmap(colors):
    values = range(len(colors))
    vmax = np.ceil(np.max(values))
    color_list = []
    for v, c in zip(values, colors):
        color_list.append( ( v/ vmax, c) )
    return LinearSegmentedColormap.from_list('custom_cmap', color_list)


#calculate LOSS
#LOSS-1
def loss_1(beta0,beta1):
    loss = -5 * (beta1**2) * np.exp(-(beta0**2) - 0.2 * (beta1**2))
    return loss


#LOSS-2
def loss_2(beta0,beta1):
    loss = - 3 * np.exp(-(((beta0 - 2)**2)/3)-(((beta1 - 2)**2)/3)) - 4 * np.exp(-(((beta0 + 2)**2)/4)-(((beta1 + 2)**2)/4))
    return loss


#visualization of LOSS
def visualization_in_3d(data):

    beta0 = np.arange(-5,5,0.1)
    beta1 = np.arange(-5,5,0.1)

    X,Y = np.meshgrid(beta0,beta1)

    #Z = loss_1(X,Y)
    Z = loss_2(X,Y)

    fig = plt.figure(1)
    ax = Axes3D(fig)
    ax.plot_wireframe(X,Y,Z)
    ax.set_xlabel("beta_0")
    ax.set_ylabel("beta_1")
    ax.set_zlabel("LOSS")

    fig = plt.figure(2)
    cm = generate_cmap(['blue', 'indigo', 'red'])
    interval = [i/10. -10 for i in range(1000)]
    im = plt.contour(X, Y, Z, interval, alpha=0.5, cmap=cm)
    fig.colorbar(im)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    #plt.show()

    return data
