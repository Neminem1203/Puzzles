#https://www.reddit.com/r/dailyprogrammer/comments/8sjcl0/20180620_challenge_364_intermediate_the_ducci/
from copy import deepcopy

ntuple = tuple(input("").strip("()").split(','))
ntuple = [int(i) for i in ntuple]
newtuple = deepcopy(ntuple)
while(not all(v == 0 for v in ntuple)):
    for j in range(len(ntuple)):
        newtuple[j] = abs(ntuple[(j+1)%len(ntuple)] - ntuple[j])
    ntuple = deepcopy(newtuple)
    print(ntuple)