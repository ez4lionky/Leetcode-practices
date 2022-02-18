class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start, end = 0, x // 2
        while start < end:
            mid = (start + end + 1) // 2
            if mid**2 > x:
                end = mid - 1
            else:
                start = mid
        return start


if __name__ == "__main__":
    sol = Solution()
    x = 6
    print(sol.mySqrt(x))
