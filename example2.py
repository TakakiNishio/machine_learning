import numpy as np
import matplotlib.pyplot as plt

alpha = 2
beta = 3
gamma = 4

mu = 0.1

def f(a,b):
    ansf = alpha + beta * a + gamma * b  
    return ansf

def h(a,b,c,d,e):
    ansh = c +  d * a + e * b
    return ansh

x1 = np.random.rand()
x2 = np.random.rand()

theta0 = np.random.rand()
theta1 = np.random.rand()
theta2 = np.random.rand()

y = f(x1,x2)

yh = h(x1,x2,theta0,theta1,theta2)

print "alpha : " + str(alpha) + "  beta : " + str(beta) + "  gamma : " + str(gamma)
print "theta0 : " + str(theta0) + "  theta1 : " + str(theta1) + "  theta2 : " + str(theta2)

for i in range(0,1000):
    theta0 = theta0 - mu * (theta0 + theta1 * x1 + theta2 * x2 - y) * x1
    theta1 = theta1 - mu * (theta0 + theta1 * x1 + theta2 * x2 - y) * x2
    theta2 = theta2 - mu * (theta0 + theta1 * x1 + theta2 * x2 - y)
    print "theta0 : " + str(theta0) + "  theta1 : " + str(theta1) + "  theta2 : " + str(theta2)
print x1
print x2
