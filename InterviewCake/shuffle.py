from random import randint

def shuffle(_list):
    start = 0
    end = len(_list) - 1

    for i in range(len(_list)):
        swap_index = randint(start, end)
        _list[i], _list[swap_index] = _list[swap_index], _list[i]
        start += 1

def shuffle_naive(_list):
    for element_to_shuffle_index in range(len(_list)-1):
        element_to_swap_index = randint(0, len(_list)-1)
        _list[element_to_shuffle_index], _list[element_to_swap_index] = _list[element_to_swap_index], _list[element_to_shuffle_index]

def test_shuffle(shuffle_func):
    test_runs = 10000
    matrix = [[0] * 10 for _ in range(10)]

    for _ in range(test_runs):
        list = range(10)
        shuffle_func(list)
        for i,v in enumerate(list):
            matrix[v][i] += 1

    matrix = [[i / float(test_runs) for i in row] for row in matrix]
    
    return matrix

matrix =  test_shuffle(shuffle)
for row in matrix:
    print row
