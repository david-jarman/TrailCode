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

print fibonacci_dp(15)
print fibonacci_dp(16)
print fibonacci_dp(17)
print fibonacci_dp(18)
print fibonacci_dp(19)
print fibonacci_dp(20)
