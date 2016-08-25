def fibonacci(n):
    if n <= 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

map_dp = {}
def fibonacci_dp(n):
    if n <= 1:
        return 1
    
    result = 0
    if n in map_dp:
        result = map_dp[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        map_dp[n] = result

    return result
def fibonacci_iter(n):
    cur_result = 1
    prev_result = 0

    for i in range(0, n):
        tmp = cur_result
        cur_result = cur_result + prev_result
        prev_result = tmp

    return cur_result
        
print fibonacci_iter(10)
print fibonacci_dp(10)
