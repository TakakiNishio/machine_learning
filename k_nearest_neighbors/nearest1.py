import numpy as np
import math
import matplotlib.pyplot as plt

l = 7

alpha = 2
beta  = 5
gamma = 3
d = 2

data = []
training_set = []
test_set = []

yh = []

def f(x1,x2):
    ans = alpha + beta * x1 + gamma * x2 + np.random.rand() * d
    return ans


#create data
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


n = 1800
#separate into two datasets
for i in range(0,n):
   training_set.append(data[i])

for i in range(0,200):
    test_set.append(data[i+1800])


#estimation
for i in range(0,200):
    min_dist = 100
    for j in range(0,1800):
        dist = math.sqrt(((test_set[i][0][0] - training_set[j][0][0])**2) +((test_set[i][0][1] - training_set[j][0][1])**2))

        if dist < min_dist:
            min_dist = dist
            min_index = j

    if training_set[min_index][1] == 1:
        yh.append(1)
    else:
        yh.append(0)

    print "No. " + str(i) + "  min_index: " + str(min_index) +   "  test_y: " + str(test_set[i][1]) + "  training_y: " + str(training_set[min_index][1]) + "  yh: " + str(yh[i])


#success_counter
success = 0
for i in range(0,200):
    if test_set[i][1] == yh[i]:
        success = success + 1

success_rate = float(success)/200

print ""
print "success points : " + str(success) + "  success_rate : " + str(success_rate)
plt.show()
