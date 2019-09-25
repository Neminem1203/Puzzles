import random


def rand7():
    def rand5():
        return random.randint(1, 5)
    sum = 0
    for i in range(7):
        sum += rand5()
    return (sum%7)+1


prob_array = [0 for i in range(7)]
len_of_test = 100000

for i in range(len_of_test):
    prob_array[rand7()-1] += 1

print(prob_array) # here's the results
for i in range(7):
    prob_array[i] = prob_array[i] / len_of_test
print(prob_array)  # probability in the end (should be around 0.1429)