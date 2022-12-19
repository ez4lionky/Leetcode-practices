# class Solution:
#     vowels = 'aeiouAEIOU'
#     def num_vowels(self, s):
#         num = 0
#         for c in s:
#             if c in self.vowels:
#                 num += 1
#         return num
#
#     def halvesAreAlike(self, s: str) -> bool:
#         l = len(s)
#         return self.num_vowels(s[:l//2]) == self.num_vowels(s[l//2:])


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = "aeiouAEIOU"
        mid = len(s) // 2
        return sum(c in VOWELS for c in s[:mid]) == sum(c in VOWELS for c in s[mid:])
