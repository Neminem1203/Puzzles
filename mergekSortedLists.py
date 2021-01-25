import time
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First Solution
# Second Solution Do a merge sort?
def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    ptrs = []
    for ll in lists:
        ptrs += [ll]  # create a list of all the ptrs so we can iterate through each list

    new_ll = ListNode(0)  # ptr we will return in the end
    ptr_new_ll = new_ll  # ptr we will use to build the list

    while True:  # hopefully there's never an infinite loop
        # # Debugging Purposes
        # for i in ptrs:
        #     if i:
        #         print(i.val, end=", ")
        #     else:
        #         print("None",end=", ")
        # print()
        # lul = new_ll
        # while lul:
        #     print(lul.val, end=", ")
        #     lul = lul.next
        # print()
        # time.sleep(1)


        smallest = -1  # smallest value index
        smallest_val = None  # smallest value found
        ind = 0

        while ind < len(ptrs):
            ptr = ptrs[ind]
            if ptr:  # if the ptr isn't None
                if smallest_val == None or ptr.val < smallest_val:  # checks for the smallest value between all the ptrs
                    smallest_val = ptr.val
                    smallest = ind
                ind += 1
            else:
                del(ptrs[ind])

        # If the list aren't empty
        if smallest_val != None:
            ptr_new_ll.next = ListNode(ptrs[smallest].val)
            ptr_new_ll = ptr_new_ll.next
            ptrs[smallest] = ptrs[smallest].next
        else:  # this only occurs when all the lists are empty
            break
    return new_ll.next  # I use the next because there's an empty node in the beginning

# Creating the lists [[1,4,5],[1,3,4],[2,6]]
first_list = ListNode(1, ListNode(4, ListNode(5)))
second_list = ListNode(1, ListNode(3, ListNode(4)))
third_list = ListNode(2, ListNode(6))
fourth_list  = ListNode(0, ListNode(2, ListNode(5)))

# new_head = mergeKLists([first_list, second_list, third_list]) # should come back with [1,1,2,3,4,4,5,6]

new_head = mergeKLists([fourth_list])

# print the new head
new_ptr = new_head
while new_ptr:
    print(new_ptr.val, end=", ")
    new_ptr = new_ptr.next


