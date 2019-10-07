'''Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
'''

def multiSetSum(multiset):
    def findSum(list, sum):
        if list == []:
            return []
        if(sum == list[0]):
            return [list[0]]
        for i in range(len(list)):
            retList = findSum(list[i+1:], sum - list[i])
            if(retList != []):
                return [list[i]] + retList
        return []
    sum = 0
    for i in multiset:
        sum += i
    if sum % 2 != 0:
        return []
    goalSum = sum/2
    n = len(multiset)
    for i in range(n):
        returnList = findSum(multiset[i+1:], goalSum - multiset[i])
        if(returnList != []):
            return [multiset[i]] + returnList
    return []

print(multiSetSum([15, 5, 20, 10, 35, 15, 10]))
print(multiSetSum([15, 5, 20, 10, 35]))
print(multiSetSum([50, 15, 20, 25, 5, 5]))