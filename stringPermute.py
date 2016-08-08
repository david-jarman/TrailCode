#functions
def merge(_str, _char):
    permutations = []
    for i in range(0, len(_str)+1):
        permutedString = _str[0:i] + _char + _str[i:len(_str)]
        permutations.append(permutedString)

    return permutations

def permute(string):
    if len(string) == 1:
        return [string]

    char = string[len(string)-1:]
    previous_permutations = permute(string[:len(string)-1])
    permutations = []
    for permutation in previous_permutations:
        new_permutations = merge(permutation, char)
        permutations += new_permutations

    return permutations

#main

testString = "abcdef"

permutations = permute(testString)

print permutations
