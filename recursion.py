#Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
#FOLLOW UP
#Imagine certain squares are "off limits", such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.
def robot(matrix, i, j):
    n = len(matrix)

    if i >= n or j >= n or matrix[i][j] == 'N':
        return 0

    #No more moves possible
    if i == (n-1) and j == (n-1):
        return 1

    return robot(matrix, i+1, j) + robot(matrix, i, j+1)

def all_subsets(_set, map_set):
    if len(_set) == 1:
        if _set[0] in map_set:
            return None
        else:
            map_set[_set[0]] = 1
            return _set

    sub_sets = []

    for i in range(0, len(_set)):
        sub_set = _set[:] #copy
        sub_set.pop(i)
        sub_sets.append(sub_set)
        return_sets = all_subsets(sub_set, map_set)
        if return_sets != None:        
            sub_sets += return_sets

    return sub_sets

def all_subsets_bit(_set):
    all_subsets = []
    combinations = 1 << len(_set)

    for i in range(0, combinations):
        subset = []
        k = i
        index = 0

        while k > 0:
            #if k is even, don't add to the subset. If odd, add.
            if (k & 1) > 0:
                subset.append(_set[index])

            k = k >> 1
            index = index + 1

        all_subsets.append(subset)

    return all_subsets

some_set = [1,2,3,4]

print all_subsets_bit(some_set)

print "%s paths" % robot([[1,2,3],[4,'N',6],[7,8,9]],0,0)
