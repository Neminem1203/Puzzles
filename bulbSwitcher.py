# https://leetcode.com/problems/bulb-switcher-iv/
def minFlips(target):
    """
    :type target: str
    :rtype: int
    """
    count = 0
    state = "0"
    for i in target:
        if state != i:
            count += 1
            state = i
    return count