def reverse_words(message):
    message_list = list(message)

    start = 0
    end = len(message_list) - 1

    reverse_characters(message_list, start, end)

    space_indices = [i for i,v in enumerate(message_list) if v == ' ']

    space_indices.append(len(message_list))

    start_word_index = 0
    for end_word_index in space_indices:
        reverse_characters(message_list, start_word_index, end_word_index-1)
        start_word_index = end_word_index + 1

    return ''.join(message_list)

def reverse_characters(message_list, start, end):

    while start < end:
        message_list[start], message_list[end] = message_list[end], message_list[start]
        start += 1
        end -= 1

    return ''.join(message_list)

message = 'find you will pain only go you recordings security the into if'
print reverse_words(message)
