from collections import deque
import itertools
from functools import reduce
import math


def part1(input_list):
    input_list = input_list.split('\n')

    instructions = input_list[0]

    location_map = {}
    for i in range(2, len(input_list)):
        location, paths = input_list[i].split(' = ')

        L, R = paths[1:-1].split(', ')
        location_map[location] = {'L': L, 'R': R}

    current_location = 'AAA'
    steps = 0
    while current_location != 'ZZZ':
        step = instructions[steps % len(instructions)]
        new_location = location_map[current_location][step]

        current_location = new_location
        steps += 1

    return steps


def part2(input_list):
    input_list = input_list.split('\n')

    instructions = input_list[0]

    location_map = {}
    current_locations = []
    for i in range(2, len(input_list)):
        location, paths = input_list[i].split(' = ')

        L, R = paths[1:-1].split(', ')
        location_map[location] = {'L': L, 'R': R}
        if location[-1] == 'A':
            current_locations.append(location)

    location_stops = {}
    for current_location in current_locations:
        steps = 0
        visited = []
        while True:
            location_str = f'{current_location}{steps % len(instructions)}'
            if location_str in visited:
                visited.append(location_str)
                break
            visited.append(location_str)
            step = instructions[steps % len(instructions)]
            new_location = location_map[current_location][step]

            current_location = new_location
            steps += 1
        location_stops[current_location] = {'visited': [val[2] for val in visited]}

    max_visited = 0
    for location, data in location_stops.items():
        visited = data['visited']

        repeating_start = visited.index(visited[-1])
        data['repeating_start'] = repeating_start

        repeating_pattern = visited[repeating_start:-1]
        data['repeating_pattern'] = repeating_pattern

        data['visited'] = visited[:-1]
        if len(visited) - 1 > max_visited:
            max_visited = len(visited) - 1

    for location, data in location_stops.items():
        visited = data['visited']
        while len(visited) < max_visited:
            visited.extend(data['repeating_pattern'])
        roll = abs(len(data['repeating_pattern']) - abs(len(visited) - max_visited)) % len(data['repeating_pattern'])
        data['visited'] = visited[:max_visited]
        if roll > 0:
            dq = deque(data['repeating_pattern'])
            dq.rotate(-1 * (roll % len(data['repeating_pattern'])))
            data['repeating_pattern'] = list(dq)

    for location, data in location_stops.items():
        z_locs = []
        for i, letter in enumerate(data['repeating_pattern']):
            if letter == 'Z':
                z_locs.append([i+1,i+1+len(data['repeating_pattern'])])
        data['Zs'] = z_locs

    min_x = float('inf')
    for line_combinations in itertools.product(*[data['Zs'] for data in location_stops.values()]):
        for i in range(0, len(line_combinations)-1):
            if i == 0:
                a = line_combinations[i][0]
                m = line_combinations[i][1] - a

            b = line_combinations[i+1][0]
            n = line_combinations[i+1][1] - b

            d = math.gcd(m, n)

            if a % d != b % d:
                break

            j = 0
            while True:
                val = a + m * j
                if val % n == b % n:
                    break
                j += 1

            a = val
            m = math.lcm(m, n)
        else:
            if a < min_x:
                min_x = a

    return min_x + len(data['visited']) - 1
