def find_unique(int_list):
    x_or_value = None

    for i,v in enumerate(int_list):
        if i == 0:
            x_or_value = v
        else:
            x_or_value = (x_or_value & ~v) | (~x_or_value & v)

    return x_or_value

print find_unique([2,3,4,2,4,8,8,1,9,7,9,1,7])
