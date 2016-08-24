# Given an NxN matrix with the only value being "O", "G", or "W", find the shortest path between the two guards
# example:
#
# input:
# ['O', 'G']
# ['G', 'O']
# output: 2
#
# input:
# [O, O, O]
# [O, W, O]
# [G, O, G]
# output: 2
#

def is_move_legal(matrix, path,  i, j):
    n = len(matrix)

    if (i + 1) > n or (j + 1) > n:
        return False
    elif i < 0 or j < 0:
        return False
    elif matrix[i][j] == 'W':
        return False
    elif path[i][j] == 1:
        return False
    elif matrix[i][j] == 'O':
        return True
    elif matrix[i][j] == 'G':
        return True
    else:
        return False

def find_path(matrix, path, pos_i, pos_j, target_i, target_j, num_moves, min_num_moves):
    if pos_i == target_i and pos_j == target_j:
        if num_moves < min_num_moves:
            return num_moves
        else:
            return min_num_moves

    #move up if possible
    if is_move_legal(matrix, path, pos_i - 1, pos_j):
        path[pos_i-1][pos_j] = 1
        min_num_moves = find_path(matrix, path, pos_i - 1, pos_j, target_i, target_j, num_moves + 1, min_num_moves)
        path[pos_i-1][pos_j] = 0
    if is_move_legal(matrix, path, pos_i, pos_j + 1):
        path[pos_i][pos_j+1] = 1
        min_num_moves = find_path(matrix, path, pos_i, pos_j+1, target_i, target_j, num_moves + 1, min_num_moves)
        path[pos_i][pos_j+1] = 0
    if is_move_legal(matrix, path, pos_i + 1, pos_j):
        path[pos_i+1][pos_j] = 1
        min_num_moves = find_path(matrix, path, pos_i + 1, pos_j, target_i, target_j, num_moves + 1, min_num_moves)
        path[pos_i+1][pos_j] = 0
    if is_move_legal(matrix, path, pos_i, pos_j-1):
        path[pos_i][pos_j-1] = 1
        min_num_moves = find_path(matrix, path, pos_i, pos_j-1, target_i, target_j, num_moves + 1, min_num_moves)
        path[pos_i][pos_j-1] = 0 

    return min_num_moves


#matrix = [['O', 'O', 'O'], ['O', 'W', 'O'], ['G', 'O', 'G']]
 
matrix = [['O','O','O','O','G'], ['O', 'W', 'O', 'W', 'O'], ['O','W','O','W','O'], ['O','W','O','W','O'], ['G','W','O','O','O']]

path = []
for i in range(len(matrix)):
    path.append([])
    for j in range(len(matrix)):
        path[i].append(0)


num_moves = find_path(matrix, path, 4, 0, 0, 4, 0, 99999)

print 'moves: %s' % num_moves
