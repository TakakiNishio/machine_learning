import numpy as np
import math
import matplotlib.pyplot as plt

import data_generator as dg
import methods as m

if __name__ == '__main__':

    n = 100
    dataset = dg.data_generator(n)
    searched_beta = m.random_search(dataset)
    result_data = m.h(n,searched_beta)
    print "last_beta : " + str(searched_beta)
    plt.show()
