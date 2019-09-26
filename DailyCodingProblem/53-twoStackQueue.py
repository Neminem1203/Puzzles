'''
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

class node:
    val = None
    below = None

    def __init__(self, val):
        self.val = val

class stack:
    topOfStack = None

    def __init__(self, val = None):
        if(val):
            newNode = node(val)
            self.topOfStack = newNode

    def push(self, val):
        if(val == None):
            return
        newNode = node(val)
        if(self.topOfStack == None):
            self.topOfStack = newNode
            return
        else:
            oldTop = self.topOfStack
            self.topOfStack = newNode
            self.topOfStack.below = oldTop
            return

    def pop(self):
        if(self.topOfStack == None):
            return None
        returnVal = self.topOfStack.val
        newTop = self.topOfStack.below
        del self.topOfStack
        self.topOfStack = newTop
        return returnVal


class queue:
    stacks = [stack(), stack()] #first stack is the queue, second is temporary

    def __init__(self):
        return

    def enqueue(self,val):
        self.stacks[0].push(val)

    def dequeue(self):
        value = self.stacks[0].pop()
        while(value != None):
            self.stacks[1].push(value)
            value = self.stacks[0].pop()
        returnVal = self.stacks[1].pop()
        value = self.stacks[1].pop()
        while(value != None):
            self.stacks[0].push(value)
            value = self.stacks[1].pop()
        return returnVal

    def print(self):
        value = self.stacks[0].pop()
        while(value != None):
            self.stacks[1].push(value)
            value = self.stacks[0].pop()
        value = self.stacks[1].pop()
        print("Queue:   ",end="")
        while(value != None):
            print(value, end=" ")
            self.stacks[0].push(value)
            value = self.stacks[1].pop()
        print()


testQueue = queue()
testQueue.enqueue(4)
testQueue.enqueue(6)
testQueue.enqueue(8)
testQueue.enqueue(3)
testQueue.enqueue(7)
testQueue.print()
popped = testQueue.dequeue()
while(popped):
    print("Dequeue:", popped)
    testQueue.print()
    popped = testQueue.dequeue()

print("Dequeue:", popped)