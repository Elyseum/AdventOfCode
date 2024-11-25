"""Day 2"""

class Spreadsheet():
    """Spreadsheet as a row of integer rows"""

    def __init__(self, file_name):
        self.rows = []
        with open(file_name) as input_file:
            for line in input_file.readlines():
                self.rows.append(list(map(int, line.split())))

    def get_line_checksum(self, list_of_numbers):
        """Checksum for a list of numbers"""
        return max(list_of_numbers) - min(list_of_numbers)

    def get_checksum(self):
        """Calculate spreadsheet checksum by Sums the checksum for each spreadsheet line"""
        return sum(map(self.get_line_checksum, self.rows))

CHECKSUM = Spreadsheet("Day02.txt").get_checksum()
print("Spreadsheet checksum: " + str(CHECKSUM))
