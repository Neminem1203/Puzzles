# https://leetcode.com/problems/sum-of-unique-elements/
def sumOfUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    state = {}
    total = 0
    for num in nums:
        if num in state:
            if state[num] == 1:
                total -= num
                state[num] += 1
        else:
            state[num] = 1
            total += num
    return total