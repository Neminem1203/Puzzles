# https://leetcode.com/problems/first-missing-positive/

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    idx = 0
    counter = 0
    while(idx < len(nums)):
        # print(nums, idx, nums[idx]-1)
        if nums[idx] > 0 and nums[idx] <= len(nums) and nums[nums[idx]-1] != nums[idx]:
            temp = nums[nums[idx]-1]
            nums[nums[idx] - 1] = nums[idx]
            nums[idx] = temp
        else:
            idx += 1
        counter += 1
        if(counter > 5):
            break
    idx = 0
    while(idx < len(nums)):
        if(nums[idx] != idx+1):
            break
        idx += 1
    return idx + 1

print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([3,4,2,1]))

