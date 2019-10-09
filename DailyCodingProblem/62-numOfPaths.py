'''
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of
starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right
'''
debug = True
if debug:
    visualMatrix = []
    def printVisualMatrix():
        for i in range(len(visualMatrix)-1, -1, -1):
            print(i,end = "\t")
        print()
        for i in range(len(visualMatrix)):
            for j in visualMatrix[i]:
                print(j,end="\t")
            print(len(visualMatrix)-i-1)

    def findAnswer(n,m):
        x = len(visualMatrix)
        y = len(visualMatrix[0])
        if(x > n and y > m):
            return visualMatrix[x-n-1][y-m-1]
        else:
            return "Not in range of previous answer"

def numOfPaths(n, m):
    if debug:
        global visualMatrix
        visualMatrix = [[0 for i in range(m)] for j in range(n)]
    def newPath(x,y, n, m):
        if debug:
            global visualMatrix
        if(x == n-1 and y == m-1):
            return 1

        sum = 0
        if(x < n-1):
            sum += newPath(x+1,y, n,m)
        if(y < m-1):
            sum += newPath(x,y+1, n,m)
        if debug:
            visualMatrix[x][y] = sum
        return sum
    return newPath(0,0,n,m)

print("2*2: ",numOfPaths(2,2))
if debug: printVisualMatrix()
print("5*5: ",numOfPaths(5,5))
if debug: printVisualMatrix()
print("10*10: ", numOfPaths(10,10))
if debug: printVisualMatrix()
if debug: print(findAnswer(6, 5))