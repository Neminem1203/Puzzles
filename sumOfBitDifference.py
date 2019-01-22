'''
https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).

Examples :

Input: arr[] = {1, 2}
Output: 4
All pairs in array are (1, 1), (1, 2)
                       (2, 1), (2, 2)
Sum of bit differences = 0 + 2 +
                         2 + 0
                      = 4

Input:  arr[] = {1, 3, 5}
Output: 8
All pairs in array are (1, 1), (1, 3), (1, 5)
                       (3, 1), (3, 3) (3, 5),
                       (5, 1), (5, 3), (5, 5)
Sum of bit differences =  0 + 1 + 1 +
                          1 + 0 + 2 +
                          1 + 2 + 0
                       = 8
'''
import math

def bitDiff(arr):
    num = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            bits = arr[i] ^ arr[j]
            if (bits % 2 == 1):
                bits -= 1
                num += 1
            while(bits > 0):
                bits -= 2**math.floor(math.log(bits)/math.log(2))
                num += 1
    return num * 2

print(bitDiff([1,2]))
print(bitDiff([1,3,5]))