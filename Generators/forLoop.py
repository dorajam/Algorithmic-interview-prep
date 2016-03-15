import time
import dis

# ---------------------------- For Loop ------------------------------
# Look at the memory usage in your RAM and the time performance
startT = time.time()

def square_num(nums):
	result = []
	for num in nums:
		result.append(num * num)
	return result

# test
my_nums = square_num([1, 2, 3, 4])
print "Time took: ", time.time() - startT
print my_nums
dis.dis(square_num) # look at the bytecode under the hood

# ---------------------------- Generator ------------------------------
startT1 = time.time()

def square_num(nums):
	result = []
	for num in nums:
		yield( num * num)

# test
my_nums = square_num([1, 2, 3, 4])	# <generator object square_num at 0x1020ec0f0>
print my_nums
print next(my_nums)			# [1]
print next(my_nums)			# [4]
print next(my_nums)			# [9]
print next(my_nums)			# [16]
# print next(my_nums)			# Error: StopIteration
print "Time took: ", time.time() - startT

for num in my_nums:
	print num			# prints out numbers one by one - knows when to stop


# ---------------------------- Generator with list comprehension ------------------------------
startT = time.time()

# my_nums = [x*x for x in [1,2,3,4]]		# this creates a normal list e.g. 1st example
my_nums = (x*x for x in [1,2,3,4])		# this creates a generator e.g. 2nd example

# test
my_nums = square_num([1, 2, 3, 4])	# <generator object square_num at 0x1020ec0f0>
# print list(my_nums)					# you will get the same performance as when using a list - as you call all items here
print "Time took: ", time.time() - startT

# Generators do not hold the values in memory unless you call them. 



