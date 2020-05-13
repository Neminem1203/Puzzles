# https://leetcode.com/problems/remove-k-digits/submissions/
def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    remainingK = k
    prevNum = 0
    newNum = ""
    for i in range(len(num)):
        if remainingK > 0:
            if newNum == 0:
                newNum += prevNum
                prevNum = 0
            elif prevNum == 0:
                prevNum = num[i]
                continue
            else:
                if prevNum > num[i]:
                    prevNum = num[i]
            remainingK -= 1
        else:
            if prevNum != "0":
                newNum += prevNum
                prevNum = "0"
            newNum += num[i]

    if newNum == "":
        return 0
    return newNum




print(removeKdigits("1432219", 3))
print(removeKdigits("10200", 1))
print(removeKdigits("10", 2))
print(removeKdigits("9241230",4))