def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) <= 1:
        return s
    letters = {}

    for ind in range(len(s)):
        char = s[ind]
        if char not in letters:
            letters[char] = []
        letters[char] += [ind]
    return_val = s[0]
    for char in letters:
        for ind1 in range(len(letters[char])):
            first_index = letters[char][ind1]
            for ind2 in range(ind1+1, len(letters[char])):
                second_index = letters[char][ind2]
                substring = s[first_index:second_index + 1]
                if len(substring) < len(return_val):
                    print("substring ", substring, " skipped.")
                    continue

                if substring == substring[::-1]:
                    return_val = substring
    return return_val

print(longestPalindrome("cdbab"))
print(longestPalindrome("ac"))
print(longestPalindrome("dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp"))

