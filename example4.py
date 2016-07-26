import numpy as np

alpha = 2
beta = 5
gamma = 3

data = []

def f(a,b):
    ansf = alpha + beta * a + gamma * b
    return ansf

def h(a,b,c,d,e):
    ansh = c + d * a + e * b
    return ansh

for i in range(0,100):

    x1 = np.random.rand()
    x2 = np.random.rand()
    y = f(x1,x2)

    data.append([[x1,x2],y])

theta0 = np.random.rand()
theta1 = np.random.rand()
theta2 = np.random.rand()

mu = 0.01

for i in range(0,500):

    ptheta0 = 0
    ptheta1 = 0
    ptheta2 = 0

    for j in range(len(data)):
        ptheta0 = ptheta0 + (theta0 + theta1 * data[j][0][0] + theta2 * data[j][0][1] - data[j][1])
        ptheta1 = ptheta1 + (theta0 + theta1 * data[j][0][0] + theta2 * data[j][0][1] - data[j][1]) * data[j][0][0]
        ptheta2 = ptheta2 + (theta0 + theta1 * data[j][0][0] + theta2 * data[j][0][1] - data[j][1]) * data[j][0][1]

    theta0 = theta0 - mu * ptheta0
    theta1 = theta1 - mu * ptheta1
    theta2 = theta2 - mu * ptheta2
    print "Epoch : " + str(i) + "  theta0 : " + str(theta0) + "  theta1 : " + str(theta1) + "  theta2 : " + str(theta2) +  "  h : " + str(h(0.2,0.3,theta0,theta1,theta2))

print ""
print "theta0 : " + str(theta0) + "  theta1 : " + str(theta1) + "  theta2 : " + str(theta2)
print ""
print "alpha : " + str(alpha) + "  beta : " + str(beta) + " gamma : " + str(gamma)
print ""
print "f : " + str(f(0.2,0.3))
print ""
