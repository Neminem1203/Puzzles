'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
'''

class node:
    val = ""
    left = None
    right = None

    def __init__(self,val):
        self.val = val


def preorder_traversal(node):
    if(node == None):
        return []
    retArr = [node.val]
    retArr += preorder_traversal(node.left)
    retArr += preorder_traversal(node.right)
    return retArr

def inorder_traversal(node):
    if(node == None):
        return []
    retArr = inorder_traversal(node.left)
    retArr += [node.val]
    retArr += inorder_traversal(node.right)
    return retArr



def recreateTree(preorder, inorder):
    if(preorder == []):
        return None
    newNode = node(preorder[0])
    center = None
    for ind in range(len(inorder)):
        if(inorder[ind] == preorder[0]):
            center = ind
            break
    # print(preorder[1:center+1], inorder[:center])
    # print(preorder[center+1:], inorder[center+1:])
    leftTree = recreateTree(preorder[1:center+1], inorder[:center])
    rightTree = recreateTree(preorder[center+1:], inorder[center+1:])
    newNode.left = leftTree
    newNode.right = rightTree
    return newNode



'''
preorder    [a, b, d, e, c, f, g]
inorder     [d, b, e, a, f, c, g]
    Tree
    a
   / \
  b   c
 / \ / \
d  e f  g
'''
# original tree
treeHead = node('a')
treeHead.left = node('b')
treeHead.left.left = node('d')
treeHead.left.right = node('e')
treeHead.right = node('c')
treeHead.right.left = node('f')
treeHead.right.right = node('g')

preorder = preorder_traversal(treeHead)
inorder = inorder_traversal(treeHead)

recreation = recreateTree(preorder, inorder)
print(preorder, end=" == ")
print(preorder_traversal(recreation))
print(preorder_traversal(treeHead)==preorder_traversal(recreation))
print(inorder, end=" == ")
print(inorder_traversal(recreation))
print(inorder_traversal(treeHead)==inorder_traversal(recreation))
