# https://www.reddit.com/r/dailyprogrammer/comments/8gzaz5/20180504_challenge_359_hard_primes_in_grids/
# needs improvement
import math

#code from online (should make my own in the future)
def checkPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    i = 3
    sqrtOfNumber = math.sqrt(number)

    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i + 2

    return True

n = int(input(''))
s = set()
grid = [[i for i in input('')] for j in range(n)]
for i in grid:
    print(i)

#horizontal
for i in range(n):
    for j in range(n):
        x = ''
        y = ''
        for k in range(j, n):
            x+=grid[i][k]
            s.add(x)
        for k in range(n-1, j-1, -1):
            y+=grid[i][k]
            s.add(y)
        # print(x,y)

# print(s,len(s))

#vertical
for i in range(n):
    for j in range(n):
        x = ''
        y = ''
        for k in range(i, n):
            x+=grid[k][j]
            s.add(x)
        for k in range(n-1, i-1, -1):
            y+=grid[k][j]
            s.add(y)
        # print(x,y)


# diagonal (top left to bottom right)
for i in range(n):
    for j in range(n):
        x = ''
        y = ''

        for k in range(n):
            if(i+k < n and j+k < n):
                x+=grid[i+k][j+k]
            s.add(x)

        for k in range(n,-1,-1):
            if (i+k < n and j+k < n):
                y += grid[i+k][j+k]
            s.add(y)
        # print(x,y)


# diagonal (top right to bottom left)
for i in range(n):
    for j in range(n):
        x = ''
        y = ''
        for k in range(n):
            if(i+k < n and j-k >= 0):
                x+=grid[i+k][j-k]
            s.add(x)

        for k in range(n,-1,-1):
            if (i+k < n and j-k >= 0):
                y += grid[i+k][j-k]
            s.add(y)
        # print(x,y)

s.discard('')
s.discard('1')
primeList = []
num = 0
for i in s:
    if(checkPrime(int(i))):
        num += 1
        primeList.append(i)

print(num)
print(primeList)