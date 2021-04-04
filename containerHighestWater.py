# https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    highest_area = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1, n):
            if n - j * height[j] < highest_area:
                break
            width = j - i
            length = height[i]
            if height[j] < length:
                length = height[j]
            area = length * width
            if area > highest_area:
                highest_area = area
    return highest_area
