def find_matching_paren(sentence, paren_pos):
    left_open = 0
    position = paren_pos + 1
    while position < len(sentence):
        char = sentence[position]
        if char == '(':
            left_open += 1
        elif char == ')':
            if left_open == 0:
                return position
            else:
                left_open -= 1

        position += 1

    raise Exception('No matching parenthesis')

print find_matching_paren("()((()()()))(()(()))",3 )
