'''
Daily Coding Problem #66
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
'''
import random

RANDOM_BIAS = random.randint(1, 99)
def toss_biased():
    rand_num = random.randint(0,100)
    return 1 if rand_num > RANDOM_BIAS else 0

def toss_unbiased():
    sum = 0
    for _ in range(100):
        sum += toss_biased()
    return 1 if sum % 2 else 0

sum = 0
for _ in range(1000):
    sum += toss_unbiased()

# Debugger to check the random bias and the average of the toin coss
print(RANDOM_BIAS)
print(sum)