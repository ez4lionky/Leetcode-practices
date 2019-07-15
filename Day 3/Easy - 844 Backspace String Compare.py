# Use two stack to compare the strings


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def push(self, a):
        self.items.append(a)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ss = Stack()
        ts = Stack()
        for i in S:
            if i != '#':
                ss.push(i)
            else:
                ss.pop()

        for i in T:
            if i != '#':
                ts.push(i)
            else:
                ts.pop()
        if ss.items == ts.items:
            return True
        else:
            return False


# Simplified version
class __Solution__(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


sol = Solution()
S = "ab#c"
T = "ad#c"
print(sol.backspaceCompare(S, T))
S = "ab##"
T = "c#d#"
print(sol.backspaceCompare(S, T))
S = "a##c"
T = "#a#c"
print(sol.backspaceCompare(S, T))
S = "a#c"
T = "b"
print(sol.backspaceCompare(S, T))
