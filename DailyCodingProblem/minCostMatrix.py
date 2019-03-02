'''
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''

testMat = [[2,9,3,2,1,6],
           [2,8,5,6,3,1],
           [1,2,4,9,3,2]]

def minCostMatrix(inpMat):
    arrayLen = len(inpMat[0])
    indLen = len(inpMat)

    minArr = [0]*indLen
    minArrCopy = [0]*indLen
    for i in range(indLen):
        minArr[i] = inpMat[i][0]
        minArrCopy[i] = inpMat[i][0]
    for ind2 in range(1, arrayLen):
        # Copy Array before using it
        for i in range(indLen):
            minArrCopy[i] = minArr[i]
        # Check min of previous array
        for ind1 in range(indLen):
            minInd = (ind1+1) % indLen
            minVal = minArrCopy[minInd%indLen]
            for i in range(minInd+1, minInd+indLen-1):
                if(minArrCopy[i%indLen] < minVal):
                    minInd = i%indLen
                    minVal = minArrCopy[i%indLen]
            minArr[ind1] = inpMat[ind1][ind2] + minArrCopy[minInd]
        # print(minArr)
    return min(minArr)

print(minCostMatrix(testMat))