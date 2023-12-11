#!/bin/python3

import sys
from collections import defaultdict

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def part_1():
    RED = 12
    GREEN = 13
    BLUE = 14

    count = 0
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            id = int(line.split(": ")[0].split(" ")[-1])
            sets = [s.strip().split(", ") for s in (line.split(": ")[1]).split(";")]

            valid = True
            for se in sets:
                used = defaultdict(int)
                for val in se:
                    tmp = val.split(" ")
                    used[tmp[1]] = int(tmp[0])

                if used["red"] > RED or used["blue"] > BLUE or used["green"] > GREEN:
                    valid = False

            if valid:
                count += id

    print(f"Part 1: {count}")


def part_2():
    RED = 12
    GREEN = 13
    BLUE = 14

    sum = 0
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            sets = [s.strip().split(", ") for s in (line.split(": ")[1]).split(";")]

            used = defaultdict(int)
            for se in sets:
                for val in se:
                    tmp = val.split(" ")
                    used[tmp[1]] = max(used[tmp[1]], int(tmp[0]))

            sum += used["red"] * used["blue"] * used["green"]

    print(f"Part 2: {sum}")


part_1()
part_2()
