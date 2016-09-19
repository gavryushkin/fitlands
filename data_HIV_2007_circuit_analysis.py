from models_wilcoxon import rank_sum_3_sites
from models_HIV_2007 import datafile_hiv_process
from partial_order_interaction import analyze_total_order_for_all_circuits, convert_to_genotype

__author__ = "@gavruskin"

# This script process the file 2007_HIV_data.csv, which must be inside the working directory,
# returns the rank order supported by the data in the file (restricted to the three loci---see models_HIV_2007),
# and for each of the 24 circuits, analyzes the circuit interaction implied by the rank order.
data = datafile_hiv_process()
ranking = rank_sum_3_sites(data)
print("\nThe rank order is\n" + convert_to_genotype(ranking) + "\n")
analyze_total_order_for_all_circuits(ranking, False)
print("The output has been written to "
      "file total_order_analysis_for_all_circuits.md located in the directory ./outputs\n")
print("The three-way interaction corresponds to the last circuit:\n"
      "w(000) - w(001) - w(010) - w(100) + w(011) + w(101) + w(110) - w(111)")
