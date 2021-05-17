# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    """
    :type head: ListNode
    :rtype: int
    """
    val, ptr = 0, head
    while ptr:
        val *= 2
        if ptr.val == 1:
            val += 1
        ptr = ptr.next
    return val