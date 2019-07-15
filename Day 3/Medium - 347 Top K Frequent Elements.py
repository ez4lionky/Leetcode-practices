import heapq
import collections

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        count = collections.Counter(nums)
        MinHeap = []
        for i, j in enumerate(count.items()):
            num, cnt = j
            if i < k:
                heapq.heappush(MinHeap, (cnt, num))
            else:
                if cnt > MinHeap[0][0]:
                    heapq.heappop(MinHeap)
                    heapq.heappush(MinHeap, (cnt, num))

        rev = [heapq.heappop(MinHeap) for _ in range(len(MinHeap))]
        topK = [_[1] for _ in rev[::-1]]
        return topK


sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(sol.topKFrequent(nums, k))

# Summary:
# About time complexity:
# https://blog.csdn.net/iteye_12150/article/details/82475159
# Introduction to Algorithms - Chapter 6
# This solution is O(n) + O(nlog(k) + klog(k)) -> O(nlog(k))
# Could use heapq's build-in method nlargest()
