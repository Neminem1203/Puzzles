# https://leetcode.com/problems/powx-n/
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    negative = False if n > 0 else True
    c = abs(n)-1
    total = x*x
    while(c > 0):
        if(c%2 == 0):
            total *= total
        else:
            total *= x
    if negative:
        return 1/total
    else:
        return total


print(pow(2.0000, 10)) # 1024.00000
print(pow(2.1000, 3)) # 9.26100
print(pow(2.0000, -2)) # 0.25000
print(pow(2.0000, 24)) # 16777216.0