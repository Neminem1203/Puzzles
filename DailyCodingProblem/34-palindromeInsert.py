'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

def palindromeInsert(word):
    checkInd = 0
    newWord = ""
    dupeWords = []
    for i in word:
        newWord += i
    while(checkInd < len(newWord)):
        if newWord[checkInd] in newWord[checkInd:]:
            for ind in range(len(newWord)-1, checkInd, -1):
                if(newWord[ind] == newWord[checkInd]):
                    dupeWords += [newWord[checkInd]]
                    newWord = newWord[:checkInd] + newWord[(checkInd+1):ind] + newWord[(ind+1):]
                    checkInd -= 1
                    break
        checkInd += 1
    palindrome = ""
    while(dupeWords != [] and newWord != ""):
        if(word[-1] == dupeWords[0]):
            palindrome += dupeWords[0]
            dupeWords = dupeWords[1:]
            word = word[:-1]
            continue
        palindrome += newWord[-1]
        newWord = newWord[:-1]
        word = word[:-1]
    if(dupeWords == []):
        palindrome += newWord[-1:0:-1]
        palindrome = palindrome + newWord[0] + palindrome[::-1]
    if(newWord == ""):
        for i in dupeWords:
            palindrome += i
        palindrome = palindrome + palindrome[::-1]
    print(palindrome)

breakTest = "ramgrma" # This should be ramrgrmar but my program gives me grammarg which is completely wrong
# Idea: use a pivot point for the words if there's no pairs in the middle
secondTest = "ragamaror" #roramagamaror
palindromeInsert(breakTest)
palindromeInsert(secondTest)
palindromeInsert("google")
palindromeInsert("race")
palindromeInsert("ragaaz")
