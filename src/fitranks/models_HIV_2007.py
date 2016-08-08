import pandas
import numpy
from three_way_epistasis import get_next_ordering, ordering_to_fitness

__author__ = '@gavruskin'


# Gives the probability P(sigma[0] < sigma[1]).
# TODO: test this.
def ranking_probability(sigma, data_file, mutations, sites):
    sites = [0] + [1] + sites  # This is specific to the data file. Column 0 contains fitness, column 1 names.
    values = pandas.read_csv(data_file, usecols=sites)
    values.iloc[:, 0] = numpy.log10(values.iloc[:, 0])  # log10 scale of fitness values.
    size = len(values.iloc[:, 1])
    f000 = []
    f001 = []
    f010 = []
    f100 = []
    f011 = []
    f101 = []
    f110 = []
    f111 = []
    for s in range(size):
        if (values.iloc[s, 2] == mutations[0][0]) & (values.iloc[s, 3] == mutations[1][0]) &\
                (values.iloc[s, 4] == mutations[2][0]):
            f000.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][0]) & (values.iloc[s, 3] == mutations[1][0]) &\
                (values.iloc[s, 4] == mutations[2][1]):
            f001.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][0]) & (values.iloc[s, 3] == mutations[1][1]) &\
                (values.iloc[s, 4] == mutations[2][0]):
            f010.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][1]) & (values.iloc[s, 3] == mutations[1][0]) &\
                (values.iloc[s, 4] == mutations[2][0]):
            f100.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][0]) & (values.iloc[s, 3] == mutations[1][1]) &\
                (values.iloc[s, 4] == mutations[2][1]):
            f011.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][1]) & (values.iloc[s, 3] == mutations[1][0]) &\
                (values.iloc[s, 4] == mutations[2][1]):
            f101.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][1]) & (values.iloc[s, 3] == mutations[1][1]) &\
                (values.iloc[s, 4] == mutations[2][0]):
            f110.append(values.iloc[s, 0])
        elif (values.iloc[s, 2] == mutations[0][1]) & (values.iloc[s, 3] == mutations[1][1]) &\
                (values.iloc[s, 4] == mutations[2][1]):
            f111.append(values.iloc[s, 0])
    f = [f000, f001, f010, f100, f011, f101, f110, f111]
    # Now use that P(sigma) = \Pi_{sigma[i] < sigma[j]} p_{i,j}, that is we multiply all such p_{i,j}.
    # For that, use P(W_i < W_j) = \sum_x P(W_j = x) * P(W_i < x):
    output = 1
    for j in range(len(sigma)):
        for i in range(j):
            probability_j = 1 / float(len(f[sigma[j] - 1]))  # This is P(W_j = x), which does not depend on x.
            # Now find probability_i = \sum_x P(W_i < x):
            count = 0
            for s in range(len(f[sigma[j] - 1])):
                for r in range(len(f[sigma[i] - 1])):
                    if f[sigma[i] - 1][r] < f[sigma[j] - 1][s]:
                        count += 1
            probability_i = count / float(len(f[sigma[i] - 1]))
            output *= probability_i * probability_j
    return output


# Testing:
sigma_mean = [8, 3, 2, 6, 7, 5, 4, 1]
HIV_data_file = "2007_HIV_data.csv"
mutations_BPS = [["L", "M"],  # mutations: L to M, M to V, t to Y
                 ["M", "V"],
                 ["t", "Y"]]
sites_BPS = [88, 244, 275]  # sites: PRO L90M, RT M184V, RT T215Y

# print ranking_probability(sigma_mean, HIV_data_file, mutations_BPS, sites_BPS)


# Comparison model (second in the paper):
def epistasis_probability_from_comparisons(data_file, mutations, sites):
    # Loop through all rankings (they called fitness in the code):
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    fitness_probability = ranking_probability(fitness, data_file, mutations,sites)
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        fitness_probability *= ranking_probability(fitness, data_file, mutations,sites)
    return fitness_probability


print epistasis_probability_from_comparisons(HIV_data_file, mutations_BPS, sites_BPS)
