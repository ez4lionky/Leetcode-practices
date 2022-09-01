from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, word in enumerate(words):
            for j, w in enumerate(words):
                if (word in w) and j != i:
                    res.append(word)
                    break
        return res


if __name__ == "__main__":
    sol = Solution()
    words = ["leetcoder","leetcode","od","hamlet","am"]
    print(sol.stringMatching(words))

