'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def threeSums(nums):
    twoNums = {}
    answer = []

    for ind in range(len(nums)):
        num = nums[ind]
        if num in twoNums:
            for sublist in twoNums[num]:
                answer += [sublist + [num]]
        for i in range(ind):
            requiredNum = 0 - (num + nums[i])
            if not requiredNum in twoNums:
                twoNums[requiredNum] = []

            if not [[num, nums[i]]] in twoNums[requiredNum]:
                twoNums[requiredNum] += [[num, nums[i]]]

    print(answer)



threeSums([-1, 0, 1, 2, -1, -4, 2])
