# ---------------------- MAGIC METHODS ----------------------

'''One distinctive feature of Python is magic methods: 
they allow the programmer to override behavior for various 
operators and behavior of objects. To override the call 
operator you'd do this:'''

# create a class object of type called Funky
class Funky:
	def __call__(self):
		print "Let's modify the behavior of this object yeyy"
	def something(self):
		print "do something"

f = Funky()   # create an instance of class Funky
print Funky.__dict__	# {'__call__': <function __call__ at 0x1020e7e60>, '__module__': '__main__', 'something': <function something at 0x1020e7ed8>, '__doc__': None}
print Funky.__dict__['something']	# lookup to the memory address of function
# print f.__dict__['something']		# keyerror for something
print type(f)
print type(Funky)
f()

# ---------------------- METACLASSES AS CALLABLES ----------------------
class Foo():
	print "Hello world"

print type(Foo)
f = Foo()
print type(f)
print super(type(Foo))