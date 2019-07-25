

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