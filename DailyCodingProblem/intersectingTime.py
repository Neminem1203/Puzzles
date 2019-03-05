'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

timeIntervals = [[30,75], [0,50], [60,150], [10,15], [44, 66]]

def intersectingTime(tIArr):
    rooms = 0
    while(tIArr):
        # print(tIArr)
        tI = tIArr.pop(0)
        ind = 0
        rooms += 1
        while(ind < len(tIArr)):
            if( (tIArr[ind][0] < tI[0] and tIArr[ind][1] > tI[0]) or
                (tIArr[ind][0] < tI[1] and tIArr[ind][1] > tI[1]) or
                (tIArr[ind][0] > tI[0] and tIArr[ind][0] < tI[1]) ):
                ind += 1
            else:
                tIArr.pop(ind)
    return rooms

print(intersectingTime(timeIntervals))


