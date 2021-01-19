def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    pairs = {}
    operations = 0
    for num in nums:
        opposite = k - num
        if opposite in pairs and pairs[opposite] > 0:
            pairs[opposite] -= 1
            operations += 1
        else:
            if num not in pairs:
                pairs[num] = 0
            pairs[num] += 1
    return operations


print(maxOperations([1,2,3,4], 5)) # 2
print(maxOperations([3,1,3,4,3],6)) # 1