import util

"""
Maps a list of chunks to the sum of each chunk
For example,
[[1, 2, 3], [5], [6, 7]]
becomes
[6, 5, 13]
"""
def parse_input(data_path):
    lines = util.read_lines(data_path)
    chunks = util.chunk(lambda x: len(x.strip()) == 0, lines)
    return map(lambda c: sum(map(int, c)), chunks)

def sum_top(take, lst):
    return sum(sorted(lst, reverse=True)[0:take])

def solve_1(part, data_path):
    util.solve(part, data_path, parse_input, lambda x: sum_top(1, x))

def solve_2(part, data_path):
    util.solve(part, data_path, parse_input, lambda x: sum_top(3, x))

solve_1("Part 1", 'data/01_example.txt')
solve_1("Part 1", 'data/01_input.txt')

solve_2("Part 2", 'data/01_example.txt')
solve_2("Part 2", 'data/01_input.txt')

