'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''


def maxContiguousSum(array):
    maxSum = 0
    sumSoFar = 0
    for num in array:
        sumSoFar += num
        if(sumSoFar < 0):
            sumSoFar = 0
            continue
        if(maxSum < sumSoFar):
            maxSum = sumSoFar
    return maxSum

print(maxContiguousSum([34, -50, 42, 14, -5, 86]))
print(maxContiguousSum([-5, -1, -8, -9]))