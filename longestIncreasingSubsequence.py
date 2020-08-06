'''
Daily Coding Problem: Problem #75
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

def longestInreasingSubsequence(array):
    longest = 0
    longest_arr = []
    for num in array:
        while len(longest_arr) > 0 and longest_arr[-1] > num:
            longest_arr = longest_arr[:-1]
        longest_arr += [num]
        if len(longest_arr) > longest:
            longest = len(longest_arr)
        if longest == 5:
            print(longest_arr)

    return longest

print(longestInreasingSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))