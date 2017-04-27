# https://www.reddit.com/r/dailyprogrammer/comments/64y4cf/20170412_challenge_310_intermediate_simplifying/

import math

def findSquares(num):
    for i in range(2, (num + 2) // 2 ):
        if(num % (i*i)  == 0):
            return i
    return -1

def GCD(num1, num2):
    if(num1 > num2):
        num = num2
    else:
        num = num1

    for i in range(num,1,-1):
        if(num1 % i == 0) and (num2 % i == 0):
            return i
    return 1

for i in range(2,2,-1):
    print(i)

numList = input("Enter the 4 numbers: ").split()
if(len(numList) != 4):
    print("Error. Not 4 numbers.", len(numList), "numbers input")
else:
    print(numList[0],"√",numList[1],"/",numList[2],"√",numList[3])
    numList[1] = int(numList[1]) * int(numList[3])
    numList[2] = int(numList[2]) * int(numList[3])
    del numList[3]
    while(findSquares(int(numList[1])) != -1):
        num = findSquares(int(numList[1]))
        numList[0] = num * int(numList[0])
        numList[1] = int(numList[1]) / (num*num)

    GCDNum = GCD(int(numList[0]), int(numList[2]))
    if(GCDNum != 1):
        numList[0] = int(numList[0]) / GCDNum
        numList[2] = int(numList[2]) / GCDNum
    print(numList)