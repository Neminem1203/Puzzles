# https://leetcode.com/problems/roman-to-integer/

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict = {"":0,"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    prevSymb = ""
    lenS = len(s)
    count = 0
    sum = 0
    totalSum = 0
    while(count < lenS):
        char = s[count]
        if(char == prevSymb):
            sum += dict[char]
        elif(dict[char] > dict[prevSymb]):
            sum = dict[char] - sum
        else:
            totalSum += sum
            sum = dict[char]
        prevSymb = char
        count += 1

    totalSum += sum
    print(totalSum)

romanToInt("LVIII")
romanToInt("MCMXCIV")