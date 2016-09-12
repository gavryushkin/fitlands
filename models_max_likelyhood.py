import random
from models_HIV_2007 import datafile_hiv_process
from three_way_epistasis import epistasis_positive, epistasis_negative
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


def simulate_competition_experiment_from_hiv_data():
    f = datafile_hiv_process()
    f_means = [numpy.mean(f[0]), numpy.mean(f[1]), numpy.mean(f[2]), numpy.mean(f[3]),
               numpy.mean(f[4]), numpy.mean(f[5]), numpy.mean(f[6]), numpy.mean(f[7])]
    mean_f0 = numpy.mean(f[0])
    f_means_shifted = numpy.subtract(f_means, [mean_f0, mean_f0, mean_f0, mean_f0, mean_f0, mean_f0, mean_f0, mean_f0])
    print(f_means)
    print(f_means_shifted)
    rankings = sample_ranks_randomly(f, 1000)
    for s in range(len(rankings)):
        print(rankings[s])


def get_epistasis_from_top_10_maxlik_rankings():
    g = [[8, 3, 6, 2, 7, 4, 5, 1],
         [8, 3, 7, 2, 4, 6, 5, 1],
         [2, 8, 6, 4, 7, 3, 5, 1],
         [8, 2, 3, 6, 7, 4, 5, 1],
         [2, 3, 8, 7, 6, 4, 1, 5],
         [7, 3, 6, 5, 8, 2, 4, 1],
         [8, 3, 7, 6, 5, 2, 1, 4],
         [8, 4, 5, 7, 2, 6, 3, 1],
         [2, 8, 5, 4, 3, 7, 6, 1],
         [8, 2, 3, 7, 6, 5, 4, 1]]
    positives = {1, 5, 6, 7}
    negatives = {4, 3, 2, 8}
    repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(len(g)):
        print(g[i])
        print("Positive epistasis: " + str(epistasis_positive(g[i], positives, negatives, repetitions)))
        print("Negative epistasis: " + str(epistasis_negative(g[i], positives, negatives, repetitions)))
        print
