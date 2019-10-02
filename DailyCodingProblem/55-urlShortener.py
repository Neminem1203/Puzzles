'''
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''
import hashlib

class node:
    key = None
    val = None
    next = None

    def __init__(self, key=None, val=None):
        if(key and val):
            self.key = key
            self.val = val

class listOfURL:
    headOfList = None

    def __init__(self, headNode=None):
        if(headNode):
            self.headOfList = headNode

    def insert(self, key):
        if(self.headOfList == None):
            newNode = node(key, hashlib.md5(key.encode()).hexdigest()[0:6])
            self.headOfList = newNode
            return newNode.val
        ptr = self.headOfList
        while(ptr.next != None):
            if(ptr.key == key):
                return ptr.val
            ptr = ptr.next
        newNode = node(key, hashlib.md5(key.encode()).hexdigest()[0:6])
        ptr.next = newNode
        return ptr.val


    def restore(self, key):
        ptr = self.headOfList
        while(ptr.key != key):
            return ptr.val
        return None

    def printAll(self):
        ptr = self.headOfList
        while(ptr != None):
            print("URL: ",ptr.key,"\tShort: ",ptr.val)
            ptr = ptr.next

dictionary = listOfURL()

def shorten(url):
    dictionary.insert(url)

def restore(short):
    dictionary.restore(short)


shorten("https://www.google.com")
shorten("https://www.bing.com")
shorten("https://www.msn.com")
shorten("https://www.yahoo.com")
dictionary.printAll()