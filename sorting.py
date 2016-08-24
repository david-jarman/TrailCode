def quickSort(unsorted_list):
    less = []
    equal = []
    greater = []

    if len(unsorted_list) > 1:
        pivot = unsorted_list[0]

        for element in unsorted_list:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)

        return quickSort(less) + equal + quickSort(greater)

    else:
        return unsorted_list

print quickSort([5,1,9,3,0,4,7,9,9,5,2,8,3,5,6,3])
