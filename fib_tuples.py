# Dora Jambor
# Find the Fibonnaci number - optimized exponential to linear time complexity
# Dynamic programming prep

def fib(n):
	if n < 0:
		raise ValueError('Invalid value')
	if n < 2:
		return n
	a,b = 0,1
	# n - 1 times
	for _ in range(1, n):
		a, b = (b, a + b)
	return b

# test
print fib(3)
print fib(0)
print fib(1)
print fib(2)
# print fib(-1)