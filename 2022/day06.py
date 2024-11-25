import util

def parse(path):
    return list(util.read_lines(path, list))[0]

def find_first_distinct(lst, size=4):
    # Start with a window with a fake value and `size-1` real values.
    # Because the loop moves forward 1 element the first loop will start with
    # the first `size` real values.
    window = [-1] + lst[0:size-1]
    index_last = size-2
    for el in lst[size-1:]:
        index_last += 1
        window = window[1:] + [el]
        if (len(set(window)) == size):
            return index_last + 1
    return -1

def solve_1(part, path):
    util.solve(part, path, parse, lambda x: find_first_distinct(x))

def solve_2(part, data):
    util.solve(part, data, parse, lambda x: find_first_distinct(x, 14))

solve_1("Part 1.0", 'data/06_example_0.txt')
solve_1("Part 1.1", 'data/06_example_1.txt')
solve_1("Part 1.2", 'data/06_example_2.txt')
solve_1("Part 1.3", 'data/06_example_3.txt')
solve_1("Part 1.4", 'data/06_example_4.txt')
solve_1("Part 1"  , 'data/06_input.txt')

solve_2("Part 1.0", 'data/06_example_0.txt')
solve_2("Part 2.1", 'data/06_example_1.txt')
solve_2("Part 2.2", 'data/06_example_2.txt')
solve_2("Part 2.3", 'data/06_example_3.txt')
solve_2("Part 2.4", 'data/06_example_4.txt')
solve_2("Part 2"  , 'data/06_input.txt')

