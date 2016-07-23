import numpy as np
import math
import matplotlib.pyplot as plt

l = 6

theta0 = 2
theta1 = 5
theta2 = 3

data = []

def f(x1,x2):
    ans = theta0 * x1 + theta1 * x2 + theta2
    return ans

for i in range(0,2000):
    x1 = np.random.rand()
    x2 = np.random.rand()
    h = f(x1,x2)
    if h > l:
        y = 1
        plt.plot(x1,x2,"bo")
    else:
        y = 0
        plt.plot(x1,x2,"ro")

    data.append([[x1,x2],y])

#for i in range(0,1799):
   # dmin = 1
    for j in range(1,1800):
        dist = math.sqrt(((data[j][0][0] - data[i][0][0] ) ** 2) + ((data[j][0][1] - data[i][0][1]) ** 2))
        if dist <  dmin:
            dmin = dist
            index = j
    

#for i in range(len(data)):
   # print data[i]



plt.show()
