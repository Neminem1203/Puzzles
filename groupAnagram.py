def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    words = {}
    for word in strs:
        key = "".join(sorted(list(word)))
        if key not in words:
            words[key] = []
        words[key].append(word)

    ret_list = []
    for key in words:
        ret_list.append(words[key])
    return ret_list