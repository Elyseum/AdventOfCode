import util

def parse_input(data_path):
    return list(util.read_lines(data_path, int))

def count_increases(window_size, depths):
    window_current = depths[0:window_size]
    count = 0
    for depth in depths[window_size:]:
        window_next = window_current[1:] + [depth]
        if sum(window_current) < sum(window_next):
            count += 1
        window_current = window_next
    return count

def solve_1(part, data_path):
    solve(part, data_path, parse_input, lambda x: count_increases(1, x))

def solve_2(part, data_path):
    solve(part, data_path, parse_input, lambda x: count_increases(3, x))
    
solve_1("Part 1", 'data/01_example.txt')
solve_1("Part 1", 'data/01_input.txt')

solve_2("Part 2", 'data/01_example.txt')
solve_2("Part 2", 'data/01_input.txt')
