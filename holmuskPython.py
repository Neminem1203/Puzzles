'''
Problem Solving (not coding):
Given an hourglass that measures 7 min, and another that measures 4 min, how will you measure 9 min ?
There may be more than one way to do this, give the best solution you can.

Solution:
7m = 7 min hourglass
4m = 4 min hourglass
1. Have both 7 min and 4 min running. (7m has 7 minutes, 4m has 4 minutes)
Once the 4 min runs out, reset it. (7m has 3 minutes, 4m has 4 minutes)
Once the 7 runs out, 3 mins have passed, and 4 minutes now has 1 minute. (7m has 0 minutes, 4m has 1 minute).

Now all we have to do is run out the one minute and reset the 4 minute hour glass 2 times (1 + 4 + 4 = 9 minutes)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coding (python):

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


def longestConsecutiveElements(list):
    seen = {}
    for num in list:
        seen[num] = True
    longest = 0
    for num in list:
        sequence = 1
        seen[num] = False

        # numbers backwards
        i = num-1
        while True:
            if seen.get(i) == True:
                seen[i] = False
                sequence += 1
            else:
                break
            i -= 1
        i = num + 1

        # numbers forward
        while True:
            if seen.get(i) == True:
                seen[i] = False
                sequence += 1
            else:
                break
            i += 1
        if sequence > longest:
            longest = sequence
    return longest

# simple print statement for testing
def test(lists):
    for list in lists:
        print(longestConsecutiveElements(list))

# test cases
test([
        # answer should be 4 because [1, 2, 3, 4]
        [100, 4, 200, 1, 3, 2],
        # answer should be 3 because [2, 3, 4]
        [100, 4, 200, 300, 2, 3, 400],
        # answer should be 3 because [5, 6, 7]
        [1, 3, 5, 7, 6],
         # add more test cases here seperated by commas at the end as shown above
         ])
