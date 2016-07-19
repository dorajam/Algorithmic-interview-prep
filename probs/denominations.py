# Dora Jambor
# denominations.py

# dynamic approach
rem = []

def all_combos(amount, denominations):
    total = 0

    for denom in denominations:
        print amount, denom
        remaining = amount - denom
        print 'remain', remaining

        if remaining == 0:
            total+= 1
            return total

        elif remaining > 0 and remaining not in rem:
            rem.append(remaining)
            total+= all_combos(remaining, denominations)
    return total

amount = 4
denominations = [1,2,3]
print all_combos(amount,denominations)
