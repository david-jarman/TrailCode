#You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e.g., M becomes a substring of N located at i and starting at j).
def five_one(N, M, i, j):
    max_mask = ~0

    left_mask = max_mask - ((1 << j) - 1)
    right_mask = ((1 << i) - 1)

    mask = left_mask | right_mask

    return (N & mask) | (M << i)

def bin(s):
    return str(s) if s <= 1 else bin(s>>1) + str(s&1)


N = 1023
M = 21

i = 2
j = 6

print bin(five_one(N, M, i, j))
