import numpy as np
import math
import matplotlib.pyplot as plt

import data_generator_3d as dg3


#calculate partial differential of LOSS-1
def prss_pbeta_1(beta_n):
    pr_pb = [0,0]
    pr_pb0 = 0
    pr_pb1 = 0
    pr_pb0 = 10 * beta_n[0] * (beta_n[1]**2) * np.exp(-(beta_n[0]**2) - 0.2 * (beta_n[1]**2))
    pr_pb1 = (2 * (beta_n[1]**3) - 10 * beta_n[1]) * np.exp(-(beta_n[0]**2) - 0.2 * (beta_n[1]**2))
    pr_pb[0] = pr_pb0
    pr_pb[1] = pr_pb1
    return pr_pb


#linear_regression -- random search
def random_search(first_beta):
    beta0_list = []
    beta1_list = []
    beta0_list.append(first_beta[0])
    beta1_list.append(first_beta[1])
    last_beta = [0,0]
    beta_n = [0,0]
    min_loss = dg3.loss_1(first_beta[0],first_beta[1])
    for i in range(0,1000):
        beta_n[0] = 10 * np.random.rand() - 5
        beta_n[1] = 10 * np.random.rand() - 5
        loss_n = dg3.loss_1(beta_n[0],beta_n[1])
        if loss_n < min_loss :
            min_loss = loss_n
            last_beta[0] = beta_n[0]
            last_beta[1] = beta_n[1]
            beta0_list.append(last_beta[0])
            beta1_list.append(last_beta[1])
            print "beta0 : "+ str(last_beta[0]) + "  beta1 : "+ str(last_beta[1]) + "  LOSS : "+ str(min_loss)
    plt.figure(2)
    plt.plot(beta0_list,beta1_list,"ro-",label = "estimated beta")
   # plt.plot(last_beta[0],last_beta[1],"go",label = "last beta")
    plt.xlabel("beta_0", fontsize=20, fontname='serif')
    plt.ylabel("beta_1", fontsize=20, fontname='serif')
    plt.legend()
    return last_beta


#linear_regression -- Newton method
def newton_method(first_beta):
    delta = 0.1
    epoch = 1000
    beta0_list = []
    beta1_list = []
    beta0_list.append(first_beta[0])
    beta1_list.append(first_beta[1])
    beta_n = first_beta
    pr_pb = []
    for i in range(0,epoch):
        loss_n = dg3.loss_1(beta_n[0],beta_n[1])
        pr_pb = prss_pbeta_1(beta_n)
        pr_pb0 = pr_pb[0]
        pr_pb1 = pr_pb[1]

        beta_n[0] += delta * (-pr_pb[0])
        beta_n[1] += delta * (-pr_pb[1])

        print "Epoch : " + str(i) + "  beta0 : " + str(beta_n[0]) + "  beta1 : " + str(beta_n[1]) + "  LOSS : " + str(loss_n)

        beta0_list.append(beta_n[0])
        beta1_list.append(beta_n[1])

    plt.figure(2)
    plt.plot(beta0_list,beta1_list,"ro-",label = "estimated beta")
    plt.xlabel("beta_0", fontsize=20, fontname='serif')
    plt.ylabel("beta_1", fontsize=20, fontname='serif')
    plt.legend()

    return beta_n

#linear_regression -- Newton method
def simple_newton_method(first_beta):
    delta = 0.000001
    beta0_list = []
    beta1_list = []
    beta_n = [1,1]
    pr_pb = []
    for i in range(0,600):
        rss_n = rss(data,beta_n)
        pr_pb = prss_pbeta_1(beta_n)
        pr_pb0 = pr_pb[0]
        pr_pb1 = pr_pb[1]

        if pr_pb0 < 0:
            beta_n[0] += delta
        elif pr_pb0 > 0:
            beta_n[0] -= delta

        if pr_pb1 < 0:
            beta_n[1] += delta
        elif pr_pb1 > 0:
            beta_n[1] -= delta

        print "Epoch : " + str(i) + "  beta0 : " + str(beta_n[0]) + "  beta1 : " + str(beta_n[1]) + "  RSS : " + str(rss_n)

        beta0_list.append(beta_n[0])
        beta1_list.append(beta_n[1])

    plt.figure(2)
    plt.plot(beta0_list,beta1_list,"bo-",label = "estimated beta")
    plt.xlabel("beta_0", fontsize=20, fontname='serif')
    plt.ylabel("beta_1", fontsize=20, fontname='serif')
    plt.legend()

    return beta_n
