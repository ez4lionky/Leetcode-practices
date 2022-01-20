# The primary method is sorting the sequence directly, then take the k-th largest element.
# Here is the implementation of a less time complexity method,
# which using the K size heap to store the K largest elements.
import heapq

class Solution:
    def __init__(self):
        self.H = []

    def findKthLargest(self, nums: [int], k: int) -> int:
        heapq.heapify(self.H)
        for i, n in enumerate(nums):
            if i < k:
                heapq.heappush(self.H, n)
            else:
                if self.H[0] < n:
                    heapq.heapreplace(self.H, n)
        return self.H[0]


sol = Solution()
# nums = [3, 2, 1, 5, 6, 4]
# k = 2
# print(sol.findKthLargest(nums, k))

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(sol.findKthLargest(nums, k))
