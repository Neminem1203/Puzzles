'''
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
'''


'''
testLife

* * * .
. * * *
* . * *
. . . .

'''
def visuaLife(array):
    minX = 100
    minY = 100
    maxX = 0
    maxY = 0
    adjustX = 0
    adjustY = 0
    for i in array:
        if i[0] < minX:
            minX = i[0]
        if i[0] > maxX:
            maxX = i[0]
        if i[1] < minY:
            minY = i[1]
        if i[1] > maxY:
            maxY = i[1]

    #Takes less memory
    #doesn't create an array for me to use
    # for i in range(minX, maxX+1):
    #     for j in range(minY, maxY+1):
    #         if [i,j] in array:
    #             print('*', end=" ")
    #         else:
    #             print('.', end=" ")
    #     print()

    #Uses more memory
    #makes program easier by returning an array
    if(minX < 0):
        adjustX -= minX
        maxX -= minX
        minX = 0

    if(minY < 0):
        adjustY -= minY
        maxY -= minY
        minY = 0
    visualArray = [['.' for x in range(minY, maxY+1)] for y in range(minX, maxX+1)]
    for i in array:
        visualArray[i[0] + adjustX][i[1]+adjustY] = '*'
    # for i in visualArray:
    #     print(i, )
    return visualArray

testLife = [[0,0],[1,3],[0,1],[2,2],[2,3],[0,2],[1,1],[1,2],[2,0],[5,4]]


arrayOfLife = visuaLife(testLife)
lenX = len(arrayOfLife)
lenY = len(arrayOfLife[0])
while(any('*' in row for row in arrayOfLife)):
    remove1 = True
    for i in range(lenX):
        for j in range(lenY):
            numNeighbors = 0
            print(arrayOfLife[i][j],end=" ")
            if(i > 0 and arrayOfLife[i-1][j] == "*"):
                numNeighbors += 1
            if(i < lenX-1 and arrayOfLife[i+1][j] == "*"):
                numNeighbors += 1
            if (j > 0 and arrayOfLife[i][j-1] == "*"):
                numNeighbors += 1
            if (j < lenY - 1 and arrayOfLife[i][j+1] == "*"):
                numNeighbors += 1

            if(arrayOfLife[i][j] == "*" and numNeighbors < 2 or numNeighbors > 3):
                arrayOfLife[i][j] = "."
            if(arrayOfLife[i][j] == "." and numNeighbors == 3):
                arrayOfLife[i][j] = "*"
        print()
    print()