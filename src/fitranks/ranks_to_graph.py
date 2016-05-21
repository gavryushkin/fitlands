import os.path


__author__ = "@gavruskin"


def ranks_to_graph(w):
    output = []
    for i in range(len(w)):
        for j in range(i+1, len(w)):
            if w[i] == w[j] - 1:
                output.append([w[i], w[j]])
            elif w[i] == w[j] + 1:
                output.append([w[i], w[j]])
    output.sort()
    return output


def graph_from_ranks_to_file():
    if not os.path.isfile("./ranks.txt"):
        print "Please create file ranks.txt in the working directory."
        return
    if not os.path.isfile("./fitness_graph.txt"):
        graph_file = open("./fitness_graph.txt", "w")
    else:
        print "File fitness_graph.txt is not empty."
        return
    ranks_file = open("./ranks.txt", "r")

    for line in ranks_file:
        line = line.replace("[", "")
        line = line.replace("]", "")
        ranks = [int(s) for s in line.split(', ')]
        new_graph = ranks_to_graph(ranks)
        graph_file.write(str(new_graph) + "\n")
    graph_file.close()
    ranks_file.close()


def number_of_different_graphs():
    graphs = open("./fitness_graph.txt", "r")
    result = ["1"]
    for graph in graphs:
        for i in range(len(result)):
            if graph != result[i] and (i == len(result) - 1 or len(result) == 0):
                result.append(graph)
    output = len(result)
    for i in range(output):
        print str(result[i])
    output -= 1
    print "The number of unique graphs is %s" % output
    graphs.close()
    return


number_of_different_graphs()
