class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 1000
        s = 0
        for n in nums:
            s += n
            if s < min_val:
                min_val = s
        res = max(1 - min_val, 1)
        return res


if __name__ == "__main__":
    pass

