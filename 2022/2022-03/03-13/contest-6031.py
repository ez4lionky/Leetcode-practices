from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idxs = [i for i, n in enumerate(nums) if n == key]
        res = []
        for i in idxs:
            res.extend(list(range(max(0, i-k), min(i+k, len(nums)-1)+1 )))
        res = sorted(set(res))
        return res

if __name__ == "__main__":
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1
    sol = Solution()
    print(sol.findKDistantIndices(nums, key, k))
