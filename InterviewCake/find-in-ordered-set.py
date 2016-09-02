def binarySearch(ordered_list, int_value):
    start  = 0
    end = len(ordered_list) - 1

    while start <= end:
        index = start + ((end - start) // 2)

        if int_value < ordered_list[index]:
            end = index - 1
        elif int_value > ordered_list[index]:
            start = index + 1
        else:
            return index

    return None

def binary_search_rotation(rotated_sorted_list):
    start = 0
    end = len(rotated_sorted_list) - 1

    if rotated_sorted_list[start] < rotated_sorted_list[end]:
        return 0

    while (end - start) > 1:
        index = start + ((end - start) // 2)

        if rotated_sorted_list[index] < rotated_sorted_list[start]:
            end = index
        elif rotated_sorted_list[index] > rotated_sorted_list[end]:
            start = index

    return end

ordered_list = range(1,100)

print binarySearch(ordered_list, 1)

print binary_search_rotation([5,6,7,8,9,10,11,12,13,14,15,1,2,3,4])

print binary_search_rotation([0,1,2,3,4,5])
