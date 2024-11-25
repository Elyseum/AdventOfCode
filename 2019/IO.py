from datetime import datetime

"""Helper methods for doing IO."""

def log(message):
    print(f"{datetime.now()} {message}")

def read_line(file_name):
    """Read first line of a file"""
    with open(file_name) as file:
        return file.readline().strip()

def read_line_list(file_name, separator=',', transform = None):
    """
    Read first line and split it into a list.
    Applies an optional transformation to each line.
    """
    parts = read_line(file_name).split(separator)
    if transform:
        return list(map(transform, parts))
    else:
        return parts

def read_lines(file_name, transform = None):
    """
    Reads lines of a file.
    Applies an optional transformation to each line.
    """
    line_transform = lambda x: x.strip()
    if transform:
        line_transform = lambda x: transform(x.strip())
    with open(file_name) as file:
        return map(line_transform, file.readlines())

def read_lines_list(file_name, separator=','):
    line_transform = lambda x: x.strip().split(separator)
    with open(file_name) as file:
        return map(line_transform, file.readlines())
