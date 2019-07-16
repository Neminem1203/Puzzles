'''
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''

def editDistance(string1, string2):
    if(len(string1) > len(string2)):
        longerString = string1
        shorterString = string2
    else:
        longerString = string2
        shorterString = string1
    shortestDistance = len(longerString)
    def recursiveCheck(lString, sString, dist, shortestDistance):
        # print(lString, sString, dist)
        if(lString == "" or sString == ""):
            return dist + len(lString) + len(sString)
        while(lString[0] == sString[0]):
            lString = lString[1:]
            sString = sString[1:]
            if(lString == '' or sString == ""):
                return dist + len(lString) + len(sString)

        deleteDist = recursiveCheck(lString[1:], sString, dist+1, shortestDistance)
        subDist = recursiveCheck(lString[1:], sString[1:], dist+1, shortestDistance)
        newDist = [subDist, deleteDist][deleteDist < subDist]
        if(newDist < shortestDistance):
            shortestDistance = newDist
        return shortestDistance

    return recursiveCheck(longerString, shorterString, 0, shortestDistance)


def findTheDistance(str1, str2):
    print("Edit Distance between ", str1, " and ", str2, ": ", editDistance(str1, str2))

findTheDistance("party", "chartly")
findTheDistance("jack of all trades", "jackal")