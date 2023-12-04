import re
import json


def part1(input_list):
    input_list = input_list.split('\n')

    points = []
    for row in input_list:
        pattern = '^Card[ ]*([0-9]*): ([ 0-9]*) \| ([ 0-9]*)$'
        match = re.match(pattern, row)

        card_id = match[1]
        winning_numbers = [val for val in match[2].split(' ') if val != '']
        possible_numbers = [val for val in match[3].split(' ') if val != '']

        matching_numbers = []
        for possible_number in possible_numbers:
            if possible_number in winning_numbers:
                matching_numbers.append(possible_number)

        if len(matching_numbers) == 0:
            points.append(0)
        else:
            points.append(2 ** (len(matching_numbers)- 1))

    return sum(points)


def part2(input_list):
    input_list = input_list.split('\n')

    card_data = {}
    for row in input_list:
        pattern = '^Card[ ]*([0-9]*): ([ 0-9]*) \| ([ 0-9]*)$'
        match = re.match(pattern, row)

        card_id = int(match[1])
        winning_numbers = [val for val in match[2].split(' ') if val != '']
        possible_numbers = [val for val in match[3].split(' ') if val != '']

        matching_numbers = []
        for possible_number in possible_numbers:
            if possible_number in winning_numbers:
                matching_numbers.append(possible_number)

        card_data[card_id] = {
            'w': winning_numbers,
            'p': possible_numbers,
            'instances': 1,
            '#_of_winners': len(matching_numbers)
        }

    for i in range(1, max(card_data.keys())+1):
        for j in range(card_data[i]['instances']):
            for k in range(1, card_data[i]['#_of_winners']+1):
                card_data[i+k]['instances'] += 1

    points = 0
    for key, val in card_data.items():
        points += val['instances']

    return points
