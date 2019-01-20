'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def fmpi(arr):
    if not arr:
        return 1
    i = 0
    steps = 0
    while(i < len(arr)):
        if arr[i] > 0  and arr[i] < len(arr)+1 and arr[i] != arr[arr[i]-1]:
            temp = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = temp
            i -= 1
        i += 1
        steps += 1
    for i in range(len(arr)):
        steps+=1
        if i+1 != arr[i]:
            print(arr, steps)  # to see the list reordered and the amount of steps taken
            return i+1
    print(arr, steps) # to see the list reordered and the amount of steps taken
    return len(arr)+1



print(fmpi([3,4,-1,1]))
print(fmpi([1,2,0]))
print(fmpi([1,2,3]))
print(fmpi([7,6,0,-2,2,9,3,10,5,1,8]))
print(fmpi([7,6,0,-2,2,9,3,10,5,1,8,4]))