# Dora Jambor
# Multiple inheritence and super()


print '-------------------------- SINGLE INHERITENCE -----------------------------'
# 
class A(object):
	def __init__(self):
		print "We are in A"
		self.x = 5
		print self.x


class B(A):
	def __init__(self):
		print "We are in B"
		self.x = 6
		print self.x
		super(B,self).__init__()
		print "Go to parent"


class C(B):
	def __init__(self):
		print "We are in C"
		self.x = 7
		print self.x
		super(C,self).__init__()		# goes through the inheritence tree up to the Parent
		print "After visiting parent"
		print self.x

C().x

print '-------------------------- MULTIPLE INHERITENCE -----------------------------'

class A(object):
	def __init__(self):
		print "We are in A"
		self.x = 5
		print self.x


class B():
	def __init__(self):
		print "We are in B"
		self.x = 6
		print self.x


class C(A,B):
	def __init__(self):
		print "We are in C"
		self.x = 7
		print self.x
		super(C,self).__init__()	# super will just ignore the 2nd inheritence arg
		print "After visiting parent"
		print self.x

C().x