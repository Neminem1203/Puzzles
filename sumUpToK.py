'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def sumUpToK(listOfNumbers, k):
    setOfComplements = set()
    for i in listOfNumbers:
        if(i in setOfComplements):
            return True
        setOfComplements.add(k-i)
    return False

print(sumUpToK([10,15,3,7], 17))