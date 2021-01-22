def canFormArray(arr, pieces):
    """
    :type arr: List[int]
    :type pieces: List[List[int]]
    :rtype: bool
    """
    for piece in pieces:
        ind = 0
        if piece[ind] in arr:
            arr_ind = arr.index(piece[ind])
        else:
            return False
        while ind < len(piece):
            if arr_ind >= len(arr):
                return False
            num = piece[ind]
            arr_num = arr[arr_ind]
            if num != arr_num:
                return False
            ind += 1
            arr_ind += 1
    return True


print(canFormArray([15,88],[[88],[15]])) # True
print(canFormArray([49,18,16], [[16,18,49]])) # False
print(canFormArray([91,4,64,78], [[78],[4,64],[91]])) # True