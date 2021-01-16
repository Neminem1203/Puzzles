def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sorted_nums = []
    for num in nums:
        ind = 0
        while ind < len(sorted_nums):
            if num >= sorted_nums[ind]:
                break
            ind += 1
        sorted_nums.insert(ind, num)
    return sorted_nums[k - 1]


print(findKthLargest([3,2,1,5,6,4],2)) # 5
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
