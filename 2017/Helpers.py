"""Helper methods"""

def read_line(file_name):
    """Read first line of a file"""
    with open(file_name) as file:
        return file.readline().strip()

def read_line_as_list(file_name):
    """Read first line and splits into a list"""
    return read_line(file_name).split(',')

def read_lines(file_name):
    """Reads lines of a file"""
    with open(file_name) as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def read_lines_as_integers(file_name):
    """Reads lines of a file, parses each line as an integer"""
    integers = []
    with open(file_name) as lines:
        for line in lines.readlines():
            integers.append(int(line))
        return integers
