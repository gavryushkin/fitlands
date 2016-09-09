from models_HIV_2007 import datafile_hiv_process
from partial_order_interaction import convert_to_genotype
from scipy.stats import ranksums


__author__ = "@gavruskin"


# Returns the ordering of vectors of measurements according to Wilcoxon rank-sum test:
def rank_sum(measurements):
    output = [1, 2, 3, 4, 5, 6, 7, 8]
    done = False
    while not done:
        done = True
        for i in range(len(measurements) - 1):
            if ranksums(measurements[output[i] - 1], measurements[output[i + 1] - 1])[0] < 0:
                output[i], output[i+1] = output[i+1], output[i]
                done = False
    for i in range(len(measurements) - 1):
        print ranksums(measurements[output[i] - 1], measurements[output[i + 1] - 1])
    return output


# Produce the ranking:
f = datafile_hiv_process()
rs = rank_sum(f)
print
print convert_to_genotype(rs)