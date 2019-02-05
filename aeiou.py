def aeiou(inputString):
    vowels = ['a','e','i','o','u']
    lst = [[0,0,""]]
    for i in inputString:
        # print(lst)
        for j in lst:
            if vowels[j[1]] == i:
                j[0] += 1
                j[2] += i
                continue
            if j[1] < 4:
                if vowels[j[1]+1] == i and j[0] > 0:
                    lst.append([j[0], j[1]+1, j[2]])
                    continue

    largest = 0
    str = ""
    for i in lst:
        if i[1] == 4:
            print(i[0], "\t", i[2])
            if i[0] > largest:
                largest = i[0]
                str = i[2]
    print("Len: ", largest,"\tString: ", str)

test = "aaiiaeeiouaauaeeaaeeuaeooaaeeaaeeiuuiieeiiooaaeiuoouuu"
aeiou(test)

