from collections import Counter


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter1, counter2 = Counter(s), Counter(target)
        min_num = 999
        for k in counter2:
            counter1[k] //= counter2[k]
        for c in target:
            if counter1[c] < min_num:
                min_num = counter1[c]
        return min_num

