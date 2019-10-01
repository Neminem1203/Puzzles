'''
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with
 the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
'''
'''
emptySudoku = [[[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]]'''
# testSudoku = [[[5], [ ], [ ], [ ], [9], [ ], [ ], [ ], [2]],
#               [[7], [6], [ ], [5], [ ], [1], [8], [9], [ ]],
#               [[ ], [3], [ ], [8], [2], [6], [1], [5], [7]],
#               [[6], [2], [ ], [9], [ ], [7], [5], [8], [1]],
#               [[8], [ ], [4], [3], [5], [2], [9], [ ], [ ]],
#               [[ ], [ ], [7], [ ], [6], [ ], [2], [ ], [ ]],
#               [[3], [4], [8], [6], [ ], [9], [7], [ ], [ ]],
#               [[ ], [7], [ ], [ ], [ ], [5], [3], [1], [ ]],
#               [[1], [9], [ ], [ ], [7], [ ], [4], [ ], [8]]]
testSudoku1 =[[[ ], [ ], [8], [ ], [ ], [5], [ ], [4], [ ]],
              [[ ], [ ], [1], [ ], [ ], [8], [9], [2], [ ]],
              [[ ], [3], [ ], [1], [ ], [ ], [8], [ ], [ ]],
              [[ ], [ ], [6], [4], [ ], [ ], [ ], [9], [ ]],
              [[ ], [ ], [7], [ ], [5], [ ], [6], [ ], [ ]],
              [[ ], [8], [ ], [ ], [ ], [7], [2], [ ], [ ]],
              [[ ], [ ], [4], [ ], [ ], [2], [ ], [3], [ ]],
              [[ ], [2], [3], [6], [ ], [ ], [4], [ ], [ ]],
              [[ ], [5], [ ], [8], [ ], [ ], [1], [ ], [ ]]]


testSudoku2 =[[[ ], [ ], [ ], [ ], [ ], [1], [ ], [7], [ ]],
              [[ ], [ ], [ ], [6], [8], [4], [ ], [ ], [5]],
              [[ ], [5], [ ], [ ], [ ], [ ], [ ], [4], [ ]],
              [[1], [ ], [7], [8], [ ], [ ], [4], [ ], [ ]],
              [[8], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [3]],
              [[ ], [ ], [5], [ ], [ ], [7], [6], [ ], [9]],
              [[ ], [1], [ ], [ ], [ ], [ ], [ ], [2], [ ]],
              [[6], [ ], [ ], [3], [4], [5], [ ], [ ], [ ]],
              [[ ], [3], [ ], [2], [ ], [ ], [ ], [ ], [ ]]]

def printSudoku(sudoku):
    x = 0
    for arr in sudoku:
        y = 0
        for num in arr:
            y+= 1
            if(len(num) == 1):
                print(num[0], end="")
            else:
                print(" ", end="")
            if(y%3==0):
                print("|\t",end="")
            else:
                print("\t",end="")
        x+=1
        if(x%3 == 0):
            print('\n----------------------------------')
        else:
            print('')
    print("\n\n")

