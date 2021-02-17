# https://leetcode.com/problems/reduce-array-size-to-the-half/
import math
def minSetSize(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 0
        count[num] += 1

    count_list = []
    for num in count:
        count_list += [count[num]]

    count_list.sort()
    count_list.reverse()

    target_size = math.ceil(len(arr)/2)
    count = 0
    for num in count_list:
        target_size -= num
        count += 1
        if target_size <= 0:
            return count

print(minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(minSetSize([7,7,7,7,7,7]))
print(minSetSize([1,9]))
print(minSetSize([1000,1000,3,7]))
print(minSetSize([1,2,3,4,5,6,7,8,9,10]))