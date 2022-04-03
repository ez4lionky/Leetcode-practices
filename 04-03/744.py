from typing import List
import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        if idx == len(letters):
            return letters[0]
        return letters[idx]


if __name__ == "__main__":
    sol = Solution()
    letters = ["c","f","j"]
    # target = "a"
    target = "j"
    print(sol.nextGreatestLetter(letters, target))

