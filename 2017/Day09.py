"""Day09"""

import Helpers

class NotGarbageFilter:
    """
    Statefully remove garbage from a stream.
    Result of the filter is everything that's not garabage
    """

    def __init__(self):
        self.garbage = False
        self.ignore_next = False

    def filter(self, char):
        if self.ignore_next:
            self.ignore_next = False
            return False
        elif char == '!':
            self.ignore_next = True
            return False
        elif char == '<':
            self.garbage = True
            return False
        elif self.garbage and char == '>':
            self.garbage = False
            return False
        else:
            return not self.garbage

class GroupScore:
    """Statefully reduces a stream of groups"""

    def __init__(self):
        self.group_level = 0

    def reduce(self, char):
        """Returns the level each time a new group is started"""
        if char == '{':
            self.group_level += 1
            return self.group_level
        elif char == '}':
            self.group_level -= 1
            return 0
        else:
            return 0

def test_garbage(stream_str):
    """Test what removing garbage would do"""
    cleaned = filter(NotGarbageFilter().filter, stream_str)
    cleaned_str = "".join(cleaned)
    print("Raw input: '" + stream_str + "'. Cleaned input: '" + cleaned_str + "'")

def count_group(chars):
    group_score = GroupScore()
    total = 0
    for char in chars:
        total += group_score.reduce(char)
    return total

def test_count_group(input_str):
    count = count_group(input_str)
    print("Score for '" + input_str + "': " + str(count))

# garbage cleanup

test_garbage("<>")
test_garbage("<abc>")
test_garbage("<<<<>")
test_garbage("<{!>}>")
test_garbage("<!!>")
test_garbage("<!!!>>")
test_garbage("<{o\"i!a,<{i<a>")

test_garbage("{<{},{},{{}}>}")
test_garbage("{{<!>},{<!>},{<!>},{<a>}}")

# counting

test_count_group('{}') # 1
test_count_group('{{}}') # 1 + 2 = 3
test_count_group('{{{}}}') # 1 + 2 + 3 = 6

test_count_group('{},{}') # 1 + 1 = 2
test_count_group('{{},{}}') # 1 + 2 + 2 = 5
test_count_group('{{{},{},{{}}}}') # 16

INPUT = Helpers.read_line("Day09.txt")
print("")
print("Raw length: " + str(len(INPUT)))

GROUP_COUNT = count_group(filter(NotGarbageFilter().filter, INPUT))
print("Group count: " + str(GROUP_COUNT))
