'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def possibilities(str):
    lst = [int(i) for i in str]
    num = 1
    prev = 0
    combos = []
    for i in range(1,len(lst)):
        if(lst[i] != 0 and lst[i-1]*10 + lst[i] < 27):
            # print("Possibility: ", lst[i-1]*10 + lst[i])
            if prev > 0:
                num += prev
            else:
                num *= 2
            prev += 1
            continue
        combos.append(num)
        num = 1
        prev = 0
    combos.append(num)
    ret = 1
    for i in combos:
        ret *= i
    print(combos, ret)
    return ret

possibilities('111')
''' 1-1-1
1 1 1
11 1
1 11
'''
possibilities('12521')
''' 1-2-5 2-1
(125) 1 2 5, 1 25, 12 5 
(21) = 2 1, 21
'''
possibilities('2112')
''' 2-1-1-2
2 1 1 2
2 1 12
2 11 2
21 1 2
21 12
'''
possibilities('22222')
''' 2-2-2-2-2
2 2 2 2 2
2 2 2 22
2 22 2 2
2 22 22
2 2 22 2
22 2 2 2
22 2 22
22 22 2
'''
possibilities('22632112')
'''2-2-6 3 2-1-1-2
(226)
2 2 6
22 6
2 26
(2212)
2 1 1 2
2 1 12
21 1 2
21 12
2 11 2
'''