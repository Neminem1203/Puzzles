# Given a string of brackets, how many brackets are required to close up all the brackets
# )()) requires 2 because the first ) is open and the last ) is open.

def bracket_match(bracket_string):
    num = 0
    left = 0
    for i in bracket_string:
        if i == '(':
            left += 1
            num += 1
        elif i == ')':
            if left > 0:
                left -= 1
                num -= 1
            else:
                num += 1
    return num

print(bracket_match(")())"))