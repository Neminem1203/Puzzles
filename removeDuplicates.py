def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return len(nums)
    ind = 2
    while ind < len(nums):
        print(nums)
        if nums[ind] == nums[ind - 1] and nums[ind] == nums[ind - 2]:
            newNumInd = ind+1
            while newNumInd < len(nums) and nums[newNumInd] == nums[ind]:
                newNumInd += 1
            for i in range(len(nums)-newNumInd):
                print(nums)
                nums[ind+i] = nums[newNumInd+i]
            for i in range(newNumInd-ind):
                del nums[-1]
        ind += 1
    return len(nums)


removeDuplicates([1,1,1,1,2,2,2,3,4])