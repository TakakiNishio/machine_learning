import numpy as np
import math
import matplotlib.pyplot as plt

#import scripts
import data_generator as dg
import methods as m

#main function
if __name__ == '__main__':

    n = 100
    real_beta = [2.6,4.3]
    dataset = dg.data_generator(n,real_beta)
    searched_beta = m.random_search(dataset,real_beta)
    #searched_beta = m.newton_method(dataset,real_beta)
    result_data = m.h(n,searched_beta)
    print "last_beta : " + str(searched_beta)
    plt.show()
