'''
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''
class node:
    val = None
    next = None

    def __init__(self, val):
        self.val = val

class queue:
    first = None

    def __init__(self,val=None):
        if(val):
            newNode = node(val)
            self.first = newNode

    def push(self, val):
        if(self.first == None):
            newNode = node(val)
            self.first = newNode
            return
        ptr = self.first
        while(ptr.next != None):
            if(ptr.val == val):
                newNext = ptr.next.next
                ptr.val = ptr.next.val
                del ptr.next
                ptr.next = newNext
            else:
                ptr = ptr.next
        newNode = node(val)
        ptr.next = newNode

    def pop(self):
        if(self.first == None):
            return None
        newFirst = self.first.next
        returnVal = self.first.val
        del self.first
        self.first = newFirst
        return returnVal

    def print(self):
        ptr = self.first
        while(ptr):
            print(ptr.val, end=" ")
            ptr = ptr.next
        print()
        return

class LRU:
    last_used = queue()
    length = 0
    max_length = 0
    cache = {}

    def __init__(self, n):
        self.max_length = n
        return

    def set(self, key, value):
        if(key not in self.cache and self.length == self.max_length):
            self.cache.pop(self.last_used.pop())
            self.length -= 1
        self.cache[key] = value
        self.length += 1
        self.last_used.push(key)

    def get(self, key):
        if(key in self.cache):
            self.last_used.push(key)
        return self.cache.get(key)

newCache = LRU(2)
newCache.set("piece", "puzzle")
newCache.set("youtube", "google")
newCache.set("pineapple", "pizza")
print(newCache.get("youtube"))
print(newCache.get("piece"))
# print(newCache.get("pineapple"))
newCache.set("brother", "sister")
print()
print("piece \t\t",newCache.get("piece"))
print("youtube \t",newCache.get("youtube"))
print("pineapple\t",newCache.get("pineapple"))
print("brother\t\t",newCache.get("brother"))