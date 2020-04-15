# https://leetcode.com/problems/count-and-say/
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    say = 1
    for i in range(n-1):
        newSay = 0
        sayString = str(say)
        oldChar = sayString[0]
        count = 0
        for j in sayString:
            if(j == oldChar):
                count += 1
            else:
                newSay *= 100
                newSay += (count * 10) + int(oldChar)
                count = 1
            oldChar = j
        newSay *= 100
        newSay += (count*10) + int(sayString[len(sayString)-1])
        # print(newSay)
        say = newSay
    print(say)
    return say


countAndSay(1)
countAndSay(2)
countAndSay(3)
countAndSay(4)
countAndSay(5)