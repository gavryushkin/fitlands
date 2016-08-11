import pandas
import numpy
from three_way_epistasis import get_next_ordering, ordering_to_fitness, epistasis_positive, epistasis_negative,\
    check_for_epistasis
import datetime

__author__ = '@gavruskin'


# Gives the probability P(sigma[0] < ... < sigma[7]).
def ranking_probability(sigma, fit_data_list):
    # Now use that P(sigma) = \Pi_{sigma[j-1] < sigma[j]} p_{j-1, j}, that is, we multiply all such p_{j-1,j}.
    # For that, use P(W_i < W_j) = \sum_x P(W_j = x) * P(W_i < x):
    output = 1
    for j in range(1, len(sigma)):  # \Pi__j
            probability_j = 1 / float(len(fit_data_list[sigma[j] - 1]))  # That's P(W_j = x), which doesn't depend on x.
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


# Comparison model (second in the paper).
# Returns the triple t of counts of rankings with higher than cutoff_prob probability such that
# t[0] imply positive epistasis, t[1] negative, t[2] the total number of such rankings.
def epistasis_probability_from_comparisons(fit_data_list, cutoff_prob):
    epistasis_probability = 0
    # Loop through all rankings (they called fitness in the code):
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    positives = {1, 5, 6, 7}
    negatives = {4, 3, 2, 8}
    repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
    prob = ranking_probability(fitness, fit_data_list)
    positive_count = 0
    negative_count = 0
    total_count = 0
    if prob > cutoff_prob:
        if epistasis_positive(fitness, positives, negatives, repetitions):
            positive_count += 1
            total_count +=1
        elif epistasis_negative(fitness, positives, negatives, repetitions):
            negative_count += 1
            total_count += 1
        else:
            total_count += 1
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        prob = ranking_probability(fitness, fit_data_list)
        if prob > cutoff_prob:
            if epistasis_positive(fitness, positives, negatives, repetitions):
                positive_count += 1
                total_count += 1
            elif epistasis_negative(fitness, positives, negatives, repetitions):
                negative_count += 1
                total_count += 1
            else:
                total_count += 1
    print "Number of positives: " + str(positive_count)
    print "Number of negative: " + str(negative_count)
    print "Total number: " + str(total_count)
    return [positive_count, negative_count, total_count]


# Uses precomputed rankings that imply epistasis and returns those that have probability higher than cutoff_prob and
# imply positive epistasis with their probabilities.
def epistasis_probability_from_comparisons_fast(fit_data_list, cutoff_prob):
    with open("outputs/circuit_u_111_orders_signed.txt") as epistasis_rankings_file:
        epistasis_probability = []
        ranking = []
        for signed_ranking in epistasis_rankings_file:
            # if signed_ranking.endswith("+\n"):
                signed_ranking_clean = signed_ranking.replace("[", "")
                signed_ranking_clean = signed_ranking_clean.replace("]", "")
                signed_ranking_clean = signed_ranking_clean.replace("+\n", "")
                signed_ranking_clean = signed_ranking_clean.replace("-\n", "")
                fitness = [int(r) for r in signed_ranking_clean.split(", ")]
                prob = ranking_probability(fitness, fit_data_list)
                if prob > cutoff_prob:
                    epistasis_probability.append(prob)
                    ranking.append(signed_ranking)
    epistasis_rankings_file.close()
    return [epistasis_probability, ranking]


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

# print "Starting at:"
# print datetime.datetime.now()
# print
# ret = epistasis_probability_from_comparisons_fast(f)
# # for i in range(len(ret[0])):
# #     print ret[0][i]
# #     print ret[1][i]
# print len(ret[0])
# count_neg = 0
# for i in range(len(ret[0])):
#     if ret[1][i].endswith("-\n"):
#         count_neg += 1
# print count_neg
# print
# print "Finishing at:"
# print datetime.datetime.now()

cl_to_m = closest_to_mean(f, 5)
all_combinations = []
for v0 in range(5):
    for v1 in range(5):
        for v2 in range(5):
            for v3 in range(5):
                for v4 in range(5):
                    for v5 in range(5):
                        for v6 in range(5):
                            for v7 in range(5):
                                fitness = [cl_to_m[v0][0], cl_to_m[v1][1], cl_to_m[v2][2], cl_to_m[v3][3],
                                           cl_to_m[v4][4], cl_to_m[v5][5], cl_to_m[v6][6], cl_to_m[v7][7]]
                                if len(set(fitness)) == 8:  # Drop tuples with identical ranks.
                                    all_combinations.append(fitness)
count_positive = 0
count_negative = 0
actual_epi_count = 0
for i in range(len(all_combinations)):
    a = all_combinations[i]
    if a[0] + a[4] + a[5] + a[6] - a[1] - a[2] - a[3] - a[7] > 0:
        actual_epi_count += 1
    check = check_for_epistasis(all_combinations[i])
    if check[0]:
        count_positive += 1
    elif check[1]:
        count_negative += 1
counts = [actual_epi_count, count_positive, count_negative, len(all_combinations)]
print "Actual count of positive epistasis profiles: " + str(counts[0])
print "Rank-positive counts: " + str(counts[1])
print "Rank-negative counts: " + str(counts[2])
print "Total counts: " + str(counts[3])

print
print "Starting at:"
print datetime.datetime.now()
print
threshold_prob = 0.0184
print "Threshold probability: " + str(threshold_prob)
t = epistasis_probability_from_comparisons(f, threshold_prob)
epi_prob = (t[0] + t[1]) / float(t[2])
print "Epistasis probability: " + str(epi_prob)
print
print "Finishing at:"
print datetime.datetime.now()
