from three_way_epistasis import list_epistasis, epistasis


__author__ = "@gavruskin"


# For plain three-way epistasis plug in:
# positives = {1, 5, 6, 7}
# negatives = {2, 3, 4, 8}

positives_list = [{1, 7},
                  {2, 8},
                  {1, 6},
                  {3, 8},
                  {1, 5},
                  {4, 8},
                  {1, 8},
                  {2, 7},
                  {1, 8},
                  {2, 7},
                  {1, 8},
                  {3, 6}]


negatives_list = [{3, 4},
                  {5, 6},
                  {2, 4},
                  {5, 7},
                  {2, 3},
                  {6, 7},
                  {5, 4},
                  {3, 6},
                  {3, 6},
                  {5, 4},
                  {2, 7},
                  {5, 4}]


for shape_number in range(12):
    shape_name = shape_number + 1
    list_epistasis(positives_list[shape_number], negatives_list[shape_number],shape_name)
