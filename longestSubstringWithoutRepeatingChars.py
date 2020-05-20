# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = 0
    prev_chars = ""
    for char in s:
        find_char = prev_chars.find(char)
        if find_char != -1:
            prev_chars = prev_chars[find_char+1:]
        prev_chars += char
        if len(prev_chars) > longest:
            longest = len(prev_chars)
    return longest

print(lengthOfLongestSubstring("abcdbefghdijklmnopqrstuvwxyz"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))