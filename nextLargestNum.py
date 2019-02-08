# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/


def nextLargest(beginNum):
    indexOfSwap = -1
    increasing = beginNum[len(beginNum)-1]
    for i in range(len(beginNum)-1, -1, -1):
        if(increasing > beginNum[i]):
            indexOfSwap = i
            break
        else:
            increasing = beginNum[i]

    if indexOfSwap != -1:
        for i in range(len(beginNum)-1, indexOfSwap, -1):
            if beginNum[indexOfSwap] < beginNum[i]:
                temp = beginNum[indexOfSwap]
                beginNum = beginNum[:indexOfSwap] + beginNum[i] + beginNum[indexOfSwap+1:]
                beginNum = beginNum[:i] + temp + beginNum[i+1:]
                break
        beginNum = beginNum[:indexOfSwap+1] + "".join(reversed(beginNum[indexOfSwap+1:]))
        return(beginNum)
    else:
        return(beginNum)

beginNum = input("Input Number: ").strip()
print(nextLargest(beginNum))