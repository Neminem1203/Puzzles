def checksum(line):
    line = line.strip()
    array = line.split('\t')
    n = len(array)
    for i in range(n):
        num = int(array[i])
        for j in range(0, n):
            num2 = int(array[j])
            if(i != j and num % num2 == 0):
                return int(num / num2)


f = open("input.txt", "r")
contents = f.readlines()

sum = 0
for num in contents:
    sum += checksum(num)
print(sum)