'''
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''
class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class stack:
    highest_num_stack = None
    top_of_stack = None

    def __init__(self,val):
        self.top_of_stack = node(val)
        self.highest_num_stack = node(val)

    def push(self, val):
        if(val >= self.top_of_stack.val):
            newHighestNode = node(val)
            newHighestNode.next = self.highest_num_stack
            self.highest_num_stack = newHighestNode

        newNode = node(val)
        newNode.next = self.top_of_stack
        self.top_of_stack = newNode

    def pop(self):
        if(self.top_of_stack == None):
            return None
        if(self.top_of_stack.val == self.highest_num_stack.val):
            newHighest = self.highest_num_stack.next
            del self.highest_num_stack
            self.highest_num_stack = newHighest

        newTop = self.top_of_stack.next
        retVal = self.top_of_stack.val
        del self.top_of_stack
        self.top_of_stack = newTop
        return retVal


    def max(self):
        if(self.highest_num_stack == None):
            return None
        return self.highest_num_stack.val

                                                # V = Top of Stack
newStack = stack(5)                             # 5
newStack.push(3)                                # 3, 5
newStack.push(7)                                # 7, 3, 5
print(newStack.max())
newStack.pop()                                  # 3. 5
print(newStack.max())
newStack.push(10)                               # 10, 3, 5
newStack.push(10)                               # 10, 10, 3, 5
print(newStack.max())
newStack.pop()                                  # 10, 3, 5
print(newStack.max())
newStack.pop()                                  # 3, 5
print(newStack.max())
newStack.push(32)                               # 32, 3, 5
newStack.push(10)                               # 10, 32, 3, 5
newStack.push(55)                               # 55, 10, 32, 3, 5
print(newStack.max())
newStack.pop()                                  # 10, 32, 3, 5
print(newStack.max())