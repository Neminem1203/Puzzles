'''
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

def starCheck(expressionList, string):
    star = True
    while(expressionList):
        if(expressionList[0] == "*"):
            star = True
            expressionList.pop(0)

            if(not expressionList):
                return True
        elif(expressionList[0] == "."):
            if(string):
                expressionList.pop(0)
                string = string[1:]
            else:
                return False
        else:
            if(not star):
                if string[:len(expressionList[0])] == expressionList[0]:
                    string = string[len(expressionList[0]):]
                    expressionList.pop(0)
                    star = False
            elif(star):
                while(not starCheck(expressionList[1:], string[string.find(expressionList[0])+len(expressionList[0]):])):
                    if(string.find(expressionList[0]) > 0):
                        string = string[string.find(expressionList[0])+1:]
                    else:
                        return False
                if(string.find(expressionList[0]) == -1):
                    return False
                string = string[string.find(expressionList[0])+len(expressionList[0]):]
                expressionList.pop(0)
                if(not expressionList):
                    if(string):
                        return False
                    else:
                        return True
    if(string):
        return False
    else:
        return True


def customRegex(expression, string):
    newExpression = []
    expressionSubstr = ''
    for i in expression:
        if i == "*" or i == ".":
            if(expressionSubstr):
                newExpression.append(expressionSubstr)
            expressionSubstr = ""
            newExpression.append(i)
            continue
        expressionSubstr += i
    if (expressionSubstr):
        newExpression.append(expressionSubstr)

    while(string and newExpression):
        if(newExpression[0] == '.'):
            if(string):
                string=string[1:]
                newExpression.pop(0)
            else:
                return False
        elif(newExpression[0] != "*"):
            if((len(newExpression[0]) > len(string)) or (newExpression[0] != string[:len(newExpression[0])])):
                return False
            else:
                string = string[len(newExpression[0]):]
                newExpression.pop(0)
        else:
            return starCheck(newExpression[1:], string)
    if(string):
        return False
    return True



regex1 = ".*at"
string1 ="chat"
string4 = "chats"
regex2 = "ra."
string2 = "ray"
string3 = "raymond"


# print(regex1, string1, customRegex(regex1, string1))
# print(regex1, string4, customRegex(regex1, string4))
# print(regex2, string2, customRegex(regex2, string2))
# print(regex2, string3, customRegex(regex2, string3))

hardregex1 = ".*fly."
hardstring1 = "azxcsflyadflys"
hardregex2 = ".*fly*.cookie."
hardstring2 = "sdflyacsokcookiesdloflycookiea"
print(hardregex1,hardstring1 , customRegex(hardregex1, hardstring1))
print(hardregex2, hardstring2, customRegex(hardregex2, hardstring2))
print(hardregex2, hardstring2[:-1], customRegex(hardregex2, hardstring2[:-1]))
