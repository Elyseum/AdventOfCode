"""Day 1"""

def get_digits():
    """Reads the input as a string"""
    with open("Day01.txt") as input_file:
        return input_file.readline()

def get_result(digits):
    """Returns the sum"""
    sum_digits = 0
    prev_digit = None
    for digit in digits:
        if prev_digit == digit:
            sum_digits += int(digit)
        prev_digit = digit
    if digits[-1] == digits[0]:
        sum_digits += int(digits[0])

    return sum_digits

DIGITS = get_digits()
RESULT = get_result(DIGITS)

print("Day01 result: " + str(RESULT))
