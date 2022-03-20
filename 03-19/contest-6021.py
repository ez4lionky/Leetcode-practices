class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        if pattern[0] == pattern[1]:
            c = text.count(pattern[0]) 
            return int(c * (c + 1) / 2)
        m, n = 0, 0
        res = 0
        for c in text:
            if c == pattern[0]: m+=1
            if c == pattern[1]: n+=1; res += m
        return res + max(m, n)


if __name__ == "__main__":
    sol = Solution()
    text = "iekbksdsmuuzwxbpmcngsfkjvpzuknqguzvzik"
    pattern = "mp"
    print(sol.maximumSubsequenceCount(text, pattern))

