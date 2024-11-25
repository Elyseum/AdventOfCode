import IO
import itertools

class Intcode:

    def __init__(self, instructions, phase):
        self.instructions = instructions
        self.input = [phase]
        self.pointer = 0
        self.finished = False

    def is_finished(self):
        return self.finished

    def get_instr_val(self, pointer, param_mode=1):
        input_param = self.instructions[pointer]
        if param_mode is 0: # pointer mode
            return self.instructions[input_param]
        else:               # input mode
            return input_param

    def execute(self, input):
        self.input.extend(input)
        output = []
        while True:
            instruction = self.instructions[self.pointer]
            opcode = instruction % 100
            input_1_mode = int(instruction / 100) % 10
            input_2_mode = int(instruction / 1000) % 10
            # Stop immediately so we don't cross input array boundaries.
            if opcode == 99:
                self.finished = True
                return output
            if opcode == 1:
                input_1 = self.get_instr_val(self.pointer + 1, input_1_mode)
                input_2 = self.get_instr_val(self.pointer + 2, input_2_mode)
                output_param = self.get_instr_val(self.pointer + 3)
                self.instructions[output_param] = input_1 + input_2
                self.pointer += 4
            elif opcode == 2:
                input_1 = self.get_instr_val(self.pointer + 1, input_1_mode)
                input_2 = self.get_instr_val(self.pointer + 2, input_2_mode)
                output_param = self.get_instr_val(self.pointer + 3)
                self.instructions[output_param] = input_1 * input_2
                self.pointer += 4
            elif opcode == 3:
                # Can't consume because we need more input.Return the output 
                # we have so far, so next amplifier can continue. We will 
                # eventually get input from through a feedback loop.
                if len(self.input) == 0:
                    return output
                output_param = self.get_instr_val(self.pointer + 1)
                self.instructions[output_param] = self.input.pop(0)
                self.pointer += 2
            elif opcode == 4:
                input_1_param = self.instructions[self.pointer + 1]
                input_1 = self.instructions[input_1_param]
                output.append(input_1)
                self.pointer += 2
            elif opcode == 5:
                if self.get_instr_val(self.pointer + 1, input_1_mode) != 0:
                    self.pointer = self.get_instr_val(self.pointer + 2, input_2_mode)
                else:
                    self.pointer += 3
            elif opcode == 6:
                if self.get_instr_val(self.pointer + 1, input_1_mode) == 0:
                    self.pointer = self.get_instr_val(self.pointer + 2, input_2_mode)
                else:
                    self.pointer += 3
            elif opcode == 7:
                input_1 = self.get_instr_val(self.pointer + 1, input_1_mode)
                input_2 = self.get_instr_val(self.pointer + 2, input_2_mode)
                output_param = self.get_instr_val(self.pointer + 3)
                self.instructions[output_param] = 1 if input_1 < input_2 else 0
                self.pointer += 4
            elif opcode == 8:
                input_1 = self.get_instr_val(self.pointer + 1, input_1_mode)
                input_2 = self.get_instr_val(self.pointer + 2, input_2_mode)
                output_param = self.get_instr_val(self.pointer + 3)
                self.instructions[output_param] = 1 if input_1 == input_2 else 0
                self.pointer += 4
            else:
                raise Exception(f"Unknown opcode {opcode} (instruction {instruction})")
        raise Exception("Failed to complete")

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
