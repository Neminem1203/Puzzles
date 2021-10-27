# AlgoExpert Tandem Bicycle
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    rSS = redShirtSpeeds
    bSS = blueShirtSpeeds
    rSS.sort()
    bSS.sort()
    speed = 0
    if fastest:
        used = 0
        redL = 0
        redR = len(redShirtSpeeds)-1
        blueL = 0
        blueR = len(blueShirtSpeeds)-1
        while used < len(rSS):
            if rSS[redR] > bSS[blueR]:
                speed += rSS[redR]
                redR -= 1
                blueL += 1
            else:
                speed += bSS[blueR]
                blueR -= 1
                redL += 1
            used += 1
    else:
        for i in range(len(rSS)):
            if bSS[i] > rSS[i]:
                speed += bSS[i]
            else:
                speed += rSS[i]
    return speed



print(tandemBicycle([2,3,5,5,9],[1,2,3,6,7], True))
print(tandemBicycle([2,3,5,5,9],[1,2,3,6,7], False))