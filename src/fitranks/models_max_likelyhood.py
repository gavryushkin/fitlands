import random
from models_HIV_2007 import datafile_hiv_process


__author__ = '@gavruskin'


# Given fitness profile (e.g. one returned by datafile_hiv_process),
# generates n samples of pairwise comparisons of fitness.
# The output is a matrix with i,j being the number of times i has higher fitness than j.
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
rankings = sample_ranks_randomly(f, 1000000)
for s in range(len(rankings)):
    print rankings[s]
