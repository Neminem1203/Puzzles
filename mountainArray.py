# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

def validMountainArray(arr):
    if len(arr) < 3:
        return False
    asc = False
    dec = False
    curr = 1
    prev = arr[0]
    while curr < len(arr) and arr[curr] > prev:
        asc = True
        prev = arr[curr]
        curr += 1

    while curr < len(arr) and arr[curr] < prev:
        dec = True
        prev = arr[curr]
        curr += 1

    return True if curr == len(arr) and asc and dec else False


print(validMountainArray([0,2,3,4,5,2,1,0]))
print(validMountainArray([0,2,3,3,5,2,1,0]))
print(validMountainArray([0,3,2,1]))