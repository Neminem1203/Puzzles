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
            
string representation: (((()left.left())left())root(()right()))

with this, '(' and ')' are illegal characters for value in tree
            this can be changed under the class Node (leftBracket, rightBracket)

'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

leftBracket = "("
rightBracket = ")"

# tree - > string
def serialize(node):
    returnstring = ""
    if(node.left):
        returnstring += serialize(node.left)
    else:
        returnstring += "()"
    returnstring+=node.val
    if(node.right):
        returnstring += serialize(node.right)
    else:
        returnstring += "()"
    return leftBracket+returnstring+rightBracket

def deserialize(strng):
    if(strng == "()"):
        return None
    brackets = []
    for i in range(len(strng)):
        if(strng[i] == "("):
            brackets.append([i, -1])
        if(strng[i] == ")"):
            for ind in range(len(brackets)-1, -1, -1):
                if(brackets[ind][1] == -1):
                    brackets[ind][1] = i
                    break
    rB = brackets[1][1] # rB = right Brackets
    for i in range(len(brackets)):
        if rB < brackets[i][0]:
            rB = i
            break
    mainNode = Node(strng[brackets[1][1]+1:brackets[rB][0]],
                deserialize(strng[brackets[1][0]:brackets[1][1]+1]),
                deserialize(strng[brackets[rB][0]:brackets[rB][1]+1]))
    return mainNode






# Main Function

node = Node('root', Node('left', Node('left.left')), Node('right'))
# testnode = Node('root', Node('left', Node('left.left'), Node('left.right',Node('left.right.left'))),Node('right', Node('right.left'), Node('right.right')))
strrep = serialize(node)
tree = deserialize(strrep)


assert deserialize(serialize(node)).left.left.val == 'left.left'
