class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # according to the definition of subsequences
        return 1 if s==s[::-1] else 2
        # if s == s[::-1]:
        #     return 1
        # return 2
