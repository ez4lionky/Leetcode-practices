class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h, h = 0, 0
        for g in gain:
            h += g
            if h > max_h:
                max_h = h
        return max_h

