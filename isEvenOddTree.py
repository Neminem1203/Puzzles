# https://leetcode.com/problems/even-odd-tree/submissions/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isEvenOddTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    nodes = [root]
    level = 0
    while len(nodes) != 0:
        prev = nodes[0].val  # checking previous number
        ind = 1  # index of nodes

        if level % 2 == 0:  # if level is even, only odd numbers
            if prev % 2 == 0:  # check the first node if it's not odd
                return False
            while ind < len(nodes):
                if nodes[ind].val % 2 == 0 or prev >= nodes[ind].val:
                    return False
                prev = nodes[ind].val
                ind += 1

        else:
            if prev % 2 == 1:  # check the first node if its not even
                return False
            while ind < len(nodes):
                if nodes[ind].val % 2 == 1 or prev <= nodes[ind].val:
                    return False
                prev = nodes[ind].val
                ind += 1

        # go to next level
        level += 1
        level_len = len(nodes)
        counter = 0
        while counter < level_len:
            node = nodes[0]
            nodes = nodes[1:]
            # checks whether they have a left and right child and push it to the array
            if node.left != None:
                nodes.append(node.left)
            if node.right != None:
                nodes.append(node.right)
            counter += 1
    return True
