
def restoreArray(adjacentPairs):
    """
    :type adjacentPairs: List[List[int]]
    :rtype: List[int]
    """
    adjacent = {}  # nums adjacent to key
    for pairs in adjacentPairs:
        n1, n2 = pairs
        # num 1
        if n1 not in adjacent:
            adjacent[n1] = [n2]
        else:
            adjacent[n1].append(n2)
        # num 2
        if n2 not in adjacent:
            adjacent[n2] = [n1]
        else:
            adjacent[n2].append(n1)
    # find the beginning with one of the nodes
    beginning = None
    for num in adjacent:
        if len(adjacent[num]) == 1:
            beginning = num
            break
    # set up first 2 nodes
    ret_arr = []
    ret_arr.append(beginning)
    ret_arr.append(adjacent[beginning][0])
    # the length of the final array
    n = len(adjacentPairs) + 1
    while len(ret_arr) < n:
        n1, n2 = adjacent[ret_arr[-1]]
        if n1 == ret_arr[-2]:
            ret_arr.append(n2)
        else:
            ret_arr.append(n1)
    return ret_arr

print(restoreArray([[2,1],[3,4],[3,2]]))