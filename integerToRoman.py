# https://leetcode.com/problems/integer-to-roman/

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    dict = {"":0,"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = num
    roman = ""
    while(total > 0):
        if(total >= 1000):
            total -= 1000
            roman += "M"
        elif(total >= 900):
            total -= 900
            roman += "CM"
        elif(total >= 500):
            total -= 500
            roman += "D"
        elif(total >= 400):
            total -= 400
            roman += "CD"
        elif(total >= 100):
            total -= 100
            roman += "C"
        elif(total >= 90):
            total -= 90
            roman += "XC"
        elif(total >= 50):
            total -= 50
            roman += "L"
        elif(total >= 40):
            total -= 40
            roman += "XL"
        elif(total >= 10):
            total -= 10
            roman += "X"
        elif(total >= 9):
            total -= 9
            roman += "IX"
        elif(total >= 5):
            total -= 5
            roman += "V"
        elif(total >= 4):
            total -= 4
            roman += "IV"
        else:
            roman += "I"*total
            total = 0
    print(roman)


intToRoman(3)
intToRoman(4)
intToRoman(58)
intToRoman(1994)