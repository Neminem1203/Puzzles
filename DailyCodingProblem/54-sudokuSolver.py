'''
Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with
 the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.

emptySudoku =[[[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]],
              [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]]

'''

testSudoku =[[[ ], [ ], [ ], [ ], [ ], [8], [ ], [ ], [2]],
              [[ ], [ ], [5], [6], [ ], [ ], [ ], [3], [ ]],
              [[ ], [ ], [9], [1], [ ], [ ], [ ], [4], [ ]],
              [[ ], [1], [3], [ ], [ ], [6], [ ], [ ], [9]],
              [[9], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [6]],
              [[8], [ ], [ ], [5], [ ], [ ], [3], [7], [ ]],
              [[ ], [6], [ ], [ ], [ ], [3], [7], [ ], [ ]],
              [[ ], [4], [ ], [ ], [ ], [9], [1], [ ], [ ]],
              [[3], [ ], [ ], [2], [ ], [ ], [ ], [ ], [ ]]]



from copy import copy, deepcopy

debug = False

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
    print("\n")

def sudokuSolver(sudokuPuzzle):
    sudokuPuzzle = deepcopy(sudokuPuzzle)
    iterations = 0
    amountOfEmpty = 0 # this is just for prevEmpty = amountOfEmpty
    while(True):
        iterations += 1
        prevEmpty = amountOfEmpty # this is to prevent infinite loops
        amountOfEmpty = 0 # empty cells in the entire sudoku
        # when we recursively call, I want to make sure all numbers are possible in each box
        # for x in range(3):
        #     for y in range(3):
        #         boxStart = [x * 3, y * 3]
        #         for boxX in range(boxStart[0], boxStart[0] + 3):
        #             for boxY in range(boxStart[1], boxStart[1] + 3):
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
                        if debug:
                            print("[",x,", ",y,"] has no available numbers")
                            printSudoku(sudokuPuzzle)
                        return []

                    # after we find out the available numbers for the cell [x,y]
                    if len(availableNums) > 1:
                        emptyBox = [[0 for i in range(3)] for j in range(3)]
                        for boxX in range(boxStart[0], boxStart[0]+3):
                            for boxY in range(boxStart[1], boxStart[1]+3):
                                if(len(sudokuPuzzle[boxX][boxY]) != 1):
                                    if(boxX != x or boxY != y):
                                        emptyBox[boxX-boxStart[0]][boxY-boxStart[1]] = 1
                        # left line
                        if  (x%3 ==0):
                            x1 = x+1
                            x2 = x+2
                        # middle vertical line
                        elif(x%3==1):
                            x1 = x-1
                            x2 = x+1
                        # right line
                        else:
                            x1 = x-2
                            x2 = x-1
                        # bottom line
                        if  (y%3==0):
                            y1 = y+1
                            y2 = y+2
                        # middle horizontal line
                        elif(y%3==1):
                            y1 = y-1
                            y2 = y+1
                        # top line
                        else:
                            y1 = y-2
                            y2 = y-1
                        if(debug):
                            print("X: ",x, " Y:", y,"\t", emptyBox)
                            print("X1:", x1, " X2:", x2, " Y1:", y1, " Y2:", y2)
                        # checking the numbers to see if it's possible in other grids of the box
                        for num in availableNums:
                            occurences = 0
                            emptyBoxCopy = deepcopy(emptyBox)
                            if debug:
                                print(emptyBoxCopy)
                            for i in range(9):
                                if(sudokuPuzzle[x1][i] == [num]):
                                    occurences += 1
                                    for j in range(3):
                                        emptyBoxCopy[x1%3][j] = 0
                                if(sudokuPuzzle[x2][i] == [num]):
                                    occurences += 1
                                    for j in range(3):
                                        emptyBoxCopy[x2%3][j] = 0
                                if(sudokuPuzzle[i][y1] == [num]):
                                    occurences += 1
                                    for j in range(3):
                                        emptyBoxCopy[j][y1%3] = 0
                                if(sudokuPuzzle[i][y2] == [num]):
                                    occurences += 1
                                    for j in range(3):
                                        emptyBoxCopy[j][y2%3] = 0
                            # if we find 4 occurences, then this exact cell is where the number should be
                            if occurences == 4:
                                sudokuPuzzle[x][y] = [num]
                                amountOfEmpty -= 1
                                break
                            if debug:
                                print("Number:",num,"\nOccurences:",occurences,"\n",emptyBoxCopy,end="\n\n")

                            # this is checking if this number can be placed in the other cells in this block
                            # print(horizontalCopy, verticalCopy)
                            useThis = False
                            for i in range(3):
                                if 1 in emptyBoxCopy[i]:
                                    useThis = False
                                    break
                                else:
                                    useThis = True
                            if useThis:
                                sudokuPuzzle[x][y] = [num]
                                amountOfEmpty -= 1
                                break
                        # print(availableNums)
                    # this only occurs when there's only one possible number for this cell [x,y]
                    else:
                        sudokuPuzzle[x][y] = availableNums
                        amountOfEmpty -= 1
        if debug:
            print("Amount of Empties:",amountOfEmpty)
            print("Iteration:", iterations)
            printSudoku(sudokuPuzzle)
        # this means the puzzle is complete
        if(amountOfEmpty == 0):
            break
        # this is to prevent infinite loops
        if(prevEmpty == amountOfEmpty):
            # trying out the cells with 2 options
            if debug:
                print("Multiple Paths here")
            for x in range(9):
                for y in range(9):
                    amountOfEmpty += 1  # [x, y] is empty so we increment the counter
                    availableNums = [i + 1 for i in range(9)]  # possible numbers in this cell
                    # this is the top left coordinate of the box [x, y] are in
                    boxStart = [int(x / 3) * 3, int(y / 3) * 3]
                    for i in range(9):
                        # getting rid of possible nums from vertical
                        if (len(sudokuPuzzle[i][y]) == 1):
                            for avail in range(len(availableNums)):
                                if (availableNums[avail] == sudokuPuzzle[i][y][0]):
                                    availableNums = availableNums[:avail] + availableNums[avail + 1:]
                                    break
                        # getting rid of possible nums from horizontal
                        if (len(sudokuPuzzle[x][i]) == 1):
                            for avail in range(len(availableNums)):
                                if (availableNums[avail] == sudokuPuzzle[x][i][0]):
                                    availableNums = availableNums[:avail] + availableNums[avail + 1:]
                                    break
                    # getting rid of possible nums from box
                    for boxX in range(boxStart[0], boxStart[0] + 3):
                        for boxY in range(boxStart[1], boxStart[1] + 3):
                            if (len(sudokuPuzzle[boxX][boxY]) == 1):
                                for avail in range(len(availableNums)):
                                    if (availableNums[avail] == sudokuPuzzle[boxX][boxY][0]):
                                        availableNums = availableNums[:avail] + availableNums[avail + 1:]
                                        break
                    for num in availableNums:
                        sudokuPuzzleCopy = deepcopy(sudokuPuzzle)
                        sudokuPuzzleCopy[x][y] = [num]
                        sudokuPuzzleCopy = sudokuSolver(sudokuPuzzleCopy)
                        if(sudokuPuzzleCopy != []):
                            return sudokuPuzzleCopy
            break
    return sudokuPuzzle


print("Original: ")
printSudoku(testSudoku)
solution = sudokuSolver(testSudoku)
print("Solution: ")
printSudoku(solution)