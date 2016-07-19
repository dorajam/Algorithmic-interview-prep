from copy import deepcopy

remainder = []
def all_combos(amount, denominations):
    
    total = 0
    for i in range(len(denominations)):
        print denominations, i
        d = denominations[i]
        remainder = amount - d
        if remainder == 0:
            return 1
        if remainder > 0:
            d = deepcopy(denominations)
            d.pop(i)
            res = all_combos(remainder, d)
            print 'res', res
            total += res
    print 'total', total
    return total


amount = 4
denominations = [1,2,3]
print all_combos(amount,denominations)
