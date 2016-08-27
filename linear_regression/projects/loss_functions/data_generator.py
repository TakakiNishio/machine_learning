import numpy as np
import math
import matplotlib.pyplot as plt


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
