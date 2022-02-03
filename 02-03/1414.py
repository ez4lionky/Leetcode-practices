class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ans = 0
        while k > 0:
            a, b = 1, 1
            c = a + b
            while a + b <= k:
                c = a + b
                a = b
                b = c
            k = k - c
            ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    # print(sol.findMinFibonacciNumbers(10))
    print(sol.findMinFibonacciNumbers(7))

