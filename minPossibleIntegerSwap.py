# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
'''
4321
[1,3],[2,2],[3,1],[4,0]
'''
class customArray:
    def __init__(self, old_arr=[]):
        self.arr = []
        for ind, i in enumerate(old_arr):
            self.insert(i, ind)

    def insert(self, val, ind):
        i = 0
        inserted = False
        while i < len(self.arr):
            info = self.arr[i]
            if info[0] > val:
                inserted = True
                self.arr.insert(i, [val, ind])
                break
            i += 1
        if not inserted:
            self.arr.append([val,ind])




def minInteger(num, k):
    ca = customArray(list(map(lambda x: int(x), num)))
    ind_used = {}
    new_start = 0
    remaining = k
    num_arr = []
    ranges = [0 for _ in range(len(num))]
    print(ca.arr)
    for val, ind in ca.arr:
        new_ind = ind + ranges[ind]
        print("PTR:",new_start,"\t\tVal:",val,"\t\tNew Ind:",new_ind,"\t\tRemaining:",remaining,"\n\n", ranges,"\n")
        if new_ind == new_start:
            ind_used[ind] = True
            num_arr.append(str(val))
            new_start += 1
        else:
            if remaining >= new_ind-new_start:
                ind_used[ind] = True
                num_arr.append(str(val))
                for i in range(new_ind+1):
                    ranges[i] += 1
                remaining -= (new_ind-new_start)
                new_start += 1
        if remaining <= 0:
            break
    for i in range(len(num)):
        if i not in ind_used:
            num_arr.append(num[i])
    return "".join(num_arr)

# print(minInteger("4321", 4))
# print(minInteger("100", 1))
# print(minInteger("36789", 1000))
# print(minInteger("22", 22))
# print(minInteger("9438957234785635408", 23))
# print(minInteger("9000900",3))
print(minInteger("294984148179", 11))
'''
9438957234785635408 23
0943895723478563548 6
0394895723478563548 4
03


"294984148179"
11
"124498948179"


294984148179 11
129498448179 5
124998448179 4
124499848179 1
'''