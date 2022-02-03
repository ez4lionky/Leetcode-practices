class Solution:
    def evalRPN(self, tokens):
        stack = []
        opts = {'+': lambda x, y: x + y, '-': lambda x, y: y - x, '*': lambda x, y: x * y, '/': lambda x, y: int(y / x)}
        for t in tokens: stack.append(opts[t](stack.pop(), stack.pop())) if t in opts else stack.append(int(t))
        return stack[-1]


if __name__ == "__main__":
    # tokens = ["2","1","+","3","*"]
    # tokens = ["4","13","5","/","+"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    sol = Solution()
    print(sol.evalRPN(tokens))

