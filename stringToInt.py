# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    value = 0
    negative = 1
    for char in str:
        if ord(char) == ord(" "):
            continue
        elif ord(char) == ord("-"):
            negative = -1
        elif ord(char) >= ord("0") and ord(char) <= ord("9"):
            value *= 10
            value += ord(char) - ord("0")
        else:
            break
    if value > 2147483648: # pretending to have a limit
        value = 2147483648
    return value * negative

print(myAtoi("91"))
print(myAtoi("   -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))