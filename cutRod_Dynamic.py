# Dora Jambor
# Rod cutting problem - dynamic programming problem
# dynamic solution - O(n^2)

def cutRod(n, prices):
	val = [0 for x in range(n+1)]

	for i in range(1,n+1):
		max_val = 0
		for j in range(i):
			max_val = max(max_val, prices[j] + val[i-j-1])
			print max_val
		val[i] = max_val
	return val[n]

# test
prices = [2,5,3]
n = len(prices)
print cutRod(n,prices)