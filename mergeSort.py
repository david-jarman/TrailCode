def mergeSort(_list):
    if len(_list) <= 1:
        return _list
    
    middle = len(_list) / 2
    
    list1 = _list[0:middle]
    list2 = _list[middle:len(_list)]

    sortedList1 = mergeSort(list1)
    sortedList2 = mergeSort(list2)
    
    return merge(sortedList1, sortedList2)
    
def merge(_list1, _list2):
    sortedList = []
    
    i = 0
    j = 0
    
    while i < len(_list1) or j < len(_list2):
        element1 = None
        element2 = None

        if i < len(_list1):
            element1 = _list1[i]
        if j < len(_list2):
            element2 = _list2[j]

        if element1 != None and element2 != None:
            if element1 < element2:
                sortedList.append(element1)
                i += 1
            else:
                sortedList.append(element2)
                j += 1
        elif element1 != None:
            sortedList.append(element1)
            i += 1
        else:
            sortedList.append(element2)
            j += 1
        
    return sortedList

list1 = [5,1,3,6,2,9,10,50,24,23,99,84,7]

print len(list1)
print list1
sortedList = mergeSort(list1)
print len(sortedList)
print sortedList
