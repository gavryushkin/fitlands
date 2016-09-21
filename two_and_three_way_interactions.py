import pandas as pd
from models_wilcoxon import rank_sum_n_sites
import networkx as nx
import pylab as plt
from conditional_and_marginal_epistasis import genotype_look_good,\
    marginal_two_way_interaction_analysis, marginal_three_way_interaction_analysis,\
    conditional_two_way_interaction_analysis


__author__ = '@gavruskin'


# First row must contain names of columns, first column---genotypes.
# Returns a dictionary with all trial values, e.g.
# datafile_fly_bacteria_process("fly_bacteria_data.csv")["100"] is a list of fitness values
# obtained in all trials for genotype 0...0100.
# Important that preceding 0's must be dropped in the call, e.g. the wild-type should be called as "0".
def datafile_fly_bacteria_process(data_file):
    values = pd.read_csv(data_file)
    landscapes = {}
    for ind in range(len(values.iloc[:, 0])):
        landscapes[str(values.iloc[ind, 0])] = values.iloc[ind, 1:]
    return landscapes


data = datafile_fly_bacteria_process("fly_bacteria_data_new.csv")

marginal_two_way_interaction_analysis(data)
marginal_three_way_interaction_analysis(data)
conditional_two_way_interaction_analysis(data)

# genotypes_with_means = rank_sum_n_sites(data, True)
# genotypes = rank_sum_n_sites(data)
# for i in range(len(genotypes_with_means)):
#     print(genotype_look_good(genotypes_with_means[i][0], 5))
#     print(genotypes_with_means[i][1])
#
# An attempt to draw partial orders:
#
# partial_order = nx.DiGraph()
# for genotype in genotypes:
#     partial_order.add_node(genotype)
# for i in range(len(genotypes) - 1):
#     equal_fitness_i = []
#     for j in range(i, len(genotypes)):
#         if genotypes_with_means[i][1] == genotypes_with_means[j][1]:
#             equal_fitness_i.append(genotypes[j])
#         else:
#             for k in range(j, len(genotypes)):
#                 if genotypes_with_means[j][1] == genotypes_with_means[k][1]:
#                     for s in equal_fitness_i:
#                         partial_order.add_edge(genotypes[k], s)
#                 else:
#                     break
#
# pos = nx.spring_layout(partial_order)
# labels = {}
# for genotype in genotypes:
#     labels[genotype] = genotype
# # nx.draw_networkx_nodes(partial_order, pos, node_size=2000)
# # nx.draw_networkx_labels(partial_order, pos, labels)
# # nx.draw_networkx_edges(partial_order, pos, partial_order.edges())
# nx.draw(partial_order, with_labels=True, )
# plt.savefig("partial_order.png")
# plt.show()
