import IO
import itertools

class Intcode:

    def __init__(self, instructions, phase = 0):
        self.instructions = {}

        instruction_counter = 0
        for instruction in instructions:
            self.instructions[instruction_counter] = instruction
            instruction_counter += 1

        self.input = [phase]
        self.pointer = 0
        self.finished = False
        self.relative_base = 0

    def is_finished(self):
        return self.finished

    def get_value(self, pointer, param_mode=1):
        input_param = self.instructions.get(pointer, 0)
        if param_mode == 0:     # position mode
            return self.instructions.get(input_param, 0)
        elif param_mode == 1:   # input mode / immediate mode
            return self.instructions.get(pointer, 0)
        else:                   # relative mode
            return self.instructions.get(input_param + self.relative_base, 0)

    def set_value(self, pointer, param_mode, value):
        if param_mode == 0:
            input_param = self.instructions.get(pointer, 0)
            self.instructions[input_param] = value
        elif param_mode == 1:
            raise Exception("Can't set value with param mode 1")
        elif param_mode == 2:
            input_param = self.instructions.get(pointer, 0)
            self.instructions[input_param + self.relative_base] = value
        else:
            raise Exception("Unknown param_mode " + str(param_mode))

    def execute(self, input = []):
        self.input.extend(input)
        output = []
        while True:
            instruction = self.instructions[self.pointer]
            opcode = instruction % 100
            input_1_mode = int(instruction / 100) % 10
            input_2_mode = int(instruction / 1000) % 10
            input_3_mode = int(instruction / 10000) % 10
            # Stop immediately so we don't cross input array boundaries.
            if opcode == 99:
                self.finished = True
                return output
            if opcode == 1:
                input_1 = self.get_value(self.pointer + 1, input_1_mode)
                input_2 = self.get_value(self.pointer + 2, input_2_mode)
                self.set_value(self.pointer + 3, input_3_mode, input_1 + input_2)
                self.pointer += 4
            elif opcode == 2:
                input_1 = self.get_value(self.pointer + 1, input_1_mode)
                input_2 = self.get_value(self.pointer + 2, input_2_mode)
                self.set_value(self.pointer + 3, input_3_mode, input_1 * input_2)
                self.pointer += 4
            elif opcode == 3:
                # Can't consume because we need more input.Return the output 
                # we have so far, so next amplifier can continue. We will 
                # eventually get input from through a feedback loop.
                if len(self.input) == 0:
                    return output
                self.set_value(self.pointer + 1, input_1_mode, self.input.pop(0))
                self.pointer += 2
            elif opcode == 4:
                input_1 = self.get_value(self.pointer + 1, input_1_mode)
                output.append(input_1)
                self.pointer += 2
            elif opcode == 5:
                if self.get_value(self.pointer + 1, input_1_mode) != 0:
                    self.pointer = self.get_value(self.pointer + 2, input_2_mode)
                else:
                    self.pointer += 3
            elif opcode == 6:
                if self.get_value(self.pointer + 1, input_1_mode) == 0:
                    self.pointer = self.get_value(self.pointer + 2, input_2_mode)
                else:
                    self.pointer += 3
            elif opcode == 7:
                input_1 = self.get_value(self.pointer + 1, input_1_mode)
                input_2 = self.get_value(self.pointer + 2, input_2_mode)
                if input_1 < input_2:
                    self.set_value(self.pointer + 3, input_3_mode, 1)
                else:
                    self.set_value(self.pointer + 3, input_3_mode, 0)
                self.pointer += 4
            elif opcode == 8:
                input_1 = self.get_value(self.pointer + 1, input_1_mode)
                input_2 = self.get_value(self.pointer + 2, input_2_mode)
                if input_1 == input_2:
                    self.set_value(self.pointer + 3, input_3_mode, 1)
                else:
                    self.set_value(self.pointer + 3, input_3_mode, 0)
                self.pointer += 4
            elif opcode == 9:
                self.relative_base += self.get_value(self.pointer + 1, input_1_mode)
                self.pointer += 2
            else:
                raise Exception(f"Unknown opcode {opcode} (instruction {instruction})")
        raise Exception("Failed to complete")

def execute_int_code(instructions, phase = 0):
    return Intcode(instructions.copy(), phase).execute()

def execute_int_code_seq(instructions, amplifier_phases):
    amplifiers = list(map(lambda x: Intcode(instructions.copy(), x), amplifier_phases))

    prev_amplifier_output = [0] # First input signal is always 0.
    while not all(map(lambda x: x.is_finished(), amplifiers)):
        for amplifier in amplifiers:
            prev_amplifier_output = amplifier.execute(prev_amplifier_output)
    return prev_amplifier_output[0]

instructions = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
print("Result " + str(execute_int_code_seq(instructions, [4,3,2,1,0])))
print("Result " + str(execute_int_code_seq(instructions, [4,0,1,2,3])))

instructions = [
    3,23,3,24,1002,24,10,24,1002,23,-1,23,
    101,5,23,23,1,24,23,23,4,23,99,0,0
]
print("Result " + str(execute_int_code_seq(instructions, [0,1,2,3,4])))

def max_int_code_seq(instructions, amplifier_sequence):
    max_input = None
    max_value = -1
    for p in itertools.permutations(amplifier_sequence):
        result = execute_int_code_seq(instructions, p)
        if result > max_value:
            max_input = p
            max_value = result
    return (max_input, max_value)

# Expected result: 43821
instructions = IO.read_line_list('07.txt', transform=int)
print(f"Part 1: {str(max_int_code_seq(instructions, [0, 1, 2, 3, 4]))}")

# Expected result: 59597414
instructions = IO.read_line_list('07.txt', transform=int)
print(f"Part 2: {str(max_int_code_seq(instructions, [9, 8, 7, 6, 5]))}")

# 109,1,204,... takes no input and produces a copy of itself as output.
instructions = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
assert(instructions == execute_int_code(instructions))

# 1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
instructions = [1102,34915192,34915192,7,4,7,99,0]
assert(16 == len(str(execute_int_code(instructions)[0])))

instructions = [104,1125899906842624,99]
assert([1125899906842624] == execute_int_code(instructions))

instructions = IO.read_line_list('09.txt', transform=int)
print("Part 1")
print(f"Part 1: {str(execute_int_code(instructions, phase = 1))}")

print("Part 2")
print(f"Part 2: {str(execute_int_code(instructions, phase = 2))}")
