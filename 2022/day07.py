import util
from collections import defaultdict

ROOT = '/'
UP = '..'

def parse(path):
    current_path = []
    for line in util.read_lines(path):
        if line.startswith('$ cd '):
            path_directive = line[len('$ cd '):]
            if path_directive == ROOT:
                current_path = ['']
            elif path_directive == UP:
                current_path = current_path[0:-1]
            else:
                current_path.append(path_directive)
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir '):
            continue
        else:
            size_str, file_name = line.split(' ')
            yield (list(current_path), file_name, int(size_str))

def calc_dir_sizes(dir_files):
    sizes = defaultdict(int)
    for dir_parts, _, size in dir_files:
        dir_path = ''
        for part in dir_parts:
            dir_path += part + '/'
            sizes[dir_path] = sizes[dir_path] + size
    return (sizes[dir_path] for dir_path in sizes)

def sum_dir_total_size(dir_files):
    return sum(x for x in calc_dir_sizes(dir_files) if x <= 100000)

def delete_smallest_dir(dir_files):
    dir_sizes = sorted(calc_dir_sizes(dir_files))
    free_size = 70000000 - dir_sizes[-1] # Size of '/'
    return next(x for x in dir_sizes if free_size + x >= 30000000)

def solve_1(part, path):
    util.solve(part, path, parse, sum_dir_total_size)

def solve_2(part, data):
    util.solve(part, data, parse, delete_smallest_dir)

solve_1("Part 1", 'data/07_example.txt')
solve_1("Part 1", 'data/07_input.txt')

solve_2("Part 2", 'data/07_example.txt')
solve_2("Part 2", 'data/07_input.txt')

