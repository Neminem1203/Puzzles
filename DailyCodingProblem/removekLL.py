'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''
import random
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



def removeKFromLL(LL, K):
    point = LL
    while(K>0):
        point = point.next
        K-=1
    behindPointer = LL
    while(point.next):
        point = point.next
        behindPointer = behindPointer.next
    return behindPointer.value


zelda = linkedList(random.randint(1, 1000))

listLen = 100
findK = 25
if(findK == listLen):
    print("ANSWER: ", end=" ")
    print(zelda.value)
for i in range(listLen):
    randomNum = random.randint(1, 1000)
    if(i == listLen-findK-1):
        print("ANSWER: ",end=" ")
        print(randomNum)
    zelda.insert(randomNum)
print()
print(removeKFromLL(zelda, findK))