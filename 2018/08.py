"""Day 08."""

import time

EXAMPLE_INPUT = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def parse_metadata(elements):
    # First two definition elements are known values
    nr_children, nr_metadata = next(elements), next(elements)
    # Next definition elements belong to the children
    children = [parse_metadata(elements) for _ in range(nr_children)]
    # When children are parsed we can start reading metadata
    metadata = [next(elements) for _ in range(nr_metadata)]
    return (metadata, children)

def sum_metadata(node):
    metadata, children = node
    return sum(metadata) + sum(map(sum_metadata, children))

def solve1(input):
    root_node = parse_metadata(iter(input))
    print(sum_metadata(root_node))

solve1(EXAMPLE_INPUT)

def read_input(file_name):
    with open(file_name) as file:
        return map(int, file.readline().split(' '))

solve1(read_input("08.txt"))

def value(node):
    meta, children = node
    if len(children) is 0:
        return sum(meta)
    meta_children = (children[x - 1] for x in meta if x - 1 < len(children))
    return sum(map(value, meta_children))

def solve2(input):
    start = time.time()
    root_node = parse_metadata(iter(input))
    root_node_value = value(root_node)
    elapsed = time.time() - start
    print(f"Puzzle 8 (part 2): {root_node_value} (duration {elapsed}s)")

solve2(EXAMPLE_INPUT)
solve2(read_input("08.txt"))
