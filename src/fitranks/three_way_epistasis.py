import random


__author__ = '@gavruskin'


# The number of tries to detect zero epistasis.
N = 1000000


def get_next_ordering(x):
    y = x
    for i in range(len(x)):
        if x[i] < 8 - i - 1:
            y[i] = x[i] + 1
            return y
    return False
