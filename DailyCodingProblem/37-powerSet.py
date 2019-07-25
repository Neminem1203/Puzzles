'''
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

def powerSet(originalSet):
    newSet = [[]]
    def combo(stack, frm, to, len):
        if(len != 1):
            for num in range(frm, to):
                combo(stack + [num], num+1, to, len-1)
        else:
            newStack = []
            for stackNum in stack:
                newStack.append(originalSet[stackNum])
            for num in range(frm, to):
                newSet.append(newStack + [originalSet[num]])
    for i in range(len(originalSet)+1):
        combo([], 0, len(originalSet), i)
    # print(newSet)
    return newSet

print(powerSet([5,7,6,4,1]))