def sudokuSolver(sudokuPuzzle):
    amountOfEmpty = 0 # this is just for prevEmpty = amountOfEmpty
    while(True):
        prevEmpty = amountOfEmpty # this is to prevent infinite loops
        amountOfEmpty = 0 # empty cells in the entire sudoku
        for x in range(9):
            for y in range(9):
                if(len(sudokuPuzzle[x][y]) != 1):
                    amountOfEmpty += 1 # [x, y] is empty so we increment the counter
                    availableNums = [i+1 for i in range(9)] # possible numbers in this cell
                    # this is the top left coordinate of the box [x, y] are in
                    boxStart = [int(x / 3) * 3, int(y / 3) * 3]
                    for i in range(9):
                        # getting rid of possible nums from vertical
                        if(len(sudokuPuzzle[i][y]) == 1):
                            for avail in range(len(availableNums)):
                                if(availableNums[avail] == sudokuPuzzle[i][y][0]):
                                    availableNums = availableNums[:avail] + availableNums[avail+1:]
                                    break
                        # getting rid of possible nums from horizontal
                        if(len(sudokuPuzzle[x][i]) == 1):
                            for avail in range(len(availableNums)):
                                if(availableNums[avail] == sudokuPuzzle[x][i][0]):
                                    availableNums = availableNums[:avail] + availableNums[avail+1:]
                                    break
                    # getting rid of possible nums from box
                    for boxX in range(boxStart[0], boxStart[0]+3):
                        for boxY in range(boxStart[1], boxStart[1]+3):
                            if(len(sudokuPuzzle[boxX][boxY]) == 1):
                                for avail in range(len(availableNums)):
                                    if (availableNums[avail] == sudokuPuzzle[boxX][boxY][0]):
                                        availableNums = availableNums[:avail] + availableNums[avail + 1:]
                                        break
                    # this means that this cell [x,y] cant hold any number
                    if len(availableNums) == 0:
                        return []
                    # after we find out the available numbers for the cell [x,y]
                    if len(availableNums) > 1:
                        horizontalEmpty = [0 for i in range(3)]
                        verticalEmpty = [0 for i in range(3)]
                        for boxX in range(boxStart[0], boxStart[0]+3):
                            for boxY in range(boxStart[1], boxStart[1]+3):
                                if(len(sudokuPuzzle[boxX][boxY]) != 1):
                                    if(boxX != x or boxY != y):
                                        horizontalEmpty[boxX-boxStart[0]] += 1
                                        verticalEmpty[boxY-boxStart[1]] += 1
                        # print(x, " ", y, " ",boxStart,"\t", horizontalEmpty, "\t", verticalEmpty)
                        # top horizontal line
                        if  (x%3 ==0):
                            x1 = x+1
                            x2 = x+2
                        # middle horizontal line
                        elif(x%3==1):
                            x1 = x-1
                            x2 = x+1
                        # bottom horizontal line
                        else:
                            x1 = x-2
                            x2 = x-1
                        # left vertical line
                        if  (y%3==0):
                            y1 = y+1
                            y2 = y+2
                        # middle vertical line
                        elif(y%3==1):
                            y1 = y-1
                            y2 = y+1
                        # right vertical line
                        else:
                            y1 = y-2
                            y2 = y-1
                        # checking the numbers to see if it's possible in other grids of the box
                        for num in availableNums:
                            occurences = 0
                            horizontalCopy = horizontalEmpty.copy()
                            verticalCopy = verticalEmpty.copy()
                            for i in range(9):
                                if(sudokuPuzzle[x1][i] == [num]):
                                    occurences += 1
                                    horizontalCopy[x1%3] = 0
                                if(sudokuPuzzle[x2][i] == [num]):
                                    occurences += 1
                                    horizontalCopy[x2%3] = 0
                                if(sudokuPuzzle[i][y1] == [num]):
                                    occurences += 1
                                    verticalCopy[y1%3] = 0
                                if(sudokuPuzzle[i][y2] == [num]):
                                    occurences += 1
                                    verticalCopy[y2%3] = 0
                            # if we find 4 occurences, then this exact cell is where the number should be
                            if occurences == 4:
                                sudokuPuzzle[x][y] = [num]
                                break
                            # print(occurences,"\t",num,"\t\t\t",horizontalCopy,"\t", verticalCopy)

                            # this is checking if this number can be placed in the other cells in this block
                            useThis = False
                            for i in range(3):
                                if horizontalCopy[i] == 0:
                                    useThis = True
                                else:
                                    useThis = False
                                    break
                            if useThis:
                                sudokuPuzzle[x][y] = [num]
                                break
                            useThis = False
                            for i in range(3):
                                if verticalCopy[i] == 0:
                                    useThis = True
                                else:
                                    useThis = False
                                    break
                            if useThis:
                                sudokuPuzzle[x][y] = [num]
                                break
                    # this only occurs when there's only one possible number for this cell [x,y]
                    else:
                        sudokuPuzzle[x][y] = availableNums
                        amountOfEmpty

        # print("Amount of Empties: ",amountOfEmpty)
        # printSudoku(sudokuPuzzle)
        # this means the puzzle is complete
        if(amountOfEmpty == 0):
            break
        # this is to prevent infinite loops
        if(prevEmpty == amountOfEmpty):
            return []
    return sudokuPuzzle


print("Original: ")
printSudoku(testSudoku2)
print("Solution: ")
solution = sudokuSolver(testSudoku2)
printSudoku(solution)