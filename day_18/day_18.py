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

    pits = defaultdict(int)
    pits[curr] = 1
    for direction, amount, _colour in lines:
        if direction == "D":
            for _ in range(amount):
                curr = (curr[0] + 1, curr[1])
                pits[curr] += 1
        elif direction == "U":
            for _ in range(amount):
                curr = (curr[0] - 1, curr[1])
                pits[curr] += 1
        elif direction == "L":
            for _ in range(amount):
                curr = (curr[0], curr[1] - 1)
                pits[curr] += 1
        elif direction == "R":
            for _ in range(amount):
                curr = (curr[0], curr[1] + 1)
                pits[curr] += 1

    y_offset = abs(min([y for (y, _x) in pits.keys()])) + 25
    x_offset = abs(min([x for (_y, x) in pits.keys()])) + 25

    height = max([y for (y, _x) in pits.keys()]) + y_offset + 50
    width = max([x for (_y, x) in pits.keys()]) + x_offset + 50

    board = []
    for _ in range(height):
        board.append([])
        for _ in range(width):
            board[-1].append(0)

    for coord, depth in pits.items():
        (y, x) = (coord[0] + y_offset, coord[1] + x_offset)
        # print(y, x)
        board[y][x] = depth

    dots_left = 0
    for row in range(height):
        for col in range(width):
            if board[row][col] > 0:
                # print("#", end="")
                answer += 1
            else:
                # print(".", end="")
                dots_left += 1
        # print("")

    # Flood fill.
    visited = {(0, 0)}
    queue = [(0, 0)]
    while queue:
        (y, x) = queue.pop()
        for neighbour in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            (new_y, new_x) = (y + neighbour[0], x + neighbour[1])
            if (
                new_y >= 0
                and new_x >= 0
                and new_y < height
                and new_x < width
                and (new_y, new_x) not in visited
                and board[new_y][new_x] == 0
            ):
                visited.add((new_y, new_x))
                queue.append((new_y, new_x))

    answer += dots_left - len(visited)

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

    for edge in edges:
        (a, b) = edge
        answer += a[0] * b[1] - a[1] * b[0]

    answer /= 2
    answer = abs(int(answer))

    print(f"Part 2: {answer}")


part_one()
part_two()
