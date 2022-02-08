class Solution:
    def sumOfUnique(self, nums) -> int:
        res = 0
        status = {}
        for n in nums:
            if n not in status:
                res += n
                status[n] = 1
            elif status[n] == 1:
                res -= n
                status[n] = 2
        return res


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,2,3,2]
    # nums = [1,1,1,1,1]
    nums = [1,2,3,4,5]
    print(sol.sumOfUnique(nums))

