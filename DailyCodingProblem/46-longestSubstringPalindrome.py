'''
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''

def longestSubstringPalindrome(string):
    strings = [string]
    while(strings != []):
        # print(strings)
        left = int(len(strings[0])/2)
        right = len(strings[0])-left-1
        # print(strings[0][:left], strings[0][-1:right:-1])
        if(strings[0][:left] == strings[0][-1:right:-1]):
            return strings[0]
        else:
            if(strings[0][1:] != ''):
                strings += [strings[0][1:]]
            if(strings[0][:-1] != ''):
                strings += [strings[0][:-1]]
            strings = strings[1:]

print(longestSubstringPalindrome("aabcdcb"))
print(longestSubstringPalindrome("bananas"))