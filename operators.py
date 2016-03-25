# Dora Jambor
# implement multiply, subtrack, devide by only using add

def multiply(a,b):
	if a==0 | b==0:
		return 0
	if b == 1 | b == -1:
		return a

	if (a >= 0 & b >=0) | (a < 0 & b < 0):
		b = abs(b)
		return a + multiply(a,b-1)
	else:
		a = abs(a)
		b = abs(b)
	return -(a + multiply(a,b-1))

def subtract(a,b):
	b = -b
	return a + b

def devide(a,b):
	res = 0
	c = abs(a)
	d = abs(b)
	if d == 0: 
		raise ZeroDivisionError
	while True:
		if d * res == c:
			break
		elif d*res > c:	
			break
		else:
			res += 1
	if d*res == c:
		if a<0 & b<0 | a>=0 & b>=0:
			return res
		else:
			return -res
	if d*res > c:
		res = res - 1
		if a<0 & b<0 | a>=0 & b>=0:
			return res
		else:
			return -res

# print devide(-40,3)
# print devide(3,-4)
# print devide(0,3)
# # print devide(3,0)

print multiply(3,4)
print multiply(3,-4)
print multiply(-3,4)
print multiply(-3,-4)
print multiply(0,1)
print multiply(1,0)