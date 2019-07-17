'''
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''


def medianList(list):
    def insert(seqList, number):
        if(seqList == []):
            return [number]
        for ind, num in enumerate(seqList):
            if num > number:
                return seqList[:ind] + [number] + seqList[ind:]
        return seqList + [number]

    median = 0
    sequence = []
    for i in list:
        sequence = insert(sequence, i)
        if(median % 1 == 0):
            medianInt = int(median)
            print(sequence[medianInt])
        else:
            print((sequence[int(median+0.5)] + sequence[int(median-0.5)])/2)
        median += 0.5

medianList([2, 1, 5, 7, 2, 0, 5])