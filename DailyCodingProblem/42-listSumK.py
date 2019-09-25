'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''

class linkedList:
    val = None
    next = None
    def __init__(self, val=None):
        self.val = val

    # for debugging purposes
    def print(self):
        print(self.val,end="")
        if(self.next != None):
            print("",end=", ")
            self.next.print()
        else:
            print()

    # Reverse order sorting of a list
    def insert(self, val):
        if(self.val == None): # empty linked list
            self.val = val
            return
        elif(self.val < val): # the val belongs here so we push the current val forward
            oldVal = self.val
            self.val = val
            newNode = linkedList(oldVal)
            newNode.next = self.next
            self.next = newNode
            return
        elif(self.next == None): # end of the list
            self.next = linkedList(val)
            return
        else: # continue
            self.next.insert(val)

    def returnArray(self, arr=[]):
        arr = arr + [self.val]
        if(self.next != None):
            return self.next.returnArray(arr)
        else:
            return arr



def listSumK(list, k):
    def testList(remainingList, list, sumOfList, k):
        if(remainingList == []):
            return None
        elif(sumOfList == k):
            return list

        if(sumOfList + remainingList[0] > k):
            return None
        sumOfList += remainingList[0]
        list += [remainingList[0]]
        if(sumOfList == k):
            return list
        remainingList = remainingList[1:]
        for index in range(len(remainingList)):
            retList = testList(remainingList[index:], list, sumOfList, k)
            if(retList != None):
                return retList
        return None


    sortedList = linkedList()
    for i in list:
        if(i < k):
            sortedList.insert(i)
    sortedArray = sortedList.returnArray()
    for index in range(len(sortedArray)):
        retList = testList(sortedArray[index:], [], 0, k)
        if(retList != None):
            return retList




list = [12, 1, 61, 5, 9, 2]
print(listSumK(list, 24))
list = [12, 1, 25, 5, 9, 2]
print(listSumK(list, 32))