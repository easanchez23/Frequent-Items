import math
import sys
from collections import defaultdict
import random


def getSample(ssize, dsize):
    index = random.sample(range(0, dsize - 1), ssize)
    index.sort()
    return index  # getSample()


def findFreq(ssize, dsize, delta, thres, file):
    index = getSample(ssize, dsize)
    results = []
    holder = defaultdict(int)
    max_trans = 0
    line_counter = -1
    index_counter = 0
    while True:
        if index_counter >= len(index):
            break
        line = file.readline()
        if not line:
            break
        line_counter = line_counter + 1
        if line_counter == index[index_counter]:
            index_counter = index_counter + 1
            temp = 0
            for element in line.split():
                temp = temp + 1
                holder[element] = holder[element] + 1
                max_trans = max(temp, max_trans)
    d_s = math.log(max_trans, 2) + 1
    eps = math.sqrt((2 * (d_s + math.log(1 / delta))) / ssize)
    for key in holder:
        if holder[key] / ssize >= thres - (eps / 2):
            results.append((int(key), round(holder[key] / ssize, 5)))
    results.sort(key=lambda tup: tup[1], reverse=True)
    # sort by tuple taken from:
    # https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    file.seek(0)
    file.close()
    return eps, results  # findFreq()


if __name__ == '__main__':
    file = open(sys.argv[5], "r")
    ssize = int(sys.argv[1])
    dsize = int(sys.argv[2])
    delta = float(sys.argv[3])
    thres = float(sys.argv[4])
    result = findFreq(ssize, dsize, delta, thres, file)
    print(result[0])
    for item in result[1]:
        print(item)
    file.close()
