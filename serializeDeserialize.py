'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

'''
                tree
            representation
            
                root
               /   |
              left  right
             /
            left.left
            
string representation: (((-left.left-)-left-)-root-(-right-))

with this, '(', ')' and '-' are illegal characters for value in tree
            this can be changed in serialize (leftBracket, rightBracket, connector)

'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# tree - > string
def serialize(node):
    connector = "-"
    leftBracket = "("
    rightBracket = ")"

    returnstring = ""
    if(node.left):
        returnstring += serialize(node.left)
    returnstring+=connector+node.val+connector
    if(node.right):
        returnstring += serialize(node.right)
    return leftBracket+returnstring+rightBracket

def deserialize(strng):
    brackets = []
    for i in range(len(strng)):
        if(strng[i] == "("):
            brackets.append([i, -1])
        if(strng[i] == ")"):
            for ind in range(len(brackets)-1, -1, -1):
                if(brackets[ind][1] == -1):
                    brackets[ind][1] = i
                    break
    '''
    IDEA 1
    build tree from bottom up.
    (-val-) = a leaf node
    anything else you parse
    for example ((-left.left-)-left-((-left.right.left-)-left.right-))
    (-left.left-) is created as left's left node
    parse right with same function
    (-left.right.left-) is a leaf node
    create it as left of left.right
    
    sidenote1:
    could add () as None to make it easier?
    (()-val-()) = leaf node
    
    IDEA 2
    deserialize entire string
    brackets[0] = full tree
    if(brackets[1][0] == brackets[0][0]+1 (left node is brackets[1][0]:brackets[1][1])
    deserialize(brackets[1][0]:brackets[1][1])
    middle is value
    check if the right node exists (does another set of brackets exist after leftNodes rightmost value (> brackets[1][1])
    if yes: deserialize(rightNode)
    
    sidenote2:
    this way we dont have to make use of sidenote1
    maybe can still implement sidenote1?
    '''
    print(brackets)







node = Node('root', Node('left', Node('left.left')), Node('right'))
testnode = Node('root', Node('left', Node('left.left'), Node('left.right',Node('left.right.left'))),Node('right', Node('right.left'), Node('right.right')))
strrep = serialize(node)
print(strrep)
strrep=serialize(testnode)
print(strrep)
for i in range(0, len(strrep), 10):
    for j in range(5):
        print("X",end="")
    for j in range(5):
        print("O", end="")
print("")


tree = deserialize(strrep)

# assert deserialize(serialize(node)).left.left.val == 'left.left'
