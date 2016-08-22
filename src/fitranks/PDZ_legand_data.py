from three_way_epistasis import check_for_epistasis
from four_way_epistasis import check_for_epistasis_four_way

__author__ = "@gavruskin"


shaker = [-1.97, -7.05, -13.57, -9.47, -7.97, -8.11, -10.01, -13.50, -7.04, -6.58, -8.42, -8.20, -5.05, -8.80,
          10.07, -7.52]
check_for_epistasis_four_way(shaker, True)

free_energy = [-8.17, -7.58, -6.13, -5.96, -6.24, -7.70, -7.67, -8.45]
check_for_epistasis(free_energy, True)

mutant_cycle = [8.17, 0.59, 2.05, 2.22, -0.70, -2.33, -3.76, 1.67]
check_for_epistasis(mutant_cycle, True)
