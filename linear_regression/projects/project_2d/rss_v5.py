import numpy as np
import math
import matplotlib.pyplot as plt


#define a function
def f(x):
    beta = [1.4, 3.2]
    ans = x * beta[1] + beta[0] + np.random.normal(0,0.01)
    return ans


#create a dataset
def data_generator(data_n):
    data = []
    x = []
    y = []
    for i in range(0,data_n):
        x.append(np.random.rand())

    for i in range(0,data_n):
        y.append(f(x[i]))

    plt.figure(1)
    plt.plot(x,y,"ro",label = "generated data")
    plt.xlabel("x", fontsize=20, fontname='serif')
    plt.ylabel("y", fontsize=20, fontname='serif')
    data = zip(x,y)
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
    beta0_list = []
    beta1_list = []
    first_beta = [1,1]
    last_beta = [1,1]
    beta_n = [1,1]
    min_r_n = rss(data,first_beta)
    plt.figure(2)
    plt.plot(1.4,3.2,"ro",label = "real beta")
    for i in range(0,1000):
        beta_n[0] = 10 * np.random.rand()
        beta_n[1] = 10 * np.random.rand()
        r_n = rss(data,beta_n)
        if r_n < min_r_n :
            min_r_n = r_n
            last_beta[0] = beta_n[0]
            last_beta[1] = beta_n[1]
            beta0_list.append(last_beta[0])
            beta1_list.append(last_beta[1])
            print "beta0 : "+ str(last_beta[0]) + "  beta1 : "+ str(last_beta[1]) + "  RSS : "+ str(min_r_n)
    plt.figure(2)
    plt.plot(beta0_list,beta1_list,"bo-",label = "estimated beta")
    plt.xlabel("beta_0", fontsize=20, fontname='serif')
    plt.ylabel("beta_1", fontsize=20, fontname='serif')
    plt.legend()
    return last_beta


#confirm the result of estimation
def h(n,last_beta):
    h_x = []
    h_y = []
    for i in range(0,2):
        y = last_beta[1] * i + last_beta[0]
        h_x.append(i)
        h_y.append(y)
    plt.figure(1)
    plt.plot(h_x,h_y,"b-",label = "estimated data")
    plt.legend()
    return h


#main function
if __name__ == '__main__':

    n = 100
    dataset = data_generator(n)
    searched_beta = random_search(dataset)
    result_data = h(n,searched_beta)
    print "last_beta : "+ str(searched_beta)
    plt.show()
