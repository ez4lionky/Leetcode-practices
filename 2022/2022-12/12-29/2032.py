from collections import Counter


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = Counter(set(nums1)) + Counter(set(nums2)) + Counter(set(nums3))
        res = []
        for k, v in counter.items():
            if v >= 2:
                res.append(k)
        return res


# class Solution:
#     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         mask = defaultdict(int)
#         for i, nums in enumerate((nums1, nums2, nums3)):
#             for x in nums:
#                 mask[x] |= 1 << i
#         return [x for x, m in mask.items() if m & (m - 1)]


