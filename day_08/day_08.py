#!/bin/python3

import sys
import numpy as np
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
    answer = 0

    instructions = list(lines.pop(0))
    lines.pop(0)

    nodes = dict()
    curr = "AAA"
    for line in lines:
        split = line.split(" = ")
        node = split[0]
        split = split[1].split(", ")
        left = split[0][1:]
        right = split[1][:-1]

        nodes[node] = (left, right)

    while curr != "ZZZ":
        for instruction in instructions:
            (left, right) = nodes[curr]
            if instruction == "L":
                curr = left
            else:
                curr = right
            answer += 1

            if curr == "ZZZ":
                break

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()

    instructions = list(lines.pop(0))
    lines.pop(0)

    nodes = dict()
    currs = []
    for line in lines:
        split = line.split(" = ")
        node = split[0]
        split = split[1].split(", ")
        left = split[0][1:]
        right = split[1][:-1]

        nodes[node] = (left, right)

        if node.endswith("A"):
            currs.append(node)

    endings = []

    for curr in currs:
        curr_answer = 0
        while not curr.endswith("Z"):
            for instruction in instructions:
                (left, right) = nodes[curr]
                if instruction == "L":
                    curr = left
                else:
                    curr = right
                curr_answer += 1

                if curr.endswith("Z"):
                    break
        endings.append(curr_answer)

    answer = np.lcm.reduce(np.array(endings))
    print(f"Part 2: {answer}")


part_one()
part_two()
