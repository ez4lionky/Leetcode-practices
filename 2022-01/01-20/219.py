class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # O(n)
        # idxs = {}
        # for i, n in enumerate(nums):
        #     if n not in idxs.keys():
        #         idxs[n] = i
        #     else:
        #         if abs(idxs[n] - i) <= k:
        #             return True
        #         else:
        #             idxs[n] = i
        # return False

        # O(n) but TIME limited exceeded
        # for i in range(len(nums)):
        #     end = min(i+k+1, len(nums))
        #     if nums[i] in nums[i+1:end]:
        #         return True
            # for j in range(i + 1, end):
            #     if nums[i] == nums[j]:
            #         return True

        # still use slide window, but pass
        # because use 'in' method of set?
        s_w = set()
        for i, n in enumerate(nums):
            if i > k:
                s_w.remove(nums[i - k - 1])
            if n in s_w:
                return True
            s_w.add(n)
        return False
