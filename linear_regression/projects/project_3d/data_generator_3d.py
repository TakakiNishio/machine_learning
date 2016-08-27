import numpy as np
import math

import matplotlib.pyplot as plt

from matplotlib.colors import LinearSegmentedColormap

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm


def generate_cmap(colors):
    values = range(len(colors))
    vmax = np.ceil(np.max(values))
    color_list = []
    for v, c in zip(values, colors):
        color_list.append( ( v/ vmax, c) )
    return LinearSegmentedColormap.from_list('custom_cmap', color_list)


#define a function
def f(x,beta):
    ans = x * beta[1] + beta[0] + np.random.normal(0,0.01)
    return ans


#create a dataset
def data_generator(data_n,beta):
    data = []
    x = []
    y = []
    for i in range(0,data_n):
        x.append(np.random.rand())

    for i in range(0,data_n):
        y.append(f(x[i],beta))

    plt.figure(1)
    plt.plot(x,y,"ro",label = "generated data")
    plt.xlabel("x", fontsize=20, fontname='serif')
    plt.ylabel("y", fontsize=20, fontname='serif')
    data = zip(x,y)
    return data


#calculate LOSS
def rss(data,beta_n):
    r_n = 0
    for i in range(0,len(data)):
        r_n += (data[i][1] - (data[i][0] * beta_n[1] + beta_n[0]))**2
    r_n/=float(len(data))
    return r_n


#calculate LOSS
def loss(data,beta0,beta1):
    loss = 0
    for i in range(0,len(data)):
        loss += (data[i][1] - (data[i][0] * beta1 + beta0))**2
    loss /= float(len(data))
    return loss


#visualization of LOSS
def visualization_in_3d(data):

    beta0 = np.arange(-5,5,0.1)
    beta1 = np.arange(-5,5,0.1)

    X,Y = np.meshgrid(beta0,beta1)

    Z = loss(data,X,Y)

    fig = plt.figure(2)
    ax = Axes3D(fig)
    ax.plot_wireframe(X,Y,Z)

    fig = plt.figure(3)
    cm = generate_cmap(['blue', 'white', 'red'])
    interval = [i/10. -1 for i in range(1000)]
    im = plt.contour(X, Y, Z, interval, alpha=0.5, cmap=cm)
    fig.colorbar(im)
    plt.xlim(0, 5)
    plt.ylim(0, 5)
    #plt.show()

    return data
