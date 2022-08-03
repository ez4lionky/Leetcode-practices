from typing import List


class Solution:
    def nextGreaterElement(self, nums1, nums2: List[int]):
        stack = []
        counts = {}
        for i in range(len(nums2)):
            if len(stack) == 0 or nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    idx = stack.pop()
                    counts[nums2[idx]] = nums2[i]
                stack.append(i)
        res = [counts[n] if n in counts else -1 for n in nums1]
        return res

if __name__ == "__main__":
    sol = Solution()
    # nums1 = [4,1,2]
    # nums2 = [1,3,4,2]
    # nums1 = [2,4]
    # nums2 = [1,2,3,4]
    nums1 = [1,3,5,2,4]
    nums2 = [5,4,3,2,1]
    print(sol.nextGreaterElement(nums1, nums2))

