def mutateChars(ind, count, chars):
    increment = 0
    while count != 0:
        chars.insert(ind, str(count % 10))
        count = int(count / 10)
        increment += 1
    return increment

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    prev_char = chars[0]
    count = 1
    ind = 1
    while ind < len(chars):
        char = chars[ind]
        if prev_char == char:
            count += 1
            chars.pop(ind)
            ind -= 1
        else:
            if count > 1:
                ind += mutateChars(ind, count, chars)
            prev_char = char
            count = 1
        ind += 1
    if count > 1:
        mutateChars(ind, count,chars)
    return len(chars)

test = ["a","b","b","b","b", "c", "c", "c", "c","b","b","b","b","b","b","b","b"]
print(compress(test))
print(test)