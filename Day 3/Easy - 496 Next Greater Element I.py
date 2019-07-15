class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        dic = {}
        stack = []
        for n in nums2:
            while len(stack) > 0 and stack[-1] < n:
                dic[stack[-1]] = n
                stack.pop()
            stack.append(n)

        greEles = []
        for n in nums1:
            if n in dic.keys():
                greEles.append(dic[n])
            else:
                greEles.append(-1)
        return greEles


sol = Solution()
# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# print(sol.nextGreaterElement(nums1, nums2))
# nums1 = [2, 4]
# nums2 = [1, 2, 3, 4]
# print(sol.nextGreaterElement(nums1, nums2))
nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]
print(sol.nextGreaterElement(nums1, nums2))
