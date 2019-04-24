'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
(1)  0
    / \
  (1) (0)
  / \
(1) (1)

*i circled the ones that are unival trees
*im also borrowing the Node class from previous day (serializeDeserialize)
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def univalTree(root):
    sum = 0
    leftExist = True if root.left else False
    rightExist = True if root.right else False
    if(leftExist and rightExist):
        if(root.val == root.left.val and root.val == root.right.val):
            sum += 1
        sum += univalTree(root.left)
        sum += univalTree(root.right)
        return sum
    elif(leftExist):
        if(root.val == root.left.val):
            sum += 1
        sum += univalTree(root.left)
        return sum
    elif(rightExist):
        if (root.val == root.right.val):
            sum += 1
        sum += univalTree(root.right)
        return sum
    else:
        return 1


testTree = Node(0, Node(1), Node(0, Node(1,Node(1), Node(1)), Node(0)))
print(univalTree(testTree))