# https://leetcode.com/problems/jump-game/
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    maxJump = 0
    idx = 0
    while idx <= maxJump:
        if maxJump > len(nums):
            return True
        if idx + nums[idx] > maxJump:
            maxJump = idx + nums[idx]
        idx += 1
    return False

print(canJump([2,3,1,1,4])) # True
print(canJump([3,2,1,0,4])) # False