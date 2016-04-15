# Dora Jambor
# Describe how you could use a single array to implement three stacks
# Stack: first in first out -> fixed size for stacks

class Stacker(object):
    def __init__(self, arr):
        self.arr = arr
        self.stack_size = len(arr) / 3
        self.start1 = arr[0]
        self.start2 = arr[self.stack_size]
        self.start3 = arr[2 *self.stack_size]
        self.size1 = 0
        self.size2 = 0
        self.size3 = 0

    def push_to_first(self, element):
        if self.size1 == self.stack_size:
            raise Exception('The stack is full!')
        self.arr[self.size1] = element
        self.size1 += 1
    def push_to_second(self,element):
        if self.size2 == self.stack_size:
            raise Exception('The stack is full!')
        self.arr[self.size2 + self.stack_size] = element
        self.size2 += 1
    def push_to_third(self,element):
        if self.size3 == self.stack_size:
            raise Exception('The stack is full!')
        self.arr[self.size3 + 2 * self.stack_size] = element
        self.size3 += 1


    def remove_from_first(self):
        if self.size1 == 0:
            raise Exception('The stack is empty!')
        self.size1 -= 1
        self.arr[self.size1] = 0
    def remove_from_second(self):
        if self.size2 == 0:
            raise Exception('The stack is empty!')
        self.size2 -= 1
        self.arr[self.size2 + self.stack_size] = 0
    def remove_from_third(self):
        if self.size3 == 0:
            raise Exception('The stack is empty!')
        self.size3 -= 1
        self.arr[self.size3 + 2 * self.stack_size] = 0
        



# test cases
stacker = Stacker([0,0,0,0,0,0,0,0,0])
stacker.push_to_first(1)
print stacker.arr
stacker.push_to_first(3)
print stacker.arr
stacker.push_to_first(2)
stacker.push_to_second(8)
stacker.push_to_second(6)
stacker.push_to_third(4)
print stacker.arr
stacker.remove_from_first()
stacker.remove_from_second()
print stacker.arr
