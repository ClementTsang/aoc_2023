#!/bin/python3

from enum import Enum
import sys
from typing import List, Set, Tuple

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
sys.setrecursionlimit(100000)


def read_lines_to_list() -> List[List[str]]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


Direction = Enum("Direction", "North East South West")


def valid_position(y: int, x: int, maze: List[List[str]]) -> bool:
    return y >= 0 and x >= 0 and y < len(maze) and x < len(maze[0])


def step_forward(y: int, x: int, direction: Direction):
    match direction:
        case Direction.North:
            y -= 1
        case Direction.East:
            x += 1
        case Direction.South:
            y += 1
        case Direction.West:
            x -= 1

    return (y, x)


def mirror(y: int, x: int, direction: Direction, maze: List[List[str]]) -> Direction:
    if maze[y][x] == "\\":
        match direction:
            case Direction.North:
                return Direction.West
            case Direction.East:
                return Direction.South
            case Direction.South:
                return Direction.East
            case Direction.West:
                return Direction.North
    elif maze[y][x] == "/":
        match direction:
            case Direction.North:
                return Direction.East
            case Direction.East:
                return Direction.North
            case Direction.South:
                return Direction.West
            case Direction.West:
                return Direction.South
    else:
        print("Something went wrong!")


def energy(maze: List[List[str]], start=None) -> int:
    queue = [(0, 0, Direction.East)] if start is None else [start]
    seen: Set[Tuple[int, int, Direction]] = set()
    seen.add(queue[0])

    while queue:
        (y, x, direction) = queue.pop(0)
        curr = maze[y][x]
        if curr == ".":
            next_step = step_forward(y, x, direction)
            if valid_position(*next_step, maze):
                to_add = (next_step[0], next_step[1], direction)
                if to_add not in seen:
                    seen.add(to_add)
                    queue.append(to_add)
        elif curr == "/" or curr == "\\":
            new_direction = mirror(y, x, direction, maze)

            next_step = step_forward(y, x, new_direction)
            to_add = (*next_step, new_direction)
            if valid_position(*next_step, maze) and to_add not in seen:
                seen.add(to_add)
                queue.append(to_add)
        elif curr == "|":
            if direction == Direction.North or direction == Direction.South:
                next_step = step_forward(y, x, direction)
                if valid_position(*next_step, maze):
                    to_add = (next_step[0], next_step[1], direction)
                    if to_add not in seen:
                        seen.add(to_add)
                        queue.append(to_add)
            else:
                if valid_position(y - 1, x, maze):
                    to_add = (y - 1, x, Direction.North)
                    if to_add not in seen:
                        seen.add(to_add)
                        queue.append(to_add)

                if valid_position(y + 1, x, maze):
                    to_add = (y + 1, x, Direction.South)
                    if to_add not in seen:
                        seen.add(to_add)
                        queue.append(to_add)
        elif curr == "-":
            if direction == Direction.East or direction == Direction.West:
                next_step = step_forward(y, x, direction)
                if valid_position(*next_step, maze):
                    to_add = (next_step[0], next_step[1], direction)
                    if to_add not in seen:
                        seen.add(to_add)
                        queue.append(to_add)
            else:
                if valid_position(y, x - 1, maze):
                    to_add = (y, x - 1, Direction.West)
                    if to_add not in seen:
                        seen.add(to_add)
                        queue.append(to_add)

                if valid_position(y, x + 1, maze):
                    to_add = (y, x + 1, Direction.East)
                    if to_add not in seen:
                        seen.add(to_add)
                        queue.append(to_add)
        else:
            print(f"hit a missing case: {curr}")

    energized = set([(a, b) for (a, b, _) in seen])

    return len(energized)


def part_one():
    maze = read_lines_to_list()
    answer = energy(maze)

    print(f"Part 1: {answer}")


def part_two():
    maze = read_lines_to_list()
    height = len(maze)
    width = len(maze[0])
    answer = 0

    for direction in [Direction.North, Direction.East, Direction.South, Direction.West]:
        match direction:
            case Direction.North:
                for col in range(width):
                    answer = max(answer, energy(maze, (height - 1, col, direction)))
            case Direction.East:
                for row in range(height):
                    answer = max(answer, energy(maze, (row, 0, direction)))
            case Direction.South:
                for col in range(width):
                    answer = max(answer, energy(maze, (0, col, direction)))
            case Direction.West:
                for row in range(height):
                    answer = max(answer, energy(maze, (row, width - 1, direction)))

    print(f"Part 1: {answer}")


part_one()
part_two()
