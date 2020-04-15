# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
import math

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    found = [-1, -1]
    high = len(nums)
    low = 0
    idx = math.floor(len(nums)/2)
    while(True):
        if(nums[idx] > target):
            high = idx
            idx = math.floor((high+low)/2)
        elif(nums[idx] < target):
            low = idx
            idx = math.floor((high+low)/2)
        else:
            found = [idx, idx]
            for i in range(idx, 0, -1):
                if(nums[i] == target):
                    found[0] = i
                else:
                    break
            for i in range(idx, len(nums)):
                if(nums[i] == target):
                    found[1] = i
                else:
                    break
            break
        if(high <= low+1):
            break
    print(found)

nums = [5,7,7,8,8,10]
searchRange(nums, 8)
searchRange(nums, 7)