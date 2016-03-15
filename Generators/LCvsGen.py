# Dora Jambor
# Performance difference between using a list comprehension or generator
'''The important point is that the list comprehension creates a new list. 
The generator creates a an iterable object that will "filter" the source 
material on-the-fly as you consume the bits.'''

import time

# ---------------------------- List comprehension ------------------------------
start = time.time()
my_nums = [x*x for x in range(1000)]		# list comprehension

# test
print my_nums				
print "Time took: ", time.time() - start # time = 0.00081992149353

# ---------------------------- Generator ------------------------------
start = time.time()
my_nums = (x*x for x in range(1000))		# parantheses changed - it's a generator now

# test
print my_nums				
print "Time took: ", time.time() - start # time = 4.79221343994e-05 

