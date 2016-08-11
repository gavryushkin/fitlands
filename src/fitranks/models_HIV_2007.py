import pandas
import numpy
from three_way_epistasis import get_next_ordering, ordering_to_fitness, epistasis_positive, epistasis_negative,\
    check_for_epistasis
import datetime

__author__ = '@gavruskin'


# Gives the probabilities p_{i, j}, where {i, j} \subset {1, ..., 8} given trial lists using
# P(W_i < W_j) = \sum_x P(W_j = x) * P(W_i < x):
def ranking_probabilities(fit_data_list):
    output = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(8):
        for i in range(8):
            if i != j:
                probability_j = 1 / float(len(fit_data_list[j]))  # That's P(W_j = x), which doesn't depend on x.
                # Now find probability_i = \sum_x P(W_i < x):
                count = 0
                for x in range(len(fit_data_list[j])):  # This is \sum_x
                    for r in range(len(fit_data_list[i])):
                        if fit_data_list[i][r] < fit_data_list[j][x]:
                            count += 1
                probability_i = count / float(len(fit_data_list[i]))
                # Multiply the running probability by p_{i, j}:
                output[i][j] = probability_j * probability_i
    return output


# The comparison (competition experiment) model.
# Returns the probability of epistasis given the trial data.
def epistasis_probability_from_comparisons(fit_data_list):
    # Compute probabilities P(W_i < W_j) = p_{i,j}:
    p_ij = ranking_probabilities(fit_data_list)
    # Loop through all rankings:
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    ranking = [1, 2, 3, 4, 5, 6, 7, 8]
    positives = {1, 5, 6, 7}
    negatives = {4, 3, 2, 8}
    repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
    positive_epi_prob = 0
    negative_epi_prob = 0
    total_prob_mass = 0
    # Compute the probability of the ranking as \Pi_{i, j} p_{i, j}.
    rank_prob = 1
    for j in range(len(ranking)):
        for i in range(j):
            rank_prob *= p_ij[ranking[i] - 1][ranking[j] - 1]
    total_prob_mass += rank_prob
    if epistasis_positive(ranking, positives, negatives, repetitions):
        positive_epi_prob += rank_prob
    elif epistasis_negative(ranking, positives, negatives, repetitions):
        negative_epi_prob += rank_prob
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        ranking = ordering_to_fitness(ordering)
        rank_prob = 1
        for j in range(len(ranking)):
            for i in range(j):
                rank_prob *= p_ij[ranking[i] - 1][ranking[j] - 1]
        total_prob_mass += rank_prob
        if epistasis_positive(ranking, positives, negatives, repetitions):
            positive_epi_prob += rank_prob
        elif epistasis_negative(ranking, positives, negatives, repetitions):
            negative_epi_prob += rank_prob
    positive_epi_prob /= total_prob_mass
    negative_epi_prob /= total_prob_mass
    print "Probability of positive epistasis: " + str(positive_epi_prob)
    print "Probability of negative epistasis: " + str(negative_epi_prob)
    return [positive_epi_prob, negative_epi_prob]


# Returns k closest entries to the mean for each component of fit_data_list:
def closest_to_mean(fit_data_list, k, mean_type="mean"):
    if mean_type == "mean":
        means = [numpy.mean(fit_data_list[j]) for j in range(len(fit_data_list))]
    elif mean_type == "median":
        means = [numpy.median(fit_data_list[j]) for j in range(len(fit_data_list))]
    fit_data_list_copy = []
    for r in range(len(fit_data_list)):
        copy = [fit_data_list[r][l] for l in range(len(fit_data_list[r]))]
        fit_data_list_copy.append(copy)
    output = []
    for r in range(k):
        output_r = []
        for l in range(len(means)):
            close_to_mean_index = (numpy.abs(fit_data_list_copy[l] - means[l])).argmin()
            output_r.append(fit_data_list_copy[l][close_to_mean_index])
            del fit_data_list_copy[l][close_to_mean_index]
        output.append(output_r)
    return output


sigma_mean = [8, 3, 2, 6, 7, 5, 4, 1]
data_file = "2007_HIV_data.csv"
mutations = [["L", "M"],  # mutations: L to M, M to V, t to Y
                 ["M", "V"],
                 ["t", "Y"]]
sites = [88, 244, 275]  # sites: PRO L90M, RT M184V, RT T215Y


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
for m in range(size):
    if (values.iloc[m, 2] == mutations[0][0]) & (values.iloc[m, 3] == mutations[1][0]) &\
            (values.iloc[m, 4] == mutations[2][0]):
        f000.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][0]) & (values.iloc[m, 3] == mutations[1][0]) &\
            (values.iloc[m, 4] == mutations[2][1]):
        f001.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][0]) & (values.iloc[m, 3] == mutations[1][1]) &\
            (values.iloc[m, 4] == mutations[2][0]):
        f010.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][1]) & (values.iloc[m, 3] == mutations[1][0]) &\
            (values.iloc[m, 4] == mutations[2][0]):
        f100.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][0]) & (values.iloc[m, 3] == mutations[1][1]) &\
            (values.iloc[m, 4] == mutations[2][1]):
        f011.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][1]) & (values.iloc[m, 3] == mutations[1][0]) &\
            (values.iloc[m, 4] == mutations[2][1]):
        f101.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][1]) & (values.iloc[m, 3] == mutations[1][1]) &\
            (values.iloc[m, 4] == mutations[2][0]):
        f110.append(values.iloc[m, 0])
    elif (values.iloc[m, 2] == mutations[0][1]) & (values.iloc[m, 3] == mutations[1][1]) &\
            (values.iloc[m, 4] == mutations[2][1]):
        f111.append(values.iloc[m, 0])
f = [f000, f001, f010, f100, f011, f101, f110, f111]


epistasis_probability_from_comparisons(f)
