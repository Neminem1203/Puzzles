'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def insert(self,val):
        nodePtr = self
        while(nodePtr.next != None):
            nodePtr = nodePtr.next
        nodePtr.next = node(val)

linkedList = node(3)
linkedList.insert(7)
linkedList.insert(8)
linkedList.insert(10)

linkedList2 = node(99)
linkedList2.insert(5)
linkedList2.insert(1)
linkedList2.next.next.next = linkedList.next.next


def intersectingNode(header1, header2):
    head1 = header1
    head2 = header2
    lenDiff = 0
    while(head1.next != None and head2.next != None):
        head1 = head1.next
        head2 = head2.next
    if(head2.next != None):
        while(head2.next != None):
            lenDiff += 1
            head2 = head2.next
    if(head1.next != None):
        while (head1.next != None):
            lenDiff -= 1
            head1 = head1.next
    head1 = header1
    head2 = header2
    while(lenDiff > 0):
        head2 = head2.next
        lenDiff -= 1
    while(lenDiff < 0):
        head1 = head1.next
        lenDiff += 1

    while(head1 != None):
        if(head1.val == head2.val):
            return head1.val
        head1 = head1.next
        head2 = head2.next
    return None

print(intersectingNode(linkedList, linkedList2))