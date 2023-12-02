def find_first_digit(row):
    for char in row:
        if char.isnumeric():
            return char


def convert_words(row):
    conversion = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    i = 0
    while i <= len(row):
        three_char = row[i:i + 3]
        four_char = row[i:i + 4]
        five_char = row[i:i + 5]

        if conversion.get(three_char) is not None:
            row = row[:i] + conversion[three_char] + row[i:]
            i += 1

        elif conversion.get(four_char) is not None:
            row = row[:i] + conversion[four_char] + row[i:]
            i += 1

        elif conversion.get(five_char) is not None:
            row = row[:i] + conversion[five_char] + row[i:]
            i += 1

        i += 1

    return row


def part1(input_list):
    input_list = input_list.split('\n')

    output = 0
    for row in input_list:
        first_digit = find_first_digit(row)
        second_digit = find_first_digit(row[::-1])

        output += int(first_digit + second_digit)

    return output


def part2(input_list):
    input_list = input_list.split('\n')

    output = 0
    for row in input_list:
        row = convert_words(row)
        first_digit = find_first_digit(row)
        second_digit = find_first_digit(row[::-1])

        output += int(first_digit + second_digit)

    return output
