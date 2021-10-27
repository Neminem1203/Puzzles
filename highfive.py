'''
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
'''

LIMIT = 5

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, val, level=0):
        if level > LIMIT:
            return

        if self.val < val:
            newNext = Node(self.val)
            oldNext = self.next
            newNext.next = oldNext
            self.next = newNext
            self.val = val
        elif self.next == None:
            newNext = Node(val)
            self.next = newNext
        else:
            self.next.insert(val, level+1)

    def print(self):
        print(self.val, end=" ")
        if self.next == None:
            print()
        else:
            self.next.print()

    def firstNSum(self, n, level=1):
        if level > n:
            return 0

        if self.next:
            return self.val+self.next.firstNSum(n, level+1)
        else:
            return self.val

def highfiveLL(scores):
    students = {}
    for id, score in scores: # O(n)
        if id not in students:
            students[id] = Node(0)
        students[id].insert(score)

    averages = []
    for id in students:
        averages.append([id, int(students[id].firstNSum(5)/5)])
    print(averages)




#######################################################################
class sortedArray:
    def __init__(self, array=[],limit = None):
        self.arr = []
        self.limit = limit
        for i in array:
            self.insert(i)

    def insert(self, val):
        ind = 0
        while ind < len(self.arr):
            if val > self.arr[ind]:
                break
            ind += 1
        self.arr.insert(ind, val)
        if self.limit != None:
            while len(self.arr) > self.limit:
                self.arr.pop()

def highfive(scores):
    students = {}
    for id, score in scores: # O(n)
        if id not in students:
            students[id] = sortedArray([], LIMIT)
        students[id].insert(score) #O(6)

    averages = []
    for id in students:
        average = 0
        for score in students[id].arr:
            average += score
        average = int(average/len(students[id].arr))
        averages.append([id, average])
    return averages


tests = [[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]]

for test in tests:
    print(highfive(test))
    print(highfiveLL(test))


