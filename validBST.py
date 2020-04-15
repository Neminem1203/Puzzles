# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def helper(node, min=None, max=None):
        if node == None:
            return True
        left = False
        right = False

        if min == None or node.val >= min:
            left = helper(node.left, min, node.val)
        else:
            return False

        if max == None or node.val <= max:
            right = helper(node.right, node.val, max)
        else:
            return False
        return left and right

    return helper(head)


head = TreeNode(5)
lt = TreeNode(2)
rt = TreeNode(8)
llt = TreeNode(1)
lrt = TreeNode(3)
rlt = TreeNode(6)
rrt = TreeNode(10)
head.left = lt
head.right = rt
lt.left = llt
lt.right = lrt
rt.left = rlt
rt.right = rrt

#       5
#      /  \
#     2    8
#    / \  / \
#   1  3 6   10
print(isValidBST(head))  # True

newNode = TreeNode(4)
rlt.left = newNode
#       5
#      /  \
#     2    8
#    / \  / \
#   1  3 6   10
#       /
#      4
print(isValidBST(head))  # False
