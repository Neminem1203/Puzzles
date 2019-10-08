# inspired by computerphille
# visual representation of tower of hanoi
tower= [[],[],[]]

def towerPrint():
    global tower
    highest = 0
    for stacks in tower:
        if highest < len(stacks):
            highest = len(stacks)
    ind0, ind1, ind2 = 0, 0, 0
    for height in range(highest-1, -1, -1):
        if height < len(tower[0]):
            print(tower[0][ind0],end="\t")
            ind0 += 1
        else:
            print(" ", end="\t")

        if height < len(tower[1]):
            print(tower[1][ind1],end="\t")
            ind1 += 1
        else:
            print(" ", end="\t")

        if height < len(tower[2]):
            print(tower[2][ind2],end="\t")
            ind2 += 1
        else:
            print(" ", end="\t")
        print()
    print("_________\n\n")


def towerOfHanoi(height):
    def algo(stacks, fromStack, midStack, toStack):
        global tower
        if(stacks == 0):
            pass
        else:
            algo(stacks-1, fromStack, toStack, midStack)
            tower[toStack] = [tower[fromStack].pop(0)] + tower[toStack]
            towerPrint()
            algo(stacks-1, midStack, fromStack, toStack)
        return
    tower[0] = [i for i in range(height)]
    towerPrint()
    algo(height, 0, 1, 2)

towerOfHanoi(5)