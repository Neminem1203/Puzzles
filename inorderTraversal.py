# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversalRecur(root): # Recursive
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if(root == None):
        return []
    in_order = inorderTraversalRecur(root.left)
    in_order += [root.val]
    in_order += inorderTraversalRecur(root.right)
    return in_order

def inorderTraversalIter(root):
    stack = [root.left]



RL = TreeNode(3)
R = TreeNode(2, RL)
HEAD = TreeNode(1, None, R)
print(inorderTraversalRecur(HEAD))