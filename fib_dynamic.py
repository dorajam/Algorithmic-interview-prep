# linear time

if n < 0
exception
if n < len(fibs):
return fibs[n]
result = fib(n-1) + fib(n-2)
fibs.append(result)
return result