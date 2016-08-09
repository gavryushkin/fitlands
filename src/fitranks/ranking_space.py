import numpy


__author__ = '@gavruskin'


# Returns a list of permutation neighbors of w.
def give_rank_neighbors(w):
    output = []
    for i in range(len(w) - 1):
        v = [None]*len(w)
        for j in range(len(w)):
            if j == i:
                v[j] = w[i+1]
            elif j == i+1:
                v[j] = w[i]
            else:
                v[j] = w[j]
        output.append(v)
    return output


# A negative number indicates how strong the positive epistasis is.
def dist_to_positive_epi(w, positives={1, 5, 6, 7}, negatives={4, 3, 2, 8}):
    count = 0
    count_values = []
    for i in range(len(w)):
        if w[i] in negatives:
            count -= 1
            count_values.append(count)
        elif w[i] in positives:
            count += 1
            count_values.append(count)
        else:
            print "Your w has an unsigned entry in dist_to_positive_epi."
            return
    output = numpy.max(count_values)
    return output


# A negative number indicates how strong the negative epistasis is.
def dist_to_negative_epi(w, positives={1, 5, 6, 7}, negatives={4, 3, 2, 8}):
    count = 0
    count_values = []
    for i in range(len(w)):
        if w[i] in negatives:
            count -= 1
            count_values.append(count)
        elif w[i] in positives:
            count += 1
            count_values.append(count)
        else:
            print "Your w has an unsigned entry in dist_to_positive_epi"
            return
    output = numpy.min(count_values)
    return output


print dist_to_positive_epi([8, 3, 7, 6, 5, 2, 4, 1])
print dist_to_negative_epi([8, 3, 7, 6, 5, 2, 4, 1])
