# ---------------------- MAGIC METHODS ----------------------

'''One distinctive feature of Python is magic methods: 
they allow the programmer to override behavior for various 
operators and behavior of objects. To override the call 
operator you'd do this:'''
# create a class object of type called Funky
class Funky:
	def __call__(self):
		print "Let's modify the behavior of this object yeyy"

f = Funky()   # create an instance of class Funky
print type(f)
print type(Funky)
f()