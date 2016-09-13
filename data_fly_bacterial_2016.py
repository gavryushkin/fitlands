import pandas
from models_wilcoxon import rank_sum_n_sites


__author__ = '@gavruskin'


# First row must contain names of columns, first column---genotypes.
# Returns a dictionary with all trial values, e.g.
# datafile_fly_bacteria_process("fly_bacteria_data.csv")["100"] is a list of fitness values
# obtained in all trials for genotype 0...0100.
# Important that preceding 0's must be dropped in the call, e.g. the wild-type should be called as "0".
def datafile_fly_bacteria_process(data_file):
    values = pandas.read_csv(data_file)
    landscapes = {}
    for i in range(len(values.iloc[:, 0])):
        landscapes[str(values.iloc[i, 0])] = values.iloc[i, :]
    return landscapes


data = datafile_fly_bacteria_process("fly_bacteria_data.csv")
rank_sum_n_sites(data)
