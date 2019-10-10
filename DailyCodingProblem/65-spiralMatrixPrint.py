'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:
1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
'''

def spiralMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if n < m:
        loops = int(n/2)
    else:
        loops = int(m/2)
    location = [0,0]
    m -= 1
    n -= 1
    for loopNum in range(loops):
        for step in range(m):
            print(matrix[location[0]][location[1]],end=" ")
            location[1] += 1
        for step in range(n):
            print(matrix[location[0]][location[1]],end=" ")
            location[0] += 1
        for step in range(m):
            print(matrix[location[0]][location[1]],end=" ")
            location[1] -= 1
        for step in range(n):
            print(matrix[location[0]][location[1]],end=" ")
            location[0] -= 1
        m -= 2
        n -= 2
        location[0] += 1
        location[1] += 1
    print()

testMatrix = [  [1,  2,  3,  4,  5],
                [6,  7,  8,  9,  10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]]
m = 6
n = 2
biggerTest = [[] for j in range(m)]
num = 1
for i in range(m):
    for j in range(n):
        biggerTest[i] += [num]
        num += 1

spiralMatrix(testMatrix)
for i in biggerTest:
    print(i)
spiralMatrix(biggerTest)