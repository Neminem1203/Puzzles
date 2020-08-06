'''
Daily Coding Problem: Problem #75
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''



if False:
    # Suboptimal Solution
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
else:
    def longestInreasingSubsequence(array):
        def helper(arr, current=[]):
            if len(arr) == 0:
                return len(current)
            max = 0
            for ind in range(len(arr)):
                if len(current) == 0 or arr[ind] > current[-1]:
                    val = helper(arr[ind+1:], current+[arr[ind]])
                    if val > max:
                        max = val
            if max == 0:
                return len(current)
            return max
        return helper(array)





print(longestInreasingSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))