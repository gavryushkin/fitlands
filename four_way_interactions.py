from three_way_epistasis import epistasis_positive, epistasis_negative
import numpy

__author__ = '@gavruskin'


# Returns a pair of truth values for positive and (then) negative epistasis
# derived from ranks induces by fitness vector v.
# For three way epistasis: positives = {1, 5, 6, 7}, negatives = {4, 3, 2, 8}, repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
# w_0000, w_0001 ... enumerated in the order of binary numbers, e.g. w_1000 comes after w_0111.
def four_way_from_proxy(v, details=False):
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
        print("\n")
    return output


# Returns the number given binary sequence, for using in epistasis_positive and alike.
def get_geno_number(genotype_binary):
    genotype_binary = str(genotype_binary)
    genotype_number = int(genotype_binary, 2) + 1
    return genotype_number


# Returns a pair of truth values for positive and (then) negative epistasis derived from ranking w.
# For three way epistasis: positives = {1, 5, 6, 7}, negatives = {4, 3, 2, 8}, repetitions = [1, 1, 1, 1, 1, 1, 1, 1]
# w_0000, w_0001 ... enumerated in the order of binary numbers, e.g. w_1000 comes after w_0111:
# w = [0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]; indices:
# w = [   1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16]
# u0011 = 0000 + 0100 + 1000 + 1100 + 0011 + 0111 + 1011 + 1111 - 0001 - 0101 - 1001 - 1101 - 0010 - 0110 - 1010 - 1110
# u0101 = 0000 + 0010 + 1000 + 1010 + 0101 + 0111 + 1101 + 1111 - 0001 - 0011 - 1001 - 1011 - 0100 - 0110 - 1100 - 1110
# u0110 = 0000 + 0001 + 1000 + 1001 + 0110 + 0111 + 1110 + 1111 - 0010 - 0011 - 1010 - 1011 - 0100 - 0101 - 1100 - 1101
# u1001 = 0000 + 0010 + 0100 + 0110 + 1001 + 1011 + 1101 + 1111 - 0001 - 0011 - 0101 - 0111 - 1000 - 1010 - 1100 - 1110
# u1010 = 0000 + 0001 + 0100 + 0101 + 1010 + 1011 + 1110 + 1111 - 0010 - 0011 - 0110 - 0111 - 1000 - 1001 - 1100 - 1101
# u1100 = 0000 + 0001 + 0010 + 0011 + 1100 + 1101 + 1110 + 1111 - 0100 - 0101 - 0110 - 0111 - 1000 - 1001 - 1010 - 1011
# u0111 = 0000 + 1000 + 0011 + 1011 + 0101 + 1101 + 0110 + 1110 - 0001 - 1001 - 0010 - 1010 - 0100 - 1100 - 0111 - 1111
# u1011 = 0000 + 0100 + 0011 + 0111 + 1001 + 1101 + 1010 + 1110 - 0001 - 0101 - 0010 - 0110 - 1000 - 1100 - 1011 - 1111
# u1101 = 0000 + 0010 + 0101 + 0111 + 1001 + 1011 + 1100 + 1110 - 0001 - 0011 - 0100 - 0110 - 1000 - 1010 - 1101 - 1111
# u1110 = 0000 + 0001 + 0110 + 0111 + 1010 + 1011 + 1100 + 1101 - 0010 - 0011 - 0100 - 0101 - 1000 - 1001 - 1110 - 1111
# u1111 = even_number_of_1 - odd_number_of_1
def four_way_from_ranking(w, u=1111):
    repetitions = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    output = []
    # u_0101
    if u == 11:
        positives = { get_geno_number(0), get_geno_number(100), get_geno_number(1000), get_geno_number(1100),
                     get_geno_number(11), get_geno_number(111), get_geno_number(1011), get_geno_number(1111)}
        negatives = { get_geno_number(1), get_geno_number(101), get_geno_number(1001), get_geno_number(1101),
                     get_geno_number(10), get_geno_number(110), get_geno_number(1010), get_geno_number(1110)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_0011
    if u == 101:
        positives = {  get_geno_number(0),  get_geno_number(10), get_geno_number(1000), get_geno_number(1010),
                     get_geno_number(101), get_geno_number(111), get_geno_number(1101), get_geno_number(1111)}
        negatives = {  get_geno_number(1),  get_geno_number(11), get_geno_number(1001), get_geno_number(1011),
                     get_geno_number(100), get_geno_number(110), get_geno_number(1100), get_geno_number(1110)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_0110
    if u == 110:
        positives = {  get_geno_number(0),   get_geno_number(1), get_geno_number(1000), get_geno_number(1001),
                     get_geno_number(110), get_geno_number(111), get_geno_number(1110), get_geno_number(1111)}
        negatives = { get_geno_number(10),  get_geno_number(11), get_geno_number(1010), get_geno_number(1011),
                     get_geno_number(100), get_geno_number(101), get_geno_number(1100), get_geno_number(1101)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1001
    if u == 1001:
        positives = {   get_geno_number(0),   get_geno_number(10),  get_geno_number(100),  get_geno_number(110),
                     get_geno_number(1001), get_geno_number(1011), get_geno_number(1101), get_geno_number(1111)}
        negatives = {   get_geno_number(1),   get_geno_number(11),  get_geno_number(101),  get_geno_number(111),
                     get_geno_number(1000), get_geno_number(1010), get_geno_number(1100), get_geno_number(1110)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1010
    if u == 1010:
        positives = {   get_geno_number(0),    get_geno_number(1),  get_geno_number(100),  get_geno_number(101),
                     get_geno_number(1010), get_geno_number(1011), get_geno_number(1110), get_geno_number(1111)}
        negatives = {  get_geno_number(10),   get_geno_number(11),  get_geno_number(110),  get_geno_number(111),
                     get_geno_number(1000), get_geno_number(1001), get_geno_number(1100), get_geno_number(1101)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1100
    if u == 1100:
        positives = {   get_geno_number(0),    get_geno_number(1),   get_geno_number(10),   get_geno_number(11),
                     get_geno_number(1100), get_geno_number(1101), get_geno_number(1110), get_geno_number(1111)}
        negatives = { get_geno_number(100),  get_geno_number(101),  get_geno_number(110),  get_geno_number(111),
                     get_geno_number(1000), get_geno_number(1001), get_geno_number(1010), get_geno_number(1011)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_0111
    if u == 111:
        positives = {  get_geno_number(0), get_geno_number(1000),  get_geno_number(11), get_geno_number(1011),
                     get_geno_number(101), get_geno_number(1101), get_geno_number(110), get_geno_number(1110)}
        negatives = {  get_geno_number(1), get_geno_number(1001),  get_geno_number(10), get_geno_number(1010),
                     get_geno_number(100), get_geno_number(1100), get_geno_number(111), get_geno_number(1111)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1011
    if u == 1011:
        positives = {   get_geno_number(0),  get_geno_number(100),   get_geno_number(11),  get_geno_number(111),
                     get_geno_number(1001), get_geno_number(1101), get_geno_number(1010), get_geno_number(1110)}
        negatives = {   get_geno_number(1),  get_geno_number(101),   get_geno_number(10),  get_geno_number(110),
                     get_geno_number(1000), get_geno_number(1100), get_geno_number(1011), get_geno_number(1111)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1101
    if u == 1101:
        positives = {   get_geno_number(0),   get_geno_number(10),  get_geno_number(101),  get_geno_number(111),
                     get_geno_number(1001), get_geno_number(1011), get_geno_number(1100), get_geno_number(1110)}
        negatives = {   get_geno_number(1),   get_geno_number(11),  get_geno_number(100),  get_geno_number(110),
                     get_geno_number(1000), get_geno_number(1010), get_geno_number(1101), get_geno_number(1111)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1110
    if u == 1110:
        positives = {get_geno_number(0), get_geno_number(1), get_geno_number(110), get_geno_number(111),
                     get_geno_number(1010), get_geno_number(1011), get_geno_number(1100), get_geno_number(1101)}
        negatives = {get_geno_number(10), get_geno_number(11), get_geno_number(100), get_geno_number(101),
                     get_geno_number(1000), get_geno_number(1001), get_geno_number(1110), get_geno_number(1111)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    # u_1111
    if u == 1111:
        positives = {   get_geno_number(0),   get_geno_number(11),  get_geno_number(101),  get_geno_number(110),
                     get_geno_number(1001), get_geno_number(1010), get_geno_number(1100), get_geno_number(1111)}
        negatives = {   get_geno_number(1),   get_geno_number(10),  get_geno_number(100),  get_geno_number(111),
                     get_geno_number(1000), get_geno_number(1011), get_geno_number(1101), get_geno_number(1110)}
        output = [epistasis_positive(w, positives, negatives, repetitions),
                  epistasis_negative(w, positives, negatives, repetitions)]
    if not output:
        print("Four way interaction from ranking received something which is not an interaction coordinate as input.")
    return output
