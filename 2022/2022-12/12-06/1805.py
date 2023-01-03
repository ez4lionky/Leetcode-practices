import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = re.sub(r'[^0-9]', ' ', word)
        digits = set([int(d) for d in word.split()])
        return len(digits)


