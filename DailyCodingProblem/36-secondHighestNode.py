class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def insert(self, value):
        if(value > self.data):
            if(self.right):
                self.right.insert(value)
            else:
                newRight = node(value)
                self.right = newRight
        if (value < self.data):
            if (self.left):
                self.left.insert(value)
            else:
                newLeft = node(value)
                self.left = newLeft



def findSecondHighest(node):
    while(True):
        if(node.right.right == None):
            if(node.right.left == None):
                return node.data
            else:
                node = node.right.left
                while(node.right != None):
                    node = node.right
                return node.data
        else:
           node = node.right

headNode = node(5)
headNode.insert(10)
headNode.insert(6)
headNode.insert(7)
print(findSecondHighest(headNode))

headNode.insert(12)
print(findSecondHighest(headNode))

headNode.insert(8)
print(findSecondHighest(headNode))

headNode.insert(11)
print(findSecondHighest(headNode))

'''
    5
     \
      10
     /   \
    6     12
     \    /
      7  11
       \
        9
       /
      8
'''