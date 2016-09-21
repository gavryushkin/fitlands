import numpy as np

__author__ = "@gavruskin"


# Adds missing 0's in front the genotype to make it of length n.
def genotype_look_good(genotype, n):
    output = str(genotype)
    for i in range(n - len(genotype)):
        output = "0" + output
    return output


# Returns a file with comprehensive analysis of conditional epistasis.
# TODO: update and finish this.
# data is a dictionary, num_sites == total number of sites,
def conditional_two_way_interaction_analysis(data):
    number_trials = 0
    for genotype in data:
        number_trials = len(data[genotype])
        break
    print("Missing data is currently not supported by conditional two-way interaction analysis. "
          "Make sure your fitness values do not have missing data.\n")
    # TODO: Add support for missing data.
    n = 0  # Number of sites.
    for genotype in data:
        if len(genotype) > n:
            n = len(genotype)
    m = 2 ** (n - 2)  # Number of sequence to condition on
    for genotype in data:  # Make the genotypes look good (all of the same length):
        data[genotype_look_good(genotype, n)] = data.pop(genotype)

    output_file = open("outputs/conditional_two_way_epistasis_analysis.md", "w")
    output_file.write("This file has been created using software package Fitlands "
                      "(Alex Gavryushkin, CBG, D-BSSE, ETH Zurich).\n"
                      "Please refer to [https://github.com/gavruskin/fitlands] for legal matters, "
                      "to obtain up-to-date bibliographic information for Fitlands, "
                      "and to stay tuned.\n"
                      "If you publish the results obtained with the help of this software, "
                      "please don't forget to cite us.\n")
    output_file.write("\n\n# Conditional two-way interaction analysis\n\n")

    epi_matrix = np.empty([number_trials, n, n, m], dtype=float)  # Compute epistasis.
    for trial in range(number_trials):
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(m):  # Loop through sites (i, j) to find the interaction conditioning on genotype #k.
                    epi = 0
                    genotype_condition = genotype_look_good("{0:b}".format(k), n - 2)
                    for genotype in data:
                        genotype_background = genotype[:i] + genotype[i + 1:j] + genotype[j + 1:]
                        if genotype_background == genotype_condition:
                            if genotype[i] == genotype[j] == "0" or genotype[i] == genotype[j] == "1":
                                epi += data[genotype][trial]
                            elif (genotype[i] == "0" and genotype[j] == "1") or \
                                    (genotype[i] == "1" and genotype[j] == "0"):
                                epi -= data[genotype][trial]
                            else:
                                print(
                                    "Attention! Your genotypes contain entries different from 0 and 1. "
                                    "Those are skipped.")
                    epi_matrix[trial][i][j][k] = epi

    for i in range(n):
        for j in range(i + 1, n):
            output_file.write("\n## Locus %s and %s\n\n" % (i + 1, j + 1))
            for k in range(m):
                for trial in range(number_trials):
                    output_file.write("Conditioning on %s, the interaction (epistasis) in trial %s is %s\n" %
                                (genotype_look_good("{0:b}".format(k), n - 2), trial + 1, epi_matrix[trial][i][j][k]))
                if i != n - 2 or j != n - 1 or k != m - 1:
                    output_file.write("\n")
    output_file.close()
    print("The output has been written into file two_way_epistasis_analysis.md in the ./outputs directory.\n")
    return epi_matrix


