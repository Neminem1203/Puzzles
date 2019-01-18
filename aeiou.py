def aeiou(inputString):
    vowels = ['a','e','i','o','u']
    lst = [[0,0,""]]
    for i in inputString:
        print(lst)
        for j in lst:
            if vowels[j[1]] == i:
                j[0] += 1
                j[2] += i
                continue
            if j[1] < 4:
                if vowels[j[1]+1] == i:
                    lst.append([j[0], j[1]+1, j[2]])
                    continue

    largest = 0
    str = ""
    for i in lst:
        if i[0] > largest and i[1] == 4:
            largest = i[0]
            str = i[2]
    print(largest, str)

test = "aaagtaayuhiejjhgiiiouaae"
aeiou(test)