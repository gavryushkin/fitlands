from three_way_epistasis import list_epistasis, epistasis


__author__ = "@gavruskin"


def testing():
    positives_list = [{1, 7},           # 1
                      {2, 8},           # 2
                      {1, 6},           # 3
                      {3, 8},           # 4
                      {1, 5},           # 5
                      {4, 8},           # 6
                      {1, 8},           # 7
                      {2, 7},           # 8
                      {1, 8},           # 9
                      {2, 7},           # 10
                      {1, 8},           # 11
                      {3, 6},           # 12
                      {1, 4, 5, 8},     # 13
                      {1, 3, 6, 8},     # 14
                      {1, 2, 7, 8},     # 15
                      {1, 5, 6, 7}]     # 16

    negatives_list = [{3, 4},           # 1
                      {5, 6},           # 2
                      {2, 4},           # 3
                      {5, 7},           # 4
                      {2, 3},           # 5
                      {6, 7},           # 6
                      {5, 4},           # 7
                      {3, 6},           # 8
                      {3, 6},           # 9
                      {5, 4},           # 10
                      {2, 7},           # 11
                      {5, 4},           # 12
                      {2, 6, 3, 7},     # 13
                      {2, 5, 4, 7},     # 14
                      {3, 5, 4, 6},     # 15
                      {4, 3, 2, 8}]     # 16

    for shape_number in range(len(positives_list)):
        shape_name = shape_number + 1
        if shape_name == 13:
            shape_name = "u_011"
        if shape_name == 14:
            shape_name = "u_101"
        if shape_name == 15:
            shape_name = "u_110"
        if shape_name == 16:
            shape_name = "u_111"
        list_epistasis(positives_list[shape_number], negatives_list[shape_number],shape_name)


# Generates a file with shared orders:
def shared_orders(file1, file2):
    ranks1 = open("./outputs/circuit_%s_orders.txt" % file1, "r")
    ranks2 = open("./outputs/circuit_%s_orders.txt" % file2, "r")
    ranks1_set = set()
    shared = set()
    for line in ranks1:
        ranks1_set.add(line)
    for line in ranks2:
        if line in ranks1_set:
            shared.add(line)
    shared_file = open("./outputs/ranks_shared_between_%s_and_%s.txt" % (file1, file2), "w")
    for x in shared:
        shared_file.write(str(x))
    ranks1.close()
    ranks2.close()
    shared_file.close()
