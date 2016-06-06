class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# import ipdb; ipdb.set_trace()

def isValid(root, lower = -float('inf'), upper = float('inf')):
    ''' A binary search tree is valid if the left node is always less than, and the right node is always greater than the parent node'''
    if not root:
        return True

    print root.value
    if (root.value < lower or root.value > upper):
        return False

    return isValid(root.left, lower, root.value) and isValid(root.right, root.value, upper)



tree = BinaryTreeNode(10)
left = tree.insert_left(5)
# right = tree.insert_right(15)
leftleft = left.insert_left(2)
# leftright = left.insert_right(6)
# leftright = leftleft.insert_right(6)
# rightleft = right.insert_left(13)
# rightright = right.insert_right(17)
# rightright = rightright.insert_left(12)

print isValid(tree)
