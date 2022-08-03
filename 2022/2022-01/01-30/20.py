class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            else:
                if len(stack) == 0 or pairs[s[i]] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    # s = "()[]{}"
    s = "(]"
    sol = Solution()
    print(sol.isValid(s))

