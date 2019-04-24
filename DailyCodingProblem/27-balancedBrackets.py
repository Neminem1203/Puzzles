'''
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''

def balancedBrackets(string):
    brackets = []
    frontDict =     {"[" : 0, "(" : 1 , "{" : 2}
    backDict =      {"]" : 0, ")" : 1 , "}" : 2}

    ind = -1
    for i in string:
        if i in frontDict:
            brackets.append(i)
            ind += 1
        elif i in backDict:
            if(ind > -1):
                if(frontDict[brackets[ind]] == backDict[i]):
                    brackets.pop(ind)
                    ind-=1
                else:
                    return False
            else:
                return False
    if(brackets):
        return False
    else:
        return True



print(balancedBrackets("([])[]({})"))
print(balancedBrackets("([)]" ))
print(balancedBrackets("((()"))