'''
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''
import math
operations = 0 # number of operations of getters and setters excluding the operations variable

def pow(base, exp):
    global operations
    returnVal = base # one operation
    repeat = math.floor(math.log(exp)/math.log(2)) # I don't know the number of operations from these formulas
    operations = 2
    iterations = 1
    for i in range(repeat):
        operations += 2
        returnVal *= returnVal
        iterations *= 2
    for i in range(exp-iterations):
        returnVal *= base
        iterations += 1
    return returnVal

print("2^10 = ", pow(2,10))
print("Operations: ", operations)
print("2^16 = ", pow(2,16))
print("Operations: ", operations)
print("5^32 = ",pow(5, 32))
print("Operations: ", operations)