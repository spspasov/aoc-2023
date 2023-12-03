from functools import reduce
from typing import Optional

def is_symbol(c: str) -> bool:
    return not(c.isdigit() or c == '.')

def is_gear(c: str) -> bool:
    return c == '*'

# def is_used_gear(c: str) -> bool:
#     return c == 'x'

def num_is_adjacent_to_symbol(row: int, start: int, end: int) -> Optional[list[int]]:
    # check the sides
    pos = check_positions_for_symbol(row, [start-1, end+1])
    if pos:
        return pos

    # check the row above, including the diagonals
    pos = check_range_for_symbol(row-1, start-1, end+1)
    if pos:
        return pos

    # check the row below, including the diagonals
    pos = check_range_for_symbol(row+1, start-1, end+1)
    if pos:
        return pos


def check_range_for_symbol(row: int, start: int, end: int) -> Optional[list[int]]:
    for pos in range(start, end+1):
        if is_gear(rows[row][pos]):
            return [row, pos]

def check_positions_for_symbol(row: int, positions: list[int]) -> Optional[list[int]]:
    for pos in positions:
        if is_gear(rows[row][pos]):
            return [row, pos]

nums: list = []
rows: list[str] = []

# used_gears = {
# row, [pos, num_1, num_2]
# 1: {4: [467, 35]}
# }
# we need to only take gears that have 2 numbers attached to them
used_gears: dict[dict[dict[list]]] = {}

def aoc_3():
    with open('test.txt') as file:
        global rows
        global used_gears
        rows = file.readlines()

        for row_index, row in enumerate(rows):
            cur_num: str = ''
            is_digit = False

            for i in range(0, len(row)):
                if row[i].isdigit():
                    cur_num += row[i]
                    is_digit = True
                else:
                    # if we had been accumulating digits so far, we need to store them and reset the accumulator
                    # keep in mind we'll be at the next character already, index-wise
                    if is_digit:
                        # we also need to see if we're adjacent to a symbol anywhere
                        start = i - len(cur_num)
                        end = i - 1

                        pos = num_is_adjacent_to_symbol(row_index, start, end)

                        # if we have pos, then we have found a gear
                        if pos:
                            # used_gears = {
                            # row, [pos, num_1, num_2]
                            # 1: {4: [467, 35]}
                            # }
                            try:
                                old_num = used_gears[pos[0]][pos[1]][0]
                            except KeyError as error:
                                old_num = None

                            # we have a bug here where we're overriding on the row level if more than 1 gear on same row
                            if old_num:
                                used_gears[pos[0]] = {pos[1]: [int(cur_num), old_num]}
                                # used_gears[pos[0]] = used_gears[pos[0]] | {pos[1]: [int(cur_num)]}
                            else:
                                # doesn't necessarily mean we don't have other chars with values!!!
                                try:
                                    used_gears[pos[0]] = used_gears[pos[0]] | {pos[1]: [int(cur_num)]}
                                except KeyError as error:
                                    used_gears[pos[0]] = {pos[1]: [int(cur_num)]}

                        # finally reset the accumulator
                        cur_num = ''
                        print(used_gears)
                    is_digit = False

        gear_ratios: int = 0
        x_used_nums = []

        for used_rows in used_gears:
            for used_chars in used_gears[used_rows]:
                used_nums = used_gears[used_rows][used_chars]
                if len(used_nums) == 2:
                    x_used_nums.append([used_nums[0], used_nums[1]])
                    gear_ratios += used_nums[0] * used_nums[1]

        print(used_gears)
        # print(gear_ratios)
        # print(len(x_used_nums))


if __name__ == '__main__':
    aoc_3()
