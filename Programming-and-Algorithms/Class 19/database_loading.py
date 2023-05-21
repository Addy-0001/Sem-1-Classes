import numpy as np


def listing_function(filename):
    data = np.loadtxt(filename, delimiter=" ",  dtype=str)
    listdata = data
    lst = []
    for individual in listdata:
        lst.append(individual)
    # print(lst)
    count = 0
    for i in lst: 
        for j in lst:
            if j == i: 
                count += 1
    print(count)
