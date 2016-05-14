import random
import os.path


__author__ = '@gavruskin'


# The number of tries to detect zero epistasis.
N = 100000


def get_next_ordering(x):
    y = x
    for i in range(len(x)):
        if x[i] < 8 - i:
            y[i] = x[i] + 1
            for j in range(i):
                y[j] = 1
            return y
    return [8, 7, 6, 5, 4, 3, 2, 1]


def ordering_to_fitness(x):
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    z = []
    for i in range(len(x)):
        z.append(y[x[i] - 1])
        del y[x[i] - 1]
    return z


def get_random_fitness_values():
    z = []
    for i in range(8):
        z.append(random.uniform(0, 1))
    return sorted(z)


# IMPORTANT: w_000 = w_1, w_001 = w_2, w_010 = w_3, w_100 = w_4, w_011 = w_5, w_101 = w_6, w_110 = w_7, w_111 = w_8
def write_epistasis_to_file():
    if not os.path.isfile("./epistasis_with_%s_cheks.txt" % N):
        epistasis_file = open("epistasis_with_%s_cheks.txt" % N, "w")
        epistasis_file.write("IMPORTANT: w_000 = w_1, w_001 = w_2, w_010 = w_3, w_100 = w_4, w_011 = w_5, w_101 = w_6, w_110 = w_7, w_111 = w_8\n")
    else:
        print "File epistasis.txt is not empty"
        return
    ordering = [1, 1, 1, 1, 1, 1, 1, 1]
    fitness = [1, 2, 3, 4, 5, 6, 7, 8]
    fitness_values1 = get_random_fitness_values()
    i = 0
    while i < N:
        fitness_values = get_random_fitness_values()
        epistasis1 = fitness_values1[fitness.index(1)] + fitness_values1[fitness.index(5)] + fitness_values1[fitness.index(6)] + fitness_values1[fitness.index(7)] - fitness_values1[fitness.index(2)] - fitness_values1[fitness.index(3)] - fitness_values1[fitness.index(4)] - fitness_values1[fitness.index(8)]
        epistasis = fitness_values[fitness.index(1)] + fitness_values[fitness.index(5)] + fitness_values[fitness.index(6)] + fitness_values[fitness.index(7)] - fitness_values[fitness.index(2)] - fitness_values[fitness.index(3)] - fitness_values[fitness.index(4)] - fitness_values[fitness.index(8)]
        if epistasis1 * epistasis < 0:
            ordering = get_next_ordering(ordering)
            if ordering == [8, 7, 6, 5, 4, 3, 2, 1]:
                epistasis_file.close()
                return
            fitness = ordering_to_fitness(ordering)
            i = 0
        i += 1
        if i >= N:
            epistasis_file.write(str(fitness) + "\n")
            # DEBUG:
            print "This one!! :"
            print ordering
            print fitness
            # DEBUG^
            if ordering == [8, 7, 6, 5, 4, 3, 2, 1]:
                epistasis_file.close()
                return
            ordering = get_next_ordering(ordering)
            fitness = ordering_to_fitness(ordering)
            i = 0


write_epistasis_to_file()
