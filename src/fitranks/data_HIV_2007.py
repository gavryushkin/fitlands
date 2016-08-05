import pandas
import numpy
from three_way_epistasis import check_for_epistasis


__author__ = '@gavruskin'


# w_000 = w[1], w_001 = w[2], w_010 = w[3], w_100 = w[4], w_011 = w[5], w_101 = w[6], w_110 = w[7], w_111 = w[8]
# The values below are from Table 6.2 in BPS
minim = [0.1917,  0.5344, -0.3355, 0.4771,  1.0000, 0.3010, 0.6021, -0.4771]
qu1 = [1.4770,  0.6990,  1.1440, 1.3470, 1.2500, 0.8673, 1.1610, 0.9472]
median = [1.6410, 1.1880, 1.2960, 1.4650, 1.5150, 1.3420, 1.3700, 1.1790]
mean = [1.5800, 1.1950, 1.1330, 1.4410, 1.4300, 1.2320, 1.2940, 1.0450]
qu3 = [1.7910, 1.7710, 1.4870, 1.7890, 1.6360, 1.5840, 1.5370, 1.3850]
maxim = [2.0530, 1.7850, 1.5310, 1.8750, 1.7240, 1.8870, 1.6920, 1.7900]

check_for_epistasis(minim)
check_for_epistasis(qu1)
check_for_epistasis(median)
check_for_epistasis(mean)
check_for_epistasis(qu3, True)
check_for_epistasis(maxim)


def get_mean_fitness(data_file, sites, mean_type="mean"):
    sites = [0] + sites
    values = pandas.read_csv(data_file, usecols=sites)
    values.iloc[:, 0] = numpy.log10(values.iloc[:, 0])
    size = len(values.iloc[:,1])
    f000 = []
    f001 = []
    f010 = []
    f100 = []
    f011 = []
    f101 = []
    f110 = []
    f111 = []
    for s in range(size):
        if (values.iloc[s, 1] == "L") & (values.iloc[s, 2] == "M") & (values.iloc[s, 3] == "t"):
            f000.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "L") & (values.iloc[s, 2] == "M") & (values.iloc[s, 3] == "Y"):
            f001.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "L") & (values.iloc[s, 2] == "V") & (values.iloc[s, 3] == "t"):
            f010.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "M") & (values.iloc[s, 2] == "M") & (values.iloc[s, 3] == "t"):
            f100.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "L") & (values.iloc[s, 2] == "V") & (values.iloc[s, 3] == "Y"):
            f011.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "M") & (values.iloc[s, 2] == "M") & (values.iloc[s, 3] == "Y"):
            f101.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "M") & (values.iloc[s, 2] == "V") & (values.iloc[s, 3] == "t"):
            f110.append(values.iloc[s, 0])
        elif (values.iloc[s, 1] == "M") & (values.iloc[s, 2] == "V") & (values.iloc[s, 3] == "Y"):
            f111.append(values.iloc[s, 0])
    if mean_type == "mean":
        w = [numpy.mean(f000), numpy.mean(f001), numpy.mean(f010), numpy.mean(f100), numpy.mean(f011), numpy.mean(f101),
             numpy.mean(f110), numpy.mean(f111)]
    elif mean_type == "max":
        w = [numpy.max(f000), numpy.max(f001), numpy.max(f010), numpy.max(f100), numpy.max(f011), numpy.max(f101),
             numpy.max(f110), numpy.max(f111)]
    elif mean_type == "min":
        w = [numpy.min(f000), numpy.min(f001), numpy.min(f010), numpy.min(f100), numpy.min(f011), numpy.min(f101),
             numpy.min(f110), numpy.min(f111)]
    elif mean_type == "median":
        w = [numpy.median(f000), numpy.median(f001), numpy.median(f010), numpy.median(f100), numpy.median(f011),
             numpy.median(f101), numpy.median(f110), numpy.median(f111)]
    elif mean_type == "qu1":
        w = [numpy.percentile(f000, 25), numpy.percentile(f001, 25), numpy.percentile(f010, 25),
             numpy.percentile(f100, 25), numpy.percentile(f011, 25), numpy.percentile(f101, 25),
             numpy.percentile(f110, 25), numpy.percentile(f111, 25)]
    elif mean_type == "qu3":
        w = [numpy.percentile(f000, 75), numpy.percentile(f001, 75), numpy.percentile(f010, 75),
             numpy.percentile(f100, 75), numpy.percentile(f011, 75), numpy.percentile(f101, 75),
             numpy.percentile(f110, 75), numpy.percentile(f111, 75)]
    return w


HIV_data_file = "2007_HIV_data.csv"
HIV_sites = [88, 244, 275]  # sites: PRO L90M, RT M184V, RT T215Y
mean_my = get_mean_fitness(HIV_data_file, HIV_sites, "qu3")
check_for_epistasis(mean_my, True)


# epi_count = 0
# for k in range(4, 281):
#     for j in range(3, k):
#         for i in range(2, j):
#             running_sites = [i, j, k]
#             running_mean = get_mean_fitness(HIV_data_file, running_sites)
#             epi = check_for_epistasis(running_mean)
#             if epi[0] or epi[1]:
#                 epi_count += 1
#                 print epi_count
#                 print running_sites
