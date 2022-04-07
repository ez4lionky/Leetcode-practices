class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) == len(goal) and (s+s).count(goal):
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    s = "abcde"
    goal = "cdeab"
    print(sol.rotateString(s, goal))


