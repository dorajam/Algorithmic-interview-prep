# Dora Jambor
# Making metaclasses as subclasses of 'type'

def trial():
	print "Hello there"

class doMagic(type):
	def __new__(cls, futureClass, parent, attr):
		attr['__add__'] = trial()
		getattr(__add__)
		return super(doMagic,cls).__new__(cls, futureClass, parent, attr)


		# magic_attr = {}
		# for name, val in attr.items():
		# 	if not name.startswith('__'):
		# 		if val == 2:
		# 			val = 2.5
		# 			magic_attr[name] = val
		# 	else:
		# 		magic_attr[name] = val
		# return super(doMagic,cls).__new__(cls, futureClass, parent, magic_attr)
	
	def __init__(cls, futureClass, parent, attr):
		print "This is working oh yey"

class Magic(object):
	__metaclass__ = doMagic
	def __init__(self):
		self.a = a

	def __add__(self, b):
		return self + b
		# if self.a == 2 & b == 2:
		# 	b = 3
		# 	print 'yo'
		# 	return self.a + b
		# else:
		# 	return self

print 4 + 5
print 2 + 2


