import random

def answer(heights):
    heightdone = [[] for i in range(len(heights))]
    water = 0
    end = len(heights)
    ind = 1  # middle
    # can't have water at the ends so we start at 1 and end at len(heights) - 1
    while (ind < end - 1):

        if heights[ind] in heightdone[ind]:
            ind += 1
            continue
        # print("Checking Index: ", ind)
        lower = ind
        left = ind  # used to check left highest
        right = ind  # used to check right highest
        for i in range(ind, -1, -1):
            if (heights[i] > heights[ind]):
                # print("Found Left: ", i)
                left = i
                break
        for i in range(ind, end):
            if (heights[i] > heights[ind]):
                # print("Found Right: ", i)
                right = i
                break

        if (left != ind and right != ind):
            if (heights[left] <= heights[right]):
                lower = left
            else:
                lower = right
            # print("Adding Water at index ", ind, ": ",((right - left) - 1) * (heights[lower] - heights[ind]))
            water += ((right - left) - 1) * (heights[lower] - heights[ind])
            for i in range(left+1, right):
                heightdone[i].append(heights[ind])
            # print(heightdone)


        ind += 1
        # print("")
    return water


# Testing the Program
visual = True       #Visual representation
n = 10              # Number of Elements
num = 10            # Number of Tests
high = 10           # highest number value
test = [0 for i in range(n)]
for i in range(num):
    for j in range(n):
        test[j] = random.randint(1,high)
    print(test)
    print("Answer: ", answer(test))
    maxnum = 0
    if visual == True:
        for i in range(max(test)):
            maxnum = max(test)
            printed = False
            for j in range(n):
                if(maxnum in test):
                    if(test[j] == maxnum):
                        print('X',end='')
                        test[j] -= 1
                        printed = True
                    else:
                        if printed == True:
                            print('O',end='')
                        else:
                            print('.',end='')
                else:
                    print('.',end='')
            print('')
    print('')