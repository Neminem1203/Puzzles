# https://leetcode.com/problems/house-robber/submissions/

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return nums[0]
    arr = []
    arr.append(nums[0])
    if nums[1] > nums[0]:
        arr.append(nums[1])
    else:
        arr.append(nums[0])

    for i in range(2, len(nums)):
        combo = nums[i] + arr[i - 2]
        if combo > arr[i - 1]:
            arr.append(combo)
        else:
            arr.append(arr[i - 1])

    return arr[-1]