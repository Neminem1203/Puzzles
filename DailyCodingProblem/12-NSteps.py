'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

def steps(N): # AKA Fibbonaci
    num1 = 0
    num2 = 1
    for i in range(N):
        temp = num2
        num2 += num1
        num1 = temp
    return num2

def setSteps(N, steps):

    pass


print(steps(4))
print(setSteps(4,[1,3,5]))