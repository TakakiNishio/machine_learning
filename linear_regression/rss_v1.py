import numpy as np
import math
import matplotlib.pyplot as plt


#define a function
def f(x):
    beta = [1.4, 3.2]
    ans = x * beta[1] + beta[0] # + np.random.normal(0,5)
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
    for i in range(len(data)):
        r_n = r_n + (data[i][1] - (data[i][0] * beta_n[1] + beta_n[0]))**2
    return r_n


#linear_regression -- random search
def random_search(data):
    first_beta = [1,1]
    last_beta =[]
    min_r_n = rss(data,first_beta)
    for i in range(0,100):
        beta_n = [np.random.rand(),np.random.rand()]
        r_n = rss(data,beta_n)
        if r_n < min_r_n :
            min_r_n = r_n
            last_beta = beta_n
    return last_beta


#main function
if __name__ == '__main__':

    dataset = data_generator(20)
    rss_0 = rss(dataset,[1.4,3.2])
    print "rss_0 : " + str(rss_0)
   #searched_beta = random_search(dataset)
   #print "beta : "+ str(searched_beta)
    plt.show()
