
def get_spiral_corners(number):
    counter = 1
    edge_number = 1
    while True:
        counter += 1
        edge_number += 2 # odd numbers: 1, 3, 5, ...
        next_square = edge_number * edge_number # 1, 9, 25, ...
        if next_square >= number:
            return (
                next_square - edge_number - edge_number - edge_number + 3,
                next_square - edge_number - edge_number + 2,
                next_square - edge_number + 1,
                next_square,
                counter - 1)

def get_distance_to_center(number, a, b):
    return abs(number - int(a + (b - a) / 2))

def where_is_it(number):
    position_info = get_spiral_corners(number)
    bottom_right = position_info[3]
    bottom_left = position_info[2]
    top_left = position_info[1]
    top_right = position_info[0]
    distance_to_side = position_info[4]
    print("Positions for " + str(number) + ": " + str(position_info))
    if bottom_left <= number and number <= bottom_right:
        distance_to_center = get_distance_to_center(number, bottom_left, bottom_right)
        distance_to_start = distance_to_center + distance_to_side
        print(str(number) + " is at the bottom. Distance to start is " + str(distance_to_start))
    elif top_right <= number and number <= top_left:
        distance_to_center = get_distance_to_center(number, top_right, top_left)
        distance_to_start = distance_to_center + distance_to_side
        print(str(number) + " is at the top. Distance to start is " + str(distance_to_start))
    elif top_left <= number and number <= bottom_left:
        distance_to_center = get_distance_to_center(number, bottom_left, top_left)
        distance_to_start = distance_to_center + distance_to_side
        print(str(number) + " is at the left. Distance to start is " + str(distance_to_start))
    else:
        print(str(number) + " is at the right")

where_is_it(8)
where_is_it(9)
where_is_it(4)
where_is_it(5)
where_is_it(6)
where_is_it(2)

where_is_it(1024)
where_is_it(312051)
