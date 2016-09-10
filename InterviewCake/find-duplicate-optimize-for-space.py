def find_duplicate(list):
    floor = 1
    ceiling = len(list) - 1

    while floor < ceiling:
        midpoint = floor + ((ceiling - floor) // 2)

        floor_range_floor, floor_range_ceiling = floor, midpoint
        ceiling_range_floor, ceiling_range_ceiling = midpoint + 1, ceiling

        items_in_lower_range = 0

        for item in list:
            if item >= floor_range_floor and item <= floor_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = floor_range_ceiling - floor_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            floor, ceiling = floor_range_floor, floor_range_ceiling
        else:
            floor, ceiling = ceiling_range_floor, ceiling_range_ceiling

    return floor

import pdb

def find_duplicate_n_1(list):
    head = list[-1]
    n = len(list) - 1
    cycle_length = 1
    first_node_in_cycle = 0

    #get to the cycle
    node = head
    for i in range(n):
        node = list[node-1]

    #inside the cycle now
    start = node
    node = list[node-1]
    while start != node:
        node = list[node-1]
        cycle_length += 1

    #find first node of the cycle
    pointer_start = n + 1
    pointer_ahead = n + 1
    for _ in range(cycle_length):
        pointer_ahead = list[pointer_ahead - 1]

    while pointer_start != pointer_ahead:
        pointer_start = list[pointer_start-1]
        pointer_ahead = list[pointer_ahead-1]

    return pointer_ahead

print find_duplicate_n_1([8,9,4,7,2,1,5,3,9,6]), ' : should be 9'
print find_duplicate_n_1([3, 4, 2, 3, 1, 5]), ' : should be 3'
print find_duplicate_n_1([3,1,2,2]), ' : should be 2'
print find_duplicate_n_1([4,3,1,1,4]), ' : should be 4'

