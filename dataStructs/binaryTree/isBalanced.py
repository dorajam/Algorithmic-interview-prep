# check if a binary tree is balanced => that is, if the difference of depths of any given node is not larger than one.
import isValid


def isLeaf(root):
    if not root:
        return True
    return False

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
    if abs(getDepth(root.right) - getDepth(root.left)) > 1:
        return False
    return isBalanced(root.right) and isBalanced(root.left)

# to test
print isBalanced(isValid.tree)
