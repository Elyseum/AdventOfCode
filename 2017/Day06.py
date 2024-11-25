"""Day 06"""

import operator

def get_reallocate_start(memory):
    """Return position to"""
    max_index, _ = max(enumerate(memory), key=operator.itemgetter(1))
    return max_index

def reallocate(memory, position):
    """Reallocate from starting position"""
    value_to_reallocate = memory[position]
    memory[position] = 0
    while value_to_reallocate > 0:
        position = position + 1
        if position >= len(memory):
            position = 0
        memory[position] += 1
        value_to_reallocate -= 1
    return memory

def register_memory(registry, memory):
    """Registers memory setting, return true if already seen"""
    key = str(memory)
    if registry.get(key, False):
        return True
    else:
        registry[key] = True
        return False

SAMPLE_MEM = [0, 2, 7, 0]
print("Reallocation start for " + str(SAMPLE_MEM) + ": "
      + str(get_reallocate_start(SAMPLE_MEM)))

SAMPLE_MEM = [3, 1, 2, 3]
print("Reallocation start for " + str(SAMPLE_MEM) + ": "
      + str(get_reallocate_start(SAMPLE_MEM)))

SAMPLE_MEM = [0, 2, 7, 0]
print("Reallocating " + str(SAMPLE_MEM) + ": "
      + str(reallocate(SAMPLE_MEM, 2)))

def redistribute(memory):
    """Redistributes the memory and returns how many cycles it took"""
    cycles = 0
    registry = {}
    while not register_memory(registry, memory):
        reallocate_start = get_reallocate_start(memory)
        memory = reallocate(memory, reallocate_start)
        cycles += 1
    return cycles

MEM = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

print("Number of redistribution cycles: " + str(redistribute(MEM)))
