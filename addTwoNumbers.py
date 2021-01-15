# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val
        head = ListNode(val%10)
        nextNode = head
        overflow = 1 if val > 9 else 0
        p1 = l1.next
        p2 = l2.next
        while p1 != None or p2 != None:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            val = val1 + val2 + overflow
            nextNode.next = ListNode(val % 10)
            nextNode = nextNode.next
            overflow = 1 if val > 9 else 0
            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
        if overflow == 1:
            nextNode.next = ListNode(1)
        return head