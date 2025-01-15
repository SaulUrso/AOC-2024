import csv
import os

path = "inputs" + os.sep
# filename = "test-day2.txt"
filename = "input-day2.txt"

def get_data(path):
    with open(path, "r") as data:
        reader = csv.reader(data, delimiter=" ")
        for line in reader:
            yield list(map(int, line))


def is_safe(report,idx = None):

    negative = None
    i= 1 if idx == 0 else 0
    report = report[:-1] if idx == len(report) -1 else report
    while i < len(report)-1:

        next = 1
        if i+1 == idx :
            next = 2

        diff = report[i] - report[i + next]
        if abs(diff) < 1 or abs(diff) > 3:
            break

        if negative is None:
            negative = True if diff < 0 else False
        elif negative != (diff < 0):
            break

        i += next

    if i < len(report)-1 :
        if idx is not None:
            return 0
        results = [
            is_safe(report, i - 1),
            is_safe(report, i),
            is_safe(report, i + 1),
        ]
        return max(results)

    return 1

if __name__ == "__main__":

    counter = 0
    for report in get_data(path + filename):
        val = is_safe(report)
        counter += val

    print(counter)