# Returns a file with comprehensive analysis of marginal two-way epistasis epistasis.
# data is a dictionary with genotypes as keys and fitness values across the trials as a list.
def marginal_two_way_interaction_analysis(data):
    number_trials = 0
    for genotype in data:
        number_trials = len(data[genotype])
        break
    print("Missing data is currently not supported by two-way interaction analysis. "
          "Make sure your fitness values do not have missing data.\n")
    # TODO: Add support for missing data.
    n = 0  # Number of sites.
    for genotype in data:
        if len(genotype) > n:
            n = len(genotype)
    for genotype in data:  # Make the genotypes look good (all of the same length):
        data[genotype_look_good(genotype, n)] = data.pop(genotype)

    output_file = open("outputs/two_way_epistasis_analysis.md", "w")
    output_file.write("This file has been created using software package Fitlands "
                      "(Alex Gavryushkin, CBG, D-BSSE, ETH Zurich).\n"
                      "Please refer to [https://github.com/gavruskin/fitlands] for legal matters, "
                      "to obtain up-to-date bibliographic information for Fitlands, "
                      "and to stay tuned.\n"
                      "If you publish the results obtained with the help of this software, "
                      "please don't forget to cite us.\n")
    output_file.write("\n\n# Marginal two-way interaction (epistasis) analysis\n")

    epi_matrix = np.empty([number_trials, n, n], dtype=float)  # Compute epistasis.
    for trial in range(number_trials):
        for i in range(n):
            for j in range(i + 1, n):  # Loop through pairs of sites (i, j) to find marginal epistasis between i and j.
                epi = 0
                for genotype in data:
                    if genotype[i] == genotype[j] == "0" or genotype[i] == genotype[j] == "1":
                        epi += data[genotype][trial]
                    elif (genotype[i] == "0" and genotype[j] == "1") or (genotype[i] == "1" and genotype[j] == "0"):
                        epi -= data[genotype][trial]
                    else:
                        print("Attention! Your genotypes contain entries different from 0 and 1. Those are skipped.")
                epi_matrix[trial][i][j] = epi

    epi_pos_percent = np.empty([n, n], dtype=float)  # Compute summaries of epistasis.
    epi_neg_percent = np.empty([n, n], dtype=float)
    epi_zero_percent = np.empty([n, n], dtype=float)
    epi_pos_sites = []
    epi_neg_sites = []
    epi_zero_sites = []
    epi_suspected_pos_sites = []  # With all >= 0 and all but one > 0. TODO: This has to be based on a stats test.
    epi_suspected_neg_sites = []
    epi_suspected_zero_sites = []
    for i in range(n):
        for j in range(i + 1, n):
            epi_pos_count = 0
            epi_neg_count = 0
            epi_zero_count = 0
            for trial in range(number_trials):
                if epi_matrix[trial][i][j] > 0:
                    epi_pos_count += 1
                elif epi_matrix[trial][i][j] < 0:
                    epi_neg_count += 1
                else:
                    epi_zero_count += 1
            epi_pos_percent[i][j] = 100 * epi_pos_count / float(number_trials)
            epi_neg_percent[i][j] = 100 * epi_neg_count / float(number_trials)
            epi_zero_percent[i][j] = 100 * epi_zero_count / float(number_trials)
            if epi_pos_percent[i][j] == 100:
                epi_pos_sites.append([i, j])
            elif epi_neg_percent[i][j] == 100:
                epi_neg_sites.append([i, j])
            elif epi_zero_percent[i][j] == 100:
                epi_zero_sites.append([i, j])
            if epi_zero_count == 1:
                if epi_pos_count == number_trials - 1:
                    epi_suspected_pos_sites.append([i, j])
                elif epi_neg_count == number_trials - 1:
                    epi_suspected_neg_sites.append([i, j])
            elif epi_zero_count == number_trials - 1:
                epi_suspected_zero_sites.append([i, j])

    output_file.write("\n\n## Summary\n")  # Write summaries to file.
    output_file.write("\nSites with positive marginal two-way epistasis: ")
    for sites in epi_pos_sites:
        output_file.write("(%s, %s) " % (sites[0] + 1, sites[1] + 1))
    output_file.write("\nSites with negative marginal two-way epistasis: ")
    for sites in epi_neg_sites:
        output_file.write("(%s, %s) " % (sites[0] + 1, sites[1] + 1))
    output_file.write("\nSites with no marginal two-way epistasis: ")
    for sites in epi_zero_sites:
        output_file.write("(%s, %s) " % (sites[0] + 1, sites[1] + 1))
    output_file.write("\n")
    output_file.write("\nSites with suspected positive epistasis: ")
    for sites in epi_suspected_pos_sites:
        output_file.write("(%s, %s) " % (sites[0] + 1, sites[1] + 1))
    output_file.write("\nSites with suspected negative epistasis: ")
    for sites in epi_suspected_neg_sites:
        output_file.write("(%s, %s) " % (sites[0] + 1, sites[1] + 1))
    output_file.write("\nSites with suspected absence of epistasis:")
    for sites in epi_suspected_zero_sites:
        output_file.write("(%s, %s) " % (sites[0] + 1, sites[1] + 1))
    output_file.write("\n")

    output_file.write("\n\n## Epistasis values sorted by sites\n\n")  # Write raw values with fractions to file.
    for i in range(n):
        for j in range(i + 1, n):
            output_file.write("Sites %s and %s:\n" % (i + 1, j + 1))
            output_file.write("Probability of positive epistasis is: %s%%\n"
                              "Probability of negative epistasis is: %s%%\n"
                              "Probability of no epistasis is: %s%%\n"
                              % (round(epi_pos_percent[i][j], 2), round(epi_neg_percent[i][j], 2),
                                 round(epi_zero_percent[i][j], 2)))
            for trial in range(number_trials):
                output_file.write("Epistasis value for sites %s and %s in trial %s is %s\n"
                                  % (i + 1, j + 1, trial + 1, epi_matrix[trial][i][j]))
            output_file.write("\n")

    output_file.close()
    print("The output has been written into file two_way_epistasis_analysis.md in the ./outputs directory.\n")
    return epi_matrix


