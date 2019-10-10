'''
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
'''
import math
def knightsTour(n):
    def copyMatrix(matrix):
        fakeMatrix = [[] for i in range(n)]
        for i in range(n):
            fakeMatrix[i] += matrix[i]
        return fakeMatrix
    def algo(location, newMatrix):
        newMatrix[location[0]][location[1]] = 1
        returnThis = True
        for i in newMatrix:
            if 0 in i:
                returnThis = False
                break
        if returnThis:
            return 1
        sum = 0
        # checking [-2,-1] and [-2,1] steps
        if location[0]-2 >= 0:
            if location[1] - 1 >= 0 and newMatrix[location[0]-2][location[1]-1] == 0:
                sum += algo([location[0] - 2, location[1] - 1], copyMatrix(newMatrix))
            if location[1] + 1 < n and newMatrix[location[0]-2][location[1]+1] == 0:
                sum += algo([location[0] - 2, location[1] + 1], copyMatrix(newMatrix))
        # checking [-1, -2] and [-1, 2] steps
        if location[0]-1 >= 0:
            if location[1] - 2 >= 0 and newMatrix[location[0]-1][location[1]-2] == 0:
                sum += algo([location[0] - 1, location[1] - 2], copyMatrix(newMatrix))
            if location[1] + 2 < n and newMatrix[location[0]-1][location[1]+2] == 0:
                sum += algo([location[0] - 1, location[1] + 2], copyMatrix(newMatrix))
        # checking [1, -2] and [1, 2] steps
        if location[0] + 1 < n:
            if location[1] - 2 >= 0 and newMatrix[location[0]+1][location[1]-2] == 0:
                sum += algo([location[0] + 1, location[1] - 2], copyMatrix(newMatrix))
            if location[1] + 2 < n and newMatrix[location[0]+1][location[1]+2] == 0:
                sum += algo([location[0] + 1, location[1] + 2], copyMatrix(newMatrix))
        # checking [2,-1] and [2,1] steps
        if location[0] + 2 < n:
            if location[1] - 1 >= 0 and newMatrix[location[0]+2][location[1]-1] == 0:
                sum += algo([location[0] + 2, location[1] - 1], copyMatrix(newMatrix))
            if location[1] + 1 < n and newMatrix[location[0]+2][location[1]+1] == 0:
                sum += algo([location[0] + 2, location[1] + 1], copyMatrix(newMatrix))
        return sum
    returnSum = 0
    for i in range(math.floor(n/2)):
        for j in range(math.ceil(n/2)):
            returnSum += algo([i,j], [[0 for i in range(n)] for j in range(n)])
            print(returnSum)
    returnSum *= 4
    if(n%2 == 1):
        returnSum += algo([int((n-1)/2), int((n-1)/2)], [[0 for i in range(n)] for j in range(n)])
        print(returnSum)
    return returnSum
# print(knightsTour(5))
print(knightsTour(6)) # This takes a long time to compute. Probably need to find a better way than brute force