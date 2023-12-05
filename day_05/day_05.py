#!/bin/python3

import sys
from typing import List, Tuple

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def read_map(lines: List[str]) -> List[Tuple[range, int]]:
    mapping = []

    if len(lines) == 0:
        return mapping
    lines.pop(0)

    while len(lines) > 0 and len(lines[0]) > 0:
        line = lines.pop(0)
        [dest, init, length] = [int(val) for val in line.split()]
        mapping.append((range(init, init + length), dest))

    if len(lines) > 0:
        lines.pop(0)

    return mapping


def find(val: int, mapping: List[Tuple[range, int]]) -> int:
    for range, end in mapping:
        if val in range:
            return val - range.start + end
    else:
        return val


def part_1():
    lines = read_lines_to_list()

    seeds_line = lines.pop(0).split("seeds: ")[1]
    seeds = [int(val) for val in seeds_line.split()]

    lines.pop(0)

    mappings = []
    for _ in range(7):
        mappings.append(read_map(lines))

    smallest = sys.maxsize
    for curr in seeds:
        for map in mappings:
            curr = find(curr, map)
        smallest = min(smallest, curr)

    print(f"Part 1: {smallest}")


def part_2():
    lines = read_lines_to_list()

    seeds_line = lines.pop(0).split("seeds: ")[1]
    seeds: List[range] = []
    part_two_itx = 0
    part_two_seeds_line = seeds_line.split()
    while part_two_itx < len(part_two_seeds_line):
        start = int(part_two_seeds_line[part_two_itx])
        length = int(part_two_seeds_line[part_two_itx + 1])
        seeds.append(range(start, start + length))
        part_two_itx += 2

    lines.pop(0)

    mappings: List[List[Tuple[range, int]]] = []
    for _ in range(7):
        mappings.append(read_map(lines))

    smallest = sys.maxsize
    for seed_range in seeds:
        ranges = [seed_range]
        for mapping in mappings:
            # TL;DR: split up ranges where intersections exist.

            new_ranges = []
            while ranges:
                current_range = ranges.pop()
                for map_range, new_start in mapping:
                    new_range_start = max(map_range.start, current_range.start)
                    new_range_stop = min(map_range.stop, current_range.stop)

                    if range(new_range_start, new_range_stop):
                        offset = new_start - map_range.start
                        new_range = range(new_range_start + offset, new_range_stop + offset)
                        new_ranges.append(new_range)

                        if new_range_start > current_range.start:
                            ranges.append(range(current_range.start, new_range_start))

                        if new_range_stop < current_range.stop:
                            ranges.append(range(new_range_stop, current_range.stop))

                        break
                else:
                    new_ranges.append(current_range)
            ranges = new_ranges

        smallest = min(smallest, min([r.start for r in ranges]))

    print(f"Part 2: {smallest}")


part_1()
part_2()