def marginal_three_way_interaction_analysis(data):
    number_trials = 0
    for genotype in data:
        number_trials = len(data[genotype])
        break
    print("Missing data is currently not supported by three-way interaction analysis. "
          "Make sure your fitness values do not have missing data.\n")
    # TODO: Add support for missing data.
    n = 0  # Number of sites.
    for genotype in data:
        if len(genotype) > n:
            n = len(genotype)
    for genotype in data:  # Make the genotypes look good (all of the same length):
        data[genotype_look_good(genotype, n)] = data.pop(genotype)

    output_file = open("outputs/three_way_epistasis_analysis.md", "w")
    output_file.write("This file has been created using software package Fitlands "
                      "(Alex Gavryushkin, CBG, D-BSSE, ETH Zurich).\n"
                      "Please refer to [https://github.com/gavruskin/fitlands] for legal matters, "
                      "to obtain up-to-date bibliographic information for Fitlands, "
                      "and to stay tuned.\n"
                      "If you publish the results obtained with the help of this software, "
                      "please don't forget to cite us.\n")
    output_file.write("\n\n# Marginal three-way interaction analysis\n")

    epi_matrix = np.empty([number_trials, n, n, n], dtype=float)  # Compute epistasis.
    for trial in range(number_trials):
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):  # Loop through sites (i, j, k) to find marginal interaction (u_111).
                    epi = 0
                    for genotype in data:
                        count_ones = 0
                        if genotype[i] == "1":
                            count_ones += 1
                        if genotype[j] == "1":
                            count_ones += 1
                        if genotype[k] == "1":
                            count_ones += 1
                        if (genotype[i] != "0" and genotype[i] != "1") or (genotype[j] != "0" and genotype[j] != "1") \
                                or (genotype[k] != "0" and genotype[k] != "1"):
                            print("Attention! Your genotypes contain entries different from 0 and 1."
                                  "Those are set to 0.")
                        if count_ones % 2 == 0:
                            epi += data[genotype][trial]
                        else:
                            epi -= data[genotype][trial]
                    epi_matrix[trial][i][j][k] = epi

    epi_pos_percent = np.empty([n, n, n], dtype=float)  # Compute summaries of epistasis.
    epi_neg_percent = np.empty([n, n, n], dtype=float)
    epi_zero_percent = np.empty([n, n, n], dtype=float)
    epi_pos_sites = []
    epi_neg_sites = []
    epi_zero_sites = []
    epi_suspected_pos_sites = []  # With all >= 0 and all but one > 0. TODO: This has to be based on a stats test.
    epi_suspected_neg_sites = []
    epi_suspected_zero_sites = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                epi_pos_count = 0
                epi_neg_count = 0
                epi_zero_count = 0
                for trial in range(number_trials):
                    if epi_matrix[trial][i][j][k] > 0:
                        epi_pos_count += 1
                    elif epi_matrix[trial][i][j][k] < 0:
                        epi_neg_count += 1
                    else:
                        epi_zero_count += 1
                epi_pos_percent[i][j][k] = 100 * epi_pos_count / float(number_trials)
                epi_neg_percent[i][j][k] = 100 * epi_neg_count / float(number_trials)
                epi_zero_percent[i][j][k] = 100 * epi_zero_count / float(number_trials)
                if epi_pos_percent[i][j][k] == 100:
                    epi_pos_sites.append([i, j, k])
                elif epi_neg_percent[i][j][k] == 100:
                    epi_neg_sites.append([i, j, k])
                elif epi_zero_percent[i][j][k] == 100:
                    epi_zero_sites.append([i, j, k])
                if epi_zero_count == 1:
                    if epi_pos_count == number_trials - 1:
                        epi_suspected_pos_sites.append([i, j, k])
                    elif epi_neg_count == number_trials - 1:
                        epi_suspected_neg_sites.append([i, j, k])
                elif epi_zero_count == number_trials - 1:
                    epi_suspected_zero_sites.append([i, j, k])

    output_file.write("\n\n## Summary\n")  # Write summaries to file.
    output_file.write("\nSites with positive marginal three-way interaction: ")
    for sites in epi_pos_sites:
        output_file.write("(%s, %s, %s) " % (sites[0] + 1, sites[1] + 1, sites[2] + 1))
    output_file.write("\nSites with negative marginal three-way interaction: ")
    for sites in epi_neg_sites:
        output_file.write("(%s, %s, %s) " % (sites[0] + 1, sites[1] + 1, sites[2] + 1))
    output_file.write("\nSites with no marginal three-way interaction: ")
    for sites in epi_zero_sites:
        output_file.write("(%s, %s, %s) " % (sites[0] + 1, sites[1] + 1, sites[2] + 1))
    output_file.write("\n")
    output_file.write("\nSites with suspected positive three-way interaction: ")
    for sites in epi_suspected_pos_sites:
        output_file.write("(%s, %s, %s) " % (sites[0] + 1, sites[1] + 1, sites[2] + 1))
    output_file.write("\nSites with suspected negative three-way interaction: ")
    for sites in epi_suspected_neg_sites:
        output_file.write("(%s, %s, %s) " % (sites[0] + 1, sites[1] + 1, sites[2] + 1))
    output_file.write("\nSites with suspected absence of three-way interaction:")
    for sites in epi_suspected_zero_sites:
        output_file.write("(%s, %s, %s) " % (sites[0] + 1, sites[1] + 1, sites[2] + 1))
    output_file.write("\n")

    output_file.write("\n\n## Epistasis values sorted by sites\n\n")  # Write raw values with fractions to file.
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                output_file.write("Sites %s, %s, %s:\n" % (i + 1, j + 1, k + 1))
                output_file.write("Probability of positive three-way interaction is: %s%%\n"
                                  "Probability of negative three-way interaction is: %s%%\n"
                                  "Probability of no three-way interaction is: %s%%\n"
                                  % (round(epi_pos_percent[i][j][k], 2), round(epi_neg_percent[i][j][k], 2),
                                     round(epi_zero_percent[i][j][k], 2)))
                for trial in range(number_trials):
                    output_file.write("Interaction value for sites %s, %s, %s in trial %s is %s\n"
                                      % (i + 1, j + 1, k + 1, trial + 1, epi_matrix[trial][i][j][k]))
                output_file.write("\n")

    output_file.close()
    print("The output has been written into file three_way_epistasis_analysis.md in the ./outputs directory.\n")
    return epi_matrix
