import numpy as np
import math
import matplotlib.pyplot as plt


#import scripts
import data_generator_3d as dg3
import methods as m

#main function
if __name__ == '__main__':

    #first_beta = [0,0]
    first_beta = [1,1]
    #first_beta = [-1,-1]

    LOSS = dg3.visualization_in_3d(1)

    #searched_beta = m.random_search(first_beta)
    searched_beta = m.newton_method(first_beta)

    print "last_beta : " + str(searched_beta)
    plt.show()
