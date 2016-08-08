import pandas
import numpy
from three_way_epistasis import check_for_epistasis


__author__ = '@gavruskin'


def ranking_probability(sigma, data_file, mutations, sites):
    sites = [0] + [1] + sites  # This is specific to the data file. Column 0 contains fitness, column 1 names.
    values = pandas.read_csv(data_file, usecols=sites)
    genotype_names = pandas.read_csv(data_file, usecols=[1])
    values.iloc[:, 0] = numpy.log10(values.iloc[:, 0])
    size = len(values.iloc[:, 1])
    f000 = []
    f000_name = []  # TODO: This is to keep track of where the sample is coming from, and can be omitted for efficiency.
    f001 = []
    f001_name = []
    f010 = []
    f010_name = []
    f100 = []
    f100_name = []
    f011 = []
    f011_name = []
    f101 = []
    f101_name = []
    f110 = []
    f110_name = []
    f111 = []
    f111_name = []
