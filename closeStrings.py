def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    """
    wordlen = len(word1)
    if wordlen != len(word2):
        return False
    count1 = {}
    count2 = {}
    ind = 0
    while ind < wordlen:
        char1, char2 = word1[ind], word2[ind]
        if char1 not in count1:
            count1[char1] = 0
        count1[char1] += 1
        if char2 not in count2:
            count2[char2] = 0
        count2[char2] += 1
        ind += 1
    countlist1 = []
    countlist2 = []
    charlist1 = []
    charlist2 = []
    for char in count1:
        countlist1 += [count1[char]]
        charlist1 += char
    for char in count2:
        countlist2 += [count2[char]]
        charlist2 += char
    countlist1.sort()
    countlist2.sort()
    charlist1.sort()
    charlist2.sort()
    return countlist1 == countlist2 and charlist1 == charlist2

