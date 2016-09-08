import os.path


__author__ = "@gavruskin"


# w_000 = w_1, w_001 = w_2, w_010 = w_3, w_100 = w_4, w_011 = w_5, w_101 = w_6, w_110 = w_7, w_111 = w_8
def are_neighbors(a, b):
    if (a == 1 and (b == 2 or b == 3 or b == 4)) or (a == 2 and (b == 1 or b == 5 or b == 6)):
        return True
    if (a == 3 and (b == 1 or b == 5 or b == 7)) or (a == 4 and (b == 1 or b == 6 or b == 7)):
        return True
    if (a == 5 and (b == 2 or b == 3 or b == 8)) or (a == 6 and (b == 2 or b == 4 or b == 8)):
        return True
    if (a == 7 and (b == 3 or b == 4 or b == 8)) or (a == 8 and (b == 5 or b == 6 or b == 7)):
        return True
    return False


def ranks_to_graph(w):
    # not tested
    output = []
    for i in range(len(w)):
        for j in range(i+1, len(w)):
            if are_neighbors(w[i], w[j]):
                output.append([w[i], w[j]])
    output.sort()
    return output


def graph_from_ranks_to_file():
    if not os.path.isfile("./outputs/ranks.txt"):
        print "Please create file 'ranks.txt' in directory 'outputs' inside the working directory."
        return
    if not os.path.isfile("./outputs/fitness_graph.txt"):
        graph_file = open("./outputs/fitness_graph.txt", "w")
    else:
        print "File fitness_graph.txt is not empty."
        return
    ranks_file = open("./outputs/ranks.txt", "r")
    for line in ranks_file:
        line = line.replace("[", "")
        line = line.replace("]", "")
        ranks = [int(s) for s in line.split(', ')]
        new_graph = ranks_to_graph(ranks)
        graph_file.write(str(new_graph) + "\n")
    graph_file.close()
    ranks_file.close()


def number_of_different_graphs():
    graphs_file = open("./outputs/fitness_graph.txt", "r")
    graphs_seen = set()
    outfile = open("./outputs/fitness_graph_unique.txt", "w")
    number_of_unique = 0
    for line in graphs_file:
        if line not in graphs_seen:
            outfile.write(line)
            graphs_seen.add(line)
            number_of_unique += 1
    outfile.close()
    print "The number of unique graphs is %s" % number_of_unique
    graphs_file.close()
    outfile.close()
    return
