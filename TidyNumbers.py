import math
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1
# doesn't work with 111111111111111110 because of some error in the 100's place
n = int(input("Number: "))

start = math.floor((math.log(n)/math.log(10)))
prevnum = 0
newnum = 0
fixspot = 0
for i in range(start, -1, -1):
    if prevnum == 10: #this is the case for the rest of the numbers being 0
        newnum += 9 * (10**i)
        continue
    fixspot = i
    mod = math.floor(n/10**i)
    if(mod == 0 or mod < prevnum): #if 0 or bad digit, rest of the numbers are 9
        prevnum = 10
        newnum += 9 * (10**i)
        newnum -= 1 * (10**(i+1))
    else: # good digit
        prevnum = mod
        newnum += mod*(10**i)
    n -= mod*(10**i)


for i in range(fixspot, start+1):
    mod1 = math.floor((newnum / (10 ** i)) % 10)
    mod2 = math.floor((newnum / (10 ** (i+1))) % 10)
    # print(mod1, mod2)
    if(mod1 < mod2):
        newnum += (9-mod1)*(10**i)
        newnum -= (10**(i+1))

print(newnum)

