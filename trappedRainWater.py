# https://leetcode.com/problems/trapping-rain-water/
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 2:
        return 0
    last_high = height[0] # first wall is the highest seen
    n = len(height)
    water_saved = [0 for i in range(n)] # water captured array
    
    # left run through assuming left wall encapsulates the water
    for i in range(1, n - 1):
        wall = height[i] # wall height at i
        if last_high > wall:
            water_saved[i] = last_high - wall # how much water would be trapped if only left wall is considered
        if last_high < wall:
            last_high = wall # reassign highest left wall

    # right run where we check the containers are valid
    last_high = height[n - 1] # last wall is the highest seen
    water = 0 # amount of water to return
    for i in range(n - 2, 0, -1):
        wall = height[i] # wall height at i
        if last_high < wall + water_saved[i]: # if the right wall can't encapsulate the water, set it to the limit
            water_saved[i] = last_high - wall
        if water_saved[i] > 0:
            water += water_saved[i]
        if wall > last_high:
            last_high = wall # reassign highest right wall
    return water