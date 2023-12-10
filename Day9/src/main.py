from collections import deque
import itertools
import math

def predict(data, reverse=False):
    if all([val == 0 for val in data]):
        return 0

    deltas = []
    for i in range(len(data)-1):
        deltas.append(data[i+1] - data[i])
    p = predict(deltas, reverse)
    if reverse:
        return data[0] - p
    else:
        return p + data[-1]

def part1(input_list):
    input_list = input_list.split('\n')

    result = []
    for row in input_list:
        data = [int(val) for val in row.split(' ')]
        result.append(predict(data))

    return sum(result)


def part2(input_list):
    input_list = input_list.split('\n')

    result = []
    for row in input_list:
        data = [int(val) for val in row.split(' ')]
        result.append(predict(data, reverse=True))

    return sum(result)
