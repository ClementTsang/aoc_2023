#!/bin/python3

import sys
from typing import Dict, List, Tuple

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
sys.setrecursionlimit(100000)


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


def get_rocks(lines: List[List[str]]) -> Dict[Tuple[int, int], str]:
    rocks = dict()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] in "O#":
                rocks[(row, col)] = lines[row][col]

    return rocks


def print_board(maze: Tuple[List[List[str]], Dict[Tuple[int, int], str]]):
    (lines, mapping) = maze

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            curr = (row, col)
            if curr in mapping:
                print(mapping[curr], end="")
            else:
                print(".", end="")

        print("")


def pull(maze: Tuple[List[List[str]], Dict[Tuple[int, int], str]], direction: str, iteration: int = 1) -> int:
    (lines, mapping) = maze
    height = len(lines)
    width = len(lines[0])

    if direction == "N":
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                curr = (row, col)
                if curr in mapping:
                    curr_mapping = mapping[curr]

                    if curr_mapping == "O":
                        if row > 0:
                            del mapping[curr]

                            # Go as far up as possible.
                            new_row = row
                            while new_row > 0:
                                new_row -= 1
                                new_coords = (new_row, col)
                                if new_coords in mapping:
                                    mapping[(new_row + 1, col)] = curr_mapping
                                    break
                                elif new_row == 0:
                                    mapping[new_coords] = curr_mapping
                                    break
    elif direction == "E":
        for row in range(len(lines)):
            for col in reversed(range(len(lines[row]))):
                curr = (row, col)
                if curr in mapping:
                    curr_mapping = mapping[curr]

                    if curr_mapping == "O":
                        if col < width - 1:
                            del mapping[curr]

                            # Go as far right as possible.
                            new_col = col
                            while new_col < (width - 1):
                                new_col += 1
                                new_coords = (row, new_col)
                                if new_coords in mapping:
                                    mapping[(row, new_col - 1)] = curr_mapping
                                    break
                                elif new_col == width - 1:
                                    mapping[new_coords] = curr_mapping
                                    break
    elif direction == "S":
        for row in reversed(range(len(lines))):
            for col in range(len(lines[row])):
                curr = (row, col)
                if curr in mapping:
                    curr_mapping = mapping[curr]

                    if curr_mapping == "O":
                        if row < (height - 1):
                            del mapping[curr]

                            # Go as far up as possible.
                            new_row = row
                            while new_row < (height - 1):
                                new_row += 1
                                new_coords = (new_row, col)
                                if new_coords in mapping:
                                    mapping[(new_row - 1, col)] = curr_mapping
                                    break
                                elif new_row == (height - 1):
                                    mapping[new_coords] = curr_mapping
                                    break
    elif direction == "W":
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                curr = (row, col)
                if curr in mapping:
                    curr_mapping = mapping[curr]

                    if curr_mapping == "O":
                        if col > 0:
                            del mapping[curr]

                            # Go as far left as possible.
                            new_col = col
                            while new_col > 0:
                                new_col -= 1
                                new_coords = (row, new_col)
                                if new_coords in mapping:
                                    mapping[(row, new_col + 1)] = curr_mapping
                                    break
                                elif new_col == 0:
                                    mapping[new_coords] = curr_mapping
                                    break

    ret = 0
    for coord, value in mapping.items():
        if value == "O":
            ret += len(lines) - coord[0]

    return ret


def part_one():
    lines = read_lines_to_list()
    mapping = get_rocks(lines)
    maze = (lines, mapping)

    # print_board(maze)
    # print("================== Part 1 ==================")

    answer = pull(maze, "N")

    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    mapping = get_rocks(lines)
    maze = (lines, mapping)

    # print_board(maze)
    # print("================== Part 2 ==================")

    answer = None

    cycle = ["N", "W", "S", "E"]
    states = []
    answers = []
    for i in range(1000000000):
        curr_answer = 0
        for curr in cycle:
            curr_answer = pull(maze, curr, (i + 1))

        state_hash = hash(frozenset(maze[1].items()))
        if state_hash in states:
            first_index = states.index(state_hash)
            cycle_length = i - first_index

            index = first_index + ((1000000000 - first_index) % cycle_length) - 1
            # print(f"first cycle at {i} with {first_index}, answer should be at index {index}!")
            answer = answers[index]
            break
        else:
            states.append(state_hash)
            answers.append(curr_answer)

    print(f"Part 2: {answer}")


part_one()
part_two()
