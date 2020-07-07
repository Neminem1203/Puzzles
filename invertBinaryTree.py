'''
https://leetcode.com/articles/invert-binary-tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
class bTNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insert(self, value):
    #
    #     if(self.value < value):
    #         if(self.right == None):
    #             newNode = bTNode(value)
    #             self.right = newNode
    #             return True
    #         else:
    #             self.right.insert(value)
    #     if(self.value > value):
    #         if(self.left == None):
    #             newNode = bTNode(value)
    #             self.left = newNode
    #             return True
    #         else:
    #             self.left.insert(value)
    #     return

    def show(self):
        if(self.left):
            self.left.show()
        print(self.value,end = ' ')
        if(self.right):
            self.right.show()

    def reverseTree(self):
        oldLeft = self.left
        oldRight = self.right
        self.right = oldLeft
        self.left = oldRight
        if(self.left != None):
            self.left.reverseTree()
        if(self.right != None):
            self.right.reverseTree()



headNode = bTNode(4)
headNode.left = bTNode(2)
headNode.left.right = bTNode(3)
headNode.left.left = bTNode(1)
headNode.right = bTNode(7)
headNode.right.left = bTNode(6)
headNode.right.right = bTNode(9)

headNode.show()
headNode.reverseTree()
print()
headNode.show()