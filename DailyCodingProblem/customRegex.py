'''
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

def starCheck(expressionList, string):
    return False


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
            string=string[1:]
            newExpression.pop(0)
        elif(newExpression[0] != "*"):
            if(newExpression[0] != string[:len(newExpression[0])]):
                return False
            else:
                string = string[len(newExpression[0]):]
                newExpression.pop(0)
        else:
            return starCheck(newExpression, newExpression[1:])
    if(string):
        return False
    return True



regex1 = ".*at"
string1 ="chat"
string4 = "chats"
regex2 = "ra."
string2 = "ray"
string3 = "raymond"


# customRegex(regex1, string1)
# customRegex(regex1, string4)
print(customRegex(regex2, string2))
print(customRegex(regex2, string3))