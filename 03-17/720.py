from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        res = ""
        s_words = sorted([(-len(w), w) for w in words], reverse=True)
        s = [""]
        for w in s_words:
            w = w[1]
            if w[:-1] in s:
                s.append(w)
                res = w
        return res


if __name__ == "__main__":
    sol = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(sol.longestWord(words))

