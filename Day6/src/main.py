def calculate_distance(current_speed, time_remaining):
    return current_speed * time_remaining


def calculate_number_of_ways_to_win(race):
    total_time, target_distance = race

    current_speed = 0
    current_time = 0
    time_remaining = total_time - current_time

    number_of_wins = 0
    while time_remaining != 0:
        if calculate_distance(current_speed, time_remaining) > target_distance:
            number_of_wins += 1

        current_speed += 1
        current_time += 1
        time_remaining = total_time - current_time

    return number_of_wins


def part1(input_list):
    input_list = input_list.split('\n')

    times = None
    distances = None
    for i, row in enumerate(input_list):
        row = row.split(':')[-1]
        row = [int(val) for val in row.split(' ') if val != '']
        if i == 0:
            times = row
        else:
            distances = row
    races = zip(times, distances)

    ways_to_win = []
    for race in races:
        ways_to_win.append(calculate_number_of_ways_to_win(race))

    result = 1
    for way_to_win in ways_to_win:
        result *= way_to_win
    return result


def part2(input_list):
    input_list = input_list.split('\n')

    times = None
    distances = None
    for i, row in enumerate(input_list):
        row = row.split(':')[-1]
        row = [val for val in row.split(' ') if val != '']
        row = [int(''.join(row))]
        if i == 0:
            times = row
        else:
            distances = row

    races = zip(times, distances)

    ways_to_win = []
    for race in races:
        ways_to_win.append(calculate_number_of_ways_to_win(race))

    result = 1
    for way_to_win in ways_to_win:
        result *= way_to_win
    return result

