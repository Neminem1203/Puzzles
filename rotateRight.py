
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    hare = head
    len = 0
    for i in range(k):
        if hare != None:
            len += 1
            hare = hare.next

    if(hare == None):
        k %= len
        if k == 0:
            return head
        hare = head
        for i in range(k):
            hare = hare.next

    tortoise = head
    while (hare.next != None):
        tortoise = tortoise.next
        hare = hare.next

    newhead = tortoise.next
    tortoise.next = None

    ptr = newhead
    while (ptr.next != None):
        ptr = ptr.next

    ptr.next = head

    return newhead

five = ListNode(5)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
head = ListNode(1, two)

test = rotateRight(head, 1)

while(test != None):
    print(test.val)
    test = test.next