from three_way_epistasis import check_for_epistasis


__author__ = '@gavruskin'


# w_000 = w[1], w_001 = w[2], w_010 = w[3], w_100 = w[4], w_011 = w[5], w_101 = w[6], w_110 = w[7], w_111 = w[8]


mean = [1.580, 1.195, 1.133, 1.441, 1.430, 1.232, 1.294, 1.045]

print check_for_epistasis(mean)
