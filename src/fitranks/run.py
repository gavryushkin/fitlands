from three_way_epistasis import epistasis, epistasis_positive, epistasis_negative


__author__ = '@gavruskin'


# w_000 = w[1], w_001 = w[2], w_010 = w[3], w_100 = w[4], w_011 = w[5], w_101 = w[6], w_110 = w[7], w_111 = w[8]
# For three way epistasis: positives = {1, 5, 6, 7}, negatives = {4, 3, 2, 8}, repetitions = [1, 1, 1, 1, 1, 1, 1, 1]


v = [1.580, 1.195, 1.133, 1.441, 1.430, 1.232, 1.294, 1.045]
positives = {1, 5, 6, 7}
negatives = {4, 3, 2, 8}
repetitions = [1, 1, 1, 1, 1, 1, 1, 1]  # TODO: Possibly make these default values.

v_sorted = sorted(v)
w = []
for i in range(len(v)):
    w.append(v.index(v_sorted[i]) + 1)

print epistasis_positive(w, positives, negatives, repetitions)
