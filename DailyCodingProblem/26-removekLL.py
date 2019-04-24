'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''
import random
verbose = True
listLen = 100
findK = 10
ind = listLen-findK-1
min = 0
max = 1000
class linkedList:

    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        if(self.next):
            self.next.insert(value)
        else:
            newNode = linkedList(value)
            self.next = newNode

    def valueAtX(self, X):
        pointer = self
        while(X>0):
            pointer = pointer.next
            X-=1
        return pointer.value



def removeKFromLL(LL, K):
    point = LL
    while(K>0):
        point = point.next
        K-=1
    point = point.next
    behindPointer = LL
    while(point.next):
        point = point.next
        behindPointer = behindPointer.next
    valueRemoved = behindPointer.next.value
    nextPointer = behindPointer.next.next
    del behindPointer.next
    behindPointer.next = nextPointer
    return valueRemoved


zelda = linkedList(random.randint(min, max))
if(verbose):
    print("0: ", zelda.value)
for i in range(1,listLen):
    randomNum = random.randint(min, max)
    if(verbose):
        if(i == ind):
            print(i,": ",randomNum, " < ANSWER")
        else:
            print(i,": ",randomNum)
    zelda.insert(randomNum)
print("Index", ind,"Before: ",zelda.valueAtX(ind))
if(verbose):
    print("Removed ",removeKFromLL(zelda, findK))
else:
    removeKFromLL(zelda, findK)
if(findK != 0):
    print("Index", ind,"After: ",zelda.valueAtX(ind))