from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {"2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits) == 0:
            return []
        return [''.join(s) for s in product(*(m[d] for d in digits))]


if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))

