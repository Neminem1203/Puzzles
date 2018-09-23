# 0s
# 1 1 n
#

# 1 x n = (n-x)! + (3-x)*2
# 1 n n = 1
# 2 2 3 = 2
# 1 2 6 = 24
import math
import itertools
def answer(x, y, n):

    # 0 cases
    if x + y > n + 1:
        return 0
    if x == 1 and y == 1:
        return 0

    if x == 1:
        if y == n:
            return 1
        if y == 2:
            return math.factorial(n-2)
    if y == 1:
        if x == n:
            return 1
        if x == 2:
            return math.factorial(n-2)


    return 0




# Brute Force Solution Checker
def view(lst,ansx, ansy):
    x = 1
    y = 1
    prev = lst[0]
    for i in range(1,len(lst)):
        if(prev < lst[i]):
            prev = lst[i]
            x += 1
    if(ansx != x):
        return False
    prev = lst[len(lst)-1]
    for i in range(len(lst)-1, -1, -1):
        if (prev < lst[i]):
            prev = lst[i]
            y += 1
    if(ansy != y):
        return False
    return True



x = 1
y = 3
print("X: ",x,"\tY: ",y,end='\t')

# n = 6
# print("N: ",n, "\nMine: ",answer(x,y,n),end='')
print('\n')

for n in range(3,10):
    sum = 0
    test = [i+1 for i in range(n)]
    perm = itertools.permutations(test)
    for i in perm:
        if(view(i,x,y)):
            sum+=1
            # print(i)
    print(n,": ",sum)


# n = 7
# print("N: ",n)
# # print("Mine: ",answer(x,y,n))
# lst = [[0 for i in range(n-1)] for j in range(n-1)]
# for x in range(1,n):
#     for y in range(1,n):
#         test = [i+1 for i in range(n)]
#         perm = itertools.permutations(test)
#         for i in perm:
#             if(view(i, x, y)):
#                 lst[x-1][y-1]+=1
#
#
# for i in range(n-1):
#     print("\t   ",i+1,end='')
# print()
# for n, i in enumerate(lst):
#     print(n+1, *i, sep='   \t')