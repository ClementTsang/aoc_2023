#!/bin/python3

import sys
from typing import List, Tuple
import numpy as np

sys.setrecursionlimit(100000)
FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(
                tuple(tuple([int(a) for a in s.split(", ")]) for s in line.split(" @ "))
            )

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 0

    TEST_AREA = (7, 27) if FILE != "input.txt" else (200000000000000, 400000000000000)

    for itx in range(len(lines)):
        for jtx in range(itx + 1, len(lines)):
            a = lines[itx]
            b = lines[jtx]

            (apx, apy, _), (avx, avy, _) = a
            (bpx, bpy, _), (bvx, bvy, _) = b

            try:
                y = (bpx - (bvx / bvy * bpy) + (avx / avy * apy) - apx) / (
                    avx / avy - bvx / bvy
                )
                x = ((y - apy) / avy) * avx + apx

                if (
                    TEST_AREA[0] <= x <= TEST_AREA[1]
                    and TEST_AREA[0] <= y <= TEST_AREA[1]
                ):
                    if (
                        np.sign(x - apx) == np.sign(avx)
                        and np.sign(y - apy) == np.sign(avy)
                        and np.sign(x - bpx) == np.sign(bvx)
                        and np.sign(y - bpy) == np.sign(bvy)
                    ):
                        answer += 1

            except:
                pass

    print(f"Part 1: {answer}")


def part_two():
    # Who needs to think when you can z3
    import z3

    lines = read_lines_to_list()
    answer = 0

    solver = z3.Solver()
    x, y, z, vx, vy, vz = [
        z3.BitVec(var, 64) for var in ["x", "y", "z", "vx", "vy", "vz"]
    ]

    # 4 unknowns, so we just need 4 equations... I think.
    for itx in range(4):
        (cpx, cpy, cpz), (cvx, cvy, cvz) = lines[itx]

        t = z3.BitVec(f"t{itx}", 64)
        solver.add(t >= 0)
        solver.add(x + vx * t == cpx + cvx * t)
        solver.add(y + vy * t == cpy + cvy * t)
        solver.add(z + vz * t == cpz + cvz * t)

    if solver.check() == z3.sat:
        model = solver.model()
        (x, y, z) = (model.eval(x), model.eval(y), model.eval(z))
        answer = x.as_long() + y.as_long() + z.as_long()
    print(f"Part 2: {answer}")


part_one()
part_two()
