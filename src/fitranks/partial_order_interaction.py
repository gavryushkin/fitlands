import os.path
from three_way_epistasis import get_next_ordering, ordering_to_fitness


__author__ = "@gavruskin"


# Given a partial order in the form of adjacency lists, return all total extensions.
# Loops through all total orders looking for compatible ones.
def all_total_extensions_brute_force(graph):
    output = []
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    compatible = True
    for edge in graph:
        if fitness.index(edge[0]) < fitness.index(edge[1]):
            compatible = False
            break
    if compatible:
        output.append(fitness)
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        compatible = True
        for edge in graph:
            if fitness.index(edge[0]) < fitness.index(edge[1]):
                compatible = False
                break
        if compatible:
            output.append(fitness)
    return output


# Returns a list of partial orders on the set {1, ..., 8} given a file with partial orders on the set {000, ..., 111}.
# The convention is: 000 = 1, 001 = 2, 010 = 3, 100 = 4, 011 = 5, 101 = 6, 110 = 7, 111 = 8
# (To be compatible with other functions.)
def partial_orders_from_file(file_name):
    if not os.path.isfile("./outputs/%s" % file_name):
        print "Please put the file with partial orders into directory 'outputs' inside the working directory."
        return
    partial_orders_file = open("./outputs/%s" % file_name, "r")
    output = []
    for line in partial_orders_file:
        if line != "\n":
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace(" ", "")
            partial_order = [int(s) for s in line.split(",")]
            for i in range(len(partial_order)):
                if partial_order[i] == 0:
                    partial_order[i] = 1
                elif partial_order[i] == 1:
                    partial_order[i] = 2
                elif partial_order[i] == 10:
                    partial_order[i] = 3
                elif partial_order[i] == 100:
                    partial_order[i] = 4
                elif partial_order[i] == 11:
                    partial_order[i] = 5
                elif partial_order[i] == 101:
                    partial_order[i] = 6
                elif partial_order[i] == 110:
                    partial_order[i] = 7
                elif partial_order[i] == 111:
                    partial_order[i] = 8
            partial_order_formatted = []
            for i in range(0, len(partial_order), 2):
                partial_order_formatted.append([partial_order[i], partial_order[i+1]])
            output.append(partial_order_formatted)
    return output


def analyze_partial_orders(file_name):
    partial_orders = partial_orders_from_file(file_name)
    for partial_order in partial_orders:
        total_extensions = all_total_extensions_brute_force(partial_order)
        for total_extension in total_extensions:
            print total_extension
        print


analyze_partial_orders("partial_orders.txt")
