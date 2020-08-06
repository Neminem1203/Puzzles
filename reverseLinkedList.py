'''
Given the head of a singly linked list, reverse it in-place.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


fifth = Node(5)
fourth = Node(4,fifth)
third = Node(3, fourth)
second = Node(2, third)
first = Node(1, second)
zero = Node(0, first)

def printLinkedList(head):
    ptr = head
    while ptr != None:
        print(ptr.value, end=", ")
        ptr = ptr.next
    print()

def reverseLinkedList(head):
    prev = None
    ptr = head
    next = head.next
    while ptr != None:
        ptr.next = prev
        prev = ptr
        ptr = next
        if next != None:
            next = next.next
    return prev

print("Old Head: ",end="")
printLinkedList(zero)
print("New Head: ",end="")
newHead = reverseLinkedList(zero)
printLinkedList(newHead)
print("Old Head: ",end="")
printLinkedList(zero)