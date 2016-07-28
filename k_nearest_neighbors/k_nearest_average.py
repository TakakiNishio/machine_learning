import numpy as np
import math
import matplotlib.pyplot as plt


#define function
def f(x1,x2,d):
    alpha = 2
    beta  = 5
    gamma = 3
    ans = alpha + beta * x1 + gamma * x2 + np.random.rand() * d
    return ans


#create data
def data_generator(data_n,d):
    l = 7
    raw_data = []
    for i in range(0,data_n):
        x1 = np.random.rand()
        x2 = np.random.rand()
        h = f(x1,x2,d)
        if h > l:
            y = 1
        else:
            y = 0

        raw_data.append([[x1,x2],y])
    return raw_data


#estimation (k-neighbors)
def estimation(training_set,test_set,k):

    y = []
    yh = []

    for i in range(0,len(test_set)):
        dist_list = []
        min_dist = 1000
        sum_y = 0
        for j in range(0,len(training_set)):
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

    #success_counter
    success = 0
    for i in range(0,test_n):
        if test_set[i][1] == yh[i]:
            success = success + 1

    error_rate = (1.0 - float(success)/test_n) * 100

    return error_rate


#main function
if __name__ == '__main__':

    N = 10
    k_max = 151
    data_n = 2000
    train_n = 1800
    test_n = 200
    disturbance = 2
    k_list = []
    error_list = []

    for k in range(1,k_max+1):
        k_list.append(k)
        error_sum = 0
        for i in range(0,N):

            data = []
            training_set = []
            test_set = []

            data = data_generator(data_n,disturbance)

            for m in range(0,train_n):
                training_set.append(data[m])

            for n in range(0,test_n):
                test_set.append(data[n+train_n])

            error_rate = estimation(training_set,test_set,k)
            #print error_rate
            error_sum = error_sum + error_rate

        error_list.append(error_sum/N)

        print "k : "+ str(k) + "  error_average : " + str(error_sum/N) + "[%]"

plt.figure(1)
plt.plot(k_list,error_list,"ro-")
plt.show()
