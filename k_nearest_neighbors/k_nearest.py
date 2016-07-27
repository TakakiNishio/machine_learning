import numpy as np
import math
import matplotlib.pyplot as plt

#origin function
def f(x1,x2):
    alpha = 2
    beta  = 5
    gamma = 3
    d = 2
    ans = alpha + beta * x1 + gamma * x2 + np.random.rand() * d
    return ans

#create data
def data_generator(data_n):
    l = 7
    raw_data = []
    plt.figure(1)
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

        raw_data.append([[x1,x2],y])
    return raw_data


#separate into two datasets
#def separate_train_set(raw_data,train_n):
#    train_set = []
#    for i in range(0,train_n):
#        training_set.append(raw_data[i])
#    return train_set

#def separate_test_set(raw_data,test_n):
#    test_set = []
#    for i in range(0,test_n):
#        test_set.append(raw_data[i+train_n])
#    return test_set


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

    error_rate = 1.0 - float(success)/test_n

    print "k : "+ str(k) + "  error : " + str(error_rate) + "[%]"

    return error_rate

if __name__ == '__main__':

    n = 2000
    train_n = 1800
    test_n = 200

    data = []
    training_set = []
    test_set = []

    k_list = []
    error_list = []
    k_variation = 20

    data = data_generator(n)

    #training_set = separate_train_set(data,train_n)
    #test_set = separate_test_set(data,test_n,train_n)

    for i in range(0,train_n):
        training_set.append(data[i])

    for i in range(0,test_n):
        test_set.append(data[i+train_n])

    plt.figure(2)

    for k in range(1,k_variation+1):
        k_list.append(k)
        error_list.append(estimation(training_set,test_set,k))
        plt.plot(k_list,error_list,"ro-")

    plt.show()
