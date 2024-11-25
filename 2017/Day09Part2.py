"""Day09Part2"""

import Helpers

class ReadableGarbageFilter:
    """
    Statefully remove group definitions and garabage instructions.
    Result of the filter is the readable garabage
    """

    def __init__(self):
        self.garbage = False
        self.ignore_next = False

    def filter(self, char):
        """Outputs readable part of the garbage"""
        if self.ignore_next:
            self.ignore_next = False
            return False
        elif char == '!':
            self.ignore_next = True
            return False
        elif char == '<' and not self.garbage:
            self.garbage = True
            return False
        elif char == '>' and self.garbage:
            self.garbage = False
            return False
        else:
            return self.garbage

def test_garbage(stream_str):
    """Test what readable garbage filter would do"""
    cleaned = filter(ReadableGarbageFilter().filter, stream_str)
    cleaned_str = "".join(cleaned)
    print("Input: '" + stream_str + "'. Readable garbage: '" + cleaned_str + "'")

test_garbage("<>")
test_garbage("<abc>")
test_garbage("<<<<>")
test_garbage("<{!>}>")
test_garbage("<!!>")
test_garbage("<!!!>>")
test_garbage("<{o\"i!a,<{i<a>")

print("")
INPUT = Helpers.read_line("Day09.txt")
READABLE_GARBAGE_LEN = len(list(filter(ReadableGarbageFilter().filter, INPUT)))
print("Readable garbage length: " + str(READABLE_GARBAGE_LEN))
