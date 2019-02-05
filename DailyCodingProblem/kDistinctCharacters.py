'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''


def distinctCharacters(s,k):
    lst = [["", 0]]
    for ind, char in enumerate(s):
        # for test in lst:
        #     if(len(lst[0] < k) and char not in lst[0]):
        #         lst.append([lst[ind]+char, lst[ind]])
        return



s = "abcba"
k = 2

print(distinctCharacters(s,k))