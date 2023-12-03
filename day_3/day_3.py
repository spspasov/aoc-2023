import os
import re
from functools import reduce

def is_symbol(c: str) -> bool:
    return not(c.isdigit() or c == '.')

def num_is_adjacent_to_symbol(row: int, start: int, end: int) -> bool:
    if check_positions_for_symbol(row, [start-1, end+1]):
        return True

    if check_range_for_symbol(row-1, start-1, end+1):
        return True

    if check_range_for_symbol(row+1, start-1, end+1):
        return True


def check_range_for_symbol(row: int, start: int, end: int) -> bool:
    for pos in range(start, end+1):
        if is_symbol(rows[row][pos]):
            return True

def check_positions_for_symbol(row: int, positions: list[int]) -> bool:
    for pos in positions:
        if is_symbol(rows[row][pos]):
            return True

nums: list = []
rows: list[str] = []

def aoc_3():
    with open('input_3.txt') as file:
        global rows
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
                        if num_is_adjacent_to_symbol(row_index, start, end):
                            nums.append(int(cur_num))

                        # finally reset the accumulator
                        cur_num = ''
                    is_digit = False

        print(reduce(lambda a, b: a + b, nums))

if __name__ == '__main__':
    aoc_3()
