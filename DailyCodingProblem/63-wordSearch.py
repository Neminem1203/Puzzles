'''
Given a 2D matrix of characters and a target word, write a function that returns
whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''
def wordSearch(matrix, word):
    wordLen = len(word)
    xLen = len(matrix)
    yLen = len(matrix[0])
    def lookFor(x, y):
        if(x+wordLen<=xLen):
            found = True
            for wordInd in range(wordLen):
                if(word[wordInd] != matrix[x+wordInd][y]):
                    found = False
            if found: return True
        if(y+wordLen<=yLen):
            found = True
            for wordInd in range(wordLen):
                if (word[wordInd] != matrix[x][y + wordInd]):
                    found = False
            if found: return True
        return False

    for i in range((xLen - wordLen)+1):
        for j in range(yLen):
            if(matrix[i][j] == word[0]):
                if(lookFor(i,j)):
                    return [i,j]
    for i in range((xLen - wordLen)+1, xLen):
        for j in range(yLen-wordLen+1):
            if(matrix[i][j] == word[0]):
                if(lookFor(i,j)):
                    return [i,j]
    return False

passInMatrix = [['F', 'A', 'C', 'I'],
                ['O', 'B', 'Q', 'A'],
                ['A', 'N', 'B', 'R'],
                ['M', 'A', 'Z', 'E']]
print("FOAM: \t", wordSearch(passInMatrix, "FOAM"))
print("COPY: \t", wordSearch(passInMatrix, "COPY"))
print("MASS: \t", wordSearch(passInMatrix, "MASS"))
print("MAZE: \t", wordSearch(passInMatrix, "MAZE"))
print("ARE: \t", wordSearch(passInMatrix, "ARE"))
print("BAN: \t", wordSearch(passInMatrix, "BAN"))
print("ZZ: \t", wordSearch(passInMatrix, "ZZ"))