# Dora Jambor
# fibonacci

def fib(n):
	if n < 0:
		raise Exception
	if n < 2:
		return n
	a = 0
	b = 1
	for _ in range(1, n):
		a,b = (b, a + b)
	return b