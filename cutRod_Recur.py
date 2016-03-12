# Dora Jambor
# Rod cutting problem - dynamic programming problem
# recursive solution (exponential time complexity -> overlapping computations)

def cutRod(n, prices):
	if n <= 1:
		return prices[0]
	max_val = 0
	for i in range(n):
		print i, max_val
		max_val = max(max_val, prices[i] + cutRod(n-i-1, prices))
		print max_val

	return max_val


# test
prices = [2,5,3]
n = len(prices)
print cutRod(n,prices)