# First Solution
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

# # second solution
# def longestPalindrome(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     return_val = s[0]
#     ind = 0
#     double_middle = False
#     while ind < len(s):
#         left = 1
#         right = 1
#         if double_middle:
#             right = 2
#         while True:
#             l = ind - left
#             r = ind + right
#             if l < 0 or r > len(s):
#                 break
#             ss = s[l:r + 1]
#             print(ss)
#             if ss == ss[::-1]:
#                 if len(ss) > len(return_val):
#                     return_val = ss
#             else:
#                 break
#             left += 1
#             right += 1
#         if double_middle:
#             double_middle = False
#         elif ind + 1 < len(s) and s[ind] == s[ind + 1]:
#             double_middle = True
#             continue
#         ind += 1
#
#     return return_val

print(longestPalindrome("cdbab"))
print(longestPalindrome("ac"))
print(longestPalindrome("babad"))
print(longestPalindrome("aacabdkacaa"))
print(longestPalindrome("bacabab"))
print(longestPalindrome("dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp"))

