import numpy as np
import math
import matplotlib.pyplot as plt


#define a function
def f(x):
    beta = [1.4, 3.2]
    ans = x * beta[1] + beta[0] + np.random.normal(0,5)
    return ans


#create a dataset
def data_generator(data_n):
    data = []
    for i in range(0,data_n):
        y = f(i)
        data.append([i,y])
        plt.figure(1)
        plt.plot(i,y,"ro")
    return data


#calculate RSS
def rss(data,beta_n):
    r_n = 0
    for i in range(0,len(data)):
        r_n = r_n + (data[i][1] - (data[i][0] * beta_n[1] + beta_n[0]))**2
    r_n/=float(len(data))
    return r_n


#linear_regression -- random search
def random_search(data):
    first_beta = [1,1]
    last_beta = [1,1]
    beta_n = [1,1]
    min_r_n = rss(data,first_beta)
    plt.figure(2)
    plt.plot(1.4,3.2,"ro")
    for i in range(0,100000):
        beta_n[0] = 10 * np.random.rand()
        beta_n[1] = 10 * np.random.rand()
        r_n = rss(data,beta_n)
        if r_n < min_r_n :
            min_r_n = r_n
            last_beta[0] = beta_n[0]
            last_beta[1] = beta_n[1]
            print "beta0 : "+ str(last_beta[0]) + "  beta1 : "+ str(last_beta[1]) + "  RSS : "+ str(min_r_n)
            plt.figure(2)
            plt.plot(last_beta[0],last_beta[1],"bo")
    plt.plot(last_beta[0],last_beta[1],"go")
    return last_beta


#confirm the result of estimation
def h(n,last_beta):
    h = []
    for i in range(0,n):
        y = last_beta[1] * i + last_beta[0]
        h.append(y)
        plt.figure(1)
        plt.plot(i,y,"bo")
    return h


#main function
if __name__ == '__main__':

    n = 100
    dataset = data_generator(n)
    searched_beta = random_search(dataset)
    result_data = h(n,searched_beta)
    print "last_beta : "+ str(searched_beta)
    plt.show()
