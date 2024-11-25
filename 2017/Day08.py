"""Day08"""

import Helpers

class Registry:
    """Simulate conditional registry operations"""

    def __init__(self):
        self.values = {}

    def conditional_execute(self, cond_inst):
        """Execute instruction if condition evaluates to True"""
        parts = cond_inst.strip().split(" if ") # b inc 5 if a > 1
        inst = parts[0] # b inc 5
        cond = parts[1] # a > 1

        if self.condition(cond):
            self.execute(inst)

    def condition(self, cond):
        """Evaluates condition string and returns its result"""
        parts = cond.split(' ') # a <= 3

        variable = self.values.get(parts[0], 0) # 'a'
        operator = parts[1] # '<='
        value = int(parts[2]) # 3

        if operator == '<':
            return variable < value
        elif operator == '<=':
            return variable <= value
        elif operator == '==':
            return variable == value
        elif operator == '>':
            return variable > value
        elif operator == '>=':
            return variable >= value
        elif operator == '!=':
            return variable != value
        else:
            raise NotImplementedError("Operator '" + operator + "'")

    def execute(self, inst):
        """Parse and execute instruction"""
        print("Executing '" + inst + "'")

        parts = inst.split(' ') # 'a inc 10'
        variable = self.values.get(parts[0], 0) # 'a'
        operator = parts[1] # 'inc'
        value = int(parts[2]) # '10'

        if operator == 'inc':
            variable += value
        elif operator == 'dec':
            variable -= value
        else:
            raise NotImplementedError("Operator '" + operator + "'")

        self.values[parts[0]] = variable

    def max_value(self):
        """Returns the max value in the registry"""
        return max(self.values.values())

REGISTRY = Registry()

for line in Helpers.read_lines("Day08.txt"):
    REGISTRY.conditional_execute(line)

print("Max value is '" + str(REGISTRY.max_value()) + "'")
