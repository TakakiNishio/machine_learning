import numpy as np
import math
import matplotlib.pyplot as plt


#calculate RSS
def rss(data,beta_n):
    r_n = 0
    for i in range(0,len(data)):
        r_n = r_n + (data[i][1] - (data[i][0] * beta_n[1] + beta_n[0]))**2
    r_n/=float(len(data))
    return r_n


#calculate RSS
def prss_pbeta(data,beta_n):
    pr_pb = [1,1]
    pr_pb0 = 0
    pr_pb1 = 0
    for i in range(0,len(data)):
        pr_pb0 = pr_pb0 + (-2 * (data[i][1] - (data[i][0] * beta_n[1] + beta_n[0])))
        pr_pb1 = pr_pb0 + (-2 * data[i][0] * (data[i][1] - (data[i][0] * beta_n[1] + beta_n[0])))
    pr_pb[0] = pr_pb0/float(len(data))
    pr_pb[1] = pr_pb1/float(len(data))
    return pr_pb


#linear_regression -- random search
def random_search(data,real_beta):
    beta0_list = []
    beta1_list = []
    first_beta = [1,1]
    last_beta = [1,1]
    beta_n = [1,1]
    min_r_n = rss(data,first_beta)
    plt.figure(2)
    plt.plot(real_beta[0],real_beta[1],"ro",label = "real beta")
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


#linear_regression -- Newton method
def newton_method(data,real_beta):
    delta = 0.2
    beta0_list = []
    beta1_list = []
    first_beta = [1,1]
    last_beta = [1,1]
    beta_n = [0,0]
    pr_pb = []
    rss_n = rss(data,first_beta)
    plt.figure(2)
    plt.plot(real_beta[0],real_beta[1],"ro",label = "real beta")
    for i in range(0,1000):
        rss_n = rss(data,beta_n)
        pr_pb = prss_pbeta(data,beta_n)
        pr_pb0 = pr_pb[0]
        pr_pb1 = pr_pb[1]

        if pr_pb0 < 0:
            beta_n[0] += delta
        elif pr_pb > 0:
            beta_n[0] -= delta

        if pr_pb1 < 0:
            beta_n[1] += delta
        elif pr_pb > 0:
            beta_n[1] -= delta

        print "Epoc : " + str(i) + "  pr_pb0 : " + str(pr_pb0) + "  pr_pb1 : " + str(pr_pb1) + "  RSS : " + str(rss_n)

        beta0_list.append(beta_n[0])
        beta1_list.append(beta_n[1])

    plt.figure(2)
    plt.plot(beta0_list,beta1_list,"bo-",label = "estimated beta")
    plt.xlabel("beta_0", fontsize=20, fontname='serif')
    plt.ylabel("beta_1", fontsize=20, fontname='serif')
    plt.legend()

    return beta_n


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
