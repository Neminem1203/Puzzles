def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    indList = []
    numList = [nums[0]]
    for num in nums[1:]:
        ind = len(numList)-1
        while ind >= 0 and numList[ind] > num:
            ind -= 1
        numList = numList[:ind+1] + [num] + numList[ind+1:]

    print(numList)
    print(indList)

print(maxCoins([3,1,5,8]))
print(maxCoins([3,7,1,2,4,9,6]))