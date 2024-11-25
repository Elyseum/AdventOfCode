
from collections import deque

def calc(nr_players, last_marble):
    scores = [0 for _ in range(nr_players + 1)]
    player = 0
    marbles = deque([0])
    for marble in range(1, last_marble + 1):
        player = player + 1 if player < nr_players else 1
        if marble % 23 is 0:
            marbles.rotate(7)
            scores[player] += marbles.pop() + marble
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)
    print(max(scores))

# Examples
calc(9, 25)
calc(10, 1618)
calc(13, 7999)
calc(17, 1104)
calc(21, 6111)
calc(30, 5807)

calc(477, 70851)
calc(477, 70851 * 100)