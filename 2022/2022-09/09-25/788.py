class Solution:
    def rotatedDigits(self, n: int) -> int:
        nums1 = ['2', '5', '6', '9']
        nums2 = ['3', '4', '7']
        res = 0
        for i in range(n+1):
            if any(str(i).__contains__(n) for n in nums1) and not any(str(i).__contains__(n) for n in nums2):
                res += 1
        return res

