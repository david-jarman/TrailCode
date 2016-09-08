from random import randint

def rand5():
    return randint(1,5)

def rand7():
    
    val = 22
    while val > 21:
        val = (rand5()-1) * 5 + (rand5()-1) + 1

    return (val % 7) + 1

def test_rand(rand_func, iterations):
    dict = {}

    for i in range(iterations):
        val = rand_func()
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1

    return dict

print test_rand(rand7, 1000)
