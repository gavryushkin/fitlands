import pandas as pd
import numpy as np
from three_way_epistasis import check_for_epistasis


__author__ = '@gavruskin'


# w_000 = w[0], w_001 = w[1], w_010 = w[2], w_100 = w[3], w_011 = w[4], w_101 = w[5], w_110 = w[6], w_111 = w[7]
# The values below are from Table 6.2 in BPS
minim = [0.1917,  0.5344, -0.3355, 0.4771,  1.0000, 0.3010, 0.6021, -0.4771]
qu1 = [1.4770,  0.6990,  1.1440, 1.3470, 1.2500, 0.8673, 1.1610, 0.9472]
median = [1.6410, 1.1880, 1.2960, 1.4650, 1.5150, 1.3420, 1.3700, 1.1790]
mean = [1.5800, 1.1950, 1.1330, 1.4410, 1.4300, 1.2320, 1.2940, 1.0450]
qu3 = [1.7910, 1.7710, 1.4870, 1.7890, 1.6360, 1.5840, 1.5370, 1.3850]
maxim = [2.0530, 1.7850, 1.5310, 1.8750, 1.7240, 1.8870, 1.6920, 1.7900]

# check_for_epistasis(minim)
# check_for_epistasis(qu1)
# check_for_epistasis(median)
# check_for_epistasis(mean, True)
# check_for_epistasis(qu3)
# check_for_epistasis(maxim)
#
#
# minim.reverse()
# check_for_epistasis(minim)


def get_mean_fitness(data_file, mutations, sites, mean_type=""):  # Default mean_type returns all possible combinations
    # of fitness values for the fist n values where n is the min number of fitness measurements over all genotypes.
    # This should not be used!
    sites = [0] + sites  # This is specific to the data file. Column 0 contains fitness, column 1 names.
    values = pd.read_csv(data_file, usecols=sites)
    values.iloc[:, 0] = np.log10(values.iloc[:, 0])
    size = len(values.iloc[:, 1])
    f000 = []
    f001 = []
    f010 = []
    f100 = []
    f011 = []
    f101 = []
    f110 = []
    f111 = []
    for s in range(size):
        if (values.iloc[s, 1] == mutations[0][0]) & (values.iloc[s, 2] == mutations[1][0]) &\
                (values.iloc[s, 3] == mutations[2][0]):
            f000.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][0]) & (values.iloc[s, 2] == mutations[1][0]) &\
                (values.iloc[s, 3] == mutations[2][1]):
            f001.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][0]) & (values.iloc[s, 2] == mutations[1][1]) &\
                (values.iloc[s, 3] == mutations[2][0]):
            f010.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][1]) & (values.iloc[s, 2] == mutations[1][0]) &\
                (values.iloc[s, 3] == mutations[2][0]):
            f100.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][0]) & (values.iloc[s, 2] == mutations[1][1]) &\
                (values.iloc[s, 3] == mutations[2][1]):
            f011.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][1]) & (values.iloc[s, 2] == mutations[1][0]) &\
                (values.iloc[s, 3] == mutations[2][1]):
            f101.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][1]) & (values.iloc[s, 2] == mutations[1][1]) &\
                (values.iloc[s, 3] == mutations[2][0]):
            f110.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == mutations[0][1]) & (values.iloc[s, 2] == mutations[1][1]) &\
                (values.iloc[s, 3] == mutations[2][1]):
            f111.append(values.iloc[s, 0])
    if mean_type == "mean":
        w = [np.mean(f000), np.mean(f001), np.mean(f010), np.mean(f100), np.mean(f011), np.mean(f101),
             np.mean(f110), np.mean(f111)]
        return w
    elif mean_type == "max":
        w = [np.max(f000), np.max(f001), np.max(f010), np.max(f100), np.max(f011), np.max(f101),
             np.max(f110), np.max(f111)]
        return w
    elif mean_type == "min":
        w = [np.min(f000), np.min(f001), np.min(f010), np.min(f100), np.min(f011), np.min(f101),
             np.min(f110), np.min(f111)]
        return w
    elif mean_type == "median":
        w = [np.median(f000), np.median(f001), np.median(f010), np.median(f100), np.median(f011),
             np.median(f101), np.median(f110), np.median(f111)]
        return w
    elif mean_type == "qu1":
        w = [np.percentile(f000, 25), np.percentile(f001, 25), np.percentile(f010, 25),
             np.percentile(f100, 25), np.percentile(f011, 25), np.percentile(f101, 25),
             np.percentile(f110, 25), np.percentile(f111, 25)]
        return w
    elif mean_type == "qu3":
        w = [np.percentile(f000, 75), np.percentile(f001, 75), np.percentile(f010, 75),
             np.percentile(f100, 75), np.percentile(f011, 75), np.percentile(f101, 75),
             np.percentile(f110, 75), np.percentile(f111, 75)]
        return w
    f_min_length = min(len(f000), len(f001), len(f010), len(f100), len(f011), len(f101), len(f110), len(f111))
    f000_sorted = sorted(f000)
    f000_sorted = f000_sorted[0:f_min_length]
    f001_sorted = sorted(f001)
    f001_sorted = f001_sorted[0:f_min_length]
    f010_sorted = sorted(f010)
    f010_sorted = f010_sorted[0:f_min_length]
    f100_sorted = sorted(f100)
    f100_sorted = f100_sorted[0:f_min_length]
    f011_sorted = sorted(f011)
    f011_sorted = f011_sorted[0:f_min_length]
    f101_sorted = sorted(f101)
    f101_sorted = f101_sorted[0:f_min_length]
    f110_sorted = sorted(f110)
    f110_sorted = f110_sorted[0:f_min_length]
    f111_sorted = sorted(f111)
    f111_sorted = f111_sorted[0:f_min_length]
    w_list = []
    for f0 in f000_sorted:
        for f1 in f001_sorted:
            for f2 in f010_sorted:
                for f3 in f100_sorted:
                    for f4 in f011_sorted:
                        for f5 in f101_sorted:
                            for f6 in f110_sorted:
                                for f7 in f111_sorted:
                                    if len({f0, f1, f2, f3, f4, f5, f6, f7}) == 8:  # To skip missing data.
                                        w_list.append([f0, f1, f2, f3, f4, f5, f6, f7])
    return w_list


HIV_data_file = "2007_HIV_data.csv"
mutations_BPS = [["L", "M"],  # mutations: L to M, M to V, t to Y
                 ["M", "V"],
                 ["t", "Y"]]
sites_BPS = [88, 244, 275]  # sites: PRO L90M, RT M184V, RT T215Y
list_with_five_variants = get_mean_fitness(HIV_data_file, mutations_BPS, sites_BPS)
total_num_genotypes = len(list_with_five_variants)
positive_epi_num = 0
negative_epi_num = 0
non_informative_num = 0
for ranking in list_with_five_variants:
    epi_pair = check_for_epistasis(ranking)
    if epi_pair[0]:
        positive_epi_num += 1
    elif epi_pair[1]:
        negative_epi_num += 1
    elif not epi_pair[0] and not epi_pair[1]:
        non_informative_num += 1
analysis_output = [positive_epi_num, negative_epi_num, non_informative_num, total_num_genotypes]
print(analysis_output)
