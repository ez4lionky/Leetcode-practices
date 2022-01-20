def lengthOfLongestSubstring(s: str) -> int:
    maxl, i, j = 0, 0, 0
    subs = ''
    n = len(s)
    while i < n and j < n:
        if s[j] not in subs:
            subs = subs + s[j]
            j += 1
            maxl = max(maxl, len(subs))
        else:
            i += 1
            subs = subs[1:]

    return maxl


print(lengthOfLongestSubstring('bbtablud'))
print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('aab'))
print(lengthOfLongestSubstring(' '))
print(lengthOfLongestSubstring('dvdf'))
