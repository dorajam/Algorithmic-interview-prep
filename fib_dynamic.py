# Dora Jambor
# Find the Fibonnaci number - optimized exponential to linear time complexity
# Dynamic programming prep

def fib(n):
	if n < 0:
		raise ValueError('Invalid input')
	fibs = [0,1]
	for i in range(2, n+1):
		fibs.append(fibs[n-1] + fibs[n-2])
	print fibs
	return fibs[n]

# test
print fib(3)
print fib(0)
print fib(1)
print fib(2)
print fib(6)