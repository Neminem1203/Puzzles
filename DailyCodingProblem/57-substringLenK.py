'''
Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less.
 You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
'''


def substringLenK(string, k):
    previousStart = 0
    previousSpace = -1
    returnSubString = []
    ind = 0
    while(ind < len(string)):
        if(ind - previousStart == k+1):
            returnSubString += [string[previousStart:previousSpace]]
            previousStart = previousSpace+1
            previousSpace = previousStart
        if string[ind] == ' ':
            previousSpace = ind
        ind += 1
    returnSubString += [string[previousStart:]]
    return returnSubString

print(substringLenK("the quick brown fox jumps over the lazy dog", 10))