class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s, j = [], 0
        for n in pushed:
            s.append(n)
            while s and s[-1] == popped[j]:
                s.pop()
                j += 1
        return len(s) == 0

