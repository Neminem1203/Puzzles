'''
https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
Given an square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
'''
import math
testMatrix1 = [[1,2,3],[4,5,6],[7,8,9]]
testMatrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
testMatrix3 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],
               [19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]




def shift(magicNumbers):
    shiftNumbers = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i in range(4):
        for j in range(2):
            magicNumbers[i][j] += shiftNumbers[i][j]
    return magicNumbers

def swapInd(matrix, arrpos):
    ind = 1
    while(ind != len(arrpos)):
        temp = matrix[arrpos[0][0]][arrpos[0][1]]
        matrix[arrpos[0][0]][arrpos[0][1]] = matrix[arrpos[ind][0]][arrpos[ind][1]]
        matrix[arrpos[ind][0]][arrpos[ind][1]] = temp
        ind += 1
    return matrix


def inplaceRotation(mat):
    if(not mat):
        return mat
    n = len(mat)-1
    mN = [[0, 0], [n, 0], [n, n], [0, n]] #magic numbers
    for i in range(math.floor((n+1)/2)):
        # for i in magicNumbers:
        #     print(i,end=", ")
        # print("")
        for j in range(math.ceil((n+1)/2)):
            # displacement of [0][j], [-j][0], [0][-j], [j][0]
            # print(mat   [mN[0][0]]      [mN[0][1]+j]) # pos0 -> pos1
            # print(mat   [mN[1][0]-j]    [mN[1][1]]) # pos1 -> pos2
            # print(mat   [mN[2][0]]      [mN[2][1]-j]) # pos2 -> pos3
            # print(mat   [mN[3][0]+j]    [mN[3][1]]) # pos3 -> pos0
            swapPositions = [[mN[0][0],   mN[0][1]+j],
                             [mN[1][0]-j, mN[1][1]],
                             [mN[2][0],   mN[2][1]-j],
                             [mN[3][0]+j, mN[3][1]]]
            mat = swapInd(mat, swapPositions)
        mN = shift(mN)
    return mat

print(testMatrix1)
print(inplaceRotation(testMatrix1),"\n")
print(testMatrix2)
print(inplaceRotation(testMatrix2),"\n")
print(testMatrix3)
print(inplaceRotation(testMatrix3),"\n")