def find_number_in_range_that_appears_twice(int_range, n):
    sum_1_n = (n * (n + 1)) / 2
    int_range_sum = 0
    for i in int_range:
        int_range_sum += i

    return int_range_sum - sum_1_n

print find_number_in_range_that_appears_twice([1,2,3,4,5,6,7,8,8,9,10,11,12,13,14,15], 15)
