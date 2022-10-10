class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff1, diff2 = [], []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff1.append(s1[i])
                diff2.append(s2[i])
        if len(diff1) > 2 or len(diff1) == 1:
            return False
        if set(diff1) == set(diff2):
            return True
        return False

