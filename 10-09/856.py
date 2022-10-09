class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score, depth = 0, 0
        for i, c in enumerate(s):
            depth += 1 if c is '(' else -1
            if c == ')' and s[i-1] == '(':
                score += 1 << depth
        return score 

