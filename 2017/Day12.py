"""Day12"""

import Helpers

class Program:

    def __init__(self, program_id):
        self.program_id = program_id
        self.programs = []

    def link_programs(self, programs):
        self.programs = programs

    def __str__(self):
        return "ID=" + self.program_id

def parse_programs(file_name):
    """Parses programs from file and returns them as a list"""
    programs = {}
    program_links = {}

    for line in Helpers.read_lines(file_name):
        parts = line.split(' <-> ')

        program_id = parts[0]
        program = Program(program_id)
        programs[program_id] = program

        program_links[program_id] = parts[1].split(', ')

    for program_id, program in programs.items():
        linked_program_ids = program_links.get(program_id, [])
        linked_programs = list(map(lambda x: programs[x], linked_program_ids))
        program.link_programs(linked_programs)

    return programs

def programs_that_communicate_with(root):
    return programs_that_communicate_with_rec({}, root)

def programs_that_communicate_with_rec(visited, root):
    result = []
    root_id = root.program_id
    if not visited.get(root_id, False):
        result.append(root)
        visited[root_id] = True
        for program in root.programs:
            result += programs_that_communicate_with_rec(visited, program)
    return result

PROGRAMS = parse_programs('Day12.txt')
ROOT = PROGRAMS["0"]
COMMUNICATES_WITH_ROOT = programs_that_communicate_with(ROOT)
print(str(len(COMMUNICATES_WITH_ROOT)) + " programs that communicate with root")

# Part 2

def count_groups(programs):
    global_registry = {} # share registry
    group_count = 0
    first_unregistered = programs[0]
    while first_unregistered: # continue until all are visited
        programs_that_communicate_with_rec(global_registry, first_unregistered)
        not_registered = (x for x in programs if not global_registry.get(x.program_id, False))
        first_unregistered = next(not_registered, None)
        group_count += 1
    return group_count

GROUPS = count_groups(list(PROGRAMS.values()))
print("Total unconnected groups: " + str(GROUPS))
