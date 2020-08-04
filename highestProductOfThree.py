'''
Daily Coding Problem: Problem #69
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
'''

def largestOfThreeProducts(intList):
    positives = []
    negatives = []
    for num in intList:
        ind = 0
        if num >= 0:
            while ind < len(positives) and num > positives[ind]:
                ind += 1
            positives = positives[:ind] + [num] + positives[ind:]
            if len(positives) > 3:
                positives = positives[-3:]
        else:
            while ind < len(negatives) and num < negatives[ind]:
                ind += 1
            negatives = negatives[:ind] + [num] + negatives[ind:]
            if len(negatives) > 2:
                negatives = negatives[-2:]
    if len(negatives) > 1:
        highest_negative = negatives[-1] * negatives[-2]
    if len(positives) < 3:
        return positives[-1] * highest_negative
    if positives[0] == 0:
        return highest_negative * positives[-1]
    if len(positives) > 1:
        highest_positive = positives[-1] * positives[-2]
    return highest_negative * positives[-1] if highest_negative > highest_positive else highest_positive * positives[0]

print(largestOfThreeProducts([10, -11, 7, -10, 5, -6, -12, 2, 12]))
print(largestOfThreeProducts([12, 11, -5, -2]))
print(largestOfThreeProducts([0, 5, -5, -2, 0]))
print(largestOfThreeProducts([5, 5, -5, -2, 0]))