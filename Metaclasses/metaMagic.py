# Dora Jambor
# Making metaclasses as subclasses of 'type'

'''
type.__new__(meta, cls, bases, attributes) will set the 
correct metaclass (which is MyMeta) for MyClass
type(cls, bases, attributes) will set the default metaclass (which is type) for MyClass
'''

class Meta(type):
	def __new__(cls, name, bases, dict):
		print "Meta.__new__ is called"
		return type(name, bases, dict)
	def __init__(cls,name, bases, dict):
		print "Meta.__init__ is called"

class A(object):
	__metaclass__ = Meta 	# this will intialize the metaclass using __new__ --> type
	def __init__(self):
		print 'Yo'

# check how class A is created ---> " Meta.__new__ is called"
# that means that you're creating a whole new class with __new__,
# but it still follows the instructions given in type
# type(A) --> <type 'type' >

print ' ---------------------------- Next ------------------------------'

class MetaMagic(type):
	def __new__(cls, name, bases, dict):
		print "Meta.__new__ is called"
		return type.__new__(cls,name, bases, dict)	# type.__new__ OVERRIDES TYPE HERE!!!
	def __init__(cls,name, bases, dict):
		print "Meta.__init__ is called"

class B(object):
	__metaclass__ = MetaMagic
	def __init__(self):
		print 'Yolo'

# check how class B is created ---> " Meta.__new__ is called" and "Meta.__init__ is called"
# that means that you're creating a whole new class with __new__,
# but it still follows the instructions given in type
# type(B) --> <class '__main__.MetaMagic'>

