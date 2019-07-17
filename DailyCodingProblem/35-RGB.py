'''Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''

def RGB(array):
    ind = 0
    for i in range(len(array)):
        if(array[i] == 'R'):
            array[i] = array[ind]
            array[ind] = 'R'
            ind += 1
    for i in range(ind, len(array)):
        if (array[i] == 'G'):
            array[i] = array[ind]
            array[ind] = 'G'
            ind += 1
    return array

print(RGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']))