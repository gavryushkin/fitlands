from three_way_epistasis import list_epistasis, list_epistasis_signed, get_next_ordering, ordering_to_fitness

__author__ = "@gavruskin"


def get_positives_list():
    return [{1, 7},  # 1 a
            {2, 8},  # 2 b
            {1, 6},  # 3 c
            {3, 8},  # 4 d
            {1, 5},  # 5 e
            {4, 8},  # 6 f

            {1, 8},  # 7 g
            {2, 7},  # 8 h
            {1, 8},  # 9 i
            {2, 7},  # 10 j
            {1, 8},  # 11 k
            {3, 6},  # 12 l

            {2, 3, 4},  # 13 m
            {5, 6, 7},  # 14 n
            {3, 4, 8},  # 15 o
            {1, 5, 6},  # 16 p
            {2, 4, 8},  # 17 q
            {1, 5, 7},  # 18 r
            {1, 6, 7},  # 19 s
            {2, 3, 8},  # 20 t

            {1, 4, 5, 8},  # 21 u_011
            {1, 3, 6, 8},  # 22 u_101
            {1, 2, 7, 8},  # 23 u_110
            {1, 5, 6, 7}]  # 24 u_111


def get_negatives_list():
    return [{3, 4},  # 1 a
            {5, 6},  # 2 b
            {2, 4},  # 3 c
            {5, 7},  # 4 d
            {2, 3},  # 5 e
            {6, 7},  # 6 f

            {5, 4},  # 7 g
            {3, 6},  # 8 h
            {3, 6},  # 9 i
            {5, 4},  # 10 j
            {2, 7},  # 11 k
            {5, 4},  # 12 l

            {8, 1},  # 13 m
            {1, 8},  # 14 n
            {2, 7},  # 15 o
            {7, 2},  # 16 p
            {3, 6},  # 17 q
            {6, 3},  # 18 r
            {5, 4},  # 19 s
            {4, 5},  # 20 t

            {2, 6, 3, 7},  # 21 u_011
            {2, 5, 4, 7},  # 22 u_101
            {3, 5, 4, 6},  # 23 u_110
            {4, 3, 2, 8}]  # 24 u_111


# Returns the list of coefficients that corresponds to circuit number n from {1, ..., 24}.
# Will return all coefficients 1 if the circuit number is out of range.
def get_repetitions_from_circuit_number(n):
    if n == 13:
        return [2, 1, 1, 1, 1, 1, 1, 1]
    elif n == 14:
        return [1, 1, 1, 1, 1, 1, 1, 2]
    elif n == 15:
        return [1, 1, 1, 1, 1, 1, 2, 1]
    elif n == 16:
        return [1, 2, 1, 1, 1, 1, 1, 1]
    elif n == 17:
        return [1, 1, 1, 1, 1, 2, 1, 1]
    elif n == 18:
        return [1, 1, 2, 1, 1, 1, 1, 1]
    elif n == 19:
        return [1, 1, 1, 2, 1, 1, 1, 1]
    elif n == 20:
        return [1, 1, 1, 1, 2, 1, 1, 1]
    else:
        return [1, 1, 1, 1, 1, 1, 1, 1]


# For every circuit, generates a file that contains orders that imply epistasis.
def orders_to_circuits():
    positives_list = get_positives_list()
    negatives_list = get_negatives_list()
    for shape_number in range(len(positives_list)):
        shape_name = shape_number + 1
        if shape_name == 21:
            shape_name = "u_011"
        elif shape_name == 22:
            shape_name = "u_101"
        elif shape_name == 23:
            shape_name = "u_110"
        elif shape_name == 24:
            shape_name = "u_111"
        elif shape_name == 13:
            rep = [2, 1, 1, 1, 1, 1, 1, 1]
        elif shape_name == 14:
            rep = [1, 1, 1, 1, 1, 1, 1, 2]
        elif shape_name == 15:
            rep = [1, 1, 1, 1, 1, 1, 2, 1]
        elif shape_name == 16:
            rep = [1, 2, 1, 1, 1, 1, 1, 1]
        elif shape_name == 17:
            rep = [1, 1, 1, 1, 1, 2, 1, 1]
        elif shape_name == 18:
            rep = [1, 1, 2, 1, 1, 1, 1, 1]
        elif shape_name == 19:
            rep = [1, 1, 1, 2, 1, 1, 1, 1]
        elif shape_name == 20:
            rep = [1, 1, 1, 1, 2, 1, 1, 1]
        else:
            rep = [1, 1, 1, 1, 1, 1, 1, 1]
        list_epistasis(positives_list[shape_number], negatives_list[shape_number], shape_name, rep)
        list_epistasis_signed(positives_list[shape_number], negatives_list[shape_number], shape_name, rep)


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


# Generates a big file with the list of all rankings.
# A ranking is followed by a list of circuits that imply epistasis.
def circuits_to_orders():
    circuits_to_orders_file = open("./outputs/circuits_to_orders.txt", "w")
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    line = str(fitness) + "\n"
    circuits_to_orders_file.write(line)
    for circuit in range(1, 21):
        if line in open("./outputs/circuit_%s_orders.txt" % circuit, "r"):
            circuits_to_orders_file.write(str(circuit))
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        line = str(fitness) + "\n"
        circuits_to_orders_file.write("\n" + line)
        for circuit in range(1, 21):
            if line in open("./outputs/circuit_%s_orders.txt" % circuit, "r"):
                circuits_to_orders_file.write(str(circuit) + " ")
    circuits_to_orders_file.close()


# Generates a big file with the list of all rankings.
# A ranking is followed by a list of circuits with signs that imply epistasis.
def circuits_to_orders_signed():
    circuits_to_orders_file = open("./outputs/circuits_to_orders_signed.txt", "w")
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    line = str(fitness) + "\n"
    line_positive = str(fitness) + " +" + "\n"
    line_negative = str(fitness) + " -" + "\n"
    circuits_to_orders_file.write(line)
    for circuit in range(1, 21):
        if line_positive in open("./outputs/circuit_%s_orders_signed.txt" % circuit, "r"):
            circuits_to_orders_file.write("+" + str(circuit) + " ")
        elif line_negative in open("./outputs/circuit_%s_orders_signed.txt" % circuit, "r"):
            circuits_to_orders_file.write("-" + str(circuit) + " ")
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        line = str(fitness) + "\n"
        line_positive = str(fitness) + " +" + "\n"
        line_negative = str(fitness) + " -" + "\n"
        circuits_to_orders_file.write("\n" + line)
        for circuit in range(1, 21):
            if line_positive in open("./outputs/circuit_%s_orders_signed.txt" % circuit, "r"):
                circuits_to_orders_file.write("+" + str(circuit) + " ")
            elif line_negative in open("./outputs/circuit_%s_orders_signed.txt" % circuit, "r"):
                circuits_to_orders_file.write("-" + str(circuit) + " ")
    circuits_to_orders_file.close()

# To generate the big file, call:
# orders_to_circuits()
# circuits_to_orders_signed()
