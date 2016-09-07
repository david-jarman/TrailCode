def generate_permutations(string):
    if len(string) == 1:
        return set([string])

    char = string[0]
    permutations = generate_permutations(string[1:])
    return_set = set()
    for permutation in permutations:
        for i in range(len(permutation)+1):
            return_set.add(permutation[0:i] + char + permutation[i:])

    return return_set

print generate_permutations("jarman")
