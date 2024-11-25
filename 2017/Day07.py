"""Day07"""

import re

import Helpers

class Program():
    """Program and its subprograms"""

    def __init__(self, name, weight):
        # Simple properties
        self.name = name
        self.weight = weight
        # Reference properties. Will be added after creation.
        self.parent = None
        self.subprograms = []
        # Calculated properties. Filled in on first calculation
        self.total_weight = None

    def get_total_weight(self):
        """Weight + subprogram weights"""
        if not self.total_weight:
            sub_total_weight = sum(map(lambda x: x.get_total_weight(), self.subprograms))
            self.total_weight = self.weight + sub_total_weight
        return self.total_weight

    def subprograms_grouped_by_weight(self):
        """Dict with different weights linked to subprograms"""
        total_weights = {} #<weight, subprograms[]>
        for subprogram in self.subprograms:
            total_weight = subprogram.get_total_weight()
            group = total_weights.get(total_weight, [])
            group.append(subprogram)
            total_weights[total_weight] = group
        return total_weights

    def subtree_with_wrong_weight(self):
        """Find the subtree with the wrong weight"""
        total_weights = self.subprograms_grouped_by_weight()
        if not total_weights or len(total_weights) == 1:
            return None

        # if we have multiple groups, we have a group with wrong weight
        # and a group with the right weight.
        # Assignment assumption: only one item has a wrong weight
        groups = total_weights.items()
        wrong_total_w_group = next((x for x in groups if len(x[1]) == 1))
        wrong_total_w = wrong_total_w_group[0]
        wrong_program = wrong_total_w_group[1][0]
        right_total_w_group = next((x for x in groups if len(x[1]) > 1))
        right_total_w = right_total_w_group[0]

        return (wrong_program, wrong_total_w, right_total_w)

    def subprogram_with_wrong_weight(self):
        """Keep iterating subtree with wrong weight until we find bad program"""
        subtree = None
        next_subtree = self.subtree_with_wrong_weight()
        while next_subtree:
            subtree = next_subtree
            next_subtree = next_subtree[0].subtree_with_wrong_weight()

        wrong_program, wrong_total_w, right_total_w = subtree

        if right_total_w < wrong_total_w: # Weight is too high
            right_w = wrong_program.weight - abs(wrong_total_w - right_total_w)
        else: # Weight is too low
            right_w = wrong_program.weight + abs(wrong_total_w - right_total_w)

        return wrong_program, right_w

def parse_program(line):
    """
    Possible lines are:
    * "uylvg (403) -> xrvcjq, hihltxf"
    * "uylvg (403) -> xrvcjq"
    * "uylvg (403)"
    """
    parts = re.findall(r'\w+', line)
    return (Program(parts[0], int(parts[1])), parts[2:])

def parse_programs(lines):
    """List of programs linked to its children and parent"""
    programs = {} # <name, program>
    program_subprograms = {} # <name, subprogam_names[]>

    # create all the program objects
    for line in lines:
        program, subprogram_names = parse_program(line)
        programs[program.name] = program
        program_subprograms[program.name] = subprogram_names

    # link all the program objects: parent - child relations
    for name, subprogram_names in program_subprograms.items():
        program = programs[name]
        for subprogram_name in subprogram_names:
            subprogram = programs[subprogram_name]
            program.subprograms.append(subprogram)
            subprogram.parent = program

    return list(programs.values())

def parse_program_tree(file):
    """Parses all programs into a tree structure and returns the root"""
    lines = Helpers.read_lines(file)
    programs = parse_programs(lines)
    return next((x for x in programs if not x.parent), None)

ROOT = parse_program_tree("Day07.txt")
print("Root program: '" + ROOT.name + "'")

# 'jriph' should have weight 1993
WRONG = ROOT.subprogram_with_wrong_weight()
print("Wrong subprogram: '" + WRONG[0].name + "'. " +
      "Weight '" +  str(WRONG[0].weight) + "' should be '" + str(WRONG[1]) + "'")
