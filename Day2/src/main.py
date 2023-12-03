def parse_game(game):
    game_info, round_info = game.split(':')

    game_id = int(game_info.replace('Game ', ''))

    rounds = []
    for round in round_info[1:].split('; '):
        round_data = {}
        for cube_info in round.split(', '):
            number, color = cube_info.split(' ')
            round_data[color] = int(number)
        rounds.append(round_data)

    return game_id, rounds
def part1(input_list):
    cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    input_list = input_list.split('\n')

    game_ids = set()
    impposible = set()
    for game in input_list:
        game_id, rounds = parse_game(game)
        game_ids.add(game_id)
        for round in rounds:
            for color, number in round.items():
                if number > cubes[color]:
                    impposible.add(game_id)
    return sum(game_ids - impposible)


def part2(input_list):
    input_list = input_list.split('\n')

    output = 0
    for game in input_list:
        game_id, rounds = parse_game(game)

        cubes = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for round in rounds:
            for color, number in round.items():
                if number > cubes[color]:
                    cubes[color] = number

        result = 1
        for color, number in cubes.items():
            result *= number

        output += result
    return output
