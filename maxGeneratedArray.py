def getMaximumGenerated(n):
    """
    :type n: int
    :rtype: int
    """
    highest = 0
    if n < 1:
        return 0
    nums = [0 for i in range(n + 1)]
    nums[1] = 1

    for i in range(n + 1):
        if i % 2 == 0:
            nums[i] = nums[int(i / 2)]
        else:
            ind = int((i - 1) / 2)
            nums[i] = nums[ind] + nums[ind + 1]

        if highest < nums[i]:
            highest = nums[i]

    return highest


print(getMaximumGenerated(7))
print(getMaximumGenerated(3))