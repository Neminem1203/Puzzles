"""
When it rains it pours
======================
It's raining, it's pouring. You and your agents are nearing the building where the captive rabbits are being held, but a
sudden storm puts your escape plans at risk. The structural integrity of the rabbit hutches you've built to house the
fugitive rabbits is at risk because they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's
lab, you must compute how much standing water has accumulated on the rabbit hutches.
Specifically, suppose there is a line of hutches, stacked to various heights and water is poured from the top (and
allowed to run off the sides). We'll assume all the hutches are square, have side length 1, and for the purposes of this
problem we'll pretend that the hutch arrangement is two-dimensional.
For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] (the hutches are shown below):
...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123
When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:
...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123
The amount of water that has accumulated is the number of Os, which, in this instance, is 5.
Write a function called answer(heights) which, given the heights of the stacked hutches from left-to-right as
a list,computes the total area of standing water accumulated when water is poured from the top and allowed to run off
the sides.
The heights array will have at least 1 element and at most 9000 elements. Each element will have a value of at least 1,
and at most 100000.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int list) heights = [1, 4, 2, 5, 1, 2, 3]
Output:
    (int) 5
Inputs:
    (int list) heights = [1, 2, 3, 2, 1]
Output:
    (int) 0
"""
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
maxnum = 0
# waterrep = 0
for i in range(num):
    for j in range(n):
        test[j] = random.randint(1,high)
    print(test)
    print("Answer: ", answer(test))

    if visual == True:
        # waterrep = 0
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
                            # waterrep += 1
                        else:
                            print('.',end='')
                else:
                    print('.',end='')
            print('')
        # print("Visual Rep Answer: ",waterrep)
    print('')