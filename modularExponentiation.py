'''
Given three numbers x, y and p, compute (x**y) % p.
'''

def modExp(x,y,p):
    num = 1
    for i in range(y):
        num = num * x
        while(num > p):
            num -= p
    return num


print(modExp(2,3,5))
print(modExp(2,5,13))