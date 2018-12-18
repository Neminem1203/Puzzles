import sys


# automatic random number generator version

import random
upperbound = 1000000000
tests = 10
guesses = 30
for i in range(tests):
    random_num = random.randint(0, upperbound) + 1
    low = 0
    high = upperbound
    tries = 0
    for j in range(guesses):
        tries += 1
        # print([low, high])
        average = int((high + low) / 2)
        if(random_num > average):
            low = average
        elif(random_num < average):
            high = average
        else:
            low = average
            high = average
            break
    print("Actual: ", random_num, "\tGuess: ", low, "\tTries: ", tries,end='\t')
    if random_num == low:
        print("Correct")
    else:
        print("Wrong")

# # testing_tool version
#
# tests = int(input())
#
# for i in range(tests):
#     lowerbound, upperbound = input().split(' ')
#     guesses = int(input())
#     low = int(lowerbound)
#     high = int(upperbound)
#     for i in range(guesses):
#         guess = int((high + low) / 2)
#         print(guess, flush=True)
#         sys.stdout.flush()
#         s = str(input())
#         if(s == "TOO_SMALL"):
#             low = guess
#         elif(s == "TOO_BIG"):
#             high = guess
#         else:
#             break