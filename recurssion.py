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

print "%s paths" % robot([[1,2,3],[4,'N',6],[7,8,9]],0,0)
