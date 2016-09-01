#Imagine you landed a new job as a cashier...
#Your quirky boss found out that you're a programmer and has a weird request about something they've been wondering for a long time.

#Write a function that, given:

#an amount of money
#a list of coin denominations
#computes the number of ways to make amount of money with coins of the available denominations.

#bottom up solution:

def count_ways_to_make_change(amount, denominations):
    ways_to_make_change = [0] * (amount + 1)

    ways_to_make_change[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_to_make_change[higher_amount] += ways_to_make_change[higher_amount_remainder]

    return ways_to_make_change[amount]

