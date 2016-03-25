# Dora Jambor
# design stack with push, pop and min methods that operate in O(1) time each.

class Stack(object):
	def __init__(self):
		self.l = []
		self.min = 0
	def push(self, e):
		if self.l == []:
			self.min = e
			return self.l.append(e)
		if e <= self.min:
			self.min = e
		return self.l.append(e)
	def pop(self):
		return self.l.pop(-1)


stack = Stack()
stack.push(3)
print stack.l
stack.push(4)
stack.push(6)
stack.push(1)
print stack.l
stack.pop()
print stack.l,stack.min
