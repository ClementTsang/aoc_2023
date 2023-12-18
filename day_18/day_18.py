#!/bin/python3

import sys
from collections import defaultdict
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
sys.setrecursionlimit(100000)


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split()
            lines.append((line[0], int(line[1]), line[2][2:-1]))

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    curr = (0, 0)
    edges = []

    for direction, amount, _colour in lines:
        prev = curr
        if direction == "R":
            # Right
            curr = curr[0], curr[1] + amount
        elif direction == "D":
            # Down
            curr = curr[0] + amount, curr[1]
        elif direction == "L":
            # Left
            curr = curr[0], curr[1] - amount
        elif direction == "U":
            # Up
            curr = curr[0] - amount, curr[1]
        edges.append((prev, curr))
        answer += amount
    edges.append((curr, (0, 0)))

    area = 0

    # Shoelace
    for edge in edges:
        (a, b) = edge
        area += a[1] * b[0] - a[0] * b[1]
    area = int(abs(area) / 2)

    # Pick's theorem
    square_area = int(area - answer / 2 + 1)

    answer += square_area
    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    curr = (0, 0)
    edges = set()

    for _, _, colour in lines:
        amount = int(colour[0:-1], 16)
        direction = int(colour[-1])

        prev = curr
        if direction == 0:
            # Right
            curr = curr[0], curr[1] + amount
        elif direction == 1:
            # Down
            curr = curr[0] + amount, curr[1]
        elif direction == 2:
            # Left
            curr = curr[0], curr[1] - amount
        elif direction == 3:
            # Up
            curr = curr[0] - amount, curr[1]
        edges.add((prev, curr))
        answer += amount

    area = 0

    # Shoelace
    for edge in edges:
        (a, b) = edge
        area += a[1] * b[0] - a[0] * b[1]
    area = int(abs(area) / 2)

    # Pick's theorem
    square_area = int(area - answer / 2 + 1)

    answer += square_area

    print(f"Part 2: {answer}")


part_one()
part_two()
