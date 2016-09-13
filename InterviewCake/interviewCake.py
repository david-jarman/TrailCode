def get_products_of_all_ints_except_at_index(int_list):
    products = [None] * len(int_list)
    product_so_far = 1

    for index, value in enumerate(int_list):
        products[index] = product_so_far
        product_so_far *= value

    i = len(int_list) - 1
    product_so_far = 1

    while i >= 0:
        products[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return products

def highest_product(list_of_ints):
    #[2,3,5,7,-8,-5] = 280
    #[2,3,5] = 30
    #[3,5,7]
    #[7,-8,-5]

    #highest = 7
    #lowest = -8

    #Find largest product of two ints
    #positive #'s: 3, 5
    #negative #'s: -5, 7

    # highest * #positives
    # lowest * negatives

    #return max(highest* positives, lowest * negatives)

    largest_product_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    largest_product_2 = list_of_ints[0] * list_of_ints[1]
    smallest_product_2 = list_of_ints[0] * list_of_ints[1]

    for value in list_of_ints[2:]:

        largest_product_3 = max(largest_product_3, max(largest_product_2 * value, smallest_product_2 * value))

        largest_product_2 = max(largest_product_2, max(highest * value, lowest * value))

        smallest_product_2 = min(smallest_product_2, min(lowest * value, highest * value))


        if value > highest:
            highest = value
        if value < lowest:
            lowest = value

    return largest_product_3
            
def condense_meeting_times(meetings):
    #Iterate throught list
    #Determine if the meeting overlaps a condensed meeting
    #Merge or add

    # 1 - (0,1) (2,3) no overlap, left
    # 2 - (0,1) (1,3) overlap, left
    # 3 - (1,2) (0,3) overlap, center
    # 4 - (2,3) (1,2) overlap, right
    # 5 - (2,3) (0,1) no overlap, right
    
    sorted_meetings = sorted(meetings)

    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        
        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

def compute_ways_to_make_change(amount, denominations):
    if amount < 0:
        return 0
    elif amount == 0:
        return 1
    elif len(denominations) == 0:
        return 0

    count = 0

    print "checking ways to make %s with %s" % (amount, denominations)

    current_coin, other_currencies = denominations[0], denominations[1:]

    while amount >= 0:
        count += compute_ways_to_make_change(amount, other_currencies)
        amount -= current_coin

    return count

def compute_ways_to_make_change_bottom_up(amount, denominations):
    ways_to_make_n_cents = [0] * (amount + 1)
    ways_to_make_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_to_make_n_cents[higher_amount] += ways_to_make_n_cents[higher_amount_remainder]

    return ways_to_make_n_cents[amount]
    


print compute_ways_to_make_change_bottom_up(4, [1,2,3])

#print condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

#print condense_meeting_times(  [(1, 2), (2, 3)])

#print condense_meeting_times(  [(1, 5), (2, 3)])

#print condense_meeting_times(  [(1, 10), (2, 6), (3, 5), (7, 9)])

#print highest_product([1,10,-5,1,-100])

