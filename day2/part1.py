import os
import csv


path = "Inputs" + os.sep
# filename = "test-day2.txt"
filename = "input-day2.txt"


def get_data(path):
    with open(path, "r") as data:
        reader = csv.reader(data, delimiter=" ")
        for line in reader:
            yield list(map(int, line))


def is_safe(report):

    negative = None
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return 0

        if negative is None:
            negative = True if diff < 0 else False
        elif negative != (diff < 0):
            return 0

    return 1


if __name__ == "__main__":

    counter = 0
    for report in get_data(path + filename):
        val = is_safe(report)
        counter += val

    print(counter)
