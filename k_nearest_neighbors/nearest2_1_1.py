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

data_n = 2000
train_n = 1800
test_n = 200

def f(x1,x2):
    ans = alpha + beta * x1 + gamma * x2
    return ans


#create data
for i in range(0,data_n):
    x1 = np.random.rand()
    x2 = np.random.rand()
    h = f(x1,x2)
    if h > np.random.rand() * 10:
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


#estimation (k-neighbors)

k = 5
y = []
yh = []

for i in range(0,test_n):
    dist_list = []
    min_dist = 1000
    sum_y = 0
    for j in range(0,train_n):
        dist = math.sqrt(((test_set[i][0][0] - training_set[j][0][0])**2) +((test_set[i][0][1] - training_set[j][0][1])**2))
        dist_list.append([dist,j])

    dist_list = sorted(dist_list)

    for n in range(0,k):
        index_y = dist_list[n][1]
        sum_y = sum_y + training_set[index_y][1]

    if sum_y > int(k/2)+1:
        yh.append(1)
    else:
        yh.append(0)

    print "No. " + str(i) + "  test_y : " + str(test_set[i][1]) + "  estimated_y : " + str(yh[i])


#success_counter
success = 0
for i in range(0,test_n):
    if test_set[i][1] == yh[i]:
        success = success + 1

success_rate = (float(success)/test_n) * 100

print ""
print "k : " + str(k)
print "success points : " + str(success) + "  success_rate : " + str(success_rate) + "[%]"
plt.show()
