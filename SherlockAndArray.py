# https://www.hackerrank.com/challenges/sherlock-and-array/problem

def sherlockArray(array):
    sum = 0
    for i in array:
        sum += i
    leftSum = 0
    for i in array:
        sum -= i
        if sum == leftSum:
            return "YES"
        leftSum += i
    return "NO"

print(sherlockArray([1,2,3,3])) # YES
print(sherlockArray([1,2,3])) # NO
print(sherlockArray([1,1,4,1,1])) # YES
print(sherlockArray([2,0,0,0])) # YES
print(sherlockArray([0,0,2,0])) # YES