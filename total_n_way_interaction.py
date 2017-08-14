from three_way_epistasis import epistasis_positive, epistasis_negative
from four_way_interactions import get_geno_number

__author__ = '@gavruskin'


def total_n_way_interaction(w):
    w = [get_geno_number(i) for i in w]
    n = len(w)
    repetitions = [1] * n
    positives = set()
    negatives = set()
    for genotype in w:
        genotype = bin(genotype - 1)
        number_ones = genotype[2:].count("1")
        if number_ones % 2 == 0:
            positives.add(get_geno_number(genotype))
        else:
            negatives.add(get_geno_number(genotype))
    output = [epistasis_positive(w, positives, negatives, repetitions),
              epistasis_negative(w, positives, negatives, repetitions)]
    return output
