# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/

def findKthPositive(arr, k):
    if k < arr[0]:
        return k
    count = 0
    ind = 0
    lastPositive = 0
    while ind < len(arr):
        if arr[ind] != lastPositive+1:
            if k - count < arr[ind] - lastPositive:
                return lastPositive + k - count
            else:
                count += arr[ind] - lastPositive - 1
        lastPositive = arr[ind]
        ind += 1
    return k - count + arr[-1]

print(findKthPositive([8,17,23,34,37,42], 16)) #18
print(findKthPositive([1,3], 1)) # 2
print(findKthPositive([2,3,4,7,11], 5)) # 9
print(findKthPositive([1,2,3,4], 2)) # 6