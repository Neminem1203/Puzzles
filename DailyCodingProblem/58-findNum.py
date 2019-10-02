'''
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''
import math
import random
debug = False

randomMax = 70
randomRemoves = 30
randomArray = [x for x in range(randomMax)]
for i in range(randomRemoves):
    randomIndex = random.randint(0, len(randomArray))
    randomArray = randomArray[:randomIndex] + randomArray[randomIndex+1:]
randomIndex = random.randint(0, len(randomArray))
randomArray = randomArray[randomIndex:] + randomArray[:randomIndex]

print("Index:",end="\t\t")
for x in range(len(randomArray)):
    print(x,end="\t")
print("\nNumbers:",end="\t")
for x in range(len(randomArray)):
    print(randomArray[x], end="\t")
print("\n")

def findNum(array, num):
    if debug: print("Finding ", num)
    operations = 0
    n = len(array)
    front = 0
    middle = int(n/2)
    end = n
    # this while loop is to find the max in the array
    # this takes approximately log(n) operations to find the max
    while True:
        if debug: print("Middle Index for finding Max:", middle)
        operations += 1
        if(array[(middle+1)%n] < array[middle] and array[middle-1]<array[middle]):
            break
        if(array[middle] < array[front]): # max is between 0 and n/2
            end = middle
            middle = int((end+front)/2)
        else:
            front = middle
            middle = int((end+front)/2)
    if debug:print()
    front = middle+1
    end = n+middle
    middle = int((end+front)/2)
    # apparently my program breaks if the number is not between lowest number and highest number
    if num < array[front%n] or num > array[end%n]:
        return None
    while True:
        operations += 1
        if(operations > n):
            break
        if debug: print("Front:",front%n,"End:",end%n,"\tMiddle Index for finding Num:",middle%n)
        if array[middle%n] == num:
            if debug: print("Loops: ", operations)
            return middle
        if num > array[middle%n]:
            if num < array[(middle+1)%n]:
                if debug: print("Loops: ", operations)
                return None
            front = middle
            middle = math.ceil((end+front)/2)
        else:
            if num > array[(middle-1)%n]:
                if debug: print("Loops: ", operations)
                return None
            end = middle
            middle = math.floor((end+front)/2)
    if debug: print("Exceeded number of operations for linear time")


findThisNum = random.randint(0,randomMax-1)
foundIndex = findNum(randomArray, findThisNum)
if foundIndex:
    print("Found num",findThisNum,"at",foundIndex%len(randomArray))
else:
    print("Can't find num ",findThisNum)