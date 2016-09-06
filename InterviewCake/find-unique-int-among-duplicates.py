def find_unique(int_list):
    unique_int = 0

    for i,v in enumerate(int_list):
        unique_int = unique_int ^ v

    return unique_int

print find_unique([2,3,4,2,4,8,8,1,9,7,9,1,7])
