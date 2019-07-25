'''
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
'''

numPossibilities = 0

def nQueens(num, positions=[]):
    global numPossibilities
    posLens = len(positions)
    for i in range(0, num):
        availablePosition = True
        if(posLens > 0):
            # testing to see if any positions conflict with this new position
            for posInd in range(len(positions)):
                if(positions[posInd] == i or positions[posInd] == i + (posLens-posInd) or positions[posInd] == i - (posLens-posInd)):
                    availablePosition = False
                    break
            if(availablePosition):
                if(posLens == num-1):
                    numPossibilities += 1
                    # print(positions+[i]) # uncomment this out to see all the possible positions
                else:
                    nQueens(num, positions + [i])
            else:
                continue
        else:
            nQueens(num, [i])
    return numPossibilities

print(nQueens(8))