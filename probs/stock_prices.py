# Dora Jambor

'''Maximize profit by buying one stock and selling it at another time stamp'''

stock_prices_yesterday = [10, 7, 5, 4, 3, 2]

def get_max_profit(stock_prices_yesterday):
    buy = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - buy

    for curr in stock_prices_yesterday:
        print buy, max_profit
        if curr == buy:
            continue

        profit = curr - buy
        max_profit = max(max_profit, profit)
        buy = min(buy, curr)

    return max_profit

print get_max_profit(stock_prices_yesterday)
