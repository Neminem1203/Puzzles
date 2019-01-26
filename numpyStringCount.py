# https://www.geeksforgeeks.org/numpy-string-operations-count-function/

def npCount(strLst, SS, start=0, end=-1):
    endDefined = True if end > -1 else False
    count = [0]*len(strLst)
    for num, str in enumerate(strLst):
        ind = 0
        if not endDefined:
            end = len(str) - len(SS) + 1
        for charInd in range(start, end):
            for SSInd in range(len(SS)):
                if(SS[SSInd] != str[SSInd+charInd]):
                    break
                if SSInd == len(SS)-1:
                    count[num] += 1
            ind += 1
    return count


# input arrays
in_arr = ['Sayantan' , '  Sayan  ', 'Sayansubhra']
print("Input array : ", in_arr)

# output arrays
out_arr = npCount(in_arr, 'an')
print("Output array: ", out_arr)
out_arr = npCount(in_arr, 'a', 1, 8)
print("Output array: ", out_arr)