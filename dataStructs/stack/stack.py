# Dora Jambor
# June 2016

# stack implementation + basic operations

class Node(object):
    def __init__(self, node=None, next_node = None):
        self.node = node
        self.next_node = next_node

    def get_val(self):
        return self.node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node


class Stack(object):
    def __init__(self, head = None, next_node = None):
        self.head = Node(head,next_node)

    def get_peek(self):
        return self.head

    def push(self,element):
        ''' pushes element on top of stack -> reset peek'''
        self.head = Node(element, self.head)

    def remove(self):
        self.head = self.head.get_next()

    def search(self,element):
        curr = self.head
        at = 1
        while curr:
            if curr.get_val() == element:
                return 'found element at: ', at
            curr = curr.get_next()
            at+=1
        return 'Not found'


stack = Stack(3)
stack.push(1)
stack.push(2)
# print stack.head.get_val()
# print stack.head.get_next().node
# stack.remove()
# print stack.head.get_val()
# print stack.head.get_next().node

print stack.search(2)

