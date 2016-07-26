import numpy as np
import matplotlib.pyplot as plt

l = 6
theta0 = 2
theta1 = 5
theta2 = 3

def f(x1,x2):
    ans = theta0 * x1 + theta1 * x2 + theta2
    return ans

for i in range(0,100):
    x1 = np.random.rand()
    x2 = np.random.rand()
    h = f(x1,x2)
    if h > l:
        plt.plot(x1,x2,"bo")
    else:
        plt.plot(x1,x2,"ro")

plt.show()
