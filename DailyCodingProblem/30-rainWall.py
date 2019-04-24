'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

def rainWall(walls):
    highest = walls[0]
    ind = 0
    for i in range(len(walls)):
        if walls[i] > highest:
            highest = walls[i]
            ind = i

    for i in range(0, ind+1):
        print(i,end=", ")
    for i in range(len(walls)-1, ind-1, -1):
        print(i,end=", ")
    print()

sampleWall = [3, 0, 1, 3, 0, 5]
bigWall = [2,5,3,6,9,5,3,9,1,5,3,4]
rainWall(sampleWall)
rainWall(bigWall)