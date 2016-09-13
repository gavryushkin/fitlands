from scipy.stats import ranksums
import math
import sys


__author__ = "@gavruskin"


# Returns the ordering of vectors of measurements according to Wilcoxon rank-sum test:
def rank_sum_3_sites(measurements):
    output = [1, 2, 3, 4, 5, 6, 7, 8]
    done = False
    while not done:
        done = True
        for i in range(len(measurements) - 1):
            if ranksums(measurements[output[i] - 1], measurements[output[i+1] - 1])[0] < 0:
                output[i], output[i+1] = output[i+1], output[i]
                done = False
    return output


# Does the same thing as rank_sum_3_sites but for an arbitrary number of sites.
# Unlike rank_sum_3_sites, produce the ranking of {0, ... n-1}.
# Unlike rank_sum_3_sites, takes a dictionary, where measurements["genotype"] == list of fitnesses, as an input.
def rank_sum_n_sites(measurements):
    if math.frexp(len(measurements))[0] != 0.5:
        print("rank_sum_n_sites received an input of length %s, which is not equal to the number of genotypes."
              "Quitting." % len(measurements))
        sys.exit()
    output_indices = []
    for genotype in measurements:
        output_indices.append(measurements.keys().index(genotype))
    done = False
    while not done:
        done = True
        for i in range(len(measurements) - 1):
            if ranksums(measurements[measurements.keys()[output_indices[i]]],
                        measurements[measurements.keys()[output_indices[i+1]]])[0] < 0:
                output_indices[i], output_indices[i + 1] = output_indices[i + 1], output_indices[i]
                done = False
    output = []
    for index in output_indices:
        output.append(measurements.keys()[index])
    return output
