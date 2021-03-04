# https://leetcode.com/problems/sequential-digits/
# using sequence of numbers and indexing in
def sequentialDigits(low, high):
    if low > 123456789:
        return []
    seq = [str(i + 1) for i in range(9)]

    def numseq(ind, len):
        return int("".join(seq[ind: ind + len]))

    ld = len(str(low))
    hd = len(str(high))
    if hd > 9:
        hd = 9
    n = ld
    start = int(str(low)[0]) - 1
    print(numseq(start, n))
    if numseq(start, n) < low:
        start += 1
        if start + n > 9:
            start = 0
            n += 1
    print(numseq(start, n))
    return_list = []
    while n <= hd and numseq(start, n) <= high:
        return_list.append(numseq(start, n))
        start += 1
        if start + n > 9:
            start = 0
            n += 1
    return return_list

# finding the first lowest then adding the pattern number until we go above high
def sequentialDigits(low, high):
    if low > 123456789:
        return []
    stl = str(low)
    sth = str(high)
    lind = len(stl)
    hind = len(sth)
    start = ["0" for i in range(len(stl))]
    start[0] = stl[0]
    pattern = int("".join(["1" for _ in range(len(stl))]))
    next_step = False

    for i in range(1,len(start)):
        start[i] = chr(ord(start[i-1])+1)
    if ord("0") <= ord(start[-1]) <= ord("9"):
        start = int("".join(start))
        if start < low:
            start += pattern
    else:
        next_step = True
        lind += 1

    return_list = []
    for i in range(lind, hind+1):
        if next_step:
            start = int("".join([str(x+1) for x in range(i)]))
        pattern = int("".join(["1" for _ in range(i)]))
        while start <= high:
            if start < low or start % 10 == 0:
                next_step = True
                break
            return_list.append(start)
            start += pattern
            if start % 10 == 0:
                next_step = True
                break
    return return_list

print(sequentialDigits(100,300))
print(sequentialDigits(10,1000000000))
print(sequentialDigits(8511,23553))
print(sequentialDigits(28932835,733240848))