"""Day13"""

import Helpers

class Layer:

    def __init__(self, layer_range):
        self.layer_range = layer_range
        self.scan_position = 0
        self.scan_direction = 1 # 1 for up, -1 for down

    def scan_next(self):
        self.scan_position += self.scan_direction * 1
        # Switch scan direction if end or start position reached
        if self.scan_position == self.layer_range - 1:
            self.scan_direction = -1
        elif self.scan_position == 0:
            self.scan_direction = 1

class Firewall:

    def __init__(self, debug):
        self.packet_depth = -1 # Not entered yet
        self.layers = []
        self.debug = debug

        self.penalty = 0
        self.times_caught = 0

    def add_layer(self, position, layer):
        for _ in range(len(self.layers), position):
            self.layers.append(None)
        self.layers.append(layer)

    def scan_next(self):
        for layer in filter(None, self.layers):
            layer.scan_next()

    def move_next(self):
        self.packet_depth += 1
        return self.packet_depth

    def advance(self, steps):
        for layer in filter(None, self.layers):
            layer.advance(steps)

    def send_package(self, break_when_caught=False):
        """Returns penalty"""
        for scanned in range(0, len(self.layers)):
            packet_depth = self.move_next()

            if self.debug:
                print(FirewallPrinter(self))

            layer = self.layers[packet_depth] # check if caught
            if layer and layer.scan_position == 0:
                print("Penalty on position " + str(packet_depth))
                self.penalty += packet_depth * layer.layer_range
                self.times_caught += 1
                if break_when_caught:
                    if not scanned:
                        self.scan_next()
                    return self.times_caught, self.penalty

            self.scan_next()

        return self.times_caught, self.penalty

class FirewallPrinter:

    def __init__(self, firewall):
        self.firewall = firewall

    def get_header(self):
        layers = self.firewall.layers
        return " ".join(map(lambda x: " " + str(x) + " ", range(0, len(layers))))

    def get_cell_nolayer(self, row, col):
        if row == 0:
            if self.firewall.packet_depth == col:
                return "(.) "
            else:
                return "... "
        else:
            return "    "

    def get_cell_layer(self, row, col, layer):
        if row >= layer.layer_range:
            return "    "

        if row == layer.scan_position:
            if row == 0 and self.firewall.packet_depth == col:
                return "(S) "
            else:
                return "[S] "
        else:
            if row == 0 and self.firewall.packet_depth == col:
                return "( ) "
            else:
                return "[ ] "

    def get_row(self, row):
        layers = self.firewall.layers
        row_str = ""
        for col, layer in enumerate(layers):
            if layer:
                row_str += self.get_cell_layer(row, col, layer)
            else:
                row_str += self.get_cell_nolayer(row, col)
        return row_str

    def __str__(self):
        layers = self.firewall.layers

        if not layers:
            return "<empty>"

        lines = [self.get_header()]

        max_range = max(map(lambda x: x.layer_range, filter(None, layers)))
        for row_index in range(0, max_range):
            lines.append(self.get_row(row_index))

        return "\n".join(lines)

def create_firewall_example():
    firewall = Firewall(True)

    firewall.add_layer(0, Layer(3))
    firewall.add_layer(1, Layer(2))
    firewall.add_layer(4, Layer(4))
    firewall.add_layer(6, Layer(4))

    return firewall

# FIREWALL = create_firewall_example()
# PENALTY = FIREWALL.send_package()
# print("Penalty for moving package: " + str(PENALTY))

def create_firewall_from_lines(lines):
    firewall = Firewall(False)
    for line in lines:
        parts = line.split(': ') # '3: 6' is a layer with range 6 on position 3
        layer = Layer(int(parts[1]))
        firewall.add_layer(int(parts[0]), layer)
    return firewall

def create_firewall_from_file(file_name):
    lines = Helpers.read_lines(file_name)
    return create_firewall_from_lines(lines)

FIREWALL = create_firewall_from_file("Day13.txt")
PENALTY = FIREWALL.send_package()
print("Penalty for moving package: " + str(PENALTY))

def min_delay_without_getting_caught():
    times_caught = 1
    delay = 0
    # firewall = create_firewall_from_file("Day13.txt")
    firewall = create_firewall_example()
    while times_caught > 0 and delay < 11:
        # Reset start position
        firewall.packet_depth = -1
        firewall.times_caught = 0

        delay += 1
        print("delay: " + str(delay))
        result = firewall.send_package(True)
        print("Result: " + str(result))
        times_caught = result[0]
    return delay

MIN_DELAY = min_delay_without_getting_caught()
print("Min delay: " + str(MIN_DELAY))
