class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> [str]:
        self.generate("", n, n)
        return self.result

    def generate(self, item, left, right):
        if left == 0 and right == 0:
            self.result.append(item)
            return
        if left > 0:
            self.generate(item + '(', left - 1, right)
        if left < right:
            self.generate(item + ')', left, right - 1)


n = 3
sol = Solution()
print(sol.generateParenthesis(3))
