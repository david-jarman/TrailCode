def get_max_profits(stock_prices):
    start = 0
    max_profit = -99999999

    while start < len(stock_prices) - 1:
        index = start + 1
        buy_price = stock_prices[start]
        for index in range(start+1, len(stock_prices)):
            sell_price = stock_prices[index]
            if sell_price - buy_price > max_profit:
                max_profit = sell_price - buy_price

        start = start + 1

    return max_profit

def get_max_profits_n(stock_prices):
    if len(stock_prices) < 2:
        raise IndexError('Need at least two prices to sell at')

    max_profit = stock_prices[1] - stock_prices[0]
    current_best_buy_price = stock_prices[0]

    for index, price in enumerate(stock_prices):
        if index == 0:
            continue

        potential_profit = price - current_best_buy_price

        max_profit = max(max_profit, potential_profit)

        current_best_buy_price = min(price, current_best_buy_price)

        index = index + 1

    return max_profit
    

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
bad_prices = [10, 8, 6, 4, 3]

print get_max_profits(stock_prices_yesterday)
print get_max_profits(bad_prices)

print get_max_profits_n(stock_prices_yesterday)
print get_max_profits_n(bad_prices)
