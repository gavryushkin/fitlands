from models_HIV_2007 import datafile_hiv_process
from scipy.stats import ranksums
import numpy


__author__ = "@gavruskin"


def rank_sum(measurements):
    output = [1, 2, 3, 4, 5, 6, 7, 8]
    done = False
    while not done:
        done = True
        for i in range(len(measurements) - 1):
            if ranksums(measurements[output[i] - 1], measurements[output[i + 1] - 1])[0] > 0:
                output[i], output[i+1] = output[i+1], output[i]
                done = False
    for i in range(len(measurements) - 1):
        print ranksums(measurements[output[i] - 1], measurements[output[i + 1] - 1])
    return output


f = datafile_hiv_process()
rs = rank_sum(f)
print
print rs
print
for i in range(len(rs)):
    print numpy.mean(f[rs[i] - 1])
