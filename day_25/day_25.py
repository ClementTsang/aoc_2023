#!/bin/python3

import sys
from networkx import Graph, connected_components, minimum_edge_cut
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            split = line.split(": ")
            lines.append((split[0], split[1].split(" ")))

    return lines


def part_one():
    lines = read_lines_to_list()
    answer = 1

    graph = Graph()

    for node, connections in lines:
        graph.add_node(node)
        for connection in connections:
            graph.add_node(connection)
            graph.add_edge(
                *((node, connection) if node > connection else (connection, node))
            )

    cut = minimum_edge_cut(graph)
    graph.remove_edges_from(cut)

    components = connected_components(graph)
    for component in components:
        answer *= len(component)

    print(f"Part 1: {answer}")


def part_two():
    print(f"Merry Christmas!")


part_one()
part_two()
