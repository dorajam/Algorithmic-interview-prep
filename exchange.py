# Dora and Leo
currencies = ["USD","JPY","BTC","EUR"]
rates = {}

rates["USD"] = {"JPY": 102.4, "EUR": 0.92, "BTC": 0.085}
rates["JPY"] = {"EUR": 0.009, "USD": 0.01, "BTC": 0.00092}
rates["BTC"] = {"USD": 12, "JPY": 1400, "EUR": 10}
rates["EUR"] = {"USD": 1.1, "JPY": 114, "BTC": 0.092}


# one of X is worth the given amount of Y
# given an amount of M what transactions do you have to go through to maximize M?
# you are allowed to do 3 transactions to maximize your value

# m -> k1m -> k1k2m -> k1k2k3m = m' where m' > m


def path(initial_currency):
    max_path = 0
    current = 0
    for c1,v1 in rates[initial_currency].items():
        for c2,v2 in list(set(rates[c1].items())-set([(initial_currency, rates[c1][initial_currency])])):
            current = rates[c2][initial_currency] * v2 * v1
            if current > max_path:
                max_path = current
                path = [initial_currency, c1,c2, initial_currency]
    return max_path

print path("JPY")
