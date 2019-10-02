
def checksum(line):
    line = line.strip()
    array = line.split('\t')
    min = int(array[0])
    max = int(array[0])
    n = len(array)
    for i in range(1, n):
        num = int(array[i])
        if(num > max):
            max = num
        if(num < min):
            min = num
    return max - min

f = open("input.txt", "r")
contents = f.readlines()

sum = 0
for num in contents:
    sum += checksum(num)
print(sum)