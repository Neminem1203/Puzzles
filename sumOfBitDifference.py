'''
https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements. Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).
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