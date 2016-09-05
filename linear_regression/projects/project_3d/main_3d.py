import numpy as np
import math
import matplotlib.pyplot as plt

#import scripts
import data_generator_3d as dg3
import methods as m

#main function
if __name__ == '__main__':

    n = 1000
    real_beta = [1.4,3.2]
    dataset = dg3.data_generator(n,real_beta)
    LOSS = dg3.visualization_in_3d(dataset)

    searched_beta = m.random_search(dataset,real_beta)
    #searched_beta = m.newton_method(dataset,real_beta)
    result_data = m.h(n,searched_beta)
    print "last_beta : " + str(searched_beta)
    plt.show()
