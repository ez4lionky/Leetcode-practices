from typing import List
from collections import defaultdict, Counter


class Solution:
    # def countKDifference(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     num_dict = defaultdict(list)
    #     for i, n in enumerate(nums):
    #         num_dict[n].append(i)
    #     for i, n in enumerate(nums):
    #         for key in [n+k, n-k]:
    #             if key not in num_dict:
    #                 continue
    #             for j in num_dict[key]:
    #                 if j > i:
    #                     res += 1
    #     return res
    
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        counter = Counter()
        for n in nums:
            res += counter[n-k] + counter[n+k]
            counter[n] += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,2,2,1]
    # k = 1
    # nums = [1,2,2,1]
    # k = 1
    nums = [1,3]
    k = 3
    print(sol.countKDifference(nums, k))

