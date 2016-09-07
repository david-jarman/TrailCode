#strings not mutable in python, so we'll do a "close enough" solution
def reverse_string(string):
    string_list = list(string)

    start = 0
    end = len(string_list) - 1

    while start < end:
        string_list[start], string_list[end] = string_list[end], string_list[start]
        start += 1
        end -= 1

    return ''.join(string_list)

print reverse_string("david jarman")
