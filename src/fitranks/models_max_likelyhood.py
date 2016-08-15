import random
from models_HIV_2007 import datafile_hiv_process
import numpy

__author__ = '@gavruskin'


# Given fitness profile (e.g. one returned by datafile_hiv_process),
# generates n samples of pairwise comparisons of fitness.
# The output is a matrix with i,j being the number of times i has higher fitness than j.
# w_000 = w[0], w_001 = w[1], w_010 = w[2], w_100 = w[3], w_011 = w[4], w_101 = w[5], w_110 = w[6], w_111 = w[7]:^
def sample_ranks_randomly(fit_data_list, n):
    output = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
    for sample in range(n):
        for i in range(8):
            for j in range(8):
                if i != j:
                    f_i_rand = random.randint(0, len(fit_data_list[i]) - 1)
                    f_j_rand = random.randint(0, len(fit_data_list[j]) - 1)
                    if fit_data_list[i][f_i_rand] > fit_data_list[j][f_j_rand]:
                        output[i][j] += 1
                    elif fit_data_list[i][f_i_rand] < fit_data_list[j][f_j_rand]:
                        output[j][i] += 1
    return output


f = datafile_hiv_process()
f_means = [numpy.mean(f[0]), numpy.mean(f[1]), numpy.mean(f[2]), numpy.mean(f[3]),
           numpy.mean(f[4]), numpy.mean(f[5]), numpy.mean(f[6]), numpy.mean(f[7])]
mean_f0 = numpy.mean(f[0])
f_means_shifted = numpy.subtract(f_means, [mean_f0, mean_f0, mean_f0, mean_f0, mean_f0, mean_f0, mean_f0, mean_f0])
print f_means
print f_means_shifted
rankings = sample_ranks_randomly(f, 1000)
for s in range(len(rankings)):
    print rankings[s]
