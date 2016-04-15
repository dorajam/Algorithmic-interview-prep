# Dora Jambor
# Create a program that creates a new stack if the stack size exceed a threshold level. Make sure the stack behavies in the same way if you need to pop the last element

class SetOfStacks(object):
    def __init__(self):
        self.stack = []
        self.thres = 2
        self.current_size = 0
        self.counter = 0
        self.list_of_stacks = []

    def push(self, element):
        if self.current_size < self.thres:
            self.stack.append(element)
            self.current_size += 1
        elif self.current_size == self.thres:
            self.list_of_stacks.append(self.stack)
            self.stack = [element]
            self.current_size = 1
            self.counter += 1

    def pop(self):
        if self.current_size == 0 and self.counter == 0:
            raise Exception('The stack is empty!')
        if self.current_size == 0:
            self.getLastStack()
            self.list_of_stacks.pop()
            self.counter -= 1
        self.current_size -=1
        print self.stack.pop()

    def getLastStack(self):
        self.stack = self.list_of_stacks[-1]

    def popAt(self, index):
        if index == self.counter:
            self.pop()
        print self.list_of_stacks[index].pop()

# ---------------- test cases ----------------
# stacks = SetOfStacks()
# stacks.push(1)
# stacks.push(2)
# print stacks.stack
# print stacks.list_of_stacks
# stacks.push(3)
# stacks.push(4)
# stacks.push(5)
# stacks.push(5)
# stacks.push(6)
# stacks.push(6)
# print stacks.stack
# print stacks.list_of_stacks
# # stacks.pop()
# print stacks.stack
# print stacks.list_of_stacks
# stacks.popAt(1)
# print stacks.stack
# print stacks.list_of_stacks
