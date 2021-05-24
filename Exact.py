import sys
from collections import defaultdict


def findFreq(thres, file):
    holder = defaultdict(int)
    total_transactions = 0
    results = []
    while True:
        line = file.readline()
        if not line:
            break
        total_transactions = total_transactions + 1
        for element in line.split():
            holder[element] = holder[element] + 1

    for key in holder:
        if holder[key] / total_transactions >= thres:
            results.append((int(key), round(holder[key] / total_transactions, 5)))
    results.sort(key=lambda tup: tup[1], reverse=True)
    # sort by tuple taken from:
    # https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    file.seek(0)
    file.close()
    return results  # findFreq()


if __name__ == '__main__':
    file = open(sys.argv[2], "r")
    theta = float(sys.argv[1])
    result = findFreq(theta, file)
    for item in result:
        print(item)
