# Design a function called rand2 that outputs 0 or 1 with equal chance. Use standard libraries to do this.
# Design a function called rand7 that produces a value between 0 and 6 with equal chance. The function can only use calls to rand2.
# Write a function to test the random number generators you design.

from random import random

rand2 = lambda : 0 if random() < 0.5 else 1

rand4 = lambda : rand2() * 2 + rand2()

rand8 = lambda : rand2() * 4 + rand4()

def rand7():
    rand_val = rand8()
    while rand_val >= 7:
        rand_val = rand8()

    return rand_val

def test_rand(func):
    num_map = {}
    
    for i in xrange(1000):
        rand = func()
        if rand in num_map:
            num_map[rand] += 1
        else:
            num_map[rand] = 1

    return num_map

print test_rand(rand2)
print test_rand(rand4)
print test_rand(rand8)
print test_rand(rand7)

