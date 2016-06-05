# Dora Jambor
# Single Linked List: a linked list is a data structure that consists of vertices that together represent a sequence.
# Each vertex is composed of some data and a reference (link) to the next vertex in the sequence.


class Node(object):
    def __init__(self, value=None, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_val(self):
        return self.value

    def get_next(self):
        return self.next_node 

    def set_next(self, node):
        self.next_node = node


head = 5
# linkedlist = [5,3,4,5,6]

# linkedList = Node(head)
# print linkedList.get_val()
# print linkedList.next_node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(head)

    def insert(self,node):
        ''' pushed new node to the front -> reset head '''
        new_node = Node(node, self.head)
        # new_node.set_next = head
        self.head = new_node

    def insert_at(self,element,index):
        current  = self.head
        prev = None
        while index != 0:
            print 'currently looking at: ', current.get_val()
            prev = current
            current = current.get_next()
            index -= 1
        new_node = Node(element,current)
        prev = new_node
        # print prev.get_val(), current.get_val()

    def get_size(self):
        counter = 1
        while self.head.get_next():
            self.head = self.head.get_next()
            counter += 1
        return counter

    def search(self, element):
        current = self.head
        location = 1
        while current:
            if current.get_val() == element:
                return 'Found node at: ', current, location
            current = current.get_next()
            location +=1
        raise ValueError('Element is not in the list')

    def delete(self, element):
        # 3,4,5 -> look for 4
        current = self.head
        if current.get_val() == element:
            self.head = current.get_next()
            return 'The new head is: ', head.get_val()
        prev_node_pointer = current
        current = current.get_next()

        while current:
            if current.get_val() == element:
                tmp = current.get_next()
                prev_node_pointer.next_node = tmp
                return current.get_val()
            prev_node_pointer = current
            current = current.get_next()
        return "Element wasn't found"



ll = LinkedList(3)
ll.insert(4)
ll.insert(7)
ll.insert(9)
print ll.head.value
print ll.head.get_next().value
# print ll.get_size()
print 'searching...', ll.search(3)
print 'deleting...', ll.delete(3)

ll.insert_at(5, 2)

