def reverseString(string):
    return ''.join([string[pos] for pos in range(len(string)-1, -1, -1)])

example = "namraj divad"
print reverseCStyleString(example)


