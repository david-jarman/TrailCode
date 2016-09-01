def swap_in_place(arr, i, j):
    arr[j] += arr[i]
    arr[i] = arr[j] - arr[i]
    arr[j] -= arr[i]

def is_winner_tic_tac_toe(matrix):
    if len(matrix) != 3:
        return False

    if len(matrix[0]) != 3:
        return false

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        row_match = True
        col_match = True
        for j in range(cols):
            row_target = matrix[i][0]
            col_target = matrix[0][j]

            row_val = matrix[i][j]
            col_val = matrix[j][i]

            if row_target == '':
                row_match = False
            elif row_target != row_val:
                row_match = False

            if col_target == '':
                row_match = False
            elif col_target != col_val:
                col_match = False

        if row_match || col_match:
            return True

    #check diagnols 
    
    
            

            

            

def determine_match(target_value, value):
    

arr = [1,2,3,4,5]

swap_in_place(arr, 1, 3)

print arr
