# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
def maximumSum(a, m):
    def find(sumSoFar, array):
        highest = sumSoFar%m
        for ind, num in enumerate(array):
            if (num+sumSoFar)%m == m-1:
                return m-1
            findResult = find(num+sumSoFar, array[:ind]+array[ind+1:])
            if findResult%m > highest:
                highest = findResult%m
        return highest
    newArr = []
    for i in a:
        result = i%m
        if result == m-1:
            return m-1
        if result != 0:
            newArr += [i%m]
    return find(0, newArr)

print(maximumSum([1, 9], 7)) # answer should be 3. 1 + 9 = 10 % 7 = 3
print(maximumSum([3, 8], 7)) # answer should be 4. 3 + 8 = 11 % 7 = 4
print(maximumSum([203, 336, 126, 2373, 3333, 555], 7))  # answer should be 3. 3333 + 555 = 3888 % 7 = 3 the other numbers
                                                        # are duplicates of 7