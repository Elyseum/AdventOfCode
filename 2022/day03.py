import util

"""
1234
567890
will give
[
  [[1, 2], [3, 4]]
  [[5, 6, 7], [8, 9, 0]]
]
"""
def parse_input(data_path):
    lines = util.read_lines(data_path)
    for line in lines:
        middle = len(line) // 2
        yield [line[:middle], line[middle:], line]

def priority(item):
    if ord(item) >= ord('a'):
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 1 + 26

def rucksack_priority(rucksack):
    overlap = set(rucksack[0]).intersection(set(rucksack[1]))
    return sum(map(priority, overlap))

def solve_1(part, data_path):
    solver = lambda x: sum(map(rucksack_priority, x))
    util.solve(part, data_path, parse_input, solver)

def rucksack_group_priority(rucksacks):
    l1 = rucksacks[0][2]
    l2 = rucksacks[1][2]
    l3 = rucksacks[2][2]
    overlap = set(l1).intersection(set(l2)).intersection(set(l3))
    return sum(map(priority, overlap))

def solve_2(part, data_path):
    solver = lambda x: sum(map(rucksack_group_priority, util.chunk_size(3, x)))
    util.solve(part, data_path, parse_input, solver)

solve_1("Part 1", 'data/03_example.txt')
solve_1("Part 1", 'data/03_input.txt')

solve_2("Part 2", 'data/03_example.txt')
solve_2("Part 2", 'data/03_input.txt')

