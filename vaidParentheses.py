def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    openers = ['(', '{', '[']
    closers = [')', '}', ']']
    complement = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in s:
        if char in openers:
            stack += [char]
        if char in closers:
            if len(stack) == 0 or complement[char] != stack[-1]:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    return False

print(isValid("()[]{}")) # True
print(isValid("{[]}")) # True
print(isValid("([)]")) # False