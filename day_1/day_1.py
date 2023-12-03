import os
import re


def string2digit(string: str) -> str:
    if string.isdigit():
        return string

    d = {
        "zero": '0',
        "nil": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        "ten": '10',
    }

    return d[string]


def aoc_1():
    with open('input_1.txt') as file:
        lines = file.readlines()
        sum: int = 0

        for line in lines:
            numbers: str = ''

            spelled_numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten|[0-9]+)"

            cursor_numbers = []

            for cursor in range(len(line)):
                x = re.findall(spelled_numbers, line[cursor:])

                # only add the array if there are any numbers present
                if len(x) != 0:
                    cursor_numbers.append(x)

            sum += int(string2digit(cursor_numbers[0][0])[0] + string2digit(cursor_numbers[-1][-1])[-1])

        print(sum)
        file.close()


if __name__ == '__main__':
    aoc_1()
