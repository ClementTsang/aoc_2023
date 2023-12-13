#!/bin/python3

import sys
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = [[]]
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                lines.append([])
            else:
                lines[-1].append(list(line))

    return lines


def find_horizontal_reflection(pattern: List[List[str]], smudge: int) -> int:
    for row in range(1, len(pattern)):
        top = pattern[:row]
        bottom = pattern[row:]

        checked_length = min(len(top), len(bottom))
        top = top[-checked_length:]
        bottom = bottom[:checked_length]
        bottom = bottom[::-1]

        bad = 0
        for ra, rb in zip(top, bottom):
            for ca, cb in zip(ra, rb):
                if ca != cb:
                    bad += 1

        if bad == smudge:
            return row


def find_reflection(pattern: List[List[str]], smudge: int = 0) -> int:
    result = find_horizontal_reflection(pattern, smudge)
    if result is not None:
        return result * 100

    result = find_horizontal_reflection(list(zip(*pattern[::-1])), smudge)
    if result is not None:
        return result


def part_one():
    lines = read_lines_to_list()
    answer = 0

    for pattern in lines:
        answer += find_reflection(pattern)

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    answer = 0

    for pattern in lines:
        answer += find_reflection(pattern, 1)

    print(f"Part 2: {answer}")


part_one()
part_two()
