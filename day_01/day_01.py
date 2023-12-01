#!/bin/python3

import sys

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

NUM_STRINGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part_1():
    with open(FILE, "r", encoding="utf-8") as f:
        total = 0
        for line in f:
            first = None
            last = None
            for c in line:
                if c.isdigit():
                    if first is None:
                        first = int(c)
                    last = int(c)

            val = first * 10 + last
            print(val)
            total += val
        print(f"Part 1: {total}")


def part_2():
    with open(FILE, "r", encoding="utf-8") as f:
        total = 0
        for line in f:
            line = line.strip()
            first = None
            last = None

            curr_string = ""

            for c in line:
                if c.isdigit():
                    if first is None:
                        first = int(c)
                    last = int(c)
                    curr_string = ""
                    continue

                curr_string += c
                for itx, num in enumerate(NUM_STRINGS):
                    if num in curr_string:
                        if first is None:
                            first = itx + 1
                        last = itx + 1
                        curr_string = curr_string[-1]
                        break

            val = first * 10 + last
            print(val)
            total += val
        print(f"Part 2: {total}")


def main():
    part_1()
    part_2()


main()
