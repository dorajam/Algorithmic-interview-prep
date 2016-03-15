# Dora Jambor
# Metaclass in Python - singleton.py

class MySingleton(object):
	_instance = None
	def __new__(self):
		# only if doesn't yet exist
		if not self._instance:
			self._instance = super(MySingleton, self).__new__(self)
			self.y = 10
		return self._instance

x = MySingleton()
print x.y 			# =10
x.y = 20
z = MySingleton()	# pointer at existing instance
print z.y 			# =20 now it points to the modified value of the instance we created earlier

# ---------------------- USING DECORATORS ----------------------

def singleton(myClass):
	instances = {}
	def getInstance(*args, **kwargs):
		if myClass not in instances:
			instances[myClass] = myClass(*args, **kwargs)
		return instances[myClass]
	return getInstance

@singleton
class Test(object):
	pass

x = Test()
x = 2
y = Test()
print y