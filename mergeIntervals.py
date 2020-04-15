# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    newInts = []
    for ints in intervals:
        newInterval = [ints[0], ints[1]]
        print(newInts)
        idx = 0
        while(idx < len(newInts)):
            if newInts[idx][0] < newInterval[0] and newInts[idx][1] and newInts[idx][1] > newInterval[1]:
                newInterval[0] = newInts[idx][0]
                newInterval[1] = newInts[idx][1]
                del newInts[idx]
            elif newInts[idx][0] <= newInterval[1] and newInts[idx][0] >= newInterval[0]:
                if newInts[idx][0] < newInterval[0]:
                    newInterval[0] = newInts[idx][0]
                if newInts[idx][1] > newInterval[1]:
                    newInterval[1] = newInts[idx][1]
                del newInts[idx]
            elif newInts[idx][1] <= newInterval[1] and newInts[idx][1] >= newInterval[0]:
                if newInts[idx][0] < newInterval[0]:
                    newInterval[0] = newInts[idx][0]
                if newInts[idx][1] > newInterval[1]:
                    newInterval[1] = newInts[idx][1]
                del newInts[idx]
            else:
                idx += 1
        newInts += [newInterval]
    return newInts

print(merge([[1,3],[8,10],[15,18], [4,8],[2,4]]))
print(merge([[1,4],[4,5]]))