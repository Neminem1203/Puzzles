# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/

beginNum = input("Input Number: ")

indexOfSwap = -1
nonZeroMinIndex = 0
increasing = beginNum[len(beginNum)-1]
for i, value in enumerate(reversed(beginNum)):
    if(increasing > value):
        indexOfSwap = len(beginNum) - (i + 1)
        break
    else:
        if(nonZeroMinIndex == 0 and (value != '0')):
            nonZeroMinIndex = len(beginNum) - (i + 1)
        increasing = value


if indexOfSwap != -1:
    newNum = ""
    for i, value in enumerate(beginNum):
        if(i < indexOfSwap):
            newNum += value
        else:
            newNum += beginNum[nonZeroMinIndex]
            for ind in range(len(beginNum)-1, i, -1):
                if(beginNum[ind] > value):
                    newNum += value
                    value = ""
                if(ind != nonZeroMinIndex):
                    newNum += beginNum[ind]
            break
    print(newNum)
else:
    print("Can't go higher")
