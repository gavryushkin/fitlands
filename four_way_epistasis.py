from three_way_epistasis import epistasis_positive, epistasis_negative
import numpy


__author__ = "@gavruskin"


# Returns a pair of truth values for positive and (then) negative epistasis
# derived from ranks induces by fitness vector v.
# For three way epistasis: positives = {1, 5, 6, 7}, negatives = {4, 3, 2, 8}, repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
# w_0000, w_0001 ... enumerated in the order of binary numbers, e.g. w_1000 comes after w_0111.
def check_for_epistasis_four_way(v, details=False):
    positives = {1, 4, 6, 7, 10, 11, 13, 16}
    negatives = {2, 3, 5, 6, 9, 12, 14, 15}
    repetitions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    v_sorted = sorted(v)
    w = []
    for i in range(len(v)):
        w.append(v.index(v_sorted[i]) + 1)
    epi_pos = epistasis_positive(w, positives, negatives, repetitions)
    epi_neg = epistasis_negative(w, positives, negatives, repetitions)
    output = [epi_pos, epi_neg]
    if details:
        epi = epi_neg or epi_pos
        print(numpy.round(v, 3))
        print(numpy.round(v_sorted, 3))
        print(w)
        print(epi)
        print(output)
        print
    return output
