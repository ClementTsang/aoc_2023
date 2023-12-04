#!/bin/python3

import copy
import sys
from collections import defaultdict
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def part_one():
    lines = read_lines_to_list()
    scores = []

    for line in lines:
        line = line.split(": ")[1]
        [winning, have] = line.split(" | ")
        winning = {int(val) for val in winning.split(" ") if val.isdigit()}
        have = {int(val) for val in have.split(" ") if val.isdigit()}

        num_match = len(winning.intersection(have))
        score = pow(2, num_match - 1) if num_match > 0 else 0

        # print(f"winning: {winning} - have: {have} -> {score}")

        scores.append(score)

    final_score = sum(scores)
    print(f"Part 1: {final_score}")


def part_two():
    lines = read_lines_to_list()
    num_cards = 0
    num_initial_cards = len(lines)
    total_cards = defaultdict(int)

    for itx, line in enumerate(lines):
        line = line.split(": ")[1]
        [winning, have] = line.split(" | ")
        winning = {int(val) for val in winning.split(" ") if val.isdigit()}
        have = {int(val) for val in have.split(" ") if val.isdigit()}

        total_cards[itx] += 1

        num_match = len(winning.intersection(have))
        # print(f"itx: {itx} - winning: {winning} - have: {have} -> {num_match}")
        if num_match > 0:
            for i in range(itx + 1, itx + 1 + num_match):
                total_cards[i] += 1 * total_cards[itx]

    # print(sorted(list(total_cards.items())))

    for itx, num in total_cards.items():
        if itx <= num_initial_cards:
            num_cards += num
    print(f"Part 2: {num_cards}")


part_one()
part_two()
