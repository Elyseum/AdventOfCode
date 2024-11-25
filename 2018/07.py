"""Puzzle 07."""

import re
from collections import defaultdict

def read_lines(file_name):
    with open(file_name) as file:
        return file.readlines()

EXAMPLE_INPUT = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin."
]

def parse_dependencies(lines):
    """
    Value is list of steps that have to be completed before key step can begin.
    > dict["E"] = ["B", "D", "F"]
    """
    steps = set()
    dependencies = defaultdict(set)
    for line in lines:
        step, dependency = re.findall(r'([A-Z])\s', line)
        steps.add(step)
        steps.add(dependency)
        dependencies[dependency].update(step)
    return steps, dependencies

def solve_1(lines):
    done = set()
    done_str = ''
    steps, dep = parse_dependencies(lines)
    while len(done) < len(steps):
        next_done = min(x for x in steps if x not in done and dep[x] <= done)
        done.update(next_done)
        done_str += next_done
    print(done_str)

INPUT = read_lines("07.txt")
solve_1(EXAMPLE_INPUT)
solve_1(INPUT)

class Worker:

    def __init__(self, step_duration):
        self.step = None
        self.step_duration = step_duration
        self.remaining = 0
    
    def work(self, step=1):
        if self.remaining is 0:
            return None
        self.remaining -= step
        return self.step if self.remaining is 0 else None

    def working(self):
        return self.remaining > 0

    def idle(self):
        return self.remaining is 0

    def start(self, step):
        self.step = step
        self.remaining = self.step_duration + ord(step) - ord('A') + 1


def solve_2(nr_workers, step_duration, lines):
    workers = [Worker(step_duration) for _ in range(nr_workers)]
    done = set()
    steps_remaining, dep = parse_dependencies(lines)
    total_duration = 0
    while True:
        # Process a unit of work (if any)
        for worker in workers:
            if worker.working():
                completed = worker.work()
                if completed:
                    done.update(completed)
        next_steps = sorted([x for x in steps_remaining if dep[x] <= done], reverse=True)
        if len(next_steps) is 0 and all(x.idle() for x in workers):
            break
        # Schedule work (if any)
        for worker in workers:
            if worker.idle():
                if len(next_steps) is 0:
                    break
                next_step = next_steps.pop()
                worker.start(next_step)
                steps_remaining.remove(next_step)
        total_duration += 1
    print(total_duration)

solve_2(2, 0, EXAMPLE_INPUT)
solve_2(5, 60, INPUT)