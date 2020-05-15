# https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = []
    cols = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] == 0):
                if i not in rows:
                    rows += [i]
                if j not in cols:
                    cols += [j]

    for i in rows:
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

    for j in cols:
        for i in range(len(matrix)):
            matrix[i][j] = 0

    return matrix

firstMat = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

secondMat = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

print(setZeroes(firstMat))
print(setZeroes(secondMat))