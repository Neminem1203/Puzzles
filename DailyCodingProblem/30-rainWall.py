'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''
import random

def rainWall(walls):
    def calculateRain(highest, ind1, ind2, step=1):
        secondHighest = 0
        secondHighestInd = 0
        sumOfWalls = 0
        sumOfRain = 0
        for ind in range(ind1, ind2, step):
            sumOfWalls += walls[ind]
            if(walls[ind] > secondHighest):
                sumOfRain += (secondHighest*(abs(ind-secondHighestInd)))
                secondHighest = walls[ind]
                secondHighestInd = ind
        sumOfRain += (secondHighest * (abs(ind2 - secondHighestInd)))
        # return (secondHighest*(abs(ind2-ind1))-sumOfWalls)
        return sumOfRain - sumOfWalls
    highest = walls[0]
    ind = 0
    for i in range(len(walls)):
        if walls[i] > highest:
            highest = walls[i]
            ind = i

    rain = 0
    rain += calculateRain(highest,0, ind)
    rain += calculateRain(highest,len(walls)-1, ind, -1)
    # print(rain)
    return(rain)

# sampleWall = [3, 0, 1, 3, 0, 5]
# print(sampleWall,"\n",rainWall(sampleWall))

# bigWall = [2,5,3,6,9,5,3,9,1,5,6,4]
# print(bigWall,"\n",rainWall(bigWall))

for i in range(0, 3):
    randomWall = [random.randint(0,15) for x in range(random.randint(5,15))]
    print(randomWall,"\n",rainWall(randomWall))

'''
.....X
.....X
XOOXOX
XOOXOX
XOXXOX
301305
SUM = 8

....XOOX....
....XOOX....
....XOOX....
...XXOOXOOX.
.XOXXXOXOXX.
.XOXXXOXOXXX
.XXXXXXXXXXX
XXXXXXXXXXXX
XXXXXXXXXXXX
253695391564
SUM = 18
'''