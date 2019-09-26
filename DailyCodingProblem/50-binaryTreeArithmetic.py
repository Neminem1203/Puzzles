'''
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
'''

class treeNode:
    val = None
    left = None
    right = None

    def __init__(self,val):
        self.val = val

arithTree = treeNode('*')
arithTree.left = treeNode('+')
arithTree.right = treeNode('+')
arithTree.left.left = treeNode('3')
arithTree.left.right = treeNode('2')
arithTree.right.left = treeNode('4')
arithTree.right.right = treeNode('5')

def arithmetic(tree):
    if(tree == None):
        return None
    expression = tree.val
    num1 = arithmetic(tree.left)
    num2 = arithmetic(tree.right)
    if expression == "+":
        return int(num1) + int(num2)
    elif expression == "-":
        return int(num1) - int(num2)
    elif expression == "*":
        return int(num1) * int(num2)
    elif expression == "/":
        return int(num1) / int(num2)
    else:
        return expression

print(arithmetic(arithTree))