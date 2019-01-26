'''
https://www.geeksforgeeks.org/google-interview-experience-set-7-software-engineering-intern/
Question 1: Given a string A consisting of n characters and a string B consisting of m characters, write a function that will return the number of times A must be stated such that B is a substring of the repeated A. If B can never be a substring, return -1.

Example:
A = ‘abcd’
B = ‘cdabcdab’
The function should return 3 because after stating A 3 times, getting ‘abcdabcdabcd’, B is now a substring of A.

You can assume that n and m are integers in the range [1, 1000].
'''
import math

def repeatingSubString(firstString, secondString):
    if(len(firstString) > len(secondString)):
        str2 = str(firstString)
        str1 = str(secondString)
    else:
        str1 = str(firstString)
        str2 = str(secondString)
    str1len = len(str1)
    ind = 0
    for i in str1:
        if(str2[0] == i):
            break
        ind+=1

    for i in str2:
        if i == str1[ind%str1len]:
            ind+=1
        else:
            return -1
    return math.ceil(ind/str1len)

A = 'abcd'
B = 'cdabcdab'
C = 'cdabcab'
D = 'bcdabcdabcdabcda'
