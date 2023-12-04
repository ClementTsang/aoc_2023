#!/bin/python3

import sys
from collections import defaultdict

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def is_symbol(val: str):
    return not val.isdigit() and val != "."


def possible_gear(val: str):
    return val == "*"


def solve():
    sum = 0
    with open(FILE, "r", encoding="utf-8") as f:
        schematic = []

        for line in f:
            line = line.strip()
            schematic.append(list(line))

        curr_number = None
        curr_number_valid = False

        possible_gears = defaultdict(list)
        next_to_gear = None

        for i in range(0, len(schematic)):
            if curr_number is not None and curr_number_valid:
                sum += curr_number
                if next_to_gear is not None:
                    possible_gears[next_to_gear].append(curr_number)

            curr_number = None
            curr_number_valid = False
            next_to_gear = None

            for j in range(0, len(schematic[i])):
                val: str = schematic[i][j]

                if val.isdigit():
                    if curr_number is None:
                        curr_number = int(val)
                    else:
                        curr_number = curr_number * 10 + int(val)

                    # Check in all 8 directions around number to see if valid
                    for m in [-1, 0, 1]:
                        for n in [-1, 0, 1]:
                            if i + m >= 0 and i + m < len(schematic) and j + n >= 0 and j + n < len(schematic[i + m]):
                                check = schematic[i + m][j + n]
                                curr_number_valid |= is_symbol(check)

                                if possible_gear(check):
                                    next_to_gear = (i + m, j + n)

                else:
                    if curr_number is not None:
                        if curr_number_valid:
                            sum += curr_number
                            possible_gears[next_to_gear].append(curr_number)

                    curr_number = None
                    curr_number_valid = False
                    next_to_gear = None

    print(f"Part 1: {sum}")

    sum = 0
    for nums in possible_gears.values():
        if len(nums) == 2:
            total = nums[0] * nums[1]
            sum += total

    print(f"Part 2: {sum}")


solve()
