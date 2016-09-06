def fib(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    cur = 1
    prev = 0

    for i in range(1, n):
        tmp = cur
        cur = cur + prev
        prev = tmp

    return cur

def fib_lgn(n):


print fib(0)
print fib(1)
print fib(2)
print fib(3)
print fib(4)
print fib(5)
