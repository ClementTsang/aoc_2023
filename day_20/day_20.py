#!/bin/python3

import sys
import math
from typing import List, Tuple

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            split = line.split(" -> ")

            name = split[0]
            flip_flop = name.startswith("%")
            conjunction = name.startswith("&")
            target = split[1].split(", ")

            if flip_flop:
                state = False
                name = split[0][1:]
            elif conjunction:
                state = {}
                name = split[0][1:]
            else:
                state = None

            val = (name, [target, flip_flop, conjunction, state])

            lines.append(val)

    return lines


def part_one():
    lines = read_lines_to_list()
    mappings = dict((a, b) for (a, b) in lines)

    # For any conjunction modules we must initialize inputs...
    for k, v in mappings.items():
        if v[2]:
            for a, b in mappings.items():
                if k in b[0]:
                    v[3][a] = False

    low = 0
    high = 0
    for _ in range(1000):
        queue = [("broadcaster", 0, None)]
        while queue:
            (curr, signal, input) = queue.pop(0)

            if signal:
                high += 1
            else:
                low += 1

            if curr not in mappings:
                continue

            [targets, is_ff, is_con, state] = mappings[curr]

            if is_ff:
                if not signal:
                    if state:
                        mappings[curr][3] = False
                        new_signal = 0
                    else:
                        mappings[curr][3] = True
                        new_signal = 1

                    for target in targets:
                        queue.append((target, new_signal, curr))
            elif is_con:
                state[input] = bool(signal)
                if all(state.values()):
                    new_signal = 0
                else:
                    new_signal = 1
                for target in targets:
                    queue.append((target, new_signal, curr))
            else:
                for target in targets:
                    queue.append((target, signal, curr))

    answer = low * high
    print(f"Part 1: {answer}")


def part_two():
    lines = read_lines_to_list()
    mappings = dict((a, b) for (a, b) in lines)

    for k, v in mappings.items():
        if v[2]:
            for a, b in mappings.items():
                if k in b[0]:
                    v[3][a] = False

    # A little bit of hardcoded trickery for my input... I specifically needed xr, fv, kk, and vt to all be low.
    lowest_parents = {
        "xr": None,
        "fv": None,
        "kk": None,
        "vt": None,
    }

    curr_cycle = 0
    answer = 0
    while True:
        if all(val is not None for val in lowest_parents.values()):
            answer = math.lcm(*list(lowest_parents.values()))
            break

        curr_cycle += 1
        queue = [("broadcaster", 0, None)]
        while queue:
            (curr, signal, input) = queue.pop(0)

            if curr in lowest_parents and not signal:
                lowest_parents[curr] = curr_cycle

            # Ideally this happens but it won't.
            if curr == "rx" and not signal:
                break

            if curr not in mappings:
                continue

            [targets, is_ff, is_con, state] = mappings[curr]

            if is_ff:
                if not signal:
                    if state:
                        mappings[curr][3] = False
                        new_signal = 0
                    else:
                        mappings[curr][3] = True
                        new_signal = 1

                    for target in targets:
                        queue.append((target, new_signal, curr))
            elif is_con:
                state[input] = bool(signal)
                if all(state.values()):
                    new_signal = 0
                else:
                    new_signal = 1
                for target in targets:
                    queue.append((target, new_signal, curr))
            else:
                for target in targets:
                    queue.append((target, signal, curr))

    print(f"Part 2: {answer}")


part_one()
part_two()
