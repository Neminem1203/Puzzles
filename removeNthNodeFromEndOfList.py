# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # move ahead in the list to see how far we are from the end
    ahead = head
    for i in range(n+1):
        ahead = ahead.next

    # this is going to be the node just before the one we skip
    ptr = head
    while(ahead != None):
        ptr = ptr.next
        ahead = ahead.next
    # set ptrs next to the next next node (we're skipping the next node)
    ptr.next = ptr.next.next
    return head


def printList(head):
    ptr = head
    arr = []
    while(ptr != None):
        arr += [ptr.val]
        ptr = ptr.next
    print(arr)


# setup nodes
first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
# setup connections
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
# Print List First
printList(first)
# remove nth item
removeNthFromEnd(first, 2)
# reprint list
printList(first)