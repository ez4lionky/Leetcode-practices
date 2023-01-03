class Solution:
    def secondHighest(self, s: str) -> int:
        first, second = -1, -1
        for c in s:
            if c.isnumeric():
                c = int(c)
                if c > first:
                    second = first
                    first = c
                elif c!= first and c > second:
                    second = c
        return second

