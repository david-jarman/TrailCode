def is_single_riffle(shuffled_deck, half1, half2):
    half_1_index = 0
    half_2_index = 0

    for card in shuffled_deck:
        if half_1_index < len(half1) and card == half1[half_1_index]:
            half_1_index += 1
        elif half_2_index < len(half2) and card == half2[half_2_index]:
            half_2_index += 1
        else:
            return False

    return True

print "true: ", is_single_riffle([1,2,4,5,3], [1,2,3], [4,5])
print "false: ", is_single_riffle([1,2,5,4,3], [1,2,3], [4,5])
