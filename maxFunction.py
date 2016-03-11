# Dora Jambor
# Recurse Center, February 2016

'''
Implement the max function without using if statements, comparisons or functions.
Two numbers are given of 32 bits
'''

def maxFunc(a,b):
	c = a - b
	c >> 31 & 1
	return b*c + (a*(~c))

# test
print maxFunc(3,4)
