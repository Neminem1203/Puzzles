# https://www.hackerrank.com/challenges/fibonacci-modified/problem

fib = [0, 1]

def fibMod(n):
    global fib
    while n > len(fib):
        fib += [fib[-2] + fib[-1]**2]
    return fib[n-1]


print(fibMod(5))
print(fibMod(3))
print(fibMod(8))

