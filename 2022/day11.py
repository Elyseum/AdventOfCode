import math
import util

class Monkey:

    def __init__(self, items, operation, divider, m_true, m_false):
        self.inspected = 0
        self.items = items
        self.operation = operation
        self.divider = divider
        self.m_true = m_true
        self.m_false = m_false

    def inspect(self, worry_reduce, worry_leveler):
        for i, item in enumerate(list(self.items)):
            self.inspected += 1
            worry_level = self.operation(item) // worry_reduce
            test = worry_level % self.divider == 0
            m_next = self.m_true if test else self.m_false
            if worry_leveler:
                worry_level = worry_level % worry_leveler
            yield worry_level, m_next
        self.items = []

    def throw(self, item):
        self.items.append(item)


def parse_operation(operation_str):
    parts = operation_str.split('= ')[1].split(' ')
    if parts[1] == '+':
        if parts[2] == 'old':
            return lambda x: x + x
        else:
            return lambda x: x + int(parts[2])
    else:
        if parts[2] == 'old':
            return lambda x: x * x
        else:
            return lambda x: x * int(parts[2])

def parse(path):
    for monkey in map(lambda x: x.split('\n'), util.read_parts(path)):
        items = list(map(int, monkey[1].split(': ')[1].split(', ')))
        operation = parse_operation(monkey[2])
        divider = int(monkey[3].split(' ')[-1])
        monkey_true = int(monkey[4].split(' ')[-1])
        monkey_false = int(monkey[5].split(' ')[-1])
        yield Monkey(items, operation, divider, monkey_true, monkey_false)

def run_1(monkeys, times, worry_reduce):
    # Each monkey checks if (growing) numbers are divisbile by its own divider.
    # To keep the numbers small we can replace them by the remainder after dividing
    # the multiplication of all these numbers.
    monkey_dividers = (monkey.divider for monkey in monkeys)
    worry_leveler = math.prod(monkey_dividers) * worry_reduce
    for round in range(times):
        for i, monkey in enumerate(monkeys):
            for throw, to in monkey.inspect(worry_reduce, worry_leveler):
                monkeys[to].throw(throw)
    print('After ' + str(round + 1) + ' rounds:')
    for i, monkey in enumerate(monkeys):
        print('Monkey ' + str(i) + ' inspected ' + str(monkey.inspected))
    top_inspected = sorted(map(lambda x: x.inspected, monkeys), reverse=True)
    return top_inspected[0] * top_inspected[1]

def solve_1(part, path):
    util.solve(part, path, parse, lambda x: run_1(list(x), 20, 3))

def solve_2(part, data):
    util.solve(part, data, parse, lambda x: run_1(list(x), 10000, 1))

solve_1("Part 1", 'data/11_example.txt')
solve_1("Part 1", 'data/11_input.txt')

solve_2("Part 2", 'data/11_example.txt')
solve_2("Part 2", 'data/11_input.txt')

