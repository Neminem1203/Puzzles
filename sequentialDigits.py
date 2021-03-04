# https://leetcode.com/problems/sequential-digits/
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


# def sequentialDigits(low, high):
#     seq = [str(i) for i in range(1,10)]
#     ld = len(str(low))
#     hd = len(str(high))
#     start = int(str(low)[0])
#     print(seq)
#     print(seq[start-1:start-1+ld])
#     if int("".join(seq[start:start+ld])) < low:
#         start += 1
#
#     print(seq[start:start+ld])
#     print(ld)
#     print(hd)
#     print(start)


print(sequentialDigits(8511,23553))
print(sequentialDigits(28932835,733240848))