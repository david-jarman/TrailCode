def is_any_permutation_a_palindrome(string):
    chars = {}

    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    found_1 = False

    for char, count in chars.items():
        if count == 1 and found_1 == False:
            found_1 = True
        elif count == 1 and found_1 == True:
            return False
        elif count % 2 != 0:
            return False

    return True

print is_any_permutation_a_palindrome("civic"), "True"
print is_any_permutation_a_palindrome("ivicc"), "True"
print is_any_permutation_a_palindrome("civil"), "False"
print is_any_permutation_a_palindrome("raccar"), "True"
print is_any_permutation_a_palindrome("livci"), "False"

