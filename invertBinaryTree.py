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

    def insert(self, value):

        if(self.value < value):
            if(self.right == None):
                newNode = bTNode(value)
                self.right = newNode
                return True
            else:
                self.right.insert(value)
        if(self.value > value):
            if(self.left == None):
                newNode = bTNode(value)
                self.left = newNode
                return True
            else:
                self.left.insert(value)
        return

    def show(self):
        if(self.left):
            self.left.show()
        print(self.value,end = ' ')
        if(self.right):
            self.right.show()

    def reverseTree(self):
        lNPresent = True if self.left else False
        rNPresent = True if self.right else False

        if(lNPresent and rNPresent):
            nodeLeft = self.left
            self.left = self.right
            self.right = nodeLeft
            self.left.reverseTree()
            self.right.reverseTree()
        elif(lNPresent and not rNPresent):
            self.right = self.left
            self.left = None
            self.right.reverseTree()
        elif(rNPresent and not lNPresent):
            self.left = self.right
            self.right = None
            self.left.reverseTree()
        else:
            return True



headNode = bTNode(4)
headNode.insert(2)
headNode.insert(3)
headNode.insert(1)
headNode.insert(7)
headNode.insert(6)
headNode.insert(9)

headNode.show()
headNode.reverseTree()
print()
headNode.show()