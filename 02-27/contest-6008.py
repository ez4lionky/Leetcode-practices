from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l = len(pref)
        res = 0
        for s in words:
            if s[:l] == pref:
                res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    words = ["pay","attention","practice","attend"]
    pref = "at"
    print(sol.prefixCount(words, pref))

