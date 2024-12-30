import os
import numpy as np
import time
import csv

start_time = time.time()

path = "Inputs" + os.sep
filename = "day1-input.csv"
# filename = "test_input_day1.csv"


def get_input(path):
    list_1 = list()
    list_2 = list()
    with open(path, "r") as input_file:
        inputreader = csv.reader(input_file, delimiter=" ", skipinitialspace=True)
        for line in inputreader:
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))

    return list_1, list_2


def compute_total_similarity(list_1, list_2):
    list_1 = np.sort(list_1)
    list_2 = np.sort(list_2)

    total_score = 0
    prec_score = 0
    prec_num = None
    idx2 = 0
    for n_1 in list_1:
        if prec_num is not None and prec_num == n_1:
            total_score += prec_score
        else:
            occurrences = 0
            while list_2[idx2] < n_1:
                idx2 += 1
            while list_2[idx2] == n_1:
                idx2 += 1
                occurrences += 1
            prec_score = n_1 * occurrences
            prec_num = n_1
            total_score += prec_score

    return total_score


if __name__ == "__main__":
    list_1, list_2 = get_input(path + filename)
    print(compute_total_similarity(list_1, list_2))

print("--- %s seconds ---" % (time.time() - start_time))
