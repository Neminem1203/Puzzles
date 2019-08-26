'''
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''
'''
not sure how to make it O(1) space, but here's my attempt with O(n)
bitwise operator xor would work with duplicates but not sure how to deal with triples
'''

def noTriples(array):
    dupes = {}
    for i in array:
        if i in dupes:
            dupes[i] += 1
        else:
            dupes[i] = 1
    for i in dupes:
        if dupes[i] == 1:
            return i

print(noTriples([6,1,3,3,3,6,6]))
print(noTriples([13,19,13,13]))