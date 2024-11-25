"""Day 04"""

import Helpers

def is_valid_passphrase(passphrase):
    words = passphrase.split()
    return len(set(words)) == len(words)

def evaluate_valid_passphrase(passphrase):
    valid = is_valid_passphrase(passphrase)
    print("Is '" + passphrase + "' valid? " + str(valid))

evaluate_valid_passphrase("aa bb")
evaluate_valid_passphrase("aa bb aa")

PASSPHRASES = Helpers.read_lines("Day04.txt")
VALID_PASSPHRASES = list(filter(is_valid_passphrase, PASSPHRASES))
print("Number of valid passphrases: " + str(len(VALID_PASSPHRASES)))
