def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    pattern_dict = {}
    for char in pattern:
        if char not in pattern_dict:
            pattern_dict[char] = ''
    match_list = []
    for word in words:
        patt_dict = pattern_dict.copy()
        word_dict = {}
        matching = True
        for char_ind in range(len(word)):
            pattern_char = pattern[char_ind]
            char = word[char_ind]
            found_pattern = patt_dict[pattern_char]
            if char not in word_dict:
                word_dict[char] = pattern_char
            elif word_dict[char] != pattern_char:
                matching = False
                break
            elif found_pattern != '' and found_pattern != char:
                matching = False
                break
            patt_dict[pattern_char] = char
        if matching:
            match_list.append(word)
    return match_list
