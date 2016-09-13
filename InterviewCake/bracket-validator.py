def bracket_validator(string):
    stack = []

    for char in string:
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            elif not open_matches(stack[-1], char):
                return False
            else:
                stack.pop()

    return len(stack) == 0

def open_matches(_open, _close):
    matching_paren_dict = { '{': '}', '(': ')', '[': ']' }
    return _close == matching_paren_dict[_open]


print bracket_validator("{ [ ] ( ) }"), 'True'
print bracket_validator("{ [ ( ] ) }"), 'False'
print bracket_validator("{ [ }"), 'False'
