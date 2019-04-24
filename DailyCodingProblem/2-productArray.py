'''
Daily Coding Problem: Problem #2

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def productArray(arr):
    product = 1
    for i in arr:
        product*=i
    newarr = [product]*len(arr)
    for i in range(len(newarr)):
        newarr[i] = int(newarr[i]/arr[i])
    return newarr

print(productArray([1, 2, 3, 4, 5]))
print(productArray([3, 2, 1]))

def productArrayNoDiv(arr):
    newarr = []
    for i in range(len(arr)):
        newarr.append(1)
        for j in range(len(arr)):
            if(i!=j):
                newarr[i]*=arr[j]
    return newarr

print(productArrayNoDiv([1, 2, 3, 4, 5]))
print(productArrayNoDiv([3, 2, 1]))
