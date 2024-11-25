import math
import IO

print(f"Solving Day {__file__.split('.')[0]}")
print()

def adjacent_same(digits):
    """ Adjacents can be 2 long, 3 long, ..."""
    for i in range(1, len(digits)):
        if digits[i] == digits[i - 1]:
            return True
    return False

def adjacent_same_strict(digits):
    """ At least one adjacent group has to be exactly 2 long."""
    if digits[0] == digits[1] and digits[1] != digits[2]:
        return True

    len_d = len(digits)
    if digits[len_d - 1] == digits[len_d - 2] and digits[len_d - 2] != digits[len_d - 3]:
        return True

    for i in range(2, len(digits) - 1):
        if digits[i] == digits[i - 1] and digits[i - 1] != digits[i - 2] and digits[i] != digits[i + 1]:
            return True
    return False

def never_decrease(digits):
    for i in range(1, len(digits)):
        prev = digits[i - 1]
        curr = digits[i]
        if curr < prev:
            return False
    return True

def is_valid_password(number):
    digits = str(number)
    return adjacent_same(digits) and never_decrease(digits)

def is_valid_password_strict(number):
    digits = str(number)
    return adjacent_same_strict(digits) and never_decrease(digits)

def nr_passwords_brute_force(start, stop):
    return len([x for x in range(start, stop) if is_valid_password(x)])

def nr_passwords_strict_brute_force(start, stop):
    return len([x for x in range(start, stop) if is_valid_password_strict(x)])

###############################################################################
print("...Testing Part One...")
assert(adjacent_same("111111"))
assert(not adjacent_same("123456"))

assert(never_decrease("123456"))
assert(never_decrease("111111"))
assert(not never_decrease("223450"))

print("All tests passed!")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

valid_passwords = nr_passwords_brute_force(231832, 767346)
print(f"Number of valid passwords in range: {valid_passwords}")

print()
###############################################################################

###############################################################################
print("...Testing Part Two...")

assert(adjacent_same_strict("112233"))
assert(not adjacent_same_strict("123444"))
assert(adjacent_same_strict("111122"))

print("All tests passed!")
print()
###############################################################################

###############################################################################
print("Solving Part Two...")

valid_passwords_strict = nr_passwords_strict_brute_force(231832, 767346)
print(f"Number of valid strict passwords in range: {valid_passwords_strict}")

###############################################################################
