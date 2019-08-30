'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

class linkedList:
    val = ""
    next = None
    def __init__(self, val):
        self.val = val

    def print(self):
        print(self.val,end="")
        if(self.next != None):
            print("",end=", ")
            self.next.print()
        else:
            print()

    def insert(self, val):
        if(self.next == None):
            if(self.val == None):
                self.val = val
                return
            self.next = linkedList(val)
        else:
            self.next.insert(val)

    # alphabetical insert
    def aInsert(self, val):
        if(val < self.val):
            newLink = linkedList(self.val)
            self.val = val
            self.next = newLink
        else:
            if(self.next == None):
                self.next = linkedList(val)
            else:
                self.next.insert(val)

    # array insert
    # def insert(self, arrayVal):
    #     if(arrayVal == []):
    #         return
    #     if(self.next == None):
    #         reference = self
    #         for i in arrayVal:
    #             reference.next = linkedList(i)
    #             reference = reference.next
    #     else:
    #         self.next.insert(arrayVal)

    def pop(self):
        # if(self.next == None):
        #     retVal = self.val
        #     self.val = None
        #     return retVal
        if(self.next.next == None):
            retVal = "" + self.next.val
            del(self.next)
            return(retVal)
        else:
            return(self.next.pop())


def flightItinerary(flights, origin):
    

flightItinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')