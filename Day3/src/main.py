def left(i, indexes, rows, numeric=False):
    if 0 in indexes:
        return False
    if numeric:
        return rows[i][min(indexes) - 1].isnumeric()
    else:
        return rows[i][min(indexes)-1] != '.'


def right(i, indexes, rows, numeric=False):
    if len(rows[0])-1 in indexes:
        return False
    if numeric:
        rows[i][max(indexes)+1].isnumeric()
    else:
        return rows[i][max(indexes)+1] != '.'


def top(i, indexes, rows, numeric=False):
    if i == 0:
        return False
    if numeric:
        return any([rows[i-1][j].isnumeric() for j in indexes])
    else:
        return any([rows[i-1][j] != '.' for j in indexes])


def bottom(i, indexes, rows, numeric=False):
    if i == len(rows)-1:
        return False
    if numeric:
        return any([rows[i+1][j].isnumeric() for j in indexes])
    else:
        return any([rows[i+1][j] != '.' for j in indexes])


def top_left(i, indexes, rows, numeric=False):
    if i == 0 or 0 in indexes:
        return False
    if numeric:
        return rows[i-1][min(indexes)-1].isnumeric()
    else:
        return rows[i-1][min(indexes)-1] != '.'


def top_right(i, indexes, rows, numeric=False):
    if i == 0 or len(rows[0])-1 in indexes:
        return False
    if numeric:
        rows[i-1][max(indexes)+1].isnumeric()
    else:
        return rows[i-1][max(indexes)+1] != '.'


def bottom_left(i, indexes, rows, numeric=False):
    if i == len(rows)-1 or 0 in indexes:
        return False
    if numeric:
        return rows[i+1][min(indexes)-1].isnumeric()
    else:
        return rows[i+1][min(indexes)-1] != '.'


def bottom_right(i, indexes, rows, numeric=False):
    if i == len(rows)-1 or len(rows[0])-1 in indexes:
        return False
    if numeric:
        return rows[i+1][max(indexes)+1].isnumeric()
    else:
        return rows[i+1][max(indexes)+1] != '.'


def part1(input_list):
    input_list = input_list.split('\n')

    numbers = []
    for i, row in enumerate(input_list):
        indexes = []
        number = ''

        j = 0
        while j < len(row):
            if row[j].isnumeric():
                number += row[j]
                indexes.append(j)
            else:
                if number.isnumeric():
                    if left(i, indexes, input_list) \
                            or right(i, indexes, input_list) \
                            or top(i, indexes, input_list) \
                            or bottom(i, indexes, input_list) \
                            or top_left(i, indexes, input_list) \
                            or top_right(i, indexes, input_list) \
                            or bottom_left(i, indexes, input_list) \
                            or bottom_right(i, indexes, input_list):
                        numbers.append(int(number))
                number = ''
                indexes = []
            j += 1

        # Handle the edge
        if number.isnumeric():
            if left(i, indexes, input_list) \
                    or right(i, indexes, input_list) \
                    or top(i, indexes, input_list) \
                    or bottom(i, indexes, input_list) \
                    or top_left(i, indexes, input_list) \
                    or top_right(i, indexes, input_list) \
                    or bottom_left(i, indexes, input_list) \
                    or bottom_right(i, indexes, input_list):
                numbers.append(int(number))

    return sum(numbers)


def part2(input_list):
    input_list = input_list.split('\n')

    ratios = []
    for i, row in enumerate(input_list):
        j = 0
        while j < len(row):
            if row[j] == '*':
                    if left(i, [j], input_list, numeric=True) \
                            or right(i, [j], input_list, numeric=True) \
                            or top(i, [j], input_list, numeric=True) \
                            or bottom(i, [j], input_list, numeric=True) \
                            or top_left(i, [j], input_list, numeric=True) \
                            or top_right(i, [j], input_list, numeric=True) \
                            or bottom_left(i, [j], input_list, numeric=True) \
                            or bottom_right(i, [j], input_list, numeric=True):
                        adjacent_numbers = get_adjacent_numbers(i, [j], input_list)
                        if len(adjacent_numbers) == 2:
                            ratios.append(adjacent_numbers[0] * adjacent_numbers[1])
            j += 1

        # Handle the edge
        if row[j] == '*':
            if left(i, [j], input_list, numeric=True) \
                    or right(i, [j], input_list, numeric=True) \
                    or top(i, [j], input_list, numeric=True) \
                    or bottom(i, [j], input_list, numeric=True) \
                    or top_left(i, [j], input_list, numeric=True) \
                    or top_right(i, [j], input_list, numeric=True) \
                    or bottom_left(i, [j], input_list, numeric=True) \
                    or bottom_right(i, [j], input_list, numeric=True):
                adjacent_numbers = get_adjacent_numbers(i, [j], input_list)
                if len(adjacent_numbers) == 2:
                    ratios.append(adjacent_numbers[0] * adjacent_numbers[1])

    return sum(ratios)
