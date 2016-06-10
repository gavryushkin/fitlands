from three_way_epistasis import get_next_ordering, ordering_to_fitness, epistasis
from ranks_to_graph import ranks_to_graph


__author__="@gavruskin"


# Nodes are the fitness graph as a linked list.
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.head = True
        self.tail = True


def print_node(node):
    edges = []
    for edge in node.edges:
        edges.append(edge.name)
    edges.sort()
    print "Name: " + str(node.name)
    print "Edges: " + str(edges)
    print "Head: " + str(node.head)
    print "Tail: " + str(node.tail) + "\n"


# Convert a graph given as an edge list to a graph given as a linked list of nodes:
def edge_list_to_graph(g):
    nodes = []
    for i in range(8):
        nodes.append(Node(i+1))
    for edge in g:
        nodes[edge[0] - 1].edges.append(nodes[edge[1] - 1])
        nodes[edge[1] - 1].head = False
        nodes[edge[0] - 1].tail = False
    for j in range(8):
        nodes[j].edges = list(set(nodes[j].edges))
    return nodes


# Returns a list of fitness rankings consistent with graph given by edge list:
def consistent_rankings(graph):
    output = []
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = ordering_to_fitness(ordering)
    good = True
    i = 0
    while good and i < len(graph):
        if fitness.index(graph[i][0]) > fitness.index(graph[i][1]):
            good = False
        else:
            i += 1
    if good:
        output.append(fitness)
    while ordering != [8, 7, 6, 5, 4, 3, 2, 1]:
        ordering = get_next_ordering(ordering)
        fitness = ordering_to_fitness(ordering)
        good = True
        i = 0
        while good and i < len(graph):
            if fitness.index(graph[i][0]) > fitness.index(graph[i][1]):
                good = False
            else:
                i += 1
        if good:
            output.append(fitness)
    return output


# Returns whether graph has strict epistasis.
def strict_epistasis_for_graph(graph):
    consistent_orders = consistent_rankings(graph)
    for order in consistent_orders:
        if not epistasis(order):
            return False
    return True


def strict_epistasis():
    output = []
    ranks_file = open("./ranks.txt", "r")
    graphs = set()
    unique_graphs = []
    for line in ranks_file:
        line = line.replace("[", "")
        line = line.replace("]", "")
        ranks = [int(s) for s in line.split(', ')]
        new_graph = ranks_to_graph(ranks)
        if not str(new_graph) in graphs:
            graphs.add(str(new_graph))
            unique_graphs.append(new_graph)
            if strict_epistasis_for_graph(new_graph):
                output.append(new_graph)
                print str(new_graph)  # TODO: print to file?
    ranks_file.close()
    print "\nThe number of graphs that have a strict epistasis is " + str(len(output))
    print "The number of graphs that have an epistasis is " + str(len(graphs))
    return output


strict_epistasis()
