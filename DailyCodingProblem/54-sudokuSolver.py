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
testSudoku = [[[5], [ ], [ ], [ ], [9], [ ], [ ], [ ], [2]],
              [[7], [6], [ ], [5], [ ], [1], [8], [9], [ ]],
              [[ ], [3], [ ], [8], [2], [6], [1], [5], [7]],
              [[6], [2], [ ], [9], [ ], [7], [5], [8], [1]],
              [[8], [ ], [4], [3], [5], [2], [9], [ ], [ ]],
              [[ ], [ ], [7], [ ], [6], [ ], [2], [ ], [ ]],
              [[3], [4], [8], [6], [ ], [9], [7], [ ], [ ]],
              [[ ], [7], [ ], [ ], [ ], [5], [3], [1], [ ]],
              [[1], [9], [ ], [ ], [7], [ ], [4], [ ], [8]]]
# testSudoku = [[[ ], [ ], [8], [ ], [ ], [5], [ ], [4], [ ]],
#               [[ ], [ ], [1], [ ], [ ], [8], [9], [2], [ ]],
#               [[ ], [3], [ ], [1], [ ], [ ], [8], [ ], [ ]],
#               [[ ], [ ], [6], [4], [ ], [ ], [ ], [9], [ ]],
#               [[ ], [ ], [7], [ ], [5], [ ], [6], [ ], [ ]],
#               [[ ], [8], [ ], [ ], [ ], [7], [2], [ ], [ ]],
#               [[ ], [ ], [4], [ ], [ ], [2], [ ], [3], [ ]],
#               [[ ], [2], [3], [6], [ ], [ ], [4], [ ], [ ]],
#               [[ ], [5], [ ], [8], [ ], [ ], [1], [ ], [ ]]]

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
    amountOfEmpty = 0
    firstRun = False
    while(True):
        prevEmpty = amountOfEmpty
        amountOfEmpty = 0
        for x in range(9):
            for y in range(9):
                if(len(sudokuPuzzle[x][y]) != 1):
                    amountOfEmpty += 1
                    availableNums = [i+1 for i in range(9)]
                    boxStart = [int(x / 3) * 3, int(y / 3) * 3]
                    for i in range(9):
                        if(len(sudokuPuzzle[i][y]) == 1):
                            for avail in range(len(availableNums)):
                                if(availableNums[avail] == sudokuPuzzle[i][y][0]):
                                    availableNums = availableNums[:avail] + availableNums[avail+1:]
                                    break
                        if(len(sudokuPuzzle[x][i]) == 1):
                            for avail in range(len(availableNums)):
                                if(availableNums[avail] == sudokuPuzzle[x][i][0]):
                                    availableNums = availableNums[:avail] + availableNums[avail+1:]
                                    break
                    for boxX in range(boxStart[0], boxStart[0]+3):
                        for boxY in range(boxStart[1], boxStart[1]+3):
                            if(len(sudokuPuzzle[boxX][boxY]) == 1):
                                for avail in range(len(availableNums)):
                                    if (availableNums[avail] == sudokuPuzzle[boxX][boxY][0]):
                                        availableNums = availableNums[:avail] + availableNums[avail + 1:]
                                        break
                    sudokuPuzzle[x][y] = availableNums
                    if(len(availableNums) == 0):
                        return []
                    # print("X: ",x, "Y: ",y,"\t",availableNums)
                    if(len(availableNums) == 1):
                        sudokuPuzzle[x][y] = availableNums
                        amountOfEmpty -= 1
        # print("Amount of Empties: ",amountOfEmpty)
        # printSudoku(sudokuPuzzle)
        if(amountOfEmpty == 0):
            break
        if(prevEmpty == amountOfEmpty):
            return []
        firstRun = True
    return sudokuPuzzle
            # print("X: ", x, "\tY: ", y, "\t", availableNums, "\n : ",boxStart[0],"\t : ", boxStart[1])



    # def horizontalFill(line):
    #     availableNumbers = [i for i in range(1,10)]
    #     for num in line:
    #         if num != ' ':
    #             for index, availNum in enumerate(availableNumbers):
    #                 if(str(availNum) == num):
    #                     availableNumbers = availableNumbers[:index] + availableNumbers[index+1:]
    #                     continue
    #     return availableNumbers
    #
    # horizontalEmpties = [0 for x in range(9)]
    # # checks and fills what's available based on the horizontal
    # for line in range(9):
    #     newLine = horizontalFill(sudokuPuzzle[line])
    #     horizontalEmpties[line] = len(newLine)
    #     for ind in range(9):
    #         if sudokuPuzzle[line][ind] == ' ':
    #             sudokuPuzzle[line][ind] = newLine
    # print(horizontalEmpties)


print("Original: ")
printSudoku(testSudoku)
print("Solution: ")
printSudoku(sudokuSolver(testSudoku))
