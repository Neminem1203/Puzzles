'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

perfect_sums = [10]

def digitalSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num/10)
    return sum


def nthPerfectSum(n):
    global perfect_sums
    if n < len(perfect_sums):
        return perfect_sums[n]
    num = perfect_sums[-1]+1
    while n >= len(perfect_sums):
        num += 1
        if digitalSum(num) == 10:
            perfect_sums += [num]
    return perfect_sums[-1]


print(nthPerfectSum(15))
print(perfect_sums)