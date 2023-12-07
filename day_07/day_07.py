#!/bin/python3

from collections import Counter
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


def hand_rank_one(hand: Counter) -> int:
    if len(hand) == 1:
        return 7
    if len(hand) == 5:
        return 1
    else:
        most_common = hand.most_common()
        if most_common[0][1] == 4:
            return 6
        elif most_common[0][1] == 3:
            if most_common[1][1] == 2:
                return 5
            else:
                return 4
        elif most_common[0][1] == 2:
            if most_common[1][1] == 2:
                return 3
            else:
                return 2


def hand_rank_two(hand: Counter) -> int:
    num_jokers = hand["J"]

    if hand["J"] < 5:
        del hand["J"]
        most_frequent_card = hand.most_common()[0][0]
        hand[most_frequent_card] += num_jokers

    if len(hand) == 1:
        return 7
    elif len(hand) == 5:
        return 1
    else:
        most_common = hand.most_common()
        if most_common[0][1] == 4:
            return 6
        elif most_common[0][1] == 3:
            if most_common[1][1] == 2:
                return 5
            else:
                return 4
        elif most_common[0][1] == 2:
            if most_common[1][1] == 2:
                return 3
            else:
                return 2


def card_val(a: Tuple[int, List[str], int]) -> int:
    RANKING = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    sorting = (a[0], *[RANKING.index(val) for val in a[1]], a[2])
    return sorting


def part_one():
    lines = read_lines_to_list()
    total = 0
    hands = []

    for line in lines:
        split = line.split()

        hand = list(split[0])
        hand_counter = Counter(hand)
        bid = int(split[1])

        hands.append((hand_rank_one(hand_counter), hand, bid))

    hands.sort(key=card_val, reverse=True)

    curr_rank = 1
    while hands:
        curr = hands.pop()
        score = curr_rank * curr[2]
        # print(f"{curr[1]} has a value of {curr[0]}, giving a score of {curr[2]} * {curr_rank} = {score}")
        total += score
        curr_rank += 1

    print(f"Part 1: {total}")


def part_two():
    lines = read_lines_to_list()
    total = 0
    hands = []

    for line in lines:
        split = line.split()

        hand = list(split[0])
        hand_counter = Counter(hand)
        bid = int(split[1])
        rank = hand_rank_two(hand_counter)

        hands.append((rank, hand, bid))

    hands.sort(key=card_val, reverse=True)

    curr_rank = 1
    while hands:
        curr = hands.pop()
        score = curr_rank * curr[2]
        # print(f"{curr[1]} has a value of {curr[0]}, giving a score of {curr[2]} * {curr_rank} = {score}")
        total += score
        curr_rank += 1

    print(f"Part 2: {total}")


part_one()
part_two()
