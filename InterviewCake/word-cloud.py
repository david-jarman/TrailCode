def make_word_cloud_dictionary(string):
    word_cloud = {}
    current_word = []
    for char in string:
        if char.isalpha() or char == '-' or char == '\'':
            current_word.append(char)
        elif len(current_word) > 0:
            current_word_str = ''.join(current_word).lower()
            if current_word_str in word_cloud:
                word_cloud[current_word_str] += 1
            else:
                word_cloud[current_word_str] = 1

            current_word = []

    return word_cloud    

sentence = "After beating the eggs, Dana-kun read the next step: Add milk and eggs, then add flour and sugar."
sentence2 = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."

print make_word_cloud_dictionary(sentence)
print make_word_cloud_dictionary(sentence2)
