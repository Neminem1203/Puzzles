# https://code.google.com/codejam/contest/5304486/dashboard

n = int(input())
inputs = [[] for i in range(n)]
for i in range(n):
    inputs[i] = input().split(" ")
    pass

def flip(pancake):
    newcake = ""
    for cake in pancake:
        if(cake == "-"):
            newcake += "+"
        else:
            newcake += "-"
    return newcake

testcase = 0
for i in inputs:
    flipper = int(i[1])
    flips = 0
    possible = True
    testcase += 1
    for j in range(len(i[0])-flipper+1):
        if(i[0][j] == "-"):
            flips += 1
            i[0] = i[0][:j] + flip(i[0][j:j+flipper]) + i[0][j+flipper:]
    for j in range(len(i[0])-flipper+1, len(i[0])):
        if(i[0][j] == "-"):
            possible = False
    if(possible):
        print("Case #"+str(testcase)+": "+str(flips))
    else:
        print("Case #"+str(testcase)+": IMPOSSIBLE")

# Test Input:
# 3
# ---+-++- 3
# +++++ 4
# -+-+- 4
#
# Test Output:
# Test Case 1: 3
# Test Case 2: 0
# Test Case 3: IMPOSSIBLE