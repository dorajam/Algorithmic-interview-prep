# Dora Jambor
# June 2016

# to test
from isValid import *

def second(root, largest=root.value, secondlargest=root.value):
    if node.right:
        if not left_taken:
            largest= node.right
        else:
            secondLargest=node.right
    elif node.left:
        if not left_taken:
            secondLargest = node.left
            left_taken = True
        else:
            return secondLargest
    else:
        return secondLargest
    second(node, largest,secondLargest, left_taken)
print second(tree)
n
