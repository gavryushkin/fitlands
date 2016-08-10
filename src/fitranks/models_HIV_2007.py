import pandas
import numpy
from three_way_epistasis import get_next_ordering, ordering_to_fitness, check_for_epistasis, epistasis_positive, ranks_to_values
import datetime

__author__ = '@gavruskin'


# Gives the probability P(sigma[0] < ... < sigma[7]).
def ranking_probability(sigma, fit_data_list):
    # Now use that P(sigma) = \Pi_{sigma[j-1] < sigma[j]} p_{j-1, j}, that is, we multiply all such p_{j-1,j}.
    # For that, use P(W_i < W_j) = \sum_x P(W_j = x) * P(W_i < x):
    output = 1
    for j in range(1, len(sigma)):  # \Pi__j
            probability_j = 1 / float(len(fit_data_list[sigma[j] - 1]))  # This is P(W_j = x), which does not depend on x.
            # Now find probability_i = \sum_x P(W_i < x):
            count = 0
            for s in range(len(fit_data_list[sigma[j] - 1])):
                for r in range(len(fit_data_list[sigma[j-1] - 1])):
                    if fit_data_list[sigma[j-1] - 1][r] < fit_data_list[sigma[j] - 1][s]:
                        count += 1
            probability_i = count / float(len(fit_data_list[sigma[j - 1] - 1]))
            # Multiply the running probability by p_{i, j}:
            output *= probability_j * probability_i
    return output


# Comparison model (second in the paper):
def epistasis_probability_from_comparisons(fit_data_list):
    epistasis_probability = 0
    # Loop through all rankings (they called fitness in the code):
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    positives = {1, 5, 6, 7}
    negatives = {4, 3, 2, 8}
    repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
    if epistasis_positive(fitness, positives, negatives, repetitions):
        epistasis_probability = ranking_probability(fitness, fit_data_list)
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        if epistasis_positive(fitness, positives, negatives, repetitions):
            epistasis_probability += ranking_probability(fitness, fit_data_list)
    return epistasis_probability


# Does the same thing as above but uses the file with precomputed rankings that imply epistasis.
# Faster by about 2 seconds on the data used for testing (from [BPS2007]).
def epistasis_probability_from_comparisons_fast(fit_data_list):
    with open("outputs/circuit_u_111_orders_signed.txt") as epistasis_rankings_file:
        epistasis_probability = 0
        prob_max = 0  # TODO: rm all occurrences of prob_max
        for signed_ranking in epistasis_rankings_file:
            if signed_ranking.endswith("+\n"):
                signed_ranking = signed_ranking.replace("[", "")
                signed_ranking = signed_ranking.replace("]", "")
                signed_ranking = signed_ranking.replace("+\n", "")
                fitness = [int(r) for r in signed_ranking.split(", ")]
                prob = ranking_probability(fitness, fit_data_list)
                epistasis_probability += prob
                if prob > prob_max:
                    prob_max = prob
    epistasis_rankings_file.close()
    print "Max prob: " + str(prob_max)
    return epistasis_probability


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

print "Starting fast method at:"
print datetime.datetime.now()
print
print epistasis_probability_from_comparisons_fast(f)
print
print "Finishing fast method at:"
print datetime.datetime.now()
