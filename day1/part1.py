import os
import numpy as np
import csv
import time

start_time = time.time()

path = "Inputs" + os.sep
# filename = "day1-input.csv"
filename = "day1-input.csv"


def get_input(path):
    list_1 = list()
    list_2 = list()
    with open(path, "r") as input_file:
        inputreader = csv.reader(input_file, delimiter=" ", skipinitialspace=True)
        for line in inputreader:
            list_1.append(int(line[0]))
            list_2.append(int(line[1]))

    return np.array(list_1), np.array(list_2)


def compute_total_distance(list_1, list_2):
    list_1 = np.sort(list_1)
    list_2 = np.sort(list_2)

    return np.sum(np.abs(list_1 - list_2))


if __name__ == "__main__":
    list_1, list_2 = get_input(path + filename)
    print(compute_total_distance(list_1, list_2))


print("--- %s seconds ---" % (time.time() - start_time))
