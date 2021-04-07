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


def setZeroes(matrix): # second try
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    clear_rows = [False for _ in range(m)]
    clear_cols = [False for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                clear_rows[i] = True
                clear_cols[j] = True

    for i in range(m):
        if clear_rows[i] == True:
            for ind in range(n):
                matrix[i][ind] = 0

    for j in range(n):
        if clear_cols[j] == True:
            for ind in range(m):
                matrix[ind][j] = 0

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