from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for p in "!?',;.":
            paragraph = paragraph.replace(p, ' ')
        paragraph = paragraph.lower().split()
        c = Counter(paragraph)
        for b in banned:
            if b in c:
                c[b] = 0
        return c.most_common()[0][0]


if __name__ == "__main__":
    sol = Solution()
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ['a']
    print(sol.mostCommonWord(paragraph, banned))

