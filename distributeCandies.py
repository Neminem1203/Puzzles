# https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/
def distributeCandies(candyType):
    """
    :type candyType: List[int]
    :rtype: int
    """
    candict = {}
    n = len(candyType)/2
    diff_types = 0
    for candy in candyType:
        if candy not in candict:
            diff_types += 1
            candict[candy] = True


    if diff_types < n:
        return diff_types

    return n