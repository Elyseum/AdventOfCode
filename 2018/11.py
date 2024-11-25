"""Day 11."""

def power_level(x, y, grid_serial_number):
    rack_id = x + 10
    power_level = (rack_id * y + grid_serial_number) * rack_id
    return power_level // 100 % 10 - 5

print("Power level examples:")
print(power_level(3, 5, 8))
print(power_level(122, 79, 57))
print(power_level(217, 196, 39))
print(power_level(101, 153, 71))
print("")

def create_grid(dimension, serial_number):
    rng = range(0, dimension + 1)
    return [[power_level(x, y, serial_number) for y in rng] for x in rng]

class SummedArea:

    def __init__(self, grid):
        self.sums = [[0 for y in range(len(grid))] for x in range(len(grid))]
        for x in range(len(grid)):
            for y in range(len(grid)):
                x_area = self.sums[x - 1][y] if x > 0 else 0
                y_area = self.sums[x][y - 1] if y > 0 else 0
                xy_area = self.sums[x - 1][y - 1] if x > 0 and y > 0 else 0
                self.sums[x][y] = x_area + y_area - xy_area + grid[x][y]

    def get_sum(self, x, y):
        return self.sums[x][y] if x >= 0 and y >= 0 else 0

    def area(self, x, y, d):
        area = self.get_sum(x + d - 1, y + d - 1)
        area -= self.get_sum(x + d - 1, y - 1)
        area -= self.get_sum(x - 1, y + d - 1)
        area += self.get_sum(x - 1, y - 1)
        return area
    
    def max_area(self, d):
        max_x, max_y, max_size = None, None, 0
        for y in range(1, len(self.sums) - d):
            for x in range(1, len(self.sums) - d):
                size = self.area(x, y, d)
                if size > max_size:
                    max_x, max_y, max_size = x, y, size
        return max_x, max_y, d, max_size

def max_subgrid(grid, d):
    summed_area = SummedArea(grid)
    max_x, max_y, max_size = None, None, 0
    for y in range(1, len(grid) - d):
        for x in range(1, len(grid) - d):
            size = summed_area.area(x, y, d)
            if size > max_size:
                max_x, max_y, max_size = x, y, size
    return max_x, max_y, d, max_size

print("Max subgrid: ")
print(max_subgrid(create_grid(300, 18), 3))
print(max_subgrid(create_grid(300, 42), 3))
print(max_subgrid(create_grid(300, 8444), 3))

def max_dynamic_subgrid(grid):
    summed_area = SummedArea(grid)
    max_x, max_y, dimension, max_size = None, None, None, 0
    for d in range(4, len(grid)):
        x, y, _, s = summed_area.max_area(d)
        if s > max_size:
            max_x, max_y, dimension, max_size = x, y, d, s
    return max_x, max_y, dimension, max_size

print("Max dynamic subgrid: ")
print(max_dynamic_subgrid(create_grid(300, 18)))
print(max_dynamic_subgrid(create_grid(300, 42)))
print(max_dynamic_subgrid(create_grid(300, 8444)))
