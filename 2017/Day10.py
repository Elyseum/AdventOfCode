"""Day10"""

def reverse(numbers, start_pos, length):
    """Cyclic reverse in sublist of length starting at start_pos"""
    list_length = len(numbers)
    length = min([list_length, length])

    switch_length = int(length / 2)
    for index_to_switch in range(switch_length):
        to_switch = (start_pos + index_to_switch) % list_length
        switch = (start_pos + length - 1 - index_to_switch) % list_length
        numbers[to_switch], numbers[switch] = numbers[switch], numbers[to_switch]
    return numbers

print("Testing reverse logic: ")
print(reverse([0, 1, 2, 3, 4], 0, 3))
print(reverse([2, 1, 0, 3, 4], 3, 4))

def knot_hash(numbers, reverse_lengths, iterations=1):
    """Apply knot hash to list of numbers for given iterations."""
    start_pos = 0
    skip_size = 0
    numbers_length = len(numbers)
    for _ in range(iterations):
        for reverse_length in reverse_lengths:
            reverse(numbers, start_pos, reverse_length)
            start_pos = (start_pos + skip_size + reverse_length) % numbers_length
            skip_size += 1
    return numbers

print("Testing apply reverse: ")
print(knot_hash([0, 1, 2, 3, 4], [3, 4, 1, 5]))

INPUT = [76, 1, 88, 148, 166, 217, 130, 0, 128, 254, 16, 2, 130, 71, 255, 229]
REVERSED = knot_hash(list(range(0, 256)), INPUT)
print("First 2 numbers multiplied: " + str(REVERSED[0] * REVERSED[1]))

# Part 2

def convert_to_ascii(input_str):
    """Returns list of ascii numbers for given input string"""
    return list(map(ord, input_str))

def finalize_length_sequence(length_sequence):
    """Adding a salt"""
    return length_sequence + [17, 31, 73, 47, 23]

print("Testing convert to ASCII: " + str(convert_to_ascii("1,2,3")))

def dense_hash_block(numbers):
    """XORs the numbers to create a dense hash"""
    result = 0
    for number in numbers:
        result = result ^ number
    return result

def dense_hash(values, block_size):
    """Creates a dense hash for given input and given block size"""
    block_start_positions = range(0, len(values), block_size)
    blocks = [values[i:i+block_size] for i in block_start_positions]
    return list(map(dense_hash_block, blocks))

print("Testing dense hash (block): ")
print(dense_hash_block([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]))
print(dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22], 16))

def two_letter_hex(number):
    """two letter hex for given number"""
    return hex(number)[2:].zfill(2) # hex gives 0x40, 0x7, ... we want 40, 07

def to_hex(numbers):
    """List of numbers into a hex string"""
    return "".join(map(two_letter_hex, numbers))

print("Testing hex: " + str(to_hex([64, 7, 255])))

def knot_hash_str(numbers, lengths_str):
    lengths_ascii = convert_to_ascii(lengths_str)
    finalized = finalize_length_sequence(lengths_ascii)
    knotted = knot_hash(numbers, finalized, 64)
    dense_hashed = dense_hash(knotted, 16)
    return to_hex(dense_hashed)

print(knot_hash_str(list(range(0, 256)), "1,2,3"))
print(knot_hash_str(list(range(0, 256)), "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"))
