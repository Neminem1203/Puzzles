import random

# # VERSION 1
# def rectanglesInCoordinates(coords):
#     numSquares = []
#     xHash = {}
#     for pt in coords:
#         if pt[0] not in xHash:
#             xHash[pt[0]] = []
#         xHash[pt[0]] += [pt[1]]
#     test = xHash.keys()
#     for key1, arr1 in xHash.items(): # first x-coordinate hash
#         for key2, arr2 in xHash.items(): # second x-coordinate hash
#             if key1 < key2: # we need different x-coordinate hash
#                 for idx1, val1 in enumerate(arr1): #
#                     if val1 in arr2:
#                         for val2 in arr1[idx1+1: len(arr1)]:
#                             if val2 in arr2:
#                                 numSquares.append([[key1, val1], [key1, val2], [key2, val1], [key2, val2]])
#     return numSquares

# # VERSION 2
def commonPermutations(arr1, arr2):
    inCommon = []
    for i in arr1:
        if i in arr2:
            inCommon.append(i)
    permutations = []
    for idx, i in enumerate(inCommon):
        for j in inCommon[idx+1:len(inCommon)]:
            permutations.append([i, j])
    return permutations
def rectanglesInCoordinates(coords):
    numSquares = []
    xHash = {}
    for pt in coords:
        if pt[0] not in xHash:
            xHash[pt[0]] = []
        xHash[pt[0]] += [pt[1]]
    test = xHash.keys()
    for key1, arr1 in xHash.items(): # first x-coordinate hash
        for key2, arr2 in xHash.items(): # second x-coordinate hash
            if key1 < key2: # we need different x-coordinate hash
                for i in commonPermutations(arr1, arr2):
                    numSquares.append([[key1, i[0]],[key1, i[1]], [key2, i[0]], [key2, i[1]]])
    return numSquares

test = rectanglesInCoordinates([[0,0], [1,1], [0,1],[2,0],[1,0], [2,1], [3,5]])
for i in test:
    print(i)

coordinates = []
for i in range(50):
    coordinates.append([random.randint(1,25), random.randint(1,25)])
print(coordinates)
for i in rectanglesInCoordinates(coordinates):
    print(i)
