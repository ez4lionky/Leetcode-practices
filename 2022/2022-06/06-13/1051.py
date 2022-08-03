class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m = max(heights)
        cnt = [0] * (m + 1)
        for h in heights:
            cnt[h] += 1

        idx, res = 0, 0
        for i in range(1, m+1):
            for j in range(cnt[i]):
                if heights[idx] != i:
                    res += 1
                idx += 1
        return res

