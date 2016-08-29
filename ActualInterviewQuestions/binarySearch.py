def findIndexOfDate(orders, date):
    start_i = 0
    end_i = len(orders) - 1

    while start_i <= end_i:
        index = start_i + ((end_i - start_i) // 2)

        element = orders[index]

        if element == date:
            return [index, index]
        elif element < date:
            start_i = index + 1
        else:
            end_i = index - 1

    return [end_i, start_i]

orders = [1,3,5,7,9,19]
index = findIndexOfDate(orders, 14)
print "element exists between %s and %s" % (index[0], index[1])

# 3, 5, 7, 9

# look for 1
