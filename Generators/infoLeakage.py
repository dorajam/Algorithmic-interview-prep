import time
start = time.time()

# this will store x for you -> information leaked - Python 3 corrects for it
K = [x**2 for x in range(5)]
print x

# this will not store y for you 
R = list(y**2 for y in range(5))
print y

print time.time()-start