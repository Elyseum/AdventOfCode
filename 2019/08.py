import math
import IO

print(f"Solving Day {__file__.split('.')[0]}")
print()

class Image:

    PIXEL_BLACK = 0
    PIXEL_WHITE = 1
    PIXEL_TRANS = 2

    def __init__(self, pixels, width, height):
        self.width = width
        self.height = height
        # Split list of pixels into equally sized layers
        layer_size = width * height
        layer_starts = range(0, len(pixels), layer_size)
        self.layers = [
            pixels[layer_start:layer_start+layer_size]
            for layer_start in layer_starts
        ]
        # By default, the layered image is not decoded.
        # Call decode() to decode it.
        self.decoded = None

    def get_layers(self):
        return self.layers

    def get_layer_min_count(self, value):
        """
        Count given value in all layers and return the layer with lowest count.
        """
        layers_count = map(lambda x: (x, x.count(value)), self.layers)
        return min(layers_count, key=lambda x: x[1])[0]

    def decode(self):
        if self.decoded is None:
            prev = None
            for layer in self.layers:
                prev = self.combine_layers(prev, layer)
            self.decoded = prev
        return self.decoded

    def combine_layers(self, front, back):
        if front is None:
            return list(back)
        else:
            return list(map(self.combine_pixels, front, back))

    def combine_pixels(self, front, back):
        return back if front == self.PIXEL_TRANS else front

    def print_decoded(self):
        row_starts = range(0, len(self.decoded), self.width)
        rows = [
            self.decoded[row_start:row_start+self.width]
            for row_start in row_starts
        ]
        for row in rows:
            print(''.join(map(self.printable_pixel, row)))
    
    def printable_pixel(self, pixel):
        return ' ' if pixel is 0 else '@'


###############################################################################
example = Image([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 3, 2)
assert(2 == len(example.get_layers()))

print("...Testing Part One: All tests passed!...")
print()
###############################################################################

###############################################################################
print("...Solving Part One...")

def solve_part_1(image):
    layer_min_count_zero = image.get_layer_min_count(0)
    return layer_min_count_zero.count(1) * layer_min_count_zero.count(2)

instructions = list(map(int, IO.read_line('08.txt')))
image = Image(instructions, 25, 6)

print(f"Part 1: {solve_part_1(image)}")

print()
###############################################################################

###############################################################################

example = Image([0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0], 2, 2)
assert(4 == len(example.get_layers()))
assert([0, 1, 1, 0] == example.decode())

print("...Testing Part Two: All tests passed!...")
print()
###############################################################################

###############################################################################
print("Solving Part Two...")

image.decode()
image.print_decoded()

###############################################################################
