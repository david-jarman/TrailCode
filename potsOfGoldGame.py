dp_dict = {}

def max_coin(coins, start, end):
    if start > end:
        return 0

    key = "%s %s" % (start, end)
    if key in dp_dict:
        return dp_dict[key]

    a = coins[start] + min(max_coin(coins, start+2, end), max_coin(coins, start+1, end-1))
    b = coins[end] + min(max_coin(coins, start+1,end-1), max_coin(coins, start, end-2))

    result = max(a,b)
    dp_dict[key] = result
    return result

coins = [8,1,2,5,3,7,3,2,3,6,10,11,4]

print max_coin(coins, 0, len(coins)-1)
