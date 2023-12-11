#!/bin/python3

import sys
from typing import List, Tuple

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


def expand(image: List[List[str]]):
    length = len(image)
    width = len(image[0])

    no_galaxy_row = []

    for i in range(length):
        if "#" not in image[i]:
            no_galaxy_row.append(i)

    no_galaxy_col = []
    for i in range(width):
        to_check = [image[j][i] for j in range(length)]
        if "#" not in to_check:
            no_galaxy_col.append(i)

    no_galaxy_row.reverse()
    no_galaxy_col.reverse()

    for index in no_galaxy_row:
        new_row = []
        for i in range(width):
            new_row.append(".")
        image.insert(index, new_row)

    new_length = len(image)
    for index in no_galaxy_col:
        for i in range(new_length):
            image[i].insert(index, ".")


def part_one():
    image = read_lines_to_list()
    answer = 0
    expand(image)

    galaxies = []
    for row in range(len(image)):
        for col in range(len(image[row])):
            if image[row][col] == "#":
                galaxies.append((row, col))

    pairs = set()
    for a in galaxies:
        for b in galaxies:
            if a == b:
                continue

            if a < b:
                start = a
                end = b
            else:
                start = b
                end = a

            pairs.add((start, end))

    for start, end in pairs:
        answer += abs(start[0] - end[0]) + abs(start[1] - end[1])

    print(f"Part 1: {answer}")


def part_two():
    image = read_lines_to_list()
    answer = 0

    length = len(image)
    width = len(image[0])

    galaxies = {}
    for row in range(len(image)):
        for col in range(len(image[row])):
            if image[row][col] == "#":
                galaxies[(row, col)] = (row, col)

    no_galaxy_row = []
    for i in range(length):
        if "#" not in image[i]:
            no_galaxy_row.append(i)

    no_galaxy_col = []
    for i in range(width):
        to_check = [image[j][i] for j in range(length)]
        if "#" not in to_check:
            no_galaxy_col.append(i)

    no_galaxy_row.reverse()
    no_galaxy_col.reverse()

    for row in no_galaxy_row:
        for original, new in galaxies.items():
            if original[0] > row:
                galaxies[original] = (new[0] + 1000000 - 1, new[1])

    for col in no_galaxy_col:
        for original, new in galaxies.items():
            if original[1] > col:
                galaxies[original] = (new[0], new[1] + 1000000 - 1)

    new_galaxies = list(galaxies.values())

    pairs = set()
    for a in new_galaxies:
        for b in new_galaxies:
            if a == b:
                continue

            if a < b:
                start = a
                end = b
            else:
                start = b
                end = a

            pairs.add((start, end))

    for start, end in pairs:
        answer += abs(start[0] - end[0]) + abs(start[1] - end[1])

    print(f"Part 2: {answer}")


part_one()
part_two()
