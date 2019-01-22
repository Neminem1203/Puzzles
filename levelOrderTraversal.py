'''

Write a function to connect all the adjacent nodes at the same level in a binary tree. Structure of the given Binary Tree node is like following.

struct node{
  int data;
  struct node* left;
  struct node* right;
  struct node* nextRight;
}
Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.

Example

Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->NULL
      / \
     B-->C-->NULL
    / \   \
   D-->E-->F-->NULL
'''

class node:
    def __init__(self,val=None,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.nextRight = None


head = node('A', node('B', node('D'),node('E')),node('C', None, node('F')) )

def LOT(cur,prev=None, next=None):
    if(cur == None):
        return
    if(cur.left):
        if(prev):
            prev.nextRight = cur.left
        prev = cur.left
    if(cur.right):
        if(prev):
            prev.nextRight = cur.right
        prev = cur.right
    if(next):
        cur.nextRight = next
        LOT(next,prev)
    LOT(cur.left, prev,cur.right)

LOT(head)
# C, E, F
print(head.left.nextRight.val)
print(head.left.left.nextRight.val)
print(head.left.left.nextRight.nextRight.val)