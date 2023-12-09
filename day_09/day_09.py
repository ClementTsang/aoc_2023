#!/bin/python3

import sys
from itertools import pairwise
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append([int(val) for val in line.split()])

    return lines


def build_and_rev_sequences(start: List[int]) -> List[List[int]]:
    """Builds the sequences, then reverses them."""

    sequences = [start]
    while any(val != 0 for val in sequences[-1]):
        curr = sequences[-1]
        next_sequence = [b - a for (a, b) in pairwise(curr)]
        sequences.append(next_sequence)

    sequences.reverse()

    return sequences


def part_one():
    lines = read_lines_to_list()
    answer = 0

    for line in lines:
        sequences = build_and_rev_sequences(line[:])
        sequences[0].append(0)

        for prev, curr in pairwise(sequences):
            curr.append(curr[-1] + prev[-1])

        answer += sequences[-1][-1]

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    for line in lines:
        sequences = build_and_rev_sequences(line[:])
        sequences[0].append(0)  # Can just stick it at the end because they're all 0 anyways.

        for prev, curr in pairwise(sequences):
            curr.insert(0, curr[0] - prev[0])

        answer += sequences[-1][0]

    print(f"Part 2: {answer}")


part_one()
part_two()
