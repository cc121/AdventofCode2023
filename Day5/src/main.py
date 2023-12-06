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
        dtm_lower, dtm_upper = [int(dtm_val) for dtm_val in dtm.split('-')]
        while dtm_lower <= dtm_upper:
            for key, val in data.items():
                lower, upper = [int(bound) for bound in key.split('-')]
                if lower <= dtm_lower <= upper:
                    start = val['start']
                    start_range = abs(lower - dtm_lower)
                    end_range = min(dtm_upper, upper) - dtm_lower
                    result.append(f"{start+start_range}-{start+start_range+end_range}")
                    dtm_lower += end_range + 1
                    break
            else:
                min_dist = float('inf')
                min_key = None
                for key in data.keys():
                    lower, upper = [int(val) for val in key.split('-')]
                    if dtm_lower <= lower and lower - dtm_lower < min_dist:
                        min_dist = lower - dtm_lower
                        min_key = key

                if min_key is not None:
                    result.append(f"{dtm_lower}-{min(dtm_upper, dtm_lower+min_dist-1)}")
                    dtm_lower += min_dist
                else:
                    result.append(f"{dtm_lower}-{dtm_upper}")
                    dtm_lower = dtm_upper + 1
    i += 2
    return i, result


def part1(input_list):
    input_list = input_list.split('\n')

    # Get seeds
    i = 0
    seeds = [f"{val}-{val}" for val in input_list[i][7:].split(' ')]
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

    locations = [int(val.split('-')[0]) for val in locations]
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

    locations = [int(val.split('-')[0]) for val in locations]
    return min(locations)

