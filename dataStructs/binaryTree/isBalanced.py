# check if a binary tree is balanced => that is, if the difference of depths of any given node is not larger than one.
import isValid


def isLeaf(root):
    return not (root.right or root.left)

def getDepth(root):
    if not root:
        return 0
    depth = 0
    if isLeaf(root):
        return depth
    depth += 1
    return depth + max(getDepth(root.right), getDepth(root.left))

def isBalanced(root):
    if isLeaf(root):
        return True
    return abs(getDepth(root.right) - getDepth(root.left)) <= 1

# to test
print isBalanced(isValid.tree)
