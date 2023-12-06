import re

def get_map_and_map(i, input_list, data_to_map):
    data = {}
    while i < len(input_list) and input_list[i] != '':
        range_start, source_range_start, range_length = [int(val) for val in input_list[i].split(' ')]
        data[f"{source_range_start}-{source_range_start+range_length-1}"] = {
            "start": range_start,
            "range": range_length
        }
        i += 1

    result = []
    for dtm in data_to_map:
        for key, val in data.items():
            lower, upper = [int(bound) for bound in key.split('-')]
            if dtm >= lower and dtm <= upper:
                value_range = dtm - lower
                result.append(val['start'] + value_range)
                break
        else:
            result.append(dtm)
    i += 2

    return i, result


def part1(input_list):
    input_list = input_list.split('\n')

    # Get seeds
    i = 0
    seeds = [int(val) for val in input_list[i][7:].split(' ')]
    i += 3

    # Get seed to soil map
    i, soils = get_map_and_map(i, input_list, seeds)

    # Get soil to fertilizer map
    i, fertilizers = get_map_and_map(i, input_list, soils)

    # Get fertilizer to water map
    i, water = get_map_and_map(i, input_list, fertilizers)

    # Get water to light map
    i, light = get_map_and_map(i, input_list, water)

    # Get light to temp map
    i, temps = get_map_and_map(i, input_list, light)

    # Get temp to humidity map
    i, humidity = get_map_and_map(i, input_list, temps)

    # Get humidity to location map
    i, locations = get_map_and_map(i, input_list, humidity)

    return min(locations)


def part2(input_list):
    input_list = input_list.split('\n')

    # Get seeds
    i = 0
    seed_data = [int(val) for val in input_list[i][7:].split(' ')]
    i += 3

    seeds = []
    for j in range(0, len(seed_data), 2):
        seed_start = seed_data[j]
        seed_range = seed_data[j+1]
        seeds.append(f"{seed_start}-{seed_start+seed_range-1}")

    print(seeds)

    # Get seed to soil map
    i, soils = get_map_and_map(i, input_list, seeds)

    # Get soil to fertilizer map
    i, fertilizers = get_map_and_map(i, input_list, soils)

    # Get fertilizer to water map
    i, water = get_map_and_map(i, input_list, fertilizers)

    # Get water to light map
    i, light = get_map_and_map(i, input_list, water)

    # Get light to temp map
    i, temps = get_map_and_map(i, input_list, light)

    # Get temp to humidity map
    i, humidity = get_map_and_map(i, input_list, temps)

    # Get humidity to location map
    i, locations = get_map_and_map(i, input_list, humidity)

    return min(locations)
