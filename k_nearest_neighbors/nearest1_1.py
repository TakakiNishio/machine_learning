import numpy as np
import math
import matplotlib.pyplot as plt

l = 6

alpha = 2
beta  = 5
gamma = 3

data = []
training_set = []
test_set = []

yh = []

data_n = 2000
train_n = 3
test_n = 200

def f(x1,x2):
    ans = alpha + beta * x1 + gamma * x2
    return ans

#create data
for i in range(0,data_n):
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


#separate into two datasets
for i in range(0,train_n):
   training_set.append(data[i])

for i in range(0,test_n):
    test_set.append(data[i+train_n])


#estimation (1-neighbors)
for i in range(0,test_n):
    min_dist = 1000
    for j in range(0,train_n):
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
for i in range(0,test_n):
    if test_set[i][1] == yh[i]:
        success = success + 1

success_rate = float(success)/test_n

print ""
print "success points : " + str(success) + "  success_rate : " + str(success_rate)
plt.show()
