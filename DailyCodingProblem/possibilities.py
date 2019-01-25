'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def possibilities(str):
    lst = [int(i) for i in str]
    print("Original: ", lst)
    fib = 1
    prev = 1
    combos = []
    for i in range(1,len(lst)):
        if(lst[i] == 0):
            fib = fib-prev
            if(prev > 1):
                combos.append(prev)
            fib = 1
            prev = 1
            continue

        if(lst[i-1]*10 + lst[i] < 27 and lst[i-1]*10 + lst[i] > 10):
            fib += prev
            prev = fib-prev
            continue

        if(fib > 1):
            combos.append(fib)
        fib = 1
        prev = 1
    if(fib > 1):
        combos.append(fib)
    ret = 1
    for i in combos:
        ret *= i
    print("Result: ", ret)
    return ret

possibilities('111')
''' 1-1-1
1 1 1
11 1
1 11
'''
possibilities('2112')
''' 2-1-1-2
2 1 1 2
2 1 12
2 11 2
21 1 2
21 12
'''
possibilities('12521')
''' 1-2-5 2-1
(125) 1 2 5, 1 25, 12 5 
(21) = 2 1, 21
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
possibilities('1101121023')
'''1 10 1-1 20 2-3
'''